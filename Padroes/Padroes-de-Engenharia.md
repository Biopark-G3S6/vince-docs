# Padrões de Engenharia

**Projeto:** VinceArt
**Versão:** 1.6
**Status:** Vigente
**Data:** 2026-08-27

---

## 1. Objetivo e escopo

Este documento consolida os **padrões de engenharia**, as **restrições tecnológicas** e os
**padrões de especificação** do VinceArt. É o critério de conformidade usado em revisão de código,
em verificação automatizada e na aceitação de um requisito como especificado.

Os itens aqui registrados NÃO são requisitos de usuário: não foram solicitados por cliente algum e
não decorrem de análise do domínio. Decorrem de decisões da própria equipe sobre como construir o
sistema e como documentá-lo. Os requisitos do usuário estão em `Requisitos/URS.md`.

Cada padrão declara **o que a equipe deve satisfazer**. A justificativa está no ADR referenciado na
coluna de rastreio; padrão sem ADR decorre de decisão de processo tomada em discussão.

---

## 2. Convenções

### 2.1 Termos normativos

| Termo | Significado |
| :--- | :--- |
| **DEVE** / **NÃO DEVE** | Obrigatório / proibido. Não conformidade reprova a entrega. |
| **PODE** | Permitido, sem obrigação. |

### 2.2 Identificação

`PAD-<CATEGORIA>-<NNN>`, com numeração sequencial e imutável dentro da categoria.

| Categoria | Significado |
| :--- | :--- |
| `MOD` | Modularidade e manutenibilidade |
| `EVO` | Evolutividade e capacidade de extração |
| `ESC` | Escalabilidade e desempenho |
| `CON` | Confiabilidade e integridade |
| `OBS` | Observabilidade |
| `SEG` | Segurança |
| `VER` | Verificação e qualidade |
| `REQ` | Especificação de requisitos |
| `NOM` | Nomeação e internacionalização |
| `TEC` | Restrição tecnológica imposta |

Os identificadores `PAD-<CAT>-<NNN>` e `PAD-TEC-<NNN>` sucedem, com o mesmo número, os antigos
`RNF-<CAT>-<NNN>` e `RES-<NNN>` da URS 0.9.

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
| `STK` | Imposição da equipe ou do responsável técnico. |
| `PRO` | Decisão de processo, sem ADR correspondente. |

---

## 3. Padrões

### 3.1 Modularidade e manutenibilidade

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-MOD-001 | O backend DEVE ser organizado em módulos delimitados por capacidade de negócio, e não por camada técnica. | E | ARQ | Inspeção da estrutura de diretórios contra a estrutura normativa. | ADR-0001 §1; ADR-0003 §1, §2 |
| PAD-MOD-002 | Cada módulo DEVE expor uma única superfície pública, sendo todo o restante de sua implementação inacessível aos demais módulos. | E | ARQ | Análise estática: nenhuma importação entre módulos fora de `contracts/`. | ADR-0004 §1, §4, §5 |
| PAD-MOD-003 | Um módulo NÃO DEVE depender de detalhe de implementação de outro módulo. | E | ARQ | Análise estática de importações; ausência de referência a classe concreta externa. | ADR-0004 §6; ADR-0005 §1, §5 |
| PAD-MOD-004 | A conformidade com as fronteiras entre módulos DEVE ser verificada automaticamente a cada integração, impedindo a incorporação de código não conforme. | E | ARQ | Pipeline de CI reprova build com violação de fronteira. | ADR-0007 §1, §6, §7 |
| PAD-MOD-005 | NÃO DEVEM existir dependências cíclicas entre módulos. | E | ARQ | Verificação automatizada de ciclos no CI. | ADR-0005 §6; ADR-0007 §10 |
| PAD-MOD-006 | A adição ou remoção de um módulo NÃO DEVE exigir alteração no código dos demais módulos. | E | ARQ | Remoção do módulo do composition root sem erro de compilação nos demais. | ADR-0003 §10, §11 |
| PAD-MOD-007 | O código DEVE observar os princípios SOLID, DRY e KISS, com precedência definida em caso de conflito. | E | STK | Critério explícito de revisão de código. | ADR-0001 §5; ADR-0009 |
| PAD-MOD-008 | Código de infraestrutura transversal compartilhado NÃO DEVE conter semântica de negócio. | I | ARQ | Inspeção do conteúdo de `shared/` em revisão. | ADR-0009 §4, §5, §7 |
| PAD-MOD-009 | Cada fila de processamento assíncrono DEVE ser de propriedade de um único módulo, e NÃO DEVE ser publicada ou consumida por módulo diverso do proprietário. | E | STK | Inspeção do registro de filas por módulo; análise estática. | ADR-0012 §7; ADR-0020 §5–§9 |
| PAD-MOD-010 | Nenhum módulo DEVE acessar model de dados pertencente a outro módulo, ainda que o cliente de persistência seja único no processo. | E | ARQ | Inspeção do cliente escopado; regra de análise estática. | ADR-0010 §4, §5, §6 |
| PAD-MOD-011 | O frontend DEVE ser organizado em features correspondentes aos módulos do backend, cada uma com superfície pública única, e NÃO DEVE ter diretórios de primeiro nível por camada técnica fora de `shared/`. | E | ARQ | Inspeção da estrutura; análise estática de importações entre features. | ADR-0015 §1–§5 |
| PAD-MOD-012 | As fronteiras entre features do frontend DEVEM ser verificadas automaticamente na integração contínua, com violação classificada como erro, e NÃO DEVEM existir dependências cíclicas entre features. | E | ARQ | Pipeline reprova build com violação de fronteira ou ciclo. | ADR-0015 §8, §9 |
| PAD-MOD-013 | Dado proveniente da API NÃO DEVE ser copiado para store de estado de cliente nem tratado como fonte da verdade no frontend. | E | ARQ | Inspeção dos stores; ausência de dado originado da API. | ADR-0015 §11–§13 |
| PAD-MOD-014 | Componente de biblioteca visual do frontend NÃO DEVE conter regra de negócio nem realizar chamada à API. | I | ARQ | Inspeção de `shared/ui/`. | ADR-0016 §21 |
| PAD-MOD-015 | Toda fila DEVE ser nomeada com o prefixo do módulo proprietário e toda chave criada no Redis DEVE ser prefixada pelo nome do módulo. | E | ARQ | Análise estática dos nomes de fila e de chave. | ADR-0020 §5, §6, §9 |
| PAD-MOD-016 | Um módulo NÃO DEVE enfileirar tarefa em fila de outro módulo, nem conhecer os módulos consumidores dos eventos que publica. | E | ARQ | Inspeção do registro de filas e do publicador. | ADR-0020 §13; ADR-0021 §18 |
| PAD-MOD-017 | Módulo de plataforma DEVE observar integralmente as mesmas regras estruturais dos módulos de negócio, e sua criação DEVE ser justificada pela existência de dados próprios que `shared/` não pode possuir. | E | ARQ | Inspeção da estrutura e da justificativa no ADR do módulo. | ADR-0003 §1, §14, §15 |
| PAD-MOD-018 | DEVE existir um único comando de verificação, definido em ponto único e reutilizado por gancho local e por execução remota, executando tipos, análise estática, formatação, fronteiras e testes. | E | ARQ | Comparação entre a definição local e a do workflow remoto. | ADR-0023 §8–§10 |

