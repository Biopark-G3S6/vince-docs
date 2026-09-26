# ADR-0031 — Módulo `cohort`: turmas, matrículas e ingresso

- **Status:** Aceito
- **Data:** 2026-09-26
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0014, ADR-0018, ADR-0019, ADR-0021, ADR-0024, ADR-0025, ADR-0027, ADR-0029

## Contexto

`RF-TUR-001` a `RF-TUR-005` definem a turma como a unidade de organização do período letivo, dos
professores designados e das matrículas dos alunos. O curso é proprietário do curso e da coordenação;
`access` é proprietário da identidade, dos papéis e do mecanismo de convite. Nenhum desses módulos pode
ler diretamente as tabelas dos demais.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `cohort`, cuja capacidade é manter turmas, designar professores,
   registrar matrículas e coordenar o ingresso por convite, conforme `RF-TUR-001` a `RF-TUR-005`.
2. O módulo `cohort` NÃO DEVE possuir capacidade sobre curso, instituição, identidade, credencial,
   papel ou permissão.

### Propriedade de dados

3. O schema PostgreSQL do módulo DEVE chamar-se `cohort`.
4. As tabelas sob propriedade do módulo DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `cohort` | identificação, curso, período letivo, intervalo de datas e estado |
   | `cohort_professor` | vínculo corrente entre turma e professor |
   | `cohort_professor_audit` | trilha imutável de designações e revogações |
   | `enrollment` | matrícula do aluno, turma e situação |
   | `cohort_invitation` | vínculo local entre convite emitido e turma |
   | `outbox` | fatos produzidos pelo módulo |
   | `processed_event` | identificadores de eventos consumidos para idempotência |

5. Tabela não enumerada no item 4 NÃO DEVE ser criada no schema `cohort` sem a reescrita deste ADR.
6. Chaves primárias DEVEM ser UUIDv7 geradas pela aplicação. Referências a `course`, `user` e
   `invitation` DEVEM ser identificadores opacos indexados, sem chave estrangeira entre módulos.
   Referências entre registros de `cohort` DEVEM usar chave estrangeira.
7. A identificação da turma DEVE ser única dentro do curso e do período letivo. A matrícula ativa DEVE
   ser única por aluno, conforme a restrição atual da URS.
8. A trilha `cohort_professor_audit` DEVE ser append-only e registrar ator, professor, turma, operação e
   instante. Nenhuma operação do módulo pode alterar ou remover seus registros.

### Integração e titularidade

9. O módulo DEVE consultar `CourseFacade` para validar existência, estado ativo e coordenador do curso,
   e `AccessFacade` para consultar ou alterar contas, papéis e convites. Nenhuma tabela externa pode ser
   lida ou escrita diretamente.
10. A permissão DEVE ser verificada na borda e a titularidade do curso ou da turma DEVE ser verificada
    dentro do caso de uso (`ADR-0014` §11, §12).
11. A designação de professor DEVE atribuir o papel `PROFESSOR` antes de gravar o vínculo local; ambas
    as etapas DEVEM ser idempotentes e não podem participar de uma transação distribuída.
12. A emissão de convite DEVE validar a turma e o professor no módulo `cohort` e solicitar ao `access`
    um convite com contexto opaco `scopeType=COHORT` e `scopeId=<cohortId>`.
13. A aceitação de convite de turma DEVE ser concluída pela combinação da criação da conta no `access`
    e do consumo idempotente de `InvitationAccepted` no `cohort`. O evento DEVE ser gravado na outbox
    do publicador na mesma transação do fato que o origina.
14. O consumidor de `InvitationAccepted` NÃO DEVE reverter a criação da conta. Duplicidade DEVE ser
    tratada como sucesso; falhas DEVEM usar retentativa e dead-letter queue (`ADR-0012`, `ADR-0021`).

### Superfície pública

15. `CohortFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo e DEVE
    transportar somente DTOs, comandos, identificadores opacos e eventos de contrato.
16. As rotas DEVEM seguir o envelope, a paginação, os códigos de falha, o cabeçalho `Location` e a
    especificação OpenAPI definidos em `ADR-0017` e `ADR-0025`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Colocar turma ou matrícula em `course` | O curso é a unidade curricular; turma, matrícula e designação de professor possuem ciclo e propriedade próprios. |
| Colocar turma ou convite em `access` | `ADR-0027` exclui vínculo organizacional da capacidade de identidade e autorização. |
| Chave estrangeira para `course` ou `access` | Viola a propriedade exclusiva de dados e impede a extração independente do módulo. |
| Transação entre criação da conta e matrícula | Viola `ADR-0005` e `ADR-0019`; a consistência entre módulos é obtida por outbox e consumidor idempotente. |
| Papel escopado à turma | `ADR-0027` proíbe papéis escopados; o escopo vem do vínculo local verificado pelo caso de uso. |

## Implicações

1. A criação do módulo exige schema Prisma próprio, migração versionada, fachada, consumidor de evento,
   casos de uso, controllers e registro no composition root.
2. A aceitação de convite pode deixar conta criada antes da matrícula; o estado deve ser observável e a
   reconciliação deve ocorrer por `invitationId`, sem criação duplicada.
3. O módulo depende de uma implementação comum de outbox, relay, filas e DLQ conforme `ADR-0020` e
   `ADR-0021`.
