# Workflow — Corrigir após revisão (developer)

Corrigir só defeito ou regressão de implementação, CRÍTICO e ALTO, na rodada 1 ou 2.

Antes de editar, leia `~/.cursor/skills/harness/oficio/developer.md` por inteiro.

Outra causa não entra neste workflow:

- Regra ambígua, critério incompleto ou violação nascida do plano: architect, com nova aprovação.
- Expectativa de teste errada: tester. Se a spec mudou, a aprovação cai junto.
- Mudança de escopo pedida pela pessoa: requisito, plano e testes afetados.
- Infraestrutura que impede a verificação: `BLOQUEADO`. A tarefa não fica verificada.
- Pergunta aberta: pare. Um papel não responde dúvida de outro.

## 1. Ler o veredito

Implemente apenas os itens obrigatórios do relatório de revisão e, se houver tela, do veredito visual. Ignore MÉDIO e BAIXO.

Reabra só os arquivos citados no relatório ou no diff; não varra o repositório de novo.

## 2. Limites

Não altere teste do tester. Sem refatoração fora da correção. Se a correção exigir mudança de REQ ou contrato, pare em `BLOQUEADO` e volte ao architect.

## 3. Sensor

Rode de novo os comandos da seção Validação da IU. Passou: uma linha `PASS`. Falhou: corrija com o erro, sem chamar a pessoa. Não rodou: `NAO_EXECUTADO`. Isso não aprova e não muda o estado para `VALIDADO`.

## 4. Handoff

Novo handoff com a rodada incrementada. Sensor em `PASS`: status `VALIDADO`. Sensor em `NAO_EXECUTADO`: não use `VALIDADO`. Devolva só o cartão. O reviewer olha de novo; com tela, o designer visual também.
