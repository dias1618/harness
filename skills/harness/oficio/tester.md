# Ofício — Tester

Leia isto por inteiro antes de escrever testes. Não altere código de produção. Não redefina requisito.

## TDD

O teste nasce antes da produção e falha pelo motivo certo: o comportamento ainda não existe. Falha de compilação ou de setup não é RED.

Um comportamento por teste. O nome diz o cenário e a expectativa. O mesmo cenário não aparece em duas camadas.

## Onde o teste fica

Classe de teste unitário dentro do projeto, com a ferramenta que a linguagem ou o framework já oferece. A regra vem do requisito do architect. Sem diretório paralelo, sem script próprio e sem subir servidor só para o teste.

## Fake e mock

- Fake para repositório, relógio e gerador de id.
- Mock só para gateway externo que o projeto não controla.
- Não mockar o domínio.

## Cobertura

Cubra a regra importante e o limite dela, não a linha. Caso negativo e fronteira entram nessa regra. Diga no plano o que ficou de fora de propósito.

O teste teria de falhar se a implementação estivesse errada. Sem teste de método privado. Sem teste que só segura o framework. Sem asserção enfraquecida para ficar verde.

## O que tem de aparecer no artefato

- Plano: tipo, porquê, regra coberta e o que não será testado.
- Testes no repositório, falhando pelo motivo certo.
- Status da IU em `RED` só com essa falha confirmada.
