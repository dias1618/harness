# Workflow — Corrigir após revisão (developer)

Corrigir só CRÍTICO e ALTO, na rodada 1 ou 2.

## 1. Ler o veredito

Implemente apenas os itens obrigatórios do relatório de revisão e, se houver tela, do veredito visual. Ignore MÉDIO e BAIXO.

## 2. Limites

Não altere teste do tester. Sem refatoração fora da correção. Se a correção exigir mudança de REQ ou contrato, pare em `BLOQUEADO` e volte ao architect.

## 3. Sensor

Rode de novo os comandos da IU. Passou: uma linha. Falhou: corrija com o erro, sem chamar a pessoa.

## 4. Handoff

Novo handoff com a rodada incrementada e status `VALIDADO`. Devolva só o cartão. O reviewer olha de novo; com tela, o designer visual também.
