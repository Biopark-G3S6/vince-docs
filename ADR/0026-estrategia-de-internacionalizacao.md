# ADR-0026 — Estratégia de internacionalização

- **Status:** Aceito
- **Data:** 2026-08-19
- **Relacionados:** ADR-0015, ADR-0016, ADR-0017, ADR-0022, ADR-0023, ADR-0025

## Contexto

O sistema é publicado em um único idioma, mas deve admitir outros sem reescrita, e o ADR-0025 §7 já
exige código de resposta independente de idioma sem definir onde a tradução ocorre. Falta fixar o
idioma dos identificadores de software, a origem do texto exibido e a fronteira entre servidor e
cliente na produção desse texto.

## Decisão

### Escopo

1. A internacionalização DEVE alcançar exclusivamente a interface e as mensagens emitidas pelo sistema.
2. Conteúdo produzido por usuário — tema, artigo, apontamento, mensagem, nome de curso, turma ou evento — NÃO DEVE ser traduzido nem ter idioma inferido.
3. O idioma padrão DEVE ser `pt-BR`, único publicado no lançamento.
4. A adição de idioma DEVE ser trabalho de catálogo, e NÃO DEVE exigir alteração de código de feature.

### Idioma dos identificadores

5. Todo identificador de software DEVE ser em inglês: arquivo de código, diretório, tipo, função, variável, tabela, coluna, índice, migração, rota, papel, permissão, código de resposta, nome de fila e chave de cache.
6. Identificador de software NÃO DEVE conter texto destinado à exibição.
7. A documentação do repositório PERMANECE em português; identificador de documento — `ADR-NNNN`, `PAD-<CAT>-<NNN>`, `RF-<CAT>-<NNN>` — NÃO É identificador de software e NÃO DEVE ser traduzido.

### Origem do texto

8. NÃO DEVE existir literal de texto destinado à exibição no código.
9. Todo texto exibido DEVE provir de catálogo de tradução, organizado por idioma e por namespace correspondente à feature.
10. A chave de tradução DEVE ser estável e independente do texto que representa; revisão de redação NÃO DEVE alterar a chave.
11. Chave ausente no idioma selecionado DEVE recair no idioma padrão; ausente também nele, DEVE exibir a própria chave e registrar aviso.
12. Chave órfã e chave ausente DEVEM ser detectadas pelo comando único de verificação (ADR-0023 §8).

### Fronteira com a API

13. A API NÃO DEVE retornar texto destinado à exibição.
14. A tradução DEVE ocorrer no cliente, a partir de `status.code` e de `errors[].code`.
15. `status.message` PERMANECE texto de reserva, exibido apenas quando o cliente não reconhecer o código, conforme ADR-0025 §10 e §12.
16. Os valores a interpolar em mensagem traduzida DEVEM trafegar em `errors[].meta`, e NÃO DEVEM ser embutidos em texto pré-formatado pelo servidor.
17. Todo código do catálogo de códigos de resposta DEVE possuir chave correspondente no catálogo de tradução do idioma padrão.

### Mensagens fora da interface

18. Mensagem emitida por canal externo à interface — notadamente correio eletrônico — DEVE ser renderizada no backend a partir de catálogo próprio, sujeito às mesmas regras de §9 a §12.
19. A renderização DEVE usar a preferência de idioma do destinatário e recair no idioma padrão quando ela não existir.
20. O idioma da mensagem NÃO DEVE ser derivado do idioma do ator que originou a operação.

### Formatação

21. Data, hora, número e moeda DEVEM ser formatados pelas APIs nativas `Intl`, a partir do idioma selecionado.
22. NÃO DEVE ser adotada biblioteca de formatação que embarque dados de localidade próprios.
23. O instante DEVE trafegar em UTC no formato ISO 8601 e ser convertido para o fuso de exibição no cliente.
24. A ordenação de texto apresentada ao usuário DEVE usar `Intl.Collator` com o idioma selecionado, e NÃO DEVE depender da ordenação binária do banco de dados.

### Seleção do idioma

25. A preferência de idioma DEVE ser persistida no perfil do usuário.
26. Na ausência de preferência, o idioma DEVE ser inferido do cabeçalho do navegador e recair no padrão quando não houver correspondência.
27. A troca de idioma NÃO DEVE exigir recarregamento da aplicação nem nova autenticação.

### Implementação

28. A solução de tradução do frontend DEVE ser `i18next` com `react-i18next`.
29. Os catálogos DEVEM ser carregados sob demanda por namespace, e NÃO DEVEM ser embarcados integralmente no artefato inicial.
30. O mecanismo de tradução DEVE residir em `shared/` do frontend; feature NÃO DEVE configurar instância própria.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Tradução no servidor, com texto pronto na resposta | Acopla apresentação a servidor, exige negociação de idioma em toda requisição e contraria ADR-0025 §7 e §11, que já fazem do código a unidade de decisão do cliente. |
| Texto do idioma padrão como chave de tradução | Toda revisão de redação altera a chave e invalida os catálogos dos demais idiomas. |
| Publicação de um segundo idioma no lançamento | Nenhuma parte interessada solicitou idioma adicional; o custo de manutenção do catálogo seria contínuo e sem demanda (URS §10, item 9). |
| Identificadores de software em português | Divergiriam da linguagem das bibliotecas adotadas e produziriam identificadores mistos em cada arquivo. |
| Documentação em inglês | O público da documentação é a própria equipe e as partes interessadas, todas lusófonas; a evidência de elicitação é em português e a tradução quebraria a rastreabilidade exigida por PAD-REQ-005. |
| Solução de tradução em tempo de compilação, com macros | Exige etapa adicional no ferramental de build fixado em ADR-0016 §4, com ganho de artefato desproporcional ao volume de texto do sistema. |
| Bibliotecas de data com dados de localidade próprios | Duplicam o que `Intl` oferece nativamente e ampliam o artefato entregue, contrariando ADR-0016 §24. |

## Implicações

1. Todo requisito funcional passa a exigir chave de tradução para os códigos de resposta que declara; código sem chave no idioma padrão é entrega incompleta.
2. O idioma dos identificadores separa-se do idioma da documentação; a revisão de código verifica as duas convenções.
3. O backend passa a manter catálogo próprio, ainda que restrito às mensagens de correio eletrônico, e a persistir a preferência de idioma do usuário para usá-la.
4. A verificação de chaves órfãs e ausentes integra o comando único de verificação, e sua falha reprova a integração.
5. Publicar um segundo idioma passa a ser tradução de catálogo, sem alteração de código de feature.
