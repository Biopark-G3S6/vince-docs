# ADR-0003 — Fronteira e estrutura interna de módulo

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0001, ADR-0004, ADR-0006, ADR-0007

## Contexto

Um monolito modular só permite extração futura se a fronteira do módulo coincidir com a fronteira do
negócio e da propriedade dos dados, e não com um agrupamento técnico.

## Decisão

1. Um módulo constitui a fronteira de consistência transacional e de propriedade de dados, e DEVE ser de uma de duas naturezas: **módulo de negócio**, correspondente a uma capacidade de negócio; ou **módulo de plataforma**, correspondente a uma capacidade técnica transversal que exija dados próprios.
2. NÃO DEVEM existir módulos definidos por camada técnica — `controllers`, `services`, `repositories` ou equivalentes — no nível raiz de `modules/`.
3. Todo módulo DEVE residir em `modules/<modulo>/` e adotar a seguinte estrutura interna:

   ```
   modules/<modulo>/
     contracts/          # superfície pública
     domain/             # entidades, value objects, regras, ports
     application/        # casos de uso
     infrastructure/     # implementação dos ports
     presentation/       # controllers e rotas HTTP
     <modulo>.module.ts  # composition root do módulo
   ```

4. O conteúdo de cada camada DEVE observar:

   | Camada | DEVE conter | NÃO DEVE conter |
   | :--- | :--- | :--- |
   | `contracts/` | fachada abstrata, DTOs, tipos de evento publicados, enums | regra de negócio, tipos de ORM, dependência de framework |
   | `domain/` | entidades, value objects, regras invariantes, interfaces de port | acesso a I/O, SQL, HTTP, dependência de framework |
   | `application/` | casos de uso, orquestração, transações | SQL, HTTP, detalhes de persistência |
   | `infrastructure/` | repositórios, adapters, consumers, clientes externos | regra de negócio |
   | `presentation/` | controllers, rotas, validação de entrada, mapeamento HTTP | regra de negócio, acesso direto a repositório |

5. `domain/` NÃO DEVE importar de `application/`, `infrastructure/` ou `presentation/`.
6. `application/` NÃO DEVE importar de `infrastructure/` ou `presentation/`; DEVE depender exclusivamente de ports declarados em `domain/`.
7. `presentation/` NÃO DEVE acessar `infrastructure/` nem `domain/` diretamente; DEVE invocar casos de uso de `application/`.
8. Cada caso de uso DEVE ser uma classe com um único método público de execução.
9. `<modulo>.module.ts` DEVE ser o único ponto de registro de providers, rotas, consumers e jobs agendados do módulo.
10. O composition root da aplicação DEVE conhecer apenas a lista de módulos; adicionar ou remover um módulo DEVE ser uma alteração de uma linha.
11. A remoção de um módulo do composition root NÃO DEVE quebrar a compilação dos demais módulos.
12. A criação de um novo módulo DEVE ser precedida de ADR que declare sua capacidade de negócio e as tabelas sob sua propriedade.
13. Submódulos PODEM existir dentro de um módulo, desde que não exponham superfície pública própria.
14. Módulo de plataforma DEVE observar integralmente as regras deste ADR e as de ADR-0004 a ADR-0007, sem exceção decorrente de sua natureza.
15. A criação de módulo de plataforma DEVE ser justificada pela existência de dados próprios que `shared/` não pode possuir por força de ADR-0009 §5; capacidade transversal sem dados próprios DEVE residir em `shared/`.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Organização por camada técnica no topo | Impede extração; toda alteração de negócio atravessa todas as pastas. |
| Hexagonal completa com portas e adaptadores em todos os pontos | Cerimônia desproporcional ao porte do projeto; viola KISS (ADR-0001 §5). |

## Implicações

1. Uma capacidade de negócio mal recortada gera fronteira errada, cujo custo de correção cresce com o tempo.
2. A estrutura é repetida em todos os módulos, o que aumenta o número de arquivos em troca de previsibilidade e recortabilidade.
