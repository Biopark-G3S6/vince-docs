# ADR-0032 — Módulo `event`: evento, cronograma e orientação

- **Status:** Aceito
- **Data:** 2026-11-07
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0014, ADR-0018, ADR-0019, ADR-0021, ADR-0024, ADR-0025, ADR-0027, ADR-0028, ADR-0029, ADR-0031

## Contexto

`RF-EVT-001` a `RF-EVT-004` definem o evento como a unidade que organiza a produção acadêmica de um
período: tema, problema, objetivos, cronograma de etapas, limites de formação de equipe e os
professores que orientam. O evento nasce vinculado a um alvo — turma, curso ou instituição — mas
`institution`, `course` e `cohort` são proprietários desses alvos e dos vínculos que tornam um
usuário elegível. A equipe e o artigo, que consomem os limites e o cronograma, pertencem a verticais
próprias.

Falta decidir de quem é o evento. Sem essa decisão, a elegibilidade por escopo tenderia a ser
resolvida por leitura direta das tabelas de turma e curso, e o cronograma, a ser duplicado por
equipe.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `event`, cuja capacidade é manter o ciclo de vida do evento, o
   seu escopo, o seu cronograma de etapas e a designação dos seus orientadores, conforme
   `RF-EVT-001` a `RF-EVT-004`.
2. O módulo `event` NÃO DEVE possuir capacidade sobre instituição, curso, turma, matrícula,
   identidade, papel, equipe, integrante, artigo, entrega ou revisão. Esses conceitos pertencem às
   suas respectivas verticais.
3. O evento é a unidade que **declara** limites e prazos; o módulo NÃO DEVE guardar o consumo desses
   limites, que é fato do módulo proprietário da equipe.

### Propriedade de dados

4. O schema PostgreSQL do módulo DEVE chamar-se `event`.
5. As tabelas sob propriedade do módulo DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `event` | título, tema, problema, objetivos, escopo, ancestralidade do alvo, limites, uso projetado e estado |
   | `milestone` | etapa do cronograma do evento, com nome, ordem e prazo |
   | `event_advisor` | vínculo corrente entre evento e professor orientador |
   | `event_advisor_audit` | trilha imutável de designações e revogações de orientador |
   | `outbox` | fatos produzidos pelo módulo |
   | `processed_event` | identificadores de eventos consumidos para idempotência |

6. Tabela não enumerada no item 5 NÃO DEVE ser criada no schema `event` sem a reescrita deste ADR.
7. Toda chave primária DEVE ser UUIDv7 gerada pela aplicação. Referências a `institution`, `course`,
   `cohort` e `user` DEVEM ser identificadores opacos indexados, sem chave estrangeira entre
   módulos. Referências entre registros de `event` DEVEM usar chave estrangeira.
8. O escopo DEVE ser gravado como o par `scope_type` e `scope_id`, em que `scope_type` é texto com
   restrição de verificação sobre `INSTITUTION`, `COURSE` e `COHORT`. `ENUM` nativo é proibido
   (`ADR-0018` §19).
9. O evento DEVE guardar a **ancestralidade do seu alvo** — a instituição sempre, e o curso quando o
   alvo for curso ou turma —, derivada no momento da criação e imutável depois dela. Guardá-la é o
   que permite responder "os eventos do meu curso" e "os da minha instituição" com um predicado
   indexado, sem pedir ao módulo vizinho a lista de turmas de cada curso. Alteração de evento NÃO
   DEVE mudar o escopo nem a ancestralidade.
10. A ordem da etapa DEVE ser única dentro do evento, e o prazo DEVE crescer estritamente conforme a
    ordem. A trilha `event_advisor_audit` DEVE ser append-only e registrar ator, professor, evento,
    operação e instante.

### Escopo e elegibilidade

11. A elegibilidade DEVE ser derivada do escopo, não inscrita: são elegíveis os professores e alunos
    vinculados ao alvo do evento (`RF-EVT-001` RN2).
12. O módulo DEVE resolver o alvo e a elegibilidade por `InstitutionFacade`, `CourseFacade` e
    `CohortFacade`, conforme o `scope_type`, e por `AccessFacade` para contas e papéis. NÃO DEVE ler
    tabela, fila ou schema desses módulos diretamente.
13. A verificação de elegibilidade de um conjunto de usuários DEVE ocorrer por operação em lote.
    Consulta dentro de laço é proibida (`ADR-0011` §7, `PAD-ESC-009`).
14. Criar evento em escopo superior ao vínculo do ator DEVE falhar com `EVENT_SCOPE_NOT_ALLOWED`;
    alvo inexistente ou inativo, com `RESOURCE_NOT_FOUND`.

### Cronograma, limites e estado

15. Os limites de quantidade de equipes e de tamanho de equipe DEVEM ser positivos. Alteração que os
    reduza abaixo do uso corrente DEVE falhar com `VALIDATION_FAILED`.
16. O uso corrente DEVE ser mantido como **projeção local** no próprio registro do evento,
    atualizada pelo consumo idempotente dos fatos de formação publicados pelo módulo proprietário da
    equipe. O módulo `event` NÃO DEVE consultar aquele módulo por fachada: a dependência entre os
    dois é de mão única — a equipe conhece o evento, e o evento conhece apenas os fatos que ela
    publica (`ADR-0005` §6).
