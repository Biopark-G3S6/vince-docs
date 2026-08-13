# ADR-0015 — Arquitetura do frontend

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0003, ADR-0007, ADR-0009, ADR-0016, ADR-0017

## Contexto

O frontend reside em repositório separado e está sujeito à mesma erosão de fronteira que ADR-0007
previne no backend, somada a um risco próprio: tratar dados pertencentes ao servidor como estado da
aplicação, o que obriga a reimplementar cache, invalidação e controle de concorrência manualmente.

## Decisão

### Organização

1. O frontend DEVE ser organizado em features, cada uma correspondendo a um módulo do backend.
2. NÃO DEVEM existir diretórios de primeiro nível definidos por camada técnica fora de `shared/`.
3. A estrutura DEVE ser:

   ```
   src/
     app/                     # bootstrap, providers, roteamento raiz
     features/<feature>/
       api/                   # chamadas HTTP e hooks de consulta e mutação
       components/            # componentes da feature
       pages/                 # telas
       model/                 # tipos, validação e lógica de apresentação
       index.ts               # superfície pública
     shared/                  # design system, cliente HTTP, utilitários
   ```

4. Cada feature DEVE expor sua superfície pública exclusivamente por `index.ts`.
5. Uma feature NÃO DEVE importar símbolo de outra feature fora do `index.ts` dela.
6. `shared/` NÃO DEVE importar de `features/`.
7. `shared/` NÃO DEVE conter regra de negócio.
8. As regras §4 a §7 DEVEM ser verificadas por análise estática na integração contínua, com violação classificada como erro.
9. NÃO DEVEM existir dependências cíclicas entre features.

### Estado

10. O estado DEVE ser classificado em estado de servidor e estado de cliente.
11. Dado proveniente da API DEVE ser tratado como estado de servidor e mantido exclusivamente em cache de requisições.
12. Dado proveniente da API NÃO DEVE ser copiado para store de estado de cliente.
13. O cache de estado de servidor NÃO DEVE ser tratado como fonte da verdade.
14. Mutação que altere dado de servidor DEVE invalidar as consultas afetadas.
15. Estado de cliente DEVE ser local ao componente por padrão; store global PODE ser usado apenas para estado genuinamente transversal à aplicação.

### Rotas e desempenho

16. O código DEVE ser dividido por rota.
17. Conteúdo carregado de forma assíncrona DEVE ter espaço reservado com dimensão equivalente à do conteúdo final.
18. Rota protegida NÃO DEVE ser renderizada antes da resolução da identidade do usuário.

### Autorização na interface

19. A interface DEVE ocultar ou desabilitar ações para as quais o usuário não possua permissão efetiva.
20. A ocultação de ação na interface NÃO DEVE ser considerada controle de segurança.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Organização por camada técnica no primeiro nível | Espalha cada alteração de negócio por todas as pastas; impede recorte por capacidade. |
| Store global único para todo o estado da aplicação | Reimplementa cache manualmente; produz dado desatualizado, invalidação esquecida após mutação e duplicação de estados de carregamento e erro. |
| Ausência de fronteiras entre features | Reproduz no frontend a erosão que ADR-0007 previne no backend; a organização por features degrada para organização por pastas. |

## Implicações

1. A correspondência entre features e módulos depende da decomposição do sistema em módulos, ainda pendente.
2. Duplicação entre features é preferível ao acoplamento, pelas mesmas razões de ADR-0009 §2.
3. A separação entre estado de servidor e estado de cliente é estrutural: convertê-la posteriormente exige reescrever as telas afetadas.
