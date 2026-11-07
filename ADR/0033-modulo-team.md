# ADR-0033 — Módulo `team`: equipe, integrantes e responsabilidade de orientação

- **Status:** Aceito
- **Data:** 2026-11-07
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0012, ADR-0014, ADR-0018, ADR-0019, ADR-0020, ADR-0021, ADR-0024, ADR-0025, ADR-0027, ADR-0030, ADR-0031, ADR-0032

## Contexto

`RF-EQP-001` a `RF-EQP-006` definem a equipe como a unidade de participação no evento: ela é criada
pelo orientador dentro dos limites do evento, reúne alunos elegíveis, admite convite com prazo e tem
um orientador responsável direto. O evento (`ADR-0032`) é proprietário do escopo, do cronograma e dos
limites; o artigo (`ADR-0030`) é proprietário da situação e das avaliações, e nasce na proporção de um
por equipe (`RE-05`).

Falta decidir de quem é a equipe, e como a criação da equipe e a existência do artigo convergem sem
transação entre módulos.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `team`, cuja capacidade é formar equipes no evento, manter os seus
   integrantes, mediar o convite de integrante e registrar o orientador responsável por cada equipe,
   conforme `RF-EQP-001` a `RF-EQP-006`.
2. O módulo `team` NÃO DEVE possuir capacidade sobre evento, cronograma, escopo, turma, curso,
   instituição, identidade, papel, artigo, avaliação, entrega ou revisão.
3. O módulo `team` é o guardião do consumo dos limites declarados pelo evento: a contagem de equipes
   do evento e a contagem de integrantes da equipe são fatos seus.

### Propriedade de dados

4. O schema PostgreSQL do módulo DEVE chamar-se `team`.
5. As tabelas sob propriedade do módulo DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `team` | identificação da equipe, evento, instituição e estado |
   | `team_member` | participação do aluno na equipe, com situação e instante de entrada e saída |
   | `team_invitation` | convite de integrante, com prazo de validade e situação |
   | `team_advisor` | orientador responsável corrente pela equipe |
   | `team_advisor_audit` | trilha imutável de designações e revogações de responsável |
   | `outbox` | fatos produzidos pelo módulo, entre eles `TeamCreated` |
   | `processed_event` | identificadores de eventos consumidos para idempotência |

6. Tabela não enumerada no item 5 NÃO DEVE ser criada no schema `team` sem a reescrita deste ADR.
7. Toda chave primária DEVE ser UUIDv7 gerada pela aplicação. Referências a `event`, `cohort`,
   `course`, `institution`, `user` e `article` DEVEM ser identificadores opacos indexados, sem chave
   estrangeira entre módulos. Referências entre registros de `team` DEVEM usar chave estrangeira.
8. A participação DEVE ser única por aluno e evento **entre as participações ativas** (`RE-04`),
   garantida por índice único parcial sobre `(event_id, user_id)` restrito à situação ativa. A
   unicidade não pode ser obtida por índice total: isso impediria a reentrada após remoção.
9. A remoção de integrante NÃO DEVE apagar a linha de `team_member`: DEVE encerrá-la, preservando o
   instante de entrada e de saída (`RF-EQP-003` RN2). A contribuição registrada no artigo pertence a
   `article` e permanece lá, intocada.
10. A equipe DEVE ter no máximo um orientador responsável ativo por vez (`RF-EQP-005` RN3), garantido
    por índice único parcial sobre `team_id` restrito ao vínculo ativo. A trilha
    `team_advisor_audit` DEVE ser append-only e registrar ator, orientador, equipe, operação e
    instante.
11. O convite DEVE guardar prazo de validade e situação; a expiração DEVE ser avaliada pelo instante
    do aceite, não por rotina de varredura.

### Integração e titularidade

12. O módulo DEVE consultar `EventFacade` para existência, estado, escopo, limites e orientação do
    evento; `CohortFacade` e `CourseFacade`, quando a elegibilidade do aluno exigir, sempre em
    operação em lote; e `AccessFacade` para contas e papéis. NÃO DEVE ler tabela, fila ou schema
    desses módulos diretamente.
13. A permissão DEVE ser verificada na borda e a titularidade DEVE ser verificada dentro do caso de
    uso (`ADR-0014` §11, §12): criar equipe, designar, remover e convidar exigem orientação no
    evento — `ADVISOR_NOT_ASSIGNED_TO_EVENT`; nomear o responsável exige ser dono do escopo do
    evento — `PERMISSION_DENIED`; ingressar exige elegibilidade — `STUDENT_NOT_ELIGIBLE`.
14. A criação de equipe DEVE validar o limite do evento **dentro da própria transação**, por escrita
    condicional sobre a contagem corrente, e recusar com `EVENT_TEAM_LIMIT_REACHED`. Leitura prévia
    do limite NÃO DEVE ser aceita como garantia.
