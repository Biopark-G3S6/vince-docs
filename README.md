# VinceArt — Arquitetura e Requisitos

Documentação normativa do projeto VinceArt. Este repositório é a fonte da verdade sobre as decisões
de arquitetura e os requisitos do sistema; divergência entre o código e o que está aqui é defeito.

## Estrutura

| Diretório | Conteúdo |
| :--- | :--- |
| [`ADR/`](ADR/) | Registros de decisão arquitetural. As regras do processo estão em [ADR-0000](ADR/0000-adocao-de-adrs.md). |
| [`Requisitos/`](Requisitos/) | [URS](Requisitos/URS.md) — o que o **cliente** precisa, e o material bruto de elicitação. |
| [`Padroes/`](Padroes/) | [Padrões de Engenharia](Padroes/Padroes-de-Engenharia.md) — o que a **equipe** decidiu: como construir o sistema e como especificá-lo. |

## Repositórios do projeto

| Repositório | Conteúdo |
| :--- | :--- |
| [vince-back](https://github.com/Biopark-G3S6/vince-back) | Backend — monolito modular em NestJS |
| [vince-front](https://github.com/Biopark-G3S6/vince-front) | Frontend — aplicação de página única em React |
| **vince-docs** | Este repositório — arquitetura e requisitos |

## Documentos oficiais

Todo documento oficial produzido com estes repositórios DEVE ser versionado aqui, em Markdown. O
Markdown é a fonte da verdade; qualquer outro formato — `.docx`, Google Docs, PDF — é derivado dele
e NÃO DEVE ser editado diretamente.

A versão publicada de cada documento fica na pasta do projeto no Google Drive, convertida em Google
Docs para leitura e distribuição às partes interessadas.

| Item | Identificador |
| :--- | :--- |
| Pasta do projeto no Drive | `1_0pTI8OCNCmm8zTS3hR0HNFvJylFYd79` |
| URS — documento publicado | `138OfIS9sPFyvktQKJXV8iGbSfz5J-g8-VDk-XlNCWHk` |
| URS — fonte | [`Requisitos/URS.md`](Requisitos/URS.md) |

- [Pasta do projeto no Drive](https://drive.google.com/drive/folders/1_0pTI8OCNCmm8zTS3hR0HNFvJylFYd79)
- [URS publicada](https://docs.google.com/document/d/138OfIS9sPFyvktQKJXV8iGbSfz5J-g8-VDk-XlNCWHk/edit)

### Publicação

A publicação é de mão única: do Markdown para o Drive, em duas etapas. O `.docx` é intermediário
descartável e não é versionado.

**1. Gerar.** [`Requisitos/gerar-docx.py`](Requisitos/gerar-docx.py) depende de `python-docx`, que
não precisa ser instalado no Python do sistema:

```
python3 -m venv .venv && .venv/bin/pip install python-docx
.venv/bin/python Requisitos/gerar-docx.py Requisitos/URS.md Requisitos/URS.docx
```

**2. Publicar.** Substitui o conteúdo do documento preservando o mesmo identificador e a mesma URL:

```
rclone copy --drive-import-formats docx Requisitos/URS.docx \
  "gdrive,root_folder_id=1_0pTI8OCNCmm8zTS3hR0HNFvJylFYd79:"
```

O remote `gdrive` é criado uma única vez com `rclone config create gdrive drive scope=drive.file`.
O escopo `drive.file` limita o acesso aos arquivos que o próprio rclone criar.

Publicar sobrescreve. Comentário ou edição feita dentro do Google Doc se perde na publicação
seguinte; retorno de parte interessada DEVE ser trazido de volta ao Markdown antes de republicar.

## Como ler

A **URS** declara o que o **cliente** precisa: requisitos elicitados junto às partes interessadas,
rastreados até a evidência que os originou. Nada entra na URS por decisão da equipe.

Os **Padrões de Engenharia** declaram o que a **equipe** decidiu — tanto sobre como construir o
sistema quanto sobre como especificá-lo. Não são requisitos: ninguém os pediu. São o critério de
conformidade da revisão de código e da aceitação de um requisito como especificado. Cada um é
rastreado até o ADR que o originou, ou marcado como decisão de processo quando não há ADR.

Os **ADRs** registram *como* cada decisão foi tomada, com as alternativas consideradas e suas
implicações.

Os termos normativos seguem uma convenção estrita: **DEVE** é obrigatório, **NÃO DEVE** é proibido,
**PODE** é permitido sem obrigação. Código que viole uma regra `DEVE` ou `NÃO DEVE` é rejeitado em
revisão, salvo se acompanhado da reescrita do ADR correspondente.

## Revisão de decisões

Um ADR revisto é **reescrito no próprio arquivo** — não existe ADR substituto nem emenda por outro
documento. A decisão abandonada fica registrada na seção `Alternativas rejeitadas` do próprio ADR, e
o histórico completo é o deste repositório.
