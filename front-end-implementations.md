# Implementações para o frontend

Registro cronológico do que o backend entregou e do que o frontend precisa saber para consumir.
Cada vertical concluída acrescenta **uma entrada**, no topo. Entrada publicada não é reescrita: se
algo mudar, a mudança vira entrada nova, com a data em que passou a valer.

Este documento é **contrato de integração**, não recado. Existe porque a lista de códigos, cookies e
cabeçalhos que uma vertical introduz precisa sobreviver à conversa que a originou — e porque
`PAD-NOM-008` exige que todo código do catálogo de resposta tenha chave correspondente no catálogo de
tradução do cliente, o que é trabalho do outro repositório e não acontece por adivinhação.

## O que entra aqui

Tudo que o frontend não consegue descobrir sozinho lendo a especificação OpenAPI:

- os **códigos de resposta** que passaram a ser emitidos, e o que a interface deve fazer com cada um;
- **cookies, cabeçalhos e a configuração do cliente HTTP** que a vertical exige;
- o que ficou **declaradamente por fazer** no backend e produz efeito observável na interface;
- decisões do backend que **restringem** a interface — o que ela não pode assumir.

O que **não** entra: a forma de requisição e de resposta de cada endpoint. Isso vem da especificação
OpenAPI publicada, de que o cliente deriva os seus tipos (`ADR-0017` §2, §5). Repetir os campos aqui
criaria uma segunda fonte da verdade que envelheceria em silêncio.

## Onde está a especificação

Com o backend em execução:

| Recurso | Caminho |
| :--- | :--- |
| Especificação OpenAPI (JSON) | `/api/openapi.json` |
| Navegador da especificação | `/api/docs` |

Ela é **gerada do código** (`ADR-0017` §1): endpoint novo passa a constar sem que ninguém edite
documento algum.

---

## 2026-09-01 — Autenticação por sessão, envelope de resposta e guarda de borda

Mudança OpenSpec `add-session-authentication`. É a primeira vertical que publica rota: até ela, o
sistema não tinha endpoint algum. O que ela fixa em envelope, correlação e tratamento de erro passa
a valer para **todo** endpoint que o sistema vier a ter.

### 1. O envelope de resposta

Toda resposta JSON de negócio vem embrulhada (`ADR-0025`):

```json
{
  "data": { "...": "o recurso, ou null em falha" },
  "status": { "code": "SUCCESS", "severity": "success" },
  "errors": [{ "field": "newPassword", "code": "TOO_SHORT", "meta": { "minimum": 12 } }]
}
```

Regras que a interface pode assumir como invariantes:

- `data` e `status` estão **sempre** presentes em resposta com corpo.
- `errors` está **ausente** quando não há detalhamento por campo — nunca `null`, nunca `[]`.
- `pagination` **ainda não existe**: esta vertical não publica listagem alguma. Ele aparecerá quando
  a primeira listagem existir, e será acréscimo — não quebra o que já está escrito.
- Resposta `204` não tem corpo **e não tem envelope**.
- Os endpoints `/api/openapi.json` e `/api/docs` não usam o envelope.
- **O código HTTP não é replicado no corpo.** Não procure `status.httpCode`; não existe, e não vai
  existir (`ADR-0025` §13).
- **A decisão é sempre por `status.code`, nunca pelo texto** (`ADR-0017` §15).

### 2. A API não devolve texto para exibir

`ADR-0026` §13 e `PAD-NOM-006`: nenhuma resposta carrega texto redigido para o usuário final.
`status.message` é **texto de reserva** e vem omitido em toda esta vertical — a tradução é do
cliente, a partir de `status.code` e de `errors[].code`.

`status.message` continua existindo no contrato por um motivo só: quando o backend emitir um código
que o catálogo de tradução do frontend ainda não conhece, é ele que evita a tela em branco
(`ADR-0025` §12). **Não o remova do tratamento de erro.**

### 3. Códigos de resposta que passam a ser emitidos

Cada um precisa de chave no catálogo de tradução do idioma padrão (`PAD-NOM-008`).

