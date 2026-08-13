# ADR-0023 — Ambiente de desenvolvimento e verificação automatizada

- **Status:** Aceito
- **Data:** 2026-08-12
- **Relacionados:** ADR-0000, ADR-0007, ADR-0011, ADR-0015, ADR-0017, ADR-0020, ADR-0024

## Contexto

Diversas regras de arquitetura determinam que código não conforme seja reprovado antes da
integração. Essa verificação precisa de pontos de execução reais para não ser mera declaração. A
automação de implantação, por outro lado, exige ambiente, segredos e estratégia de release que o
estágio atual não comporta.

## Decisão

### Ambiente de desenvolvimento

1. O ambiente de desenvolvimento DEVE ser provisionado por Docker Compose.
2. O Compose DEVE prover PostgreSQL e Redis, com versões fixadas explicitamente.
3. As versões dos serviços de apoio DEVEM corresponder às do ambiente produtivo.
4. O ambiente DEVE ser iniciado por um único comando, sem passo manual adicional.
5. DEVE existir carga de dados inicial reproduzível.
6. A aplicação DEVE executar na máquina do desenvolvedor; apenas os serviços de apoio provêm do Compose.
7. O Compose NÃO DEVE incluir coletor de log nem servidor de métricas nesta fase.

### Comando de verificação

8. DEVE existir um único comando de verificação que execute: verificação de tipos, análise estática, verificação de formatação, verificação de fronteiras entre módulos e testes.
9. O comando DEVE ser definido em ponto único e reutilizado por todos os seus pontos de execução, sem duplicação de definição.
10. Qualquer violação DEVE reprovar a verificação por completo; NÃO DEVE ser emitido apenas aviso.

### Pontos de execução

11. O gancho de pré-commit DEVE executar verificação de formatação e análise estática sobre os arquivos alterados.
12. O gancho de pré-push DEVE executar o comando de verificação completo.
13. O código e a documentação DEVEM ser hospedados no GitHub, na organização `Biopark-G3S6`, em três repositórios: `vince-back` para o backend, `vince-front` para o frontend e `vince-docs` para os registros de decisão arquitetural e a especificação de requisitos.
14. Cada repositório de código DEVE possuir workflow do GitHub Actions executando o comando de verificação a cada envio e em cada pull request.
15. O workflow DEVE prover PostgreSQL e Redis como serviços, nas mesmas versões declaradas no Compose.
16. A integração na ramificação principal DEVE ocorrer por pull request.
17. A ramificação principal DEVE ter proteção que exija a aprovação do workflow de verificação como condição de incorporação.
18. Alteração com verificação reprovada NÃO DEVE ser incorporada, ainda que o gancho local tenha sido contornado.

### Implantação

19. A automação de implantação, a estratégia de ambientes e a gestão de segredos ficam diferidas e DEVEM ser objeto de ADR próprio quando adotadas.
20. A ausência de automação de implantação NÃO DEVE ser fundamento para reduzir, adiar ou desativar qualquer verificação.

## Alternativas rejeitadas

| Alternativa | Motivo da rejeição |
| :--- | :--- |
| Verificação apenas por gancho local | Contornável por opção de linha de comando, sem qualquer barreira antes da incorporação. |
| Ausência de proteção de ramificação | O workflow sinalizaria a falha, mas a incorporação seguiria possível; a verificação passaria a ser informativa e ADR-0007 §7 perderia efeito. |
| Verificação completa no gancho de pré-commit | Cada commit aguardaria a suíte inteira, o que empurra a equipe a agrupar alterações ou a contornar o gancho por hábito. |
| Verificação apenas no gancho de pré-push | Erros de formatação e de tipo se acumulariam ao longo de vários commits e apareceriam juntos, dificultando atribuir a causa. |
| Verificações distribuídas em vários comandos | Torna possível executar apenas parte delas; deixa de existir ponto único de verificação. |
| Aplicação executando em container durante o desenvolvimento | Ambiente mais fiel a produção, ao custo de recarga mais lenta e de depuração por porta remota. |
| Serviços de apoio instalados diretamente na máquina | Produz divergência de versão entre desenvolvedores e em relação ao ambiente produtivo. |
| Automação de implantação desde o início | Exige ambiente, segredos e estratégia de release antes de existir aplicação a implantar. |

## Implicações

1. A proteção de ramificação é o que torna a verificação efetivamente não contornável; sem ela, as regras de reprovação dos demais ADRs não têm mecanismo de imposição.
2. O workflow depende de serviços em container, o que soma tempo a cada verificação remota.
3. A versão do runtime na máquina do desenvolvedor pode divergir da de produção, uma vez que a aplicação não executa em container.
4. A habilitação efetiva do repositório sob controle de versão permanece pendente, conforme ADR-0000 §16.
5. O comando de verificação executa testes de integração e, portanto, depende do ambiente do Compose ativo na máquina.
