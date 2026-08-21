# URS — Especificação de Requisitos do Usuário

**Projeto:** VinceArt
**Versão:** 0.1
**Status:** Em elaboração — fatia estrutural registrada; fatia de correção pendente
**Data:** 2026-08-19

---

## 1. Objetivo

Este documento especifica **o que as partes interessadas do VinceArt precisam que o sistema faça**.

Todo item registrado aqui DEVE ter origem em parte interessada e DEVE ser rastreável até a evidência
que o originou. Decisão da equipe NÃO DEVE ser registrada nesta URS: o seu lugar é
[`Padroes/Padroes-de-Engenharia.md`](../Padroes/Padroes-de-Engenharia.md) ou um ADR em
[`ADR/`](../ADR/).

As regras de redação desta URS — identificação, prioridade, origem, rastreabilidade e estrutura do
requisito funcional — estão em `PAD-REQ-001` a `PAD-REQ-008`. Elas dizem **como** escrever um
requisito, nunca **qual** requisito escrever.

O material bruto de elicitação está em [`Coleta de Requisitos/`](Coleta%20de%20Requisitos/).

---

## 2. Escopo desta versão

Esta versão registra a **fatia estrutural** do sistema: identidade e acesso, hierarquia
institucional, evento acadêmico, formação de equipes e o artigo como entidade.

**Não está nesta versão**, e será registrado a seguir: o ciclo de correção — submissão de versões,
apontamentos, verificação de atendimento entre etapas, conformidade a normas e template,
acompanhamento de progresso e relatórios à coordenação.

**Fora do escopo do produto nesta fase**, por decisão registrada em §10: eventos científicos
externos e periódicos (radar de oportunidades), participação de um usuário em mais de uma
instituição e matrícula em mais de uma turma.

---

## 3. Convenções

### 3.1 Identificação

`RF-<CATEGORIA>-<NNN>`, numeração sequencial e imutável dentro da categoria (`PAD-REQ-002`).

| Categoria | Domínio |
| :--- | :--- |
| `ACS` | Acesso e identidade |
| `INS` | Instituição |
| `CUR` | Curso |
| `TUR` | Turma |
| `EVT` | Evento |
| `EQP` | Equipe |
| `ART` | Artigo |
| `INT` | Internacionalização |

Os códigos de categoria acompanham a convenção em português já adotada pelos identificadores
`PAD-*`. Isso não conflita com o padrão de nomeação em inglês: aquele rege **identificadores de
software** — código, tabela, coluna, rota, papel, permissão e código de resposta —, não os
identificadores de documento.

### 3.2 Prioridade

Escala `E` (essencial), `I` (importante), `D` (desejável).

Por `PAD-REQ-003`, a prioridade DEVE ser atribuída pela parte interessada. **Nenhuma prioridade
desta versão foi atribuída por parte interessada.** Os valores aqui registrados aparecem com o
sufixo **`(proposta)`** e são sugestão da equipe, sem valor de acordo, pendentes de ratificação —
ver §10, item 1.

### 3.3 Origem

| Código | Significado |
| :--- | :--- |
| `ELI` | Declarado por parte interessada na elicitação |
| `STK` | Imposto por parte interessada fora da elicitação |
| `DER` | Derivado; indica o item de origem e NÃO É considerado acordado antes de validação (`PAD-REQ-004`) |

### 3.4 Rastreio

| Sigla | Evidência |
| :--- | :--- |
| `M-P<n>` | Marciele R. Siveres, resposta à pergunta `<n>` — `Coleta de Requisitos/Requisitos Marciele.md` |
| `M-perfil` | Marciele, perfil do respondente |
| `A-P<n>` | Angélica P. S. Meurer, resposta à pergunta `<n>` — `Coleta de Requisitos/Requisitos Angélica.md` |
| `A-perfil` | Angélica, perfil do respondente |

---

## 4. Partes interessadas

| Parte interessada | Papel na elicitação | Estado |
| :--- | :--- | :--- |
| Marciele R. Siveres | Orientadora, Administração, 5 anos, ~35 orientandos simultâneos | Entrevistada |
| Angélica P. S. Meurer | Orientadora, Administração, 12 anos, 50+ orientandos por semestre | Entrevistada |
| Aluno orientando | Ator de grande parte dos requisitos | **Não entrevistado** — §10, item 5 |
| Coordenador de curso | Destinatário dos relatórios | **Não entrevistado** — §10, item 5 |

Ambas as entrevistadas pertencem ao curso de Administração. Não há evidência de outras áreas, o que
limita a generalização das normas exigidas — ver §10, item 6.

---

## 5. Atores e papéis

Os papéis são **globais e pré-criados por carga inicial**. O papel autoriza a ação; **o escopo vem
do vínculo**, verificado como titularidade dentro do caso de uso, conforme `ADR-0014` §12 e §13.
Não existe papel escopado.

| Papel | Identificador | Escopo obtido por |
| :--- | :--- | :--- |
| Administrador de Sistema | `SYSTEM_ADMIN` | Nenhum — atua sobre todas as instituições |
| Administrador Institucional | `INSTITUTION_ADMIN` | Designação a uma instituição |
| Coordenador | `COORDINATOR` | Designação a um curso |
| Professor | `PROFESSOR` | Designação a turmas e a eventos/equipes |
| Aluno | `STUDENT` | Matrícula em uma turma |

### 5.1 Premissas de identidade

1. O primeiro usuário `SYSTEM_ADMIN` é criado por script de carga inicial. Não existe autocadastro
   para esse papel nem para nenhum outro papel administrativo.
2. O e-mail é identificador único global do usuário. Quem atua em mais de uma instituição usa
   e-mails distintos, um por conta — consequência da decisão de §10, item 4.
3. O `SYSTEM_ADMIN` administra instituições e configurações gerais de suporte. **Não** acessa
   conteúdo acadêmico: artigo, apontamento, nota ou avaliação.

---

## 6. Modelo de domínio

```
Instituição
├── Curso                              INSTITUTION_ADMIN cria; designa COORDINATOR
│   └── Turma                          COORDINATOR cria; período letivo, data de início;
│       │                              designa PROFESSOR
│       └── Matrícula ── Aluno         PROFESSOR cadastra ou aluno ingressa por convite
└── Evento                             escopo: INSTITUICAO | CURSO | TURMA
    ├── tema, problema, objetivos       definidos pelo dono do escopo
    ├── limites de equipe               quantidade de equipes e tamanho máximo
    ├── cronograma de etapas            3 a 4 entregas com prazo, fixadas no início do período
    ├── orientadores do evento          podem ver e atuar sobre todas as equipes do evento
    └── Equipe ──1:1── Artigo           STARTED → IN_PROGRESS → IN_REVIEW → FINISHED
        └── orientador responsável      subconjunto dos orientadores do evento
```

### 6.1 Regras estruturais transversais

| ID | Regra |
| :--- | :--- |
| RE-01 | O criador de um evento é o dono do seu escopo: `PROFESSOR` para escopo de turma, `COORDINATOR` para escopo de curso, `INSTITUTION_ADMIN` para escopo de instituição. |
| RE-02 | A elegibilidade a um evento é automática por escopo: todos os professores e todos os alunos vinculados ao alvo do escopo são elegíveis. Não existe inscrição prévia. |
| RE-03 | Participar de um evento significa pertencer a uma equipe dele. Aluno elegível sem equipe não participa. |
| RE-04 | Um aluno pertence a no máximo uma equipe por evento e pode participar de eventos distintos simultaneamente. |
| RE-05 | Uma equipe possui exatamente um artigo. |
| RE-06 | Uma equipe pode reunir alunos de turmas e de cursos distintos quando o escopo do evento o permitir. |
| RE-07 | Um evento possui exatamente um tema nesta versão. Múltiplos temas por evento estão previstos como expansão. |
| RE-08 | O orientador possui dois vínculos de natureza distinta: com a **turma**, que autoriza cadastrar alunos e emitir convites; e com o **evento**, que autoriza orientar e avaliar. A designação a uma **equipe** nomeia o responsável direto por ela. |
| RE-09 | A nota é individual por aluno e existe também uma nota do artigo. |

---

## 7. Requisitos funcionais

### 7.1 ACS — Acesso e identidade

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-ACS-001 | Autenticar-se no sistema | E (proposta) | `DER` |
| RF-ACS-002 | Encerrar a sessão | E (proposta) | `DER` |
| RF-ACS-003 | Recuperar o acesso | E (proposta) | `DER` |
| RF-ACS-004 | Definir ou alterar a própria senha | E (proposta) | `DER` |
| RF-ACS-005 | Manter o próprio perfil | I (proposta) | `DER` |
| RF-ACS-006 | Conceder permissão a outro usuário | I (proposta) | `ELI` |
| RF-ACS-007 | Revogar concessão de permissão | I (proposta) | `DER` |
| RF-ACS-008 | Consultar concessões diretas ativas | D (proposta) | `DER` |

---

#### RF-ACS-001 — Autenticar-se no sistema

- **Descrição:** permite ao usuário estabelecer sessão autenticada mediante e-mail e senha, para
  acessar as funcionalidades correspondentes aos seus papéis e vínculos.
