# ADR-0012 — Política de retentativa e dead-letter queue

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0005, ADR-0006

## Contexto

O processamento assíncrono definido em ADR-0005 exige política explícita de falha. Retentativa
indiscriminada multiplica carga sobre dependências já degradadas; ausência de destino final para
mensagens irrecuperáveis produz perda silenciosa de trabalho.

## Decisão

1. Toda fila DEVE declarar explicitamente seu número máximo de tentativas e sua política de backoff.
2. O padrão DEVE ser de 5 tentativas — uma inicial e quatro retentativas.
3. O backoff DEVE ser exponencial, com atraso inicial de 5 s, fator 2 e teto de 5 min.
4. O backoff DEVE aplicar jitter.
5. As falhas DEVEM ser classificadas em transitórias e permanentes.
6. Falha permanente — payload inválido, violação de regra de negócio, referência inexistente, erro de contrato — NÃO DEVE ser retentada e DEVE ser encaminhada imediatamente à dead-letter queue.
7. Cada fila DEVE possuir uma dead-letter queue correspondente, de propriedade do mesmo módulo.
8. Mensagem encaminhada à dead-letter queue DEVE reter o payload original, o número de tentativas, o erro de cada tentativa, os instantes de execução e o identificador de correlação.
9. NÃO DEVE existir consumidor automático de dead-letter queue.
10. O reprocessamento a partir da dead-letter queue DEVE ser ação explícita, sujeita a permissão e registrada em auditoria.
11. O reprocessamento DEVE reingressar a mensagem na fila de origem, preservando seu identificador original.
12. Mensagens em dead-letter queue DEVEM ser retidas por no mínimo 30 dias.
13. O ingresso de mensagem em dead-letter queue DEVE emitir sinal observável de alerta.
14. Crescimento sustentado de uma dead-letter queue DEVE ser tratado como incidente.
15. O esgotamento de tentativas NÃO DEVE resultar em descarte da mensagem.
16. O processamento DEVE ser idempotente, uma vez que a retentativa PODE ocorrer após aplicação de efeito parcial.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Descarte após esgotamento de tentativas | Perda silenciosa de trabalho, sem rastro para diagnóstico ou recuperação. |
| Retentativa indefinida | Mensagem irrecuperável bloqueia a fila e consome recurso indefinidamente. |
| Backoff fixo, sem jitter | Mensagens que falham em conjunto retentam em conjunto, repetindo a sobrecarga sobre a dependência degradada. |
| Consumidor automático da dead-letter queue | Reintroduz a falha em laço; a fila deixa de ser destino final. |
| Retentativa uniforme, sem classificação de falha | Falha permanente consome as tentativas integralmente, atrasando as mensagens seguintes sem chance de sucesso. |

## Implicações

1. A classificação entre falha transitória e permanente passa a ser responsabilidade explícita de cada consumidor.
2. A dead-letter queue exige interface de inspeção e reprocessamento, com permissão associada.
3. O alerta de ingresso em dead-letter queue pressupõe mecanismo de observabilidade definido.