15. O ingresso, a designação e o aceite de convite DEVEM revalidar, no instante da escrita,
    elegibilidade, unicidade por evento e tamanho máximo, recusando com `STUDENT_NOT_ELIGIBLE`,
    `STUDENT_ALREADY_IN_TEAM`, `TEAM_SIZE_LIMIT_REACHED` e `INVITATION_EXPIRED` conforme o caso
    (`RF-EQP-004` RN2).
16. Operação de formação em evento cancelado DEVE falhar com `VALIDATION_FAILED`.

### Criação do artigo

17. A criação da equipe DEVE gravar o fato `TeamCreated` na outbox do módulo, na mesma transação que
    cria a equipe (`ADR-0021` §1). O módulo `team` NÃO DEVE criar, consultar como pré-condição, nem
    possuir o artigo.
18. O artigo inicial é criado pelo consumo idempotente de `TeamCreated` em `article` (`ADR-0030` §9).
    A transação de `team` NÃO DEVE depender desse consumo para concluir, e nenhum consumidor pode
    reverter a criação da equipe.
19. `TeamCreated` DEVE transportar identificadores opacos — equipe, evento, instituição e ator — e o
    instante do fato, com versão de contrato explícita. Falhas de entrega DEVEM usar retentativa e
    dead-letter queue (`ADR-0012`, `ADR-0021`).
20. O módulo DEVE publicar também os fatos de alteração da composição — criação e encerramento de
    equipe, entrada e saída de integrante —, cada um transportando o evento, a equipe e a
    **contagem resultante** que o módulo apurou dentro da sua transação. É deles que `event`
    alimenta a sua projeção de uso (`ADR-0032` §16); publicar apenas o fato sem a contagem obrigaria
    o consumidor a perguntar de volta e fecharia o ciclo que `ADR-0005` §6 proíbe.
21. A ausência temporária do artigo após a criação da equipe é estado eventual legítimo e DEVE ser
    observável; a resposta da criação apresenta o vínculo quando o consumidor o confirma.

### Convite de integrante

22. O convite de integrante de equipe é entidade **deste** módulo e NÃO DEVE ser confundido com o
    convite de ingresso de `access` (`ADR-0027`), que cria conta. O convite de equipe pressupõe conta
    existente e aluno elegível, e suas rotas DEVEM ser explicitamente vinculadas à equipe.
23. A recusa do convite DEVE encerrá-lo sem efeito sobre a equipe.

### Superfície pública

24. `TeamFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo e DEVE
    transportar somente DTOs, comandos, identificadores opacos e eventos de contrato. Não pode expor
    entidades de domínio nem tipos gerados pelo ORM.
25. A fachada DEVE oferecer, no mínimo, consulta de equipe por identificador, consulta das equipes de
    um evento, contagem de equipes e de integrantes, verificação de participação de um aluno e
    verificação do responsável direto — operações de que `event` e `article` dependem.
26. As rotas DEVEM seguir o envelope, a paginação, os códigos de falha, o cabeçalho `Location` e a
    especificação OpenAPI definidos em `ADR-0017` e `ADR-0025`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Colocar a equipe em `event` | O evento é a unidade de organização do período; a formação de equipe tem ciclo, concorrência e autorização próprios, e faria `event` possuir integrante e convite. |
| Colocar o artigo em `team` | `ADR-0030` atribui o artigo ao módulo `article`; a proporção de um para um não implica propriedade comum. |
| Criar equipe e artigo na mesma transação | Exigiria transação distribuída, proibida por `ADR-0005` e `ADR-0019`; a outbox com consumidor idempotente preserva o isolamento. |
| Apagar a linha do integrante na remoção | Perderia a evidência da participação exigida por `RF-EQP-003` RN2 e deixaria a nota individual de `article` sem referente. |
| Índice único total sobre `(event_id, user_id)` | Impediria o aluno removido de reingressar, o que nenhum requisito proíbe. |
| Guardar a contagem de equipes no evento | Faria a transação de `team` escrever em tabela de outro módulo. |
| Reutilizar o convite de `access` para a equipe | Confunde criação de conta com formação de equipe; os prazos, as validações e o alcance são distintos. |
| Expirar convites por rotina de varredura | A validade importa no instante do aceite; a varredura apenas antecipa limpeza e abriria janela de divergência. |

## Implicações

1. A criação do módulo exige schema Prisma próprio, migração versionada, fachada, outbox, casos de
   uso, controllers e registro no composition root, com `access`, `institution`, `course`, `cohort` e
   `event` ativos.
2. `article` depende de `TeamCreated` para existir e `event`, dos fatos de composição para a sua
   projeção de uso; interromper a publicação da outbox deixa equipes sem artigo e limites
   defasados, e o reprocessamento precisa convergir sem duplicar.
3. As invariantes de limite e unicidade exigem teste com operações concorrentes (`ADR-0024`), não
   apenas teste sequencial de caso de uso.
4. A consulta de alunos elegíveis sem equipe cruza a elegibilidade mantida por `cohort`/`course` com
   a participação mantida aqui: exige fachada em lote e paginação, nunca consulta por aluno.