- **Ator:** Usuário
- **Pré-condições:** conta ativa; instituição do usuário ativa.
- **Fluxo principal:**
  1. O ator informa e-mail e senha.
  2. O sistema verifica a credencial.
  3. O sistema estabelece a sessão e devolve a identidade do usuário e suas permissões efetivas.
- **Fluxos alternativos e de exceção:**
  - E1. Credencial inválida ou conta inexistente → `AUTHENTICATION_FAILED`, sem distinguir qual dos
    dois ocorreu.
  - E2. Conta desativada → `AUTHENTICATION_FAILED`.
  - E3. Instituição do usuário desativada → `INSTITUTION_INACTIVE`.
  - E4. Senha ainda não definida (conta criada por professor ou por convite) → o sistema conduz ao
    fluxo de `RF-ACS-004`.
- **Regras de negócio:**
  - RN1. O e-mail é identificador único global.
  - RN2. As permissões efetivas são a união das concedidas pelos papéis e das concessões diretas
    ativas, resolvidas a cada requisição.
  - RN3. As permissões devolvidas ao cliente destinam-se à composição da interface e não substituem
    a verificação no servidor.
- **Permissões geradas:** — (acesso público)
- **Escopo de titularidade:** —
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de A-P8 e M-P8, que definem quem pode ver o trabalho em cada fase; a
  restrição de acesso pressupõe identidade verificada.
- **Critério de aceitação:** usuário com credencial válida obtém sessão e recebe suas permissões
  efetivas; credencial inválida e conta inexistente produzem resposta indistinguível.
- **Rastreio:** A-P8; M-P8; `ADR-0013`.

#### RF-ACS-002 — Encerrar a sessão

- **Descrição:** permite ao usuário encerrar a própria sessão, tornando a credencial inválida
  imediatamente.
- **Ator:** Usuário autenticado
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator solicita o encerramento.
  2. O sistema invalida a sessão e descarta a credencial do cliente.
- **Fluxos alternativos e de exceção:**
  - E1. Sessão já expirada → a operação é idempotente e conclui com sucesso.
- **Regras de negócio:**
  - RN1. O encerramento afeta apenas a sessão corrente.
- **Permissões geradas:** — (própria sessão)
- **Escopo de titularidade:** restrito à sessão do próprio ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-ACS-001`.
- **Critério de aceitação:** após o encerramento, requisição com a credencial anterior é recusada.
- **Rastreio:** `RF-ACS-001`; `ADR-0013`.

#### RF-ACS-003 — Recuperar o acesso

- **Descrição:** permite ao usuário que perdeu a senha solicitar, pelo próprio e-mail, um meio de
  redefini-la.
- **Ator:** Usuário
- **Pré-condições:** nenhuma.
- **Fluxo principal:**
  1. O ator informa o e-mail.
  2. O sistema envia mensagem contendo meio de redefinição com prazo de validade.
  3. O ator conclui a redefinição por `RF-ACS-004`.
- **Fluxos alternativos e de exceção:**
  - E1. E-mail não cadastrado → a resposta é idêntica à do caso de sucesso, para não revelar a
    existência da conta.
  - E2. Meio de redefinição expirado ou já utilizado → `INVITATION_EXPIRED`.
- **Regras de negócio:**
  - RN1. O meio de redefinição é de uso único e possui prazo de validade.
  - RN2. A resposta não revela se o e-mail existe.
- **Permissões geradas:** — (acesso público)
- **Escopo de titularidade:** —
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-ACS-001`.
- **Critério de aceitação:** e-mail cadastrado recebe o meio de redefinição; e-mail não cadastrado
  produz resposta indistinguível da de sucesso.
- **Rastreio:** `RF-ACS-001`.

#### RF-ACS-004 — Definir ou alterar a própria senha

- **Descrição:** permite ao usuário definir a senha na primeira entrada ou alterá-la posteriormente.
- **Ator:** Usuário
- **Pré-condições:** possuir meio de redefinição válido ou sessão ativa.
- **Fluxo principal:**
  1. O ator informa a nova senha.
  2. O sistema valida a política de senha e a registra.
  3. O sistema encerra as demais sessões do usuário.
- **Fluxos alternativos e de exceção:**
  - E1. Senha fora da política → `VALIDATION_FAILED`.
  - E2. Alteração por usuário autenticado sem informar a senha atual → `VALIDATION_FAILED`.
  - E3. Meio de redefinição expirado → `INVITATION_EXPIRED`.
- **Regras de negócio:**
  - RN1. A alteração por usuário autenticado exige a senha atual; a definição por meio de
    redefinição, não.
  - RN2. Concluída a operação, as demais sessões do usuário são encerradas.
- **Permissões geradas:** — (própria conta)
- **Escopo de titularidade:** restrito à conta do próprio ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-ACS-001` e `RF-ACS-003`.
- **Critério de aceitação:** senha alterada passa a ser exigida na entrada seguinte e as sessões
  anteriores deixam de ser aceitas.
- **Rastreio:** `RF-ACS-001`; `RF-ACS-003`.

#### RF-ACS-005 — Manter o próprio perfil

- **Descrição:** permite ao usuário consultar e atualizar os próprios dados de identificação e a
  área de atuação ou pesquisa.
- **Ator:** Usuário autenticado
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator consulta o próprio perfil.
  2. O ator altera nome, área de atuação ou pesquisa e preferência de idioma.
  3. O sistema registra a alteração.
- **Fluxos alternativos e de exceção:**
  - E1. Dado obrigatório ausente ou inválido → `VALIDATION_FAILED`.
  - E2. Tentativa de alterar o próprio e-mail, papéis ou vínculos → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. E-mail, papéis e vínculos não são editáveis pelo próprio usuário.
  - RN2. A área de atuação ou pesquisa é registrada no perfil do professor.
- **Permissões geradas:** — (próprio perfil)
- **Escopo de titularidade:** restrito ao registro do próprio ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — deriva do perfil do respondente coletado na elicitação (nome, curso, área de
  atuação ou pesquisa, tempo de experiência).
- **Critério de aceitação:** alteração de nome e área persiste e é refletida nas consultas; tentativa
  de alterar e-mail ou papéis é recusada.
- **Rastreio:** M-perfil; A-perfil.

#### RF-ACS-006 — Conceder permissão a outro usuário

- **Descrição:** permite a um usuário conceder a outro uma permissão que ele próprio possui, para
  que um professor assuma temporariamente atribuições de outro em período de sobrecarga.
- **Ator:** Usuário autenticado com a permissão de concessão
- **Pré-condições:** concedente e beneficiário ativos; concedente possui a permissão a conceder.
- **Fluxo principal:**
  1. O ator seleciona o beneficiário e a permissão.
  2. O ator informa, opcionalmente, prazo de validade da concessão.
  3. O sistema verifica que a permissão pertence às permissões efetivas do concedente.
  4. O sistema registra a concessão e a trilha de auditoria.
- **Fluxos alternativos e de exceção:**
  - E1. Permissão não pertence ao concedente → `GRANT_NOT_HELD_BY_GRANTER`.
  - E2. Concedente e beneficiário são o mesmo usuário → `SELF_GRANT_NOT_ALLOWED`.
  - E3. Beneficiário inexistente ou inativo → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. Ninguém concede permissão a si mesmo.
  - RN2. A concessão pode ter prazo de validade; expirada, deixa de compor as permissões efetivas.
  - RN3. A revogação da permissão do concedente não revoga as concessões que ele realizou.
  - RN4. Toda concessão é registrada em trilha de auditoria imutável com concedente, beneficiário,
    permissão e instante.
- **Permissões geradas:** `PERMISSION_GRANT:CREATE`
- **Escopo de titularidade:** restrito às permissões efetivas do próprio ator.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Marciele descreve a força-tarefa entre professores para socorrer trabalhos
  próximos ao prazo, que exige que um orientador atue sobre trabalho de outro.
- **Critério de aceitação:** usuário concede permissão que possui e o beneficiário passa a exercê-la;
  tentativa de conceder permissão não possuída é recusada.
- **Rastreio:** M-P3; M-P1 (acesso compartilhado entre orientadores); `ADR-0014` §15–§19.

#### RF-ACS-007 — Revogar concessão de permissão

- **Descrição:** permite revogar, a qualquer momento, uma concessão direta ativa, independentemente
  de quem a concedeu.
- **Ator:** Usuário autenticado com a permissão de revogação
- **Pré-condições:** concessão direta ativa.
- **Fluxo principal:**
  1. O ator localiza a concessão ativa.
  2. O ator solicita a revogação.
  3. O sistema encerra a concessão e registra a trilha de auditoria.
- **Fluxos alternativos e de exceção:**
  - E1. Concessão inexistente ou já encerrada → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. A revogação é possível por qualquer usuário que possua a permissão de revogação, mesmo não
    tendo sido o concedente.
  - RN2. A revogação surte efeito imediato sobre as permissões efetivas do beneficiário.
- **Permissões geradas:** `PERMISSION_GRANT:REVOKE`
- **Escopo de titularidade:** —
- **Prioridade:** I (proposta)
- **Origem:** `DER` — deriva de `RF-ACS-006`.
- **Critério de aceitação:** revogada a concessão, a requisição seguinte do beneficiário que dependa
  dela é recusada.
- **Rastreio:** `RF-ACS-006`; `ADR-0014` §21.

#### RF-ACS-008 — Consultar concessões diretas ativas

- **Descrição:** permite listar as concessões diretas ativas de um usuário, com concedente e data,
  para revisão periódica de privilégios.
- **Ator:** Usuário autenticado com a permissão de leitura de concessões
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator seleciona o usuário a revisar.
  2. O sistema lista as concessões ativas com permissão, concedente e data de concessão.
- **Fluxos alternativos e de exceção:**
  - E1. Usuário inexistente → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. Concessões expiradas não constam da lista de ativas.
- **Permissões geradas:** `PERMISSION_GRANT:READ`
- **Escopo de titularidade:** —
- **Prioridade:** D (proposta)
- **Origem:** `DER` — deriva de `RF-ACS-006`.
- **Critério de aceitação:** a lista apresenta toda concessão ativa com seu concedente e nenhuma
  concessão expirada.
- **Rastreio:** `RF-ACS-006`; `ADR-0014` §20.

---

### 7.2 INS — Instituição

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-INS-001 | Manter instituição | E (proposta) | `DER` |
| RF-INS-002 | Designar administrador institucional | E (proposta) | `DER` |

---

#### RF-INS-001 — Manter instituição

- **Descrição:** permite ao administrador de sistema cadastrar, consultar, alterar e desativar
  instituições, além de manter as suas configurações gerais de suporte.
- **Ator:** Administrador de Sistema
- **Pré-condições:** sessão ativa com o papel `SYSTEM_ADMIN`.
- **Fluxo principal:**
  1. O ator informa nome e dados de identificação da instituição.
  2. O sistema registra a instituição em estado ativo.
  3. O ator consulta, altera ou desativa a instituição quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Dado obrigatório ausente → `VALIDATION_FAILED`.
  - E2. Desativação de instituição com cursos ativos → a operação é aceita e a desativação se propaga
    ao acesso dos seus usuários, conforme RN2.
- **Regras de negócio:**
  - RN1. A instituição é a fronteira de isolamento dos dados: todo curso, turma, evento, equipe,
    artigo e usuário pertence a exatamente uma instituição.
  - RN2. Usuário de instituição desativada não autentica (`INSTITUTION_INACTIVE`).
  - RN3. O `SYSTEM_ADMIN` não acessa conteúdo acadêmico: artigo, apontamento, nota ou avaliação.
- **Permissões geradas:** `INSTITUTION:CREATE`, `INSTITUTION:READ`, `INSTITUTION:UPDATE`,
  `INSTITUTION:DEACTIVATE`
- **Escopo de titularidade:** —
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de M-P5 e M-P9, que situam o trabalho dentro de uma instituição com
  congresso interno e coordenação própria.
- **Critério de aceitação:** instituição cadastrada passa a admitir cursos; instituição desativada
  impede a autenticação dos seus usuários.
- **Rastreio:** M-P5; M-P9; A-P1; decisão de escopo de §10, item 4.

#### RF-INS-002 — Designar administrador institucional

- **Descrição:** permite ao administrador de sistema atribuir a um usuário o papel de administrador
  de uma instituição, e revogar essa atribuição.
- **Ator:** Administrador de Sistema
- **Pré-condições:** instituição ativa; usuário beneficiário ativo.
- **Fluxo principal:**
  1. O ator seleciona a instituição e o usuário.
  2. O sistema atribui o papel `INSTITUTION_ADMIN` ao usuário e cria o vínculo com a instituição.
  3. O sistema registra a operação em trilha de auditoria.
- **Fluxos alternativos e de exceção:**
  - E1. Usuário já é administrador dessa instituição → a operação é idempotente.
  - E2. Instituição inativa → `INSTITUTION_INACTIVE`.
  - E3. Usuário inexistente → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. Uma instituição admite mais de um administrador institucional ativo.
  - RN2. O papel é global; o escopo decorre do vínculo com a instituição.
  - RN3. A revogação do vínculo remove o papel quando não houver outro vínculo que o justifique.
- **Permissões geradas:** `INSTITUTION:ASSIGN_ADMIN`, `INSTITUTION:REVOKE_ADMIN`
- **Escopo de titularidade:** —
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-INS-001` e da cadeia de criação de usuários definida para o
  produto.
