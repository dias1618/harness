# Workflow — Orquestrador

O agente do chat classifica, delega e só fala com a pessoa no portão. Não substitui os papéis.

`GUIA.md` é para pessoas. Não leia em runtime.

## 1. Projeto com orquestrador próprio

Se existir `.cursor/workflows/00-orquestrador-harness.md`, siga esse arquivo e pare este workflow.

## 2. Classificar

Prefira **curto** quando REQ e IU já fecharem o comportamento. Só vá ao completo com regra nova, IU nova, tela nova ou lacuna real de contrato.

| Situação | Caminho |
|----------|---------|
| Correção já coberta por REQ e IU, sem regra nova e sem tela | Curto: developer |
| Dúvida entre analisar e implementar | Análise: architect |
| Regra nova, IU nova ou comportamento sem contrato | Completo |
| IU citada | Retome pelo status abaixo |
| Mudança de escopo pedida pela pessoa | Reavalie requisito, plano e testes afetados |

Grave o caminho em `.cursor/memoria/estado.md` ([modelo](../templates/estado.md)).

## 3. Status da IU

| Status | Próximo |
|--------|---------|
| Ausente, rascunho ou `BLOQUEADO` | architect ([01](01-descobrir-requisitos.md)) |
| `PRONTO_PARA_TESTES` sem contrato visual, e a IU tem tela | designer ([06](06-designer.md)) |
| `PRONTO_PARA_TESTES` | tester ([02](02-testar-primeiro.md)) |
| `RED` | developer ([03](03-implementar-tdd.md)) |
| `AGUARDANDO_TESTE` | Pessoa. Não chame o próximo papel |
| `VALIDADO` | reviewer ([04](04-revisar-entrega.md)); com tela, designer visual em paralelo. Só a última função, depois que a pessoa escolher Seguir |
| `ALTERACOES_NECESSARIAS`, rodada 1 ou 2, defeito de implementação | developer ([05](05-corrigir-revisao.md)) |
| Expectativa de teste errada | tester ([02](02-testar-primeiro.md)). Se a spec mudou, a aprovação cai junto |
| Regra ambígua, critério incompleto ou violação nascida do plano | architect ([01](01-descobrir-requisitos.md)), com nova aprovação |
| Rodada 3, spec a mudar, ou infra que impede a verificação | Pare. `BLOQUEADO`. A tarefa não fica verificada |
| `CANCELADO` | Ninguém |

## 3.1 Aprovação

A aprovação vale para a revisão gravada de REQ, IU e plano de testes, na seção Revisão aceita de `estado.md`. Se um desses mudar, o status que dependia dele volta ao dono: requisito ou plano ao architect, testes ao tester.

Correção pequena regrava `estado.md` e o relatório da etapa que rodou. Persistência, integração ou mudança de arquitetura regrava requisito, unidade, testes afetados e a decisão.

## 4. Delegar

Uma fase por vez, com contexto mínimo:

- Pedido em uma frase.
- Caminho de `.cursor/memoria/estado.md` e `função atual`.
- Caminhos de REQ, IU, ADR, contrato visual, plano, handoff ou revisão.
- Status e rodada.
- Proibições: developer não edita teste do tester; architect, designer e reviewer não editam código de produção; reviewer e designer visual não recebem o resumo do developer como evidência.

Não cole o corpo dos documentos nem recapitule o chat. Mantenha **Processos do ciclo** em `estado.md` alinhado ao que o agente deixou rodando (ou `Nenhum`). Espere o cartão. `Preciso de você: nenhuma` segue e não abre formulário. Função entregue não é `nenhuma`: o cartão diz o que abrir e o que experimentar, e o formulário abre no mesmo turno. Qualquer pergunta vai para a pessoa. Pergunta aberta interrompe a delegação. Um papel não responde dúvida de outro e não abre o formulário. O pai lê `Alterado nesta rodada` e `Preciso de você` em **Último cartão** de `estado.md` (e o cartão devolvido) e Perguntas abertas; monta o AskQuestion com os blocos Alterado e Preciso de você em cada `prompt`, antes das opções.

