# Workflow — Orquestrador

O agente do chat classifica, delega e só fala com a pessoa no portão. Não substitui os papéis.

## 1. Projeto com orquestrador próprio

Se existir `.cursor/workflows/00-orquestrador-harness.md`, siga esse arquivo e pare este workflow.

## 2. Classificar

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
| `VALIDADO` | reviewer ([04](04-revisar-entrega.md)); com tela, designer visual em paralelo. Só a última função, depois que a pessoa mandou seguir |
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
- Caminhos de REQ, IU, ADR, contrato visual, plano, handoff.
- Status e rodada.
- Proibições: developer não edita teste do tester; architect, designer e reviewer não editam código de produção; reviewer e designer visual não recebem o resumo do developer como evidência.

Não cole o corpo dos documentos. Espere o cartão. `Preciso de você: nenhuma` segue. Função commitada não é `nenhuma`. Qualquer pergunta vai para a pessoa. Pergunta aberta interrompe a delegação. Um papel não responde dúvida de outro.

## 5. Funções

Quando REQ, IU e, se houver tela, o contrato visual existem, grave em `estado.md` a lista ordenada. Cada item é um comportamento que a pessoa usa no sistema. Não reabra o requisito.

Uma função por ciclo: tester, developer, commit do orquestrador, parada. O commit segue o estilo do repositório e leva só os arquivos dessa função. O cartão diz o que abrir e o que experimentar. A próxima função espera a pessoa mandar seguir.

Reviewer e, se houver tela, designer visual só depois da última função, quando a pessoa mandar seguir. Architect e o designer de contrato não refazem documento.

No caminho curto, o mesmo portão: depois do commit, pare para o teste no sistema.

## 6. Análise

Architect grava nota curta em `.cursor/tecnico/analises/` com [relatorio-analise.md](../templates/relatorio-analise.md). Regra de negócio vai para `.cursor/requisitos/`, não para a análise. Se a análise indicar implementação, pergunte se continua no caminho completo.

## 7. Revisão com tela

Depois que a pessoa testou a última função e mandou seguir, lance reviewer e designer visual juntos. Junte os vereditos. CRÍTICO ou ALTO de implementação devolve ao developer. Regra, critério, plano ou expectativa de teste voltam ao papel da causa. Tela sem layout moderno, agradável, minimalista e profissional bloqueia. Mudança além disso a pessoa pede na revisão dela.

## 8. Parar

- Pergunta de negócio sem resposta, ou risco ALTO sem aceite.
- RED inválido.
- Terceira rodada de `ALTERACOES_NECESSARIAS`.
- Função commitada. A pessoa testa o sistema.
- Conflito entre REQ, IU e o pedido. Não infira.
- Pergunta aberta. Um papel não responde dúvida de outro.
- Infraestrutura que impede a verificação. Grave `BLOQUEADO`. A tarefa não fica verificada.
- Cancelamento explícito. Grave `CANCELADO`.
