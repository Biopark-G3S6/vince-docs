# URS — Especificação de Requisitos do Usuário

**Projeto:** VinceArt
**Versão:** 0.9
**Status:** Rascunho — em elaboração
**Data:** 2026-08-11

---

## 1. Objetivo e escopo do documento

Este documento especifica os requisitos do sistema VinceArt. Nesta versão estão consolidados
exclusivamente os **requisitos não funcionais e as restrições** decorrentes das decisões de
arquitetura tomadas até a data acima. Os requisitos funcionais permanecem pendentes de
consolidação (seção 5).

Este documento declara **o que o sistema deve satisfazer**. As decisões que determinam **como**
cada requisito é satisfeito estão registradas em `ADR/`, referenciadas na coluna de rastreio.

---

## 2. Convenções

### 2.1 Termos normativos

| Termo | Significado |
| :--- | :--- |
| **DEVE** / **NÃO DEVE** | Obrigatório / proibido. Não conformidade reprova a entrega. |
| **PODE** | Permitido, sem obrigação. |

### 2.2 Identificação

`<TIPO>-<CATEGORIA>-<NNN>`, com numeração sequencial e imutável dentro da categoria.

| Tipo | Significado |
| :--- | :--- |
| `RF` | Requisito funcional |
| `RNF` | Requisito não funcional |
| `RES` | Restrição de projeto — imposta, não derivada de análise |

### 2.3 Prioridade

| Sigla | Significado |
| :--- | :--- |
| **E** | Essencial — sem ele o sistema não atende ao propósito. |
| **I** | Importante — ausência degrada significativamente o resultado. |
| **D** | Desejável — agrega valor, pode ser postergado. |

### 2.4 Origem

| Sigla | Significado |
| :--- | :--- |
| `ARQ` | Decisão de arquitetura registrada em ADR. |
| `STK` | Imposição de stakeholder. |
| `ELI` | Elicitação junto a usuários. |

---

## 3. Visão geral do sistema

> **Pendente.** A ser redigida após a consolidação dos requisitos funcionais.

---

## 4. Partes interessadas

> **Pendente.** A ser consolidada a partir do material em `Requisitos/Coleta de Requisitos/`.

---

## 5. Requisitos funcionais

### 5.1 Estrutura do requisito funcional

Todo requisito funcional DEVE conter os campos abaixo. Requisito que omita campo obrigatório
DEVE ser considerado incompleto e NÃO DEVE ser encaminhado à implementação.

| Campo | Obrigatório | Conteúdo |
| :--- | :--: | :--- |
| Identificador | Sim | `RF-<CATEGORIA>-<NNN>` |
| Nome | Sim | Frase verbal curta, na voz do usuário |
| Descrição | Sim | O que o sistema deve permitir, sem definir solução técnica |
| Ator | Sim | Perfil que executa a ação |
| Pré-condições | Sim | Estado exigido para que a ação seja possível |
| Fluxo principal | Sim | Sequência de passos do caminho de sucesso |
| Fluxos alternativos e de exceção | Sim | Desvios, erros e seus tratamentos |
| Regras de negócio | Sim | Invariantes e validações aplicáveis |
| **Permissões geradas** | **Sim** | Permissões `RECURSO:ACAO` originadas por este requisito |
| Escopo de titularidade | Sim | Se a ação é restrita a registros do próprio ator; ausente quando irrestrita |
| Prioridade | Sim | `E`, `I` ou `D` |
| Origem | Sim | `STK`, `ELI` ou `ARQ` |
| Critério de aceitação | Sim | Condição objetiva e verificável de conclusão |
| Rastreio | Não | RNFs e ADRs relacionados |

O campo **Permissões geradas** decorre de `RNF-SEG-008`. O campo **Escopo de titularidade** decorre
de `RNF-SEG-010`: RBAC autoriza a ação, mas não autoriza a ação sobre um registro específico — a
distinção precisa estar declarada no requisito, não deduzida na implementação.

### 5.2 Requisitos

> **Pendente.** A elicitação está em andamento; o material bruto encontra-se em
> `Requisitos/Coleta de Requisitos/`. Os requisitos funcionais serão consolidados,
> identificados e priorizados em versão posterior deste documento.

### 5.3 Catálogo de permissões

Consolida as permissões declaradas pelos requisitos funcionais. É documento derivado: nenhuma
permissão DEVE constar aqui sem requisito de origem (`RNF-SEG-008`).

**Formato:** `RECURSO:ACAO` — recurso no singular, ambos em maiúsculas, sem curinga.
Exemplo: `USUARIO:CRIAR`, `USUARIO:ATUALIZAR`, `USUARIO:EXCLUIR`, `USUARIO:CONSULTAR`.

| Permissão | Recurso | Requisito de origem | Descrição |
| :--- | :--- | :--- | :--- |
| *(a preencher)* | | | |

> **Pendente.** Será preenchido conforme os requisitos funcionais forem consolidados em 5.2.

### 5.4 Catálogo de códigos de resposta

Consolida os códigos retornados em `status.code` e em `errors[].code`, conforme ADR-0025.
É documento derivado: nenhum código DEVE existir sem requisito ou regra de negócio que o origine.

**Formato:** identificador em maiúsculas, sem acento, independente de idioma.
Exemplo de estado: `ARTIGO_CRIADO`, `VALIDACAO_FALHOU`. Exemplo de campo: `OBRIGATORIO`,
`TAMANHO_MAXIMO_EXCEDIDO`.

| Código | Escopo | Severidade | Origem | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| *(a preencher)* | | | | |

> **Pendente.** Será preenchido conforme os requisitos funcionais forem consolidados em 5.2.

---

## 6. Requisitos não funcionais

