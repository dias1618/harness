# Workflow — Revisar entrega (reviewer)

Julgar a entrega pela spec, pelo diff e pelo sensor. Não pelo resumo do developer.

Antes de julgar, leia `~/.cursor/skills/harness/oficio/reviewer.md` por inteiro.

## Pré-condição

A última função está commitada, a pessoa mandou seguir, e o estado está `VALIDADO`. Sem lista de funções, basta o handoff da unidade com o comando em PASS.

## 1. Evidência

Abra IU, REQ, ADRs e o diff real. O handoff serve para a lista de arquivos e os comandos. Ignore o resumo como prova. Reexecute o comando da IU se o resultado for duvidoso.

Perguntas:

- Só o escopo da IU?
- Comportamento igual à REQ?
- Testes cobrem comportamento, e o developer não os editou?
- Limites da IU respeitados?

Teste verde não aprova sozinho.

## 2. Veredito

Grave `.cursor/tecnico/revisoes/IU-XXX-revisao.md` ([relatorio-revisao.md](../templates/relatorio-revisao.md)).

- `APROVADO` — escopo, comportamento e testes ok. Atualize a IU.
- `ALTERACOES_NECESSARIAS` — só CRÍTICO ou ALTO, rodada 1 ou 2.
- `BLOQUEADO` — a spec precisa mudar, ou esta é a terceira rodada. Escale à pessoa ou ao architect.

MÉDIO e BAIXO são sugestão. Não bloqueiam. Não procure defeito para preencher o relatório.

## 3. Devolução

Só o cartão, com o veredito na frase de Feito.