- **Critério de aceitação:** designado, o usuário passa a criar cursos naquela instituição e em
  nenhuma outra.
- **Rastreio:** `RF-INS-001`; §10, item 2.

---

### 7.3 CUR — Curso

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-CUR-001 | Manter curso | E (proposta) | `DER` |
| RF-CUR-002 | Designar coordenador do curso | E (proposta) | `ELI` |

---

#### RF-CUR-001 — Manter curso

- **Descrição:** permite ao administrador institucional cadastrar, consultar, alterar e desativar os
  cursos da sua instituição.
- **Ator:** Administrador Institucional
- **Pré-condições:** instituição ativa; ator vinculado a ela.
- **Fluxo principal:**
  1. O ator informa nome e identificação do curso.
  2. O sistema registra o curso, vinculado à instituição do ator, em estado ativo.
  3. O ator consulta, altera ou desativa o curso quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Dado obrigatório ausente → `VALIDATION_FAILED`.
  - E2. Curso de outra instituição → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. O curso pertence a exatamente uma instituição.
  - RN2. Curso desativado não admite novas turmas nem novos eventos.
- **Permissões geradas:** `COURSE:CREATE`, `COURSE:READ`, `COURSE:UPDATE`, `COURSE:DEACTIVATE`
- **Escopo de titularidade:** restrito aos cursos da instituição à qual o ator está vinculado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de M-perfil e A-perfil, que identificam o curso como unidade de
  organização da orientação, e de M-P9, cujo relatório é prestado à coordenação do curso.
- **Critério de aceitação:** curso criado admite turmas; administrador de outra instituição não o
  enxerga.
- **Rastreio:** M-perfil; A-perfil; M-P9.

#### RF-CUR-002 — Designar coordenador do curso

- **Descrição:** permite ao administrador institucional atribuir a um usuário o papel de coordenador
  de um curso, e revogar essa atribuição.
- **Ator:** Administrador Institucional
- **Pré-condições:** curso ativo na instituição do ator; usuário beneficiário ativo.
- **Fluxo principal:**
  1. O ator seleciona o curso e o usuário.
  2. O sistema atribui o papel `COORDINATOR` e cria o vínculo com o curso.
  3. O sistema registra a operação em trilha de auditoria.
- **Fluxos alternativos e de exceção:**
  - E1. Curso já possui coordenador ativo → `COORDINATOR_ALREADY_ASSIGNED`.
  - E2. Curso de outra instituição → `PERMISSION_DENIED`.
  - E3. Usuário inexistente → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. O curso possui no máximo um coordenador ativo por vez — premissa a confirmar, §10, item 7.
  - RN2. O coordenador do curso é o destinatário dos relatórios de pesquisa; não existe papel
    separado de coordenador de pesquisa.
  - RN3. A revogação do vínculo não revoga as concessões diretas realizadas pelo coordenador.
- **Permissões geradas:** `COURSE:ASSIGN_COORDINATOR`, `COURSE:REVOKE_COORDINATOR`
- **Escopo de titularidade:** restrito aos cursos da instituição à qual o ator está vinculado.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Marciele identifica o coordenador como destinatário do relatório de
  orientações e publicações.
- **Critério de aceitação:** designado, o usuário cria turmas naquele curso e em nenhum outro.
- **Rastreio:** M-P9; `ADR-0014` §17.

---

### 7.4 TUR — Turma

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-TUR-001 | Manter turma | E (proposta) | `ELI` |
| RF-TUR-002 | Designar professor à turma | E (proposta) | `ELI` |
| RF-TUR-003 | Cadastrar aluno na turma | E (proposta) | `DER` |
| RF-TUR-004 | Emitir convite de ingresso na turma | E (proposta) | `DER` |
| RF-TUR-005 | Ingressar na turma por convite | E (proposta) | `DER` |

---

#### RF-TUR-001 — Manter turma

- **Descrição:** permite ao coordenador cadastrar, consultar, alterar e desativar turmas do seu
  curso, delimitando o período letivo em que a orientação ocorre.
- **Ator:** Coordenador
- **Pré-condições:** curso ativo; ator designado a esse curso.
- **Fluxo principal:**
  1. O ator informa identificação da turma, período letivo, data de início e data de término.
  2. O sistema registra a turma vinculada ao curso, em estado ativo.
  3. O ator consulta, altera ou desativa a turma quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Data de término anterior à de início → `VALIDATION_FAILED`.
  - E2. Turma de curso ao qual o ator não está designado → `PERMISSION_DENIED`.
  - E3. Curso desativado → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. A turma pertence a exatamente um curso e carrega o período letivo, sem o qual não é possível
    consolidar por semestre os relatórios à coordenação.
  - RN2. A identificação da turma deve ser única dentro do curso e do período letivo.
