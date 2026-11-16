# ADR-0031 — Módulo `notification`: caixa e entrega de notificações

- **Status:** Aceito
- **Data:** 2026-11-05
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0012, ADR-0014, ADR-0018, ADR-0020, ADR-0021, ADR-0026

## Contexto

`RF-DSC-005` e `RF-DSC-006` exigem caixa pessoal persistente e entrega por mais de um canal, alimentada
por fatos produzidos por módulos distintos. A caixa deve sobreviver à falha de e-mail e ao reprocessamento
de eventos.

## Decisão

1. DEVE existir o módulo de negócio `notification`, proprietário da caixa, estado de leitura,
   preferências de e-mail e retentativas de entrega.
2. O schema PostgreSQL DEVE chamar-se `notification` e possuir exclusivamente `notification`,
   `notification_email_preference`, `email_delivery` e `notification_outbox`.
3. Toda notificação DEVE pertencer a um destinatário e guardar tipo, IDs opacos do objeto relacionado,
   instante e instante de leitura. Chave única por evento e destinatário DEVE impedir duplicidade em
   entrega pelo menos uma vez.
4. Os eventos `ArticleSubmitted`, `ArticleReturned`, `RemarkChanged`, `RemarkDecided`,
   `ArticleConcluded`, `MessagePublished` e `RiskSignalActivated` DEVEM chegar por filas próprias do
   módulo `notification`. O consumidor DEVE persistir a caixa antes de tentar e-mail.
5. E-mail desativado por preferência NÃO DEVE desativar a caixa. Falha de provedor DEVE manter a
   notificação e registrar tentativa retentável, sem reverter o fato de origem.
6. O e-mail DEVE usar a preferência de idioma do destinatário consultada por `AccessFacade`, com fallback
   `pt-BR`, e não pode incluir conteúdo de artigo, mensagem ou apontamento.
7. `NotificationFacade` DEVE permitir aos módulos publicadores solicitar entrega de fato e aos
   consumidores consultar/alterar somente notificações do ator autenticado. Nenhum consumidor pode ler
   diretamente tabelas de outro módulo.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Caixa no módulo `discussion` | Artigo, prazo e risco também originam notificações; a caixa não pertence à discussão. |
| Enviar e-mail antes de gravar a caixa | Falha de e-mail perderia a notificação na interface, contrariando `RF-DSC-005 E1`. |
| Chave estrangeira para o objeto notificado | Objetos pertencem a módulos distintos; ADR-0006 e ADR-0018 vedam FK entre schemas. |

## Implicações

1. O módulo exige schema, fila de consumidor, idempotência, retentativa e trilha/outbox próprios.
2. Um adaptador de e-mail configurável é necessário; sem serviço configurado, a caixa continua operante e
   as tentativas permanecem retentáveis.

## Estado de implementação

A caixa e o worker de e-mail estão implementados, incluindo preferências, isolamento por destinatário,
retentativa e assunto/texto em `pt-BR`. O módulo `discussion` publica mensagens por outbox e chama a
fachada de forma idempotente no papel `worker`. Artigo e risco ainda chamam `NotificationFacade` após a
operação, sem outbox transacional. O relay BullMQ e o uso da `notification_outbox` permanecem pendentes
em OpenSpec.