17. O módulo NÃO DEVE participar da transação que cria equipe ou integrante. A reserva e a
    revalidação do limite no instante da escrita são obrigação do módulo proprietário da equipe, que
    responde `EVENT_TEAM_LIMIT_REACHED` e `TEAM_SIZE_LIMIT_REACHED`. A projeção é, por isso,
    conveniência de recusa antecipada, e não a guarda do limite: a sua defasagem pode admitir uma
    redução que deixe equipes acima do novo teto, e isso é aceito — o teto é cap de novas
    formações, não ordem de desfazer o que existe.
18. Remoção de etapa já iniciada DEVE falhar com `VALIDATION_FAILED`; prazo fora da ordem crescente,
    com `MILESTONE_DATE_CONFLICT`.
19. O cancelamento DEVE ser idempotente e preservar o evento como registro consultável. Evento
    cancelado DEVE recusar novas operações de formação de equipe, verificado pelo consumidor da
    fachada no momento da operação.

### Integração e titularidade

20. A permissão DEVE ser verificada na borda e a titularidade do escopo DEVE ser verificada dentro do
    caso de uso (`ADR-0014` §11, §12).
21. A consulta de eventos DEVE devolver somente os eventos alcançados pelos vínculos do ator: aluno,
    os em que é elegível; professor, os em que é orientador ou dono do escopo; coordenador, os do seu
    curso; administrador institucional, os da sua instituição (`RF-EVT-004` RN1). Evento fora do
    alcance DEVE ser indistinguível de inexistente — `RESOURCE_NOT_FOUND`.
22. A designação de orientador DEVE ser idempotente e DEVE recusar professor inelegível pelo escopo
    com `STUDENT_NOT_ELIGIBLE`, conforme o código declarado na URS para o caso.
23. Fatos relevantes a outras verticais DEVEM ser gravados na outbox do módulo na mesma transação do
    fato que os origina (`ADR-0021` §1).

### Superfície pública

24. `EventFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo e DEVE
    transportar somente DTOs, comandos, identificadores opacos e eventos de contrato. Não pode expor
    entidades de domínio nem tipos gerados pelo ORM.
25. A fachada DEVE oferecer, no mínimo, consulta de evento por identificador, consulta em lote de
    eventos alcançados, consulta de etapa e de etapa corrente, verificação de orientação e
    verificação de alcance de um usuário — operações de que `team` e `article` dependem.
26. As rotas DEVEM seguir o envelope, a paginação, os códigos de falha, o cabeçalho `Location` e a
    especificação OpenAPI definidos em `ADR-0017` e `ADR-0025`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Colocar o evento em `course` ou `cohort` | O evento atravessa os três escopos; alojá-lo em um deles obrigaria o escopo de instituição a ser lido de dentro de um módulo de curso. |
| Uma tabela de evento por escopo | Duplicaria ciclo de vida, cronograma e autorização por três, sem ganho de isolamento. |
| `ENUM` nativo para `scope_type` e estado | Proibido por `ADR-0018` §19: a alteração do conjunto exigiria migração de tipo. |
| Apurar o uso chamando a fachada do módulo de equipe | Fecharia o ciclo `team` → `event` → `team`, proibido por `ADR-0005` §6. A projeção por fato preserva a mão única. |
| Participar da transação de criação de equipe para reservar o limite | Transação distribuída, proibida por `ADR-0019`; a guarda definitiva é a escrita condicional do módulo da equipe. |
| Chave estrangeira para `course` ou `cohort` | Viola a propriedade exclusiva de dados e impede a extração independente do módulo. |
| Resolver o alcance do coordenador pedindo as turmas de cada curso | Lista sem cota natural a cada consulta de listagem; a ancestralidade derivada responde com um predicado indexado. |
| Replicar localmente as matrículas para avaliar elegibilidade | Antecipa consistência eventual sem necessidade; a fachada em lote atende `ADR-0011`. |
| Cronograma por equipe | `RF-EVT-002` RN1 fixa o cronograma no evento, para padronizar os prazos de todas as suas equipes. |

## Implicações

1. A criação do módulo exige schema Prisma próprio, migração versionada, fachada, casos de uso,
   controllers e registro no composition root, com `access`, `institution`, `course` e `cohort`
   ativos.
2. `institution`, `course` e `cohort` precisam oferecer verificação de alcance e de elegibilidade em
   lote; a ausência desses contratos bloqueia a consulta por escopo sem N+1.
3. O limite de equipes é declarado aqui e aplicado em `team`: a divergência momentânea entre a
   projeção e a escrita é aceita, e a recusa definitiva ocorre na transação de `team`. A projeção
   exige consumidor idempotente e tolerância à reentrega do mesmo fato.
4. As etapas são a unidade à qual se prenderão as entregas (`RF-REV-001`) e os apontamentos
   (`RF-REV-004`); mudar a identidade da etapa depois disso quebraria o ciclo de correção.
