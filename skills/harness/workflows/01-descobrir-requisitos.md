# Workflow — Descobrir requisitos (architect)

Transformar o pedido em REQ e IU, sem inferir negócio e sem código de produção.

## 1. Contexto mínimo

1. `.cursor/context/projeto.md`
2. ADRs citados
3. REQ ou IU se for continuação

Não leia o repositório inteiro.

## 2. Perguntar

Se faltar ator, regra testável, exceção ou integração: pare com até 3 perguntas, a mais bloqueante primeiro. Grave `BLOQUEADO` em `.cursor/memoria/estado.md`. Não preencha lacuna com suposição.

Resposta da pessoa vira regra testável em `.cursor/requisitos/REQ-XXX.md` ([requisito.md](../templates/requisito.md)). Não deixe a decisão só na análise.

## 3. Contrato técnico

Grave `.cursor/tecnico/unidades-implementacao/IU-XXX.md` ([unidade-implementacao.md](../templates/unidade-implementacao.md)).

A IU tem critérios testáveis, tipos de teste, comando de validação (placeholder aceitável) e risco. Limite novo que valha para várias IUs vira ADR em `.cursor/decisoes/ADR/` ([decisao-adr.md](../templates/decisao-adr.md)).

## 4. Status

- `PRONTO_PARA_TESTES` — negócio e contrato bastam para o tester. Se houver tela, o designer ainda precisa do contrato visual antes do tester.
- `BLOQUEADO` — pergunta aberta ou ADR pendente.
- Risco ALTO: peça aceite explícito antes do tester.

## 5. Devolução

Só o cartão. O pai não recebe o corpo do REQ.
