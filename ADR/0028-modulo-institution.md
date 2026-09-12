# ADR-0028 — Módulo `institution`: a instituição como fronteira de isolamento

- **Status:** Aceito
- **Data:** 2026-09-02
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0011, ADR-0013, ADR-0014, ADR-0018, ADR-0025, ADR-0027

## Contexto

RF-INS-001 RN1 declara que curso, turma, evento, equipe, artigo e usuário pertencem a exatamente uma
instituição, mas nenhum módulo é dono desse conceito. Sem ele, a conta criada pelo módulo `access`
guarda identificador de instituição que não corresponde a registro algum, e RF-ACS-001 E3
(`INSTITUTION_INACTIVE`) não tem estado que a fundamente. ADR-0003 §12 exige que a criação de um
módulo seja precedida da declaração de sua capacidade e das tabelas sob sua propriedade.

## Decisão

### Capacidade e natureza

1. DEVE existir o módulo de negócio `institution`, cuja capacidade é a **instituição como fronteira de isolamento**: sua existência, seus dados de identificação, seu estado ativo ou inativo, e quem a administra.
2. O módulo `institution` NÃO DEVE possuir capacidade sobre identidade, credencial, papel ou permissão, que pertencem ao módulo `access` (ADR-0027 §1).
3. O módulo `institution` NÃO DEVE possuir capacidade sobre curso, turma, evento, equipe ou artigo; cada um pertence ao módulo que vier a ser declarado seu proprietário, e o vínculo com a instituição DEVE ser coluna de identificador, sem chave estrangeira (ADR-0018 §13).

### Propriedade de dados

4. O schema PostgreSQL do módulo DEVE chamar-se `institution` (ADR-0018 §1).
5. As tabelas sob propriedade do módulo `institution` DEVEM ser exclusivamente:

   | Tabela | Conteúdo |
   | :--- | :--- |
   | `institution` | a instituição, seus dados de identificação e seu estado |
   | `institution_admin` | o vínculo de administração entre uma conta de usuário e uma instituição |

6. Tabela não enumerada em §5 NÃO DEVE ser criada no schema `institution` sem a reescrita deste ADR.
7. Os dados de identificação de §5 DEVEM ser declarados em ponto único no módulo, e o acréscimo de dado obrigatório DEVE prever valor para as linhas existentes.
8. A referência de `institution_admin` à conta de usuário DEVE ser coluna de identificador indexada, sem chave estrangeira, por a conta pertencer ao módulo `access` (ADR-0006 §4, ADR-0018 §13, §14).

### Estado e seu efeito sobre o acesso

9. A instituição DEVE possuir estado ativo ou inativo. O estado é atributo de negócio da instituição, e não exclusão lógica: a instituição inativa continua a ser consultada e listada, distinguida pelo estado.
10. A desativação NÃO DEVE remover a instituição nem registro associado a ela, e DEVE ser aceita ainda que existam cursos ativos (RF-INS-001 E2).
11. A desativação e a reativação DEVEM ser idempotentes, e NÃO DEVEM ser alcançáveis pela operação de alteração dos dados da instituição.
12. O estado inativo DEVE zerar as permissões efetivas dos usuários vinculados à instituição, e NÃO DEVE encerrar sessão já estabelecida (ADR-0013 §18).
13. A composição entre as permissões efetivas do módulo `access` e o estado da instituição NÃO DEVE ser feita por chamada de um módulo ao outro; DEVE residir no composition root da aplicação, sobre port declarado em `shared/`, único arranjo compatível com §16 e com ADR-0009 §6.
14. A invalidação do cache de permissões de ADR-0014 §10 na desativação e na reativação DEVE ser feita por padrão de chave ou por versionamento, e NÃO DEVE iterar usuário a usuário com uma consulta por elemento (ADR-0011 §13).
15. A recusa de autenticação por instituição inativa DEVE ocorrer somente depois de a credencial ter sido verificada com sucesso, de modo a não tornar o código de resposta oráculo de existência de conta (RF-ACS-001 E1).

### Posição na dependência entre módulos

16. O módulo `institution` PODE depender da fachada do módulo `access`, e o módulo `access` NÃO DEVE depender da fachada do módulo `institution` (ADR-0027 §9).
17. A atribuição e a revogação do papel `INSTITUTION_ADMIN` DEVEM ser feitas pela fachada do módulo `access`, e NÃO DEVEM ser feitas por escrita em tabela do schema `access` (ADR-0006 §2).
18. A designação de administrador institucional NÃO DEVE constituir transação única entre os dois módulos (ADR-0005 §7). Ela DEVE atribuir o papel antes de gravar o vínculo, e ambas as etapas DEVEM ser idempotentes, de modo que a repetição da operação conclua a que ficou pela metade.
19. A revogação DEVE remover o papel `INSTITUTION_ADMIN` apenas quando não restar vínculo que o justifique, e DEVE preservá-lo quando restar (RF-INS-002 RN3).

