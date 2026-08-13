# VinceArt — Formulário de Elicitação de Requisitos
## Público-alvo: Professores Orientadores

---

## 1. Identificação do Projeto

| Campo | Descrição |
|---|---|
| **Projeto** | VinceArt |
| **Documento** | Formulário de Elicitação de Requisitos — Stakeholder: Professor Orientador |
| **Versão** | 1.0 |
| **Data** | 11/08/2026 |
| **Técnica de elicitação** | Questionário estruturado (survey) com perguntas abertas e fechadas |

---

## 2. Contexto e Objetivo

O VinceArt pretende ser uma plataforma acadêmica que conecta **alunos**, **professores** e **instituições de ensino** em torno da produção de artigos científicos e projetos de pesquisa.

Este formulário tem por objetivo **elicitar requisitos junto aos professores orientadores**, identificando as dores reais do processo atual de orientação, acompanhamento e correção de trabalhos acadêmicos.

> **Importante:** as perguntas foram formuladas para investigar **o problema**, e não para validar uma solução pré-concebida. Evite responder pensando em "como o sistema deveria ser"; descreva **como o trabalho acontece hoje** e **o que atrapalha**.

---

## 3. Perfil do Respondente

*(Dados de contexto — usados para segmentação das respostas e construção de personas)*

1. Nome (opcional): ________________________________________
2. Instituição / Curso: ____________________________________
3. Área de atuação/pesquisa: _______________________________
4. Tempo de experiência como orientador: ___________________
5. Quantos alunos você orienta simultaneamente, em média? ___
6. Nível dos orientandos: ( ) Graduação ( ) Iniciação Científica ( ) Especialização ( ) Mestrado ( ) Doutorado

---

## 4. Questionário de Elicitação

---

### Pergunta 1 — Fluxo de trabalho atual

**Descreva, passo a passo, como acontece hoje a orientação de um aluno desde a definição do tema até a entrega final do artigo. Quais ferramentas você utiliza em cada etapa (e-mail, WhatsApp, Google Docs, planilhas, sistema da instituição, reuniões presenciais)?**

```
Resposta:



```

<sub>**Objetivo (Eng. de Requisitos):** Modelagem do processo de negócio *as-is*. Permite mapear o fluxo real, identificar atores, artefatos e pontos de ruptura antes de propor o processo *to-be*.</sub>

---

### Pergunta 2 — Identificação da dor principal

**Na sua rotina de orientação, qual é a atividade que mais consome tempo e que você considera menos produtiva? Com que frequência ela ocorre e quanto tempo, em média, ela toma por semana?**

```
Resposta:



```

<sub>**Objetivo:** Elicitação de *pain points* com quantificação. A métrica de tempo/frequência serve de base para priorização de requisitos (custo x benefício) e para definir metas mensuráveis de melhoria.</sub>

---

### Pergunta 3 — Acompanhamento e visibilidade do progresso

**Como você verifica hoje se um orientando está realmente progredindo entre um encontro e outro? Já aconteceu de você perceber tardiamente que um aluno estava travado ou atrasado? Descreva a situação e o impacto disso.**

```
Resposta:



```

<sub>**Objetivo:** Investigar a necessidade de **rastreabilidade e monitoramento de progresso**. O relato de um incidente concreto (técnica de *incident-based interviewing*) revela requisitos de notificação, marcos e indicadores de acompanhamento.</sub>

---

### Pergunta 4 — Processo de correção e feedback

**Como você registra e devolve as correções de um trabalho ao aluno? Quais dificuldades você enfrenta ao lidar com múltiplas versões do mesmo documento e ao verificar se o feedback anterior foi de fato aplicado?**

```
Resposta:



```

<sub>**Objetivo:** Levantar requisitos de **versionamento, comentários contextuais e histórico de feedback**. Endereça diretamente a dor de "controle de versões" e o retrabalho de reler o documento inteiro a cada revisão.</sub>

---

### Pergunta 5 — Padronização e conformidade

**Quais normas, templates ou critérios de avaliação você exige dos alunos (ABNT, IEEE, template do evento, rubrica de avaliação)? Que parte dessa verificação você faz manualmente e gostaria que fosse conferida automaticamente?**

```
Resposta:



```

<sub>**Objetivo:** Elicitar **regras de negócio e restrições (constraints)** do domínio acadêmico, além de identificar candidatos à automação — insumo direto para requisitos funcionais de validação.</sub>