### 6.1 Modularidade e manutenibilidade

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-MOD-001 | O backend DEVE ser organizado em módulos delimitados por capacidade de negócio, e não por camada técnica. | E | ARQ | Inspeção da estrutura de diretórios contra a estrutura normativa. | ADR-0001 §1; ADR-0003 §1, §2 |
| RNF-MOD-002 | Cada módulo DEVE expor uma única superfície pública, sendo todo o restante de sua implementação inacessível aos demais módulos. | E | ARQ | Análise estática: nenhuma importação entre módulos fora de `contracts/`. | ADR-0004 §1, §4, §5 |
| RNF-MOD-003 | Um módulo NÃO DEVE depender de detalhe de implementação de outro módulo. | E | ARQ | Análise estática de importações; ausência de referência a classe concreta externa. | ADR-0004 §6; ADR-0005 §1, §5 |
| RNF-MOD-004 | A conformidade com as fronteiras entre módulos DEVE ser verificada automaticamente a cada integração, impedindo a incorporação de código não conforme. | E | ARQ | Pipeline de CI reprova build com violação de fronteira. | ADR-0007 §1, §6, §7 |
| RNF-MOD-005 | NÃO DEVEM existir dependências cíclicas entre módulos. | E | ARQ | Verificação automatizada de ciclos no CI. | ADR-0005 §6; ADR-0007 §10 |
| RNF-MOD-006 | A adição ou remoção de um módulo NÃO DEVE exigir alteração no código dos demais módulos. | E | ARQ | Remoção do módulo do composition root sem erro de compilação nos demais. | ADR-0003 §10, §11 |
| RNF-MOD-007 | O código DEVE observar os princípios SOLID, DRY e KISS, com precedência definida em caso de conflito. | E | STK | Critério explícito de revisão de código. | ADR-0001 §5; ADR-0009 |
| RNF-MOD-008 | Código de infraestrutura transversal compartilhado NÃO DEVE conter semântica de negócio. | I | ARQ | Inspeção do conteúdo de `shared/` em revisão. | ADR-0009 §4, §5, §7 |
| RNF-MOD-009 | Cada fila de processamento assíncrono DEVE ser de propriedade de um único módulo, e NÃO DEVE ser publicada ou consumida por módulo diverso do proprietário. | E | STK | Inspeção do registro de filas por módulo; análise estática. | ADR-0012 §7; ADR-0020 §5–§9 |
| RNF-MOD-010 | Nenhum módulo DEVE acessar model de dados pertencente a outro módulo, ainda que o cliente de persistência seja único no processo. | E | ARQ | Inspeção do cliente escopado; regra de análise estática. | ADR-0010 §4, §5, §6 |
| RNF-MOD-011 | O frontend DEVE ser organizado em features correspondentes aos módulos do backend, cada uma com superfície pública única, e NÃO DEVE ter diretórios de primeiro nível por camada técnica fora de `shared/`. | E | ARQ | Inspeção da estrutura; análise estática de importações entre features. | ADR-0015 §1–§5 |
| RNF-MOD-012 | As fronteiras entre features do frontend DEVEM ser verificadas automaticamente na integração contínua, com violação classificada como erro, e NÃO DEVEM existir dependências cíclicas entre features. | E | ARQ | Pipeline reprova build com violação de fronteira ou ciclo. | ADR-0015 §8, §9 |
| RNF-MOD-013 | Dado proveniente da API NÃO DEVE ser copiado para store de estado de cliente nem tratado como fonte da verdade no frontend. | E | ARQ | Inspeção dos stores; ausência de dado originado da API. | ADR-0015 §11–§13 |
| RNF-MOD-014 | Componente de biblioteca visual do frontend NÃO DEVE conter regra de negócio nem realizar chamada à API. | I | ARQ | Inspeção de `shared/ui/`. | ADR-0016 §21 |
| RNF-MOD-015 | Toda fila DEVE ser nomeada com o prefixo do módulo proprietário e toda chave criada no Redis DEVE ser prefixada pelo nome do módulo. | E | ARQ | Análise estática dos nomes de fila e de chave. | ADR-0020 §5, §6, §9 |
| RNF-MOD-016 | Um módulo NÃO DEVE enfileirar tarefa em fila de outro módulo, nem conhecer os módulos consumidores dos eventos que publica. | E | ARQ | Inspeção do registro de filas e do publicador. | ADR-0020 §13; ADR-0021 §18 |
| RNF-MOD-017 | Módulo de plataforma DEVE observar integralmente as mesmas regras estruturais dos módulos de negócio, e sua criação DEVE ser justificada pela existência de dados próprios que `shared/` não pode possuir. | E | ARQ | Inspeção da estrutura e da justificativa no ADR do módulo. | ADR-0003 §1, §14, §15 |
| RNF-MOD-018 | DEVE existir um único comando de verificação, definido em ponto único e reutilizado por gancho local e por execução remota, executando tipos, análise estática, formatação, fronteiras e testes. | E | ARQ | Comparação entre a definição local e a do workflow remoto. | ADR-0023 §8–§10 |

### 6.2 Evolutividade e capacidade de extração

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-EVO-001 | Qualquer módulo DEVE poder ser extraído para serviço independente sem alteração no código dos módulos consumidores. | E | STK | Substituição da implementação da fachada por cliente remoto, sem alteração em consumidores. | ADR-0001 §3; ADR-0004 §10 |
| RNF-EVO-002 | A extração de um módulo NÃO DEVE exigir migração de dados nem alteração de schema pertencente a outro módulo. | E | ARQ | Ausência de junções e de chaves estrangeiras entre módulos. | ADR-0006 §3, §4 |
| RNF-EVO-003 | Toda decisão arquitetural DEVE ser registrada de forma versionada, rastreável e imutável. | I | ARQ | Existência do ADR correspondente antes da implementação. | ADR-0000 |
| RNF-EVO-004 | Alteração incompatível em contrato público de módulo DEVE permitir convivência entre versões durante a migração dos consumidores. | I | ARQ | Revisão de contrato; presença das duas versões no período de transição. | ADR-0004 §11 |
| RNF-EVO-005 | Módulo extraído para serviço independente DEVE receber a identidade já autenticada pela borda e NÃO DEVE reautenticar credencial de usuário final. | I | ARQ | Inspeção do fluxo de autenticação do módulo extraído. | ADR-0013 §19 |
| RNF-EVO-006 | Os tipos do contrato de API usados pelo frontend DEVEM ser derivados da especificação publicada pelo backend, e divergência entre ambos DEVE reprovar o build do frontend. | E | ARQ | Regeneração dos tipos na integração contínua com comparação. | ADR-0017 §1–§5 |
| RNF-EVO-007 | O backend DEVE publicar especificação de API gerada a partir do próprio código, mantida como contrato e não como documentação. | E | ARQ | Comparação entre a especificação publicada e as rotas expostas. | ADR-0017 §1 |
| RNF-EVO-008 | A extração dos dados de um módulo DEVE ser possível pelo despejo integral de seu schema, sem seleção manual de tabelas. | E | ARQ | Despejo e restauração do schema de um módulo em instância distinta. | ADR-0018 §1, §2 |
| RNF-EVO-009 | Toda resposta JSON de negócio DEVE usar o envelope único com `data` e `status`, em `camelCase`, omitindo `pagination` e `errors` quando não aplicáveis em vez de enviá-los nulos. | E | STK | Inspeção das respostas de cada endpoint contra o envelope. | ADR-0025 §1–§6 |
| RNF-EVO-010 | `status.code` DEVE ser identificador estável e independente de idioma, e NÃO DEVE ter sua semântica alterada após publicado; o cliente DEVE decidir por ele, nunca pelo texto da mensagem. | E | ARQ | Inspeção do catálogo e do tratamento no cliente. | ADR-0025 §7, §8, §11 |
| RNF-EVO-011 | O código de status HTTP NÃO DEVE ser replicado no corpo, e o corpo NÃO DEVE contradizer o status HTTP. | E | ARQ | Verificação de falha retornada sob status de sucesso. | ADR-0025 §13, §14 |
| RNF-EVO-012 | Falha de validação DEVE incluir `errors` com um item por campo inválido, contendo identificação do campo e código; falha inesperada NÃO DEVE incluir `errors`. | E | ARQ | Submissão com múltiplos campos inválidos e provocação de falha inesperada. | ADR-0025 §16, §17, §19 |