### 3.2 Evolutividade e capacidade de extração

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-EVO-001 | Qualquer módulo DEVE poder ser extraído para serviço independente sem alteração no código dos módulos consumidores. | E | STK | Substituição da implementação da fachada por cliente remoto, sem alteração em consumidores. | ADR-0001 §3; ADR-0004 §10 |
| PAD-EVO-002 | A extração de um módulo NÃO DEVE exigir migração de dados nem alteração de schema pertencente a outro módulo. | E | ARQ | Ausência de junções e de chaves estrangeiras entre módulos. | ADR-0006 §3, §4 |
| PAD-EVO-003 | Toda decisão arquitetural DEVE ser registrada de forma versionada, rastreável e imutável. | I | ARQ | Existência do ADR correspondente antes da implementação. | ADR-0000 |
| PAD-EVO-004 | Alteração incompatível em contrato público de módulo DEVE permitir convivência entre versões durante a migração dos consumidores. | I | ARQ | Revisão de contrato; presença das duas versões no período de transição. | ADR-0004 §11 |
| PAD-EVO-005 | Módulo extraído para serviço independente DEVE receber a identidade já autenticada pela borda e NÃO DEVE reautenticar credencial de usuário final. | I | ARQ | Inspeção do fluxo de autenticação do módulo extraído. | ADR-0013 §19 |
| PAD-EVO-006 | Os tipos do contrato de API usados pelo frontend DEVEM ser derivados da especificação publicada pelo backend, e divergência entre ambos DEVE reprovar o build do frontend. | E | ARQ | Regeneração dos tipos na integração contínua com comparação. | ADR-0017 §1–§5 |
| PAD-EVO-007 | O backend DEVE publicar especificação de API gerada a partir do próprio código, mantida como contrato e não como documentação. | E | ARQ | Comparação entre a especificação publicada e as rotas expostas. | ADR-0017 §1 |
| PAD-EVO-008 | A extração dos dados de um módulo DEVE ser possível pelo despejo integral de seu schema, sem seleção manual de tabelas. | E | ARQ | Despejo e restauração do schema de um módulo em instância distinta. | ADR-0018 §1, §2 |
| PAD-EVO-009 | Toda resposta JSON de negócio DEVE usar o envelope único com `data` e `status`, em `camelCase`, omitindo `pagination` e `errors` quando não aplicáveis em vez de enviá-los nulos. | E | STK | Inspeção das respostas de cada endpoint contra o envelope. | ADR-0025 §1–§6 |
| PAD-EVO-010 | `status.code` DEVE ser identificador estável e independente de idioma, e NÃO DEVE ter sua semântica alterada após publicado; o cliente DEVE decidir por ele, nunca pelo texto da mensagem. | E | ARQ | Inspeção do catálogo e do tratamento no cliente. | ADR-0025 §7, §8, §11 |
| PAD-EVO-011 | O código de status HTTP NÃO DEVE ser replicado no corpo, e o corpo NÃO DEVE contradizer o status HTTP. | E | ARQ | Verificação de falha retornada sob status de sucesso. | ADR-0025 §13, §14 |
| PAD-EVO-012 | Falha de validação DEVE incluir `errors` com um item por campo inválido, contendo identificação do campo e código; falha inesperada NÃO DEVE incluir `errors`. | E | ARQ | Submissão com múltiplos campos inválidos e provocação de falha inesperada. | ADR-0025 §16, §17, §19 |

### 3.3 Escalabilidade e desempenho

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-ESC-001 | O sistema DEVE permitir escalar de forma independente a capacidade de processamento de cada módulo, sem replicar a aplicação inteira e sem extrair o módulo para serviço próprio. | E | STK | Execução do artefato com papel e conjunto de módulos definidos por variável de ambiente. | ADR-0008 §2, §6, §11 |
| PAD-ESC-002 | Todo processo da aplicação DEVE ser stateless, admitindo replicação horizontal sem afinidade de sessão. | E | ARQ | Ausência de estado em memória entre requisições; teste com múltiplas réplicas. | ADR-0008 §9 |
| PAD-ESC-003 | Processamento intensivo de CPU ou de longa duração NÃO DEVE ser executado no ciclo de requisição HTTP. | E | ARQ | Inspeção dos casos de uso expostos por rota; medição de tempo de resposta. | ADR-0008 §12 |
| PAD-ESC-004 | Nenhum módulo DEVE presumir execução no mesmo processo que outro módulo. | E | ARQ | Ausência de comunicação por estado compartilhado em memória. | ADR-0008 §10 |
| PAD-ESC-005 | O tempo de resposta medido no servidor DEVE observar: leitura — p95 ≤ 300 ms e p99 ≤ 800 ms; escrita transacional — p95 ≤ 500 ms e p99 ≤ 1500 ms. | E | STK | Teste de carga sob a carga de referência, com medição por percentil. | ADR-0011 §1, §2 |
| PAD-ESC-006 | A disponibilidade mensal DEVE ser de, no mínimo, 99,5%. | I | ARQ | Monitoramento de disponibilidade em janela mensal. | ADR-0011 §4 |
| PAD-ESC-007 | A experiência de carregamento do frontend DEVE observar, no percentil 75: LCP ≤ 2,5 s, INP ≤ 200 ms e CLS ≤ 0,1. | I | STK | Medição de campo das métricas Core Web Vitals. | ADR-0011 §3 |
| PAD-ESC-008 | Toda listagem DEVE ser paginada, com limite máximo de 100 itens por página. | E | ARQ | Inspeção do contrato da API; requisição acima do limite. | ADR-0011 §6, §7 |
| PAD-ESC-009 | Toda chamada a dependência externa DEVE declarar timeout explícito. | E | ARQ | Inspeção de código; teste com dependência não responsiva. | ADR-0011 §8 |
| PAD-ESC-010 | O número de consultas ao banco por requisição DEVE ser constante em relação à quantidade de registros retornados. | E | STK | Teste de invariância: mesmo endpoint com um e com dez registros DEVE emitir a mesma contagem de consultas. | ADR-0011 §9, §10, §12 |
| PAD-ESC-011 | Divergência no teste de invariância de contagem de consultas DEVE reprovar o build. | E | ARQ | Execução do teste no pipeline de CI. | ADR-0011 §11 |
| PAD-ESC-012 | Toda coluna utilizada como filtro ou ordenação de consulta recorrente DEVE possuir índice. | I | ARQ | Revisão de migração; análise de plano de execução. | ADR-0011 §16 |
| PAD-ESC-013 | A carga de referência sob a qual as metas de desempenho são aferidas DEVE ser definida. | I | — | *A definir.* | ADR-0011 §17; *pendente* |
| PAD-ESC-014 | O código do frontend DEVE ser dividido por rota, e conteúdo carregado de forma assíncrona DEVE ter espaço reservado com dimensão equivalente à do conteúdo final. | I | ARQ | Inspeção dos pacotes gerados por rota; medição de CLS. | ADR-0015 §16, §17 |
| PAD-ESC-015 | NÃO DEVE ser adotada no frontend solução de estilo com custo em tempo de execução. | I | ARQ | Inspeção das dependências de estilização. | ADR-0016 §20 |
| PAD-ESC-016 | O tamanho do pool de conexões por processo DEVE ser declarado, e o produto entre réplicas e pool DEVE caber em orçamento de conexões inferior ao limite do servidor, com reserva para migração e manutenção. | E | ARQ | Cálculo do orçamento contra a configuração de réplicas; medição das conexões em uso. | ADR-0019 §9–§13 |
| PAD-ESC-017 | A indicação de existência de próxima página DEVE ser obtida pela busca de um registro além do tamanho da página, sem consulta de contagem; totais DEVEM ser retornados apenas quando solicitados explicitamente. | E | ARQ | Inspeção das consultas emitidas em listagem com e sem solicitação de totais. | ADR-0025 §22–§24 |

