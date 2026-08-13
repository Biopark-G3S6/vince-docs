# ADR-0010 — Camada HTTP e ORM

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0002 (complementa), ADR-0004, ADR-0006, ADR-0007

## Contexto

O ADR-0002 fixou NestJS e TypeScript sem definir o adapter HTTP nem o mecanismo de acesso a dados.
Ambos são pré-requisitos da implementação e o segundo tem efeito direto sobre a propriedade de dados
estabelecida em ADR-0006.

## Decisão

1. A camada HTTP DEVE ser o adapter Express do NestJS (`@nestjs/platform-express`).
2. O acesso a dados DEVE ser feito por Prisma ORM.
3. O schema Prisma DEVE ser dividido em um arquivo `.prisma` por módulo, residente no próprio módulo.
4. Cada módulo DEVE receber um cliente Prisma escopado, construído por extensão de cliente, expondo exclusivamente os models de sua propriedade.
5. Nenhum módulo DEVE receber por injeção a instância não escopada do `PrismaClient`.
6. O acesso a um model por módulo diverso do seu proprietário DEVE ser bloqueado por regra de análise estática, adicionalmente ao escopo do cliente.
7. DEVE existir uma única instância de `PrismaClient` por processo; NÃO DEVEM ser instanciados clientes independentes por módulo.
8. Tipos gerados pelo Prisma NÃO DEVEM constar de `contracts/` nem atravessar a fronteira do módulo.
9. Tipos gerados pelo Prisma NÃO DEVEM ser usados como entidade de domínio; `domain/` DEVE definir seus próprios tipos.
10. O diretório de migrações geradas pelo Prisma DEVE ser único para a aplicação, nos termos de ADR-0006 §9.
11. Migrações DEVEM ser versionadas em repositório e aplicadas por `prisma migrate deploy` em ambientes não locais.
12. `prisma db push` NÃO DEVE ser executado fora do ambiente local de desenvolvimento.
13. Migração que altere tabela pertencente a módulo diverso do autor DEVE ser rejeitada em revisão.
14. Consultas em SQL bruto PODEM ser usadas para leitura de desempenho crítico, DEVEM residir em `infrastructure/` e NÃO DEVEM referenciar tabelas de outro módulo.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Adapter Fastify | Ganho de vazão irrelevante frente ao gargalo real, que é I/O de banco; ecossistema de middlewares menor. |
| Projeto Prisma independente por módulo | Isolamento superior, ao custo de um cliente gerado e um pool de conexões por módulo por processo — incompatível com o limite de conexões de uma instância única de PostgreSQL. |
| TypeORM | Integração mais idiomática com o container do NestJS, porém migrações e inferência de tipos menos previsíveis. |

## Implicações

1. O `PrismaClient` não escopado é a principal superfície de violação de ADR-0006; seu uso direto por módulo é defeito, não estilo.
2. O mapeamento entre tipos do Prisma e entidades de domínio passa a ser obrigatório, com custo de código em todo repositório.
3. O diretório único de migrações transfere para a revisão de código a garantia de propriedade estabelecida em ADR-0006.