### 6.3 Escalabilidade e desempenho

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-ESC-001 | O sistema DEVE permitir escalar de forma independente a capacidade de processamento de cada módulo, sem replicar a aplicação inteira e sem extrair o módulo para serviço próprio. | E | STK | Execução do artefato com papel e conjunto de módulos definidos por variável de ambiente. | ADR-0008 §2, §6, §11 |
| RNF-ESC-002 | Todo processo da aplicação DEVE ser stateless, admitindo replicação horizontal sem afinidade de sessão. | E | ARQ | Ausência de estado em memória entre requisições; teste com múltiplas réplicas. | ADR-0008 §9 |
| RNF-ESC-003 | Processamento intensivo de CPU ou de longa duração NÃO DEVE ser executado no ciclo de requisição HTTP. | E | ARQ | Inspeção dos casos de uso expostos por rota; medição de tempo de resposta. | ADR-0008 §12 |
| RNF-ESC-004 | Nenhum módulo DEVE presumir execução no mesmo processo que outro módulo. | E | ARQ | Ausência de comunicação por estado compartilhado em memória. | ADR-0008 §10 |
| RNF-ESC-005 | O tempo de resposta medido no servidor DEVE observar: leitura — p95 ≤ 300 ms e p99 ≤ 800 ms; escrita transacional — p95 ≤ 500 ms e p99 ≤ 1500 ms. | E | STK | Teste de carga sob a carga de referência, com medição por percentil. | ADR-0011 §1, §2 |
| RNF-ESC-006 | A disponibilidade mensal DEVE ser de, no mínimo, 99,5%. | I | ARQ | Monitoramento de disponibilidade em janela mensal. | ADR-0011 §4 |
| RNF-ESC-007 | A experiência de carregamento do frontend DEVE observar, no percentil 75: LCP ≤ 2,5 s, INP ≤ 200 ms e CLS ≤ 0,1. | I | STK | Medição de campo das métricas Core Web Vitals. | ADR-0011 §3 |
| RNF-ESC-008 | Toda listagem DEVE ser paginada, com limite máximo de 100 itens por página. | E | ARQ | Inspeção do contrato da API; requisição acima do limite. | ADR-0011 §6, §7 |
| RNF-ESC-009 | Toda chamada a dependência externa DEVE declarar timeout explícito. | E | ARQ | Inspeção de código; teste com dependência não responsiva. | ADR-0011 §8 |
| RNF-ESC-010 | O número de consultas ao banco por requisição DEVE ser constante em relação à quantidade de registros retornados. | E | STK | Teste de invariância: mesmo endpoint com um e com dez registros DEVE emitir a mesma contagem de consultas. | ADR-0011 §9, §10, §12 |
| RNF-ESC-011 | Divergência no teste de invariância de contagem de consultas DEVE reprovar o build. | E | ARQ | Execução do teste no pipeline de CI. | ADR-0011 §11 |
| RNF-ESC-012 | Toda coluna utilizada como filtro ou ordenação de consulta recorrente DEVE possuir índice. | I | ARQ | Revisão de migração; análise de plano de execução. | ADR-0011 §16 |
| RNF-ESC-013 | A carga de referência sob a qual as metas de desempenho são aferidas DEVE ser definida. | I | — | *A definir.* | ADR-0011 §17; *pendente* |
| RNF-ESC-014 | O código do frontend DEVE ser dividido por rota, e conteúdo carregado de forma assíncrona DEVE ter espaço reservado com dimensão equivalente à do conteúdo final. | I | ARQ | Inspeção dos pacotes gerados por rota; medição de CLS. | ADR-0015 §16, §17 |
| RNF-ESC-015 | NÃO DEVE ser adotada no frontend solução de estilo com custo em tempo de execução. | I | ARQ | Inspeção das dependências de estilização. | ADR-0016 §20 |
| RNF-ESC-016 | O tamanho do pool de conexões por processo DEVE ser declarado, e o produto entre réplicas e pool DEVE caber em orçamento de conexões inferior ao limite do servidor, com reserva para migração e manutenção. | E | ARQ | Cálculo do orçamento contra a configuração de réplicas; medição das conexões em uso. | ADR-0019 §9–§13 |
| RNF-ESC-017 | A indicação de existência de próxima página DEVE ser obtida pela busca de um registro além do tamanho da página, sem consulta de contagem; totais DEVEM ser retornados apenas quando solicitados explicitamente. | E | ARQ | Inspeção das consultas emitidas em listagem com e sem solicitação de totais. | ADR-0025 §22–§24 |