### 3.4 Confiabilidade e integridade

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-CON-001 | Todo dado persistido DEVE ter exatamente um módulo proprietário, responsável por sua escrita. | E | ARQ | Mapa de propriedade de tabelas por módulo; análise estática de acesso. | ADR-0006 §1, §2 |
| PAD-CON-002 | O reprocessamento de uma mesma mensagem ou evento NÃO DEVE produzir efeito duplicado. | E | ARQ | Teste de entrega repetida com verificação de estado final. | ADR-0005 §10; ADR-0012 §16 |
| PAD-CON-003 | Falha no processamento assíncrono de um módulo NÃO DEVE reverter nem impedir a conclusão da operação do módulo publicador. | E | ARQ | Teste de falha injetada no consumidor. | ADR-0005 §12 |
| PAD-CON-004 | A integridade referencial entre dados de módulos distintos DEVE ser assegurada pela aplicação. | E | ARQ | Validação no módulo proprietário; teste de referência inexistente. | ADR-0006 §4, §5 |
| PAD-CON-005 | O sistema DEVE tolerar consistência eventual entre módulos, e a interface DEVE representar esse estado quando perceptível ao usuário. | I | ARQ | Revisão de fluxos assíncronos com reflexo em interface. | ADR-0005 §2; ADR-0006 §7 |
| PAD-CON-006 | Réplica local de dado pertencente a outro módulo NÃO DEVE ser tratada como fonte da verdade nem alterada por escrita própria. | E | ARQ | Inspeção das projeções; ausência de escrita fora do consumo de evento. | ADR-0006 §7, §8 |
| PAD-CON-007 | Toda fila DEVE aplicar número máximo de tentativas e backoff exponencial com jitter, sendo o padrão de 5 tentativas, atraso inicial de 5 s, fator 2 e teto de 5 min. | E | STK | Inspeção da configuração da fila; teste de falha sucessiva com medição dos intervalos. | ADR-0012 §1–§4 |
| PAD-CON-008 | Falhas DEVEM ser classificadas em transitórias e permanentes; falha permanente NÃO DEVE ser retentada e DEVE ser encaminhada imediatamente à dead-letter queue. | E | ARQ | Teste com payload inválido: ausência de retentativa e encaminhamento imediato. | ADR-0012 §5, §6 |
| PAD-CON-009 | Cada fila DEVE possuir dead-letter queue de propriedade do mesmo módulo, e NÃO DEVE existir consumidor automático de dead-letter queue. | E | STK | Inspeção da topologia de filas e dos consumidores registrados. | ADR-0012 §7, §9 |
| PAD-CON-010 | Mensagem irrecuperável NÃO DEVE ser descartada; DEVE ser retida por no mínimo 30 dias com payload original, histórico de tentativas, erro e identificador de correlação. | E | ARQ | Teste de esgotamento de tentativas com inspeção do conteúdo retido. | ADR-0012 §8, §12, §15 |
| PAD-CON-011 | O reprocessamento a partir da dead-letter queue DEVE ser ação explícita, sujeita a permissão e registrada em auditoria. | E | ARQ | Tentativa de reprocessamento sem permissão; verificação da trilha de auditoria. | ADR-0012 §10, §11 |
| PAD-CON-012 | O ingresso de mensagem em dead-letter queue DEVE emitir alerta observável, e o crescimento sustentado de uma dead-letter queue DEVE ser tratado como incidente. | I | ARQ | Simulação de falha permanente com verificação do alerta emitido. | ADR-0012 §13, §14 |
| PAD-CON-013 | Cada módulo DEVE possuir schema próprio no banco de dados, com todas as suas tabelas nele residentes; NÃO DEVE existir schema compartilhado nem tabela de negócio em `public`. | E | ARQ | Inspeção da distribuição de tabelas por schema. | ADR-0018 §1–§4 |
| PAD-CON-014 | A chave primária de toda tabela DEVE ser um UUID versão 7 gerado pela aplicação. | E | ARQ | Inspeção do schema e da origem da geração do identificador. | ADR-0018 §9, §10 |
| PAD-CON-015 | Referência a registro do mesmo módulo DEVE declarar chave estrangeira; referência a registro de outro módulo DEVE ser coluna de identificador indexada, sem chave estrangeira. | E | ARQ | Inspeção das restrições e dos índices declarados. | ADR-0018 §12–§14 |
| PAD-CON-016 | Colunas de data e hora DEVEM usar tipo com fuso horário, e toda tabela DEVE registrar instante de criação e de última atualização. | E | ARQ | Inspeção dos tipos de coluna declarados. | ADR-0018 §15, §17 |
| PAD-CON-017 | Toda transação DEVE estar contida em um único caso de uso de um único módulo, com tempo limite declarado, sem abranger chamada à fachada de outro módulo nem chamada de rede. | E | ARQ | Inspeção do escopo transacional; teste com dependência externa não responsiva. | ADR-0019 §1–§5 |
| PAD-CON-018 | A gravação do evento em outbox DEVE ocorrer na mesma transação do fato que o originou, e a consistência entre módulos NÃO DEVE ser obtida por transação distribuída. | E | ARQ | Teste de falha após o commit do fato, com verificação da presença do evento. | ADR-0019 §7, §8 |
| PAD-CON-019 | Cada módulo DEVE possuir tabela de outbox em seu próprio schema, e o evento NÃO DEVE ser publicado no barramento dentro da transação que o originou. | E | ARQ | Inspeção do schema e do ponto de publicação. | ADR-0021 §1–§3 |
| PAD-CON-020 | A entrega de eventos é garantida como pelo menos uma vez; a publicação DEVE preservar a ordem de criação dentro de cada módulo e a linha DEVE ser marcada apenas após confirmação. | E | ARQ | Teste de falha entre publicação e marcação, com verificação de republicação. | ADR-0021 §8–§11 |
| PAD-CON-021 | A falha de entrega a um consumidor NÃO DEVE impedir a entrega aos demais; cada fila de consumidor DEVE possuir retentativa e dead-letter queue próprias. | E | ARQ | Falha injetada em um consumidor com verificação dos demais. | ADR-0021 §14, §16, §17 |
| PAD-CON-022 | Linhas de outbox publicadas DEVEM ser marcadas e expurgadas após 7 dias; linha não publicada NÃO DEVE ser expurgada. | I | ARQ | Execução da rotina de expurgo com verificação das linhas remanescentes. | ADR-0021 §19–§21 |

### 3.5 Observabilidade

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-OBS-001 | Fluxo de negócio que atravesse módulos DEVE ser rastreável de ponta a ponta por identificador de correlação. | I | ARQ | Rastreio de uma operação completa nos registros de log. | ADR-0005 (implicações); ADR-0009 §4 |
| PAD-OBS-002 | Cada processo DEVE identificar, em seus registros, o papel de execução e os módulos ativos. | I | ARQ | Inspeção dos registros de log de processos `api` e `worker`. | ADR-0008 (implicações) |
| PAD-OBS-003 | Cada processo DEVE expor endpoint de verificação de saúde. | I | ARQ | Requisição ao endpoint em ambos os papéis. | ADR-0008 §5 |
| PAD-OBS-004 | Consulta ao banco com duração superior a 200 ms DEVE ser registrada em log em ambiente de desenvolvimento, e estatísticas de consulta DEVEM estar habilitadas em produção. | I | ARQ | Inspeção do log em desenvolvimento; verificação de `pg_stat_statements` em produção. | ADR-0011 §14, §15 |
| PAD-OBS-005 | Toda negativa de autorização DEVE ser registrada em log. | I | ARQ | Requisição sem permissão com verificação do registro. | ADR-0014 §14 |
| PAD-OBS-006 | O atraso entre a gravação e a publicação de um evento DEVE ser observável e sujeito a alerta, e o crescimento sustentado de eventos não publicados DEVE ser tratado como incidente. | I | ARQ | Interrupção do relay com verificação do alerta emitido. | ADR-0021 §13, §22 |
| PAD-OBS-007 | Todo processo DEVE emitir log estruturado na saída padrão como canal primário e síncrono, sem depender de banco de dados, fila ou serviço externo. | E | ARQ | Registro de falha com banco e fila indisponíveis. | ADR-0022 §1, §2 |
| PAD-OBS-008 | As falhas DEVEM ser classificadas em esperadas e inesperadas, registradas na mesma estrutura e distinguidas por classificação. | E | STK | Inspeção da estrutura e da classificação atribuída. | ADR-0022 §12, §16 |
| PAD-OBS-009 | O registro de erros DEVE ser agregado por assinatura derivada do tipo da exceção, do primeiro quadro do código do projeto e da mensagem normalizada, sem número de linha; NÃO DEVE ser persistida uma linha por ocorrência. | E | ARQ | Geração de ocorrências repetidas com verificação de uma única linha e do contador. | ADR-0022 §20–§25 |
| PAD-OBS-010 | Falha inesperada DEVE reter amostras de contexto em quantidade limitada; falha esperada NÃO DEVE reter contexto. As assinaturas DEVEM ser retidas indefinidamente e as amostras expurgadas em 30 dias. | E | ARQ | Execução da rotina de expurgo com verificação do que permanece. | ADR-0022 §26–§29 |
| PAD-OBS-011 | A falha na publicação ou na persistência de um erro NÃO DEVE propagar-se à requisição de origem. | E | ARQ | Indisponibilidade do consumidor de erros durante requisição bem-sucedida. | ADR-0022 §19 |
| PAD-OBS-012 | Cada processo DEVE expor métricas em formato Prometheus, em porta distinta da API e não publicada externamente, incluindo latência por rota, profundidade de filas, atraso do outbox, ingresso em dead-letter queue e conexões em uso. | I | ARQ | Requisição ao endpoint pela rede interna e tentativa pela externa. | ADR-0022 §31–§33 |
| PAD-OBS-013 | A verificação de saúde DEVE distinguir vivacidade de prontidão; a vivacidade NÃO DEVE consultar dependência externa e a prontidão NÃO DEVE reprovar por indisponibilidade transitória. | E | ARQ | Indisponibilidade breve de dependência com verificação de que as réplicas permanecem em rotação. | ADR-0008 §14 |

