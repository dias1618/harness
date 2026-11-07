# Guia do harness

Texto para consulta. O passo a passo que os agentes seguem está nos workflows da mesma pasta.

## O que liga o ciclo

`#harness` na mensagem liga o ciclo. Sem essa tag, o trabalho segue direto, fora desta máquina de estados.

Se o projeto aberto tiver `.cursor/workflows/00-orquestrador-harness.md`, vale o orquestrador desse projeto. É o caso do sharechar. Este guia descreve o harness geral.

## Papéis

O orquestrador é o agente do chat. Ele escolhe o caminho, delega e só fala com você num portão. Não implementa a feature.

| Papel | Faz | Não faz |
|-------|-----|---------|
| Architect | Pergunta o que falta e publica requisito e unidade de implementação | Não inventa regra de negócio e não escreve código |
| Designer | Contrato visual mobile e web; depois revisa o que foi renderizado | Não escreve código e não inventa regra. Só entra se a tarefa tem tela |
| Tester | Escreve os testes e confirma que falham pelo motivo certo | Não altera código de produção |
| Developer | Faz os testes passarem e roda o comando da unidade | Não edita o teste do tester e não amplia o escopo |
| Reviewer | Compara o diff com o requisito, a unidade e o resultado do comando | Não corrige código. Não usa o resumo do developer como prova |

## Dois caminhos

Curto: a correção já está coberta pelo requisito e pela unidade, sem regra nova e sem tela. Só o developer, mais o comando de validação. O reviewer entra se você pedir ou se essa unidade não tiver comando.

Completo: regra nova, unidade nova ou comportamento ainda sem contrato.

1. Architect publica o requisito e a unidade.
2. Se há tela, o designer publica o contrato visual.
3. Tester deixa os testes falhando pelo motivo certo.
4. Developer implementa e roda o comando.
5. Reviewer julga. Se há tela, o designer revisa o render ao mesmo tempo.
6. Correção só para achado crítico ou alto, no máximo duas vezes. Na terceira, para em você ou no architect.

Em dúvida entre analisar e implementar, a análise vem primeiro. Uma unidade por vez.

## Status

| Status | Significado | Quem segue |
|--------|-------------|------------|
| `BLOQUEADO` | Falta decisão sua, o risco é alto ou a spec mudou | Você, ou o architect |
| `PRONTO_PARA_TESTES` | Requisito e unidade fechados. Com tela, o contrato visual também | Tester |
| `RED` | Testes escritos e falhando como esperado | Developer |
| `VALIDADO` | O comando da unidade passou | Reviewer (e designer, se há tela) |
| `ALTERACOES_NECESSARIAS` | Crítico ou alto, rodada 1 ou 2 | Developer |
| `APROVADO` | Entrega aceita | Ninguém |

O comando que passa não aparece no chat. O que falha volta para o developer, com o erro.

## Quando o chat para

Você recebe este cartão quando falta uma decisão, o risco é alto, a revisão estourou, ou quando você pede o status. Fase que passou só atualiza o estado.

```text
Feito: [uma frase]
Preciso de você: nenhuma
Próximo: [papel ou sua resposta]
Resto: [um caminho]
```

No portão, no máximo três perguntas, a mais bloqueante primeiro.

## Onde fica cada coisa

Processo desta máquina, igual para todos os projetos:

- `~/.cursor/rules/` — ordens curtas
- `~/.cursor/skills/harness/` — este guia, workflows e modelos em branco
- `~/.cursor/agents/` — os cinco papéis
- `~/.cursor/hooks.json` e `~/.cursor/hooks/` — bloqueio de comando destrutivo

Documento e memória de um projeto ficam no `.cursor` desse projeto, nunca em `~/.cursor`:

- `.cursor/context/projeto.md` — o que o projeto é
- `.cursor/memoria/estado.md` — onde a próxima sessão retoma
- `.cursor/requisitos/` — regra de negócio
- `.cursor/tecnico/` — unidade, testes, handoff, revisão, análise e contrato de UI
- `.cursor/decisoes/` — decisão técnica
- `.cursor/rules/` e `.cursor/skills/` — rule ou skill só daquele projeto

Sem `.cursor/context/projeto.md`, o orquestrador pergunta antes de criar essa estrutura.

## Rule ou skill

Depois de uma correção sua, ou de uma decisão sobre como trabalhar, o chat pergunta uma vez:

```text
Isto que você acabou de decidir pode virar artefato permanente?

1. Rule só neste projeto — .cursor/rules/
2. Rule em todos os projetos — ~/.cursor/rules/
3. Skill só neste projeto — .cursor/skills/
4. Skill em todos os projetos — ~/.cursor/skills/
5. Não

Responda com o número. Se for 1 a 4, eu escrevo o arquivo e te devolvo o caminho.
```

Rule é uma ordem curta, carregada sempre. Skill é um procedimento aberto só quando a situação pede. Fato do produto vai para `.cursor/requisitos/` e não entra nessa pergunta. Sem o número, nada é criado. A mesma decisão não é perguntada de novo.

Controle novo no harness só entra depois de uma falha real e de um sim nessa pergunta. Quando um papel, status, caminho, gatilho ou pasta mudar, este guia muda na mesma edição.

## Git de ~/.cursor

A pasta inteira pode ser um repositório. O bloco manual no final de `~/.cursor/.gitignore` é o que decide, e pasta nova só entra se esse bloco for editado à mão.

Entra no Git: `.gitignore`, `rules/`, `skills/`, `agents/`, `hooks.json` e `hooks/`.

Fica de fora: `skills-cursor/`, `plugins/`, `plans/`, `projects/`, `commands/` e `subagents/`.

O commit fica com você.
