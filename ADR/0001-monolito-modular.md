# ADR-0001 — Monolito modular como estilo arquitetural do backend

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0003, ADR-0005, ADR-0008

## Contexto

O backend precisa de baixo custo operacional e velocidade de entrega no estágio atual, sem abrir mão da
possibilidade de escalar e extrair capacidades de negócio individualmente no futuro.

## Decisão

1. O backend DEVE ser implementado como monolito modular: repositório único, artefato de build único e unidade de deploy única.
2. O sistema NÃO DEVE ser iniciado como arquitetura de microsserviços.
3. Todo módulo DEVE ser projetado de forma que sua extração para serviço independente não exija alteração no código dos módulos consumidores.
4. A extração efetiva de um módulo para serviço independente NÃO DEVE ocorrer sem ADR próprio, fundamentado em dados observados de carga, isolamento de falha ou ciclo de release divergente.
5. Em conflito entre princípios de design, a ordem de precedência DEVE ser: (1) integridade da fronteira de módulo, (2) KISS, (3) SOLID, (4) DRY.
6. Padrões táticos avançados — CQRS, Event Sourcing, Saga — NÃO DEVEM ser adotados de forma global; PODEM ser adotados no escopo de um único módulo mediante ADR específico.
7. Antecipação de necessidade não comprovada NÃO DEVE ser justificativa para complexidade estrutural adicional.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Microsserviços desde o início | Custo operacional e de infraestrutura incompatível com o estágio do projeto; fronteiras de negócio ainda não estabilizadas. |
| Monolito tradicional em camadas | Não oferece caminho de extração nem isolamento de domínio; degrada em acoplamento generalizado. |

## Implicações

1. A disciplina de fronteira deixa de ser opcional: sem enforcement automatizado (ADR-0007), a arquitetura degrada para monolito tradicional.
2. Todos os módulos compartilham o mesmo ciclo de release enquanto não houver extração.
3. Falha não tratada em um módulo PODE derrubar o processo inteiro; isolamento de falha depende de tratamento explícito.
