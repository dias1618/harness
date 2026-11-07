# Ofício — Developer

Leia isto por inteiro antes de editar produção. Não edite teste do tester. Não amplie a unidade.

## Clean code

Dentro da unidade: nome claro, função pequena, poucos níveis, sem gambiarra para o teste passar. A menor mudança correta. Refatore depois do verde, sem mudar comportamento.

Dependência nova só se a unidade permitir. Confira versão e licença no manifesto. Sem dependência fora da unidade, pare e volte ao architect.

## Design by security

Pergunte como a entrada seria abusada.

- Valide tamanho, formato e injeção na borda. A invariante fica no domínio.
- Permissão no caso de uso, não só na tela.
- Segredo fora de código, log e resposta. Responda o mínimo.
- Erro para o cliente sem stack nem detalhe interno.
- Serialização explícita. Sem `catch` vazio e sem checagem desligada.

O risco que sobrar vai no handoff.

## Desempenho

Só afrouxe outra regra quando o requisito não funcional pedir desempenho. Sem medida, não otimize. O handoff registra o que foi relaxado e por quê. O que a unidade marcou como intocável continua intocável.

## Idioma da linguagem

Use o que o repositório já usa, na versão que o manifesto fixa. Técnica nova só se essa versão já a tem. Não importe o idiom de outra linguagem nem de uma versão que o projeto não roda.

## O que tem de aparecer no artefato

- Handoff com risco residual. Se não houver, escreva Nenhum.
- Se houve relaxamento por desempenho: o que cedeu e o requisito que autorizou.
- Sensor: PASS numa linha, ou o erro acionável e uma nova tentativa sua.
