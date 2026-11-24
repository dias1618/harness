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
  prompt: [pergunta autocontida; o agente do chat também coloca isso no AskQuestion, depois do resumo factual e de Preciso de você, quando for o caso]
  opcoes: [alternativas reais separadas por " | ", ou vazio]
  multipla: nao

## Último veredito

[uma frase]

## Último cartão

Feito:
Alterado nesta rodada:
[1 a 3 frases factuais, só o que entrou nesta rodada: recurso, endpoint/rota, campos, tela ou artefato (REQ, IU, teste RED, contrato). Uma condição atípica só se for o ponto do teste (ex.: erro ao excluir se houver vínculo). Evite o que não mudou, happy path óbvio, motivação, tópicos, termos vagos; ~350 caracteres. Tom: "Criado o endpoint PUT /recursos/{id}; no body entram nome, tipo e ativo." | "A exclusão de recurso está disponível; retorna erro se estiver vinculado a outro." | "Registrada a regra de desconto no REQ-003; código de produto não foi alterado." | "Testes cobrem o cálculo de desconto; a produção ainda não implementa esse cálculo."]
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