- **Permissões geradas:** `COHORT:CREATE`, `COHORT:READ`, `COHORT:UPDATE`, `COHORT:DEACTIVATE`
- **Escopo de titularidade:** restrito aos cursos aos quais o ator está designado.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas descrevem a orientação organizada por semestre, com formalização das
  atividades e datas no início do período.
- **Critério de aceitação:** turma criada com período letivo admite professores e alunos; coordenador
  de outro curso não a enxerga.
- **Rastreio:** A-P1; A-P3; M-P1; M-P9.

#### RF-TUR-002 — Designar professor à turma

- **Descrição:** permite ao coordenador designar professores a uma turma do seu curso, e revogar a
  designação.
- **Ator:** Coordenador
- **Pré-condições:** turma ativa em curso ao qual o ator está designado; usuário beneficiário ativo.
- **Fluxo principal:**
  1. O ator seleciona a turma e o usuário.
  2. O sistema atribui o papel `PROFESSOR` e cria o vínculo com a turma.
  3. O sistema registra a operação em trilha de auditoria.
- **Fluxos alternativos e de exceção:**
  - E1. Professor já designado à turma → a operação é idempotente.
  - E2. Turma de curso ao qual o ator não está designado → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. Uma turma admite mais de um professor designado.
  - RN2. O vínculo com a turma autoriza cadastrar alunos e emitir convites; não autoriza, por si só,
    orientar ou avaliar — isso decorre do vínculo com o evento (RE-08).
- **Permissões geradas:** `COHORT:ASSIGN_PROFESSOR`, `COHORT:REVOKE_PROFESSOR`
- **Escopo de titularidade:** restrito aos cursos aos quais o ator está designado.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica registra três professores atuando conjuntamente sobre a mesma
  população de alunos, o que exige mais de um professor por turma.
- **Critério de aceitação:** designado, o professor cadastra alunos naquela turma e em nenhuma outra.
- **Rastreio:** A-perfil; A-P1; M-P1.

#### RF-TUR-003 — Cadastrar aluno na turma

- **Descrição:** permite ao professor registrar um aluno e matriculá-lo na turma, criando a conta
  quando o e-mail ainda não existir no sistema.
- **Ator:** Professor
- **Pré-condições:** turma ativa; ator designado a essa turma.
- **Fluxo principal:**
  1. O ator informa nome e e-mail do aluno.
  2. O sistema cria o usuário com o papel `STUDENT`, quando o e-mail ainda não existir.
  3. O sistema cria a matrícula do aluno na turma, em situação ativa.
  4. O sistema envia ao aluno a mensagem de definição de senha (`RF-ACS-004`).
- **Fluxos alternativos e de exceção:**
  - E1. E-mail já cadastrado no sistema → `EMAIL_ALREADY_REGISTERED`.
  - E2. Aluno já possui matrícula ativa → `STUDENT_ALREADY_ENROLLED`.
  - E3. Turma inativa ou ator não designado a ela → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. **A matrícula é entidade própria** (`Enrollment`: aluno, turma, situação), nunca coluna no
    registro do usuário. Nesta versão o aluno possui no máximo uma matrícula ativa; a expansão para
    múltiplas turmas será a remoção dessa restrição, sem migração de dados, e o histórico
    multissemestral exigido pelos relatórios já nasce apoiado nessa entidade.
  - RN2. O e-mail é identificador único global; quem atua em mais de uma instituição usa e-mails
    distintos.
  - RN3. A conta criada por este fluxo nasce sem senha definida.
- **Permissões geradas:** `ENROLLMENT:CREATE`, `ENROLLMENT:READ`
- **Escopo de titularidade:** restrito às turmas às quais o ator está designado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de A-P1 e M-P1, que descrevem a formalização da turma e das atividades
  do semestre pelo professor.
- **Critério de aceitação:** professor designado cadastra aluno inexistente e ele passa a constar na
  turma com matrícula ativa; professor não designado é recusado.
- **Rastreio:** A-P1; M-P1; §10, item 4.

#### RF-TUR-004 — Emitir convite de ingresso na turma

- **Descrição:** permite ao professor gerar um convite de ingresso na turma, para que os alunos criem
  a própria conta em vez de serem cadastrados um a um.
- **Ator:** Professor
- **Pré-condições:** turma ativa; ator designado a essa turma.
- **Fluxo principal:**
  1. O ator solicita o convite para a turma.
  2. O ator informa o prazo de validade.
  3. O sistema gera o convite e devolve o endereço de ingresso.
  4. O ator consulta ou revoga convites emitidos.
- **Fluxos alternativos e de exceção:**
  - E1. Turma inativa ou ator não designado → `PERMISSION_DENIED`.
  - E2. Prazo de validade ausente ou no passado → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. O convite é de uso múltiplo e vinculado a uma única turma.
  - RN2. O convite possui prazo de validade obrigatório e pode ser revogado a qualquer momento.
  - RN3. O convite concede exclusivamente o papel `STUDENT` e a matrícula na turma a que se refere.
- **Permissões geradas:** `INVITATION:CREATE`, `INVITATION:READ`, `INVITATION:REVOKE`
- **Escopo de titularidade:** restrito às turmas às quais o ator está designado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de A-perfil e M-perfil: o volume de orientandos por professor torna
  inviável o cadastro individual, que agravaria a falta de tempo relatada como dor principal.
- **Critério de aceitação:** convite válido conduz ao ingresso; convite revogado ou expirado é
  recusado.
- **Rastreio:** A-perfil; A-P2; M-perfil; M-P2.

#### RF-TUR-005 — Ingressar na turma por convite

- **Descrição:** permite ao aluno criar a própria conta e matricular-se na turma a partir do convite
  recebido.
- **Ator:** Visitante
- **Pré-condições:** possuir convite válido.
- **Fluxo principal:**
  1. O ator acessa o endereço do convite.
  2. O ator informa nome, e-mail e senha.
  3. O sistema cria a conta com o papel `STUDENT`.
  4. O sistema cria a matrícula na turma indicada pelo convite.
- **Fluxos alternativos e de exceção:**
  - E1. Convite expirado → `INVITATION_EXPIRED`.
  - E2. Convite revogado → `INVITATION_REVOKED`.
  - E3. E-mail já cadastrado → `EMAIL_ALREADY_REGISTERED`.
  - E4. Já existe matrícula ativa para esse aluno → `STUDENT_ALREADY_ENROLLED`.
  - E5. Senha fora da política → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. O ingresso por convite não permite escolher papel nem turma: ambos vêm do convite.
  - RN2. Aplica-se a RN1 de `RF-TUR-003` quanto à matrícula como entidade própria.
