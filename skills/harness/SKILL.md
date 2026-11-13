---
name: harness
description: Orquestra o ciclo #harness — caminho curto (developer e validação) ou completo (architect, tester, developer, reviewer, e designer se houver tela). Use quando a mensagem contiver #harness, ao retomar uma IU, ou ao seguir o estado em .cursor/memoria/estado.md. Não use se o projeto tiver .cursor/workflows/00-orquestrador-harness.md.
---

# Harness

`GUIA.md` é documentação para pessoas. Agentes não leem em runtime. Siga só o workflow da fase; não carregue os outros workflows nem o guia.

## Antes de delegar

1. Se existir `.cursor/workflows/00-orquestrador-harness.md` no projeto aberto, pare esta skill e siga o arquivo do projeto.
2. Se a raiz do workspace for `~/.cursor`, não crie requisito nem memória aqui. Diga para abrir o projeto do produto.
3. Sem `.cursor/context/projeto.md`, pergunte antes de criar o esqueleto. Não invente produto.
4. Leia `.cursor/memoria/estado.md` quando existir. É a memória da sessão, não o chat.

Resposta da etapa corrente continua sem `#harness`. Pedido novo sem a tag fica fora do ciclo. Cancelamento explícito grava `CANCELADO` e para.

## Caminho

Classifique antes de delegar. Na dúvida entre curto e completo, prove que falta contrato; senão escolha **curto**.

Declare em `estado.md`: curto ou completo.

- **Curto.** REQ e IU já cobrem a correção, sem regra nova e sem tela. Delegue só o developer ([03](workflows/03-implementar-tdd.md)). Depois do commit, pare para a pessoa testar. Reviewer só se a pessoa pedir ou se a IU não tiver comando de validação, e só depois desse teste.
- **Completo.** [00](workflows/00-orquestrador.md). Análise primeiro se houver dúvida. Com tela, [06](workflows/06-designer.md) antes do tester. Uma função por vez. A revisão visual e o reviewer entram só depois da última função, quando a pessoa mandar seguir.

Com `APROVADO` na IU, pare e peça conversa nova para a próxima unidade (ver `00-conversa`).

## Delegação

Passe ao subagente apenas: pedido em uma frase; caminhos de `estado.md`, REQ, IU, plano, handoff ou revisão; status; `função atual`; rodada; proibições. Sem resumo do chat, sem corpo de REQ, IU, handoff ou diff.

O subagente grava o artefato no `.cursor/` do projeto e devolve só o cartão em [templates/cartao-humano.md](templates/cartao-humano.md). Se `Preciso de você` for `nenhuma`, continue. Função commitada não é `nenhuma`: pare e mostre o cartão com o que abrir e o que experimentar. Pergunta aberta interrompe a delegação. Um papel não responde dúvida de outro.

## Portões

Pare e fale com a pessoa quando faltar regra de negócio, o risco da IU for ALTO sem aceite, o RED for inválido, a revisão chegar à terceira rodada, ou uma função tiver sido commitada. Até três perguntas. A próxima função espera a pessoa mandar seguir. Na última, esse seguir chama o reviewer e, se houver tela, o designer visual.

## Manutenção

Controle novo só depois de uma falha real, com o sim da pergunta de rule ou skill, e com essa falha escrita numa linha. Tire o controle quando ficar redundante. Mudou papel, status, caminho, gatilho ou pasta: atualize [GUIA.md](GUIA.md) na mesma edição.

Cada papel lê o próprio arquivo em [oficio](oficio) antes de agir.

Workflows: [00](workflows/00-orquestrador.md) [01](workflows/01-descobrir-requisitos.md) [02](workflows/02-testar-primeiro.md) [03](workflows/03-implementar-tdd.md) [04](workflows/04-revisar-entrega.md) [05](workflows/05-corrigir-revisao.md) [06](workflows/06-designer.md).
