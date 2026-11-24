# Guia do harness

Documentação **somente para pessoas**. Agentes do harness não leem este arquivo; seguem `SKILL.md` e o workflow da fase.

Texto para consulta. O passo a passo que os agentes seguem está nos workflows da mesma pasta.

## O que liga o ciclo

`#harness` na mensagem abre o ciclo. Pedido novo sem essa tag segue direto, fora desta máquina de estados.

Resposta de um ciclo já aberto continua a etapa, sem repetir a tag. Cancelamento explícito grava `CANCELADO` e para.

Na raiz do projeto, o harness cria o `README.md` quando o arquivo não existe. Se existe, mantém o informe geral, as tecnologias, as principais bibliotecas e como colocar o projeto no ar. Senha e segredo ficam de fora.

Se o projeto aberto tiver `.cursor/workflows/00-orquestrador-harness.md`, vale o orquestrador desse projeto. É o caso do sharechar. Este guia descreve o harness geral.

## Papéis

O orquestrador é o agente do chat. Ele escolhe o caminho, delega e só fala com você num portão. Não implementa a feature.

| Papel | Faz | Não faz |
|-------|-----|---------|
| Architect | Pergunta o que falta e publica requisito e unidade de implementação | Não inventa regra de negócio e não escreve código |
| Designer | Contrato visual mobile e web; depois revisa o que foi renderizado | Não escreve código e não inventa regra. Só entra se a tarefa tem tela |
| Tester | Registra testes unitários das regras de negócio, dentro de cada projeto, com a ferramenta da linguagem | Não altera código de produção e não cria estrutura paralela de teste |
| Developer | Faz os testes passarem e roda o comando da unidade | Não edita o teste do tester e não amplia o escopo |
| Reviewer | Compara o diff com o requisito, a unidade e o resultado do comando | Não corrige código. Não usa o resumo do developer como prova |

O ofício de cada um está em `~/.cursor/skills/harness/oficio/`. O agente lê o seu antes de agir. Este guia não repete o ofício.

O architect desenha para desacoplar: domínio sem framework, portas, tradeoff escrito e requisito funcional separado do não funcional, com o ponto em que o developer precisa estar atento. Detalhe em [oficio/architect.md](oficio/architect.md).

O designer faz a tela usável sem manual: fluxo na ordem do pensamento, função importante na frente, mobile e web com ergonomia própria. Em qualquer função, mesmo sem instrução específica, exige layout moderno, agradável, minimalista e profissional. Mudança além disso a pessoa pede na revisão dela. Detalhe em [oficio/designer.md](oficio/designer.md).

O tester registra testes unitários das regras de negócio pedidas pelo architect, em classes dentro de cada projeto, com a ferramenta da linguagem ou do framework. Detalhe em [oficio/tester.md](oficio/tester.md).

O developer escreve código claro, trata segurança como parte do desenho, só afrouxa forma quando o desempenho é requisito, e usa a linguagem na versão que o projeto já fixa. Detalhe em [oficio/developer.md](oficio/developer.md).

O reviewer não refaz esses ofícios. No diff, confere se eles apareceram, e só bloqueia em crítico ou alto. Detalhe em [oficio/reviewer.md](oficio/reviewer.md).

## Dois caminhos

Curto: a correção já está coberta pelo requisito e pela unidade, sem regra nova e sem tela. Só o developer, mais o comando de validação. Depois da função, pare para você testar. O harness não commita, não faz ação de Git e não pergunta. O reviewer entra se você pedir ou se essa unidade não tiver comando, e só depois desse teste.

Completo: regra nova, unidade nova ou comportamento ainda sem contrato.

1. Architect publica o requisito e a unidade.
2. Se há tela, o designer publica o contrato visual.
3. O orquestrador grava a lista de funções e trata uma por vez.
4. Tester deixa os testes dessa função falhando pelo motivo certo.
5. Developer implementa essa função e roda o comando.
6. O orquestrador para para você testar o sistema. O Git fica com você, fora do ciclo.
7. Na última função, quando você escolher Seguir, o reviewer julga. Se há tela, o designer revisa o render ao mesmo tempo.
8. Defeito de implementação, crítico ou alto, volta ao developer, no máximo duas vezes. Regra, plano ou teste voltam ao papel da causa. Na terceira, para em você ou no architect.

Em dúvida entre analisar e implementar, a análise vem primeiro. Uma unidade por vez. Uma função por ciclo. A falha que originou este portão: a unidade inteira foi implementada antes da pessoa testar.

## Status

| Status | Significado | Quem segue |
|--------|-------------|------------|
| `BLOQUEADO` | Falta decisão sua, o risco é alto ou a spec mudou | Você, ou o architect |
| `PRONTO_PARA_TESTES` | Requisito e unidade fechados. Com tela, o contrato visual também | Tester |
| `RED` | Testes escritos e falhando como esperado | Developer |
| `AGUARDANDO_TESTE` | A função foi entregue | Você testa o sistema. Com Seguir, a próxima função ou, na última, o reviewer |
| `VALIDADO` | A última função já foi testada por você e você escolheu Seguir. Sem lista de funções, o comando da unidade passou | Reviewer (e designer, se há tela) |
| `ALTERACOES_NECESSARIAS` | Crítico ou alto, rodada 1 ou 2 | Developer se for defeito. Tester ou architect se a causa for outra |
| `APROVADO` | Entrega aceita. O sensor foi executado e a revisão não tem achado impeditivo | Ninguém |
| `CANCELADO` | Você cancelou | Ninguém |