- **Permissões geradas:** — (acesso público mediante convite)
- **Escopo de titularidade:** —
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-TUR-004`.
- **Critério de aceitação:** o portador de convite válido conclui o ingresso e passa a constar na
  turma; convite inválido não cria conta alguma.
- **Rastreio:** `RF-TUR-004`.

---

### 7.5 EVT — Evento

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-EVT-001 | Manter evento | E (proposta) | `ELI` |
| RF-EVT-002 | Definir o cronograma de etapas do evento | E (proposta) | `ELI` |
| RF-EVT-003 | Designar orientadores ao evento | E (proposta) | `ELI` |
| RF-EVT-004 | Consultar eventos por escopo | E (proposta) | `DER` |

---

#### RF-EVT-001 — Manter evento

- **Descrição:** permite ao dono do escopo criar, consultar, alterar e cancelar um evento acadêmico,
  definindo o tema, o problema de pesquisa, os objetivos e os limites de formação de equipes. O
  evento é a unidade que organiza a produção dos artigos do período.
- **Ator:** Professor, Coordenador ou Administrador Institucional, conforme o escopo
- **Pré-condições:** ator vinculado ao alvo do escopo pretendido.
- **Fluxo principal:**
  1. O ator seleciona o escopo — turma, curso ou instituição — e o alvo correspondente.
  2. O ator informa título, tema, problema de pesquisa e objetivos.
  3. O ator informa a quantidade máxima de equipes e o tamanho máximo da equipe.
  4. O sistema registra o evento e torna elegíveis todos os professores e alunos do alvo do escopo.
  5. O ator consulta, altera ou cancela o evento quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Escopo superior ao vínculo do ator → `EVENT_SCOPE_NOT_ALLOWED`.
  - E2. Alvo do escopo inexistente ou inativo → `RESOURCE_NOT_FOUND`.
  - E3. Limite de equipes ou tamanho de equipe ausente ou não positivo → `VALIDATION_FAILED`.
  - E4. Alteração dos limites para valor inferior ao já utilizado → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. O criador é o dono do escopo, conforme RE-01, e é ele quem define o tema.
  - RN2. A elegibilidade é automática por escopo, conforme RE-02; não existe inscrição prévia.
  - RN3. O evento possui exatamente um tema nesta versão (RE-07).
  - RN4. Os limites de quantidade de equipes e de tamanho da equipe são definidos por evento.
  - RN5. O evento pertence à instituição do seu alvo de escopo.
- **Permissões geradas:** `EVENT:CREATE`, `EVENT:READ`, `EVENT:UPDATE`, `EVENT:CANCEL`
- **Escopo de titularidade:** restrito ao alvo ao qual o ator está vinculado — sua turma, seu curso
  ou sua instituição, conforme o papel.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas descrevem a produção de artigos organizada por período, com tema,
  problema e objetivos definidos pelo professor e com o congresso interno como destino.
- **Critério de aceitação:** professor cria evento de escopo de turma e é recusado ao tentar escopo
  de curso; criado o evento, os alunos do alvo passam a poder formar equipes nele.
- **Rastreio:** A-P1 (tema, problema e objetivos definidos pelo professor); M-P1; M-P5 (template do
  congresso interno).

#### RF-EVT-002 — Definir o cronograma de etapas do evento

- **Descrição:** permite ao dono do escopo definir as etapas de entrega do evento, com nome, ordem e
  prazo, fixando o calendário no início do período.
- **Ator:** Professor, Coordenador ou Administrador Institucional, conforme o escopo
- **Pré-condições:** evento ativo; ator é o dono do seu escopo.
- **Fluxo principal:**
  1. O ator informa, para cada etapa, nome, ordem e data de entrega.
  2. O sistema valida a sequência e registra o cronograma.
  3. O ator altera ou remove etapas quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Datas fora de ordem crescente em relação à sequência das etapas → `MILESTONE_DATE_CONFLICT`.
  - E2. Remoção de etapa já iniciada → `VALIDATION_FAILED`.
  - E3. Ator não é dono do escopo do evento → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. O cronograma pertence ao evento, o que padroniza os prazos de todas as suas equipes desde o
    início do período.
  - RN2. As datas devem crescer estritamente conforme a ordem das etapas.
  - RN3. A etapa é a unidade à qual se prendem as versões e os apontamentos do ciclo de correção,
    especificado em versão posterior desta URS.
- **Permissões geradas:** `MILESTONE:CREATE`, `MILESTONE:READ`, `MILESTONE:UPDATE`,
  `MILESTONE:DELETE`
- **Escopo de titularidade:** restrito aos eventos de cujo escopo o ator é dono.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica declara que o cronograma de entregas é definido no início do semestre;
  Marciele registra de três a quatro etapas de entrega por período.
- **Critério de aceitação:** cronograma com etapas em ordem crescente é aceito; etapa com data
  anterior à da etapa precedente é recusada.
- **Rastreio:** A-P1; A-P3; M-P1; M-P2.

#### RF-EVT-003 — Designar orientadores ao evento

- **Descrição:** permite ao dono do escopo designar os professores que orientarão no evento, e
  revogar a designação.
- **Ator:** Professor, Coordenador ou Administrador Institucional, conforme o escopo
- **Pré-condições:** evento ativo; ator é o dono do seu escopo; professor elegível pelo escopo.
- **Fluxo principal:**
  1. O ator seleciona o evento e o professor.
  2. O sistema verifica a elegibilidade do professor pelo escopo do evento.
  3. O sistema registra a designação.
- **Fluxos alternativos e de exceção:**
  - E1. Professor não elegível pelo escopo do evento → `STUDENT_NOT_ELIGIBLE`.
  - E2. Ator não é dono do escopo → `PERMISSION_DENIED`.
  - E3. Professor já designado → a operação é idempotente.
- **Regras de negócio:**
  - RN1. Um evento admite mais de um orientador.
  - RN2. O orientador do evento pode ver e atuar sobre todas as equipes e artigos do evento,
    independentemente de ser o responsável direto por elas.
  - RN3. A designação a uma equipe específica (`RF-EQP-005`) nomeia o responsável direto e não
    restringe o alcance dos demais orientadores do evento.
- **Permissões geradas:** `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`
- **Escopo de titularidade:** restrito aos eventos de cujo escopo o ator é dono.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica registra três professores orientando conjuntamente; Marciele mantém a
  planilha compartilhada justamente para que qualquer professor envolvido possa atender o aluno.
- **Critério de aceitação:** designado ao evento, o professor enxerga todas as suas equipes;
  professor não designado não enxerga nenhuma.
- **Rastreio:** A-perfil; A-P1; M-P1; M-P3.

#### RF-EVT-004 — Consultar eventos por escopo

- **Descrição:** permite ao usuário localizar os eventos aos quais tem acesso, organizados por
  escopo — instituição, curso e turma.
- **Ator:** Usuário autenticado
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator abre a consulta de eventos.
  2. O sistema apresenta os eventos agrupados por escopo, restritos aos vínculos do ator.
  3. O ator seleciona um evento e consulta o seu tema, cronograma e equipes.
- **Fluxos alternativos e de exceção:**
  - E1. Evento fora dos vínculos do ator → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. O aluno enxerga os eventos em que é elegível; o professor, aqueles em que é orientador ou
    dono do escopo; o coordenador, os do seu curso; o administrador institucional, os da sua
    instituição.
  - RN2. Esta regra implementa a posição de acesso restrito e não a de abertura institucional
    ampla — divergência registrada em §10, item 8.
- **Permissões geradas:** `EVENT:READ`
- **Escopo de titularidade:** restrito aos eventos alcançados pelos vínculos do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-EVT-001` e da decisão de apresentar os eventos organizados por
  escopo.
- **Critério de aceitação:** cada perfil vê exatamente os eventos alcançados pelos seus vínculos, e
  nenhum outro.
- **Rastreio:** `RF-EVT-001`; A-P8; M-P8.

---

### 7.6 EQP — Equipe

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-EQP-001 | Criar equipe no evento | E (proposta) | `ELI` |
| RF-EQP-002 | Ingressar em equipe | E (proposta) | `ELI` |
| RF-EQP-003 | Designar aluno a equipe | E (proposta) | `ELI` |
| RF-EQP-004 | Convidar aluno para a equipe | I (proposta) | `DER` |
| RF-EQP-005 | Designar orientador responsável pela equipe | E (proposta) | `ELI` |
| RF-EQP-006 | Consultar alunos elegíveis sem equipe | I (proposta) | `ELI` |

---

#### RF-EQP-001 — Criar equipe no evento

- **Descrição:** permite ao orientador criar equipes no evento, respeitando a quantidade máxima
  definida para ele.
- **Ator:** Professor orientador do evento
- **Pré-condições:** evento ativo; ator designado como orientador do evento.
- **Fluxo principal:**
  1. O ator informa a identificação da equipe.
  2. O sistema verifica o limite de equipes do evento.
  3. O sistema cria a equipe e o seu artigo, no estado `STARTED`.
- **Fluxos alternativos e de exceção:**
  - E1. Limite de equipes do evento atingido → `EVENT_TEAM_LIMIT_REACHED`.
  - E2. Ator não é orientador do evento → `ADVISOR_NOT_ASSIGNED_TO_EVENT`.
  - E3. Evento cancelado → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. A criação da equipe cria o seu artigo, na proporção de um para um (RE-05).
  - RN2. A quantidade de equipes não excede o limite definido no evento.
- **Permissões geradas:** `TEAM:CREATE`
- **Escopo de titularidade:** restrito aos eventos em que o ator é orientador.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas descrevem o trabalho realizado por equipes formadas dentro do período.
- **Critério de aceitação:** criada a equipe, existe um artigo associado a ela em estado `STARTED`;
  criação além do limite do evento é recusada.
- **Rastreio:** A-P1; A-perfil; M-P1.

#### RF-EQP-002 — Ingressar em equipe

- **Descrição:** permite ao aluno elegível ingressar por conta própria em uma equipe do evento,
  preservando a autonomia de escolha dos colegas que hoje existe no processo.
- **Ator:** Aluno
- **Pré-condições:** aluno elegível pelo escopo do evento; equipe com vaga.
- **Fluxo principal:**
  1. O ator consulta as equipes do evento e as suas vagas.
  2. O ator solicita o ingresso em uma equipe.
  3. O sistema registra o ator como integrante.
- **Fluxos alternativos e de exceção:**
  - E1. Aluno não elegível pelo escopo do evento → `STUDENT_NOT_ELIGIBLE`.
  - E2. Aluno já integra outra equipe do mesmo evento → `STUDENT_ALREADY_IN_TEAM`.
  - E3. Tamanho máximo da equipe atingido → `TEAM_SIZE_LIMIT_REACHED`.
  - E4. Evento cancelado → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. Um aluno pertence a no máximo uma equipe por evento (RE-04).
  - RN2. A equipe pode reunir alunos de turmas e cursos distintos quando o escopo do evento o
    permitir (RE-06).
  - RN3. O tamanho máximo é o definido no evento.
- **Permissões geradas:** `TEAM:JOIN`
- **Escopo de titularidade:** restrito às equipes de eventos em que o ator é elegível.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica inicia o processo pedindo aos alunos que escolham o próprio grupo,
  com limite de integrantes.
- **Critério de aceitação:** aluno elegível ingressa em equipe com vaga; ingresso em segunda equipe
  do mesmo evento é recusado.
- **Rastreio:** A-P1.

#### RF-EQP-003 — Designar aluno a equipe

- **Descrição:** permite ao orientador designar um aluno elegível a uma equipe, ou removê-lo dela.
- **Ator:** Professor orientador do evento
- **Pré-condições:** evento ativo; ator designado como orientador do evento; aluno elegível.
- **Fluxo principal:**
  1. O ator seleciona a equipe e o aluno.
  2. O sistema verifica elegibilidade, limite de tamanho e ausência de outra equipe no mesmo evento.
  3. O sistema registra o aluno como integrante.
