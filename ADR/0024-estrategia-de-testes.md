# ADR-0024 — Estratégia de testes

- **Status:** Aceito
- **Data:** 2026-08-12
- **Relacionados:** ADR-0001, ADR-0004, ADR-0011, ADR-0016, ADR-0019, ADR-0023

## Contexto

Vários requisitos não funcionais só se tornam verificáveis por teste automatizado. É necessário
definir os níveis de teste, a fronteira de cada um e onde executam — em especial a fronteira do
teste unitário, que determina se a suíte protege ou obstrui a refatoração.

## Decisão

### Níveis

1. Os testes DEVEM ser organizados nos seguintes níveis:

   | Nível | Abordagem | Escopo |
   | :--- | :--- | :--- |
   | Unitário | Caixa branca | Caso de uso, pela fachada do módulo |
   | Integração de módulo | Caixa branca | Repositórios e adaptadores contra serviços reais |
   | Contrato de API | Caixa preta | Endpoint exercitado por HTTP |
   | Ponta a ponta | Caixa preta | Jornada do usuário pela interface |
   | Carga | Caixa preta | Tempo de resposta sob concorrência |

2. A fronteira do teste unitário DEVE ser o caso de uso, exercitado pela fachada do módulo.
3. O interno do módulo — repositórios, serviços e entidades — DEVE ser real durante o teste.
4. Somente as fachadas de outros módulos DEVEM ser substituídas por implementação de teste.
5. NÃO DEVE ser escrito teste acoplado a estrutura interna cujo comportamento não seja observável pela fachada.
6. Regra de domínio sem dependência PODE ser testada isoladamente, sem banco de dados.
7. Teste de caixa preta DEVE exercitar o sistema exclusivamente por sua interface pública.
8. Teste ponta a ponta DEVE cobrir a autenticação e o caminho principal de cada capacidade, e NÃO DEVE cobrir variações de regra de negócio.

### Infraestrutura de teste

9. Repositórios e adaptadores DEVEM ser testados contra PostgreSQL e Redis reais.
10. NÃO DEVE ser usado substituto em memória do banco de dados.
11. Cada processo paralelo de teste DEVE operar em schema próprio.
12. As tabelas DEVEM ser truncadas entre testes.
13. NÃO DEVE ser usada transação revertida como mecanismo de isolamento, por conflitar com a abertura de transação pelo próprio caso de uso (ADR-0019 §1).
14. Cada teste DEVE declarar o estado de que depende e NÃO DEVE depender de estado deixado por outro teste.
15. Cada teste DEVE ser independente da ordem de execução.
16. Os dados de teste DEVEM ser produzidos por construtores parametrizáveis, e não por arquivos de dados fixos.
17. Os arquivos de teste DEVEM residir junto do código que exercitam.

### Obrigatoriedade

18. Toda regra de negócio DEVE possuir teste.
19. Todo caso de uso DEVE possuir teste do caminho de sucesso e dos caminhos de falha previstos.
20. Toda correção de defeito DEVE ser acompanhada de teste que reproduza o defeito corrigido.
21. NÃO DEVE ser adotada meta percentual de cobertura como critério de aprovação.
22. Teste intermitente DEVE ser corrigido ou removido; NÃO DEVE ser silenciado, ignorado ou submetido a nova execução automática.

### Desempenho

23. DEVE existir teste de invariância de contagem de consultas, conforme ADR-0011 §10, integrando o comando de verificação.
24. NÃO DEVE existir, no comando de verificação, teste que reprove por limiar de tempo de resposta.
25. As metas de tempo de resposta de ADR-0011 §1 DEVEM ser aferidas por teste de carga executado deliberadamente, em ambiente controlado.
26. Teste de carga DEVE executar contra base com massa de dados representativa e reproduzível.

### Execução

27. Testes unitários, de integração e de contrato DEVEM integrar o comando de verificação de ADR-0023 §8.
28. Testes ponta a ponta e de carga PODEM executar fora do comando de verificação, em razão de sua duração.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Teste unitário com fronteira na classe e dependências substituídas | Suíte mais rápida e diagnóstico mais preciso, porém acoplada à estrutura interna: extrair um método ou trocar uma dependência quebra dezenas de testes sem que comportamento algum tenha mudado, transformando a suíte em custo de refatoração. |
| Substituto em memória para o banco de dados | Não reproduz comportamento transacional, de índice nem de dialeto; produz confiança falsa exatamente na camada onde os defeitos de persistência residem. |
| Transação revertida por teste | Mecanismo usual de isolamento, inaplicável aqui porque o caso de uso abre a própria transação, produzindo aninhamento e commit efetivo. |
| Banco único com truncate, sem schema por processo | Configuração mínima, mas impede execução paralela: processos concorrentes truncariam as tabelas uns dos outros. |
| Container de banco por execução da suíte | Estado limpo garantido, ao custo de dezenas de segundos de inicialização em toda execução. |
| Teste de tempo de resposta com limiar no comando de verificação | A medição de tempo varia com a carga da máquina; o teste falharia de forma intermitente, ensinando a equipe a ignorar falha vermelha. |
| Meta percentual de cobertura | Mensura linha executada, não comportamento verificado; induz a produção de teste sem asserção útil para atingir o número. |
| Cobertura ampla por teste ponta a ponta | Lento e frágil: quebra a cada ajuste de layout, e a manutenção tende a ser abandonada quando o custo supera o benefício percebido. |
| Ausência de teste ponta a ponta | Deixaria sem verificação automática justamente a costura entre repositórios separados. |
| Árvore de testes paralela ao código | Separa o teste do módulo que ele exercita; na extração prevista em ADR-0001 §3, os testes não acompanham o módulo. |
| Arquivos de dados fixos | Quebram em conjunto a cada alteração de schema e obscurecem qual dado é relevante para cada teste. |

## Implicações

1. O teste unitário toca o banco de dados, o que torna a suíte mais lenta que a de uma abordagem com dependências substituídas. O ganho é que refatoração interna não quebra teste algum.
2. O comando de verificação passa a depender do ambiente do Compose ativo, tornando-o sensível ao estado da máquina.
3. O schema por processo exige rotina de preparação e limpeza, executada também no workflow remoto.
4. A ausência de meta de cobertura transfere para a revisão de código o julgamento sobre a suficiência dos testes.
5. Testes de carga executados fora da verificação dependem de execução deliberada e podem acumular regressões entre execuções.
6. O diagnóstico de falha aponta o caso de uso, não a linha exata: a precisão do diagnóstico foi trocada por resiliência à refatoração.
