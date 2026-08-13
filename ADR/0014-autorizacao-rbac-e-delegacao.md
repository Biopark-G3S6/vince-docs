# ADR-0014 — Autorização por RBAC e delegação de permissões

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0009, ADR-0013

## Contexto

O sistema exige controle de acesso por ação, com a possibilidade de um usuário conceder permissões a
outro. É necessário definir o modelo, o formato de identificação das permissões, sua origem e as
regras de concessão e revogação.

## Decisão

### Modelo

1. A autorização DEVE ser baseada em controle de acesso por papéis.
2. Uma permissão DEVE ser identificada no formato `RECURSO:ACAO`, em maiúsculas, com o recurso no singular.
3. Permissões NÃO DEVEM admitir curinga.
4. Um papel DEVE ser um agrupamento nomeado de permissões.
5. Um usuário PODE possuir papéis e concessões diretas; suas permissões efetivas DEVEM ser a união de ambos.

### Origem e rastreabilidade

6. Todo requisito funcional DEVE declarar as permissões que origina.
7. NÃO DEVE existir permissão sem requisito funcional que a origine.
8. O catálogo de permissões DEVE ser derivado dos requisitos funcionais e mantido na URS.

### Verificação

9. As permissões efetivas NÃO DEVEM ser transportadas na credencial de sessão; DEVEM ser resolvidas no servidor a cada requisição.
10. A resolução das permissões efetivas DEVE utilizar cache, invalidado imediatamente a cada alteração de papel, concessão ou revogação.
11. A verificação de permissão DEVE ocorrer na borda, antes da execução do caso de uso.
12. A verificação de permissão NÃO DEVE ser suficiente para autorizar operação sobre registro específico; a titularidade do registro DEVE ser verificada dentro do caso de uso.
13. Regras de titularidade de registro NÃO DEVEM ser modeladas como permissões.
14. A negativa de autorização DEVE ser registrada em log.

### Delegação

15. A concessão de uma permissão `P` por um usuário `A` a um usuário `B` DEVE ser permitida somente se `P` pertencer às permissões efetivas de `A` e `A` possuir a permissão de concessão.
16. Um usuário NÃO DEVE conceder permissão a si mesmo.
17. A revogação de uma permissão de um usuário NÃO DEVE revogar as concessões por ele realizadas; a concessão é independente de sua origem após efetivada.
18. Toda concessão e toda revogação DEVEM ser registradas em trilha de auditoria imutável, contendo concedente, beneficiário, permissão e instante.
19. Uma concessão direta PODE ter prazo de validade; expirada, DEVE deixar de compor as permissões efetivas.
20. DEVE existir consulta que liste as concessões diretas ativas de um usuário, com concedente e data, para fins de revisão periódica.
21. A revogação de uma concessão direta DEVE ser possível a qualquer momento por usuário que possua a permissão de revogação, independentemente de quem a concedeu.

### Localização

22. O mecanismo de autorização DEVE ser implementado como preocupação transversal em `shared/`.
23. Cada módulo DEVE declarar as permissões de seus recursos, mas NÃO DEVE implementar mecanismo próprio de verificação.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Permissões embarcadas na credencial | Revogação só surtiria efeito na expiração da credencial; incompatível com a exigência de revogação direta imediata (§21). |
| Curingas em permissões | Exigem expansão contra um catálogo que muda a cada requisito novo, tornando a verificação de delegação (§15) dependente de estado mutável. |
| ABAC ou motor de políticas | Expressividade superior, com complexidade desproporcional ao estágio do projeto (ADR-0001 §5). |
| Revogação em cascata das concessões | Preteria o invariante de que ninguém exerce privilégio cuja origem o perdeu, mas produz revogações em massa inesperadas; rejeitada por decisão de stakeholder, com mitigação por §18, §19, §20 e §21. |
| Titularidade de registro modelada como permissão | Produz explosão combinatória do catálogo a cada recurso com regra de escopo. |

## Implicações

1. Uma permissão concedida sobrevive à revogação de quem a concedeu; a contenção do privilégio órfão depende de revisão periódica (§20), não de mecanismo automático.
2. Todo requisito funcional passa a exigir declaração de permissões; requisito sem esse campo está incompleto.
3. Toda requisição autenticada implica resolução de permissões efetivas; o cache é caminho crítico e sua indisponibilidade equivale à indisponibilidade do sistema.
4. A verificação de autorização ocorre em duas camadas distintas — borda e caso de uso — e ambas são obrigatórias.
