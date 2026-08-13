# ADR-0008 — Escalabilidade por papel de processo

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0001, ADR-0003

## Contexto

O requisito de escalar módulos individualmente não implica, necessariamente, extraí-los para serviços
independentes. É possível escalar por papel de processo mantendo artefato e repositório únicos.

## Decisão

1. O artefato de build DEVE ser único e comum a todos os papéis de execução.
2. O papel do processo DEVE ser determinado pela variável de ambiente `ROLE`.
3. Os valores admitidos para `ROLE` DEVEM ser `api`, `worker` e `relay`.
4. Com `ROLE=api`, o processo DEVE registrar os controllers HTTP e NÃO DEVE registrar processadores de fila.
5. Com `ROLE=worker`, o processo DEVE registrar os processadores de fila dos módulos indicados e NÃO DEVE expor rotas HTTP, exceto o endpoint de verificação de saúde.
6. Os módulos ativos em um processo DEVEM ser determinados pela variável de ambiente `MODULES`.
7. `MODULES` ausente ou vazio DEVE ser interpretado como todos os módulos.
8. A separação por papel DEVE existir desde o primeiro commit, ainda que os papéis sejam executados em conjunto em ambiente de desenvolvimento.
9. Nenhum módulo DEVE depender de estado mantido em memória entre requisições ou entre execuções; todo processo DEVE ser stateless.
10. Nenhum módulo DEVE presumir a execução no mesmo processo que outro módulo.
11. Diante de gargalo de desempenho, o ajuste de réplicas por papel e por módulo DEVE ser a resposta anterior a qualquer proposta de extração de serviço.
12. Processamento intensivo de CPU ou de longa duração NÃO DEVE ser executado sob `ROLE=api`.
13. Com `ROLE=relay`, o processo DEVE publicar os eventos registrados no outbox dos módulos indicados e NÃO DEVE expor rotas HTTP, exceto o endpoint de verificação de saúde. Diferentemente dos demais papéis, `relay` NÃO DEVE ser replicado horizontalmente para um mesmo módulo, conforme ADR-0021 §7.
14. A verificação de saúde DEVE distinguir vivacidade de prontidão. A verificação de vivacidade NÃO DEVE consultar dependência externa, sob pena de a reinicialização do processo ser disparada por falha alheia a ele. A verificação de prontidão PODE consultar dependências, com tolerância declarada, e NÃO DEVE reprovar por indisponibilidade transitória — do contrário, uma oscilação de segundos retira todas as réplicas de rotação simultaneamente.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Escalar apenas o processo único | Réplicas dimensionadas pelo módulo mais custoso; desperdício de recurso. |
| Extrair o módulo custoso para serviço | Custo operacional e de rede sem evidência prévia de que a separação de papéis é insuficiente. |
| Artefatos de build distintos por papel | Multiplica pipeline e superfície de divergência entre imagens. |

## Implicações

1. O bootstrap da aplicação passa a ser condicional ao papel e DEVE ser coberto por teste.
2. A observabilidade DEVE identificar papel e módulos ativos em cada processo.
3. O ganho de isolamento é de recurso computacional, não de falha: todos os papéis compartilham o mesmo código e as mesmas dependências.
