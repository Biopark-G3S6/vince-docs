# ADR-0025 — Formato de resposta da API

- **Status:** Aceito
- **Data:** 2026-08-12
- **Relacionados:** ADR-0011, ADR-0017, ADR-0022

## Contexto

O ADR-0017 §14 exige formato único de resposta de erro, com código estável e legível por máquina, sem
definir sua estrutura. Repositórios separados e tipos derivados da especificação tornam o formato um
contrato: sua ausência produz tratamento divergente a cada endpoint.

## Decisão

### Envelope

1. Toda resposta JSON de negócio DEVE usar o envelope único definido neste ADR.
2. O envelope NÃO DEVE ser aplicado a respostas sem corpo, a transferência de arquivo, nem aos endpoints de verificação de saúde e de métricas.
3. As chaves DEVEM usar `camelCase`.
4. O envelope DEVE conter `data` e `status`.
5. `pagination` e `errors` DEVEM estar ausentes quando não aplicáveis, e NÃO DEVEM ser enviados como nulos.
6. `data` DEVE ser o objeto solicitado em consulta por identificador, o vetor de objetos em listagem, e nulo em resposta de falha.

### Status

7. `status.code` DEVE ser identificador estável, em maiúsculas, independente de idioma.
8. `status.code` NÃO DEVE ter sua semântica alterada após publicado; significado novo exige código novo.
9. `status.severity` DEVE ser um de `success`, `warning` ou `error`.
10. `status.message` é texto de reserva e PODE ser omitido quando não houver mensagem a exibir.
11. O cliente DEVE decidir a partir de `status.code`, e NÃO DEVE decidir a partir de `status.message`.
12. O cliente DEVE exibir `status.message` apenas quando não reconhecer o código recebido.
13. O código de status HTTP NÃO DEVE ser replicado no corpo da resposta.
14. O corpo NÃO DEVE contradizer o status HTTP; falha NÃO DEVE ser retornada sob status HTTP de sucesso.

### Erros

15. Resposta de falha DEVE ter `data` nulo.
16. Falha originada na validação de campos DEVE incluir `errors`, com um item por campo inválido.
17. Cada item de `errors` DEVE conter `field` e `code`, e PODE conter `meta` com dados que qualifiquem a violação.
18. `errors` NÃO DEVE conter o valor submetido pelo usuário.
19. Falha inesperada NÃO DEVE incluir `errors` nem qualquer detalhe interno, conforme ADR-0022 §15.
20. O catálogo de códigos DEVE ser único, declarado em ponto central e mantido na URS.

### Paginação

21. Toda listagem DEVE incluir `pagination`.
22. `pagination` DEVE conter `page`, `pageSize` e `hasNext`.
23. `hasNext` DEVE ser determinado pela busca de um registro além do tamanho da página, sem consulta de contagem.
24. `totalItems` e `totalPages` DEVEM ser retornados apenas quando solicitados explicitamente por parâmetro de consulta.
25. `pageSize` DEVE observar o limite máximo estabelecido em ADR-0011 §7.

### Semântica HTTP

26. `200` DEVE ser usado em leitura e em mutação que retorne o recurso.
27. `201` DEVE retornar o recurso criado em `data` e o cabeçalho `Location`.
28. `204` DEVE ser usado quando não houver corpo, e NÃO DEVE conter envelope.
29. As falhas DEVEM observar: `400` para requisição malformada, `401` para não autenticado, `403` para não autorizado, `404` para recurso inexistente, `409` para conflito de estado, `422` para violação de regra de negócio e `500` para falha inesperada.
30. O identificador de correlação DEVE ser retornado no cabeçalho `X-Correlation-Id` em toda resposta, inclusive nas sem corpo e nas de falha.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Replicar o código HTTP no corpo | Cria duas fontes de verdade. O modo de falha típico é responder `200` com código de erro no corpo, fazendo cliente, cache e proxy tratarem a falha como sucesso, e distorcendo a classificação de ADR-0022 §12. |
| Texto da mensagem definido pelo backend | Transfere a cópia de interface para o servidor, que passaria a precisar conhecer o idioma do usuário e impediria texto distinto para a mesma situação em telas diferentes. |
| Ausência de campo de mensagem | Código não reconhecido pelo cliente deixaria o usuário sem retorno algum. |
| Contagem total em toda listagem | Uma consulta de contagem por listagem cresce com a tabela e pressiona a meta de percentil de ADR-0011 §1 nas telas mais usadas. |
| Paginação por cursor | Desempenho constante e imunidade a deslocamento de registros, ao custo de eliminar a navegação por número de página e o total de itens. |
| RFC 9457 (Problem Details) para os erros | Padrão reconhecido por ferramentas, ao custo de duas formas distintas de ler uma resposta; o detalhamento por campo permaneceria como extensão própria de qualquer modo. |
| Resposta sem envelope, apoiada apenas na semântica HTTP | Menos aninhamento e uso mais idiomático do protocolo, ao custo de tratamento distinto a cada endpoint no cliente. |
| Campos não aplicáveis enviados como nulos | Obrigam verificação em todo ponto de uso; a ausência produz união discriminada verificável em tempo de compilação. |
| Eco do valor submetido em `errors` | Reapresentaria dado pessoal em resposta e em log de cliente, contrariando a restrição de ADR-0022 §4. |

## Implicações

1. O catálogo de códigos torna-se artefato mantido, à semelhança do catálogo de permissões.
2. O cliente precisa manter mapa de código para texto; código novo ainda não mapeado recai no texto de reserva, que por isso não pode ser omitido em falhas.
3. A determinação de `hasNext` obriga a buscar um registro além do solicitado em toda listagem.
4. A tela que exibir total de itens paga consulta adicional, de forma explícita e localizada.
5. O envelope aninha o conteúdo sob `data`, o que se reflete nos tipos derivados da especificação e no acesso feito pelo cliente.