### 3.6 Segurança

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-SEG-001 | Autenticação e autorização DEVEM ser tratadas de forma transversal, fora da regra de negócio dos módulos, e nenhum módulo DEVE implementar mecanismo próprio. | E | ARQ | Inspeção da localização do mecanismo; ausência de implementação em módulos. | ADR-0009 §4; ADR-0013 §17, §18; ADR-0014 §22, §23 |
| PAD-SEG-002 | A autenticação DEVE ser baseada em sessão opaca mantida no servidor, com identificador sem significado semântico e no mínimo 128 bits de entropia. | E | STK | Inspeção do identificador emitido; ausência de dado decodificável. | ADR-0013 §1–§5 |
| PAD-SEG-003 | A sessão DEVE expirar por inatividade em 8 horas e por prazo absoluto em 7 dias; a janela de inatividade DEVE ser renovada a cada requisição autenticada e o prazo absoluto NÃO DEVE ser renovado. | E | ARQ | Teste de expiração por inatividade e por prazo absoluto. | ADR-0013 §6, §7 |
| PAD-SEG-004 | O encerramento de sessão DEVE ter efeito imediato, e DEVE ser possível revogar em uma operação todas as sessões ativas de um usuário. | E | ARQ | Requisição com credencial encerrada imediatamente após o encerramento. | ADR-0013 §10, §11 |
| PAD-SEG-005 | A credencial de sessão DEVE ser transportada em cookie `HttpOnly`, `Secure`, `SameSite` e com `Path` restrito, e NÃO DEVE trafegar em URL, corpo de requisição, cabeçalho customizado ou armazenamento acessível a script. | E | ARQ | Inspeção dos atributos do cookie e do armazenamento no cliente. | ADR-0013 §8, §9 |
| PAD-SEG-006 | Toda requisição que altere estado DEVE ser protegida contra falsificação de requisição entre sítios. | E | ARQ | Requisição forjada a partir de origem distinta. | ADR-0013 §13, §14 |
| PAD-SEG-007 | A autorização DEVE ser baseada em papéis, com permissões no formato `RECURSO:ACAO` e sem curinga. | E | STK | Inspeção do catálogo de permissões e do mecanismo de verificação. | ADR-0014 §1–§5 |
| PAD-SEG-008 | Todo requisito funcional DEVE declarar as permissões que origina, e NÃO DEVE existir permissão sem requisito funcional de origem. | E | STK | Revisão da seção 5 desta URS contra o catálogo em 5.3. | ADR-0014 §6–§8 |
| PAD-SEG-009 | As permissões efetivas DEVEM ser resolvidas no servidor a cada requisição, com cache invalidado imediatamente a cada alteração de papel, concessão ou revogação. | E | ARQ | Teste de revogação com verificação de efeito na requisição seguinte. | ADR-0014 §9, §10 |
| PAD-SEG-010 | A verificação de permissão DEVE ocorrer na borda, e a titularidade do registro DEVE ser verificada dentro do caso de uso; regras de titularidade NÃO DEVEM ser modeladas como permissões. | E | ARQ | Teste com usuário autorizado operando sobre registro de terceiro. | ADR-0014 §11–§13 |
| PAD-SEG-011 | A concessão de permissão DEVE ser restrita às permissões efetivas do concedente e condicionada à posse da permissão de concessão; um usuário NÃO DEVE conceder permissão a si mesmo. | E | STK | Teste de concessão de permissão não possuída e de autoconcessão. | ADR-0014 §15, §16 |
| PAD-SEG-012 | A revogação de uma permissão de um usuário NÃO DEVE revogar as concessões por ele realizadas. | E | STK | Teste de revogação do concedente com verificação do beneficiário. | ADR-0014 §17 |
| PAD-SEG-013 | Toda concessão e toda revogação DEVEM ser registradas em trilha de auditoria imutável, com concedente, beneficiário, permissão e instante. | E | ARQ | Inspeção da trilha após concessão e revogação. | ADR-0014 §18 |
| PAD-SEG-014 | DEVE existir consulta das concessões diretas ativas de um usuário, com concedente e data; a concessão PODE ter prazo de validade e sua revogação DEVE ser possível a qualquer momento por usuário com permissão de revogação. | E | ARQ | Execução da consulta; teste de expiração e de revogação por terceiro autorizado. | ADR-0014 §19–§21 |
| PAD-SEG-015 | O tratamento de dados pessoais DEVE observar a legislação aplicável. | E | — | *A definir.* | *Pendente* |
| PAD-SEG-016 | O identificador de sessão DEVE ser regenerado na autenticação bem-sucedida e em qualquer elevação de privilégio. | E | ARQ | Comparação do identificador antes e depois da autenticação. | ADR-0013 §12 |
| PAD-SEG-017 | A indisponibilidade do repositório de sessões DEVE resultar em negativa de autenticação; NÃO DEVE existir modo degradado que aceite requisição sem verificação. | E | ARQ | Requisição com o repositório de sessões indisponível. | ADR-0013 §16 |
| PAD-SEG-018 | As permissões expostas ao cliente destinam-se exclusivamente à composição da interface e NÃO DEVEM ser consideradas em decisão de autorização. | E | ARQ | Requisição direta à API sem a permissão, com a ação oculta na interface. | ADR-0013 §20; ADR-0014 §11; ADR-0015 §19, §20 |
| PAD-SEG-019 | O backend DEVE restringir as origens aceitas a uma lista explícita e NÃO DEVE aceitar origem curinga; frontend e backend DEVEM ser servidos sob o mesmo domínio registrável. | E | ARQ | Requisição a partir de origem não listada. | ADR-0017 §9, §10 |
| PAD-SEG-020 | Rota protegida NÃO DEVE ser renderizada antes da resolução da identidade do usuário. | E | ARQ | Acesso direto a rota protegida sem sessão estabelecida. | ADR-0015 §18; ADR-0017 §16 |
| PAD-SEG-021 | O consumidor de uma mensagem NÃO DEVE executar com a autoridade do usuário que a originou; o identificador do ator destina-se exclusivamente a auditoria. | E | ARQ | Processamento de mensagem cujo ator perdeu a permissão original. | ADR-0020 §17 |
| PAD-SEG-022 | O payload de uma mensagem NÃO DEVE conter entidade de domínio, tipo gerado pelo ORM nem dado pessoal além do estritamente necessário ao processamento. | E | ARQ | Inspeção dos payloads publicados. | ADR-0020 §15, §16 |
| PAD-SEG-023 | Os campos registrados em log e em contexto de erro DEVEM ser definidos por lista de permissão declarada em ponto único; NÃO DEVE ser usada lista de bloqueio. | E | ARQ | Introdução de campo sensível não declarado, com verificação de sua ausência no registro. | ADR-0022 §4, §5 |
| PAD-SEG-024 | A resposta ao cliente NÃO DEVE conter mensagem de exceção, rastro de pilha ou identificação de componente interno, e DEVE conter o identificador de correlação. | E | ARQ | Provocação de falha inesperada com inspeção da resposta. | ADR-0022 §10, §15; ADR-0025 §30 |
| PAD-SEG-025 | O detalhamento de erro por campo NÃO DEVE conter o valor submetido pelo usuário. | E | ARQ | Submissão de campo inválido com dado pessoal e inspeção da resposta. | ADR-0025 §18 |

