# ADR-0030 — Módulo `discussion`: conversa contínua da equipe

- **Status:** Aceito
- **Data:** 2026-11-05
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0014, ADR-0018, ADR-0021, ADR-0025

## Contexto

`RF-DSC-001` a `RF-DSC-004` definem mensagens contínuas ligadas ao artigo, com escopo de equipe e
atualização em tempo real. Artigo, equipe e apontamento pertencem a outros dados; o novo módulo precisa
preservar esses limites e permitir retomada após interrupção.

## Decisão

1. DEVE existir o módulo de negócio `discussion`, proprietário de discussões e mensagens públicas
   entre integrantes da equipe e o orientador responsável.
2. O schema PostgreSQL DEVE chamar-se `discussion` e possuir exclusivamente `discussion_message` e
   `discussion_outbox`. A mensagem DEVE guardar identificadores opacos de artigo, equipe, autor e,
   quando aplicável, apontamento; a referência local entre mensagem raiz e resposta DEVE usar chave
   estrangeira.
3. Uma discussão DEVE ser única por artigo e contínua entre etapas. Respostas DEVEM apontar à raiz e
   não podem formar terceiro nível. Referência a apontamento DEVE ser navegável nos dois sentidos por
   identificador.
4. Titularidade DEVE ser validada por consulta a `ArticleFacade` e conferência de `memberIds` ou do
   orientador responsável; coordenador e outros orientadores NÃO DEVEM participar.
5. Exclusão DEVE ser lógica e preservar o registro de exclusão. Mensagem excluída continua como raiz
   identificável para suas respostas, sem expor o conteúdo como mensagem ativa.
6. A transmissão ao vivo DEVE usar SSE com cursor estável por mensagem. A ordenação total DEVE usar
   `(createdAt, id)`. O servidor DEVE armazenar mensagens antes da publicação; reconexão com cursor
   DEVE consultar o histórico persistido e eliminar lacunas e duplicidade. Publicação efêmera entre
   instâncias PODE usar canal Redis prefixado `discussion:`; esse canal NÃO substitui o outbox nem o
   histórico.
7. Mensagem criada DEVE gravar evento `MessagePublished` no mesmo commit da mensagem. O evento DEVE
   conter apenas IDs, instante, correlação e versão do contrato; consumidores DEVEM ser idempotentes.
8. `DiscussionFacade` e seus DTOs opacos DEVEM ser a única superfície pública do módulo. O módulo pode
   depender de `ArticleFacade` e `AccessFacade`, sem ciclo de dependência.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Discussão dentro do schema de `article` | A conversa tem ciclo de escrita e atualização próprios; misturá-la amplia a fronteira de consistência do artigo. |
| Redis Pub/Sub como histórico de mensagens | Não retém eventos durante desconexão e não permite retomada confiável. |
| WebSocket bidirecional | A troca é servidor-cliente; SSE permite retomada nativa por ID e publicação permanece em HTTP. |
| Mensagem privada | `RF-DSC-001 RN4` declara que toda mensagem é visível aos participantes nesta versão. |

## Implicações

1. O módulo exige schema, migração, fachada, controller, outbox e relay próprios.
2. O uso de SSE requer manter autenticação por cookie e reconexão sem exigir token anti-CSRF em leitura.

## Estado de implementação

O controller usa SSE consultando o banco em intervalos de um segundo, com cursor por `Last-Event-ID` e
ordenação por `(createdAt, id)`. A mensagem e o outbox são gravados na mesma transação. O worker do
módulo reproduz o outbox com retentativa exponencial e envia a notificação pela `NotificationFacade`;
a chave do evento torna a entrega idempotente. Este relay usa polling no papel `worker`, sem BullMQ. Os
outros fatos que geram notificações ainda são enviados diretamente após as operações de artigo e risco,
sem outbox transacional; esse alinhamento permanece pendente em OpenSpec.