| `status.code` | HTTP | O que a interface deve fazer |
| :--- | :--- | :--- |
| `SUCCESS` | 200 | Segue o fluxo. Não exibe mensagem; o resultado já é a confirmação. |
| `AUTHENTICATION_FAILED` | 401 | Encerra a sessão no cliente e leva à tela de autenticação (`ADR-0017` §16). Na tela de entrada, exibe erro genérico — **nunca** "e-mail não cadastrado" ou "senha incorreta": o servidor não distingue, e a interface não deve inventar a distinção. |
| `PERMISSION_DENIED` | 403 | **Não** encerra a sessão (`ADR-0017` §17). Exibe recusa e mantém o usuário onde está. Também é o código da recusa anti-CSRF — ver §6. |
| `VALIDATION_FAILED` | 400 | Exibe o erro **junto de cada campo** de `errors`. O valor submetido nunca volta na resposta; a interface já o tem. |
| `RESOURCE_NOT_FOUND` | 404 | Recurso inexistente. Também é o que responde uma rota que não existe. |
| `INVITATION_EXPIRED` | 422 | O meio de redefinição de senha não vale mais — expirado, já usado ou inexistente, sem distinção. Oferece pedir outro. |
| `LANGUAGE_NOT_SUPPORTED` | 422 | O idioma escolhido não está entre os suportados. Só `pt-BR` está, hoje. |
| `INTERNAL_ERROR` | 500 | Falha inesperada. A resposta é deliberadamente vazia de detalhe: sem mensagem de exceção, sem pilha, sem nome de componente. Exibe erro genérico e **registra o `X-Correlation-Id`** — é por ele que o backend encontra o que houve. |

### 4. Códigos de `errors[].code`

O detalhamento por campo tem vocabulário próprio, mais fino que o do `status.code`. Cada um também
precisa de chave de tradução:

| `code` | Significado | `meta` |
| :--- | :--- | :--- |
| `REQUIRED` | Campo obrigatório ausente ou vazio | — |
| `MALFORMED` | Tipo ou forma inválidos | — |
| `TOO_SHORT` | Abaixo do comprimento mínimo | `minimum` |
| `TOO_LONG` | Acima do comprimento máximo | `maximum` |
| `INCORRECT` | Bem formado, mas não confere — a senha atual, notadamente | — |
| `NOT_EDITABLE` | Campo não alterável pelo titular | — |

`meta` carrega os valores a interpolar na mensagem traduzida (`ADR-0026` §16), e **nunca** o valor
submetido pelo usuário (`ADR-0025` §18). Interpole no cliente: `"Mínimo de {{minimum}} caracteres"`.

### 5. Sessão: o navegador cuida, a interface não

A credencial é uma **sessão opaca em cookie** (`ADR-0013`). O que isso significa na prática:

- **A interface nunca lê, guarda ou envia a credencial.** O cookie de sessão é `HttpOnly`: script
  algum o alcança, e é assim de propósito.
- **Não há token, não há refresh, não há interceptador de renovação.** Nada disso existe do lado do
  cliente (`ADR-0013`, implicação 2).
- O cliente HTTP DEVE enviar credenciais em **todas** as requisições à API (`ADR-0017` §11):
  `credentials: 'include'` em `fetch`, `withCredentials: true` em Axios. Sem isso, nada funciona.
- O cookie tem `Path` restrito a `/api/v1` e `SameSite=Lax`.
- O cookie tem `Secure`. Em desenvolvimento isso **não** é problema: o navegador trata
  `http://localhost` como contexto seguro. Servir o frontend por IP de rede local, não.
- A origem do frontend precisa constar de `CORS_ORIGINS` no backend; curinga é proibido
  (`ADR-0017` §10).

Expiração: **8 horas de inatividade**, renovadas a cada requisição autenticada, e **7 dias de prazo
absoluto**, que não se renovam. Vencido qualquer um dos dois, a requisição seguinte responde `401` —
e o tratamento é o mesmo de qualquer `401`. A interface **não** precisa contar tempo.

### 6. Proteção anti-CSRF — o que a interface precisa fazer

É a única parte da autenticação que exige trabalho do cliente.

1. Ao autenticar, o backend emite um segundo cookie, **legível por script**, com o token anti-CSRF
   da sessão. O nome vem de `CSRF_COOKIE_NAME` (padrão `vince_csrf`).
2. Em **toda requisição que altere estado** — `POST`, `PUT`, `PATCH`, `DELETE` — a interface lê esse
   cookie e o devolve no cabeçalho **`X-CSRF-Token`**.
3. Requisição de leitura (`GET`) não precisa dele.
4. Faltando o token, ou vindo o token de outra sessão, a resposta é `403 PERMISSION_DENIED` e
   **nada é alterado**.