---

### 3.7 Verificação e qualidade

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-VER-001 | O ambiente de desenvolvimento DEVE ser provisionado por Docker Compose, com PostgreSQL e Redis em versões fixadas correspondentes às de produção, iniciado por um único comando e com carga inicial reproduzível. | E | STK | Provisionamento em máquina limpa a partir do repositório. | ADR-0023 §1–§5 |
| PAD-VER-002 | A integração na ramificação principal DEVE ocorrer por pull request, e a ramificação DEVE ter proteção que exija a aprovação do workflow de verificação como condição de incorporação. | E | ARQ | Tentativa de incorporação com verificação reprovada. | ADR-0023 §16–§18 |
| PAD-VER-003 | O gancho de pré-commit DEVE executar formatação e análise estática sobre os arquivos alterados; o gancho de pré-push DEVE executar o comando de verificação completo. | E | ARQ | Commit e push com violação deliberada. | ADR-0023 §11, §12 |
| PAD-VER-004 | A fronteira do teste unitário DEVE ser o caso de uso exercitado pela fachada, com o interno do módulo real; somente fachadas de outros módulos DEVEM ser substituídas. | E | STK | Inspeção dos testes; refatoração interna sem quebra de teste. | ADR-0024 §2–§5 |
| PAD-VER-005 | Repositórios e adaptadores DEVEM ser testados contra PostgreSQL e Redis reais; NÃO DEVE ser usado substituto em memória do banco de dados. | E | ARQ | Inspeção da configuração de teste. | ADR-0024 §9, §10 |
| PAD-VER-006 | O isolamento entre testes DEVE usar schema por processo com truncate entre testes; NÃO DEVE usar transação revertida. | E | ARQ | Execução paralela da suíte com verificação de ausência de interferência. | ADR-0024 §11–§13 |
| PAD-VER-007 | Toda regra de negócio, todo caso de uso e toda correção de defeito DEVEM possuir teste correspondente. | E | STK | Revisão de código contra o critério. | ADR-0024 §18–§20 |
| PAD-VER-008 | NÃO DEVE ser adotada meta percentual de cobertura como critério de aprovação, e teste intermitente DEVE ser corrigido ou removido, nunca silenciado. | E | ARQ | Inspeção da configuração e da lista de testes ignorados. | ADR-0024 §21, §22 |
| PAD-VER-009 | O teste de invariância de contagem de consultas DEVE integrar o comando de verificação; NÃO DEVE existir nele teste que reprove por limiar de tempo de resposta. | E | ARQ | Inspeção da composição do comando de verificação. | ADR-0024 §23, §24 |
| PAD-VER-010 | As metas de tempo de resposta DEVEM ser aferidas por teste de carga executado deliberadamente, contra base com massa representativa e reproduzível. | I | STK | Execução do teste de carga com relatório por percentil. | ADR-0024 §25, §26 |
| PAD-VER-011 | Os testes ponta a ponta DEVEM cobrir a autenticação e o caminho principal de cada capacidade, e NÃO DEVEM cobrir variações de regra de negócio. | I | STK | Inspeção do escopo dos cenários. | ADR-0024 §8 |
| PAD-VER-012 | Os arquivos de teste DEVEM residir junto do código que exercitam, e os dados de teste DEVEM ser produzidos por construtores parametrizáveis. | I | ARQ | Inspeção da localização dos arquivos e da origem dos dados. | ADR-0024 §16, §17 |

### 3.8 Especificação de requisitos

Regem como a equipe redige a URS. Não determinam o conteúdo dos requisitos, que é do cliente.

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-REQ-001 | Todo requisito registrado na URS DEVE ter origem em parte interessada e NÃO DEVE decorrer de decisão da equipe; decisão da equipe DEVE ser registrada neste documento ou em ADR. | E | PRO | Revisão da URS: todo item possui parte interessada identificada. | — |
| PAD-REQ-002 | Todo requisito DEVE ser identificado por `<TIPO>-<CATEGORIA>-<NNN>`, com numeração sequencial e imutável dentro da categoria; identificador publicado NÃO DEVE ser reatribuído. | E | PRO | Inspeção da URS contra o histórico de revisões. | — |
| PAD-REQ-003 | Todo requisito DEVE declarar prioridade `E`, `I` ou `D`, e a prioridade DEVE ser atribuída pela parte interessada, não pela equipe. | E | PRO | Revisão da URS contra o registro da elicitação. | — |
| PAD-REQ-004 | Todo requisito DEVE declarar origem `ELI`, `STK` ou `DER`; requisito `DER` DEVE indicar o item do qual deriva e NÃO DEVE ser considerado acordado antes de validação com a parte interessada. | E | PRO | Revisão da URS: todo `DER` possui item de origem e estado de validação. | — |
| PAD-REQ-005 | Todo requisito DEVE ser rastreável até a evidência que o originou; requisito sem evidência DEVE ser marcado `DER`. | E | PRO | Inspeção da matriz de rastreabilidade da URS. | — |
| PAD-REQ-006 | Todo requisito funcional DEVE conter os campos declarados em 3.8.1; requisito que omita campo obrigatório NÃO DEVE ser encaminhado à implementação. | E | PRO | Revisão do requisito contra a estrutura obrigatória. | — |
| PAD-REQ-007 | Toda permissão DEVE constar de catálogo consolidado no formato `RECURSO:ACAO`, recurso no singular, ambos em maiúsculas e sem curinga; NÃO DEVE existir permissão sem requisito funcional de origem. | E | ARQ | Revisão do catálogo contra os requisitos funcionais. | ADR-0014 §6–§8 |
| PAD-REQ-008 | Todo código retornado em `status.code` e em `errors[].code` DEVE constar de catálogo consolidado, em maiúsculas, sem acento e independente de idioma; NÃO DEVE existir código sem requisito ou regra de negócio que o origine. | E | ARQ | Revisão do catálogo contra os requisitos e as regras de negócio. | ADR-0025 §20 |

#### 3.8.1 Estrutura do requisito funcional

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
| Origem | Sim | `ELI`, `STK` ou `DER` |
| Critério de aceitação | Sim | Condição objetiva e verificável de conclusão |
| Rastreio | Sim | Evidência de elicitação que originou o requisito |

Os campos **Permissões geradas** e **Escopo de titularidade** decorrem de `PAD-SEG-008` e
`PAD-SEG-010`: a autorização por papel permite a ação, mas não a permite sobre um registro
específico — a distinção precisa estar declarada no requisito, não deduzida na implementação.

### 3.9 Nomeação e internacionalização

