# Registros de Decisão Arquitetural — VinceArt

Este diretório contém os ADRs (Architecture Decision Records) do projeto VinceArt.
As regras de criação, numeração e revisão estão em [ADR-0000](0000-adocao-de-adrs.md).

Um ADR revisto é **reescrito no próprio arquivo**; não há ADR substituto. A decisão anterior fica
registrada na seção `Alternativas rejeitadas` do próprio ADR, e o histórico completo é o do
repositório de versionamento.

## Índice

| ADR | Título | Status | Data |
| :--- | :--- | :--- | :--- |
| [0000](0000-adocao-de-adrs.md) | Adoção de Architecture Decision Records | Aceito | 2026-08-11 |
| [0001](0001-monolito-modular.md) | Monolito modular como estilo arquitetural do backend | Aceito | 2026-08-11 |
| [0002](0002-stack-backend-nestjs.md) | Stack do backend: NestJS + TypeScript | Aceito | 2026-08-11 |
| [0003](0003-fronteira-e-estrutura-de-modulo.md) | Fronteira e estrutura interna de módulo | Aceito | 2026-08-11 |
| [0004](0004-fachada-como-superficie-publica.md) | Fachada abstrata como única superfície pública do módulo | Aceito | 2026-08-11 |
| [0005](0005-comunicacao-entre-modulos.md) | Comunicação entre módulos | Aceito | 2026-08-11 |
| [0006](0006-propriedade-de-dados-por-modulo.md) | Propriedade exclusiva de dados por módulo | Aceito | 2026-08-11 |
| [0007](0007-enforcement-de-fronteiras.md) | Enforcement automatizado de fronteiras | Aceito | 2026-08-11 |
| [0008](0008-escalabilidade-por-papel-de-processo.md) | Escalabilidade por papel de processo | Aceito | 2026-08-11 |
| [0009](0009-dry-e-shared-kernel.md) | Aplicação de DRY e escopo do shared kernel | Aceito | 2026-08-11 |
| [0010](0010-camada-http-e-orm.md) | Camada HTTP e ORM | Aceito | 2026-08-11 |
| [0011](0011-desempenho-e-prevencao-de-n-mais-1.md) | Metas de desempenho e prevenção de N+1 | Aceito | 2026-08-11 |
| [0012](0012-retentativa-e-dead-letter-queue.md) | Política de retentativa e dead-letter queue | Aceito | 2026-08-11 |
| [0013](0013-autenticacao-por-sessao-opaca.md) | Autenticação por sessão opaca | Aceito | 2026-08-11 |
| [0014](0014-autorizacao-rbac-e-delegacao.md) | Autorização por RBAC e delegação de permissões | Aceito | 2026-08-11 |
| [0015](0015-arquitetura-do-frontend.md) | Arquitetura do frontend | Aceito | 2026-08-11 |
| [0016](0016-stack-do-frontend.md) | Stack do frontend | Aceito | 2026-08-11 |
| [0017](0017-contrato-de-integracao-frontend-backend.md) | Contrato de integração entre frontend e backend | Aceito | 2026-08-11 |
| [0018](0018-organizacao-fisica-do-banco-de-dados.md) | Organização física do banco de dados | Aceito | 2026-08-11 |
| [0019](0019-transacoes-e-gestao-de-conexoes.md) | Transações e gestão de conexões | Aceito | 2026-08-11 |
| [0020](0020-transporte-de-mensagens-e-isolamento-de-filas.md) | Transporte de mensagens e isolamento de filas | Aceito | 2026-08-11 |
| [0021](0021-outbox-transacional-e-relay-de-eventos.md) | Outbox transacional e relay de eventos | Aceito | 2026-08-11 |
| [0022](0022-observabilidade-e-registro-de-erros.md) | Observabilidade e registro de erros | Aceito | 2026-08-12 |
| [0023](0023-ambiente-de-desenvolvimento-e-verificacao.md) | Ambiente de desenvolvimento e verificação automatizada | Aceito | 2026-08-12 |
| [0024](0024-estrategia-de-testes.md) | Estratégia de testes | Aceito | 2026-08-12 |
| [0025](0025-formato-de-resposta-da-api.md) | Formato de resposta da API | Aceito | 2026-08-12 |
| [0026](0026-estrategia-de-internacionalizacao.md) | Estratégia de internacionalização | Aceito | 2026-08-19 |
| [0027](0027-modulo-access.md) | Módulo `access`: identidade e autorização | Aceito | 2026-08-31 |

## Decisões pendentes

| Tópico | Observação |
| :--- | :--- |
| Decomposição do sistema em módulos | Exige um ADR por módulo (ADR-0003 §12); depende dos requisitos funcionais. O módulo `access` está decidido em ADR-0027; os demais permanecem pendentes. |
| Carga de referência e capacidade | Necessária para revalidar as metas de ADR-0011. |
| Infraestrutura de implantação | Automação de implantação, ambientes, segredos, coletor de log e servidor de métricas (ADR-0022 §6 e §34; ADR-0023 §19). |
| Conformidade legal no tratamento de dados pessoais | Padrões de Engenharia, PAD-SEG-015. |
| Catálogo de códigos de resposta | Derivado dos requisitos funcionais (ADR-0025 §20); mantido na URS §9. Parcialmente preenchido pela URS 0.1; a fatia de correção o ampliará. |
| Catálogo de permissões | Derivado dos requisitos funcionais (ADR-0014 §8); mantido na URS §8. Parcialmente preenchido pela URS 0.1; a fatia de correção o ampliará. |

## Uso

Novo ADR: copie [`template.md`](template.md), renomeie para `NNNN-titulo-em-kebab-case.md` e
atualize o índice acima no mesmo commit.

Revisão de decisão: reescreva o ADR existente, registre a decisão abandonada em
`Alternativas rejeitadas`, atualize a data do cabeçalho e as referências cruzadas afetadas.