### 6.4 Confiabilidade e integridade

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-CON-001 | Todo dado persistido DEVE ter exatamente um módulo proprietário, responsável por sua escrita. | E | ARQ | Mapa de propriedade de tabelas por módulo; análise estática de acesso. | ADR-0006 §1, §2 |
| RNF-CON-002 | O reprocessamento de uma mesma mensagem ou evento NÃO DEVE produzir efeito duplicado. | E | ARQ | Teste de entrega repetida com verificação de estado final. | ADR-0005 §10; ADR-0012 §16 |
| RNF-CON-003 | Falha no processamento assíncrono de um módulo NÃO DEVE reverter nem impedir a conclusão da operação do módulo publicador. | E | ARQ | Teste de falha injetada no consumidor. | ADR-0005 §12 |
| RNF-CON-004 | A integridade referencial entre dados de módulos distintos DEVE ser assegurada pela aplicação. | E | ARQ | Validação no módulo proprietário; teste de referência inexistente. | ADR-0006 §4, §5 |
| RNF-CON-005 | O sistema DEVE tolerar consistência eventual entre módulos, e a interface DEVE representar esse estado quando perceptível ao usuário. | I | ARQ | Revisão de fluxos assíncronos com reflexo em interface. | ADR-0005 §2; ADR-0006 §7 |
| RNF-CON-006 | Réplica local de dado pertencente a outro módulo NÃO DEVE ser tratada como fonte da verdade nem alterada por escrita própria. | E | ARQ | Inspeção das projeções; ausência de escrita fora do consumo de evento. | ADR-0006 §7, §8 |
| RNF-CON-007 | Toda fila DEVE aplicar número máximo de tentativas e backoff exponencial com jitter, sendo o padrão de 5 tentativas, atraso inicial de 5 s, fator 2 e teto de 5 min. | E | STK | Inspeção da configuração da fila; teste de falha sucessiva com medição dos intervalos. | ADR-0012 §1–§4 |
| RNF-CON-008 | Falhas DEVEM ser classificadas em transitórias e permanentes; falha permanente NÃO DEVE ser retentada e DEVE ser encaminhada imediatamente à dead-letter queue. | E | ARQ | Teste com payload inválido: ausência de retentativa e encaminhamento imediato. | ADR-0012 §5, §6 |
| RNF-CON-009 | Cada fila DEVE possuir dead-letter queue de propriedade do mesmo módulo, e NÃO DEVE existir consumidor automático de dead-letter queue. | E | STK | Inspeção da topologia de filas e dos consumidores registrados. | ADR-0012 §7, §9 |
| RNF-CON-010 | Mensagem irrecuperável NÃO DEVE ser descartada; DEVE ser retida por no mínimo 30 dias com payload original, histórico de tentativas, erro e identificador de correlação. | E | ARQ | Teste de esgotamento de tentativas com inspeção do conteúdo retido. | ADR-0012 §8, §12, §15 |
| RNF-CON-011 | O reprocessamento a partir da dead-letter queue DEVE ser ação explícita, sujeita a permissão e registrada em auditoria. | E | ARQ | Tentativa de reprocessamento sem permissão; verificação da trilha de auditoria. | ADR-0012 §10, §11 |
| RNF-CON-012 | O ingresso de mensagem em dead-letter queue DEVE emitir alerta observável, e o crescimento sustentado de uma dead-letter queue DEVE ser tratado como incidente. | I | ARQ | Simulação de falha permanente com verificação do alerta emitido. | ADR-0012 §13, §14 |
| RNF-CON-013 | Cada módulo DEVE possuir schema próprio no banco de dados, com todas as suas tabelas nele residentes; NÃO DEVE existir schema compartilhado nem tabela de negócio em `public`. | E | ARQ | Inspeção da distribuição de tabelas por schema. | ADR-0018 §1–§4 |
| RNF-CON-014 | A chave primária de toda tabela DEVE ser um UUID versão 7 gerado pela aplicação. | E | ARQ | Inspeção do schema e da origem da geração do identificador. | ADR-0018 §9, §10 |
| RNF-CON-015 | Referência a registro do mesmo módulo DEVE declarar chave estrangeira; referência a registro de outro módulo DEVE ser coluna de identificador indexada, sem chave estrangeira. | E | ARQ | Inspeção das restrições e dos índices declarados. | ADR-0018 §12–§14 |
| RNF-CON-016 | Colunas de data e hora DEVEM usar tipo com fuso horário, e toda tabela DEVE registrar instante de criação e de última atualização. | E | ARQ | Inspeção dos tipos de coluna declarados. | ADR-0018 §15, §17 |
| RNF-CON-017 | Toda transação DEVE estar contida em um único caso de uso de um único módulo, com tempo limite declarado, sem abranger chamada à fachada de outro módulo nem chamada de rede. | E | ARQ | Inspeção do escopo transacional; teste com dependência externa não responsiva. | ADR-0019 §1–§5 |
| RNF-CON-018 | A gravação do evento em outbox DEVE ocorrer na mesma transação do fato que o originou, e a consistência entre módulos NÃO DEVE ser obtida por transação distribuída. | E | ARQ | Teste de falha após o commit do fato, com verificação da presença do evento. | ADR-0019 §7, §8 |
| RNF-CON-019 | Cada módulo DEVE possuir tabela de outbox em seu próprio schema, e o evento NÃO DEVE ser publicado no barramento dentro da transação que o originou. | E | ARQ | Inspeção do schema e do ponto de publicação. | ADR-0021 §1–§3 |
| RNF-CON-020 | A entrega de eventos é garantida como pelo menos uma vez; a publicação DEVE preservar a ordem de criação dentro de cada módulo e a linha DEVE ser marcada apenas após confirmação. | E | ARQ | Teste de falha entre publicação e marcação, com verificação de republicação. | ADR-0021 §8–§11 |
| RNF-CON-021 | A falha de entrega a um consumidor NÃO DEVE impedir a entrega aos demais; cada fila de consumidor DEVE possuir retentativa e dead-letter queue próprias. | E | ARQ | Falha injetada em um consumidor com verificação dos demais. | ADR-0021 §14, §16, §17 |
| RNF-CON-022 | Linhas de outbox publicadas DEVEM ser marcadas e expurgadas após 7 dias; linha não publicada NÃO DEVE ser expurgada. | I | ARQ | Execução da rotina de expurgo com verificação das linhas remanescentes. | ADR-0021 §19–§21 |

