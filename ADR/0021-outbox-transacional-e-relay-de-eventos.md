# ADR-0021 — Outbox transacional e relay de eventos

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0005, ADR-0008, ADR-0012, ADR-0018, ADR-0019, ADR-0020

## Contexto

O fato e o evento residem em sistemas distintos — PostgreSQL e Redis — sem transação comum. Publicar
dentro da transação expõe evento de fato que pode não ser confirmado; publicar após o commit perde o
evento se o processo falhar no intervalo. O ADR-0019 §7 já determinou a gravação em outbox, restando
definir sua estrutura, sua entrega e o destino das linhas publicadas.

## Decisão

### Outbox

1. Cada módulo DEVE possuir tabela de outbox em seu próprio schema.
2. O evento DEVE ser gravado no outbox na mesma transação do fato que o originou.
3. O evento NÃO DEVE ser publicado no Redis dentro da transação.
4. A linha de outbox DEVE conter identificador do evento, tipo, versão do contrato, payload, instante de criação, instante de publicação, identificador de correlação e contagem de tentativas.
5. O identificador do evento DEVE ser UUID versão 7 gerado no momento da criação.

### Relay

6. A publicação DEVE ser executada por processo de papel dedicado `relay`, distinto de `api` e de `worker`.
7. O papel `relay` DEVE executar em instância única por módulo, garantida por trava distribuída.
8. O relay DEVE ler o outbox em ordem de criação e publicar preservando essa ordem dentro de cada módulo.
9. O relay DEVE marcar a linha como publicada somente após a confirmação da publicação.
10. Falha entre a publicação e a marcação DEVE resultar em republicação; a entrega é, portanto, pelo menos uma vez.
11. Todo consumidor DEVE ser idempotente.
12. A indisponibilidade do relay NÃO DEVE impedir a gravação de novos eventos no outbox.
13. O atraso entre a gravação e a publicação DEVE ser observável e sujeito a alerta.

### Entrega a múltiplos consumidores

14. O relay DEVE publicar o evento em uma fila por módulo consumidor, nomeada conforme ADR-0020 §5.
15. As inscrições dos módulos consumidores em cada tipo de evento DEVEM ser declaradas em registro explícito.
16. A falha de entrega a um consumidor NÃO DEVE impedir a entrega aos demais.
17. Cada fila de consumidor DEVE possuir retentativa e dead-letter queue próprias, conforme ADR-0012.
18. O módulo publicador NÃO DEVE conhecer os módulos consumidores de seus eventos.

### Retenção

19. A linha publicada DEVE ser marcada como tal, e não removida no ato da publicação.
20. Linhas publicadas DEVEM ser expurgadas por rotina periódica decorridos 7 dias da publicação.
21. A rotina de expurgo NÃO DEVE remover linha ainda não publicada.
22. O crescimento sustentado de linhas não publicadas DEVE ser tratado como incidente.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Publicação direta no Redis dentro da transação | Publica evento de fato que pode não ser confirmado, e faz a transação depender de chamada de rede, contrariando ADR-0019 §3. |
| Publicação após o commit, sem outbox | Falha do processo entre o commit e a publicação perde o evento definitivamente, sem rastro. |
| Relay embutido no papel `worker` | Dispensa papel novo, mas faz réplicas competirem pelas mesmas linhas e elimina a garantia de ordem de publicação por módulo. |
| Captura de alterações do log de replicação | Menor latência e sem carga de consulta, ao custo de introduzir componente externo de infraestrutura desproporcional ao estágio do projeto. |
| Remoção imediata da linha publicada | Mantém a tabela pequena, mas elimina o rastro necessário para investigar entrega duvidosa. |
| Retenção permanente das linhas | Crescimento ilimitado de tabela situada em caminho crítico de escrita, com degradação progressiva de inserção e de índice. |
| Barramento em processo, sem fila | Perde retentativa, isolamento de falha e dead-letter queue, e deixa de funcionar assim que um módulo for extraído. |
| Publicação em fila única compartilhada pelos consumidores | Faz a falha de um consumidor bloquear os demais e contraria a propriedade de fila por módulo (RNF-MOD-009). |

## Implicações

1. A entrega pelo menos uma vez transforma a idempotência do consumidor em condição de correção, não em boa prática.
2. O papel `relay` é ponto único por módulo: sua parada acumula eventos sem perdê-los, mas suspende toda a integração assíncrona daquele módulo.
3. O registro de inscrições torna-se artefato arquitetural: acrescentar consumidor a um evento passa a ser alteração de configuração, sujeita a revisão.
4. O mesmo evento é duplicado no Redis por consumidor inscrito, com custo de memória proporcional ao número de inscrições.
5. O ADR-0008 passa a admitir três papéis de execução.
6. A trava distribuída do §7 reside no Redis, o que soma mais uma dependência crítica àquele componente.
