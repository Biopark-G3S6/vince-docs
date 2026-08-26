# URS — Especificação de Requisitos do Usuário

**Disciplina:** Arquitetura e Requisitos
**Professor:** «a preencher»
**Acadêmicos:** Grupo 03 — Camilly Azevedo, Gustavo Ferreira, Matheus Akio, Vitor Fernandes
**Projeto:** VinceArt
**Cliente:** Marciele R. Siveres e Angélica P. S. Meurer — curso de Administração
**Versão:** 0.4
**Status:** Em elaboração — pendente de ratificação pelas partes interessadas
**Data:** 2026-08-26

---

## 1. Objetivo do Documento

Este documento especifica **o que as partes interessadas do VinceArt precisam que o sistema faça**.

Todo item registrado aqui DEVE ter origem em parte interessada e DEVE ser rastreável até a evidência
que o originou. Decisão da equipe NÃO DEVE ser registrada nesta URS: o seu lugar é
[`Padroes/Padroes-de-Engenharia.md`](../Padroes/Padroes-de-Engenharia.md) ou um ADR em
[`ADR/`](../ADR/).

As regras de redação desta URS — identificação, prioridade, origem, rastreabilidade e estrutura do
requisito funcional — estão em `PAD-REQ-001` a `PAD-REQ-008`. Elas dizem **como** escrever um
requisito, nunca **qual** requisito escrever.

Os requisitos são classificados em:

- **Requisitos Funcionais (RF)** — o que o sistema deve fazer: comportamento, regra de negócio,
  interface e relatório. Estão em 2.1, um quadro por requisito.
- **Requisitos Não Funcionais (RNF)** — o que não é funcionalidade: aspectos técnicos, gerenciais,
  premissas e restrições. Neste projeto eles não são registrados aqui, pelo motivo exposto em 2.2.

O material bruto de elicitação está em [`Coleta de Requisitos/`](Coleta%20de%20Requisitos/).

---

### 1.1 Escopo desta versão

Esta versão registra duas fatias:

- **Estrutural** — identidade e acesso, hierarquia institucional, evento acadêmico, formação de
  equipes e o artigo como entidade.
- **Produção e correção do artigo** — edição do artigo dentro do sistema, template, norma, entrega
  por etapa, apontamento ancorado, devolução, discussão, notificação e verificações automatizadas.
- **Acompanhamento e relatórios** — painéis de orientação e de coordenação, sinalização de equipe
  parada ou em risco, contribuição por integrante e relatório de produção do curso.

Com esta versão o escopo funcional está coberto. O que resta é ratificação, não elicitação: nenhum
requisito teve prioridade atribuída por parte interessada e nenhum requisito `DER` foi validado —
§3, itens 1, 2 e 11.

**Fora do escopo do produto nesta fase**, por decisão registrada em §3: eventos científicos
externos e periódicos (radar de oportunidades), participação de um usuário em mais de uma
instituição e matrícula em mais de uma turma.

---

### 1.2 Convenções

#### 1.2.1 Identificação

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
| `TPL` | Template |
| `EDT` | Edição do artigo |
| `REV` | Ciclo de correção |
| `DSC` | Discussão e notificações |
| `IAA` | Assistência automatizada |
| `ACP` | Acompanhamento e relatórios |
| `INT` | Internacionalização |

Os códigos de categoria acompanham a convenção em português já adotada pelos identificadores
`PAD-*`. Isso não conflita com o padrão de nomeação em inglês: aquele rege **identificadores de
software** — código, tabela, coluna, rota, papel, permissão e código de resposta —, não os
identificadores de documento.

#### 1.2.2 Prioridade

Escala `E` (essencial), `I` (importante), `D` (desejável).

Por `PAD-REQ-003`, a prioridade DEVE ser atribuída pela parte interessada. **Nenhuma prioridade
desta versão foi atribuída por parte interessada.** Os valores aqui registrados aparecem com o
sufixo **`(proposta)`** e são sugestão da equipe, sem valor de acordo, pendentes de ratificação —
ver §3, item 1.

#### 1.2.3 Origem

| Código | Significado |
| :--- | :--- |
| `ELI` | Declarado por parte interessada na elicitação |
| `STK` | Imposto por parte interessada fora da elicitação |
| `DER` | Derivado; indica o item de origem e NÃO É considerado acordado antes de validação (`PAD-REQ-004`) |

#### 1.2.4 Rastreio

| Sigla | Evidência |
| :--- | :--- |
| `M-P<n>` | Marciele R. Siveres, resposta à pergunta `<n>` — `Coleta de Requisitos/Requisitos Marciele.md` |
| `M-perfil` | Marciele, perfil do respondente |
| `A-P<n>` | Angélica P. S. Meurer, resposta à pergunta `<n>` — `Coleta de Requisitos/Requisitos Angélica.md` |
| `A-perfil` | Angélica, perfil do respondente |

---

### 1.3 Partes interessadas

| Parte interessada | Papel na elicitação | Estado |
| :--- | :--- | :--- |
| Marciele R. Siveres | Orientadora, Administração, 5 anos, ~35 orientandos simultâneos | Entrevistada |
| Angélica P. S. Meurer | Orientadora, Administração, 12 anos, 50+ orientandos por semestre | Entrevistada |
| Aluno orientando | Ator de grande parte dos requisitos | **Não entrevistado** — §3, item 5 |
| Coordenador de curso | Destinatário dos relatórios | **Não será entrevistado** — decisão registrada em §3, item 5 |

Ambas as entrevistadas pertencem ao curso de Administração. Não há evidência de outras áreas, o que
limita a generalização das normas exigidas — ver §3, item 6.

---

### 1.4 Atores e papéis

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

#### 1.4.1 Premissas de identidade

1. O primeiro usuário `SYSTEM_ADMIN` é criado por script de carga inicial. Não existe autocadastro
   para esse papel nem para nenhum outro papel administrativo.
2. O e-mail é identificador único global do usuário. Quem atua em mais de uma instituição usa
   e-mails distintos, um por conta — consequência da decisão de §3, item 4.
3. O `SYSTEM_ADMIN` administra instituições e configurações gerais de suporte. **Não** acessa
   conteúdo acadêmico: artigo, apontamento, nota ou avaliação.

---

### 1.5 Modelo de domínio

```
Instituição
├── Template                            semente do artigo; PODE ser restrito a um curso
├── Curso                               INSTITUTION_ADMIN cria; designa COORDINATOR
│   └── Turma                           COORDINATOR cria; período letivo, data de início;
│       │                               designa PROFESSOR
│       └── Matrícula ── Aluno          PROFESSOR cadastra ou aluno ingressa por convite
└── Evento                              escopo: INSTITUICAO | CURSO | TURMA
    ├── tema, problema, objetivos       definidos pelo dono do escopo
    ├── template selecionado            versão congelada na criação, ou "em branco"
    ├── limites de equipe               quantidade de equipes e tamanho máximo
    ├── cronograma de etapas            3 a 4 entregas com prazo, fixadas no início do período
    ├── orientadores do evento          podem ver e atuar sobre todas as equipes do evento
    └── Equipe ──1:1── Artigo           STARTED → IN_PROGRESS → IN_REVIEW → FINISHED
        ├── orientador responsável      subconjunto dos orientadores do evento
        ├── Referência ── Citação       dado estruturado; gera a lista pela norma
        ├── Discussão ── Mensagem       equipe + orientador responsável; contínua
        └── Entrega (por etapa)         versão imutável; congela o artigo
            └── Apontamento             OPEN → ADDRESSED → RESOLVED | DISMISSED
```

#### 1.5.1 Regras estruturais transversais

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
| RE-10 | O texto do artigo é dado estruturado do sistema, não arquivo. Toda a fatia de produção e correção depende disso. |
| RE-11 | O artigo alterna entre `IN_PROGRESS` e `IN_REVIEW` uma vez por etapa: a entrega o congela, a devolução o libera. `FINISHED` é declarado pelo orientador, não decorre da última devolução. |
| RE-12 | Durante `IN_REVIEW` a equipe não altera o texto. A discussão permanece aberta em todos os estados. |
| RE-13 | O apontamento nasce e é encerrado apenas em `IN_REVIEW`; é atendido pela equipe apenas em `IN_PROGRESS`. |
| RE-14 | Apontamento não encerrado pelo orientador acompanha o artigo para a etapa seguinte, esteja em `OPEN` ou em `ADDRESSED`. |
| RE-15 | Quem corrige o texto é a equipe. O orientador aponta, valida, reabre e dispensa; NÃO DEVE alterar o texto do artigo. |
| RE-16 | O template é semente e a norma é contrato: o template fornece o documento inicial e não é verificado depois; a norma é verificada ao longo de todo o ciclo. |
| RE-17 | Toda saída de verificação automática é subsídio. Nenhuma decisão do ciclo de correção é tomada pelo sistema. |

---

## 2. Lista de Requisitos

Os requisitos funcionais estão em 2.1, um quadro por requisito, na estrutura fixada por
`PAD-REQ-008`. Os requisitos não funcionais estão em 2.2. Os catálogos de 2.3 e 2.4 são derivados
dos requisitos funcionais e não acrescentam exigência: consolidam o que os quadros já declaram.

---

### 2.1 Requisitos Funcionais

#### 2.1.1 ACS — Acesso e identidade

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

##### RF-ACS-001 — Autenticar-se no sistema

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

##### RF-ACS-002 — Encerrar a sessão

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

##### RF-ACS-003 — Recuperar o acesso

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

##### RF-ACS-004 — Definir ou alterar a própria senha

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

##### RF-ACS-005 — Manter o próprio perfil

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

##### RF-ACS-006 — Conceder permissão a outro usuário

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

##### RF-ACS-007 — Revogar concessão de permissão

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

##### RF-ACS-008 — Consultar concessões diretas ativas

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

#### 2.1.2 INS — Instituição

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-INS-001 | Manter instituição | E (proposta) | `DER` |
| RF-INS-002 | Designar administrador institucional | E (proposta) | `DER` |

---

##### RF-INS-001 — Manter instituição

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
- **Rastreio:** M-P5; M-P9; A-P1; decisão de escopo de §3, item 4.

##### RF-INS-002 — Designar administrador institucional

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
- **Rastreio:** `RF-INS-001`; §3, item 2.

---

#### 2.1.3 CUR — Curso

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-CUR-001 | Manter curso | E (proposta) | `DER` |
| RF-CUR-002 | Designar coordenador do curso | E (proposta) | `ELI` |

---

##### RF-CUR-001 — Manter curso

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

##### RF-CUR-002 — Designar coordenador do curso

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
  - RN1. O curso possui no máximo um coordenador ativo por vez — premissa a confirmar, §3, item 7.
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

#### 2.1.4 TUR — Turma

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-TUR-001 | Manter turma | E (proposta) | `ELI` |
| RF-TUR-002 | Designar professor à turma | E (proposta) | `ELI` |
| RF-TUR-003 | Cadastrar aluno na turma | E (proposta) | `DER` |
| RF-TUR-004 | Emitir convite de ingresso na turma | E (proposta) | `DER` |
| RF-TUR-005 | Ingressar na turma por convite | E (proposta) | `DER` |

---

##### RF-TUR-001 — Manter turma

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

##### RF-TUR-002 — Designar professor à turma

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

##### RF-TUR-003 — Cadastrar aluno na turma

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
- **Rastreio:** A-P1; M-P1; §3, item 4.

##### RF-TUR-004 — Emitir convite de ingresso na turma

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

##### RF-TUR-005 — Ingressar na turma por convite

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

#### 2.1.5 EVT — Evento

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-EVT-001 | Manter evento | E (proposta) | `ELI` |
| RF-EVT-002 | Definir o cronograma de etapas do evento | E (proposta) | `ELI` |
| RF-EVT-003 | Designar orientadores ao evento | E (proposta) | `ELI` |
| RF-EVT-004 | Consultar eventos por escopo | E (proposta) | `DER` |

---

##### RF-EVT-001 — Manter evento

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

##### RF-EVT-002 — Definir o cronograma de etapas do evento

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
  - RN3. A etapa é a unidade à qual se prendem as entregas (`RF-REV-001`) e os apontamentos
    (`RF-REV-004`) do ciclo de correção, especificado em §2.1.10.
- **Permissões geradas:** `MILESTONE:CREATE`, `MILESTONE:READ`, `MILESTONE:UPDATE`,
  `MILESTONE:DELETE`
- **Escopo de titularidade:** restrito aos eventos de cujo escopo o ator é dono.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica declara que o cronograma de entregas é definido no início do semestre;
  Marciele registra de três a quatro etapas de entrega por período.
- **Critério de aceitação:** cronograma com etapas em ordem crescente é aceito; etapa com data
  anterior à da etapa precedente é recusada.
- **Rastreio:** A-P1; A-P3; M-P1; M-P2.

##### RF-EVT-003 — Designar orientadores ao evento

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

##### RF-EVT-004 — Consultar eventos por escopo

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
    ampla — divergência registrada em §3, item 8.
