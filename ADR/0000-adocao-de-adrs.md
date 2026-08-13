# ADR-0000 — Adoção de Architecture Decision Records

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** —

## Contexto

As decisões arquiteturais do projeto precisam de registro rastreável e citável. No estágio atual, o
volume de documentação é um custo relevante, o que desaconselha mecanismos que multipliquem
documentos para representar a evolução de uma mesma decisão.

## Decisão

1. Toda decisão arquitetural DEVE ser registrada como um ADR neste diretório antes de ser implementada.
2. Cada ADR DEVE registrar exatamente uma decisão.
3. O nome do arquivo DEVE seguir o padrão `NNNN-titulo-em-kebab-case.md`, com `NNNN` sequencial de quatro dígitos.
4. O número de um ADR é imutável e NÃO DEVE ser reutilizado, mesmo após descontinuação.
5. O status DEVE ser um dos seguintes: `Proposto`, `Aceito`, `Descontinuado`.
6. A revisão de uma decisão DEVE ser feita pela reescrita do próprio ADR; NÃO DEVE ser criado ADR substituto.
7. O ADR reescrito DEVE registrar a decisão anterior na seção `Alternativas rejeitadas`, com o motivo de seu abandono.
8. A data no cabeçalho DEVE refletir a última revisão do ADR.
9. Um ADR NÃO DEVE emendar regra de outro ADR; a regra afetada DEVE ser reescrita no ADR que a contém.
10. As regras da seção `Decisão` DEVEM ser numeradas e são referenciáveis no formato `ADR-NNNN §N`.
11. Reescrita que altere a numeração das regras DEVE ser acompanhada da atualização das referências correspondentes nos demais ADRs e na URS.
12. Os termos normativos DEVEM ser interpretados como: **DEVE** = obrigatório; **NÃO DEVE** = proibido; **PODE** = permitido sem obrigação.
13. Código, configuração ou pull request que viole uma regra `DEVE`/`NÃO DEVE` DEVE ser rejeitado em revisão, salvo se acompanhado da reescrita do ADR correspondente.
14. O índice em `README.md` DEVE ser atualizado no mesmo commit que criar um ADR ou alterar seu status.
15. Novos ADRs DEVEM ser criados a partir de `template.md`.
16. O histórico de alterações dos ADRs é o histórico do repositório de versionamento; o versionamento de código DEVE estar habilitado no projeto.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| ADR imutável, com substituição por novo documento | Preserva integralmente o histórico, ao custo de multiplicar documentos e obrigar a percorrer cadeias de substituição para conhecer a regra vigente. Desproporcional ao estágio atual do projeto. |
| Emenda parcial de regra por outro ADR | Dispersa a regra vigente entre dois documentos; exige ler o ADR original e todas as suas emendas para conhecer o estado atual. |
| Documento único de arquitetura | Não preserva contexto nem alternativas consideradas por decisão. |
| Registro apenas em issues ou pull requests | Vinculado à ferramenta, não versionado com o código, difícil de citar. |

## Implicações

1. O estado vigente da arquitetura é sempre o conteúdo atual dos arquivos; não há cadeia de substituições a percorrer.
2. O histórico das decisões passa a depender integralmente do versionamento do repositório — sem ele, a decisão anterior é perdida na reescrita.
3. Reescrita que renumere regras exige revisão das referências cruzadas, sob pena de rastreabilidade incorreta.
4. O diretório `ADR/` é a fonte da verdade sobre arquitetura; divergência entre código e ADR é defeito.
