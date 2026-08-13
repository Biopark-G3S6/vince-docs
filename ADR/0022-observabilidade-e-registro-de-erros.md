# ADR-0022 — Observabilidade e registro de erros

- **Status:** Aceito
- **Data:** 2026-08-12
- **Relacionados:** ADR-0003, ADR-0008, ADR-0009, ADR-0017, ADR-0020

## Contexto

Os requisitos de observabilidade pressupõem mecanismo até aqui indefinido. A orientação de
stakeholder é registrar as exceções em tabela consultável, alimentada por fila, sem bloquear a
requisição de origem.

## Decisão

### Log estruturado

1. Todo processo DEVE emitir log estruturado, em formato legível por máquina, na saída padrão.
2. A saída padrão DEVE ser o canal primário e síncrono de registro, e NÃO DEVE depender de banco de dados, fila ou serviço externo.
3. Todo registro DEVE conter instante, nível, identificador de correlação, papel do processo e módulo de origem.
4. Os campos que compõem o contexto de um registro DEVEM ser definidos por lista de permissão declarada em ponto único; campo não declarado NÃO DEVE ser registrado.
5. NÃO DEVE ser usada lista de bloqueio de campos sensíveis como mecanismo de proteção.
6. A retenção do log em ambiente produtivo depende de coletor, cuja adoção fica diferida.

### Correlação

7. Toda requisição DEVE receber identificador de correlação na borda.
8. Identificador recebido do cliente PODE ser reaproveitado, e DEVE ser descartado se não obedecer ao formato declarado.
9. O identificador DEVE ser propagado aos casos de uso, às consultas, às mensagens publicadas e aos consumidores.
10. A resposta ao cliente DEVE conter o identificador de correlação.

### Classificação e tratamento de falhas

11. DEVE existir um único tratador global de exceções, residente em `shared/`.
12. As falhas DEVEM ser classificadas em esperadas e inesperadas.
13. Falha esperada — validação, violação de regra de negócio, recurso inexistente, autorização negada — DEVE produzir resposta conforme ADR-0017 §14.
14. Falha inesperada DEVE produzir resposta genérica.
15. A resposta ao cliente NÃO DEVE conter mensagem de exceção, rastro de pilha ou identificação de componente interno.

### Registro de erros

16. Falhas esperadas e inesperadas DEVEM ser registradas na mesma estrutura, distinguidas por coluna de classificação.
17. A publicação DEVE ser feita pelo tratador global, em fila dedicada; nenhum módulo de negócio DEVE publicar nessa fila.
18. A persistência DEVE ser realizada por consumidor próprio, fora do ciclo da requisição.
19. Falha na publicação ou na persistência do erro NÃO DEVE propagar-se à requisição de origem.
20. O registro DEVE ser agregado por assinatura.
21. A assinatura DEVE ser derivada do tipo da exceção, do primeiro quadro da pilha pertencente ao código do projeto e da mensagem normalizada.
22. A normalização DEVE substituir identificadores, números e endereços de correio eletrônico por marcadores antes do cálculo da assinatura.
23. A assinatura NÃO DEVE incorporar número de linha.
24. Cada assinatura DEVE manter contagem de ocorrências, instante da primeira e da última ocorrência e sua classificação.
25. NÃO DEVE ser persistida uma linha por ocorrência.
26. Falha inesperada DEVE reter as ocorrências mais recentes com contexto, em quantidade limitada e declarada.
27. Falha esperada NÃO DEVE reter contexto de ocorrência.
28. As linhas de assinatura DEVEM ser retidas indefinidamente.
29. As amostras de contexto DEVEM ser expurgadas decorridos 30 dias de seu registro.
30. A fila e a tabela de erros DEVEM pertencer ao módulo de plataforma de observabilidade.

### Métricas e saúde

31. Cada processo DEVE expor endpoint de métricas em formato Prometheus.
32. O endpoint de métricas DEVE escutar em porta distinta da porta da API e NÃO DEVE ser publicado externamente.
33. DEVEM ser expostas, no mínimo: latência por rota, profundidade das filas, atraso de publicação do outbox, ingresso em dead-letter queue e conexões de banco em uso.
34. A adoção de servidor de coleta de métricas fica diferida.
35. O surgimento de nova assinatura de erro e o crescimento acelerado de assinatura existente DEVEM ser sujeitos a alerta.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Persistência em tabela como canal único | Torna invisível justamente a falha de banco ou de fila — o momento em que o registro mais importa. |
| Gravação síncrona do erro dentro da requisição | Acopla o caminho de resposta à disponibilidade do banco e amplifica a carga durante o incidente. |
| Uma linha persistida por ocorrência | Tempestade de exceções idênticas satura o banco no pior momento possível. |
| Descarte das falhas esperadas | Elimina a análise de tendência: um pico de autorização negada ou de erro de validação deixa de ser visível. |
| Retenção de contexto para falhas esperadas | Armazenaria aos milhares dados submetidos por usuários, contrariando RNF-SEG-022, sem ganho de diagnóstico. |
| Lista de bloqueio para redação de campos sensíveis | Falha para o lado inseguro: todo campo novo é registrado até que alguém se lembre de bloqueá-lo. |
| Assinatura derivada da mensagem sem normalização | Produz assinatura distinta por identificador presente na mensagem, anulando a agregação. |
| Assinatura incluindo número de linha | Refatoração desloca linhas e zera os contadores; erro antigo reaparece como novo a cada release. |
| Plataforma externa de observabilidade | Recursos superiores, ao custo de dependência e de custo recorrente não previstos no estágio. Reversível: como o canal primário é a saída padrão, a substituição não afeta módulo algum. |
| Exposição do rastro de pilha ao cliente | Revela estrutura interna e caminhos de arquivo, facilitando o reconhecimento do sistema. |
| Endpoint de métricas na porta da API | Expõe topologia, volume de requisições e número de réplicas na superfície pública. |

## Implicações

1. O log em saída padrão exige coletor no ambiente produtivo; sem ele, o histórico se perde a cada reinicialização do processo.
2. A agregação por assinatura descarta o detalhe das ocorrências individuais além das amostras retidas.
3. A tabela de erros é índice de investigação, não registro integral: o log em saída padrão permanece a fonte completa.
4. A lista de permissão obriga a declarar explicitamente cada campo novo de contexto, sob pena de perder informação útil de diagnóstico. É o custo deliberado de falhar para o lado seguro.
5. O módulo de observabilidade é o primeiro módulo de plataforma do sistema, na acepção de ADR-0003 §1.
6. A publicação em fila e a persistência dependem de Redis e PostgreSQL, o que reforça a concentração de responsabilidades já registrada em ADR-0020.