## 5. Funções

Quando REQ, IU e, se houver tela, o contrato visual existem, grave em `estado.md` a lista ordenada. Cada item é um comportamento que a pessoa usa no sistema. Não reabra o requisito.

Uma função por ciclo: tester, developer, parada. O harness não commita, não faz ação de Git e não pergunta. O cartão diz o que abrir e o que experimentar. O formulário oferece Seguir e Parar. Problema no campo livre não avança a função. A próxima função espera Seguir.

Reviewer e, se houver tela, designer visual só depois da última função, quando a pessoa escolher Seguir. Architect e o designer de contrato não refazem documento.

No caminho curto, o mesmo portão: depois da função, pare para o teste no sistema. Sem commit e sem pergunta de Git.

## 6. Análise

Architect grava nota curta em `.cursor/tecnico/analises/` com [relatorio-analise.md](../templates/relatorio-analise.md). Regra de negócio vai para `.cursor/requisitos/`, não para a análise. Se a análise indicar implementação, o formulário oferece Seguir no caminho completo ou Parar.

## 7. Revisão com tela

Depois que a pessoa testou a última função e escolheu Seguir, lance reviewer e designer visual juntos. Junte os vereditos. Se a máquina estiver no limite de memória e a pessoa pedir, delegue em sequência (reviewer primeiro, designer visual depois), em vez de paralelo. CRÍTICO ou ALTO de implementação devolve ao developer. Regra, critério, plano ou expectativa de teste voltam ao papel da causa. Tela sem layout moderno, agradável, minimalista e profissional bloqueia. Mudança além disso a pessoa pede na revisão dela.

## 8. Parar

Antes do cartão ou do formulário que espera resposta: encerre servidores e jobs em background que o agente abriu neste ciclo (confira terminais do turno; mate só o que o agente iniciou, não o Cursor nem processos da pessoa). Se `estado.md` listar algo em **Processos do ciclo**, encerre e deixe `Nenhum`, salvo `servidor_persiste_ate_teste: sim` na IU — aí encerre no portão mesmo assim e o cartão manda a pessoa subir com o comando mínimo da Validação, sem processo órfão do agente.

Cada parada que espera resposta mostra o cartão (quatro linhas) e, no mesmo turno, o formulário AskQuestion. Só o agente do chat abre. Cada `prompt` traz primeiro **Alterado nesta rodada** (de `estado.md`; se vazio, bullet de `Feito:`), depois **Preciso de você**, depois a pergunta. O detalhe das mudanças não vai no texto do chat. Não repita só as opções na mensagem do chat. Até três perguntas, a mais bloqueante primeiro, só se forem independentes. A recomendada, se existir, vai na frente com `(Recommended)`. Pedido de status sem decisão pendente mostra só o cartão.

Campo livre é a resposta da pessoa. Sem alternativa real, as opções são `A resposta está no campo livre` e `Ainda não sei — manter bloqueado`. Alternativa que o papel já encontrou entra no lugar desse par. Texto livre que for fato do produto vira regra em `.cursor/requisitos/`. `Ainda não sei — manter bloqueado` deixa `BLOQUEADO`.

- `APROVADO` na IU: cartão final. Opções: Encerrar esta conversa, Continuar nesta conversa sem abrir a próxima unidade.
- Pergunta de negócio sem resposta. Não infira.
- Risco ALTO sem aceite. Opções: Aceito o risco, Não aceito.
- RED inválido.
- Terceira rodada de `ALTERACOES_NECESSARIAS`.
- Função entregue. Sem commit e sem pergunta de Git. O cartão diz o que abrir e o que experimentar. Opções: Seguir, Parar. Problema no campo livre não avança a função.
- Conflito entre REQ, IU e o pedido. Não infira.
- Pergunta aberta. Um papel não responde dúvida de outro.
- Infraestrutura que impede a verificação. Grave `BLOQUEADO`. A tarefa não fica verificada.
- Cancelamento explícito. Grave `CANCELADO`. Não abra formulário.