### 6.5 Observabilidade

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-OBS-001 | Fluxo de negócio que atravesse módulos DEVE ser rastreável de ponta a ponta por identificador de correlação. | I | ARQ | Rastreio de uma operação completa nos registros de log. | ADR-0005 (implicações); ADR-0009 §4 |
| RNF-OBS-002 | Cada processo DEVE identificar, em seus registros, o papel de execução e os módulos ativos. | I | ARQ | Inspeção dos registros de log de processos `api` e `worker`. | ADR-0008 (implicações) |
| RNF-OBS-003 | Cada processo DEVE expor endpoint de verificação de saúde. | I | ARQ | Requisição ao endpoint em ambos os papéis. | ADR-0008 §5 |
| RNF-OBS-004 | Consulta ao banco com duração superior a 200 ms DEVE ser registrada em log em ambiente de desenvolvimento, e estatísticas de consulta DEVEM estar habilitadas em produção. | I | ARQ | Inspeção do log em desenvolvimento; verificação de `pg_stat_statements` em produção. | ADR-0011 §14, §15 |
| RNF-OBS-005 | Toda negativa de autorização DEVE ser registrada em log. | I | ARQ | Requisição sem permissão com verificação do registro. | ADR-0014 §14 |
| RNF-OBS-006 | O atraso entre a gravação e a publicação de um evento DEVE ser observável e sujeito a alerta, e o crescimento sustentado de eventos não publicados DEVE ser tratado como incidente. | I | ARQ | Interrupção do relay com verificação do alerta emitido. | ADR-0021 §13, §22 |
| RNF-OBS-007 | Todo processo DEVE emitir log estruturado na saída padrão como canal primário e síncrono, sem depender de banco de dados, fila ou serviço externo. | E | ARQ | Registro de falha com banco e fila indisponíveis. | ADR-0022 §1, §2 |
| RNF-OBS-008 | As falhas DEVEM ser classificadas em esperadas e inesperadas, registradas na mesma estrutura e distinguidas por classificação. | E | STK | Inspeção da estrutura e da classificação atribuída. | ADR-0022 §12, §16 |
| RNF-OBS-009 | O registro de erros DEVE ser agregado por assinatura derivada do tipo da exceção, do primeiro quadro do código do projeto e da mensagem normalizada, sem número de linha; NÃO DEVE ser persistida uma linha por ocorrência. | E | ARQ | Geração de ocorrências repetidas com verificação de uma única linha e do contador. | ADR-0022 §20–§25 |
| RNF-OBS-010 | Falha inesperada DEVE reter amostras de contexto em quantidade limitada; falha esperada NÃO DEVE reter contexto. As assinaturas DEVEM ser retidas indefinidamente e as amostras expurgadas em 30 dias. | E | ARQ | Execução da rotina de expurgo com verificação do que permanece. | ADR-0022 §26–§29 |
| RNF-OBS-011 | A falha na publicação ou na persistência de um erro NÃO DEVE propagar-se à requisição de origem. | E | ARQ | Indisponibilidade do consumidor de erros durante requisição bem-sucedida. | ADR-0022 §19 |
| RNF-OBS-012 | Cada processo DEVE expor métricas em formato Prometheus, em porta distinta da API e não publicada externamente, incluindo latência por rota, profundidade de filas, atraso do outbox, ingresso em dead-letter queue e conexões em uso. | I | ARQ | Requisição ao endpoint pela rede interna e tentativa pela externa. | ADR-0022 §31–§33 |
| RNF-OBS-013 | A verificação de saúde DEVE distinguir vivacidade de prontidão; a vivacidade NÃO DEVE consultar dependência externa e a prontidão NÃO DEVE reprovar por indisponibilidade transitória. | E | ARQ | Indisponibilidade breve de dependência com verificação de que as réplicas permanecem em rotação. | ADR-0008 §14 |