O token é reemitido a cada `GET /api/v1/identity`. É a via de recuperação quando o cookie se perde —
aba nova, cookie de sessão ainda válido.

> Isto pertence à camada `api/` do frontend (`ADR-0017` §6), uma vez só. Componente algum deve saber
> que o token existe.

### 7. Correlação

Toda resposta traz **`X-Correlation-Id`**, inclusive as sem corpo e as de falha. A interface DEVE
propagá-lo (`ADR-0017` §19): envie o mesmo cabeçalho na requisição e o backend o reaproveita.

O formato declarado é **UUID canônico**. Valor fora do formato é descartado em silêncio e outro é
gerado — não é erro, mas o rastro se perde. Registre o valor devolvido junto de qualquer erro que a
interface reportar: é por ele que se acha a requisição no log do servidor.

### 8. Identidade e composição da interface

`GET /api/v1/identity` devolve identificação, papéis e **permissões efetivas**. Consulte-o **uma vez
por carregamento da aplicação** (`ADR-0017` §18).

> **As permissões servem exclusivamente para compor a interface** (`ADR-0013` §20, RF-ACS-001 RN3).
> Esconder um botão não protege nada: o servidor verifica a permissão a cada requisição, e a mesma
> ação chamada diretamente responde `403`. A ausência de uma permissão nessa resposta **não deve ser
> o único obstáculo** à ação correspondente — mas também não precisa ser mais que isso: pode confiar
> que o servidor recusa.

As permissões refletem revogação **imediatamente**: revogado um papel, a consulta seguinte já não as
traz. Não há janela de cache a considerar.

`preferredLanguage` vem `null` quando o usuário nunca escolheu. Nesse caso, infira do navegador e
recaia em `pt-BR` (`ADR-0026` §26) — o backend **não** grava um padrão.

### 9. Rotas publicadas

Todas sob o prefixo `/api/v1`. A forma exata de cada corpo está na especificação OpenAPI.

| Método e caminho | Exige sessão | Sucesso | Falhas |
| :--- | :--- | :--- | :--- |
| `POST /sessions` | não | `200` com a identidade | `400`, `401` |
| `DELETE /sessions/current` | não | `204` | — |
| `GET /identity` | sim | `200` com a identidade | `401` |
| `GET /profile` | sim | `200` com o perfil | `401`, `404` |
| `PATCH /profile` | sim | `200` com o perfil | `400`, `401`, `403`, `404`, `422` |
| `PUT /password` | sim | `204` | `400`, `401` |
| `POST /password/recovery` | não | `204` | `400` |
| `POST /password/reset` | não | `204` | `400`, `422` |

Observações que a especificação não diz:

- **`POST /sessions` responde `200`, não `201`.** A sessão é opaca e não tem endereço; o que volta em
  `data` é a identidade.
- **`DELETE /sessions/current` é idempotente e não exige sessão válida** (RF-ACS-002 E1): encerrar
  com credencial já expirada conclui com `204`. Continua exigindo o token anti-CSRF quando a
  requisição porta cookie de sessão. Encerra **apenas a sessão corrente** — as demais sessões do
  mesmo usuário permanecem válidas.
- **`PATCH /profile` recusa a operação INTEIRA** com `403 PERMISSION_DENIED` se o corpo contiver
  `email`, `roleCode`, `institutionId` ou `active` (RF-ACS-005 E2). Nenhum campo é alterado — nem os
  alteráveis. Não envie esses campos "por conveniência" a partir do objeto que veio do `GET`.
- **`PUT /password` derruba as demais sessões** do usuário e preserva a corrente (RF-ACS-004 RN2). A
  sessão de onde a alteração partiu continua valendo; as outras abas do usuário, não.
- **`POST /password/reset` derruba TODAS as sessões**, inclusive a corrente, se houver.
- Senha fora da política **não queima** o meio de redefinição: a pessoa pode tentar de novo com o
  mesmo link.

### 10. Política de senha

Mínimo de **12** e máximo de **128** caracteres. **Sem** exigência de maiúscula, dígito ou símbolo —
regra de composição empurra o usuário para o padrão previsível sem aumentar a entropia real.

Os limites constam da especificação OpenAPI; derive a validação de cliente dela, não de constantes
escritas à mão. E lembre que validação de cliente é conveniência: quem recusa é o servidor.

**A decisão está pendente de confirmação com as partes interessadas.** Se a instituição tiver
política própria, ela prevalece e os números mudam.

