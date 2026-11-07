# Workflow — Implementar (developer)

Levar a IU de `RED` a `VALIDADO` sem alterar teste do tester.

## Pré-condição

IU em `RED` e tester liberou. No caminho curto, a IU já está contratada e os testes existentes cobrem a correção; se não houver teste, pare e volte ao caminho completo.

## 1. Contexto

IU, REQ, contrato visual se houver, testes da IU, código relacionado. Caminhos, não corpos colados.

## 2. GREEN e REFACTOR

A solução mais simples que respeita a IU e faz o teste passar. Depois, clareza sem mudar comportamento.

Proibido editar teste do tester, ampliar escopo ou mudar arquitetura fora da IU. Se precisar, pare em `BLOQUEADO`.

## 3. Sensor

Rode cada comando da seção Validação da IU.

- Passou: uma linha no handoff, `PASS`. Não descreva o que foi checado.
- Falhou: o erro acionável volta para você. Corrija e rode de novo. Não chame a pessoa.

Sem comando na IU, diga isso no handoff. No caminho curto, o reviewer entra por causa dessa falta.

## 4. Handoff

Grave `.cursor/tecnico/handoffs/IU-XXX-handoff.md` ([handoff-desenvolvedor.md](../templates/handoff-desenvolvedor.md)). `VALIDADO` só com comandos ok e critérios marcados.

Atualize `estado.md`. Devolva só o cartão. O resumo do handoff não é evidência para reviewer nem designer.
