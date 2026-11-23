# Estado

## IU

IU-XXX

## Caminho

curto | completo

## Status

BLOQUEADO | PRONTO_PARA_TESTES | RED | AGUARDANDO_TESTE | VALIDADO | ALTERACOES_NECESSARIAS | APROVADO | CANCELADO

## Revisão aceita

REQ, IU e plano de testes na revisão gravada. Artefato mudou: o status que dependia dele volta ao dono.

## Próximo papel

architect | designer | tester | developer | reviewer | pessoa

## Perguntas abertas

Nenhuma

ou, até três, a mais bloqueante primeiro:

- id: [curto]
  prompt: [pergunta autocontida; o agente do chat também coloca isso no AskQuestion, depois de Alterado nesta rodada e Preciso de você, quando for o caso]
  opcoes: [alternativas reais separadas por " | ", ou vazio]
  multipla: nao

## Último veredito

[uma frase]

## Último cartão

Feito:
Alterado nesta rodada:
- [comportamento ou efeito visível que mudou; caminho só se ajudar no teste]
Preciso de você:
Próximo:
Resto:

## Função atual

[nome | nenhuma]

## Funções

Mesmos nomes e ordem da seção **Funções por ciclo** da IU.

- [ ] [comportamento que a pessoa usa no sistema]

## Processos do ciclo

Nenhum

ou, se o agente deixou servidor até o portão (`servidor_persiste_ate_teste: sim` na IU):

- [porta] — [comando] — encerrar no portão AGUARDANDO_TESTE

## Decisões de trabalho já perguntadas

| Decisão | Escolha |
|---------|---------|
| | |
