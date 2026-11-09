# Workflow — Implementar (developer)

Levar a função atual de `RED` a `AGUARDANDO_TESTE` sem alterar teste do tester.

Antes de editar, leia `~/.cursor/skills/harness/oficio/developer.md` por inteiro.

## Pré-condição

IU em `RED` e tester liberou. No caminho curto, a IU já está contratada e os testes existentes cobrem a correção; se não houver teste, pare e volte ao caminho completo.

## 1. Contexto

IU, REQ, contrato visual se houver, testes da IU, código relacionado. Caminhos, não corpos colados.

## 2. GREEN e REFACTOR

A solução mais simples que respeita a função atual e faz o teste dela passar. Depois, clareza sem mudar comportamento. Não comece a próxima função.

Proibido editar teste do tester, ampliar escopo ou mudar arquitetura fora da IU. Se precisar, pare em `BLOQUEADO`. Não commite: o orquestrador commita a função.

## 3. Sensor

Rode cada comando da seção Validação da IU. Só esses. Suíte e build não entram por conta própria.

- Passou: uma linha no handoff, `PASS`. Não descreva o que foi checado.
- Falhou: o erro acionável volta para você. Corrija e rode de novo. Não chame a pessoa.
- Ausente ou não executado: `NAO_EXECUTADO` no handoff. Isso não aprova. No caminho curto, o reviewer entra por causa dessa falta.

Não afirme merge, publicação nem implantação. Essas operações só contam depois de executadas.

## 4. Handoff

Grave `.cursor/tecnico/handoffs/IU-XXX-handoff.md` ([handoff-desenvolvedor.md](../templates/handoff-desenvolvedor.md)). Marque só o critério da função atual. Não marque critério de função futura. Não use `VALIDADO` enquanto a pessoa não tiver testado a última função.

Atualize `estado.md` para `AGUARDANDO_TESTE` e próximo papel `pessoa`. Devolva só o cartão. O resumo do handoff não é evidência para reviewer nem designer.