O comando que passa não aparece no chat. O que falha volta para o developer, com o erro. Comando que ninguém rodou fica `NAO_EXECUTADO` e não aprova. Merge, publicação e implantação só são afirmados depois de executados.

A aprovação vale para a revisão gravada do requisito, da unidade e do plano de testes. Se um deles mudar, o status que dependia dele volta ao dono.

## Quando o chat para

Você recebe este cartão quando falta uma decisão, o risco é alto, a revisão estourou, uma função foi entregue, ou quando você pede o status. O harness não commita e não pergunta. Fora disso, fase que passou só atualiza o estado. No fim da função, o cartão diz o que abrir e o que experimentar.

```text
Feito: [uma frase]
Preciso de você: [uma frase, sem alternativas]
Próximo: [papel ou sua resposta]
Resto: [um caminho]
```

`Preciso de você: nenhuma` não abre formulário e o ciclo segue. Se você só pede o status e não há decisão pendente, aparece só o cartão.

Toda parada que espera resposta abre, no mesmo turno, o formulário de perguntas do Cursor. Cada pergunta começa com **duas ou três frases**, diretas, do que foi feito nesta rodada — endpoint e campos, tela, documento ou teste — **sem título** e sem repetir o manual do produto. Em seguida vem **Preciso de você:**, no mesmo sentido do cartão. O chat continua curto; o detalhe fica só no formulário. As alternativas ficam no formulário, não no texto do cartão. São no máximo três, a mais bloqueante primeiro. O campo livre serve para uma resposta que não estava na lista. Sem alternativa real, as opções são escrever a resposta nesse campo ou manter bloqueado. Se você ainda não souber, nada é inventado no seu lugar.

No fim da função, o formulário oferece Seguir e Parar. Um problema descrito no campo livre não avança a função. Risco alto pede Aceito o risco ou Não aceito. Depois de uma análise, Seguir no caminho completo ou Parar. Com a unidade aprovada, Encerrar esta conversa ou Continuar nesta conversa sem abrir a próxima unidade.

## Memória na máquina

RAM sobe de dois jeitos: processos que o agente deixa no sistema (Node, Java, Flutter, servidores) e o próprio Cursor (chat longo, subagentes, MCP, browser na revisão visual). O harness manda encerrar processos do ciclo em cada portão (rule `06-fechar-servidores`) e registrar exceções em **Processos do ciclo** no `estado.md`.

| Momento | Ação sua |
|---------|----------|
| `APROVADO` na IU | Prefira **Encerrar esta conversa**; retome com `#harness` e `estado.md` |
| Conversa longa fora do ciclo | Chat novo; não arrastar IUs já fechadas |
| Projetos grandes | `.cursorignore` em `node_modules/`, `dist/`, `.next/` e artefatos de build |
| MCP que o ciclo não usa | Desligar em Customize → MCPs |
| Revisão com tela e máquina lenta | Peça revisão **sequencial** (reviewer, depois designer visual) em vez de paralela |
| Diagnóstico | *Developer: Open Process Explorer* no Cursor; `pgrep -af 'node|java|flutter'` após portão |

O architect prefere comandos one-shot na IU; servidor até o teste manual só com `servidor_persiste_ate_teste: sim` e comando mínimo documentado.

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

Sem `.cursor/context/projeto.md`, o orquestrador para e pergunta no formulário antes de criar essa estrutura.

## Rule ou skill

Depois de uma correção sua, ou de uma decisão sobre como trabalhar, o chat pergunta uma vez, no formulário: isto pode virar artefato permanente? As opções são rule só neste projeto, rule em todos os projetos, skill só neste projeto, skill em todos os projetos, ou Não. O campo livre não cria arquivo. A escolha fica registrada pelo texto da opção.

Rule é uma ordem curta, carregada sempre. Skill é um procedimento aberto só quando a situação pede. Fato do produto vai para `.cursor/requisitos/` e não entra nessa pergunta. A mesma decisão não é perguntada de novo.

Controle novo no harness só entra depois de uma falha real e de um sim nessa pergunta. Quando um papel, status, caminho, gatilho ou pasta mudar, este guia muda na mesma edição.

## Git de ~/.cursor

A pasta inteira pode ser um repositório. O bloco manual no final de `~/.cursor/.gitignore` é o que decide, e pasta nova só entra se esse bloco for editado à mão.

Entra no Git: `.gitignore`, `rules/`, `skills/`, `agents/`, `hooks.json` e `hooks/`.

Fica de fora: `skills-cursor/`, `plugins/`, `plans/`, `projects/`, `commands/` e `subagents/`.

O commit fica com você.
