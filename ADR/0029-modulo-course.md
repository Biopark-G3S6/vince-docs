# ADR-0029 — Módulo `course`: manutenção de cursos e coordenação

- **Status:** Aceito
- **Data:** 2026-09-17
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0014, ADR-0018, ADR-0019, ADR-0025, ADR-0027, ADR-0028

## Contexto

`RF-CUR-001` e `RF-CUR-002` definem curso como unidade de organização pertencente a uma instituição,
mas a decomposição modular ainda não declarou seu proprietário. Turmas e eventos precisarão consultar
o estado do curso e a designação do coordenador sem acessar tabelas de outro módulo.

## Decisão

1. DEVE existir o módulo de negócio `course`, cuja capacidade é manter cursos e designar ou revogar o
   coordenador responsável, conforme `RF-CUR-001` e `RF-CUR-002`.
2. O schema PostgreSQL do módulo DEVE chamar-se `course`. As tabelas de negócio sob sua propriedade
   DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `course` | identificação, vínculo institucional e estado do curso |
   | `course_coordinator` | vínculo corrente entre um curso e seu coordenador |
   | `course_coordinator_audit` | trilha imutável de designações e revogações |

3. A tabela `course` DEVE possuir chave primária UUIDv7 gerada pela aplicação, `institution_id` como
   identificador opaco indexado sem chave estrangeira, os campos obrigatórios de nome e identificação,
    estado ativo ou inativo e os instantes de criação e atualização.
4. A tabela `course_coordinator` DEVE possuir chave estrangeira para `course`, `user_id` como
   identificador opaco indexado sem chave estrangeira e uma restrição que permita no máximo um vínculo
   corrente por curso. A revogação DEVE remover o vínculo corrente, preservando o histórico na tabela de
   auditoria.
5. A tabela `course_coordinator_audit` DEVE possuir chave primária UUIDv7 gerada pela aplicação,
   referência ao curso do próprio módulo, identificadores opacos do usuário e do ator, operação textual
   restrita a designação ou revogação e instante da operação. A tabela DEVE ser imutável: nenhuma
   operação do módulo pode alterar ou remover seus registros.
6. O módulo `course` DEVE depender de `InstitutionFacade` para validar existência e estado da
   instituição e de `AccessFacade` para consultar o vínculo institucional do ator e do usuário-alvo,
   verificar conta ativa e atribuir ou revogar `COORDINATOR`. Nenhuma tabela de `institution` ou
   `access` pode ser lida ou escrita diretamente.
7. A autorização de borda DEVE exigir as permissões de `RF-CUR-001` e `RF-CUR-002`. Cada caso de uso
   DEVE verificar também, dentro da própria execução, que o ator pertence à instituição do registro;
   possuir a permissão não autoriza operar curso de outra instituição.
8. Curso inativo DEVE permanecer consultável e preservar seus vínculos e auditoria, mas não DEVE
   admitir novas turmas ou eventos. Os módulos proprietários de turma e evento DEVEM consultar a
   fachada de `course` antes de criar registros vinculados; `course` não acessará tabelas desses módulos.
9. A designação DEVE validar curso ativo, titularidade institucional e usuário ativo, atribuir o papel
   `COORDINATOR` pela fachada de `access` antes de gravar o vínculo local e registrar vínculo e
   auditoria na mesma transação local. Repetir a designação do mesmo usuário DEVE ser idempotente;
   outro usuário enquanto houver coordenador corrente DEVE resultar em
   `COORDINATOR_ALREADY_ASSIGNED`.
10. A revogação DEVE ser idempotente, registrar a operação somente quando houver vínculo a remover e
    não DEVE remover concessões diretas de permissão do usuário. O papel `COORDINATOR` DEVE ser
    revogado por `access` apenas quando não houver outro vínculo corrente do mesmo usuário que o
    justifique.
11. As chamadas entre módulos DEVEM ocorrer fora da transação local, e nenhuma transação do módulo
    `course` pode abranger chamada à fachada de outro módulo. A repetição da operação DEVE convergir
    para o estado correto quando uma das etapas entre módulos falhar.
12. `CourseFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo e DEVE
    transportar apenas DTOs e identificadores opacos. Além das operações HTTP da capacidade, a fachada
    DEVE oferecer as consultas mínimas de estado do curso e de coordenador para consumidores como
    `cohort` e `event`, sem expor repositórios, entidades ou tipos do Prisma.
13. As rotas HTTP DEVEM ser versionadas pela API e seguir a semântica do envelope, da paginação, dos
    códigos de falha e do cabeçalho `Location` definidos em ADR-0017 e ADR-0025. As rotas de
    desativação e de designação ou revogação de coordenador DEVEM permanecer operações distintas de
    `PATCH`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Colocar cursos no módulo `institution` | `ADR-0028 §3` reserva aquele módulo à instituição e aos seus administradores. |
| Colocar cursos no módulo `access` | `ADR-0027 §2` exclui vínculo organizacional, curso e coordenação da capacidade de `access`. |
| Usar papel `COORDINATOR` escopado ao curso | `ADR-0027 §16` proíbe papéis escopados; o vínculo em `course_coordinator` fornece o escopo. |
| Consultar diretamente tabelas de `institution` ou `access` | Viola propriedade exclusiva de dados e impediria a extração independente do módulo. |
| Alterar o estado por `PATCH` | Misturaria `COURSE:UPDATE` e `COURSE:DEACTIVATE`, concedendo ao primeiro uma autoridade que o catálogo não lhe atribui. |
| Manter somente o coordenador atual | Perderia a trilha exigida por `RF-CUR-002` e por `ADR-0018 §6`. |

## Implicações

1. A criação do módulo exige schema Prisma próprio, cliente Prisma escopado, migração versionada,
   fachada, casos de uso, controllers e registro no composition root.
2. A integridade entre curso, instituição e usuário será garantida pela aplicação e pelas fachadas,
   não por chaves estrangeiras entre schemas.
3. O máximo de um coordenador corrente deve ser garantido por restrição do banco, além da validação de
   aplicação para suportar requisições concorrentes.
4. O papel global `COORDINATOR` pode permanecer atribuído quando o usuário ainda coordenar outro curso;
   revogar a designação de um curso não pode retirar autoridade concedida por outro vínculo nem
   concessões diretas.
5. A regra de no máximo um coordenador implementa a premissa registrada em `RF-CUR-002 RN1`, que a
   URS marca como pendente de confirmação; sua alteração exige revisão deste ADR e da mudança
   `add-course-management`.
