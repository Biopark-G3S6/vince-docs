# ADR-0019 — Transações e gestão de conexões

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0005, ADR-0008, ADR-0010, ADR-0018

## Contexto

Uma instância única de PostgreSQL atende processos replicados por papel, cada um com seu próprio
pool. O número total de conexões é recurso global e finito, e cada conexão do PostgreSQL é um
processo do sistema operacional com custo de memória.

## Decisão

### Transações

1. O escopo de uma transação DEVE ser um único caso de uso de um único módulo.
2. Uma transação NÃO DEVE abranger chamada à fachada de outro módulo.
3. Uma transação NÃO DEVE abranger chamada de rede a serviço externo.
4. Uma transação NÃO DEVE permanecer aberta durante processamento de longa duração.
5. Toda transação DEVE declarar tempo limite.
6. O nível de isolamento padrão DEVE ser `READ COMMITTED`; nível superior DEVE ser declarado explicitamente pelo caso de uso que o exigir.
7. A gravação do evento em outbox DEVE ocorrer na mesma transação do fato que o originou.
8. Operação que exija consistência entre módulos NÃO DEVE ser resolvida por transação distribuída; DEVE ser resolvida por evento e compensação.

### Conexões

9. O tamanho do pool de conexões por processo DEVE ser declarado explicitamente.
10. O produto entre o número de réplicas e o tamanho do pool DEVE caber em orçamento de conexões declarado, inferior ao limite do servidor.
11. O orçamento DEVE reservar conexões para migrações, manutenção e diagnóstico.
12. Os processos de papel `api` e de papel `worker` DEVEM ter orçamentos declarados separadamente.
13. A necessidade de ultrapassar o orçamento DEVE ser resolvida pela adoção de pooler externo em modo transação, e não pela elevação do limite do servidor.
14. Adotado pooler em modo transação, a configuração do cliente DEVE desabilitar prepared statements.
15. Conexão NÃO DEVE ser mantida aberta entre requisições fora do pool.
16. Consulta de longa duração NÃO DEVE ser executada sob o papel `api`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Transação distribuída entre módulos | Reintroduz acoplamento temporal e de disponibilidade entre módulos, anulando o isolamento estabelecido em ADR-0005. |
| Elevar o limite de conexões do servidor | Cada conexão é um processo do sistema operacional; elevar o limite adia o problema e degrada o servidor sob carga. |
| Pool único compartilhado por todos os papéis | Impede dimensionar `api` e `worker` de forma independente, contrariando ADR-0008 §11. |
| Pooler em modo sessão | Não reduz o número de conexões efetivas ao servidor; não resolve o problema que motiva sua adoção. |
| Transação aberta durante chamada externa | Mantém conexão retida pelo tempo de resposta de terceiro, exaurindo o pool sob indisponibilidade alheia. |

## Implicações

1. O orçamento de conexões torna-se restrição de capacidade: aumentar réplicas exige revisar o tamanho do pool, não apenas a contagem de processos.
2. A proibição de transação distribuída implica que fluxos entre módulos são eventualmente consistentes e exigem compensação explícita.
3. O tempo limite de transação converte contenção em erro observável, em vez de espera indefinida.
4. A adoção futura de pooler em modo transação altera a configuração do cliente Prisma e precisa ser prevista antes de ser necessária.
