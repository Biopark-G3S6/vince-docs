# ADR-0018 — Organização física do banco de dados

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0006, ADR-0010, ADR-0011, ADR-0019

## Contexto

O ADR-0006 estabeleceu propriedade exclusiva de dados por módulo sobre uma instância única de
PostgreSQL compartilhada. Falta definir como essa propriedade se materializa no banco e quais
convenções a sustentam, em especial diante da proibição de chave estrangeira entre módulos.

## Decisão

### Separação

1. Cada módulo DEVE possuir um schema próprio no PostgreSQL, nomeado conforme o módulo.
2. Toda tabela DEVE residir no schema de seu módulo proprietário.
3. NÃO DEVEM existir tabelas de negócio no schema `public`.
4. NÃO DEVE existir schema compartilhado entre módulos.
5. A tabela de outbox de um módulo DEVE residir no schema desse módulo.
6. A trilha de auditoria DEVE residir no schema do módulo que a produz.
7. O arquivo de schema Prisma de cada módulo DEVE declarar exclusivamente os models do schema correspondente.
8. A criação do schema de um módulo DEVE ser feita por migração versionada.

### Identificadores

9. A chave primária de toda tabela DEVE ser um UUID versão 7.
10. O identificador DEVE ser gerado pela aplicação, e não pelo banco de dados.
11. Tabela de associação PODE usar chave primária composta pelas colunas de referência.
12. Referência a registro do mesmo módulo DEVE declarar chave estrangeira.
13. Referência a registro de outro módulo DEVE ser feita por coluna de identificador, sem chave estrangeira.
14. Coluna de referência a outro módulo DEVE possuir índice.

### Tipos e convenções

15. Colunas de data e hora DEVEM usar `timestamptz`; `timestamp` sem fuso NÃO DEVE ser usado.
16. Identificadores de objeto no banco DEVEM usar `snake_case`, com o mapeamento para o código declarado no schema Prisma.
17. Toda tabela DEVE possuir colunas de instante de criação e de última atualização.
18. Exclusão lógica NÃO DEVE ser adotada por padrão; PODE ser adotada em tabela cuja retenção seja exigida por auditoria ou por requisito legal, mediante declaração explícita.
19. Enumeração de negócio DEVE ser representada por texto com restrição de verificação ou por tabela de domínio; o tipo `ENUM` nativo do PostgreSQL NÃO DEVE ser usado.
20. Toda coluna usada como filtro ou ordenação recorrente DEVE possuir índice.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Prefixo de tabela em schema único | Propriedade por convenção; a extração exige selecionar tabelas manualmente por padrão de nome, em tensão com RNF-EVO-002. |
| Papel do PostgreSQL por módulo, com concessão por schema | Daria enforcement pelo próprio banco, mas exige uma conexão por módulo — incompatível com o cliente único de ADR-0010 §7 e com o orçamento de conexões de ADR-0019 §10. |
| `bigint` identity como chave primária | Identificadores colidem entre módulos: como ADR-0006 §4 proíbe chave estrangeira entre eles, uma referência cruzada incorreta pode apontar para linha válida de outra tabela sem gerar erro. |
| UUID versão 4 | Globalmente único, porém aleatório: fragmenta o índice B-tree e degrada a inserção sob volume. |
| Chave interna `bigint` com UUID exposto | Elimina o vazamento de volume mantendo desempenho interno, ao custo de duas identidades por linha e do risco permanente de expor a errada. |
| Tipo `ENUM` nativo | Alterar o conjunto de valores exige migração custosa e não admite remoção simples. |
| Exclusão lógica por padrão | Contamina toda consulta do sistema com filtro adicional, cuja omissão expõe registro excluído. |

## Implicações

1. O recurso de múltiplos schemas do Prisma passa a ser dependência da decisão; sua estabilidade deve ser verificada na versão adotada.
2. Ferramentas que presumem tabelas em `public` exigem configuração explícita de caminho de busca.
3. A chave de 16 bytes produz índices maiores que os de `bigint`, compensados pela unicidade global e pela ordenação temporal.
4. Como não há chave estrangeira entre módulos, o banco não cria nem sugere índice nas colunas de referência: a regra §14 passa a ser a única proteção contra varredura completa nessas junções feitas em memória.
5. A extração de um módulo passa a ser o despejo e a restauração de um schema completo.
