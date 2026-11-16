# ADR-0032 — Módulo `assistance`: análises de apoio ao artigo

- **Status:** Aceito
- **Data:** 2026-11-05
- **Relacionados:** ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0014, ADR-0018, ADR-0019, ADR-0025

## Contexto

`RF-IAA-001` a `RF-IAA-005` reúnem verificações estruturadas e uma análise externa opcional, cujas
saídas são subsídios. Consentimento institucional, resultados e credenciais de provedores não devem
ser misturados à propriedade do artigo.

## Decisão

1. DEVE existir o módulo de negócio `assistance`, proprietário de consentimentos de processamento
   externo e dos resultados de assistência automatizada.
2. O schema PostgreSQL DEVE chamar-se `assistance` e possuir exclusivamente `institution_ai_consent`,
   `article_analysis`, `processed_event` e `assistance_outbox`. Resultados de similaridade são armazenados
   como resultado tipado de `article_analysis`; uma tabela separada de trechos poderá ser introduzida se
   volume ou consulta independente justificar.
3. O consentimento DEVE guardar instituição por ID opaco, versão e conteúdo exato da declaração,
   autor, instante e revogação. `InstitutionFacade` DEVE validar instituição ativa e `AccessFacade`
   titularidade do administrador; consentir não pode iniciar processamento.
4. ABNT, similaridade interna e indícios de autoria DEVEM operar sobre dados obtidos por `ArticleFacade`
   e NÃO DEVEM enviar conteúdo a terceiros. A origem dos artigos coincidentes só pode ser devolvida ao
   orientador responsável.
5. O resumo de entrega só pode chamar provider externo quando a instituição estiver consentida e o
   provider estiver configurado. Ausência de provider ou consentimento mantém íntegra a correção e
   retorna estado explícito de indisponibilidade.
6. Nenhuma análise pode alterar texto, estado de apontamento, nota ou avaliação, nem classificar texto
   como gerado por IA. `AssistanceFacade` é a única superfície pública e transporta DTOs sem ORM.
7. Chamada externa não pode ocorrer dentro de transação. Resultado e evento de conclusão são gravados
   após a resposta do provider, com correlação e versão do contrato.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Análises dentro do módulo `article` | O ciclo de vida e integrações externas têm falhas e dados próprios, diferentes do texto fonte. |
| Serviço externo obrigatório para todas as análises | `RF-IAA-002`, `RF-IAA-003` e `RF-IAA-004` vedam ou não exigem envio externo; `RF-IAA-001` deve ser opcional. |
| Decisão automática com base na análise | `RE-17` atribui decisões do ciclo de correção ao orientador. |

## Implicações

1. O módulo exige integração por fachada com artigo e instituição e configuração explícita de provider.
2. Serviço externo não configurado mantém o resumo indisponível até definição de fornecedor, finalidade,
   declaração e base legal registradas na URS.

## Estado de implementação

O lançamento ainda não tem provider externo: o endpoint permanece indisponível até que toda a configuração
de consentimento e serviço esteja presente. O contrato atual do artigo não armazena medidas tipográficas
suficientes para confirmar os valores de formatação ABNT; a verificação reporta esses campos como ausentes,
sem afirmar conformidade.
