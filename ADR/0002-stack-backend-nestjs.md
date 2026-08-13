# ADR-0002 — Stack do backend: NestJS + TypeScript

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0001, ADR-0004

## Contexto

O estilo definido em ADR-0001 exige um framework com modularidade e injeção de dependências de primeira
classe, para que a inversão de dependência entre módulos seja idiomática e não construída manualmente.

## Decisão

1. O backend DEVE ser implementado em NestJS sobre Node.js, com TypeScript.
2. O TypeScript DEVE ser configurado com `strict: true`.
3. As camadas `domain/` e `application/` NÃO DEVEM importar símbolos do NestJS, exceto os decoradores de injeção de dependência.
4. Dependências de framework HTTP, ORM, fila e clientes externos DEVEM ficar confinadas às camadas `infrastructure/` e `presentation/`.
5. Toda dependência externa DEVE ser acessada por meio de um port declarado em `domain/`, nunca importada diretamente por `application/`.
6. A escolha de ORM, biblioteca de fila, validação e demais bibliotecas transversais DEVE ser objeto de ADR próprio.
7. Bibliotecas que exijam um modelo de dados único e compartilhado entre todos os módulos NÃO DEVEM ser adotadas.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Java + Spring Modulith | Enforcement de fronteira superior, mas curva de aprendizado e verbosidade incompatíveis com o prazo e a equipe. |
| .NET (C#) | Fronteiras garantidas em tempo de compilação, ao custo de maior cerimônia estrutural e de um segundo ecossistema no projeto. |
| Go | Isolamento real via `internal/`, porém wiring e injeção de dependências manuais, com ferramental de fila e ORM menos maduro. |

## Implicações

1. TypeScript não oferece visibilidade em nível de pacote; o isolamento entre módulos passa a depender integralmente de ADR-0004 e ADR-0007.
2. Backend e frontend compartilham linguagem, viabilizando tipos de contrato de API derivados de uma fonte única.
3. O projeto assume as limitações do runtime Node.js para carga intensiva de CPU; tarefas dessa natureza DEVEM ser tratadas por workers dedicados (ADR-0008).
