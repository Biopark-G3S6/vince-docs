# ADR-0005 — Comunicação entre módulos

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0003, ADR-0004, ADR-0006

## Contexto

O acoplamento entre módulos de um monolito modular é determinado pela forma como eles se comunicam.
Comunicação síncrona generalizada reproduz, em processo único, os problemas de um monolito tradicional.

## Decisão

1. Um módulo NÃO DEVE importar qualquer símbolo de outro módulo que não esteja em `contracts/`.
2. A comunicação assíncrona por eventos DEVE ser a forma padrão de integração entre módulos.
3. A comunicação síncrona PODE ser usada apenas quando houver necessidade real de resposta imediata para concluir a operação em curso.
4. A comunicação síncrona DEVE ocorrer exclusivamente por meio da fachada do módulo de destino, obtida por injeção de dependência.
5. Um módulo NÃO DEVE conhecer, referenciar ou instanciar a implementação concreta da fachada de outro módulo.
6. Chamadas síncronas entre módulos NÃO DEVEM formar ciclo de dependência; ciclo identificado DEVE ser resolvido por inversão para comunicação por evento.
7. Um módulo NÃO DEVE participar da transação de banco de dados de outro módulo.
8. Os eventos publicados por um módulo DEVEM ser declarados em seu `contracts/` e nomeados no passado, descrevendo fato consumado.
9. Um evento NÃO DEVE ser endereçado a um consumidor específico nem carregar instrução de ação.
10. Todo consumidor de evento DEVE ser idempotente.
11. O publicador NÃO DEVE depender da existência, da quantidade ou do resultado do processamento de seus consumidores.
12. Falha no processamento de um evento NÃO DEVE reverter a transação do publicador.
13. O mecanismo de transporte, garantia de entrega e tratamento de falha dos eventos DEVE ser definido em ADR próprio.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Chamada síncrona direta como padrão | Cria grafo de dependências rígido; inviabiliza extração e propaga falha entre módulos. |
| Barramento de eventos apenas em memória | Perda de eventos em caso de falha do processo; sem garantia de entrega. |
| Acesso direto ao banco do outro módulo | Vedado por ADR-0006. |

## Implicações

1. Parte das operações passa a ser eventualmente consistente; a interface de usuário DEVE refletir esse estado quando aplicável.
2. Idempotência exige controle de eventos já processados, com custo de armazenamento e de código.
3. O rastreamento de um fluxo de negócio passa a exigir correlação entre módulos, tornando a observabilidade um requisito e não um opcional.