- **Fluxos alternativos e de exceção:**
  - E1. Aluno não elegível → `STUDENT_NOT_ELIGIBLE`.
  - E2. Aluno já integra outra equipe do evento → `STUDENT_ALREADY_IN_TEAM`.
  - E3. Tamanho máximo atingido → `TEAM_SIZE_LIMIT_REACHED`.
- **Regras de negócio:**
  - RN1. Aplicam-se as regras RN1 a RN3 de `RF-EQP-002`.
  - RN2. A remoção de integrante não apaga a sua contribuição já registrada no artigo.
- **Permissões geradas:** `TEAM:ASSIGN_MEMBER`, `TEAM:REMOVE_MEMBER`
- **Escopo de titularidade:** restrito aos eventos em que o ator é orientador.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas descrevem o professor conduzindo a organização dos grupos no início do
  período.
- **Critério de aceitação:** aluno designado passa a integrar a equipe; designação que viole limite
  ou unicidade é recusada.
- **Rastreio:** A-P1; M-P1.

#### RF-EQP-004 — Convidar aluno para a equipe

- **Descrição:** permite ao orientador convidar um aluno elegível para uma equipe, cabendo ao aluno
  aceitar.
- **Ator:** Professor orientador do evento
- **Pré-condições:** evento ativo; ator designado como orientador do evento; aluno elegível.
- **Fluxo principal:**
  1. O ator seleciona a equipe e o aluno.
  2. O sistema registra o convite e notifica o aluno.
  3. O aluno aceita e passa a integrar a equipe.
- **Fluxos alternativos e de exceção:**
  - E1. Aluno recusa → o convite é encerrado sem efeito.
  - E2. Convite expirado → `INVITATION_EXPIRED`.
  - E3. Aluno já integra outra equipe do evento no momento do aceite → `STUDENT_ALREADY_IN_TEAM`.
  - E4. Tamanho máximo atingido no momento do aceite → `TEAM_SIZE_LIMIT_REACHED`.
- **Regras de negócio:**
  - RN1. O convite possui prazo de validade.
  - RN2. As validações de elegibilidade, unicidade e limite são reavaliadas no aceite, não apenas na
    emissão.
- **Permissões geradas:** `TEAM:INVITE_MEMBER`
- **Escopo de titularidade:** restrito aos eventos em que o ator é orientador.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — deriva de `RF-EQP-002` e `RF-EQP-003`, como alternativa que preserva a escolha
  do aluno sem exigir designação direta.
- **Critério de aceitação:** convite aceito insere o aluno na equipe; convite aceito após o
  preenchimento das vagas é recusado.
- **Rastreio:** `RF-EQP-002`; `RF-EQP-003`; A-P1.

#### RF-EQP-005 — Designar orientador responsável pela equipe

- **Descrição:** permite ao dono do escopo do evento nomear, entre os orientadores do evento, o
  responsável direto por cada equipe, distribuindo a carga de orientação.
- **Ator:** Professor, Coordenador ou Administrador Institucional, conforme o escopo
- **Pré-condições:** evento ativo; ator é o dono do seu escopo; professor já designado como
  orientador do evento.
- **Fluxo principal:**
  1. O ator seleciona a equipe e o orientador.
  2. O sistema verifica que o orientador está designado ao evento.
  3. O sistema registra a responsabilidade.
- **Fluxos alternativos e de exceção:**
  - E1. Professor não designado ao evento → `ADVISOR_NOT_ASSIGNED_TO_EVENT`.
  - E2. Ator não é dono do escopo → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. Em eventos de escopo amplo, cada orientador responde diretamente por um subconjunto das
    equipes, sem que isso restrinja o alcance dos demais orientadores do evento (RN2 de
    `RF-EVT-003`).
  - RN2. A atribuição de nota cabe ao orientador responsável pela equipe (`RF-ART-002`,
    `RF-ART-003`).
  - RN3. Uma equipe possui no máximo um orientador responsável ativo por vez.
- **Permissões geradas:** `TEAM:ASSIGN_ADVISOR`, `TEAM:REVOKE_ADVISOR`
- **Escopo de titularidade:** restrito aos eventos de cujo escopo o ator é dono.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica descreve três professores dividindo cerca de oitenta alunos em
  equipes; Marciele registra a necessidade de qualquer professor envolvido poder atender o aluno.
- **Critério de aceitação:** o orientador responsável consta na equipe e é quem atribui as notas;
  professor não designado ao evento não pode ser nomeado responsável.
- **Rastreio:** A-perfil; A-P1; M-P1; M-P3.

#### RF-EQP-006 — Consultar alunos elegíveis sem equipe

- **Descrição:** permite ao orientador identificar os alunos elegíveis ao evento que ainda não
  integram nenhuma equipe, evitando que a ausência de participação seja percebida tardiamente.
- **Ator:** Professor orientador do evento
- **Pré-condições:** evento ativo; ator designado como orientador do evento.
- **Fluxo principal:**
  1. O ator abre a consulta de formação de equipes do evento.
  2. O sistema lista os alunos elegíveis pelo escopo que não integram equipe alguma.
- **Fluxos alternativos e de exceção:**
  - E1. Ator não é orientador do evento → `ADVISOR_NOT_ASSIGNED_TO_EVENT`.
- **Regras de negócio:**
  - RN1. Participar do evento é integrar uma equipe dele (RE-03); o aluno elegível sem equipe não
    participa e é o primeiro sinal de afastamento.
- **Permissões geradas:** `TEAM:READ`
- **Escopo de titularidade:** restrito aos eventos em que o ator é orientador.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Marciele relata a percepção tardia de alunos travados ou atrasados, com
  necessidade de força-tarefa próxima ao prazo final.
- **Critério de aceitação:** a lista apresenta exatamente os alunos elegíveis sem equipe e se esvazia
  quando todos ingressam.
- **Rastreio:** M-P3.

---

### 7.7 ART — Artigo

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-ART-001 | Acompanhar a situação do artigo | E (proposta) | `ELI` |
| RF-ART-002 | Avaliar o artigo | E (proposta) | `ELI` |
| RF-ART-003 | Avaliar individualmente cada integrante | E (proposta) | `ELI` |
| RF-ART-004 | Registrar publicação externa do artigo | I (proposta) | `ELI` |

---

#### RF-ART-001 — Acompanhar a situação do artigo

- **Descrição:** permite consultar o artigo da equipe, o seu estado no ciclo de produção e a etapa
  corrente do cronograma.
- **Ator:** Aluno integrante, Professor orientador do evento, Coordenador do curso
- **Pré-condições:** artigo existente; ator alcançado pelo vínculo correspondente.
- **Fluxo principal:**
  1. O ator seleciona a equipe.
  2. O sistema apresenta o artigo, o seu estado e a etapa corrente.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo fora dos vínculos do ator → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. Os estados do artigo são `STARTED`, `IN_PROGRESS`, `IN_REVIEW` e `FINISHED`.
  - RN2. O artigo percorre `IN_PROGRESS` e `IN_REVIEW` uma vez por etapa do cronograma, em ciclo, até
    a conclusão; as transições e o ciclo de correção que as governa serão especificados em versão
    posterior desta URS.
  - RN3. O aluno enxerga apenas o artigo da sua equipe; o orientador do evento, os de todas as
    equipes do evento; o coordenador, os do seu curso.
- **Permissões geradas:** `ARTICLE:READ`
- **Escopo de titularidade:** restrito aos artigos alcançados pelos vínculos do ator.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas acompanham a evolução do trabalho ao longo das etapas de entrega.
- **Critério de aceitação:** cada perfil vê exatamente os artigos alcançados pelos seus vínculos;
  aluno de outra equipe não os vê.
- **Rastreio:** M-P3; A-P3; M-P1.

#### RF-ART-002 — Avaliar o artigo

- **Descrição:** permite ao orientador responsável registrar a nota do artigo produzido pela equipe.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo existente; ator é o orientador responsável pela equipe.
- **Fluxo principal:**
  1. O ator informa a nota do artigo.
  2. O sistema registra a nota e a autoria da avaliação.
- **Fluxos alternativos e de exceção:**
  - E1. Ator não é o orientador responsável pela equipe → `PERMISSION_DENIED`.
  - E2. Nota fora da faixa admitida → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. O artigo possui uma única nota, distinta das notas individuais dos integrantes.
  - RN2. A nota do artigo não determina, por si só, a aprovação dos alunos.
  - RN3. Toda alteração de nota preserva o registro anterior, com autor e instante.
- **Permissões geradas:** `ARTICLE:GRADE`
- **Escopo de titularidade:** restrito às equipes das quais o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — decorre da avaliação do trabalho descrita como atividade central da orientação.
- **Critério de aceitação:** a nota registrada é apresentada no artigo e a alteração preserva o
  histórico; orientador não responsável é recusado.
- **Rastreio:** M-P2; M-P9; A-P4.

#### RF-ART-003 — Avaliar individualmente cada integrante