### Superfície pública

20. A fachada `InstitutionFacade`, declarada em `contracts/`, DEVE ser a única superfície pública do módulo (ADR-0004 §1).
21. A fachada DEVE expor a consulta de existência e de estado de instituição por identificador, individual e em lote, e a consulta em lote DEVE executar em número de consultas ao banco independente da quantidade de identificadores informados (ADR-0011 §9).
22. A fachada NÃO DEVE expor operação de cadastro, de alteração ou de mudança de estado de instituição: são de uso administrativo e entram pela camada HTTP do módulo.
23. O identificador de instituição DEVE atravessar a fronteira do módulo como texto opaco, e NÃO DEVE atravessá-la como entidade de domínio nem como tipo gerado por ORM (ADR-0004 §9).

### Procedência do vínculo institucional

24. O identificador de instituição gravado por outro módulo DEVE provir de operação já validada pelo módulo `institution` — a emissão de um convite ou a carga inicial — e NÃO DEVE ser aceito como valor arbitrário submetido pelo cliente.
25. A validação de §24 é responsabilidade de quem fornece o identificador; o módulo `access` NÃO DEVE validá-lo, por §16.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| `institution` e `institution_admin` no schema `access` | Faria do módulo `access` proprietário do vínculo organizacional do ator, que ADR-0027 §2 já lhe nega, e ampliaria para onze tabelas o módulo que ADR-0027, implicação 1, aponta como de maior superfície do sistema. |
| Réplica local da instituição dentro do `access`, projetada de eventos | É a saída que ADR-0006 §6 a §8 preferem, e será a correta quando o outbox e o relay de ADR-0021 existirem. Hoje essa infraestrutura não existe, e construí-la apenas para validar um identificador seria desproporcional. |
| Módulo `access` autorizado a chamar a fachada de `institution` | Fecharia o ciclo de chamadas síncronas que ADR-0005 §6 proíbe e que ADR-0027 §9 evita ao fazer de `access` módulo folha. |
| Verificação do estado da instituição a cada requisição, na resolução da sessão | ADR-0013 §15 proíbe consulta ao banco relacional na resolução da sessão. |
| Encerramento das sessões dos usuários na desativação da instituição | ADR-0013 §18 proíbe módulo de invalidar sessão. O efeito prático é obtido por §12, ao custo declarado na implicação 3. |
| Composição de §13 em módulo de plataforma próprio | ADR-0003 §15 desautoriza módulo de plataforma sem dados próprios, e a composição não os tem. |
| Composição de §13 em `shared/` | ADR-0009 §6 impede `shared/` de importar de `modules/`, e a composição precisa dos dois `contracts/`. |
| Designação em saga com compensação | Desproporcional para duas escritas cuja repetição já converge, por §18. |
| Gravar o vínculo antes de atribuir o papel | Das duas falhas parciais possíveis, produziria a nociva: vínculo sem papel aparenta designação concluída e não autoriza nada. A ordem de §18 produz papel sem vínculo, que não autoriza nada porque ADR-0014 §12 obriga a verificação de titularidade dentro do caso de uso. |
| Papel `INSTITUTION_ADMIN` escopado à instituição | ADR-0027 §16 proíbe papel escopado a instituição, curso, turma ou evento; o escopo vem do vínculo de `institution_admin` (RF-INS-002 RN2). |
| Chave estrangeira de `institution_admin` para `access.user` | ADR-0006 §4 e ADR-0018 §13 vedam integridade referencial declarada entre módulos. |
| Remoção da instituição em vez de desativação | RF-INS-001 E2 aceita a desativação com cursos ativos; a remoção destruiria o acervo acadêmico que a instituição isola. |

## Implicações

1. O módulo `institution` é o primeiro a depender da fachada de outro módulo, e sua implementação é onde a regra de ADR-0027 §9 deixa de ser declaração e passa a ser exercida.
2. A composição de §13 estica ADR-0003 §10, que atribui ao composition root apenas a lista de módulos. Enquanto forem as duas composições de hoje — verificação de credencial e estado da instituição —, o custo é menor que o de um módulo de plataforma sem dados próprios; a terceira DEVE motivar a reescrita deste ADR.
3. A sessão do usuário de instituição desativada sobrevive à desativação, e por ADR-0017 §17 o `403` não a encerra no cliente. O usuário permanece em aplicação na qual nada funciona, em vez de ser levado à autenticação. O fecho correto depende de ADR-0021 e não existe até lá.
4. A conta deixa de ter sua instituição validada por quem a grava (§25); conta com vínculo para instituição inexistente passa a ser defeito do módulo emissor do convite, e é no teste dele que se verifica.
5. `INSTITUTION:CONSENT_AI` (RF-IAA-005) não é tratada por este ADR: o consentimento de uso de IA pertence à vertical de assistência automatizada, cujo teor e base legal a URS §3, item 12, registra como indefinidos.