### 6.6 Segurança

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-SEG-001 | Autenticação e autorização DEVEM ser tratadas de forma transversal, fora da regra de negócio dos módulos, e nenhum módulo DEVE implementar mecanismo próprio. | E | ARQ | Inspeção da localização do mecanismo; ausência de implementação em módulos. | ADR-0009 §4; ADR-0013 §17, §18; ADR-0014 §22, §23 |
| RNF-SEG-002 | A autenticação DEVE ser baseada em sessão opaca mantida no servidor, com identificador sem significado semântico e no mínimo 128 bits de entropia. | E | STK | Inspeção do identificador emitido; ausência de dado decodificável. | ADR-0013 §1–§5 |
| RNF-SEG-003 | A sessão DEVE expirar por inatividade em 8 horas e por prazo absoluto em 7 dias; a janela de inatividade DEVE ser renovada a cada requisição autenticada e o prazo absoluto NÃO DEVE ser renovado. | E | ARQ | Teste de expiração por inatividade e por prazo absoluto. | ADR-0013 §6, §7 |
| RNF-SEG-004 | O encerramento de sessão DEVE ter efeito imediato, e DEVE ser possível revogar em uma operação todas as sessões ativas de um usuário. | E | ARQ | Requisição com credencial encerrada imediatamente após o encerramento. | ADR-0013 §10, §11 |
| RNF-SEG-005 | A credencial de sessão DEVE ser transportada em cookie `HttpOnly`, `Secure`, `SameSite` e com `Path` restrito, e NÃO DEVE trafegar em URL, corpo de requisição, cabeçalho customizado ou armazenamento acessível a script. | E | ARQ | Inspeção dos atributos do cookie e do armazenamento no cliente. | ADR-0013 §8, §9 |
| RNF-SEG-006 | Toda requisição que altere estado DEVE ser protegida contra falsificação de requisição entre sítios. | E | ARQ | Requisição forjada a partir de origem distinta. | ADR-0013 §13, §14 |
| RNF-SEG-007 | A autorização DEVE ser baseada em papéis, com permissões no formato `RECURSO:ACAO` e sem curinga. | E | STK | Inspeção do catálogo de permissões e do mecanismo de verificação. | ADR-0014 §1–§5 |
| RNF-SEG-008 | Todo requisito funcional DEVE declarar as permissões que origina, e NÃO DEVE existir permissão sem requisito funcional de origem. | E | STK | Revisão da seção 5 desta URS contra o catálogo em 5.3. | ADR-0014 §6–§8 |
| RNF-SEG-009 | As permissões efetivas DEVEM ser resolvidas no servidor a cada requisição, com cache invalidado imediatamente a cada alteração de papel, concessão ou revogação. | E | ARQ | Teste de revogação com verificação de efeito na requisição seguinte. | ADR-0014 §9, §10 |
| RNF-SEG-010 | A verificação de permissão DEVE ocorrer na borda, e a titularidade do registro DEVE ser verificada dentro do caso de uso; regras de titularidade NÃO DEVEM ser modeladas como permissões. | E | ARQ | Teste com usuário autorizado operando sobre registro de terceiro. | ADR-0014 §11–§13 |
| RNF-SEG-011 | A concessão de permissão DEVE ser restrita às permissões efetivas do concedente e condicionada à posse da permissão de concessão; um usuário NÃO DEVE conceder permissão a si mesmo. | E | STK | Teste de concessão de permissão não possuída e de autoconcessão. | ADR-0014 §15, §16 |
| RNF-SEG-012 | A revogação de uma permissão de um usuário NÃO DEVE revogar as concessões por ele realizadas. | E | STK | Teste de revogação do concedente com verificação do beneficiário. | ADR-0014 §17 |
| RNF-SEG-013 | Toda concessão e toda revogação DEVEM ser registradas em trilha de auditoria imutável, com concedente, beneficiário, permissão e instante. | E | ARQ | Inspeção da trilha após concessão e revogação. | ADR-0014 §18 |
| RNF-SEG-014 | DEVE existir consulta das concessões diretas ativas de um usuário, com concedente e data; a concessão PODE ter prazo de validade e sua revogação DEVE ser possível a qualquer momento por usuário com permissão de revogação. | E | ARQ | Execução da consulta; teste de expiração e de revogação por terceiro autorizado. | ADR-0014 §19–§21 |
| RNF-SEG-015 | O tratamento de dados pessoais DEVE observar a legislação aplicável. | E | — | *A definir.* | *Pendente* |
| RNF-SEG-016 | O identificador de sessão DEVE ser regenerado na autenticação bem-sucedida e em qualquer elevação de privilégio. | E | ARQ | Comparação do identificador antes e depois da autenticação. | ADR-0013 §12 |
| RNF-SEG-017 | A indisponibilidade do repositório de sessões DEVE resultar em negativa de autenticação; NÃO DEVE existir modo degradado que aceite requisição sem verificação. | E | ARQ | Requisição com o repositório de sessões indisponível. | ADR-0013 §16 |
| RNF-SEG-018 | As permissões expostas ao cliente destinam-se exclusivamente à composição da interface e NÃO DEVEM ser consideradas em decisão de autorização. | E | ARQ | Requisição direta à API sem a permissão, com a ação oculta na interface. | ADR-0013 §20; ADR-0014 §11; ADR-0015 §19, §20 |
| RNF-SEG-019 | O backend DEVE restringir as origens aceitas a uma lista explícita e NÃO DEVE aceitar origem curinga; frontend e backend DEVEM ser servidos sob o mesmo domínio registrável. | E | ARQ | Requisição a partir de origem não listada. | ADR-0017 §9, §10 |
| RNF-SEG-020 | Rota protegida NÃO DEVE ser renderizada antes da resolução da identidade do usuário. | E | ARQ | Acesso direto a rota protegida sem sessão estabelecida. | ADR-0015 §18; ADR-0017 §16 |
| RNF-SEG-021 | O consumidor de uma mensagem NÃO DEVE executar com a autoridade do usuário que a originou; o identificador do ator destina-se exclusivamente a auditoria. | E | ARQ | Processamento de mensagem cujo ator perdeu a permissão original. | ADR-0020 §17 |
| RNF-SEG-022 | O payload de uma mensagem NÃO DEVE conter entidade de domínio, tipo gerado pelo ORM nem dado pessoal além do estritamente necessário ao processamento. | E | ARQ | Inspeção dos payloads publicados. | ADR-0020 §15, §16 |
| RNF-SEG-023 | Os campos registrados em log e em contexto de erro DEVEM ser definidos por lista de permissão declarada em ponto único; NÃO DEVE ser usada lista de bloqueio. | E | ARQ | Introdução de campo sensível não declarado, com verificação de sua ausência no registro. | ADR-0022 §4, §5 |
| RNF-SEG-024 | A resposta ao cliente NÃO DEVE conter mensagem de exceção, rastro de pilha ou identificação de componente interno, e DEVE conter o identificador de correlação. | E | ARQ | Provocação de falha inesperada com inspeção da resposta. | ADR-0022 §10, §15; ADR-0025 §30 |
| RNF-SEG-025 | O detalhamento de erro por campo NÃO DEVE conter o valor submetido pelo usuário. | E | ARQ | Submissão de campo inválido com dado pessoal e inspeção da resposta. | ADR-0025 §18 |

---

### 6.7 Verificação e qualidade

| ID | Requisito | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| RNF-VER-001 | O ambiente de desenvolvimento DEVE ser provisionado por Docker Compose, com PostgreSQL e Redis em versões fixadas correspondentes às de produção, iniciado por um único comando e com carga inicial reproduzível. | E | STK | Provisionamento em máquina limpa a partir do repositório. | ADR-0023 §1–§5 |
| RNF-VER-002 | A integração na ramificação principal DEVE ocorrer por pull request, e a ramificação DEVE ter proteção que exija a aprovação do workflow de verificação como condição de incorporação. | E | ARQ | Tentativa de incorporação com verificação reprovada. | ADR-0023 §16–§18 |
| RNF-VER-003 | O gancho de pré-commit DEVE executar formatação e análise estática sobre os arquivos alterados; o gancho de pré-push DEVE executar o comando de verificação completo. | E | ARQ | Commit e push com violação deliberada. | ADR-0023 §11, §12 |
| RNF-VER-004 | A fronteira do teste unitário DEVE ser o caso de uso exercitado pela fachada, com o interno do módulo real; somente fachadas de outros módulos DEVEM ser substituídas. | E | STK | Inspeção dos testes; refatoração interna sem quebra de teste. | ADR-0024 §2–§5 |
| RNF-VER-005 | Repositórios e adaptadores DEVEM ser testados contra PostgreSQL e Redis reais; NÃO DEVE ser usado substituto em memória do banco de dados. | E | ARQ | Inspeção da configuração de teste. | ADR-0024 §9, §10 |
| RNF-VER-006 | O isolamento entre testes DEVE usar schema por processo com truncate entre testes; NÃO DEVE usar transação revertida. | E | ARQ | Execução paralela da suíte com verificação de ausência de interferência. | ADR-0024 §11–§13 |
| RNF-VER-007 | Toda regra de negócio, todo caso de uso e toda correção de defeito DEVEM possuir teste correspondente. | E | STK | Revisão de código contra o critério. | ADR-0024 §18–§20 |
| RNF-VER-008 | NÃO DEVE ser adotada meta percentual de cobertura como critério de aprovação, e teste intermitente DEVE ser corrigido ou removido, nunca silenciado. | E | ARQ | Inspeção da configuração e da lista de testes ignorados. | ADR-0024 §21, §22 |
| RNF-VER-009 | O teste de invariância de contagem de consultas DEVE integrar o comando de verificação; NÃO DEVE existir nele teste que reprove por limiar de tempo de resposta. | E | ARQ | Inspeção da composição do comando de verificação. | ADR-0024 §23, §24 |
| RNF-VER-010 | As metas de tempo de resposta DEVEM ser aferidas por teste de carga executado deliberadamente, contra base com massa representativa e reproduzível. | I | STK | Execução do teste de carga com relatório por percentil. | ADR-0024 §25, §26 |
| RNF-VER-011 | Os testes ponta a ponta DEVEM cobrir a autenticação e o caminho principal de cada capacidade, e NÃO DEVEM cobrir variações de regra de negócio. | I | STK | Inspeção do escopo dos cenários. | ADR-0024 §8 |
| RNF-VER-012 | Os arquivos de teste DEVEM residir junto do código que exercitam, e os dados de teste DEVEM ser produzidos por construtores parametrizáveis. | I | ARQ | Inspeção da localização dos arquivos e da origem dos dados. | ADR-0024 §16, §17 |

