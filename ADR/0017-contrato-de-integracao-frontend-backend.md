# ADR-0017 — Contrato de integração entre frontend e backend

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0004, ADR-0013, ADR-0015, ADR-0016

## Contexto

Frontend e backend residem em repositórios separados, o que cria risco de divergência silenciosa de
contrato — detectável apenas em execução. A sessão em cookie definida em ADR-0013 §8 impõe, além
disso, requisitos de origem, de compartilhamento entre origens e de proteção contra CSRF.

## Decisão

### Contrato

1. O backend DEVE publicar especificação OpenAPI gerada a partir do próprio código.
2. Os tipos usados pelo cliente DEVEM ser derivados da especificação publicada.
3. Os tipos derivados DEVEM ser versionados no repositório do frontend e regenerados na integração contínua.
4. Divergência entre a especificação publicada e os tipos versionados DEVE reprovar o build do frontend.
5. O frontend NÃO DEVE declarar manualmente tipos de requisição ou de resposta da API.
6. Toda chamada à API DEVE ocorrer pela camada `api/` da feature correspondente; componentes NÃO DEVEM chamar a API diretamente.
7. A API DEVE ser versionada por prefixo de caminho.
8. Alteração incompatível de contrato DEVE observar ADR-0004 §11.

### Origem, sessão e CSRF

9. Frontend e backend DEVEM ser servidos sob o mesmo domínio registrável.
10. O backend DEVE restringir as origens aceitas a uma lista explícita; NÃO DEVE aceitar origem curinga.
11. O cliente HTTP DEVE enviar credenciais em todas as requisições à API.
12. O cliente NÃO DEVE armazenar a credencial de sessão; seu transporte é responsabilidade do navegador.
13. Requisições que alterem estado DEVEM enviar o token anti-CSRF quando exigido por ADR-0013 §14.

### Erros e identidade

14. As respostas de erro DEVEM seguir formato único, com código de erro estável e legível por máquina.
15. O frontend NÃO DEVE tomar decisão com base no texto da mensagem de erro.
16. Resposta `401` DEVE encerrar a sessão no cliente e redirecionar à autenticação.
17. Resposta `403` NÃO DEVE encerrar a sessão no cliente.
18. O cliente DEVE obter identidade e permissões efetivas pelo endpoint de identidade, uma vez por carregamento da aplicação, revalidando conforme política de cache declarada.
19. Toda requisição DEVE propagar identificador de correlação.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Pacote npm compartilhado de tipos | Fonte única, porém exige publicar e versionar pacote a cada alteração de contrato — peso desproporcional para dois repositórios. |
| Tipos escritos manualmente nos dois lados | Divergência silenciosa; o erro se manifesta apenas em execução. |
| GraphQL | Contrato tipado por construção, ao custo de camada adicional e de autorização por campo, desproporcional ao estágio do projeto. |
| Domínios sem raiz registrável comum | Obriga `SameSite=None`, ampliando a superfície de CSRF e a complexidade de configuração. |

## Implicações

1. A especificação OpenAPI deixa de ser documentação e passa a ser contrato: mantê-la atualizada é obrigação do backend, verificada por build.
2. O domínio comum entre frontend e backend torna-se restrição de infraestrutura, a observar na decisão de implantação.
3. O build do frontend passa a depender da disponibilidade da especificação do backend.
4. O formato único de resposta de erro precisa ser definido no backend antes da primeira integração real.
