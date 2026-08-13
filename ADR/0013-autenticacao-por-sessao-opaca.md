# ADR-0013 — Autenticação por sessão opaca

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0008, ADR-0009, ADR-0014

## Contexto

O sistema exige autenticação para clientes web hospedados em repositório e possivelmente em domínio
distintos do backend, com processos stateless e replicáveis. O ADR-0014 §9 já obriga a resolução das
permissões efetivas no servidor a cada requisição, com cache em Redis.

## Decisão

### Credencial

1. A autenticação DEVE ser baseada em sessão opaca mantida no servidor.
2. O identificador de sessão DEVE ser gerado por fonte criptograficamente segura, com no mínimo 128 bits de entropia.
3. O identificador de sessão NÃO DEVE codificar qualquer informação sobre o usuário ou sobre a sessão.
4. O estado da sessão DEVE ser mantido em Redis, sob chave derivada do identificador.
5. O estado da sessão DEVE conter identificador do usuário, instante de criação, instante da última atividade e metadados de origem.

### Ciclo de vida

6. A sessão DEVE expirar por inatividade em 8 horas e por prazo absoluto em 7 dias.
7. A janela de inatividade DEVE ser renovada a cada requisição autenticada; o prazo absoluto NÃO DEVE ser renovado.
8. A credencial DEVE ser transportada em cookie com os atributos `HttpOnly`, `Secure`, `SameSite` e `Path` restrito.
9. A credencial NÃO DEVE trafegar em URL, corpo de requisição, cabeçalho customizado ou armazenamento acessível a script.
10. O encerramento de sessão DEVE remover imediatamente o registro correspondente.
11. DEVE ser possível revogar, em uma operação, todas as sessões ativas de um usuário.
12. O identificador de sessão DEVE ser regenerado na autenticação bem-sucedida e em qualquer elevação de privilégio.

### Proteção

13. Toda requisição que altere estado DEVE ser protegida contra falsificação de requisição entre sítios.
14. A proteção DEVE combinar o atributo `SameSite` do cookie e, quando a origem do cliente for de sítio distinto, token anti-CSRF por sessão.
15. A resolução da sessão em requisição autenticada NÃO DEVE exigir consulta ao banco relacional.
16. A indisponibilidade do repositório de sessões DEVE resultar em negativa de autenticação; NÃO DEVE existir modo degradado que aceite requisição sem verificação.

### Localização e fronteira

17. A autenticação DEVE ser implementada como preocupação transversal em `shared/`.
18. Nenhum módulo DEVE criar, ler diretamente ou invalidar sessões; NÃO DEVE existir mecanismo próprio de autenticação em módulo.
19. Módulo extraído para serviço independente DEVE receber a identidade já autenticada pela borda e NÃO DEVE reautenticar credencial de usuário final.
20. O endpoint de identidade do usuário autenticado DEVE retornar identificação, papéis e permissões efetivas; as permissões retornadas destinam-se exclusivamente à composição da interface e NÃO DEVEM ser consideradas em decisão de autorização.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| JWT com access token curto e refresh token rotacionado | Decisão anteriormente adotada e revista. O ganho do JWT é dispensar a consulta ao servidor por requisição, mas a resolução de permissões (ADR-0014 §9) já exige essa consulta — o ganho não se realiza. Em contrapartida, impede revogação imediata e exige refresh, rotação, detecção de reuso e gestão de par de chaves. |
| JWT com verificação de sessão em Redis | Acumula a complexidade do JWT e o custo da consulta, sem garantia adicional sobre a sessão opaca. |
| Permissões embarcadas na credencial | Revogação só surte efeito na expiração; o conteúdo desatualiza a cada alteração de papel ou concessão. |
| Transporte em cabeçalho `Authorization` | Transfere ao cliente a gestão do ciclo de vida da credencial e exige armazenamento acessível a script ou reautenticação a cada recarregamento de página. |
| Sessão em memória do processo | Incompatível com a replicação horizontal exigida por ADR-0008 §9. |

## Implicações

1. A disponibilidade do Redis passa a ser condição de disponibilidade do sistema; a falha fecha o acesso, por decisão explícita (§16).
2. O cliente não gerencia credencial: o navegador transporta o cookie, e não há interceptador, renovação ou tratamento de concorrência de renovação no frontend.
3. O uso de cookie exige que cliente e backend compartilhem domínio registrável, ou configuração explícita de CORS com credenciais somada a token anti-CSRF.
4. A revogação é imediata, sem janela de validade residual.
5. Toda requisição autenticada depende de leitura no Redis, que passa a ser caminho crítico compartilhado com a resolução de permissões (ADR-0014 §10).