### 11. Recuperação de acesso não revela quem tem conta

`POST /password/recovery` responde **exatamente igual** para e-mail cadastrado, não cadastrado e de
conta desativada — mesmo status, mesmo corpo, mesmo tempo (RF-ACS-003 RN2, E1).

A interface DEVE respeitar isso: exiba sempre "se houver conta com esse e-mail, enviamos as
instruções". **Nunca** exiba "e-mail não encontrado" nesta tela, e não tente inferir nada do tempo de
resposta.

---

## O que ainda NÃO funciona

Três lacunas declaradas. Nenhuma é esquecimento; todas têm efeito observável na interface.

### A. O e-mail de redefinição de senha não é enviado

`POST /password/recovery` cria o meio de redefinição corretamente — e ele **não chega ao
destinatário**. O envio depende de capacidade de correio eletrônico, que depende de outbox, fila e
catálogo de mensagens do backend; nada disso existe ainda.

**O que a interface deve fazer:** construir a tela normalmente. Ela está correta e vai funcionar sem
alteração quando a vertical de notificação existir. Não construa nenhuma via alternativa de entrega —
o valor do meio de redefinição **nunca** é devolvido em resposta HTTP, e não será.

**Consequência operacional:** entre esta vertical e a de notificação, ninguém recupera a senha
sozinho, e o `SYSTEM_ADMIN` da carga inicial não tem via de entrada.

### B. Não há limitação de taxa

**Questão em aberto** do `design.md` de `add-session-authentication`. Nenhum ADR a trata e nenhum
requisito a pede. Hoje, `POST /sessions` e `POST /password/recovery` aceitam tentativas sem limite.

**O que a interface deve fazer, hoje:**

- **Não repetir automaticamente** uma autenticação que falhou. Nada do lado do servidor a segura.
- Aplicar contenção própria após falhas consecutivas — atraso progressivo, botão desabilitado por
  alguns segundos. É paliativo, e não substitui a limitação no servidor.

**O que a interface deve estar preparada para receber, quando a limitação existir:** um código de
resposta novo, provavelmente sob HTTP `429`. É por isso que o tratamento genérico importa desde já:
**código não reconhecido deve recair em `status.message` e nunca quebrar a tela** (`ADR-0025` §12).
Se esse tratamento existir, a limitação de taxa entra em produção sem exigir mudança no frontend.

### C. A rotação do segredo do token anti-CSRF não está definida

**Questão em aberto** do `design.md`: a origem e a rotação da chave de assinatura. O token é a
assinatura do identificador de sessão — trocar o segredo **invalida o token de todas as sessões
vivas de uma vez**, e elas continuam autenticadas.

O efeito na interface é preciso: requisições de alteração passam a responder `403 PERMISSION_DENIED`
enquanto as de leitura seguem funcionando.

**O que a interface DEVE fazer:** ao receber `403` em requisição que altera estado, **reconsultar
`GET /api/v1/identity` uma vez** — ele reemite o cookie do token — e repetir a requisição. Se ela
falhar de novo com `403`, é recusa de autorização de verdade: exiba a recusa e **não** repita outra
vez.

Uma tentativa, e só uma. Repetir em laço transforma uma rotação de chave em enxurrada de requisições.

---

## Rastreio

| Assunto | Onde está a regra |
| :--- | :--- |
| Envelope, códigos, semântica HTTP, paginação | [`ADR-0025`](ADR/0025-formato-de-resposta-da-api.md) |
| Contrato de integração, CORS, CSRF, versionamento | [`ADR-0017`](ADR/0017-contrato-de-integracao-frontend-backend.md) |
| Sessão opaca, cookie, prazos, identidade | [`ADR-0013`](ADR/0013-autenticacao-por-sessao-opaca.md) |
| Permissões efetivas e verificação na borda | [`ADR-0014`](ADR/0014-autorizacao-rbac-e-delegacao.md) |
| Correlação e tratamento de erros | [`ADR-0022`](ADR/0022-observabilidade-e-registro-de-erros.md) |
| Tradução, chaves e catálogo | [`ADR-0026`](ADR/0026-estrategia-de-internacionalizacao.md) |
| Catálogo de códigos de resposta | [URS §2.4](Requisitos/URS.md) |
| Requisitos de acesso e identidade | [URS §2.1, grupo `ACS`](Requisitos/URS.md) |