- **Descrição:** permite ao orientador responsável atribuir nota individual a cada integrante da
  equipe, base do acompanhamento de aprovação prestado à coordenação.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** equipe com integrantes; ator é o orientador responsável pela equipe.
- **Fluxo principal:**
  1. O ator seleciona a equipe.
  2. O ator informa a nota de cada integrante.
  3. O sistema registra as notas e a autoria da avaliação.
- **Fluxos alternativos e de exceção:**
  - E1. Ator não é o orientador responsável pela equipe → `PERMISSION_DENIED`.
  - E2. Nota fora da faixa admitida → `VALIDATION_FAILED`.
  - E3. Integrante removido da equipe após a avaliação → a nota é preservada com o registro histórico
    da participação.
- **Regras de negócio:**
  - RN1. A avaliação é individual: integrantes da mesma equipe podem receber notas distintas.
  - RN2. A aprovação do aluno decorre da sua nota individual, e é a informação principal solicitada
    pela coordenação.
  - RN3. Toda alteração de nota preserva o registro anterior, com autor e instante.
- **Permissões geradas:** `ARTICLE:GRADE_MEMBER`
- **Escopo de titularidade:** restrito às equipes das quais o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Marciele identifica a aprovação dos alunos no projeto como o principal
  acompanhamento prestado à coordenação.
- **Critério de aceitação:** integrantes da mesma equipe recebem notas distintas e ambas são
  registradas; orientador não responsável é recusado.
- **Rastreio:** M-P9.

#### RF-ART-004 — Registrar publicação externa do artigo

- **Descrição:** permite registrar que o artigo foi publicado em evento científico ou periódico
  externo, informando veículo, data e endereço, para que a produção não dependa de aviso informal do
  aluno.
- **Ator:** Professor orientador do evento, Aluno integrante
- **Pré-condições:** artigo existente; ator alcançado pelo vínculo correspondente.
- **Fluxo principal:**
  1. O ator informa nome do veículo, tipo, data da publicação e endereço.
  2. O sistema registra a publicação vinculada ao artigo.
  3. O ator consulta, altera ou remove o registro quando necessário.
- **Fluxos alternativos e de exceção:**
  - E1. Endereço em formato inválido → `VALIDATION_FAILED`.
  - E2. Artigo fora dos vínculos do ator → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. O registro é manual e descritivo. Nesta versão o sistema **não** mantém catálogo de eventos
    e periódicos externos nem verifica prazos de submissão — ver §10, item 3.
  - RN2. Publicação em evento interno do sistema não constitui publicação externa e não é contada
    como tal.
  - RN3. O registro alimenta a consolidação de publicações a ser especificada com os relatórios à
    coordenação.
- **Permissões geradas:** `PUBLICATION:CREATE`, `PUBLICATION:READ`, `PUBLICATION:UPDATE`,
  `PUBLICATION:DELETE`
- **Escopo de titularidade:** restrito aos artigos alcançados pelos vínculos do ator.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Marciele relata depender de lembrar ou de o orientando avisar quando publica,
  o que gera atraso e perda de registro de produção.
- **Critério de aceitação:** publicação registrada consta no artigo e fica disponível para
  consolidação; ausência de catálogo externo não impede o registro.
- **Rastreio:** M-P9; M-P5.

---

### 7.8 INT — Internacionalização

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-INT-001 | Selecionar o idioma da interface | D (proposta) | `DER` |

---

#### RF-INT-001 — Selecionar o idioma da interface

- **Descrição:** permite ao usuário escolher o idioma da interface, com data, número e fuso
  apresentados conforme o idioma escolhido.
- **Ator:** Usuário autenticado
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator seleciona o idioma entre os disponíveis.
  2. O sistema persiste a preferência no perfil e passa a apresentar a interface nesse idioma.
- **Fluxos alternativos e de exceção:**
  - E1. Idioma não suportado → `LANGUAGE_NOT_SUPPORTED`.
  - E2. Texto sem tradução no idioma escolhido → o sistema recai no idioma padrão, sem erro.
- **Regras de negócio:**
  - RN1. O idioma padrão é o português do Brasil, único disponível no lançamento. A infraestrutura de
    tradução é entregue pronta para receber outros idiomas.
  - RN2. A tradução alcança exclusivamente a interface. Conteúdo produzido pelo usuário — tema,
    artigo, apontamento, mensagem — permanece no idioma em que foi escrito.
  - RN3. A tradução ocorre no cliente, a partir dos códigos devolvidos pela API; a API não devolve
    texto destinado à exibição.
- **Permissões geradas:** — (própria preferência)
- **Escopo de titularidade:** restrito ao perfil do próprio ator.
- **Prioridade:** D (proposta)
- **Origem:** `DER` — nenhuma parte interessada solicitou idioma adicional; o requisito decorre da
  decisão de produto de preparar o sistema para múltiplos idiomas. Pendente de validação
  (`PAD-REQ-004`).
- **Critério de aceitação:** a preferência persiste entre sessões; chave sem tradução recai no idioma
  padrão sem erro visível.
- **Rastreio:** §10, item 9; `ADR-0026` §3, §11, §25–§27; `PAD-REQ-008`; `ADR-0025` §20.

---

## 8. Catálogo de permissões

Formato `RECURSO:ACAO`, recurso no singular, tudo em maiúsculas, sem curinga (`PAD-REQ-007`,
`ADR-0014` §2, §3). Toda permissão possui requisito funcional de origem.

| Permissão | Origem |
| :--- | :--- |
| `PERMISSION_GRANT:CREATE` | RF-ACS-006 |
| `PERMISSION_GRANT:REVOKE` | RF-ACS-007 |
| `PERMISSION_GRANT:READ` | RF-ACS-008 |
| `INSTITUTION:CREATE` | RF-INS-001 |
| `INSTITUTION:READ` | RF-INS-001 |
| `INSTITUTION:UPDATE` | RF-INS-001 |
| `INSTITUTION:DEACTIVATE` | RF-INS-001 |
| `INSTITUTION:ASSIGN_ADMIN` | RF-INS-002 |
| `INSTITUTION:REVOKE_ADMIN` | RF-INS-002 |
| `COURSE:CREATE` | RF-CUR-001 |
| `COURSE:READ` | RF-CUR-001 |
| `COURSE:UPDATE` | RF-CUR-001 |
| `COURSE:DEACTIVATE` | RF-CUR-001 |
| `COURSE:ASSIGN_COORDINATOR` | RF-CUR-002 |
| `COURSE:REVOKE_COORDINATOR` | RF-CUR-002 |
| `COHORT:CREATE` | RF-TUR-001 |
| `COHORT:READ` | RF-TUR-001 |
| `COHORT:UPDATE` | RF-TUR-001 |
| `COHORT:DEACTIVATE` | RF-TUR-001 |
| `COHORT:ASSIGN_PROFESSOR` | RF-TUR-002 |
| `COHORT:REVOKE_PROFESSOR` | RF-TUR-002 |
| `ENROLLMENT:CREATE` | RF-TUR-003 |
| `ENROLLMENT:READ` | RF-TUR-003 |
| `INVITATION:CREATE` | RF-TUR-004 |
| `INVITATION:READ` | RF-TUR-004 |
| `INVITATION:REVOKE` | RF-TUR-004 |
| `EVENT:CREATE` | RF-EVT-001 |
| `EVENT:READ` | RF-EVT-001, RF-EVT-004 |
| `EVENT:UPDATE` | RF-EVT-001 |
| `EVENT:CANCEL` | RF-EVT-001 |
| `MILESTONE:CREATE` | RF-EVT-002 |
| `MILESTONE:READ` | RF-EVT-002 |
| `MILESTONE:UPDATE` | RF-EVT-002 |
| `MILESTONE:DELETE` | RF-EVT-002 |
| `EVENT:ASSIGN_ADVISOR` | RF-EVT-003 |
| `EVENT:REVOKE_ADVISOR` | RF-EVT-003 |
| `TEAM:CREATE` | RF-EQP-001 |
| `TEAM:READ` | RF-EQP-006 |
| `TEAM:JOIN` | RF-EQP-002 |
| `TEAM:ASSIGN_MEMBER` | RF-EQP-003 |
| `TEAM:REMOVE_MEMBER` | RF-EQP-003 |
| `TEAM:INVITE_MEMBER` | RF-EQP-004 |
| `TEAM:ASSIGN_ADVISOR` | RF-EQP-005 |
| `TEAM:REVOKE_ADVISOR` | RF-EQP-005 |
| `ARTICLE:READ` | RF-ART-001 |
| `ARTICLE:GRADE` | RF-ART-002 |
| `ARTICLE:GRADE_MEMBER` | RF-ART-003 |
| `PUBLICATION:CREATE` | RF-ART-004 |
| `PUBLICATION:READ` | RF-ART-004 |
| `PUBLICATION:UPDATE` | RF-ART-004 |
| `PUBLICATION:DELETE` | RF-ART-004 |

### 8.1 Composição dos papéis padrão

Os papéis são criados pela carga inicial com a composição abaixo. O papel autoriza a ação; o alcance
sobre registros específicos é resolvido pela titularidade declarada em cada requisito.

