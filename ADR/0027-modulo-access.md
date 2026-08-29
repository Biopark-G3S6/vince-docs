# ADR-0027 — Módulo `access`: identidade e autorização

- **Status:** Aceito
- **Data:** 2026-08-27
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0013, ADR-0014, ADR-0018

## Contexto

Toda vertical funcional da URS pressupõe um ator identificado e uma decisão de autorização, mas
nenhum módulo existe ainda. O ADR-0003 §12 exige que a criação de um módulo seja precedida da
declaração de sua capacidade e das tabelas sob sua propriedade, e a decomposição em módulos consta
como pendência desde a adoção dos ADRs.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `access`, cuja capacidade é **identidade e autorização**: quem é o ator, por que meio ele prova sê-lo, e o que ele está autorizado a fazer.
2. O módulo `access` NÃO DEVE possuir capacidade sobre o vínculo organizacional do ator — instituição, curso, turma, matrícula, evento ou equipe —, que pertence aos módulos proprietários desses conceitos.
3. O módulo `access` NÃO DEVE decidir titularidade de registro; ele responde quais permissões o ator possui, e a titularidade é verificada dentro do caso de uso do módulo proprietário do registro (ADR-0014 §12).

### Propriedade de dados

4. O schema PostgreSQL do módulo DEVE chamar-se `access` (ADR-0018 §1).
5. As tabelas sob propriedade do módulo `access` DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `permission` | o catálogo das permissões reconhecidas pelo sistema |
   | `role` | os papéis globais pré-criados |
   | `role_permission` | a composição de cada papel |
   | `user` | a conta de usuário e seu perfil |
   | `user_role` | a atribuição de papel a uma conta |
   | `password_credential` | a credencial de senha da conta |
   | `permission_grant` | a concessão direta de permissão entre contas (ADR-0014 §5) |
   | `invitation` | o convite como via de criação de conta |

6. Tabela não enumerada em §5 NÃO DEVE ser criada no schema `access` sem a reescrita deste ADR.
7. As tabelas de §5 residem no mesmo módulo porque a resolução das permissões efetivas percorre `user`, `user_role`, `role_permission` e `permission_grant` em toda requisição autenticada (ADR-0014 §9); separá-las faria dessa travessia uma junção entre módulos, vedada por ADR-0006 §3, e uma referência sem integridade declarada, por ADR-0006 §4.
8. A referência do módulo `access` a um registro de outro módulo — notadamente a instituição de vínculo de uma conta — DEVE ser coluna de identificador indexada, sem chave estrangeira (ADR-0018 §13, §14).

### Posição na dependência entre módulos

9. O módulo `access` DEVE ser **módulo folha** na dependência síncrona: os demais módulos PODEM depender de sua fachada, e ele NÃO DEVE depender da fachada de módulo algum.
10. A necessidade do módulo `access` de conhecer fato produzido por outro módulo DEVE ser satisfeita por evento, e nunca por chamada síncrona (ADR-0005 §2, §6).
11. A regra de §9 é o que impede ciclo de dependência com o módulo `access`, para o qual todo módulo aponta.

### Superfície pública

12. A fachada `AccessFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo (ADR-0004 §1).
13. A fachada NÃO DEVE expor operação que crie, altere, renomeie ou remova papel ou permissão, nem que altere a composição de um papel.
14. Os códigos de papel e de permissão DEVEM atravessar a fronteira do módulo como texto opaco, e NÃO DEVEM atravessá-la como entidade de domínio nem como tipo gerado por ORM (ADR-0004 §9).

### Catálogo de papéis e permissões

15. Os cinco papéis da URS §1.4 são globais, DEVEM ser criados por carga inicial e NÃO DEVEM ser administráveis em tempo de execução.
16. NÃO DEVE existir papel escopado a instituição, curso, turma ou evento; o escopo vem do vínculo (ADR-0014 §12).
17. O catálogo das permissões e a composição dos papéis DEVEM ser declarados uma única vez no repositório de código, em `domain/`, e a carga inicial e os testes DEVEM derivar dessa declaração.
18. A declaração de §17 DEVE corresponder ao catálogo da URS §2.3 e §2.3.1, e DEVE existir comando que confronte as duas e relate as diferenças em ambos os sentidos.
19. O comando de §18 NÃO DEVE integrar o comando único de verificação de ADR-0023 §8, por depender do repositório `vince-docs`, que a verificação não busca.
20. A carga inicial DEVE ser idempotente, reconciliando por código de papel e de permissão, e NÃO DEVE alterar o identificador de registro já existente.
21. A carga inicial e a conferência de §18 DEVEM alcançar o módulo por método estático de `AccessModule`, e NÃO DEVEM ser acionadas por script residente fora de `src/`, que escaparia da análise estática de fronteiras de ADR-0007.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Dois módulos, `identity` e `authorization` | Isolamento superior, ao custo de transformar a resolução das permissões efetivas — caminho crítico de toda requisição autenticada — em travessia de fachada entre módulos, sem integridade referencial entre `user_role` e `role`. |
| Catálogo de permissões em `shared/` | ADR-0009 §5 proíbe acesso a dados de módulo em `shared/`, e ADR-0003 §15 determina que dado próprio resida em módulo. |
| `permission` como coluna de texto com restrição de verificação | Admitida por ADR-0018 §19, mas faria de cada permissão nova uma migração de esquema, e privaria `permission_grant` da chave estrangeira exigida por ADR-0018 §12. |
| Papéis administráveis por endpoint | Produziria permissão sem requisito funcional de origem, vedado por ADR-0014 §7; a URS §1.4 declara os papéis pré-criados. |
| Catálogo lido da URS em tempo de execução | Elimina a segunda cópia, mas põe o repositório de documentação no caminho crítico da aplicação e perde a verificação de tipo sobre os símbolos de permissão. |
| Conferência com a URS dentro do comando de verificação | Pegaria a divergência mais cedo, ao custo de acoplar o build do backend à disponibilidade de `vince-docs` a cada execução. |
| Módulo `access` autorizado a chamar a fachada de outro módulo | Todo módulo depende de `access`; qualquer dependência de volta fecha ciclo, cuja resolução ADR-0005 §6 já determina ser por evento. |

## Implicações

1. O módulo `access` concentra oito tabelas e é o módulo de maior superfície do sistema; crescimento além das tabelas de §5 é indício de fronteira mal recortada e DEVE motivar a reescrita deste ADR (ADR-0004, implicação 2).
2. Todo módulo passa a depender da fachada de `access`, que se torna ponto único de falha da autorização síncrona.
3. O catálogo declarado em código e o catálogo da URS são duas cópias do mesmo fato; a conferência de §18 é a única proteção contra sua divergência, e por §19 ela depende de execução deliberada na revisão.
4. A carga inicial passa a ser pré-requisito de qualquer ambiente utilizável: sem ela não existe papel, e sem papel não existe autorização concedida.
