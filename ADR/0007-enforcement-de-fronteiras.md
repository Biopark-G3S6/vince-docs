# ADR-0007 — Enforcement automatizado de fronteiras

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0002, ADR-0003, ADR-0004, ADR-0005

## Contexto

TypeScript não possui visibilidade em nível de pacote e o NestJS não impede o consumo de símbolos
internos de outro módulo. Fronteira sustentada apenas por disciplina de equipe degrada com o tempo e
com a rotatividade de quem escreve o código.

## Decisão

1. As regras de fronteira definidas em ADR-0003, ADR-0004 e ADR-0005 DEVEM ser verificadas automaticamente na integração contínua.
2. A verificação de fronteiras DEVE ser implementada com `eslint-plugin-boundaries`.
3. Cada camada definida em ADR-0003 §3 DEVE ser declarada como um tipo de elemento na configuração do plugin, com suas regras de importação explícitas.
4. A configuração DEVE permitir, entre módulos distintos, exclusivamente importações originadas de `modules/*/contracts/**`.
5. `shared/` NÃO DEVE importar de `modules/`.
6. Toda violação de regra de fronteira DEVE ser classificada como `error`; NÃO DEVE ser classificada como `warning`.
7. A integração contínua DEVE reprovar o merge diante de qualquer violação.
8. DEVEM ser configurados path aliases no `tsconfig.json` apontando para o `contracts/` de cada módulo.
9. Importações relativas que atravessem o diretório raiz de um módulo NÃO DEVEM ser permitidas.
10. A integração contínua DEVE executar verificação de dependências cíclicas entre módulos.
11. A supressão pontual de uma regra de fronteira por comentário NÃO DEVE ser aceita em revisão.
12. Nx NÃO DEVE ser adotado nesta fase; sua adoção DEVE ser reavaliada por ADR caso o número de módulos ultrapasse dez ou ocorra extração efetiva de serviço.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Nx com `enforce-module-boundaries` | Enforcement superior por tags, com custo de configuração e complexidade desproporcional ao número atual de módulos. |
| Pacotes npm internos por módulo | Isolamento real, ao custo de versionamento e publicação para cada alteração interna. |
| Revisão de código como único controle | Não determinística; degrada com o volume de alterações e com a rotatividade da equipe. |

## Implicações

1. A configuração de lint passa a ser artefato arquitetural e DEVE ser alterada apenas em conjunto com o ADR correspondente.
2. Refatorações que movam arquivos entre camadas exigem atualização da configuração de fronteiras.
3. O custo de violar a arquitetura passa a ser imediato e visível, em vez de diferido.