---

### Pergunta 6 — Carga de trabalho e escalabilidade

**Se o número de orientandos sob sua responsabilidade dobrasse no próximo semestre, o que quebraria primeiro na sua forma atual de trabalhar? O que você deixaria de fazer?**

```
Resposta:



```

<sub>**Objetivo:** Cenário hipotético (*what-if scenario*) usado para expor **requisitos não funcionais** de escalabilidade, usabilidade e eficiência, além de revelar quais atividades o professor considera essenciais versus descartáveis.</sub>

---

### Pergunta 7 — Comunicação e disponibilidade

**Por quais canais os alunos entram em contato com você e em que horários? Como você lida com a dispersão dessas conversas e com dúvidas repetidas por diferentes orientandos?**

```
Resposta:



```

<sub>**Objetivo:** Mapear **requisitos de comunicação, centralização de histórico e base de conhecimento**. Também levanta requisitos não funcionais de disponibilidade e notificação (limites entre vida pessoal e trabalho).</sub>

---

### Pergunta 8 — Propriedade intelectual e confidencialidade

**Qual sua preocupação em relação à segurança e ao sigilo dos trabalhos ainda não publicados dos seus orientandos? Quem, na sua visão, deveria ter permissão para ver um artigo em cada fase (rascunho, em revisão, submetido, publicado)?**

```
Resposta:



```

<sub>**Objetivo:** Elicitar **requisitos de segurança, privacidade e controle de acesso baseado em papéis (RBAC)**, incluindo a definição dos estados do ciclo de vida do artigo e as políticas de visibilidade de cada um.</sub>

---

### Pergunta 9 — Avaliação, histórico e prestação de contas

**Que tipo de informação ou relatório sobre suas orientações é solicitado pela coordenação/instituição (produtividade, publicações, evolução dos alunos)? Como você monta esses dados hoje e qual a dificuldade nesse processo?**

```
Resposta:



```

<sub>**Objetivo:** Identificar os **stakeholders indiretos** (coordenação, instituição) e seus requisitos de relatório e indicadores. Conecta a dor do professor com a dor institucional de "mensurar e divulgar a produção científica".</sub>

---

### Pergunta 10 — Adoção, expectativa e critério de sucesso

**Você já usou alguma ferramenta de apoio à orientação? O que fez você abandoná-la ou continuar usando? Para que uma nova plataforma valesse o seu tempo de aprendizado, o que ela precisaria obrigatoriamente resolver?**

```
Resposta:



```

<sub>**Objetivo:** Investigar **barreiras de adoção, requisitos de usabilidade/integração** e definir o **critério de aceitação** do stakeholder. A pergunta final captura a expectativa mínima viável (MVP) sob a ótica do usuário.</sub>

---

## 5. Espaço Aberto

**Há alguma dificuldade importante da sua rotina de orientação que não foi abordada nas perguntas acima?**

```
Resposta:



```

<sub>**Objetivo:** Mitigar o viés do entrevistador e capturar **requisitos não antecipados** pela equipe de análise.</sub>

---

## 6. Notas Metodológicas

Este formulário aplica os seguintes conceitos de Engenharia de Requisitos:

| Conceito | Onde é aplicado |
|---|---|
| **Identificação de stakeholders** | Seção 3 (perfil) e Pergunta 9 (stakeholders indiretos) |
| **Modelagem de processo as-is** | Perguntas 1 e 3 |
| **Perguntas abertas (não indutivas)** | Todas — evitam sugerir a solução ao respondente |
| **Elicitação baseada em incidentes** | Perguntas 3 e 10 (relato de fatos concretos, não opiniões) |
| **Cenários hipotéticos (what-if)** | Pergunta 6 |
| **Requisitos não funcionais** | Perguntas 6, 7, 8 (escalabilidade, disponibilidade, segurança) |
| **Regras de negócio e restrições** | Pergunta 5 |
| **Priorização e viabilidade** | Perguntas 2 e 10 (quantificação de esforço e critério de aceitação) |
| **Redução de viés do analista** | Seção 5 (espaço aberto) |

### Próximos passos após a coleta

1. Consolidar e categorizar as respostas (funcionais / não funcionais / regras de negócio / restrições).
2. Identificar requisitos conflitantes entre professores, alunos e instituição — negociação.
3. Priorizar com MoSCoW ou matriz valor × esforço.
4. Registrar no documento de especificação de requisitos e validar com os stakeholders.
