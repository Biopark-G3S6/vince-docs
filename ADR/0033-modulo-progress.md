# ADR-0033 — Módulo `progress`: acompanhamento, sinais e relatórios

- **Status:** Aceito
- **Data:** 2026-11-05
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0014, ADR-0018, ADR-0020, ADR-0021, ADR-0025

## Contexto

`RF-ACP-001` a `RF-ACP-006` reúnem leituras agregadas, sinais automáticos e relatórios por curso. Os
dados fonte pertencem aos módulos de artigo, curso, equipe e evento, e não podem ser consultados por
junções entre schemas.

## Decisão

1. DEVE existir o módulo de negócio `progress`, proprietário de sinais de risco ativos/históricos e
   relatórios consolidados gerados.
2. O schema PostgreSQL DEVE chamar-se `progress` e possuir exclusivamente `risk_signal`, `progress_report`,
   `processed_event` e `progress_outbox`.
3. Painéis DEVEM consultar DTOs em lote por `ArticleFacade`, `CourseFacade` e, quando disponível, pelas
   fachadas de equipe e evento; acesso direto aos schemas é proibido. Dados pessoais de integrantes
   devem ser obtidos pela fachada de `access` somente quando necessários.
4. Sinais DEVEM ser recalculados por job periódico no papel `worker`, persistidos com chave estável por
   equipe/condição e desativados quando a condição cessar. Ativação produz `RiskSignalActivated` no
   outbox para notificação. Nenhum sinal pode ser mostrado à equipe ou alterar o ciclo de correção.
5. O relatório DEVE ser snapshot dos dados registrados, por curso/período, sem conteúdo do artigo,
   apontamento ou discussão. O módulo deve responder às seis perguntas de `RF-ACP-005`; dados de notas e
   publicações são consultados por DTOs do módulo proprietário, nunca por tabela externa.
6. Exportação inicial é CSV UTF-8 gerado a partir do mesmo DTO/snapshot apresentado na consulta.
   Identificadores de destinatários e de curso permanecem opacos e o caso de uso verifica titularidade.
7. `ProgressFacade` é a única superfície pública; consultas ao banco usam buscas em lote com quantidade
   de consultas independente do número de equipes retornadas.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Painéis dentro do módulo `article` | Relatório e risco cruzam capacidades e não pertencem à escrita do artigo. |
| Leitura SQL direta de outros schemas | Viola ADR-0006 e impediria extração independente. |
| Sinal mostrado aos integrantes | `RF-ACP-003 RN4` reserva o sinal ao orientador e à coordenação. |
| Nota sugerida por regra automática | `RF-ACP-004 RN1` e `RE-17` vedam recomendação e cálculo de nota. |

## Implicações

1. O módulo depende de contratos de consulta em lote ainda a completar nas fachadas de origem.
2. A criação do relatório exige que avaliações individuais, notas de artigo e publicações externas estejam
   disponíveis na fachada proprietária quando esses requisitos forem aplicados.

## Estado de implementação

Ainda não há módulo `event` neste checkout. Os painéis agrupam por `eventId`, mas não mostram título nem
cronograma; o relatório usa a data de criação do artigo como aproximação de período e registra
`periodBasis: ARTICLE_CREATED_AT` no snapshot. Os sinais chamam a fachada de notificação diretamente; o
outbox e relay de evento ainda não foram ligados.