---

## 7. Restrições de projeto

Impostas pelas partes interessadas ou pelo ambiente; não derivadas de análise e não sujeitas a
negociação técnica nesta versão.

| ID | Restrição | Origem | Rastreio |
| :--- | :--- | :--: | :--- |
| RES-001 | O backend DEVE ser implementado em NestJS sobre Node.js, com TypeScript em modo estrito. | STK | ADR-0002 §1, §2 |
| RES-002 | O backend DEVE ser um monolito modular, com repositório, artefato de build e unidade de deploy únicos. | STK | ADR-0001 §1; ADR-0008 §1 |
| RES-003 | O frontend DEVE residir em repositório separado do backend. | STK | ADR-0016 §2 |
| RES-004 | A persistência DEVE utilizar uma única instância de PostgreSQL, compartilhada por todos os módulos. | STK | ADR-0018; ADR-0019 |
| RES-005 | O enfileiramento DEVE utilizar uma única instância de Redis, compartilhada por todos os módulos. | STK | ADR-0020; ADR-0021 |
| RES-006 | NÃO DEVE ser adotada arquitetura de microsserviços no estágio atual do projeto. | STK | ADR-0001 §2 |
| RES-007 | A camada HTTP DEVE ser o adapter Express do NestJS. | STK | ADR-0010 §1 |
| RES-008 | O acesso a dados DEVE utilizar Prisma ORM. | STK | ADR-0010 §2 |
| RES-009 | O frontend DEVE ser implementado em React com TypeScript em modo estrito. | STK | ADR-0016 §1 |
| RES-010 | O frontend DEVE ser uma aplicação de página única entregue como artefato estático, sem servidor de renderização. | STK | ADR-0016 §3 |
| RES-011 | O ferramental de build do frontend DEVE ser Vite. | STK | ADR-0016 §4 |
| RES-012 | Tailwind CSS DEVE ser a única solução de estilização do frontend; NÃO DEVE ser adotada biblioteca de componentes com sistema de estilo ou tokens próprios. | STK | ADR-0016 §11, §13 |
| RES-013 | O repositório DEVE ser hospedado no GitHub, com verificação automatizada executada a cada envio e em cada pull request. | STK | ADR-0023 §13, §14 |
| RES-014 | NÃO DEVE ser adotada automação de implantação no estágio atual. | STK | ADR-0023 §19 |
| RES-015 | A documentação de arquitetura e de requisitos DEVE residir em repositório próprio, distinto dos repositórios de código, e NÃO DEVE ser duplicada neles. | STK | ADR-0023 §13 |

---

## 8. Matriz de rastreabilidade — ADR para requisito

| ADR | Requisitos atendidos |
| :--- | :--- |
| ADR-0000 — Adoção de ADRs | RNF-EVO-003 |
| ADR-0001 — Monolito modular | RNF-MOD-001, RNF-MOD-007, RNF-EVO-001, RES-002, RES-006 |
| ADR-0002 — Stack NestJS + TypeScript | RES-001 |
| ADR-0003 — Fronteira e estrutura de módulo | RNF-MOD-001, RNF-MOD-006 |
| ADR-0004 — Fachada como superfície pública | RNF-MOD-002, RNF-MOD-003, RNF-EVO-001, RNF-EVO-004 |
| ADR-0005 — Comunicação entre módulos | RNF-MOD-003, RNF-MOD-005, RNF-CON-002, RNF-CON-003, RNF-CON-005, RNF-OBS-001 |
| ADR-0006 — Propriedade de dados por módulo | RNF-EVO-002, RNF-CON-001, RNF-CON-004, RNF-CON-006 |
| ADR-0007 — Enforcement de fronteiras | RNF-MOD-004, RNF-MOD-005 |
| ADR-0008 — Escalabilidade por papel de processo | RNF-ESC-001, RNF-ESC-002, RNF-ESC-003, RNF-ESC-004, RNF-OBS-002, RNF-OBS-003 |
| ADR-0009 — DRY e shared kernel | RNF-MOD-007, RNF-MOD-008, RNF-OBS-001, RNF-SEG-001 |
| ADR-0010 — Camada HTTP e ORM | RNF-MOD-010, RES-007, RES-008 |
| ADR-0011 — Desempenho e prevenção de N+1 | RNF-ESC-005, RNF-ESC-006, RNF-ESC-007, RNF-ESC-008, RNF-ESC-009, RNF-ESC-010, RNF-ESC-011, RNF-ESC-012, RNF-ESC-013, RNF-OBS-004 |
| ADR-0012 — Retentativa e dead-letter queue | RNF-MOD-009, RNF-CON-002, RNF-CON-007, RNF-CON-008, RNF-CON-009, RNF-CON-010, RNF-CON-011, RNF-CON-012 |
| ADR-0013 — Autenticação por sessão opaca | RNF-EVO-005, RNF-SEG-001, RNF-SEG-002, RNF-SEG-003, RNF-SEG-004, RNF-SEG-005, RNF-SEG-006, RNF-SEG-016, RNF-SEG-017, RNF-SEG-018 |
| ADR-0014 — Autorização por RBAC e delegação | RNF-SEG-001, RNF-SEG-007, RNF-SEG-008, RNF-SEG-009, RNF-SEG-010, RNF-SEG-011, RNF-SEG-012, RNF-SEG-013, RNF-SEG-014, RNF-OBS-005 |
| ADR-0015 — Arquitetura do frontend | RNF-MOD-011, RNF-MOD-012, RNF-MOD-013, RNF-ESC-014, RNF-SEG-018, RNF-SEG-020 |
| ADR-0016 — Stack do frontend | RNF-MOD-014, RNF-ESC-015, RES-003, RES-009, RES-010, RES-011, RES-012 |
| ADR-0017 — Contrato de integração frontend–backend | RNF-EVO-006, RNF-EVO-007, RNF-SEG-019, RNF-SEG-020 |
| ADR-0018 — Organização física do banco de dados | RNF-CON-013, RNF-CON-014, RNF-CON-015, RNF-CON-016, RNF-EVO-008, RES-004 |
| ADR-0019 — Transações e gestão de conexões | RNF-CON-017, RNF-CON-018, RNF-ESC-016, RES-004 |
| ADR-0020 — Transporte de mensagens e isolamento de filas | RNF-MOD-009, RNF-MOD-015, RNF-MOD-016, RNF-SEG-021, RNF-SEG-022, RES-005 |
| ADR-0021 — Outbox transacional e relay de eventos | RNF-MOD-016, RNF-CON-019, RNF-CON-020, RNF-CON-021, RNF-CON-022, RNF-OBS-006, RES-005 |
| ADR-0022 — Observabilidade e registro de erros | RNF-OBS-007 a RNF-OBS-012, RNF-SEG-023, RNF-SEG-024 |
| ADR-0023 — Ambiente de desenvolvimento e verificação | RNF-MOD-018, RNF-VER-001, RNF-VER-002, RNF-VER-003, RES-013, RES-014 |
| ADR-0024 — Estratégia de testes | RNF-VER-004 a RNF-VER-012 |
| ADR-0025 — Formato de resposta da API | RNF-EVO-009 a RNF-EVO-012, RNF-ESC-017, RNF-SEG-024, RNF-SEG-025 |