Regem o idioma dos identificadores de software e a origem de todo texto exibido ao usuário.

| ID | Padrão | Prior. | Origem | Verificação | Rastreio |
| :--- | :--- | :--: | :--: | :--- | :--- |
| PAD-NOM-001 | Todo identificador de software DEVE ser em inglês: arquivo de código, diretório, tipo, função, variável, tabela, coluna, índice, migração, rota, papel, permissão, código de resposta, nome de fila e chave de cache. | E | ARQ | Análise estática dos identificadores; revisão de código. | ADR-0026 §5 |
| PAD-NOM-002 | Identificador de software NÃO DEVE conter texto destinado à exibição; a documentação do repositório e os identificadores `ADR-*`, `PAD-*` e `RF-*` PERMANECEM em português. | E | ARQ | Revisão de código e de documento. | ADR-0026 §6, §7 |
| PAD-NOM-003 | NÃO DEVE existir literal de texto destinado à exibição no código; todo texto exibido DEVE provir de catálogo de tradução organizado por idioma e por namespace da feature. | E | ARQ | Análise estática: ausência de literal exibível fora do catálogo. | ADR-0026 §8, §9 |
| PAD-NOM-004 | A chave de tradução DEVE ser estável e independente do texto que representa; revisão de redação NÃO DEVE alterar a chave. | E | ARQ | Inspeção do catálogo contra o histórico de alterações. | ADR-0026 §10 |
| PAD-NOM-005 | Chave ausente no idioma selecionado DEVE recair no idioma padrão; chave órfã e chave ausente DEVEM ser detectadas pelo comando único de verificação. | E | ARQ | Execução da verificação com chave removida e com chave órfã introduzida. | ADR-0026 §11, §12; ADR-0023 §8 |
| PAD-NOM-006 | A API NÃO DEVE retornar texto destinado à exibição; a tradução DEVE ocorrer no cliente, a partir de `status.code` e de `errors[].code`. | E | ARQ | Inspeção das respostas; ausência de texto exibível. | ADR-0026 §13–§15; ADR-0025 §7, §10–§12 |
| PAD-NOM-007 | Os valores a interpolar em mensagem traduzida DEVEM trafegar em `errors[].meta`, e NÃO DEVEM ser embutidos em texto pré-formatado pelo servidor. | E | ARQ | Inspeção das respostas de falha de validação. | ADR-0026 §16; ADR-0025 §17 |
| PAD-NOM-008 | Todo código do catálogo de códigos de resposta DEVE possuir chave correspondente no catálogo de tradução do idioma padrão. | E | ARQ | Comparação entre o catálogo da URS e o catálogo de tradução. | ADR-0026 §17; PAD-REQ-008 |
| PAD-NOM-009 | Mensagem emitida por canal externo à interface DEVE ser renderizada no backend a partir de catálogo próprio, no idioma da preferência do destinatário, e NÃO DEVE derivar o idioma do ator que originou a operação. | E | ARQ | Emissão de mensagem a destinatário com preferência distinta da do ator. | ADR-0026 §18–§20 |
| PAD-NOM-010 | Data, hora, número, moeda e ordenação de texto DEVEM usar as APIs nativas `Intl`; NÃO DEVE ser adotada biblioteca que embarque dados de localidade próprios. | E | ARQ | Inspeção das dependências e do código de formatação. | ADR-0026 §21, §22, §24; ADR-0016 §24 |
| PAD-NOM-011 | O instante DEVE trafegar em UTC no formato ISO 8601 e ser convertido para o fuso de exibição no cliente. | E | ARQ | Inspeção do contrato e da renderização. | ADR-0026 §23 |
| PAD-NOM-012 | A preferência de idioma DEVE ser persistida no perfil do usuário, e a troca de idioma NÃO DEVE exigir recarregamento da aplicação nem nova autenticação. | I | ARQ | Troca de idioma com verificação de continuidade da sessão. | ADR-0026 §25–§27 |
| PAD-NOM-013 | Os catálogos de tradução DEVEM ser carregados sob demanda por namespace, e NÃO DEVEM ser embarcados integralmente no artefato inicial. | I | ARQ | Inspeção do artefato de build. | ADR-0026 §29 |
| PAD-NOM-014 | O mecanismo de tradução DEVE residir em `shared/` do frontend; feature NÃO DEVE configurar instância própria. | E | ARQ | Análise estática de importações. | ADR-0026 §30; ADR-0015 §1–§5 |
| PAD-NOM-015 | O identificador de conceito do domínio DEVE seguir o glossário de 3.9.1; termo ausente DEVE ser acrescentado ao glossário antes de ser usado em código. | E | ARQ | Revisão de código contra o glossário. | ADR-0026 §5 |

#### 3.9.1 Glossário de nomeação

`PAD-NOM-001` exige identificador em inglês, mas não diz **qual** inglês. Este glossário fixa a
correspondência. Como `PAD-REQ-002` torna imutável o identificador já publicado, a escolha registrada
aqui não é preferência de estilo: é compromisso.

| Português | Inglês | Motivo, quando a escolha não é óbvia |
| :--- | :--- | :--- |
| Instituição | `Institution` | — |
| Curso | `Course` | — |
| Turma | `Cohort` | `Class` é palavra reservada em TypeScript e produziria `ClassEntity`, `classId`, `SchoolClass`. `Section`, a tradução acadêmica natural, colide com **seção do artigo**, que o módulo de conformidade precisa nomear. |
| Matrícula | `Enrollment` | Entidade própria, nunca coluna no usuário: o escopo inicial admite uma matrícula ativa por aluno, mas a expansão para múltiplas turmas está prevista e o relatório semestral exige histórico multissemestral. |
| Convite | `Invitation` | — |
| Evento | `Event` | — |
| Etapa de entrega | `Milestone` | Distinta do **estado** do artigo: o artigo percorre os seus estados uma vez por etapa, em ciclo. |
| Equipe | `Team` | `Group` seria ambíguo diante do vocabulário de RBAC. `Team` ainda coincide com a palavra usada pela parte interessada na elicitação. |
| Artigo | `Article` | — |
| Publicação externa | `Publication` | Reservado à publicação em evento ou periódico externo. Submissão a evento interno do sistema NÃO É publicação. |
| Conta de usuário | `User` | A identidade que se autentica, distinta do papel que ela exerce e do vínculo que lhe dá escopo. O e-mail é seu identificador único global (URS §1.4.1), e quem atua em mais de uma instituição possui mais de uma conta. |
| Área de atuação ou pesquisa | `ExpertiseArea` | Registrada no perfil, é a área em que o professor atua ou pesquisa (RF-ACS-005 RN2). Um termo só para as duas metades: `ResearchArea` deixaria a atuação de fora, e `Field` já significa **campo** no detalhamento de erro (`ADR-0025` §17). |
| Acesso (a capacidade) | `Access` | Nome do módulo que reúne identidade e autorização. `Auth` seria ambíguo entre autenticação e autorização, e o módulo faz as duas; `Identity` deixaria de fora papel, permissão e concessão, que são a maior parte do que ele possui. |
| Papel | `Role` | — |
| Permissão | `Permission` | — |
| Concessão direta | `PermissionGrant` | Distinta de `Role`: são as duas origens das permissões efetivas. |
| Aluno | `Student` | — |
| Professor | `Professor` | O papel. |
| Orientador | `Advisor` | O **vínculo** com evento ou equipe, não o papel. Um `Professor` só é `Advisor` onde foi designado. |
| Coordenador | `Coordinator` | — |
| Administrador institucional | `InstitutionAdmin` | — |
| Administrador de sistema | `SystemAdmin` | — |
| Seção do artigo | `Section` | Introdução, metodologia, conclusão. É a colisão que impede `Section` de significar turma. |
| Template | `Template` | Semente do artigo, não contrato: define o documento inicial e não é verificado depois. Quem é verificada é a norma. |
| Norma de formatação | `FormattingStandard` | A ABNT e as que vierem. Distinta de `Template`: a norma é regra verificável, o template é conteúdo inicial. |
| Referência bibliográfica | `Reference` | Dado estruturado por campos, nunca texto livre. É o que permite gerar a lista e conferir as citações. |
| Citação | `Citation` | Vínculo entre um ponto do texto e uma `Reference`, não texto copiado. |
| Entrega da etapa | `Submission` | O que a equipe entrega em uma etapa. Imutável, e é a âncora de `Remark` e a unidade de comparação. |
| Ponto do histórico | `Revision` | Estado preservado do artigo entre entregas. Distinto de `Submission`: toda `Submission` é um ponto do histórico, o inverso não. |
| Apontamento | `Remark` | Item de correção com ciclo de vida próprio — `OPEN`, `ADDRESSED`, `RESOLVED`, `DISMISSED`. `Comment` seria ambíguo com a mensagem livre da discussão, que não exige atendimento. |
| Discussão | `Discussion` | Fio único e contínuo por artigo, entre a equipe e o seu orientador responsável. |
| Mensagem | `Message` | O que se publica na `Discussion`. Um único nível de resposta. |
| Notificação | `Notification` | Aviso endereçado a um usuário. Distinta de `Message`: não é conversa e não tem resposta. |
| Resumo de alterações | `AiSummary` | Nomeado pela origem, e não pelo conteúdo, porque é a única capacidade que submete o artigo a serviço externo e a única que o consentimento institucional desliga. |
| Verificação de conformidade | `ComplianceCheck` | Confronto do artigo com a `FormattingStandard`. |
| Verificação de similaridade | `SimilarityCheck` | Confronto do artigo com o acervo. `PlagiarismCheck` afirmaria o que a verificação não apura: plágio é conclusão do orientador, não saída do sistema. |
| Indício de autoria | `AuthorshipSignal` | Fato registrado sobre como o texto foi produzido. `AiDetection` nomearia um juízo que o sistema NÃO DEVE emitir. |
| Consentimento de uso de IA | `AiConsent` | Decisão da instituição, não do orientador nem da equipe. |
| Progresso da equipe | `Progress` | Visão apurada, não entidade: nada é registrado como progresso, ele é derivado do que as demais entidades já guardam. |
| Sinal de risco | `RiskSignal` | Condição detectada sobre a equipe. `Alert` colidiria com `Notification`, que é o aviso; o sinal é a condição, e um pode existir sem o outro. |
| Contribuição | `Contribution` | Participação apurada de um integrante na produção do artigo. Subsídio à nota, nunca a própria nota. |
| Relatório de produção | `Report` | Apuração consolidada por curso e período. Não guarda juízo nem projeção. |

