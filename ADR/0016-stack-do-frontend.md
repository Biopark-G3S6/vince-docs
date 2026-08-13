# ADR-0016 — Stack do frontend

- **Status:** Aceito
- **Data:** 2026-08-11
- **Relacionados:** ADR-0002, ADR-0013, ADR-0015, ADR-0017

## Contexto

O frontend é um sistema integralmente autenticado, sem necessidade de indexação por mecanismos de
busca, com metas de experiência de carregamento definidas em ADR-0011 §3 e sessão transportada em
cookie conforme ADR-0013 §8.

## Decisão

### Base

1. O frontend DEVE ser implementado em React com TypeScript em modo estrito.
2. O frontend DEVE residir em repositório separado do backend.
3. O frontend DEVE ser uma aplicação de página única, entregue como artefato estático; NÃO DEVE existir servidor de renderização.
4. O ferramental de build DEVE ser Vite, adotando Rolldown como motor de bundling.
5. O gerenciador de pacotes DEVE ser pnpm.

### Dados, rotas e formulários

6. O estado de servidor DEVE ser gerido por TanStack Query.
7. O roteamento DEVE ser feito por TanStack Router.
8. Estado de cliente global, quando necessário, DEVE usar Zustand.
9. Formulários DEVEM usar React Hook Form.
10. A validação DEVE usar Zod, e o schema DEVE ser a fonte do tipo TypeScript correspondente.

### Estilo e componentes

11. Tailwind CSS DEVE ser a única solução de estilização do projeto.
12. Os componentes de base DEVEM ser primitivas sem estilo do Radix UI, adotadas pelo padrão shadcn/ui, com o código-fonte residente em `shared/ui/` do próprio repositório.
13. NÃO DEVE ser adotada biblioteca de componentes que traga sistema de estilo ou tokens próprios.
14. Necessidades não cobertas pelas primitivas DEVEM ser atendidas por bibliotecas sem estilo: tabela por TanStack Table, seleção de data por react-day-picker, envio de arquivo por react-dropzone, edição de texto rico por Tiptap, notificações por Sonner.
15. A composição condicional de classes DEVE usar `clsx` com `tailwind-merge`.
16. As variantes de um componente DEVEM ser declaradas com `class-variance-authority`; NÃO DEVEM ser expressas por concatenação de strings.
17. A ordenação das classes utilitárias DEVE ser automatizada por `prettier-plugin-tailwindcss`.
18. Os tokens de design — escala de espaçamento, paleta, tipografia e raios — DEVEM ser declarados uma única vez na configuração do Tailwind.
19. Valores arbitrários de estilo NÃO DEVEM ser usados quando houver token equivalente declarado.
20. NÃO DEVE ser adotada solução de estilo com custo em tempo de execução.
21. Componente residente em `shared/ui/` NÃO DEVE conter regra de negócio nem realizar chamada à API.

### Qualidade

22. Os testes DEVEM usar Vitest, Testing Library e Playwright.
23. A análise estática DEVE usar ESLint com `eslint-plugin-boundaries`, e a formatação DEVE usar Prettier.
24. Toda dependência nova DEVE ser avaliada quanto ao impacto no tamanho do artefato entregue.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Next.js ou outra solução com renderização no servidor | Introduz um segundo servidor entre navegador e API, obriga encaminhamento de cookie servidor a servidor e duplica a superfície de implantação; o ganho de indexação e de primeira carga é pouco aproveitável em sistema integralmente autenticado. |
| Vue | Curva de aprendizado menor, porém menor oferta de mão de obra e bibliotecas equivalentes às do ecossistema adotado em estágio menos maduro. |
| Angular | Arquitetura imposta pelo framework, próxima do NestJS, ao custo de curva mais íngreme, maior verbosidade e artefato maior, o que pressiona as metas de ADR-0011 §3. |
| Rsbuild, Parcel ou Bun como ferramental de build | Sem vantagem sobre Vite com Rolldown fora de cenários de migração de legado webpack. |
| Mantine | Decisão anteriormente adotada e revista. Conjunto amplo de componentes prontos, porém com sistema de estilo e tokens próprios, incompatível com Tailwind como única solução de estilização (§11, §13). |
| Material UI | Identidade visual marcante, sistema de tokens próprio e custo superior de tamanho e de tempo de execução. |
| Tailwind combinado a biblioteca de componentes com estilo próprio | Faz coexistirem dois conjuntos de tokens para os mesmos conceitos, com conflitos de especificidade e divergência visual progressiva. |
| Tailwind sem camada de componentes | Tailwind não fornece comportamento nem acessibilidade; obrigaria a implementar manualmente controle de foco, navegação por teclado, posicionamento e semântica assistiva. |
| Biome | Mais rápido e unificado, porém sem equivalente às regras de fronteira por camada de `eslint-plugin-boundaries`, das quais depende ADR-0015 §8. |
| React Router | Alternativa madura e mais difundida; preterida por não oferecer tipagem de rotas e parâmetros em tempo de compilação. |

## Implicações

1. Os componentes de base ficam sob propriedade do repositório: não são dependência versionada, e sua manutenção é responsabilidade da equipe.
2. Correções e melhorias publicadas na origem dos componentes NÃO chegam por atualização de dependência; sua incorporação é manual e deliberada.
3. A acessibilidade decorre das primitivas do Radix, não da estilização; substituir uma primitiva por marcação própria remove essa garantia.
4. A equipe assume decisões de design que uma biblioteca pronta traria decididas; §18 as concentra em um único ponto para limitar a dispersão.
5. Sem renderização no servidor, o atendimento a ADR-0011 §3 depende integralmente de divisão de código, cache e tamanho do artefato.
6. React e TypeScript comuns aos dois repositórios viabilizam a derivação de tipos do contrato prevista em ADR-0017.
