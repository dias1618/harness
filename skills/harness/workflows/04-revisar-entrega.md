# Workflow — Revisar entrega (reviewer)

Julgar a entrega pela spec, pelo diff e pelo sensor. Não pelo resumo do developer.

Antes de julgar, leia `~/.cursor/skills/harness/oficio/reviewer.md` por inteiro.

## Pré-condição

A última função está commitada, a pessoa mandou seguir, e o estado está `VALIDADO`. Sem lista de funções, basta o handoff da unidade com o sensor executado. `NAO_EXECUTADO` não aprova.

## 1. Evidência

Abra IU, REQ, ADRs e o diff real. O handoff serve para a lista de arquivos e os comandos. Ignore o resumo como prova. Reexecute o comando da IU se o resultado for duvidoso. Comando ausente ou não executado é `NAO_EXECUTADO`.

Perguntas:

- Só o escopo da IU?
- Comportamento igual à REQ?
- Testes cobrem comportamento, e o developer não os editou?
- Limites da IU respeitados?
- O sensor da Validação foi executado?

Teste verde não aprova sozinho. `NAO_EXECUTADO` não aprova. Merge, publicação e implantação só contam se a operação foi executada.

## 2. Veredito

Grave `.cursor/tecnico/revisoes/IU-XXX-revisao.md` ([relatorio-revisao.md](../templates/relatorio-revisao.md)).

- `APROVADO` — escopo, comportamento, testes coerentes com o requisito e sensor executado, sem achado impeditivo. Atualize a IU.
- `ALTERACOES_NECESSARIAS` — defeito ou regressão de implementação, CRÍTICO ou ALTO, rodada 1 ou 2. Volta ao developer.
- Expectativa de teste errada: volte ao tester. Se a spec mudou, a aprovação cai junto.
- Regra ambígua, critério incompleto ou violação nascida do plano: `BLOQUEADO` e architect, com nova aprovação.
- Mudança de escopo pedida pela pessoa: requisito, plano e testes afetados.
- Infraestrutura que impede a verificação: `BLOQUEADO`. A tarefa não fica verificada.
- `BLOQUEADO` — a spec precisa mudar, ou esta é a terceira rodada. Escale à pessoa ou ao architect.

Pergunta aberta interrompe a delegação. Um papel não responde dúvida de outro.

MÉDIO e BAIXO são sugestão. Não bloqueiam. Não procure defeito para preencher o relatório.

## 3. Devolução

Só o cartão, com o veredito na frase de Feito.