---

## 4. Restrições tecnológicas

Escolhas de tecnologia e de topologia impostas à equipe. Não derivam de análise de requisito
e não são renegociáveis por decisão técnica isolada.

| ID | Restrição | Origem | Rastreio |
| :--- | :--- | :--: | :--- |
| PAD-TEC-001 | O backend DEVE ser implementado em NestJS sobre Node.js, com TypeScript em modo estrito. | STK | ADR-0002 §1, §2 |
| PAD-TEC-002 | O backend DEVE ser um monolito modular, com repositório, artefato de build e unidade de deploy únicos. | STK | ADR-0001 §1; ADR-0008 §1 |
| PAD-TEC-003 | O frontend DEVE residir em repositório separado do backend. | STK | ADR-0016 §2 |
| PAD-TEC-004 | A persistência DEVE utilizar uma única instância de PostgreSQL, compartilhada por todos os módulos. | STK | ADR-0018; ADR-0019 |
| PAD-TEC-005 | O enfileiramento DEVE utilizar uma única instância de Redis, compartilhada por todos os módulos. | STK | ADR-0020; ADR-0021 |
| PAD-TEC-006 | NÃO DEVE ser adotada arquitetura de microsserviços no estágio atual do projeto. | STK | ADR-0001 §2 |
| PAD-TEC-007 | A camada HTTP DEVE ser o adapter Express do NestJS. | STK | ADR-0010 §1 |
| PAD-TEC-008 | O acesso a dados DEVE utilizar Prisma ORM. | STK | ADR-0010 §2 |
| PAD-TEC-009 | O frontend DEVE ser implementado em React com TypeScript em modo estrito. | STK | ADR-0016 §1 |
| PAD-TEC-010 | O frontend DEVE ser uma aplicação de página única entregue como artefato estático, sem servidor de renderização. | STK | ADR-0016 §3 |
| PAD-TEC-011 | O ferramental de build do frontend DEVE ser Vite. | STK | ADR-0016 §4 |
| PAD-TEC-012 | Tailwind CSS DEVE ser a única solução de estilização do frontend; NÃO DEVE ser adotada biblioteca de componentes com sistema de estilo ou tokens próprios. | STK | ADR-0016 §11, §13 |
| PAD-TEC-013 | O repositório DEVE ser hospedado no GitHub, com verificação automatizada executada a cada envio e em cada pull request. | STK | ADR-0023 §13, §14 |
| PAD-TEC-014 | NÃO DEVE ser adotada automação de implantação no estágio atual. | STK | ADR-0023 §19 |
| PAD-TEC-015 | A documentação de arquitetura e de requisitos DEVE residir em repositório próprio, distinto dos repositórios de código, e NÃO DEVE ser duplicada neles. | STK | ADR-0023 §13 |
| PAD-TEC-016 | A solução de tradução do frontend DEVE ser `i18next` com `react-i18next`. | STK | ADR-0026 §28 |

---

## 5. Matriz de rastreabilidade — ADR para padrão

