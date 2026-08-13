# ADR-0020 — Transporte de mensagens e isolamento de filas

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0005, ADR-0006, ADR-0012, ADR-0013, ADR-0021

## Contexto

O ADR-0005 §13 deixou em aberto o mecanismo de transporte dos eventos. Uma instância única de Redis
é compartilhada por todos os módulos, sem que nada no servidor impeça um módulo de operar a fila de
outro, contrariando a propriedade exigida por ADR-0006 §1.

## Decisão

### Transporte

1. O enfileiramento e o processamento assíncrono DEVEM usar BullMQ sobre a instância única de Redis.
2. NÃO DEVE ser adotado broker de mensageria adicional.
3. Os mecanismos nativos de publicação e assinatura do Redis NÃO DEVEM ser usados para entrega de evento entre módulos.
4. A conexão com o Redis DEVE ser compartilhada por processo, observando os limites de conexão da instância.

### Nomenclatura e isolamento

5. Toda fila DEVE ser nomeada no formato `<modulo>:<fila>`.
6. Toda chave criada no Redis por um módulo DEVE ser prefixada pelo nome do módulo.
7. Um módulo NÃO DEVE publicar em fila nem consumir fila cujo prefixo não seja o seu.
8. O registro das filas e dos processadores de um módulo DEVE ocorrer exclusivamente em seu composition root.
9. A conformidade com §5 a §7 DEVE ser verificada por análise estática na integração contínua.

### Eventos e jobs

10. As mensagens DEVEM ser classificadas em eventos e jobs.
11. Evento DEVE representar fato consumado, ser nomeado no passado e transitar pelo outbox.
12. Job DEVE representar tarefa a executar, ser nomeado no imperativo e é interno ao módulo que o enfileira.
13. Um módulo NÃO DEVE enfileirar job em fila de outro módulo.
14. Job PODE ser enfileirado diretamente, sem outbox, quando sua perda em caso de falha for aceitável; caso contrário DEVE transitar pelo outbox.

### Conteúdo da mensagem

15. O payload DEVE conter apenas dados serializáveis, o identificador de correlação e o identificador do ator de origem.
16. O payload NÃO DEVE conter entidade de domínio, tipo gerado pelo ORM nem dado pessoal além do estritamente necessário ao processamento.
17. O consumidor NÃO DEVE executar com a autoridade do usuário que originou a mensagem; o identificador do ator destina-se exclusivamente a auditoria.
18. O payload DEVE declarar a versão do contrato da mensagem.
19. Alteração incompatível no contrato de uma mensagem DEVE observar ADR-0004 §11.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| RabbitMQ, NATS ou Kafka | Roteamento e retenção superiores, ao custo de componente de infraestrutura adicional não previsto em RES-005 e sem necessidade comprovada no estágio. |
| Publicação e assinatura nativas do Redis | Entrega sem persistência: mensagem publicada sem consumidor conectado é perdida, sem retentativa nem dead-letter queue. |
| Redis Streams | Oferece histórico e grupos de consumo, porém fora da cobertura do BullMQ: exigiria implementar retentativa, backoff e dead-letter queue manualmente, duplicando o mecanismo de ADR-0012. |
| Fila compartilhada entre módulos | Torna RNF-MOD-009 inverificável e acopla módulos pelo formato da mensagem. |
| Listas de controle de acesso do Redis por módulo | Daria isolamento pelo próprio servidor, mas exige uma conexão por módulo, incompatível com o orçamento de conexões de ADR-0019 §10. |
| Consumidor executando com a autoridade do usuário de origem | Faria um trabalho já autorizado falhar por mudança posterior de papel, no meio de um fluxo iniciado. |

## Implicações

1. A ausência de distribuição nativa para múltiplos consumidores obriga uma fila por consumidor, definida em ADR-0021 §14.
2. O isolamento de filas depende de convenção e de análise estática, não de imposição do servidor Redis.
3. O Redis passa a sustentar simultaneamente as sessões (ADR-0013 §4) e a mensageria: sua indisponibilidade nega autenticação e interrompe todo o processamento assíncrono. É ponto único de falha compartilhado por duas capacidades independentes.