---

## 9. Pendências

| Item | Seção afetada | Bloqueia |
| :--- | :--- | :--- |
| Consolidação dos requisitos funcionais a partir da elicitação | 3, 4, 5.2 | Visão geral, partes interessadas, catálogo de permissões |
| Catálogo de permissões | 5.3 | RNF-SEG-008 |
| Catálogo de códigos de resposta | 5.4 | RNF-EVO-010 |
| Decomposição do sistema em módulos, com capacidade de negócio e tabelas de cada um | 5.2, 6.1 | RNF-MOD-001, RNF-MOD-006, RNF-CON-001 |
| Infraestrutura de implantação: ambientes, segredos, coletor de log e servidor de métricas | 6.5 | RNF-OBS-007, RNF-OBS-012 |
| Carga de referência e capacidade | 6.3 | RNF-ESC-005, RNF-ESC-013 |
| Conformidade legal no tratamento de dados pessoais | 6.6 | RNF-SEG-015 |
| Massa de dados representativa para teste de carga | 6.7 | RNF-VER-010 |

---

## 10. Histórico de revisões

| Versão | Data | Alteração |
| :--- | :--- | :--- |
| 0.1 | 2026-08-11 | Versão inicial. Requisitos não funcionais e restrições decorrentes de ADR-0000 a ADR-0009. Requisitos funcionais pendentes. |
| 0.9 | 2026-08-12 | Topologia de repositórios declarada: `vince-back`, `vince-front` e `vince-docs` na organização `Biopark-G3S6`. Acrescentado RES-015. Decorrente da reescrita de ADR-0023 §13 e §14. |
| 0.8 | 2026-08-12 | Definido o formato único de resposta da API, aplicável a sucesso e falha. Criada a seção 5.4 com o catálogo de códigos de resposta. Acrescentados RNF-EVO-009 a 012, RNF-ESC-017 e RNF-SEG-025. Decorrente de ADR-0025. |
| 0.7 | 2026-08-12 | Definidas observabilidade, ambiente de desenvolvimento, verificação automatizada e estratégia de testes. Criada a seção 6.7 com RNF-VER-001 a 012. Acrescentados RNF-MOD-017 e 018, RNF-OBS-007 a 013, RNF-SEG-023 e 024, e RES-013 e 014. Decorrente de ADR-0022, ADR-0023 e ADR-0024, com reescrita de ADR-0003 §1 e acréscimos de ADR-0003 §14 e §15 e ADR-0008 §14. |
| 0.6 | 2026-08-11 | Definidos o transporte de mensagens, o isolamento de filas por módulo e o outbox transacional com relay dedicado. Acrescentados RNF-MOD-015 e 016, RNF-CON-019 a 022, RNF-OBS-006 e RNF-SEG-021 e 022. Decorrente de ADR-0020 e ADR-0021, com reescrita de ADR-0008 §3 e acréscimo de ADR-0008 §13. |
| 0.5 | 2026-08-11 | Definidas a organização física do banco de dados e a gestão de transações e conexões. Acrescentados RNF-CON-013 a 018, RNF-ESC-016 e RNF-EVO-008. Decorrente de ADR-0018 e ADR-0019. |
| 0.4 | 2026-08-11 | Definidos arquitetura, stack e contrato de integração do frontend. Acrescentados RNF-MOD-011 a 014, RNF-EVO-006 e 007, RNF-ESC-014 e 015, RNF-SEG-019 e 020, e RES-009 a RES-012. Decorrente de ADR-0015, ADR-0016 e ADR-0017. |
| 0.3 | 2026-08-11 | Autenticação revista de JWT para sessão opaca em servidor: reescritos RNF-EVO-005 e RNF-SEG-001 a RNF-SEG-006, acrescentados RNF-SEG-016 a RNF-SEG-018. Decorrente da reescrita do ADR-0013. |
| 0.2 | 2026-08-11 | Definidos RNF-ESC-005, RNF-CON-007 e RNF-SEG-002, antes em aberto. Acrescentados RNF-MOD-010, RNF-EVO-005, RNF-ESC-006 a 013, RNF-CON-008 a 012, RNF-OBS-004 e 005, RNF-SEG-003 a 015, RES-007 e RES-008, decorrentes de ADR-0010 a ADR-0014. Incluída a estrutura obrigatória do requisito funcional (5.1) com os campos `Permissões geradas` e `Escopo de titularidade`, e o catálogo de permissões (5.3). |