| ADR | Padrões decorrentes |
| :--- | :--- |
| ADR-0000 — Adoção de ADRs | PAD-EVO-003 |
| ADR-0001 — Monolito modular | PAD-MOD-001, PAD-MOD-007, PAD-EVO-001, PAD-TEC-002, PAD-TEC-006 |
| ADR-0002 — Stack NestJS + TypeScript | PAD-TEC-001 |
| ADR-0003 — Fronteira e estrutura de módulo | PAD-MOD-001, PAD-MOD-006 |
| ADR-0004 — Fachada como superfície pública | PAD-MOD-002, PAD-MOD-003, PAD-EVO-001, PAD-EVO-004 |
| ADR-0005 — Comunicação entre módulos | PAD-MOD-003, PAD-MOD-005, PAD-CON-002, PAD-CON-003, PAD-CON-005, PAD-OBS-001 |
| ADR-0006 — Propriedade de dados por módulo | PAD-EVO-002, PAD-CON-001, PAD-CON-004, PAD-CON-006 |
| ADR-0007 — Enforcement de fronteiras | PAD-MOD-004, PAD-MOD-005 |
| ADR-0008 — Escalabilidade por papel de processo | PAD-ESC-001, PAD-ESC-002, PAD-ESC-003, PAD-ESC-004, PAD-OBS-002, PAD-OBS-003 |
| ADR-0009 — DRY e shared kernel | PAD-MOD-007, PAD-MOD-008, PAD-OBS-001, PAD-SEG-001 |
| ADR-0010 — Camada HTTP e ORM | PAD-MOD-010, PAD-TEC-007, PAD-TEC-008 |
| ADR-0011 — Desempenho e prevenção de N+1 | PAD-ESC-005, PAD-ESC-006, PAD-ESC-007, PAD-ESC-008, PAD-ESC-009, PAD-ESC-010, PAD-ESC-011, PAD-ESC-012, PAD-ESC-013, PAD-OBS-004 |
| ADR-0012 — Retentativa e dead-letter queue | PAD-MOD-009, PAD-CON-002, PAD-CON-007, PAD-CON-008, PAD-CON-009, PAD-CON-010, PAD-CON-011, PAD-CON-012 |
| ADR-0013 — Autenticação por sessão opaca | PAD-EVO-005, PAD-SEG-001, PAD-SEG-002, PAD-SEG-003, PAD-SEG-004, PAD-SEG-005, PAD-SEG-006, PAD-SEG-016, PAD-SEG-017, PAD-SEG-018 |
| ADR-0014 — Autorização por RBAC e delegação | PAD-SEG-001, PAD-SEG-007, PAD-SEG-008, PAD-SEG-009, PAD-SEG-010, PAD-SEG-011, PAD-SEG-012, PAD-SEG-013, PAD-SEG-014, PAD-OBS-005, PAD-REQ-007 |
| ADR-0015 — Arquitetura do frontend | PAD-MOD-011, PAD-MOD-012, PAD-MOD-013, PAD-ESC-014, PAD-SEG-018, PAD-SEG-020 |
| ADR-0016 — Stack do frontend | PAD-MOD-014, PAD-ESC-015, PAD-TEC-003, PAD-TEC-009, PAD-TEC-010, PAD-TEC-011, PAD-TEC-012 |
| ADR-0017 — Contrato de integração frontend–backend | PAD-EVO-006, PAD-EVO-007, PAD-SEG-019, PAD-SEG-020 |
| ADR-0018 — Organização física do banco de dados | PAD-CON-013, PAD-CON-014, PAD-CON-015, PAD-CON-016, PAD-EVO-008, PAD-TEC-004 |
| ADR-0019 — Transações e gestão de conexões | PAD-CON-017, PAD-CON-018, PAD-ESC-016, PAD-TEC-004 |
| ADR-0020 — Transporte de mensagens e isolamento de filas | PAD-MOD-009, PAD-MOD-015, PAD-MOD-016, PAD-SEG-021, PAD-SEG-022, PAD-TEC-005 |
| ADR-0021 — Outbox transacional e relay de eventos | PAD-MOD-016, PAD-CON-019, PAD-CON-020, PAD-CON-021, PAD-CON-022, PAD-OBS-006, PAD-TEC-005 |
| ADR-0022 — Observabilidade e registro de erros | PAD-OBS-007 a PAD-OBS-012, PAD-SEG-023, PAD-SEG-024 |
| ADR-0023 — Ambiente de desenvolvimento e verificação | PAD-MOD-018, PAD-VER-001, PAD-VER-002, PAD-VER-003, PAD-TEC-013, PAD-TEC-014 |
| ADR-0024 — Estratégia de testes | PAD-VER-004 a PAD-VER-012 |
| ADR-0025 — Formato de resposta da API | PAD-EVO-009 a PAD-EVO-012, PAD-ESC-017, PAD-SEG-024, PAD-SEG-025, PAD-REQ-008, PAD-NOM-006, PAD-NOM-007 |
| ADR-0026 — Estratégia de internacionalização | PAD-NOM-001 a PAD-NOM-015, PAD-TEC-016 |
| *(sem ADR — decisão de processo)* | PAD-REQ-001 a PAD-REQ-006 |

---

## 6. Pendências

| Item | Seção afetada | Bloqueia |
| :--- | :--- | :--- |
| Decomposição do sistema em módulos, com capacidade de negócio e tabelas de cada um | 3.1 | PAD-MOD-001, PAD-MOD-006, PAD-CON-001 |
| Infraestrutura de implantação: ambientes, segredos, coletor de log e servidor de métricas | 3.5 | PAD-OBS-007, PAD-OBS-012 |
| Carga de referência e capacidade | 3.3 | PAD-ESC-005, PAD-ESC-013 |
| Conformidade legal no tratamento de dados pessoais | 3.6 | PAD-SEG-015 |
| Massa de dados representativa para teste de carga | 3.7 | PAD-VER-010 |
| Catálogo de permissões — parcial | 3.8 | PAD-REQ-007 |
| Catálogo de códigos de resposta — parcial | 3.8 | PAD-REQ-008 |
| Catálogo de tradução do idioma padrão | 3.9 | PAD-NOM-003, PAD-NOM-008, PAD-NOM-009 |

A decomposição em módulos e os dois catálogos dependem da consolidação dos requisitos funcionais
em `Requisitos/URS.md`. Ambos os catálogos são derivados: são preenchidos pelo que os requisitos
declararem, nunca antes deles.

Os dois catálogos passam a existir em `Requisitos/URS.md` §8 e §9 a partir da URS 0.1, que registra
a fatia estrutural do sistema. Permanecem pendentes por não cobrirem ainda a fatia de correção —
submissão de versões, apontamentos, conformidade e relatórios —, que os ampliará. O catálogo de
tradução é derivado deles e do texto de interface, e nasce vazio enquanto não houver código.

---

## 7. Histórico de revisões

| Versão | Data | Alteração |
| :--- | :--- | :--- |
| 1.6 | 2026-08-27 | Glossário 3.9.1 estendido com `User` e `Access`, exigidos por `PAD-NOM-015` antes de a primeira vertical de autorização escrever código. Registrado o motivo de `Access` em vez de `Auth` ou `Identity` como nome do módulo decidido em `ADR-0027`. |
| 1.5 | 2026-08-26 | Glossário 3.9.1 estendido com os conceitos da fatia de acompanhamento registrada na URS 0.3. Registrada a distinção entre `RiskSignal`, que é a condição, e `Notification`, que é o aviso dela — um existe sem o outro. `Progress` fica anotado como visão apurada, e não entidade, para que não nasça tabela para o que é derivado. |
| 1.4 | 2026-08-25 | Glossário 3.9.1 estendido com os conceitos da fatia de produção e correção do artigo registrada na URS 0.2. `Section`, `Submission` e `Remark` deixam de ser reservados e passam a estar em uso; a tabela de reservados é suprimida por ter ficado vazia. Registradas as três escolhas de nomeação que carregam decisão de produto: `SimilarityCheck` em vez de `PlagiarismCheck`, `AuthorshipSignal` em vez de `AiDetection` e `Revision` distinta de `Submission`. |
| 1.3 | 2026-08-21 | Acrescentados `PAD-NOM-015` e a seção 3.9.1, com o glossário de nomeação: a correspondência português–inglês dos conceitos do domínio e o motivo de cada escolha não óbvia. Registrados também os termos reservados que já condicionaram escolhas em uso, em especial a colisão entre seção do artigo e turma. |
| 1.2 | 2026-08-19 | Acrescentada a categoria `NOM` e a seção 3.9, com os padrões de nomeação e internacionalização decorrentes de `ADR-0026`: idioma dos identificadores de software, origem do texto exibido, fronteira de tradução entre servidor e cliente, mensagens fora da interface, formatação por `Intl` e seleção de idioma. Acrescentada a restrição `PAD-TEC-016`. Atualizada a matriz de rastreabilidade e as pendências dos catálogos, agora parcialmente atendidas pela URS 0.1. |
| 1.1 | 2026-08-13 | Acrescentada a categoria `REQ` e a seção 3.8, com os padrões de especificação de requisitos que restavam na URS: convenção de identificação, escala de prioridade, códigos de origem, rastreabilidade até a evidência, estrutura obrigatória do requisito funcional e os catálogos de permissões e de códigos de resposta. Acrescentada a origem `PRO`, para padrão sem ADR. A URS foi zerada: nenhuma decisão da equipe permanece nela. |
| 1.0 | 2026-08-13 | Versão inicial. Extraída integralmente das seções 6, 7 e 8 da URS 0.9, sem alteração de conteúdo normativo. Identificadores `RNF-<CAT>-<NNN>` renomeados para `PAD-<CAT>-<NNN>` e `RES-<NNN>` para `PAD-TEC-<NNN>`, preservados os números. Motivo: os itens são padrões de engenharia decorrentes de ADR, não requisitos de usuário, e não cabem em uma URS. |
