# ADR-0009 — Aplicação de DRY e escopo do shared kernel

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0001, ADR-0003, ADR-0007

## Contexto

A aplicação irrestrita de DRY entre módulos produz um kernel compartilhado que cresce com semântica de
negócio e acopla permanentemente os módulos que deveriam ser independentes.

## Decisão

1. DRY DEVE ser aplicado no escopo interno de cada módulo.
2. Entre módulos, a duplicação DEVE ser preferida ao acoplamento.
3. Conceitos de mesmo nome em módulos distintos DEVEM ser modelados de forma independente em cada módulo, contendo apenas os atributos que aquele módulo utiliza.
4. `shared/` DEVE conter exclusivamente: registro de log, rastreamento e identificador de correlação, tratamento de erros, tipos utilitários de base, autenticação e autorização de borda, e carregamento de configuração.
5. `shared/` NÃO DEVE conter regra de negócio, entidade de domínio, DTO de módulo, evento de módulo ou acesso a dados de módulo.
6. `shared/` NÃO DEVE importar de `modules/`.
7. A inclusão de qualquer símbolo em `shared/` DEVE satisfazer cumulativamente: uso efetivo por dois ou mais módulos e ausência de semântica de negócio.
8. Código NÃO DEVE ser extraído para `shared/` por semelhança sintática; a extração DEVE ser justificada por identidade de responsabilidade.
9. Símbolo de `shared/` que passe a variar por módulo DEVE ser removido de `shared/` e duplicado nos módulos que o utilizam.
10. Alterações em `shared/` DEVEM ser tratadas como alterações de alto impacto e revisadas com o mesmo rigor de uma alteração de contrato.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Modelo canônico único compartilhado entre módulos | Acopla todos os módulos a um mesmo schema; qualquer alteração propaga para todo o sistema. |
| Ausência de `shared/` | Duplicação de infraestrutura transversal, com divergência de comportamento em log, erro e autenticação. |

## Implicações

1. Existirá duplicação deliberada entre módulos; ela NÃO DEVE ser tratada como defeito em revisão de código.
2. Alterações de negócio equivalentes PODEM exigir edição em mais de um módulo.
3. `shared/` tende a permanecer pequeno e estável; crescimento contínuo é indicador de erosão da fronteira e DEVE motivar revisão.
