# ADR-0030 — Módulo `article`: situação, avaliação e publicação do artigo

- **Status:** Aceito
- **Data:** 2026-09-26
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0014, ADR-0018, ADR-0019, ADR-0021, ADR-0024, ADR-0025, ADR-0029

## Contexto

`RF-ART-001` a `RF-ART-004` definem o artigo como a unidade de produção associada à equipe: ele possui
estado, avaliação do trabalho, avaliações individuais e registros manuais de publicação externa. A
equipe é proprietária da formação e dos integrantes; evento, turma e curso são proprietários dos
respectivos vínculos e cronogramas. Nenhum desses dados pode ser reunido por leitura direta de tabelas
entre schemas.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `article`, cuja capacidade é manter a situação do artigo, suas
   avaliações auditáveis e seus registros de publicação externa, conforme `RF-ART-001` a `RF-ART-004`.
2. O módulo `article` NÃO DEVE possuir capacidade sobre equipe, integrantes, evento, cronograma, turma,
   curso, edição, entrega ou revisão. Esses conceitos pertencem às suas respectivas verticais.

### Propriedade de dados

3. O schema PostgreSQL do módulo DEVE chamar-se `article`.
4. As tabelas de negócio sob propriedade do módulo DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `article` | artigo, equipe, evento, estado e etapa corrente como referências opacas |
   | `article_grade` | visão corrente da nota única do artigo |
   | `member_grade` | visão corrente da nota individual de cada integrante avaliado |
   | `article_grade_history` | histórico imutável das alterações da nota do artigo |
   | `member_grade_history` | histórico imutável das alterações das notas individuais |
   | `publication` | registro manual de publicação externa do artigo |
   | `outbox` | fatos produzidos pelo módulo e eventos necessários à integração |
   | `processed_event` | identificadores de eventos consumidos para idempotência |

5. Tabela não enumerada no item 4 NÃO DEVE ser criada no schema `article` sem a reescrita deste ADR.
6. Toda chave primária DEVE ser UUIDv7 gerada pela aplicação. Referências a `team`, `event`, `cohort`,
   `course` e `user` DEVEM ser identificadores opacos indexados, sem chave estrangeira entre módulos.
7. As tabelas de histórico DEVEM ser append-only. Nenhuma operação do módulo pode alterar ou remover
   registro histórico; cada alteração DEVE registrar valor, autor e instante.
8. A nota corrente e sua linha histórica correspondente DEVEM ser gravadas na mesma transação local.
   Atualizações concorrentes DEVEM usar versão ou escrita condicional para não perder avaliação.

### Integração e titularidade

9. A criação do artigo DEVE ocorrer pelo consumo idempotente do fato `TeamCreated`, publicado pelo módulo
   `team` em sua outbox. O artigo inicial DEVE possuir estado `STARTED`.
10. O módulo `article` DEVE consultar fachadas de `team`, `event`, `cohort`, `course` e `access` somente
    para validar alcance, existência, estado e responsabilidade. Não pode ler tabelas ou filas desses
    módulos diretamente.
11. O consumo de `TeamCreated` NÃO DEVE participar da transação do módulo publicador. Falhas DEVEM ser
    tratadas por retentativa e dead-letter queue, e o consumidor DEVE convergir ao mesmo estado quando o
    fato for entregue mais de uma vez.
12. A autorização de borda DEVE exigir a permissão do recurso. Cada caso de uso DEVE verificar também a
    titularidade: aluno somente da própria equipe; orientador do evento de todas as equipes do evento;
    coordenador dos artigos alcançados pelo seu curso; nota somente do orientador responsável.

### Estado, avaliação e publicação

13. Os estados reconhecidos pelo módulo DEVEM ser `STARTED`, `IN_PROGRESS`, `IN_REVIEW` e `FINISHED`.
    Este módulo pode consultar e persistir o estado projetado, mas transições pertencem às verticais de
    edição e revisão.
14. A nota do artigo DEVE ser distinta das notas individuais e NÃO DEVE determinar sozinha a aprovação
    dos alunos.
15. A avaliação individual DEVE permanecer vinculada ao identificador do integrante e ao snapshot mínimo
    da participação usado no momento da avaliação, mesmo após a remoção do integrante da equipe.
16. `Publication` DEVE ser registro manual e descritivo, com veículo, tipo, data e endereço. O módulo NÃO
    DEVE manter catálogo de veículos externos, verificar publicação em serviço externo ou tratar entrega
    a evento interno como publicação externa.

### Superfície pública

17. `ArticleFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo e DEVE
    transportar somente DTOs, identificadores opacos, comandos e eventos de contrato. Não pode expor
    entidades de domínio nem tipos gerados pelo ORM.
18. A fachada DEVE oferecer, no mínimo, criação idempotente a partir de `TeamCreated`, consulta de
    situação, gravação de avaliações, consulta paginada de histórico e operações de publicação externa.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Colocar o artigo no módulo `team` | A equipe e o artigo têm proprietários e ciclos de evolução distintos; isso faria a formação de equipe possuir avaliação e publicação. |
| Consultar tabelas de equipe, evento ou curso diretamente | Viola ADR-0006 e impediria a extração independente das verticais. |
| Criar artigo dentro da transação de equipe | Exigiria transação distribuída; `TeamCreated` com outbox e consumidor idempotente preserva o isolamento. |
| Substituir o histórico pela sobrescrita da nota corrente | Perderia a autoria e o instante exigidos por `RF-ART-002` e `RF-ART-003`. |
| Manter catálogo de eventos ou periódicos externos | Está fora de `RF-ART-004`; o registro desta versão é manual e descritivo. |

## Implicações

1. A criação do módulo exige schema Prisma próprio, migração versionada, fachada, consumidor de evento,
   casos de uso, controllers e registro no composition root.
2. `team`, `event`, `cohort` e `course` precisam oferecer contratos de alcance em lote para evitar N+1;
   a ausência desses contratos bloqueia a integração completa da vertical.
3. A existência temporariamente ausente do artigo após a criação da equipe é estado eventual e deve ser
   observável até o consumidor confirmar o processamento.
4. O crescimento do histórico exige índices por artigo, integrante e instante, além de paginação; a
   retenção não pode apagar evidência sem decisão específica de auditoria.
