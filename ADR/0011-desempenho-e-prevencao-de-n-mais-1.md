# ADR-0011 — Metas de desempenho e prevenção de N+1

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0008, ADR-0010

## Contexto

O sistema não possuía metas quantitativas de desempenho, o que impede verificar objetivamente os
requisitos de eficiência. A consulta em cascata (N+1) é o defeito de desempenho mais recorrente em
aplicações com ORM e não se manifesta em teste unitário nem em revisão de código.

## Decisão

1. As metas de tempo de resposta DEVEM ser:

   | Classe de operação | p95 | p99 |
   | :--- | :--- | :--- |
   | Leitura — consulta por identificador, listagem paginada | 300 ms | 800 ms |
   | Escrita transacional | 500 ms | 1500 ms |

2. As metas DEVEM ser medidas no servidor, excluída a latência de rede do cliente.
3. As métricas de experiência do frontend DEVEM observar, no percentil 75: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.
4. A disponibilidade mensal DEVE ser de, no mínimo, 99,5%.
5. Operação que não atenda à meta e não admita otimização DEVE ser convertida em processamento assíncrono.
6. Toda listagem DEVE ser paginada; NÃO DEVE existir endpoint de listagem sem limite de resultados.
7. O limite máximo DEVE ser de 100 itens por página; requisição acima do limite DEVE ser truncada ao limite.
8. Toda chamada a dependência externa DEVE declarar timeout explícito.
9. O número de consultas ao banco por requisição DEVE ser constante em relação à quantidade de registros retornados.
10. DEVE existir teste automatizado de invariância de contagem: o mesmo endpoint executado com um registro e com dez registros DEVE emitir a mesma quantidade de consultas.
11. Divergência no teste de invariância DEVE reprovar o build.
12. A contagem de consultas por requisição DEVE ser instrumentada por extensão do cliente Prisma.
13. Iteração que execute consulta ao banco por elemento NÃO DEVE ser aceita em revisão de código.
14. Consulta com duração superior a 200 ms DEVE ser registrada em log em ambiente de desenvolvimento.
15. `pg_stat_statements` DEVE estar habilitado em ambiente produtivo.
16. Toda coluna utilizada como filtro ou ordenação de consulta recorrente DEVE possuir índice.
17. A carga de referência sob a qual as metas são aferidas DEVE ser definida em ADR próprio, e as metas revalidadas contra ela.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Orçamento absoluto de consultas por endpoint | Quebra a cada alteração legítima; alto custo de manutenção e baixo sinal. |
| Detecção de N+1 apenas por revisão de código | Não determinística; o defeito só se manifesta sob volume. |
| Ausência de metas quantitativas | Torna os requisitos de desempenho não verificáveis. |
| Metas por endpoint individual | Inviável de manter à medida que a superfície da API cresce. |

## Implicações

1. O teste de invariância exige infraestrutura de teste com banco real e massa de dados controlada.
2. O limite de paginação passa a ser contrato da API e sua alteração é quebra de compatibilidade.
3. A meta de disponibilidade de 99,5% admite indisponibilidade mensal de aproximadamente 3,6 horas e não exige redundância geográfica.