- **Permissões geradas:** `EVENT:READ`
- **Escopo de titularidade:** restrito aos eventos alcançados pelos vínculos do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-EVT-001` e da decisão de apresentar os eventos organizados por
  escopo.
- **Critério de aceitação:** cada perfil vê exatamente os eventos alcançados pelos seus vínculos, e
  nenhum outro.
- **Rastreio:** `RF-EVT-001`; A-P8; M-P8.

---

#### 2.1.6 EQP — Equipe

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-EQP-001 | Criar equipe no evento | E (proposta) | `ELI` |
| RF-EQP-002 | Ingressar em equipe | E (proposta) | `ELI` |
| RF-EQP-003 | Designar aluno a equipe | E (proposta) | `ELI` |
| RF-EQP-004 | Convidar aluno para a equipe | I (proposta) | `DER` |
| RF-EQP-005 | Designar orientador responsável pela equipe | E (proposta) | `ELI` |
| RF-EQP-006 | Consultar alunos elegíveis sem equipe | I (proposta) | `ELI` |

---

##### RF-EQP-001 — Criar equipe no evento

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

##### RF-EQP-002 — Ingressar em equipe

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

##### RF-EQP-003 — Designar aluno a equipe

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

##### RF-EQP-004 — Convidar aluno para a equipe

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

##### RF-EQP-005 — Designar orientador responsável pela equipe

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

##### RF-EQP-006 — Consultar alunos elegíveis sem equipe

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

#### 2.1.7 ART — Artigo

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-ART-001 | Acompanhar a situação do artigo | E (proposta) | `ELI` |
| RF-ART-002 | Avaliar o artigo | E (proposta) | `ELI` |
| RF-ART-003 | Avaliar individualmente cada integrante | E (proposta) | `ELI` |
| RF-ART-004 | Registrar publicação externa do artigo | I (proposta) | `ELI` |

---

##### RF-ART-001 — Acompanhar a situação do artigo

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
  - RN2. O artigo percorre `IN_PROGRESS` e `IN_REVIEW` uma vez por etapa do cronograma, em ciclo,
    até a conclusão. As transições e o ciclo que as governa estão em §2.1.10 (RE-11).
  - RN3. O aluno enxerga apenas o artigo da sua equipe; o orientador do evento, os de todas as
    equipes do evento; o coordenador, os do seu curso.
- **Permissões geradas:** `ARTICLE:READ`
- **Escopo de titularidade:** restrito aos artigos alcançados pelos vínculos do ator.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas acompanham a evolução do trabalho ao longo das etapas de entrega.
- **Critério de aceitação:** cada perfil vê exatamente os artigos alcançados pelos seus vínculos;
  aluno de outra equipe não os vê.
- **Rastreio:** M-P3; A-P3; M-P1.

##### RF-ART-002 — Avaliar o artigo

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

##### RF-ART-003 — Avaliar individualmente cada integrante

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

##### RF-ART-004 — Registrar publicação externa do artigo

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
    e periódicos externos nem verifica prazos de submissão — ver §3, item 3.
  - RN2. Publicação em evento interno do sistema não constitui publicação externa e não é contada
    como tal.
  - RN3. O registro alimenta a consolidação de publicações do relatório de produção do curso
    (`RF-ACP-005` RN1).
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

#### 2.1.8 TPL — Template

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-TPL-001 | Manter template de artigo | I (proposta) | `ELI` |
| RF-TPL-002 | Selecionar o template do evento | I (proposta) | `ELI` |

---

##### RF-TPL-001 — Manter template de artigo

- **Descrição:** permite criar, consultar, alterar e desativar um template de artigo — documento
  inicial com estrutura de seções e cabeçalhos já redigidos e formatados — para servir de ponto de
  partida aos artigos de um evento.
- **Ator:** Administrador Institucional, Coordenador
- **Pré-condições:** ator vinculado à instituição; para template restrito a curso, ator vinculado ao
  curso.
- **Fluxo principal:**
  1. O ator informa nome, descrição e, opcionalmente, o curso ao qual o template fica restrito.
  2. O ator compõe o conteúdo inicial do template no mesmo editor do artigo (`RF-EDT-001`).
  3. O sistema registra o template como versão nova, preservando as anteriores.
  4. O ator consulta, altera ou desativa o template.
- **Fluxos alternativos e de exceção:**
  - E1. Nome ausente → `VALIDATION_FAILED`.
  - E2. Coordenador informando curso do qual não é coordenador → `PERMISSION_DENIED`.
  - E3. Desativação de template já selecionado por evento em andamento → a operação sucede; o evento
    permanece na versão que congelou (RN4).
- **Regras de negócio:**
  - RN1. O template pertence sempre a uma instituição e PODE ser restrito a um curso dela. Restrito,
    só pode ser selecionado por evento daquele curso ou de turma dele.
  - RN2. O `INSTITUTION_ADMIN` mantém os templates da sua instituição; o `COORDINATOR`, apenas os
    restritos ao seu curso. O `PROFESSOR` não mantém templates — apenas seleciona, ao criar evento
    de escopo de turma (`RF-TPL-002`).
  - RN3. O template é **semente**: define o conteúdo inicial do artigo e não impõe verificação
    posterior. O que se verifica ao longo do ciclo é a conformidade à **norma** (`RF-IAA-002`), não
    ao template (RE-16).
  - RN4. Alterar um template gera versão nova. Evento já criado permanece na versão que selecionou.
- **Permissões geradas:** `TEMPLATE:CREATE`, `TEMPLATE:READ`, `TEMPLATE:UPDATE`,
  `TEMPLATE:DEACTIVATE`
- **Escopo de titularidade:** restrito aos templates da instituição do ator; para o Coordenador,
  restrito adicionalmente aos do seu curso.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Marciele registra o template do congresso interno como documento já conhecido
  e reutilizado a cada edição.
- **Critério de aceitação:** coordenador cria template restrito ao seu curso e é recusado ao tentar
  restringi-lo a outro; alterar o template não altera o artigo de evento já criado.
- **Rastreio:** M-P5.

##### RF-TPL-002 — Selecionar o template do evento

- **Descrição:** permite ao criador do evento escolher, no momento da criação, o template que servirá
  de ponto de partida aos artigos das suas equipes, ou optar por documento em branco.
- **Ator:** Professor, Coordenador ou Administrador Institucional, conforme o escopo
- **Pré-condições:** evento em criação; ator é o dono do seu escopo (RE-01).
- **Fluxo principal:**
  1. O sistema apresenta os templates disponíveis ao escopo do evento e a opção "em branco".
  2. O ator seleciona uma delas.
  3. O sistema registra no evento a referência à versão corrente do template selecionado.
  4. Cada artigo criado no evento nasce com o conteúdo dessa versão.
- **Fluxos alternativos e de exceção:**
  - E1. Template indisponível ao escopo do evento → `RESOURCE_NOT_FOUND`.
  - E2. Troca do template após a criação do evento → `TEMPLATE_ALREADY_FIXED`.
- **Regras de negócio:**
  - RN1. A seleção ocorre apenas na criação do evento e é imutável a partir dela.
  - RN2. "Em branco" é opção legítima. O artigo nasce vazio e segue a mesma norma (`RF-EDT-005` RN1).
  - RN3. O evento congela a versão do template; alteração posterior não o alcança.
  - RN4. O professor seleciona template ao criar evento de escopo de turma, ainda que não possa
    mantê-lo (`RF-TPL-001` RN2).
- **Permissões geradas:** `TEMPLATE:READ` — o ato de selecionar integra `EVENT:CREATE`.
- **Escopo de titularidade:** restrito aos templates alcançados pelo escopo do evento.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — o template do congresso interno é reutilizado a cada edição, o que pressupõe
  vinculá-lo ao evento que o adota.
- **Critério de aceitação:** evento de turma de um curso não enxerga template restrito a outro curso;
  criado o evento, a troca de template é recusada.
- **Rastreio:** M-P5.

---

#### 2.1.9 EDT — Edição do artigo

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-EDT-001 | Editar o texto do artigo | E (proposta) | `DER` |
| RF-EDT-002 | Editar simultaneamente com os demais integrantes | E (proposta) | `DER` |
| RF-EDT-003 | Manter as referências bibliográficas do artigo | E (proposta) | `DER` |
| RF-EDT-004 | Citar referência no texto | E (proposta) | `DER` |
| RF-EDT-005 | Aplicar a formatação da norma | E (proposta) | `ELI` |
| RF-EDT-006 | Importar documento externo para o artigo | I (proposta) | `DER` |
| RF-EDT-007 | Exportar o artigo | E (proposta) | `DER` |
| RF-EDT-008 | Consultar o histórico de versões do artigo | I (proposta) | `DER` |

---

##### RF-EDT-001 — Editar o texto do artigo

- **Descrição:** permite ao integrante da equipe redigir e formatar o artigo dentro do sistema,
  dispensando editor de texto externo. As capacidades exigidas do editor estão em §2.1.9.1.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo em `STARTED` ou `IN_PROGRESS`; ator integrante da equipe.
- **Fluxo principal:**
  1. O ator abre o artigo da sua equipe.
  2. O sistema apresenta o editor com o conteúdo corrente.
  3. O ator redige e formata, conforme §2.1.9.1.
  4. O sistema preserva as alterações continuamente, sem ação explícita de salvar.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo em `IN_REVIEW` → `ARTICLE_LOCKED_FOR_REVIEW`; o editor abre em modo de leitura.
  - E2. Artigo em `FINISHED` → `ARTICLE_ALREADY_FINISHED`; o editor abre em modo de leitura.
  - E3. Ator sem vínculo com a equipe → `RESOURCE_NOT_FOUND`.
  - E4. Perda de conexão durante a edição → o sistema retém as alterações e as reconcilia ao
    restabelecer, sem descarte silencioso.
- **Regras de negócio:**
  - RN1. Só integrante da equipe edita. O orientador **NÃO DEVE** alterar o texto do artigo; a sua
    intervenção se dá por apontamento (`RF-REV-004`) e por mensagem (`RF-DSC-001`) — RE-15.
  - RN2. O artigo é editável apenas em `STARTED` e `IN_PROGRESS`.
  - RN3. A perda de trabalho por falha de conexão ou de navegador é inaceitável. O sistema preserva o
    que foi digitado sem ação explícita do autor.
  - RN4. O conteúdo do artigo é dado estruturado do sistema, não arquivo (RE-10). É o que torna
    possíveis a formatação por norma (`RF-EDT-005`), a âncora do apontamento (`RF-REV-004`) e a
    comparação de versões (`RF-REV-010`).
  - RN5. A formatação direta sobre o estilo é permitida. O desvio em relação à norma é reportado por
    `RF-IAA-002`, nunca bloqueado.
- **Permissões geradas:** `ARTICLE:EDIT`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Deriva de M-P4, em que a correção ocorre sobre o arquivo
  enviado pelo aluno em ambiente externo: trazer o texto para dentro do sistema é a condição de todo
  o restante desta fatia.
- **Critério de aceitação:** o aluno redige e formata o artigo sem usar editor externo; ao recarregar
  a página, o que foi digitado está preservado; o orientador abre o mesmo artigo e não consegue
  alterar o texto.
- **Rastreio:** M-P4; A-P5.

###### 2.1.9.1 Capacidades exigidas do editor

O editor DEVE cobrir integralmente o que a produção de um artigo acadêmico exige. As capacidades
abaixo são requisito de `RF-EDT-001`.

| Grupo | Capacidades |
| :--- | :--- |
| Caractere | Fonte e tamanho; negrito, itálico, sublinhado, tachado; sobrescrito e subscrito; cor da fonte e realce; versalete e caixa alta; espaçamento entre caracteres; limpar formatação; idioma do trecho |
| Parágrafo | Alinhamento à esquerda, centralizado, à direita e justificado; recuo de primeira linha, esquerdo e direito; entrelinhas; espaçamento antes e depois; controle de linhas órfãs e viúvas; manter com o próximo e manter linhas juntas; quebra de página antes; tabulações com preenchimento; bordas e sombreamento |
| Estilos | Estilos de parágrafo nomeados; hierarquia de títulos; estilos de caractere; redefinir estilo a partir da seleção; formatação direta sobreposta ao estilo |
| Página e seção | Margens, tamanho e orientação do papel; quebra de página e de linha; seções com formatação própria; cabeçalho e rodapé; primeira página e páginas pares/ímpares distintas; numeração de páginas com reinício e algarismos romanos nos pré-textuais; colunas |
| Listas | Marcadores e numeração; lista multinível; reiniciar e continuar numeração; alíneas com recuo normalizado |
| Tabelas | Inserir e redimensionar; inserir e excluir linha e coluna; mesclar e dividir células; repetir linha de cabeçalho entre páginas; bordas, sombreamento e estilos |
| Objetos | Imagem com posicionamento e quebra de texto; legenda numerada automaticamente; indicação de fonte da figura ou tabela; equações |
| Referências no texto | Sumário automático a partir dos títulos; listas de figuras, tabelas, quadros e abreviaturas; notas de rodapé e de fim; referência cruzada a figura, tabela e seção |
| Revisão | Comentário ancorado a trecho, com resposta e resolução (§2.1.10); comparação entre versões (`RF-REV-010`); histórico com restauração (`RF-EDT-008`); ortografia e gramática; contagem de palavras, caracteres e páginas; restrição de edição por região |
| Colaboração | Edição simultânea com cursores visíveis (`RF-EDT-002`); presença dos demais integrantes; menção a participante |
| Navegação | Painel de navegação por títulos; localizar e substituir; desfazer e refazer; colar mantendo ou removendo formatação; pincel de formatação; atalhos de teclado; autocorreção ao digitar; zoom, modo de leitura e régua |
| Entrada e saída | Importar `.docx` (`RF-EDT-006`); exportar `.docx` e PDF (`RF-EDT-007`); imprimir; metadados do documento |

**Não exigido:** mala direta, macros e linguagem de automação, suplementos, esquema XML
customizado, comparação de três ou mais documentos simultâneos, assinatura digital, marca d'água,
gráficos gerados no editor, formas e caixas de texto, dicionário de sinônimos, hifenização
automática.

##### RF-EDT-002 — Editar simultaneamente com os demais integrantes

- **Descrição:** permite que mais de um integrante da equipe edite o mesmo artigo ao mesmo tempo,
  cada um vendo o que os demais escrevem e onde estão trabalhando.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo editável; dois ou mais integrantes com o artigo aberto.
- **Fluxo principal:**
  1. Dois ou mais integrantes abrem o mesmo artigo.
  2. O sistema apresenta a cada um a presença e a posição do cursor dos demais.
  3. Cada alteração aparece aos demais sem ação explícita de atualizar.
  4. O sistema registra a autoria de cada trecho no histórico (`RF-EDT-008`).
- **Fluxos alternativos e de exceção:**
  - E1. Perda de conexão de um dos editores → as alterações locais são reconciliadas ao
    restabelecer, sem descarte silencioso.
  - E2. Edições concorrentes sobre o mesmo trecho → o sistema as combina sem perda e sem exigir
    escolha manual do autor.
- **Regras de negócio:**
  - RN1. Não existe bloqueio de trecho nem edição de um por vez. A equipe escreve junta.
  - RN2. Nenhuma alteração aceita pelo sistema pode ser descartada por conflito.
  - RN3. A autoria de cada trecho é registrada e é insumo da avaliação individual (`RF-ART-003`,
    RE-09) e dos indícios de autoria (`RF-IAA-004`).
  - RN4. A técnica de reconciliação é decisão de engenharia e **NÃO É** objeto desta URS.
- **Permissões geradas:** `ARTICLE:EDIT` — a mesma de `RF-EDT-001`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** E (proposta) — declarada indispensável à primeira versão.
- **Origem:** `DER` — definição de produto. Não há evidência de elicitação; ver §3, item 11.
- **Critério de aceitação:** dois alunos digitam em parágrafos distintos ao mesmo tempo e cada um vê
  o texto do outro surgir; digitam no mesmo parágrafo e nenhum dos dois perde texto.
- **Rastreio:** §3, item 11.

##### RF-EDT-003 — Manter as referências bibliográficas do artigo

- **Descrição:** permite à equipe registrar as referências do artigo como dado estruturado — tipo,
  autores, título, ano, veículo, edição, local, editora, páginas, DOI e URL —, de modo que o sistema
  gere a lista de referências no formato da norma.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo editável.
- **Fluxo principal:**
  1. O ator escolhe o tipo da referência.
  2. O ator preenche os campos do tipo, ou informa o DOI, ou cola a referência para interpretação.
  3. O sistema registra a referência e passa a apresentá-la na lista, formatada e ordenada pela
     norma do evento.
  4. O ator altera ou remove referências.
- **Fluxos alternativos e de exceção:**
  - E1. Campo obrigatório do tipo ausente → `VALIDATION_FAILED`.
  - E2. Interpretação de DOI ou de texto colado incompleta → o sistema registra o que reconheceu e
    assinala os campos faltantes; não recusa o registro.
  - E3. Remoção de referência citada no texto → `REFERENCE_IN_USE`.
- **Regras de negócio:**
  - RN1. A referência é dado estruturado. Texto livre digitado como se fosse referência não é
    referência para o sistema e não entra na lista gerada.
  - RN2. A lista de referências é gerada, formatada e ordenada pelo sistema; não é redigida pela
    equipe.
  - RN3. É a estrutura da referência que permite a verificação cruzada de `RF-IAA-002` — citado e
    não referenciado, referenciado e não citado.
- **Permissões geradas:** `REFERENCE:CREATE`, `REFERENCE:READ`, `REFERENCE:UPDATE`,
  `REFERENCE:DELETE`
- **Escopo de titularidade:** restrito às referências do artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de A-P5, que exige verificação automática de conformidade à ABNT: a
  formatação e a conferência de referências, núcleo da norma, só são possíveis sobre dado
  estruturado.
- **Critério de aceitação:** referência registrada por campos aparece na lista no formato da norma,
  na posição correta da ordenação; remover referência citada é recusado.
- **Rastreio:** A-P5.

##### RF-EDT-004 — Citar referência no texto

- **Descrição:** permite inserir no corpo do texto a citação de uma referência registrada, mantendo o
  vínculo entre a citação e o registro.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo editável; referência registrada (`RF-EDT-003`).
- **Fluxo principal:**
  1. O ator posiciona o cursor e escolhe a referência.
  2. O ator informa a página, quando houver.
  3. O sistema insere a citação no formato da norma, vinculada ao registro.
- **Fluxos alternativos e de exceção:**
  - E1. Referência inexistente ou removida → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. A citação é vínculo, não texto. Alterar a referência atualiza todas as suas citações.
  - RN2. A indicação de página é opcional na citação indireta e exigida na direta.
  - RN3. O vínculo sustenta a verificação cruzada de `RF-IAA-002`.
- **Permissões geradas:** `REFERENCE:CITE`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — mesma derivação de `RF-EDT-003`.
- **Critério de aceitação:** corrigir o ano de uma referência altera todas as citações dela no texto,
  sem intervenção do autor.
- **Rastreio:** A-P5.

##### RF-EDT-005 — Aplicar a formatação da norma

- **Descrição:** permite aplicar, por ação explícita, a formatação da norma vigente no evento —
  margens, fonte, entrelinhas, recuos, alinhamento, títulos, citações longas, legendas e paginação —
  ao documento inteiro ou apenas ao trecho selecionado.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo editável.
- **Fluxo principal:**
  1. O ator aciona a formatação, com ou sem trecho selecionado.
  2. O sistema aplica a norma ao alvo: o trecho, se houver seleção; o documento inteiro, se não.
  3. O sistema informa o que foi alterado.
- **Fluxos alternativos e de exceção:**
  - E1. Nenhuma divergência encontrada → o sistema informa e nada altera.
- **Regras de negócio:**
  - RN1. A norma desta versão é a **ABNT**, e vale para todo artigo — o iniciado em branco e o
    iniciado a partir de template.
  - RN2. O template não substitui nem altera a norma. Ele fornece o documento inicial, já em
    conformidade com ela (RE-16).
  - RN3. A formatação é ato explícito do autor. O sistema **NÃO DEVE** reformatar durante a
    digitação.
  - RN4. A verificação permanente de conformidade é `RF-IAA-002`. Este requisito corrige; aquele
    aponta.
  - RN5. Outras normas são expansão prevista — §3, item 14.
- **Permissões geradas:** `ARTICLE:FORMAT`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica descreve a adequação às normas ABNT como verificação que deveria ser
  automática; Marciele registra o template do congresso interno como referência de formatação.
- **Critério de aceitação:** artigo com entrelinha e margens fora da ABNT é corrigido por uma ação;
  com um parágrafo selecionado, só ele é alterado.
- **Rastreio:** A-P5; M-P5.

##### RF-EDT-006 — Importar documento externo para o artigo

- **Descrição:** permite carregar um documento `.docx` existente como conteúdo do artigo, para a
  equipe que começou a escrever fora do sistema.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo editável.
- **Fluxo principal:**
  1. O ator seleciona o arquivo.
  2. O sistema converte o que reconhece — títulos, parágrafos, listas, tabelas, imagens e notas.
  3. O sistema apresenta o resultado e relata o que não pôde converter.
  4. O ator confirma ou descarta a importação.
- **Fluxos alternativos e de exceção:**
  - E1. Formato não suportado → `FILE_FORMAT_NOT_SUPPORTED`.
  - E2. Arquivo acima do limite → `FILE_TOO_LARGE`.
  - E3. Importação sobre artigo que já tem conteúdo → o sistema exige confirmação, pois substitui.
- **Regras de negócio:**
  - RN1. A importação **substitui** o conteúdo do artigo; não o mescla.
  - RN2. A conversão é de melhor esforço. O relato do que não converteu é parte do resultado, não
    exceção.
  - RN3. Os metadados do arquivo importado são preservados e são insumo de `RF-IAA-004`.
  - RN4. A importação só é possível enquanto o artigo é editável.
- **Permissões geradas:** `ARTICLE:IMPORT`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto; condição de migração do trabalho já iniciado fora do
  sistema.
- **Critério de aceitação:** `.docx` com títulos, tabela e nota de rodapé é importado preservando os
  três; o que não converteu é listado ao autor.
- **Rastreio:** M-P4.

##### RF-EDT-007 — Exportar o artigo

- **Descrição:** permite obter o artigo como `.docx` ou PDF, formatado pela norma, para submissão a
  congresso ou periódico e para arquivo pessoal.
- **Ator:** Aluno integrante, Professor orientador do evento, Coordenador do curso
- **Pré-condições:** artigo existente; ator alcançado pelo vínculo correspondente.
- **Fluxo principal:**
  1. O ator escolhe o formato.
  2. O sistema gera o documento com a formatação da norma e o entrega ao ator.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo fora dos vínculos do ator → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. A exportação preserva a formatação da norma e a lista de referências gerada.
  - RN2. Está disponível em qualquer estado do artigo, inclusive `IN_REVIEW` e `FINISHED`.
  - RN3. Sustenta `RF-ART-004`: nenhum destino externo aceita referência à plataforma.
- **Permissões geradas:** `ARTICLE:EXPORT`
- **Escopo de titularidade:** restrito aos artigos alcançados pelos vínculos do ator, como em
  `RF-ART-001`.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — deriva de `RF-ART-004` e da submissão ao congresso interno descrita em M-P5.
- **Critério de aceitação:** o `.docx` exportado abre em editor externo com margens, entrelinha e
  lista de referências conforme a norma.
- **Rastreio:** M-P5; M-P9.

##### RF-EDT-008 — Consultar o histórico de versões do artigo

- **Descrição:** permite consultar a sucessão de estados do artigo, ver quem escreveu cada trecho e
  restaurar um estado anterior.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo existente; ator integrante da equipe.
- **Fluxo principal:**
  1. O ator abre o histórico.
  2. O sistema apresenta as entregas e os pontos intermediários preservados, em ordem cronológica,
     com a autoria de cada trecho.
  3. O ator visualiza um estado anterior e, se quiser, o restaura.
- **Fluxos alternativos e de exceção:**
  - E1. Restauração com o artigo em `IN_REVIEW` → `ARTICLE_LOCKED_FOR_REVIEW`.
- **Regras de negócio:**
  - RN1. O histórico contém as entregas (`RF-REV-001`) e os pontos intermediários preservados pelo
    sistema.
  - RN2. A entrega é imutável e **NÃO DEVE** ser removida do histórico.
  - RN3. A restauração cria estado novo; não apaga o histórico.
  - RN4. O histórico registra a autoria por trecho (`RF-EDT-002` RN3) e é a fonte principal de
    `RF-IAA-004`.
- **Permissões geradas:** `ARTICLE:READ_HISTORY`, `ARTICLE:RESTORE_VERSION`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto; decorre da edição contínua sem ação de salvar
  (`RF-EDT-001` RN3) e da edição simultânea (`RF-EDT-002`).
- **Critério de aceitação:** estado anterior à entrega é recuperável; a entrega permanece no
  histórico após a restauração.
- **Rastreio:** §3, item 11.

---

#### 2.1.10 REV — Ciclo de correção

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-REV-001 | Entregar a versão da etapa | E (proposta) | `ELI` |
| RF-REV-002 | Desfazer a entrega | I (proposta) | `DER` |
| RF-REV-003 | Encerrar a entrega no vencimento do prazo | E (proposta) | `DER` |
| RF-REV-004 | Registrar apontamento no texto entregue | E (proposta) | `ELI` |
| RF-REV-005 | Alterar ou complementar apontamento | I (proposta) | `DER` |
| RF-REV-006 | Devolver o artigo à equipe | E (proposta) | `ELI` |
| RF-REV-007 | Marcar apontamento como corrigido | E (proposta) | `DER` |
| RF-REV-008 | Validar, reabrir ou dispensar apontamento | E (proposta) | `DER` |
| RF-REV-009 | Consultar o apontamento na origem e no estado atual | E (proposta) | `DER` |
| RF-REV-010 | Comparar a versão entregue com a anterior | E (proposta) | `DER` |
| RF-REV-011 | Concluir o artigo | E (proposta) | `DER` |

---

##### RF-REV-001 — Entregar a versão da etapa

- **Descrição:** permite a qualquer integrante marcar o artigo como entregue na etapa corrente, o que
  congela o texto e o submete à correção do orientador responsável.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo em `IN_PROGRESS`; etapa corrente do cronograma aberta.
- **Fluxo principal:**
  1. O ator aciona a entrega da etapa corrente.
  2. O sistema registra a entrega — autor, data e conteúdo integral do artigo naquele instante —
     como versão imutável.
  3. O sistema transiciona o artigo para `IN_REVIEW` e o torna somente leitura para a equipe.
  4. O sistema notifica o orientador responsável (`RF-DSC-005`).
- **Fluxos alternativos e de exceção:**
  - E1. Artigo já entregue nesta etapa → `SUBMISSION_ALREADY_MADE`.
  - E2. Artigo em `IN_REVIEW` → `ARTICLE_LOCKED_FOR_REVIEW`.
  - E3. Artigo em `FINISHED` → `ARTICLE_ALREADY_FINISHED`.
  - E4. Nenhuma etapa aberta no cronograma → `MILESTONE_NOT_OPEN`.
- **Regras de negócio:**
  - RN1. Qualquer integrante entrega, e o sistema registra quem entregou. Não existe responsável pela
    equipe nesta versão.
  - RN2. A entrega congela o artigo: durante `IN_REVIEW` a equipe não altera o texto. A discussão
    (§2.1.11) permanece aberta (RE-12).
  - RN3. A versão entregue é imutável e é a unidade sobre a qual se ancoram os apontamentos
    (`RF-REV-004`) e as comparações (`RF-REV-010`).
  - RN4. A entrega vale para a etapa corrente do cronograma do evento (`RF-EVT-002`).
- **Permissões geradas:** `SUBMISSION:CREATE`, `SUBMISSION:READ`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — ambas descrevem o trabalho organizado em entregas por etapa, com correção
  entre elas.
- **Critério de aceitação:** feita a entrega, nenhum integrante consegue alterar o texto e o
  orientador recebe o aviso; o conteúdo entregue permanece idêntico ao do instante da entrega.
- **Rastreio:** M-P1; M-P2; A-P1; A-P3.

##### RF-REV-002 — Desfazer a entrega

- **Descrição:** permite à equipe reverter a entrega enquanto o prazo da etapa não venceu e o
  orientador não iniciou a correção, devolvendo o artigo à edição.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo em `IN_REVIEW` por entrega espontânea; prazo da etapa não vencido.
- **Fluxo principal:**
  1. O ator aciona o desfazimento da entrega.
  2. O sistema verifica o prazo e a ausência de apontamento na entrega.
  3. O sistema descarta a entrega e transiciona o artigo de volta para `IN_PROGRESS`.
- **Fluxos alternativos e de exceção:**
  - E1. Prazo da etapa vencido → `MILESTONE_DEADLINE_PASSED`.
  - E2. Correção já iniciada — existe apontamento na entrega → `REVIEW_ALREADY_STARTED`.
  - E3. Artigo não entregue → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. Só é possível antes do vencimento do prazo e antes do primeiro apontamento do orientador.
  - RN2. A entrega desfeita é descartada e não permanece no histórico como entrega.
  - RN3. A equipe pode entregar novamente; vale sempre a última entrega da etapa.
- **Permissões geradas:** `SUBMISSION:REVOKE`
- **Escopo de titularidade:** restrito ao artigo da equipe do ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto. Sem ele, a equipe que entrega antes do prazo fica
  impedida de trabalhar até a devolução.
- **Critério de aceitação:** entrega feita dois dias antes do prazo é desfeita e o artigo volta a ser
  editável; após o primeiro apontamento, o desfazimento é recusado.
- **Rastreio:** §3, item 11.

##### RF-REV-003 — Encerrar a entrega no vencimento do prazo

- **Descrição:** no vencimento do prazo da etapa, o sistema entrega automaticamente o estado corrente
  do artigo das equipes que não entregaram, e assinala a omissão.
- **Ator:** Sistema
- **Pré-condições:** etapa do cronograma com prazo vencido; equipes do evento sem entrega na etapa.
- **Fluxo principal:**
  1. Vence o prazo da etapa.
  2. O sistema registra entrega para toda equipe do evento sem entrega na etapa.
  3. O sistema assinala a entrega como não espontânea.
  4. O sistema transiciona os artigos para `IN_REVIEW` e notifica a equipe e o orientador
     responsável.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo vazio → a entrega é registrada assim mesmo, vazia e assinalada. O orientador precisa
    do sinal.
- **Regras de negócio:**
  - RN1. Nenhuma etapa fica sem entrega. O cronograma não trava por omissão de uma equipe.
  - RN2. A entrega automática é distinguível da espontânea e é sinal de acompanhamento da equipe.
  - RN3. Não existe prorrogação individual de prazo nesta versão — §3, item 15.
- **Permissões geradas:** nenhuma — ação do sistema, sem ator humano.
- **Escopo de titularidade:** não se aplica.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Deriva do volume de orientandos declarado no perfil de
  ambas e da necessidade de o ciclo não depender da iniciativa da equipe.
- **Critério de aceitação:** vencido o prazo, equipe sem entrega tem o artigo congelado e assinalado
  como entrega não espontânea; o orientador vê a distinção.
- **Rastreio:** M-perfil; A-perfil; A-P3.

##### RF-REV-004 — Registrar apontamento no texto entregue

- **Descrição:** permite ao orientador responsável ancorar um apontamento a um trecho do texto
  entregue, indicando o que deve ser corrigido.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo em `IN_REVIEW`; ator designado orientador responsável (`RF-EQP-005`).
- **Fluxo principal:**
  1. O ator seleciona um trecho da versão entregue.
  2. O ator escreve o apontamento.
  3. O sistema o registra ancorado ao trecho, na versão entregue, no estado `OPEN`.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo fora de `IN_REVIEW` → `ARTICLE_NOT_IN_REVIEW`.
  - E2. Ator não é o orientador responsável pela equipe → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. O apontamento só nasce em `IN_REVIEW` (RE-13). Fora dele o orientador se manifesta pela
    discussão (`RF-DSC-001`), que permanece aberta o tempo todo.
  - RN2. A âncora é a versão entregue, imutável. O apontamento permanece legível ainda que o trecho
    mude depois (`RF-REV-009`).
  - RN3. O apontamento registrado permanece **invisível à equipe** até a devolução (`RF-REV-006`).
  - RN4. O orientador **NÃO DEVE** alterar o texto do artigo. Quem corrige é a equipe (RE-15).
  - RN5. Estados do apontamento: `OPEN`, `ADDRESSED`, `RESOLVED`, `DISMISSED`.
- **Permissões geradas:** `REMARK:CREATE`, `REMARK:READ`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Marciele descreve a correção feita por comentários, destaques e apontamentos no
  próprio documento do aluno.
- **Critério de aceitação:** apontamento criado antes da devolução não aparece ao aluno; orientador
  de outra equipe do mesmo evento não consegue apontar nesta.
- **Rastreio:** M-P4.

##### RF-REV-005 — Alterar ou complementar apontamento

- **Descrição:** permite ao orientador editar o texto de um apontamento seu, inclusive depois da
  devolução, para esclarecer, reforçar ou acrescentar exigência.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** apontamento existente, de autoria do ator.
- **Fluxo principal:**
  1. O ator abre o apontamento e altera o seu texto.
  2. O sistema registra a alteração e preserva o texto anterior no histórico do apontamento.
  3. Se o apontamento já houver sido devolvido, o sistema notifica a equipe (`RF-DSC-005`).
- **Fluxos alternativos e de exceção:**
  - E1. Ator não é o autor do apontamento → `PERMISSION_DENIED`.
  - E2. Apontamento em `RESOLVED` ou `DISMISSED` → `REMARK_ALREADY_CLOSED`.
- **Regras de negócio:**
  - RN1. Só o autor altera o apontamento.
  - RN2. A alteração após a devolução é visível à equipe e a notifica.
  - RN3. O texto anterior é preservado; a alteração não apaga o que foi pedido antes.
  - RN4. Alterar o texto **não** altera o estado do apontamento.
- **Permissões geradas:** `REMARK:UPDATE`
- **Escopo de titularidade:** restrito aos apontamentos de autoria do ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto. O orientador precisa poder frisar ou reforçar exigência
  já feita, sem abrir apontamento novo sobre o mesmo trecho.
- **Critério de aceitação:** complemento a apontamento já devolvido chega à equipe como notificação e
  o texto original continua consultável.
- **Rastreio:** M-P4.

##### RF-REV-006 — Devolver o artigo à equipe

- **Descrição:** permite ao orientador encerrar a correção da etapa em ato único, publicando à equipe
  todos os apontamentos e devolvendo o artigo à edição.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo em `IN_REVIEW`.
- **Fluxo principal:**
  1. O ator conclui os apontamentos da etapa e decide sobre os pendentes (`RF-REV-008`).
  2. O ator aciona a devolução.
  3. O sistema publica à equipe todos os apontamentos da etapa, transiciona o artigo para
     `IN_PROGRESS` e o torna editável.
  4. O sistema notifica a equipe (`RF-DSC-005`).
- **Fluxos alternativos e de exceção:**
  - E1. Artigo fora de `IN_REVIEW` → `ARTICLE_NOT_IN_REVIEW`.
  - E2. Devolução sem nenhum apontamento → permitida; significa etapa aceita sem exigências.
  - E3. Ator não é o orientador responsável → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. A devolução é **ato único**. Não existe devolução parcial: ou a etapa está corrigida, ou
    não está.
  - RN2. Antes dela, nenhum apontamento da etapa é visível à equipe.
  - RN3. Devolvida a etapa, o artigo volta a `IN_PROGRESS` até a entrega seguinte (RE-11).
  - RN4. Apontamentos em `OPEN` e em `ADDRESSED` permanecem ativos e acompanham o artigo para a
    etapa seguinte, até que o orientador os encerre (RE-14, `RF-REV-008`).
- **Permissões geradas:** `ARTICLE:RETURN`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — o ciclo entrega → correção → devolução é o que ambas descrevem como rotina da
  orientação ao longo do período.
- **Critério de aceitação:** feita a devolução, a equipe passa a ver de uma só vez todos os
  apontamentos e volta a poder editar; apontamento não encerrado continua listado na etapa seguinte.
- **Rastreio:** M-P2; M-P4; A-P3.

##### RF-REV-007 — Marcar apontamento como corrigido

- **Descrição:** permite ao integrante da equipe declarar que atendeu a um apontamento, submetendo-o
  à validação do orientador.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** artigo em `IN_PROGRESS`; apontamento devolvido e em `OPEN`.
- **Fluxo principal:**
  1. O ator consulta o apontamento e o trecho a que se refere (`RF-REV-009`).
  2. O ator corrige o texto.
  3. O ator marca o apontamento como corrigido.
  4. O sistema o move para `ADDRESSED` e o mantém aguardando validação.
- **Fluxos alternativos e de exceção:**
  - E1. Apontamento em `RESOLVED` ou `DISMISSED` → `REMARK_ALREADY_CLOSED`.
  - E2. Artigo em `IN_REVIEW` → `ARTICLE_LOCKED_FOR_REVIEW`.
- **Regras de negócio:**
  - RN1. Marcar como corrigido **não encerra** o apontamento. Quem o encerra é o orientador
    (`RF-REV-008`).
  - RN2. O ator pode desmarcar enquanto o artigo estiver editável, devolvendo o apontamento a `OPEN`.
  - RN3. O apontamento em `ADDRESSED` acompanha o artigo para a etapa seguinte junto com os em
    `OPEN`, até decisão do orientador (RE-14).
  - RN4. O atendimento só ocorre em `IN_PROGRESS` (RE-13).
- **Permissões geradas:** `REMARK:ADDRESS`
- **Escopo de titularidade:** restrito aos apontamentos do artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Corresponde à verificação de atendimento entre etapas que
  ambas descrevem fazer manualmente.
- **Critério de aceitação:** apontamento marcado como corrigido continua pendente até a correção
  seguinte; o aluno consegue desmarcá-lo antes da entrega.
- **Rastreio:** M-P4; A-P3.

##### RF-REV-008 — Validar, reabrir ou dispensar apontamento

- **Descrição:** permite ao orientador, durante a correção de uma etapa, encerrar cada apontamento
  pendente das etapas anteriores — validando a correção, reabrindo-a por insuficiência ou
  dispensando a exigência.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo em `IN_REVIEW`; apontamento em `OPEN` ou `ADDRESSED`.
- **Fluxo principal:**
  1. O sistema apresenta ao ator os apontamentos pendentes, acompanhados do resumo de `RF-IAA-001`.
  2. Para cada um, o ator valida (`RESOLVED`), reabre (`OPEN`) ou dispensa (`DISMISSED`).
  3. O sistema registra a decisão, o autor e a data.
- **Fluxos alternativos e de exceção:**
  - E1. Artigo fora de `IN_REVIEW` → `ARTICLE_NOT_IN_REVIEW`.
  - E2. Apontamento já encerrado → `REMARK_ALREADY_CLOSED`.
  - E3. Ator não é o orientador responsável → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. A validação ocorre **apenas durante a correção de uma etapa**, nunca enquanto a equipe
    edita (RE-13).
  - RN2. `RESOLVED` e `DISMISSED` encerram o apontamento. Reaberto, ele volta a `OPEN` e acompanha o
    artigo para a etapa seguinte.
  - RN3. `DISMISSED` significa que o orientador retirou a exigência — tipicamente após o argumento da
    equipe na discussão —, sem que tenha havido correção.
  - RN4. A decisão é sempre do orientador. Nenhum apontamento é encerrado pelo sistema nem por saída
    de análise automática (RE-17, `RF-IAA-001` RN2).
- **Permissões geradas:** `REMARK:RESOLVE`, `REMARK:REOPEN`, `REMARK:DISMISS`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto, sobre a prática de conferir entre etapas se o que foi
  pedido foi atendido.
- **Critério de aceitação:** apontamento reaberto aparece na etapa seguinte; apontamento dispensado
  não reaparece e fica registrado como dispensado, com autor e data.
- **Rastreio:** M-P4; A-P3.

##### RF-REV-009 — Consultar o apontamento na origem e no estado atual

- **Descrição:** permite ver, ao abrir um apontamento, o trecho tal como estava quando ele foi feito e
  o trecho tal como está agora, confrontados.
- **Ator:** Aluno integrante, Professor orientador responsável
- **Pré-condições:** apontamento existente e visível ao ator.
- **Fluxo principal:**
  1. O ator abre o apontamento.
  2. O sistema apresenta o trecho ancorado na versão de origem, assinalado como estado anterior, e o
     trecho correspondente na versão corrente, assinalado como estado atual.
  3. Ao fechar o apontamento, o texto volta à apresentação normal.
- **Fluxos alternativos e de exceção:**
  - E1. Trecho de origem removido por inteiro → o sistema apresenta o trecho original e assinala a
    remoção no estado atual. O apontamento permanece válido.
- **Regras de negócio:**
  - RN1. O confronto aparece **apenas com o apontamento aberto**. Ele **NÃO DEVE** poluir a leitura
    corrente do documento.
  - RN2. A convenção de apresentação é vermelho para o estado anterior e verde para o atual.
  - RN3. A âncora não se perde quando o texto muda. Nenhum apontamento é descartado por alteração ou
    remoção do trecho a que se refere.
- **Permissões geradas:** `REMARK:READ`
- **Escopo de titularidade:** restrito aos apontamentos do artigo alcançado pelo vínculo do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Sem o confronto, o apontamento ancorado a uma versão
  anterior fica ilegível assim que o texto muda.
- **Critério de aceitação:** apontamento cujo parágrafo foi reescrito continua legível, mostrando o
  texto de origem e o texto atual; fechado o apontamento, nenhuma marcação permanece no documento.
- **Rastreio:** M-P4.

##### RF-REV-010 — Comparar a versão entregue com a anterior

- **Descrição:** permite ver, lado a lado, a versão entregue na etapa e a entregue na etapa anterior,
  com as diferenças assinaladas.
- **Ator:** Professor orientador responsável, Aluno integrante
- **Pré-condições:** existirem duas entregas do mesmo artigo.
- **Fluxo principal:**
  1. O ator seleciona a entrega.
  2. O sistema apresenta as duas versões lado a lado.
  3. O sistema assinala inserção, remoção e alteração no nível da palavra.
  4. O ator navega de diferença em diferença.
- **Fluxos alternativos e de exceção:**
  - E1. Primeira entrega, sem anterior → o sistema apresenta a versão isolada e informa a ausência de
    termo de comparação.
- **Regras de negócio:**
  - RN1. A comparação é sempre entre versões entregues, imutáveis.
  - RN2. A granularidade é de palavra dentro do parágrafo.
  - RN3. É o insumo do resumo de `RF-IAA-001`.
- **Permissões geradas:** `SUBMISSION:COMPARE`
- **Escopo de titularidade:** restrito aos artigos alcançados pelo vínculo do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Deriva do volume de orientandos declarado por ambas:
  reler o artigo inteiro a cada etapa é o que consome o tempo do orientador.
- **Critério de aceitação:** parágrafo alterado entre duas entregas aparece assinalado nas duas
  colunas, com as palavras alteradas destacadas.
- **Rastreio:** M-perfil; A-perfil; M-P4.

##### RF-REV-011 — Concluir o artigo

- **Descrição:** permite ao orientador declarar o artigo concluído, encerrando o ciclo de correção e
  habilitando a avaliação.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo em `IN_REVIEW`; última etapa do cronograma em correção.
- **Fluxo principal:**
  1. O ator aciona a conclusão.
  2. O sistema verifica que todos os apontamentos foram encerrados.
  3. O sistema transiciona o artigo para `FINISHED` e o torna somente leitura para todos.
  4. O sistema habilita `RF-ART-002` e `RF-ART-003` e notifica a equipe.
- **Fluxos alternativos e de exceção:**
  - E1. Etapas do cronograma ainda pendentes → `MILESTONE_PENDING`.
  - E2. Apontamentos pendentes sem decisão → `REMARK_PENDING`.
  - E3. Ator não é o orientador responsável → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. A conclusão é **ato explícito do orientador**, não decorrência automática da última
    devolução (RE-11).
  - RN2. Em `FINISHED` o artigo é somente leitura para todos. A exportação (`RF-EDT-007`) e o
    registro de publicação externa (`RF-ART-004`) permanecem disponíveis.
  - RN3. A avaliação (`RF-ART-002`, `RF-ART-003`) ocorre sobre o artigo concluído.
- **Permissões geradas:** `ARTICLE:CONCLUDE`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Deriva de `RF-ART-002` e `RF-ART-003`, que pressupõem um
  artigo encerrado para serem avaliados.
- **Critério de aceitação:** conclusão com apontamento pendente é recusada; concluído, o artigo não
  aceita mais edição e a avaliação fica disponível.
- **Rastreio:** M-P3; A-P3.

---

#### 2.1.11 DSC — Discussão e notificações

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-DSC-001 | Publicar mensagem na discussão da equipe | E (proposta) | `DER` |
| RF-DSC-002 | Responder a mensagem da discussão | E (proposta) | `DER` |
| RF-DSC-003 | Responder a apontamento | E (proposta) | `DER` |
| RF-DSC-004 | Acompanhar a discussão em tempo real | I (proposta) | `DER` |
| RF-DSC-005 | Receber notificação | E (proposta) | `DER` |
| RF-DSC-006 | Consultar e marcar notificações | I (proposta) | `DER` |

---

##### RF-DSC-001 — Publicar mensagem na discussão da equipe

- **Descrição:** permite aos integrantes da equipe e ao seu orientador responsável trocarem mensagens
  em uma discussão contínua vinculada ao artigo.
- **Ator:** Aluno integrante, Professor orientador responsável pela equipe
- **Pré-condições:** equipe formada; ator integrante dela ou seu orientador responsável.
- **Fluxo principal:**
  1. O ator abre a discussão da equipe.
  2. O ator escreve e publica a mensagem.
  3. O sistema registra autor e data, entrega a mensagem aos participantes conectados
     (`RF-DSC-004`) e notifica os demais (`RF-DSC-005`).
- **Fluxos alternativos e de exceção:**
  - E1. Ator sem vínculo com a equipe → `RESOURCE_NOT_FOUND`.
  - E2. Mensagem vazia → `VALIDATION_FAILED`.
- **Regras de negócio:**
  - RN1. A discussão é **única por artigo** e contínua ao longo de todas as etapas. Não há discussão
    por etapa.
  - RN2. Participam os integrantes da equipe e o orientador responsável por ela. Os demais
    orientadores do evento e o coordenador do curso **não** participam.
  - RN3. A discussão permanece aberta em todos os estados do artigo, inclusive durante `IN_REVIEW`
    (RE-12). É o canal do orientador fora do ciclo de apontamentos.
  - RN4. Toda mensagem é visível a todos os participantes. Não existe mensagem privada entre
    professores nesta versão — §3, item 13.
  - RN5. O autor pode excluir a própria mensagem; o registro de que houve exclusão permanece.
- **Permissões geradas:** `MESSAGE:CREATE`, `MESSAGE:READ`, `MESSAGE:DELETE`
- **Escopo de titularidade:** restrito à discussão da equipe a que o ator está vinculado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto; ver §3, item 11.
- **Critério de aceitação:** aluno de outra equipe do mesmo evento não alcança a discussão; o
  orientador responsável publica e a equipe recebe.
- **Rastreio:** §3, item 11.

##### RF-DSC-002 — Responder a mensagem da discussão

- **Descrição:** permite responder a uma mensagem específica da discussão, mantendo a resposta
  agrupada sob a mensagem que a originou.
- **Ator:** Aluno integrante, Professor orientador responsável pela equipe
- **Pré-condições:** mensagem existente na discussão da equipe do ator.
- **Fluxo principal:**
  1. O ator escolhe a mensagem e aciona a resposta.
  2. O ator escreve e publica.
  3. O sistema agrupa a resposta sob a mensagem raiz e notifica os participantes.
- **Fluxos alternativos e de exceção:**
  - E1. Mensagem raiz excluída → a resposta permanece, indicando que a mensagem original foi
    excluída.
- **Regras de negócio:**
  - RN1. Existe **um único nível de resposta**. A resposta a uma resposta se prende à mesma mensagem
    raiz.
  - RN2. As respostas são apresentadas em ordem cronológica sob a raiz.
- **Permissões geradas:** `MESSAGE:REPLY`
- **Escopo de titularidade:** restrito à discussão da equipe a que o ator está vinculado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto.
- **Critério de aceitação:** responder a uma resposta agrupa a nova mensagem sob a mesma raiz, sem
  criar terceiro nível.
- **Rastreio:** §3, item 11.

##### RF-DSC-003 — Responder a apontamento

- **Descrição:** permite ao integrante responder a um apontamento; a resposta é publicada na discussão
  da equipe, com referência ao apontamento que a originou.
- **Ator:** Aluno integrante da equipe
- **Pré-condições:** apontamento devolvido à equipe (`RF-REV-006`).
- **Fluxo principal:**
  1. O ator abre o apontamento e aciona a resposta.
  2. O ator escreve.
  3. O sistema publica a mensagem na discussão da equipe, referenciando o apontamento, e notifica o
     orientador responsável.
- **Fluxos alternativos e de exceção:**
  - E1. Apontamento ainda não devolvido → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. A resposta **não fica dentro do apontamento**. É mensagem da discussão com referência a ele.
    Isso mantém toda a conversa em um lugar só.
  - RN2. A referência é navegável nos dois sentidos: do apontamento para a mensagem e da mensagem
    para o apontamento.
  - RN3. Responder **não altera** o estado do apontamento. Quem o move é `RF-REV-007` e `RF-REV-008`.
- **Permissões geradas:** `MESSAGE:CREATE` — a mesma de `RF-DSC-001`
- **Escopo de titularidade:** restrito aos apontamentos do artigo da equipe do ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto.
- **Critério de aceitação:** a resposta aparece na discussão como mensagem comum, com o apontamento
  referenciado e navegável; o estado do apontamento permanece inalterado.
- **Rastreio:** §3, item 11.

##### RF-DSC-004 — Acompanhar a discussão em tempo real

- **Descrição:** permite que a mensagem publicada por um participante apareça aos demais que estejam
  com a discussão aberta, sem que precisem recarregar a página.
- **Ator:** Aluno integrante, Professor orientador responsável pela equipe
- **Pré-condições:** ator com a discussão aberta.
- **Fluxo principal:**
  1. Um participante publica.
  2. A mensagem aparece aos demais participantes conectados, sem ação deles.
- **Fluxos alternativos e de exceção:**
  - E1. Conexão interrompida → restabelecida a conexão, o participante recebe o que perdeu, sem
    lacuna e sem duplicidade.
- **Regras de negócio:**
  - RN1. O participante com a discussão aberta recebe a mensagem sem ação sua.
  - RN2. O meio técnico é decisão de engenharia e **NÃO É** objeto desta URS.
- **Permissões geradas:** `MESSAGE:READ` — a mesma de `RF-DSC-001`
- **Escopo de titularidade:** restrito à discussão da equipe a que o ator está vinculado.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto.
- **Critério de aceitação:** dois participantes com a discussão aberta veem a mensagem do outro
  aparecer sem recarregar; após queda de conexão, nada se perde.
- **Rastreio:** §3, item 11.

##### RF-DSC-005 — Receber notificação

- **Descrição:** permite que o usuário seja avisado dos fatos que exigem ação ou atenção sua, na
  interface e, quando ele assim configurar, por e-mail.
- **Ator:** Aluno integrante, Professor orientador responsável pela equipe
- **Pré-condições:** usuário ativo, alcançado pelo fato.
- **Fluxo principal:**
  1. Ocorre o fato.
  2. O sistema identifica os destinatários pelo vínculo.
  3. O sistema registra a notificação e a entrega na interface.
  4. O sistema envia por e-mail as notificações que o destinatário assim configurou.
- **Fluxos alternativos e de exceção:**
  - E1. Falha no envio de e-mail → a notificação na interface permanece registrada; o envio é
    retentado.
- **Regras de negócio:**
  - RN1. Geram notificação: entrega da etapa, ao orientador responsável; entrega automática por
    vencimento de prazo, à equipe e ao orientador; devolução do artigo, à equipe; nova mensagem na
    discussão, aos demais participantes; alteração de apontamento já devolvido, à equipe; validação,
    reabertura ou dispensa de apontamento, à equipe; conclusão do artigo, à equipe; proximidade do
    prazo da etapa, à equipe.
  - RN2. O usuário não é notificado do que ele mesmo fez.
  - RN3. O e-mail é redigido no idioma do **destinatário**, nunca no de quem originou o fato
    (`ADR-0026` §18).
  - RN4. O usuário escolhe quais notificações recebe por e-mail. A notificação na interface não é
    desligável.
- **Permissões geradas:** `NOTIFICATION:READ`
- **Escopo de titularidade:** restrito às notificações endereçadas ao próprio ator.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto; decorre do ciclo de correção, em que cada transição exige
  ação da outra parte.
- **Critério de aceitação:** quem entregou não recebe a notificação da própria entrega; o orientador
  recebe; o e-mail sai no idioma do destinatário.
- **Rastreio:** §3, item 11; `ADR-0026` §18.

##### RF-DSC-006 — Consultar e marcar notificações

- **Descrição:** permite ao usuário consultar as suas notificações, distinguir as não lidas e
  marcá-las como lidas.
- **Ator:** Qualquer usuário autenticado
- **Pré-condições:** sessão ativa.
- **Fluxo principal:**
  1. O ator abre as suas notificações.
  2. O sistema apresenta as notificações em ordem cronológica inversa, com as não lidas destacadas.
  3. O ator marca uma ou todas como lidas, ou navega até o objeto da notificação.
- **Fluxos alternativos e de exceção:**
  - E1. Objeto da notificação removido ou fora do alcance do ator → `RESOURCE_NOT_FOUND`.
- **Regras de negócio:**
  - RN1. O usuário só alcança as notificações endereçadas a ele.
  - RN2. Navegar até o objeto marca a notificação como lida.
- **Permissões geradas:** `NOTIFICATION:MARK_READ`
- **Escopo de titularidade:** restrito às notificações do próprio ator.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — definição de produto.
- **Critério de aceitação:** notificação de outro usuário não é alcançável; abrir o objeto marca a
  notificação como lida.
- **Rastreio:** §3, item 11.

---

#### 2.1.12 IAA — Assistência automatizada

Reúne as verificações que o sistema executa sobre o artigo. Destas, **apenas `RF-IAA-001` submete o
conteúdo do artigo a serviço externo de inteligência artificial** e depende do consentimento de
`RF-IAA-005`. As demais operam sobre dados do próprio sistema.

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-IAA-001 | Resumir as alterações da entrega | E (proposta) | `DER` |
| RF-IAA-002 | Verificar a conformidade do artigo à norma | E (proposta) | `ELI` |
| RF-IAA-003 | Verificar a similaridade do artigo com o acervo | I (proposta) | `ELI` |
| RF-IAA-004 | Consultar indícios sobre a autoria do texto | I (proposta) | `ELI` |
| RF-IAA-005 | Consentir com o uso de inteligência artificial | E (proposta) | `DER` |

---

##### RF-IAA-001 — Resumir as alterações da entrega

- **Descrição:** apresenta ao orientador, no início da correção de uma etapa, um resumo do que mudou
  desde a entrega anterior, indicando os apontamentos pendentes cujo trecho não sofreu alteração e
  aqueles cuja alteração aparenta não atender ao que foi pedido.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo em `IN_REVIEW`; existir entrega anterior; consentimento institucional
  vigente (`RF-IAA-005`).
- **Fluxo principal:**
  1. O ator abre a correção da etapa.
  2. O sistema submete a comparação (`RF-REV-010`) e os apontamentos pendentes à análise.
  3. O sistema apresenta o resumo das alterações, a lista de apontamentos cujo trecho não mudou e a
     lista de apontamentos cuja alteração aparenta não atender.
  4. O ator decide sobre cada apontamento (`RF-REV-008`).
- **Fluxos alternativos e de exceção:**
  - E1. Consentimento institucional ausente ou revogado → `AI_CONSENT_REQUIRED`; a correção prossegue
    sem o resumo.
  - E2. Serviço indisponível → o sistema informa e a correção prossegue sem o resumo.
- **Regras de negócio:**
  - RN1. O resumo é **subsídio ao orientador**. Não é registrado como apontamento nem apresentado à
    equipe.
  - RN2. O sistema **NÃO DEVE** validar, reabrir, dispensar ou encerrar apontamento a partir da saída
    da análise. A decisão é sempre de `RF-REV-008` (RE-17).
  - RN3. A indisponibilidade da análise **NÃO DEVE** impedir a correção.
  - RN4. A análise recai sobre a diferença entre entregas e sobre os apontamentos pendentes, nunca
    sobre a avaliação do aluno nem sobre a atribuição de nota.
- **Permissões geradas:** `AI_SUMMARY:READ`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. Deriva do volume de orientandos declarado por ambas e da
  verificação manual de atendimento entre etapas.
- **Critério de aceitação:** apontamento cujo trecho não mudou entre duas entregas aparece na lista
  de não atendidos; com o serviço fora do ar, o orientador ainda corrige e devolve normalmente.
- **Rastreio:** M-perfil; A-perfil; M-P4; A-P3.

##### RF-IAA-002 — Verificar a conformidade do artigo à norma

- **Descrição:** permite verificar em que o artigo diverge da norma vigente — formatação, estrutura e
  referências —, apresentando cada divergência ligada ao ponto do texto em que ocorre.
- **Ator:** Aluno integrante, Professor orientador do evento
- **Pré-condições:** artigo existente; ator alcançado pelo vínculo correspondente.
- **Fluxo principal:**
  1. O ator aciona a verificação.
  2. O sistema confronta o artigo com a norma.
  3. O sistema apresenta as divergências, cada uma ligada ao ponto do texto.
  4. O ator corrige — por `RF-EDT-005`, quando for divergência de formatação.
- **Fluxos alternativos e de exceção:**
  - E1. Nenhuma divergência → o sistema informa a conformidade.
- **Regras de negócio:**
  - RN1. A verificação abrange: **formatação** — margem, fonte, entrelinha, recuo, alinhamento,
    paginação, títulos, legendas e citação longa; **estrutura** — seções esperadas do artigo;
    **referências** — formato conforme a norma, citado e não referenciado, referenciado e não citado.
  - RN2. A verificação **aponta**. Não corrige e não bloqueia a entrega.
  - RN3. A verificação cruzada de citações só alcança citações e referências estruturadas
    (`RF-EDT-003`, `RF-EDT-004`).
  - RN4. A norma desta versão é a ABNT.
  - RN5. O template **não** é objeto de verificação: ele é semente, não contrato (RE-16,
    `RF-TPL-001` RN3).
  - RN6. Esta verificação não submete o artigo a serviço externo de inteligência artificial.
- **Permissões geradas:** `COMPLIANCE_CHECK:REQUEST`, `COMPLIANCE_CHECK:READ`
- **Escopo de titularidade:** restrito aos artigos alcançados pelo vínculo do ator.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Angélica declara que a verificação automática de adequação às normas da ABNT é
  condição para a plataforma compensar o tempo de adoção.
- **Critério de aceitação:** obra citada no texto e ausente da lista de referências é apontada, com o
  ponto do texto em que a citação ocorre.
- **Rastreio:** A-P5; M-P5.

##### RF-IAA-003 — Verificar a similaridade do artigo com o acervo

- **Descrição:** permite verificar a similaridade do texto com os artigos já produzidos na
  plataforma, apresentando os trechos coincidentes e a sua origem.
- **Ator:** Aluno integrante, Professor orientador responsável pela equipe
- **Pré-condições:** artigo com conteúdo.
- **Fluxo principal:**
  1. O ator aciona a verificação.
  2. O sistema confronta o texto com o acervo.
  3. O sistema apresenta os trechos coincidentes, a proporção do texto que representam e o artigo de
     origem de cada um.
- **Fluxos alternativos e de exceção:**
  - E1. Acervo vazio ou insuficiente → o sistema informa e nada afirma.
- **Regras de negócio:**
  - RN1. O acervo desta versão é **interno**: os artigos já produzidos na própria plataforma. Serviço
    externo de detecção é expansão prevista — §3, item 16.
  - RN2. A verificação aponta; não acusa. A decisão sobre o que constitui plágio é do orientador.
  - RN3. Citação corretamente referenciada **NÃO DEVE** ser contada como similaridade indevida.
  - RN4. A equipe pode verificar antes de entregar.
  - RN5. O trecho coincidente e a sua origem são apresentados ao orientador; ao aluno é apresentada a
    coincidência no seu próprio texto, sem a identificação da equipe de origem.
- **Permissões geradas:** `SIMILARITY_CHECK:REQUEST`, `SIMILARITY_CHECK:READ`
- **Escopo de titularidade:** restrito aos artigos alcançados pelo vínculo do ator.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Angélica inclui a verificação de plágio entre as verificações automáticas
  desejadas.
- **Critério de aceitação:** trecho copiado de artigo anterior da plataforma é assinalado com a
  origem ao orientador; citação direta devidamente referenciada não é assinalada.
- **Rastreio:** A-P5.

##### RF-IAA-004 — Consultar indícios sobre a autoria do texto

- **Descrição:** apresenta ao orientador os indícios objetivos sobre como o texto foi produzido —
  histórico de edição no sistema e metadados do documento importado —, para subsidiar a conversa com
  a equipe sobre autoria.
- **Ator:** Professor orientador responsável pela equipe
- **Pré-condições:** artigo com histórico de edição.
- **Fluxo principal:**
  1. O ator abre os indícios de autoria do artigo.
  2. O sistema apresenta: inserções de grande volume em ato único, com data e autor; linha do tempo
     das sessões de edição; proporção de texto revisado após a primeira escrita; autoria por
     integrante; e, havendo importação, os metadados do arquivo — tempo total de edição, número de
     revisões, aplicativo de origem e autor declarado.
- **Fluxos alternativos e de exceção:**
  - E1. Histórico insuficiente → o sistema informa e nada afirma.
- **Regras de negócio:**
  - RN1. O sistema apresenta **fatos registrados**, não julgamento. **NÃO DEVE** afirmar nem estimar
    que um texto foi gerado por inteligência artificial.
  - RN2. Nenhum indício, isolado ou combinado, constitui prova de autoria. A saída é subsídio à
    conversa com a equipe.
  - RN3. Os indícios **NÃO DEVEM** ser apresentados à equipe nem gerar sanção automática.
  - RN4. O histórico de edição do próprio sistema (`RF-EDT-008`) é a fonte principal. Os metadados de
    arquivo só existem para o conteúdo importado (`RF-EDT-006`).
  - RN5. Esta verificação não submete o artigo a serviço externo de inteligência artificial.
- **Permissões geradas:** `AUTHORSHIP_SIGNAL:READ`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Angélica inclui a detecção de texto gerado por inteligência artificial entre as
  verificações desejadas. A forma aqui registrada restringe-se a evidência objetiva, por decisão
  expressa de não submeter a questão a julgamento de modelo.
- **Critério de aceitação:** inserção de vinte mil caracteres em ato único aparece na linha do tempo,
  com data e autor; o sistema em nenhum ponto afirma que o texto foi gerado por IA.
- **Rastreio:** A-P5.

##### RF-IAA-005 — Consentir com o uso de inteligência artificial

- **Descrição:** permite ao administrador institucional registrar o consentimento da instituição com
  o processamento do conteúdo dos artigos por serviço externo de inteligência artificial, e revogá-lo.
- **Ator:** Administrador Institucional
- **Pré-condições:** instituição ativa; ator designado a ela.
- **Fluxo principal:**
  1. O sistema apresenta o que é enviado, com que finalidade e a que serviço.
  2. O ator registra ou revoga o consentimento.
  3. O sistema registra a decisão, o autor e a data.
- **Fluxos alternativos e de exceção:**
  - E1. Instituição inativa → `INSTITUTION_INACTIVE`.
- **Regras de negócio:**
  - RN1. Sem consentimento vigente, o conteúdo do artigo **NÃO DEVE** ser submetido a serviço externo
    de inteligência artificial. `RF-IAA-001` fica indisponível; as demais funções do sistema seguem
    íntegras.
  - RN2. O consentimento é por instituição e alcança todos os seus artigos.
  - RN3. A revogação vale a partir do registro e não desfaz o que já foi processado.
  - RN4. O registro é auditável: quem consentiu, quando, e o que estava declarado no momento.
- **Permissões geradas:** `INSTITUTION:CONSENT_AI`
- **Escopo de titularidade:** restrito à instituição a que o ator está designado.
- **Prioridade:** E (proposta)
- **Origem:** `DER` — definição de produto. O envio do artigo a terceiro é decisão da instituição,
  não da equipe nem do orientador.
- **Critério de aceitação:** sem consentimento, o orientador corrige e devolve normalmente e o resumo
  não é oferecido; revogado o consentimento, o resumo deixa de ser gerado a partir daquele instante.
- **Rastreio:** §3, item 12.

---

#### 2.1.13 ACP — Acompanhamento e relatórios

Reúne o que se observa **sobre** o ciclo, sem interferir nele. Nenhum requisito desta categoria
altera o artigo, o apontamento ou a nota: todos apresentam o que já foi registrado pelas categorias
anteriores.

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-ACP-001 | Acompanhar as equipes sob orientação | E (proposta) | `ELI` |
| RF-ACP-002 | Acompanhar os eventos e as equipes do curso | I (proposta) | `DER` |
| RF-ACP-003 | Sinalizar equipe parada ou em risco | E (proposta) | `ELI` |
| RF-ACP-004 | Consultar a contribuição de cada integrante | I (proposta) | `DER` |
| RF-ACP-005 | Gerar o relatório de produção do curso | I (proposta) | `ELI` |
| RF-ACP-006 | Exportar o relatório | D (proposta) | `DER` |

---

##### RF-ACP-001 — Acompanhar as equipes sob orientação

- **Descrição:** apresenta ao orientador, em uma única tela, a situação de todas as equipes de que é
  orientador responsável, de modo que ele perceba quem está parado ou atrasado sem precisar abrir
  artigo por artigo.
- **Ator:** Professor orientador responsável
- **Pré-condições:** ator designado orientador responsável por ao menos uma equipe.
- **Fluxo principal:**
  1. O ator abre o acompanhamento.
  2. O sistema apresenta, para cada equipe sob a sua responsabilidade: o evento, os integrantes, o
     estado do artigo, a etapa corrente e o seu prazo, se a etapa foi entregue e se a entrega foi
     espontânea ou automática, a quantidade de apontamentos pendentes e o tempo decorrido desde a
     última edição do artigo.
  3. O sistema destaca as equipes com sinal ativo (`RF-ACP-003`).
  4. O ator ordena e filtra a lista, e navega dali para o artigo, para a correção ou para a
     discussão da equipe.
- **Fluxos alternativos e de exceção:**
  - E1. Ator sem equipe sob responsabilidade → o sistema apresenta a tela vazia, com a informação de
    que não há equipes designadas a ele.
- **Regras de negócio:**
  - RN1. O acompanhamento alcança apenas as equipes de que o ator é orientador **responsável**, não
    todas as do evento. A visão das demais permanece a de `RF-ART-001`.
  - RN2. O acompanhamento apresenta o que já foi registrado. **NÃO DEVE** oferecer ação que altere o
    artigo, o apontamento ou a nota; ele leva às telas que as executam.
  - RN3. O tempo desde a última edição conta a partir da última alteração do texto por qualquer
    integrante (`RF-EDT-001`), não da última mensagem da discussão.
  - RN4. A composição da tela, os recortes e a apresentação são decisão de implementação, desde que
    os dados enumerados no fluxo principal estejam presentes.
- **Permissões geradas:** `PROGRESS:READ`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — Marciele relata a percepção tardia de alunos travados ou atrasados. O volume
  declarado por ambas — cerca de 35 orientandos simultâneos e mais de 50 por semestre — torna
  inviável a verificação artigo por artigo.
- **Critério de aceitação:** o orientador identifica, sem abrir nenhum artigo, quais das suas equipes
  não entregaram a etapa corrente e quais estão sem edição há mais tempo; equipe de outro orientador
  do mesmo evento não aparece na lista.
- **Rastreio:** M-P3; M-perfil; A-perfil.

##### RF-ACP-002 — Acompanhar os eventos e as equipes do curso

- **Descrição:** apresenta ao coordenador a situação dos eventos do seu curso e das equipes que
  participam deles, com o andamento agregado por evento.
- **Ator:** Coordenador do curso
- **Pré-condições:** ator designado coordenador de um curso com eventos.
- **Fluxo principal:**
  1. O ator abre o acompanhamento do curso.
  2. O sistema apresenta os eventos do curso e, para cada um, o cronograma, a quantidade de equipes,
     quantas entregaram a etapa corrente, quantas têm sinal ativo e quantos artigos já foram
     concluídos.
  3. O ator abre um evento e vê as suas equipes, com os mesmos dados de `RF-ACP-001`.
- **Fluxos alternativos e de exceção:**
  - E1. Curso sem evento no período → o sistema apresenta a tela vazia e informa.
- **Regras de negócio:**
  - RN1. O alcance é o **curso** do ator: os eventos de escopo de curso que ele coordena, os de
    escopo de turma das turmas desse curso e os de escopo institucional que alcancem o seu curso.
  - RN2. O coordenador vê a situação das equipes, mas **não** participa da discussão nem do ciclo de
    apontamentos (`RF-DSC-001` RN2).
  - RN3. Vale para esta tela a RN2 de `RF-ACP-001`: apresenta, não altera.
  - RN4. A composição e a apresentação são decisão de implementação.
- **Permissões geradas:** `PROGRESS:READ` — a mesma de `RF-ACP-001`; o alcance é resolvido pela
  titularidade, conforme `ADR-0014` §12.
- **Escopo de titularidade:** restrito aos eventos e equipes do curso que o ator coordena.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — deriva de `RF-CUR-002` RN2, que identifica o coordenador como destinatário do
  acompanhamento. O coordenador não foi entrevistado — §3, item 5.
- **Critério de aceitação:** coordenador de um curso não alcança evento de outro curso da mesma
  instituição; abrir um evento seu lista as suas equipes com o mesmo detalhe do painel do orientador.
- **Rastreio:** M-P9; §3, item 5.

##### RF-ACP-003 — Sinalizar equipe parada ou em risco

- **Descrição:** identifica automaticamente as equipes cuja situação exige atenção e avisa o
  orientador responsável, sem depender de que ele vá procurar.
- **Ator:** Sistema; Professor orientador responsável como destinatário
- **Pré-condições:** equipe com artigo em evento em andamento.
- **Fluxo principal:**
  1. O sistema avalia continuamente a situação de cada equipe.
  2. Ao identificar uma condição de risco, o sistema ativa o sinal na equipe.
  3. O sistema notifica o orientador responsável (`RF-DSC-005`).
  4. O sinal é apresentado em `RF-ACP-001` e em `RF-ACP-002`.
  5. Cessada a condição, o sistema desativa o sinal.
- **Fluxos alternativos e de exceção:**
  - E1. Condição já sinalizada e ainda ativa → o sistema não notifica de novo.
- **Regras de negócio:**
  - RN1. O sistema DEVE detectar, no mínimo: artigo sem edição por período prolongado; entrega
    automática por vencimento de prazo (`RF-REV-003`) em duas etapas seguidas; apontamentos
    pendentes acumulados sem atendimento entre etapas; integrante que nunca editou o artigo;
    proximidade do prazo da etapa com o artigo sem alteração desde a devolução anterior.
  - RN2. Os limiares de cada condição são decisão de implementação. O que esta URS fixa são as
    condições a detectar, não os seus valores.
  - RN3. O sinal é **subsídio**. **NÃO DEVE** alterar o estado do artigo, gerar apontamento, afetar
    nota nem produzir sanção automática (RE-17).
  - RN4. O sinal é dirigido ao orientador responsável e ao coordenador do curso. **NÃO DEVE** ser
    apresentado à equipe: ele é instrumento de intervenção do orientador, não de cobrança
    automatizada.
  - RN5. O sinal cessa sozinho quando a condição deixa de valer; não é encerrado manualmente.
- **Permissões geradas:** `RISK_SIGNAL:READ`
- **Escopo de titularidade:** restrito às equipes alcançadas pelo vínculo do ator — responsabilidade
  de orientação ou coordenação do curso.
- **Prioridade:** E (proposta)
- **Origem:** `ELI` — é o atendimento direto da percepção tardia relatada por Marciele. O painel de
  `RF-ACP-001` só ajuda quem foi olhar; o sinal vai até o orientador.
- **Critério de aceitação:** equipe sem edição pelo período definido tem sinal ativo e o orientador
  recebe a notificação uma única vez; retomada a edição, o sinal cessa sem intervenção.
- **Rastreio:** M-P3; M-perfil; A-perfil.

##### RF-ACP-004 — Consultar a contribuição de cada integrante

- **Descrição:** apresenta ao orientador a participação de cada integrante na produção do artigo,
  para subsidiar a avaliação individual.
- **Ator:** Professor orientador responsável
- **Pré-condições:** artigo com histórico de edição; ator orientador responsável pela equipe.
- **Fluxo principal:**
  1. O ator abre a contribuição da equipe.
  2. O sistema apresenta, por integrante, a proporção do texto de sua autoria, as sessões de edição,
     o atendimento a apontamentos (`RF-REV-007`) e a participação na discussão.
  3. O ator usa o quadro ao atribuir a nota individual (`RF-ART-003`).
- **Fluxos alternativos e de exceção:**
  - E1. Artigo importado de documento externo, sem histórico próprio → o sistema informa que a maior
    parte do texto não foi produzida na plataforma e nada afirma sobre a divisão do trabalho.
- **Regras de negócio:**
  - RN1. A contribuição é **subsídio** à avaliação. O sistema **NÃO DEVE** sugerir nota, calcular
    nota nem ordenar os integrantes por desempenho (RE-17).
  - RN2. Volume de texto não é medida de contribuição. A apresentação DEVE deixar isso explícito ao
    orientador.
  - RN3. O quadro é visível ao orientador responsável e **NÃO DEVE** ser apresentado aos integrantes
    da equipe.
  - RN4. A fonte é o histórico de edição (`RF-EDT-008`) e a autoria por trecho registrada em
    `RF-EDT-002` RN3.
- **Permissões geradas:** `CONTRIBUTION:READ`
- **Escopo de titularidade:** restrito às equipes de que o ator é orientador responsável.
- **Prioridade:** I (proposta)
- **Origem:** `DER` — deriva de RE-09 e de `RF-ART-003`, que exigem nota individual, e de
  `RF-EDT-002` RN3, que já registra a autoria por trecho. Nenhuma entrevistada pediu o quadro; ambas
  atribuem nota individual.
- **Critério de aceitação:** integrante que nunca editou o artigo aparece com contribuição nula no
  quadro; o quadro não é alcançável por nenhum aluno.
- **Rastreio:** RE-09; M-P3; A-P3.

##### RF-ACP-005 — Gerar o relatório de produção do curso

- **Descrição:** gera, para um curso e um período, o relatório consolidado da produção acadêmica, a
  ser prestado à coordenação.
- **Ator:** Coordenador do curso, Administrador Institucional
- **Pré-condições:** curso com ao menos um evento encerrado ou em andamento no período.
- **Fluxo principal:**
  1. O ator seleciona o curso e o período.
  2. O sistema consolida os dados registrados no período.
  3. O sistema apresenta o relatório.
- **Fluxos alternativos e de exceção:**
  - E1. Período sem dados → o sistema gera o relatório vazio, informando a ausência de produção. Não
    é erro.
  - E2. Consolidação ainda em curso → `REPORT_NOT_READY`.
  - E3. Curso fora do alcance do ator → `PERMISSION_DENIED`.
- **Regras de negócio:**
  - RN1. O relatório DEVE responder, no mínimo:
    - quantas equipes o curso teve no período, por evento;
    - quantos artigos foram concluídos e quantos não;
    - quantos alunos participaram;
    - qual o desempenho, pela nota do artigo e pelas notas individuais (`RF-ART-002`,
      `RF-ART-003`);
    - quantas publicações externas foram registradas (`RF-ART-004`);
    - quais equipes ficaram para trás e em que etapa.
  - RN2. **A composição do relatório, os recortes, os agrupamentos, os dados adicionais e a
    apresentação são decisão de implementação.** Esta URS fixa as perguntas que o relatório precisa
    responder, não as suas colunas. Acrescentar dado que amplie a resposta é conforme; deixar
    pergunta da RN1 sem resposta não é.
  - RN3. O relatório é apuração do que foi registrado. **NÃO DEVE** conter juízo, projeção nem
    recomendação produzidos pelo sistema.
  - RN4. O período é o do calendário do curso, delimitado pelos eventos nele contidos.
  - RN5. O relatório não alcança o conteúdo do artigo, os apontamentos nem a discussão das equipes.
- **Permissões geradas:** `REPORT:GENERATE`, `REPORT:READ`
- **Escopo de titularidade:** restrito ao curso que o ator coordena; para o Administrador
  Institucional, aos cursos da sua instituição.
- **Prioridade:** I (proposta)
- **Origem:** `ELI` — Marciele identifica o coordenador do curso como destinatário do relatório de
  pesquisa, hoje consolidado manualmente a cada semestre.
- **Critério de aceitação:** para um curso com dois eventos no período, o relatório responde às seis
  perguntas da RN1; período sem produção gera relatório vazio, e não erro.
- **Rastreio:** M-P9; §3, item 5.

##### RF-ACP-006 — Exportar o relatório

- **Descrição:** permite obter o relatório como arquivo, para envio e arquivamento fora do sistema.
- **Ator:** Coordenador do curso, Administrador Institucional
- **Pré-condições:** relatório gerado (`RF-ACP-005`).
- **Fluxo principal:**
  1. O ator escolhe o formato.
  2. O sistema gera o arquivo e o entrega ao ator.
- **Fluxos alternativos e de exceção:**
  - E1. Relatório ainda em consolidação → `REPORT_NOT_READY`.
- **Regras de negócio:**
  - RN1. O arquivo exportado reproduz o relatório apresentado, sem acrescentar nem omitir dado.
  - RN2. Os formatos oferecidos são decisão de implementação.
- **Permissões geradas:** `REPORT:EXPORT`
- **Escopo de titularidade:** o mesmo de `RF-ACP-005`.
- **Prioridade:** D (proposta)
- **Origem:** `DER` — deriva de `RF-ACP-005`: o relatório é prestado a terceiro, e a prestação
  pressupõe documento destacável do sistema.
- **Critério de aceitação:** o arquivo exportado contém as mesmas respostas apresentadas na tela.
- **Rastreio:** M-P9.

---

#### 2.1.14 INT — Internacionalização

| ID | Nome | Prior. | Origem |
| :--- | :--- | :--: | :--: |
| RF-INT-001 | Selecionar o idioma da interface | D (proposta) | `DER` |

---

##### RF-INT-001 — Selecionar o idioma da interface

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
- **Rastreio:** §3, item 9; `ADR-0026` §3, §11, §25–§27; `PAD-REQ-008`; `ADR-0025` §20.

---

### 2.2 Requisitos Não Funcionais

**Não existe requisito não funcional nesta URS, e a ausência é deliberada.**

Um requisito só entra nesta URS se tiver origem em parte interessada (1. e `PAD-REQ-004`). Nenhuma
das entrevistadas declarou exigência de desempenho, disponibilidade, segurança ou tecnologia: tudo o
que ocuparia esta seção é decisão da equipe, e decisão da equipe registrada como requisito do
usuário é falseamento de origem.

Esses itens existem, são normativos e são verificados em revisão de código — apenas moram em
[`Padroes/Padroes-de-Engenharia.md`](../Padroes/Padroes-de-Engenharia.md), no formato
`PAD-<CATEGORIA>-<NNN>`, cada um rastreado até o ADR que o originou:

| Categoria | Domínio | Itens |
| :--- | :--- | :--: |
| `MOD` | Modularidade e manutenibilidade | 18 |
| `EVO` | Evolutividade e capacidade de extração | 12 |
| `ESC` | Escalabilidade e desempenho | 17 |
| `CON` | Confiabilidade e integridade | 22 |
| `OBS` | Observabilidade | 13 |
| `SEG` | Segurança | 25 |
| `VER` | Verificação e qualidade | 12 |
| `REQ` | Especificação de requisitos | 8 |
| `NOM` | Nomeação e internacionalização | 15 |
| `TEC` | Restrição tecnológica imposta | 16 |
| | **Total** | **158** |

Se alguma parte interessada vier a declarar exigência não funcional — prazo de resposta, janela de
indisponibilidade tolerada, exigência de auditoria —, ela passa a ter origem `ELI` ou `STK` e entra
aqui, com quadro próprio, sem sair dos Padrões.

---

### 2.3 Catálogo de permissões

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
| `TEMPLATE:CREATE` | RF-TPL-001 |
| `TEMPLATE:READ` | RF-TPL-001, RF-TPL-002 |
| `TEMPLATE:UPDATE` | RF-TPL-001 |
| `TEMPLATE:DEACTIVATE` | RF-TPL-001 |
| `ARTICLE:EDIT` | RF-EDT-001, RF-EDT-002 |
| `ARTICLE:FORMAT` | RF-EDT-005 |
| `ARTICLE:IMPORT` | RF-EDT-006 |
| `ARTICLE:EXPORT` | RF-EDT-007 |
| `ARTICLE:READ_HISTORY` | RF-EDT-008 |
| `ARTICLE:RESTORE_VERSION` | RF-EDT-008 |
| `ARTICLE:RETURN` | RF-REV-006 |
| `ARTICLE:CONCLUDE` | RF-REV-011 |
| `REFERENCE:CREATE` | RF-EDT-003 |
| `REFERENCE:READ` | RF-EDT-003 |
| `REFERENCE:UPDATE` | RF-EDT-003 |
| `REFERENCE:DELETE` | RF-EDT-003 |
| `REFERENCE:CITE` | RF-EDT-004 |
| `SUBMISSION:CREATE` | RF-REV-001 |
| `SUBMISSION:READ` | RF-REV-001 |
| `SUBMISSION:REVOKE` | RF-REV-002 |
| `SUBMISSION:COMPARE` | RF-REV-010 |
| `REMARK:CREATE` | RF-REV-004 |
| `REMARK:READ` | RF-REV-004, RF-REV-009 |
| `REMARK:UPDATE` | RF-REV-005 |
| `REMARK:ADDRESS` | RF-REV-007 |
| `REMARK:RESOLVE` | RF-REV-008 |
| `REMARK:REOPEN` | RF-REV-008 |
| `REMARK:DISMISS` | RF-REV-008 |
| `MESSAGE:CREATE` | RF-DSC-001, RF-DSC-003 |
| `MESSAGE:READ` | RF-DSC-001, RF-DSC-004 |
| `MESSAGE:REPLY` | RF-DSC-002 |
| `MESSAGE:DELETE` | RF-DSC-001 |
| `NOTIFICATION:READ` | RF-DSC-005 |
| `NOTIFICATION:MARK_READ` | RF-DSC-006 |
| `AI_SUMMARY:READ` | RF-IAA-001 |
| `COMPLIANCE_CHECK:REQUEST` | RF-IAA-002 |
| `COMPLIANCE_CHECK:READ` | RF-IAA-002 |
| `SIMILARITY_CHECK:REQUEST` | RF-IAA-003 |
| `SIMILARITY_CHECK:READ` | RF-IAA-003 |
| `AUTHORSHIP_SIGNAL:READ` | RF-IAA-004 |
| `INSTITUTION:CONSENT_AI` | RF-IAA-005 |
| `PROGRESS:READ` | RF-ACP-001, RF-ACP-002 |
| `RISK_SIGNAL:READ` | RF-ACP-003 |
| `CONTRIBUTION:READ` | RF-ACP-004 |
| `REPORT:GENERATE` | RF-ACP-005 |
| `REPORT:READ` | RF-ACP-005 |
| `REPORT:EXPORT` | RF-ACP-006 |

#### 2.3.1 Composição dos papéis padrão

Os papéis são criados pela carga inicial com a composição abaixo. O papel autoriza a ação; o alcance
sobre registros específicos é resolvido pela titularidade declarada em cada requisito.

| Papel | Permissões |
| :--- | :--- |
| `SYSTEM_ADMIN` | `INSTITUTION:CREATE`, `INSTITUTION:READ`, `INSTITUTION:UPDATE`, `INSTITUTION:DEACTIVATE`, `INSTITUTION:ASSIGN_ADMIN`, `INSTITUTION:REVOKE_ADMIN` |
| `INSTITUTION_ADMIN` | `COURSE:CREATE/READ/UPDATE/DEACTIVATE`, `COURSE:ASSIGN_COORDINATOR`, `COURSE:REVOKE_COORDINATOR`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:ASSIGN_ADVISOR`, `TEAM:REVOKE_ADVISOR`, `TEMPLATE:CREATE/READ/UPDATE/DEACTIVATE`, `INSTITUTION:CONSENT_AI`, `REPORT:GENERATE`, `REPORT:READ`, `REPORT:EXPORT` |
| `COORDINATOR` | `COHORT:CREATE/READ/UPDATE/DEACTIVATE`, `COHORT:ASSIGN_PROFESSOR`, `COHORT:REVOKE_PROFESSOR`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:ASSIGN_ADVISOR`, `TEAM:REVOKE_ADVISOR`, `ARTICLE:READ`, `ARTICLE:EXPORT`, `PUBLICATION:READ`, `TEMPLATE:CREATE/READ/UPDATE/DEACTIVATE`, `SUBMISSION:READ`, `PROGRESS:READ`, `RISK_SIGNAL:READ`, `REPORT:GENERATE`, `REPORT:READ`, `REPORT:EXPORT` |
| `PROFESSOR` | `ENROLLMENT:CREATE`, `ENROLLMENT:READ`, `INVITATION:CREATE/READ/REVOKE`, `EVENT:CREATE/READ/UPDATE/CANCEL`, `EVENT:ASSIGN_ADVISOR`, `EVENT:REVOKE_ADVISOR`, `MILESTONE:CREATE/READ/UPDATE/DELETE`, `TEAM:CREATE/READ`, `TEAM:ASSIGN_MEMBER`, `TEAM:REMOVE_MEMBER`, `TEAM:INVITE_MEMBER`, `ARTICLE:READ`, `ARTICLE:GRADE`, `ARTICLE:GRADE_MEMBER`, `PUBLICATION:CREATE/READ/UPDATE/DELETE`, `PERMISSION_GRANT:CREATE`, `PERMISSION_GRANT:REVOKE`, `PERMISSION_GRANT:READ`, `COHORT:READ`, `COURSE:READ`, `TEMPLATE:READ`, `ARTICLE:EXPORT`, `ARTICLE:RETURN`, `ARTICLE:CONCLUDE`, `SUBMISSION:READ`, `SUBMISSION:COMPARE`, `REMARK:CREATE/READ/UPDATE/RESOLVE/REOPEN/DISMISS`, `MESSAGE:CREATE/READ/REPLY/DELETE`, `NOTIFICATION:READ`, `NOTIFICATION:MARK_READ`, `AI_SUMMARY:READ`, `COMPLIANCE_CHECK:REQUEST/READ`, `SIMILARITY_CHECK:REQUEST/READ`, `AUTHORSHIP_SIGNAL:READ`, `PROGRESS:READ`, `RISK_SIGNAL:READ`, `CONTRIBUTION:READ` |
| `STUDENT` | `EVENT:READ`, `MILESTONE:READ`, `TEAM:READ`, `TEAM:JOIN`, `ARTICLE:READ`, `PUBLICATION:CREATE/READ/UPDATE`, `COHORT:READ`, `ARTICLE:EDIT`, `ARTICLE:FORMAT`, `ARTICLE:IMPORT`, `ARTICLE:EXPORT`, `ARTICLE:READ_HISTORY`, `ARTICLE:RESTORE_VERSION`, `REFERENCE:CREATE/READ/UPDATE/DELETE`, `REFERENCE:CITE`, `SUBMISSION:CREATE/READ/REVOKE/COMPARE`, `REMARK:READ`, `REMARK:ADDRESS`, `MESSAGE:CREATE/READ/REPLY/DELETE`, `NOTIFICATION:READ`, `NOTIFICATION:MARK_READ`, `COMPLIANCE_CHECK:REQUEST/READ`, `SIMILARITY_CHECK:REQUEST/READ` |

A notação `A/B/C` acima abrevia a leitura desta tabela e **não** existe no catálogo: as permissões
efetivas são sempre enumeradas, sem curinga (`ADR-0014` §3).

---

### 2.4 Catálogo de códigos de resposta

Em maiúsculas, sem acento, independentes de idioma (`PAD-REQ-008`, `ADR-0025` §20). A tradução para
exibição ocorre no cliente, a partir do código.

| Código | Origem |
| :--- | :--- |
| `AUTHENTICATION_FAILED` | RF-ACS-001 |
| `INSTITUTION_INACTIVE` | RF-ACS-001, RF-INS-001, RF-INS-002, RF-IAA-005 |
| `VALIDATION_FAILED` | RF-ACS-004, RF-ACS-005, RF-INS-001, RF-CUR-001, RF-TUR-001, RF-TUR-004, RF-TUR-005, RF-EVT-001, RF-EVT-002, RF-EQP-001, RF-EQP-002, RF-ART-002, RF-ART-003, RF-ART-004, RF-TPL-001, RF-EDT-003, RF-DSC-001 |
| `PERMISSION_DENIED` | RF-ACP-005, RF-ACS-005, RF-CUR-001, RF-CUR-002, RF-TUR-001, RF-TUR-002, RF-TUR-003, RF-TUR-004, RF-EVT-002, RF-EVT-003, RF-EQP-005, RF-ART-002, RF-ART-003, RF-TPL-001, RF-REV-004, RF-REV-005, RF-REV-006, RF-REV-008, RF-REV-011 |
| `RESOURCE_NOT_FOUND` | RF-ACS-006, RF-ACS-007, RF-ACS-008, RF-INS-002, RF-CUR-002, RF-EVT-001, RF-EVT-004, RF-ART-001, RF-ART-004, RF-TPL-002, RF-EDT-001, RF-EDT-004, RF-EDT-007, RF-REV-002, RF-DSC-001, RF-DSC-003, RF-DSC-006 |
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
| `TEMPLATE_ALREADY_FIXED` | RF-TPL-002 |
| `ARTICLE_LOCKED_FOR_REVIEW` | RF-EDT-001, RF-EDT-008, RF-REV-001, RF-REV-007 |
| `ARTICLE_ALREADY_FINISHED` | RF-EDT-001, RF-REV-001 |
| `ARTICLE_NOT_IN_REVIEW` | RF-REV-004, RF-REV-006, RF-REV-008 |
| `REFERENCE_IN_USE` | RF-EDT-003 |
| `FILE_FORMAT_NOT_SUPPORTED` | RF-EDT-006 |
| `FILE_TOO_LARGE` | RF-EDT-006 |
| `SUBMISSION_ALREADY_MADE` | RF-REV-001 |
| `MILESTONE_NOT_OPEN` | RF-REV-001 |
| `MILESTONE_DEADLINE_PASSED` | RF-REV-002 |
| `MILESTONE_PENDING` | RF-REV-011 |
| `REVIEW_ALREADY_STARTED` | RF-REV-002 |
| `REMARK_ALREADY_CLOSED` | RF-REV-005, RF-REV-007, RF-REV-008 |
| `REMARK_PENDING` | RF-REV-011 |
| `AI_CONSENT_REQUIRED` | RF-IAA-001 |
| `REPORT_NOT_READY` | RF-ACP-005, RF-ACP-006 |

---

## 3. Pendências

| # | Pendência | Efeito |
| :--- | :--- | :--- |
| 1 | **Prioridades não atribuídas por parte interessada.** Nenhum requisito desta versão teve prioridade atribuída pelas entrevistadas; os valores registrados são propostas da equipe. | Viola `PAD-REQ-003`. Por `PAD-REQ-006`, nenhum requisito desta versão deve ser encaminhado à implementação antes da ratificação. |
| 2 | **Requisitos `DER` não validados.** A hierarquia institucional, a autenticação, a cadeia de criação de usuários e boa parte da fatia de produção do artigo derivam da definição de produto, não de solicitação direta — ver item 11. | Por `PAD-REQ-004`, não são considerados acordados antes de validação com as partes interessadas. |
| 3 | **Radar de eventos externos adiado.** Marciele nomeou, em P10, duas condições obrigatórias para a plataforma valer o tempo de aprendizado: apoio às correções e busca de eventos. A segunda foi adiada por decisão de escopo. Em P5 ela descreve o item como externo — "radar de eventos científicos, congressos e periódicos" com prazo, temática, requisitos e links, e o trabalho manual de "identificação de eventos e periódicos adequados à temática" e "repasse dessas oportunidades aos alunos". O congresso interno aparece separadamente, como template já conhecido. | Requisito elicitado, conhecido e não atendido. `RF-ART-004` o atende parcialmente ao permitir o registro manual da publicação externa. O módulo de correção passa a sustentar sozinho o caso de adoção dessa parte interessada. |
| 4 | **Um usuário por instituição.** Quem atua em mais de uma instituição usa contas e e-mails distintos. | Decisão de escopo. Expansão prevista. |
| 5 | **Coordenador não será entrevistado.** Decisão de escopo. O que o sistema deve prestar à coordenação foi derivado de `RF-CUR-002` RN2 e de M-P9, sem confirmação do destinatário. | `RF-ACP-002` e `RF-ACP-005` nascem `DER` sem validação possível pelo destinatário. Ninguém conferirá se o relatório responde ao que a coordenação de fato pergunta. `RF-ACP-005` RN1 fixa as perguntas mínimas justamente para que a lacuna não fique implícita. |
| 5.1 | **Aluno não entrevistado.** O aluno é ator de mais de vinte requisitos desta URS e a sua visão consta apenas em terceira pessoa, pela fala das duas orientadoras. | Pendência aberta, distinta do item 5: não houve decisão de não entrevistá-lo. Recomenda-se rodada de elicitação antes da implementação da fatia de edição. |
| 6 | **Cobertura de área.** Ambas as entrevistadas são do curso de Administração. As normas registradas se limitam a ABNT e ao template do congresso interno. | Outras áreas podem exigir normas distintas, ainda sem evidência. |
| 7 | **Coordenador único por curso.** Registrado como RN1 de `RF-CUR-002` sem evidência que o confirme. | Premissa a confirmar. |
| 8 | **Divergência de visibilidade (P8).** Marciele defende que qualquer professor da instituição veja o trabalho em qualquer fase; Angélica restringe a orientadores e autores. Esta versão implementa a posição restritiva. | Se a posição ampla prevalecer, será necessária permissão de leitura em escopo institucional, hoje inexistente. |
| 9 | **Idiomas.** Apenas português do Brasil no lançamento; nenhuma parte interessada solicitou idioma adicional. | `RF-INT-001` permanece `DER` até validação. A estratégia técnica está fixada em `ADR-0026` e nos padrões `PAD-NOM-001` a `PAD-NOM-014`; resta apenas a validação do requisito com as partes interessadas. |
| 10 | **Conteúdo do relatório e limiares dos sinais deixados à implementação.** `RF-ACP-005` RN2 fixa as perguntas que o relatório responde, não as suas colunas; `RF-ACP-003` RN2 fixa as condições a detectar, não os seus limiares. | Decisão deliberada, e não omissão. O critério de aceitação recai sobre as perguntas e as condições, que são verificáveis. O risco é a implementação responder às perguntas de forma que não sirva ao destinatário — agravado pelo item 5. |
| 11 | **Fatia de produção sem elicitação direta.** A edição do artigo no sistema, a edição simultânea, a discussão, as notificações, a comparação de versões e o resumo automático são definição de produto. O que a elicitação sustenta diretamente é o apontamento no texto (M-P4), a verificação de conformidade e de plágio (A-P5) e o template do congresso (M-P5). | Por `PAD-REQ-004`, esses requisitos não são considerados acordados antes de validação. É a maior concentração de `DER` da URS. |
| 12 | **Envio de conteúdo a terceiro.** `RF-IAA-001` submete o texto do artigo a serviço externo de inteligência artificial. `RF-IAA-005` exige consentimento institucional, mas o teor do consentimento, a base legal e o serviço a contratar não estão definidos. | Bloqueia `RF-IAA-001` em produção até que sejam. Nenhum outro requisito depende disso. |
| 13 | **Sem canal privado entre professores.** Toda mensagem da discussão é visível à equipe (`RF-DSC-001` RN4). | Decisão de escopo. Expansão prevista, a nascer junto do modelo de discussão caso seja adotada. |
| 14 | **Norma única.** Só a ABNT é verificada e aplicada. O template é semente e não é verificado (RE-16), de modo que exigência própria do congresso interno divergente da ABNT não é conferida por ninguém. | Consequência conhecida da decisão de tratar template como semente. Ver também item 6. |
| 15 | **Sem prorrogação individual de prazo.** `RF-REV-003` congela toda equipe sem entrega no vencimento, sem exceção. | Decisão de escopo. |
| 16 | **Acervo de similaridade interno.** `RF-IAA-003` confronta o artigo apenas com os já produzidos na plataforma. Nas primeiras turmas o acervo é pequeno e a verificação vale pouco. | Efeito conhecido e aceito. Serviço externo é expansão prevista. |
| 17 | **Coedição simultânea — risco de viabilidade.** `RF-EDT-002` exige reconciliar edições concorrentes sem perda e sem escolha manual. É o maior item de engenharia desta URS e não tem paralelo no restante do sistema. | Risco declarado, decisão tomada com o custo à vista. Exige ADR próprio antes da implementação. |

---

## 4. Controle de versão

| Versão | Data | Justificativa | Responsável |
| :--- | :--- | :--- | :--- |
| 0.4 | 2026-08-26 | Documento adequado ao padrão institucional de especificação de requisitos: capa, controle de versão, quadro por requisito e termo de aceite. O conteúdo normativo não mudou — nenhum requisito foi acrescentado, removido ou reescrito. A numeração das seções passa a seguir o padrão: 1 Objetivo do Documento, 2 Lista de Requisitos, 3 Pendências, 4 Controle de versão, 5 Aceite; o que era seção de primeiro nível passa a subseção de 1 e de 2. Acrescentada a seção 2.2, que registra por que não há requisito não funcional nesta URS. | Vitor Fernandes |
| 0.3 | 2026-08-26 | Registrada a fatia de acompanhamento e relatórios: categoria `ACP`, 6 requisitos funcionais, 6 permissões e 1 código de resposta. `INT` passa de §7.13 a §7.14. Com ela o escopo funcional se fecha: 70 requisitos em 14 categorias. `RF-ACP-003` e `RF-ACP-005` fixam as condições a detectar e as perguntas a responder, deixando limiares e composição à implementação. A pendência 5 passa a registrar a decisão de não entrevistar o coordenador, e a visão do aluno é separada nela como item 5.1. A pendência 10 deixa de designar a fatia faltante e passa a registrar o que foi deixado à implementação. | Vitor Fernandes |
| 0.2 | 2026-08-25 | Registrada a fatia de produção e correção do artigo: 5 categorias novas — `TPL`, `EDT`, `REV`, `DSC`, `IAA` —, 32 requisitos funcionais, 8 regras estruturais (RE-10 a RE-17), 41 permissões e 15 códigos de resposta. O modelo de domínio passa a incluir Template, Referência, Citação, Discussão, Mensagem, Entrega e Apontamento. `INT` passa de §7.8 a §7.13. Pendências 11 a 17 acrescentadas; a pendência 10 passa a designar a fatia de acompanhamento e relatórios. | Vitor Fernandes |
| 0.1 | 2026-08-19 | Registrada a fatia estrutural: 8 categorias, 32 requisitos funcionais, catálogo de 51 permissões e catálogo de 20 códigos de resposta, com rastreabilidade às entrevistas de Marciele e Angélica. Os catálogos de permissões e de códigos passam a existir, atendendo às pendências correspondentes de `Padroes-de-Engenharia.md` §6 no que se refere a esta fatia. Prioridades registradas como proposta, pendentes de atribuição por parte interessada. | Vitor Fernandes |
| 0.0 | 2026-08-13 | Documento zerado. Todo o conteúdo das versões 0.1 a 0.9.1 era decisão da própria equipe, não requisito de parte interessada, e foi movido para `Padroes/Padroes-de-Engenharia.md`. A URS recomeça vazia, a ser elaborada a partir da elicitação. O histórico anterior está no versionamento do repositório. | Vitor Fernandes |

---

## 5. Aceite

As partes interessadas abaixo declaram que os requisitos especificados neste documento correspondem
ao que necessitam do sistema.

O aceite é a ratificação de que trata `PAD-REQ-003` e `PAD-REQ-006`: com ele, as prioridades
registradas em 2.1 deixam de ser proposta da equipe e os requisitos de origem `DER` passam a ser
considerados acordados. **Enquanto não houver aceite, nenhum requisito desta versão deve ser
encaminhado à implementação** — ver 3, itens 1, 2 e 11.





&nbsp;

&nbsp;

_____________________________________________ Aceito em ____/____/________

Marciele R. Siveres — Orientadora, curso de Administração





&nbsp;

&nbsp;

_____________________________________________ Aceito em ____/____/________

Angélica P. S. Meurer — Orientadora, curso de Administração
