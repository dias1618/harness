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

Grave o caminho em `.cursor/memoria/estado.md` ([modelo](../templates/estado.md)).

## 3. Status da IU

| Status | Próximo |
|--------|---------|
| Ausente, rascunho ou `BLOQUEADO` | architect ([01](01-descobrir-requisitos.md)) |
| `PRONTO_PARA_TESTES` sem contrato visual, e a IU tem tela | designer ([06](06-designer.md)) |
| `PRONTO_PARA_TESTES` | tester ([02](02-testar-primeiro.md)) |
| `RED` | developer ([03](03-implementar-tdd.md)) |
| `VALIDADO` | reviewer ([04](04-revisar-entrega.md)); com tela, designer visual em paralelo |
| `ALTERACOES_NECESSARIAS`, rodada 1 ou 2 | developer ([05](05-corrigir-revisao.md)) |
| Rodada 3, ou spec a mudar | Pare. Pessoa ou architect |

## 4. Delegar

Uma fase por vez, com contexto mínimo:

- Pedido em uma frase.
- Caminhos de REQ, IU, ADR, contrato visual, plano, handoff.
- Status e rodada.
- Proibições: developer não edita teste do tester; architect, designer e reviewer não editam código de produção; reviewer e designer visual não recebem o resumo do developer como evidência.

Não cole o corpo dos documentos. Espere o cartão. `Preciso de você: nenhuma` segue. Qualquer pergunta para a pessoa.

## 5. Análise

Architect grava nota curta em `.cursor/tecnico/analises/` com [relatorio-analise.md](../templates/relatorio-analise.md). Regra de negócio vai para `.cursor/requisitos/`, não para a análise. Se a análise indicar implementação, pergunte se continua no caminho completo.

## 6. Revisão com tela

Depois do developer, lance reviewer e designer visual juntos. Junte os vereditos. Um CRÍTICO ou ALTO de qualquer um devolve ao developer. Sugestão de gosto não bloqueia.

## 7. Parar

- Pergunta de negócio sem resposta, ou risco ALTO sem aceite.
- RED inválido.
- Terceira rodada de `ALTERACOES_NECESSARIAS`.
- Conflito entre REQ, IU e o pedido. Não infira.
