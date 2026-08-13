# VinceArt — Arquitetura e Requisitos

Documentação normativa do projeto VinceArt. Este repositório é a fonte da verdade sobre as decisões
de arquitetura e os requisitos do sistema; divergência entre o código e o que está aqui é defeito.

## Estrutura

| Diretório | Conteúdo |
| :--- | :--- |
| [`ADR/`](ADR/) | Registros de decisão arquitetural. As regras do processo estão em [ADR-0000](ADR/0000-adocao-de-adrs.md). |
| [`Requisitos/`](Requisitos/) | [URS](Requisitos/URS.md) — especificação de requisitos do usuário, e o material bruto de elicitação. |

## Repositórios do projeto

| Repositório | Conteúdo |
| :--- | :--- |
| [vince-back](https://github.com/Biopark-G3S6/vince-back) | Backend — monolito modular em NestJS |
| [vince-front](https://github.com/Biopark-G3S6/vince-front) | Frontend — aplicação de página única em React |
| **vince-docs** | Este repositório — arquitetura e requisitos |

## Como ler

A **URS** declara *o que* o sistema deve satisfazer, com cada requisito rastreado até o ADR que o
satisfaz. Os **ADRs** registram *como* cada decisão foi tomada, com as alternativas consideradas e
suas implicações.

Os termos normativos seguem uma convenção estrita: **DEVE** é obrigatório, **NÃO DEVE** é proibido,
**PODE** é permitido sem obrigação. Código que viole uma regra `DEVE` ou `NÃO DEVE` é rejeitado em
revisão, salvo se acompanhado da reescrita do ADR correspondente.

## Revisão de decisões

Um ADR revisto é **reescrito no próprio arquivo** — não existe ADR substituto nem emenda por outro
documento. A decisão abandonada fica registrada na seção `Alternativas rejeitadas` do próprio ADR, e
o histórico completo é o deste repositório.