| Papel | Permissões |
| :--- | :--- |
| `SYSTEM_ADMIN` | `INSTITUTION:CREATE`, `INSTITUTION:READ`, `INSTITUTION:UPDATE`, `INSTITUTION:DEACTIVATE`, `INSTITUTION:ASSIGN_ADMIN`, `INSTITUTION:REVOKE_ADMIN` |
| `INSTITUTION_ADMIN` | `COURSE:CREATE/READ/UPDATE/DEACTIVATE`, `COURSE:ASSIGN_COORDINATOR`, `COURSE:REVOKE_COORDINATOR`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:ASSIGN_ADVISOR`, `TEAM:REVOKE_ADVISOR` |
| `COORDINATOR` | `COHORT:CREATE/READ/UPDATE/DEACTIVATE`, `COHORT:ASSIGN_PROFESSOR`, `COHORT:REVOKE_PROFESSOR`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:ASSIGN_ADVISOR`, `TEAM:REVOKE_ADVISOR`, `ARTICLE:READ`, `PUBLICATION:READ` |
| `PROFESSOR` | `ENROLLMENT:CREATE`, `ENROLLMENT:READ`, `INVITATION:CREATE/READ/REVOKE`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:CREATE/READ`, `TEAM:ASSIGN_MEMBER`, `TEAM:REMOVE_MEMBER`, `TEAM:INVITE_MEMBER`, `ARTICLE:READ`, `ARTICLE:GRADE`, `ARTICLE:GRADE_MEMBER`, `PUBLICATION:CREATE/READ/UPDATE/DELETE`, `PERMISSION_GRANT:CREATE`, `PERMISSION_GRANT:REVOKE`, `PERMISSION_GRANT:READ`, `COHORT:READ`, `COURSE:READ` |
| `STUDENT` | `EVENT:READ`, `MILESTONE:READ`, `TEAM:READ`, `TEAM:JOIN`, `ARTICLE:READ`, `PUBLICATION:CREATE/READ/UPDATE`, `COHORT:READ` |

A notação `A/B/C` acima abrevia a leitura desta tabela e **não** existe no catálogo: as permissões
efetivas são sempre enumeradas, sem curinga (`ADR-0014` §3).

---

## 9. Catálogo de códigos de resposta

Em maiúsculas, sem acento, independentes de idioma (`PAD-REQ-008`, `ADR-0025` §20). A tradução para
exibição ocorre no cliente, a partir do código.

| Código | Origem |
| :--- | :--- |
| `AUTHENTICATION_FAILED` | RF-ACS-001 |
| `INSTITUTION_INACTIVE` | RF-ACS-001, RF-INS-001, RF-INS-002 |
| `VALIDATION_FAILED` | RF-ACS-004, RF-ACS-005, RF-INS-001, RF-CUR-001, RF-TUR-001, RF-TUR-004, RF-TUR-005, RF-EVT-001, RF-EVT-002, RF-EQP-001, RF-EQP-002, RF-ART-002, RF-ART-003, RF-ART-004 |
| `PERMISSION_DENIED` | RF-ACS-005, RF-CUR-001, RF-CUR-002, RF-TUR-001, RF-TUR-002, RF-TUR-003, RF-TUR-004, RF-EVT-002, RF-EVT-003, RF-EQP-005, RF-ART-002, RF-ART-003 |
| `RESOURCE_NOT_FOUND` | RF-ACS-006, RF-ACS-007, RF-ACS-008, RF-INS-002, RF-CUR-002, RF-EVT-001, RF-EVT-004, RF-ART-001, RF-ART-004 |
| `EMAIL_ALREADY_REGISTERED` | RF-TUR-003, RF-TUR-005 |
| `INVITATION_EXPIRED` | RF-ACS-003, RF-ACS-004, RF-TUR-005, RF-EQP-004 |
| `INVITATION_REVOKED` | RF-TUR-005 |
| `STUDENT_ALREADY_ENROLLED` | RF-TUR-003, RF-TUR-005 |
| `COORDINATOR_ALREADY_ASSIGNED` | RF-CUR-002 |
| `EVENT_SCOPE_NOT_ALLOWED` | RF-EVT-001 |
| `EVENT_TEAM_LIMIT_REACHED` | RF-EQP-001 |
| `TEAM_SIZE_LIMIT_REACHED` | RF-EQP-002, RF-EQP-003, RF-EQP-004 |
| `STUDENT_ALREADY_IN_TEAM` | RF-EQP-002, RF-EQP-003, RF-EQP-004 |
| `STUDENT_NOT_ELIGIBLE` | RF-EVT-003, RF-EQP-002, RF-EQP-003 |
| `ADVISOR_NOT_ASSIGNED_TO_EVENT` | RF-EQP-001, RF-EQP-005, RF-EQP-006 |
| `MILESTONE_DATE_CONFLICT` | RF-EVT-002 |
| `GRANT_NOT_HELD_BY_GRANTER` | RF-ACS-006 |
| `SELF_GRANT_NOT_ALLOWED` | RF-ACS-006 |
| `LANGUAGE_NOT_SUPPORTED` | RF-INT-001 |

---

## 10. Pendências

| # | Pendência | Efeito |
| :--- | :--- | :--- |
| 1 | **Prioridades não atribuídas por parte interessada.** Nenhum requisito desta versão teve prioridade atribuída pelas entrevistadas; os valores registrados são propostas da equipe. | Viola `PAD-REQ-003`. Por `PAD-REQ-006`, nenhum requisito desta versão deve ser encaminhado à implementação antes da ratificação. |
| 2 | **Requisitos `DER` não validados.** Toda a hierarquia institucional, a autenticação e a cadeia de criação de usuários derivam da definição de produto, não de solicitação direta. | Por `PAD-REQ-004`, não são considerados acordados antes de validação com as partes interessadas. |
| 3 | **Radar de eventos externos adiado.** Marciele nomeou, em P10, duas condições obrigatórias para a plataforma valer o tempo de aprendizado: apoio às correções e busca de eventos. A segunda foi adiada por decisão de escopo. Em P5 ela descreve o item como externo — "radar de eventos científicos, congressos e periódicos" com prazo, temática, requisitos e links, e o trabalho manual de "identificação de eventos e periódicos adequados à temática" e "repasse dessas oportunidades aos alunos". O congresso interno aparece separadamente, como template já conhecido. | Requisito elicitado, conhecido e não atendido. `RF-ART-004` o atende parcialmente ao permitir o registro manual da publicação externa. O módulo de correção passa a sustentar sozinho o caso de adoção dessa parte interessada. |
| 4 | **Um usuário por instituição.** Quem atua em mais de uma instituição usa contas e e-mails distintos. | Decisão de escopo. Expansão prevista. |
| 5 | **Elicitação faltante.** Nenhum aluno e nenhum coordenador foi entrevistado, embora ambos sejam atores desta URS. | A visão do aluno consta apenas em terceira pessoa. Recomenda-se nova rodada de elicitação. |
| 6 | **Cobertura de área.** Ambas as entrevistadas são do curso de Administração. As normas registradas se limitam a ABNT e ao template do congresso interno. | Outras áreas podem exigir normas distintas, ainda sem evidência. |
| 7 | **Coordenador único por curso.** Registrado como RN1 de `RF-CUR-002` sem evidência que o confirme. | Premissa a confirmar. |
| 8 | **Divergência de visibilidade (P8).** Marciele defende que qualquer professor da instituição veja o trabalho em qualquer fase; Angélica restringe a orientadores e autores. Esta versão implementa a posição restritiva. | Se a posição ampla prevalecer, será necessária permissão de leitura em escopo institucional, hoje inexistente. |
| 9 | **Idiomas.** Apenas português do Brasil no lançamento; nenhuma parte interessada solicitou idioma adicional. | `RF-INT-001` permanece `DER` até validação. A estratégia técnica está fixada em `ADR-0026` e nos padrões `PAD-NOM-001` a `PAD-NOM-014`; resta apenas a validação do requisito com as partes interessadas. |
| 10 | **Ciclo de correção não especificado.** Submissão de versões, apontamentos, verificação de atendimento entre etapas, conformidade e relatórios. | É a próxima fatia desta URS e onde residem as dores principais das duas entrevistadas. |

---

## 11. Histórico de revisões

| Versão | Data | Alteração |
| :--- | :--- | :--- |
| 0.0 | 2026-08-13 | Documento zerado. Todo o conteúdo das versões 0.1 a 0.9.1 era decisão da própria equipe, não requisito de parte interessada, e foi movido para `Padroes/Padroes-de-Engenharia.md`. A URS recomeça vazia, a ser elaborada a partir da elicitação. O histórico anterior está no versionamento do repositório. |
| 0.1 | 2026-08-19 | Registrada a fatia estrutural: 8 categorias, 32 requisitos funcionais, catálogo de 51 permissões e catálogo de 20 códigos de resposta, com rastreabilidade às entrevistas de Marciele e Angélica. Os catálogos de permissões e de códigos passam a existir, atendendo às pendências correspondentes de `Padroes-de-Engenharia.md` §6 no que se refere a esta fatia. Prioridades registradas como proposta, pendentes de atribuição por parte interessada. |
