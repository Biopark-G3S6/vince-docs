# ADR-0006 — Propriedade exclusiva de dados por módulo

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0003, ADR-0005, ADR-0010

## Contexto

O compartilhamento de tabelas é a principal causa de falha de monolitos modulares: as fronteiras de
código permanecem íntegras enquanto o acoplamento se acumula na camada de dados, tornando a extração
inviável no momento em que ela se faz necessária.

## Decisão

1. Cada tabela DEVE pertencer a exatamente um módulo.
2. Um módulo NÃO DEVE ler nem escrever tabela pertencente a outro módulo, por qualquer meio — query direta, view, procedure ou mapeamento de ORM.
3. NÃO DEVEM existir consultas com junção entre tabelas de módulos distintos.
4. NÃO DEVEM existir chaves estrangeiras cruzando fronteiras de módulo; a referência DEVE ser feita por identificador, sem integridade referencial declarada no banco.
5. A consistência de referências entre módulos DEVE ser garantida pela aplicação, por meio de eventos e validação no módulo proprietário.
6. Dado pertencente a outro módulo e necessário para leitura DEVE ser obtido pela fachada do módulo proprietário ou mantido como réplica local projetada a partir de eventos.
7. Réplica local DEVE ser tratada como projeção eventualmente consistente e NÃO DEVE ser considerada fonte da verdade.
8. Um módulo NÃO DEVE alterar réplica local por escrita própria; a réplica DEVE ser derivada exclusivamente de eventos do módulo proprietário.
9. A propriedade de uma migração de schema pelo módulo DEVE ser expressa pela residência, dentro do módulo, do arquivo de definição de schema das tabelas afetadas; o diretório de migrações geradas PODE ser único para a aplicação.
10. A estratégia física de separação — schemas do Postgres, prefixo de tabela ou equivalente — DEVE ser definida em ADR próprio.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Banco compartilhado com acesso livre entre módulos | Acopla módulos pelo schema; qualquer alteração de tabela vira alteração global. |
| Instância de banco por módulo | Custo operacional e perda de transacionalidade local incompatíveis com o estágio do projeto. |
| Chaves estrangeiras entre módulos | Cria dependência física que precisa ser removida na extração, com migração de dados em produção. |

## Implicações

1. A integridade referencial entre módulos deixa de ser garantida pelo banco e passa a ser responsabilidade da aplicação.
2. Consultas que hoje seriam uma única junção passam a exigir composição em memória ou réplica projetada.
3. Relatórios e consultas analíticas que atravessam módulos NÃO DEVEM ser resolvidos por junção direta; exigem módulo ou mecanismo próprio de leitura.
4. A dupla escrita entre módulos deixa de ser possível; toda propagação passa por evento.
5. Como o diretório de migrações é único, a propriedade declarada em §1 depende de revisão de código para ser preservada (ADR-0010 §13).
