# ADR-0004 — Fachada abstrata como única superfície pública do módulo

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0002, ADR-0003, ADR-0005

## Contexto

No NestJS, `@Module()` é um escopo de container de injeção de dependências, não uma fronteira
arquitetural. A fronteira efetiva é determinada exclusivamente pelo array `exports`, e um export
indevido dissolve o isolamento sem produzir erro de compilação.

## Decisão

1. Cada módulo DEVE expor exatamente uma fachada pública, declarada em `contracts/`.
2. A fachada DEVE ser declarada como `abstract class`.
3. Interfaces TypeScript NÃO DEVEM ser usadas como token de injeção de dependência.
4. O array `exports` do `@Module()` DEVE conter exclusivamente o token da fachada.
5. Repositórios, casos de uso, entidades, value objects, adapters e clientes NÃO DEVEM ser exportados.
6. O registro da fachada DEVE ser feito na forma `{ provide: <Fachada>, useClass: <FachadaImpl> }`.
7. A implementação da fachada NÃO DEVE conter regra de negócio; DEVE apenas orquestrar casos de uso e mapear DTOs.
8. `contracts/` NÃO DEVE conter regra de negócio, dependência de ORM, de framework HTTP ou de biblioteca de fila.
9. Os DTOs de `contracts/` NÃO DEVEM expor entidades de domínio nem tipos gerados por ORM.
10. A extração do módulo para serviço independente DEVE exigir apenas a substituição do `useClass` por uma implementação cliente remota.
11. Alteração incompatível em qualquer símbolo de `contracts/` DEVE ser tratada como quebra de contrato: a nova versão do tipo DEVE conviver com a anterior durante a migração dos consumidores.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Exportar services do módulo diretamente | Expõe o interno; qualquer módulo consumidor passa a depender de detalhe de implementação. |
| Interface + token `Symbol` e `@Inject()` | Boilerplate em todos os pontos de injeção, sem ganho sobre `abstract class`. |
| Múltiplas fachadas por módulo | Multiplica a superfície pública e dilui a responsabilidade da fronteira. |

## Implicações

1. Toda necessidade de um módulo externo passa a ser explícita e revisável, por alterar `contracts/`.
2. A fachada tende a crescer; crescimento desproporcional é indicador de fronteira mal recortada e DEVE motivar revisão do módulo.
3. É necessário mapeamento entre entidades de domínio e DTOs, com custo de código adicional.
