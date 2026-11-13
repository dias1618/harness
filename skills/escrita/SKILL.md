---
name: escrita
description: >
  Escreve ou revisa texto, artigo, documentação, guia, capítulo e prosa para
  pessoas. Antes de redigir, pergunta em rodadas o público, o estilo e a
  formalidade. Em texto novo, pergunta também o que entra e o que fica de
  fora. Em texto já pronto, conserva as informações do original. Use ao
  escrever ou revisar documentação humana, artigo, guia, capítulo ou qualquer
  prosa para pessoas. Não use em especificação, rule, gate, skill ou checklist
  de agente.
---

# Escrita para pessoas

Prosa para gente. Especificação, rule, gate e checklist de agente continuam prescritivos e ficam fora desta skill.

## Antes de escrever

Pergunte numa rodada por vez e espere a resposta. Não junte as rodadas na mesma mensagem. Pule a rodada cujo assunto o pedido ou a conversa já tiver respondido.

1. **Público.** Quem vai ler, e o que essa pessoa já sabe do assunto? Há termo que precisa ser explicado, ou o texto pode ir direto à decisão?
2. **Estilo.** O texto é documentação corrida, artigo que desenvolve um argumento, ou manual com passos? Há algum texto de referência para aproximar a voz?
3. **Formalidade.** O tratamento é institucional, de colega, ou mais próximo da fala? Cabe tratar o leitor por você?

A quarta rodada só acontece quando o texto ainda vai ser escrito. Pergunte, de acordo com o assunto, o que precisa entrar e o que deve ficar de fora: exemplo, link, recomendação, contexto.

Quando o pedido for arrumar um texto que já está pronto, não faça essa quarta rodada. Reescreva a forma com o público, o estilo e a formalidade combinados, e conserve as informações do original. Não invente fato, exemplo, recomendação nem link que o texto não tenha.

## Leitor

Escreva para o público da primeira rodada. Se essa pessoa já domina o ofício, deixe de fora a aula do que ela sabe e conte a decisão, o contexto em que ela vale e, se o texto já apontava, o link da documentação oficial. O didático está em encadear o motivo, não em reexplicar o básico.

## Parágrafo

Um parágrafo desenvolve uma ideia: a situação, a decisão e o motivo, e então o manual para quem quiser o detalhe do ofício. Misture frase longa com frase curta. A frase curta marca uma regra no meio do parágrafo. Cinco frases de uma linha seguidas são o defeito a corrigir. Junte com porque, quando, então, e.

## O que dizer

Afirme o que a coisa faz. Corte o molde “não é X, é Y”, “o que importa é” e “não só X, mas Y”. A negação fica quando a ausência é o fato, como em “a senha não entra no Git”.

A formalidade é a da terceira rodada. No grau de colega, o tom segue o espírito do [guia de tom do Google](https://developers.google.com/style/tone): conversa, sem blog. Em qualquer grau, sem anúncio (“vale notar”), sem fecho que repete o começo, sem pergunta retórica.

Lista só quando os itens são um catálogo de verdade, como opções de biblioteca. O parágrafo comum não vira lista de decretos.

## Referências de voz

- [Cleaning Up AI Prose](https://thinkwright.ai/editorial-standards): o parágrafo desenvolve um argumento, e frase longa convive com frase curta.
- [AI-Writing Don'ts](https://marin.readthedocs.io/en/latest/dev-guide/writing-style/ai-writing-donts/): corte o contraste de estoque.
- [Deslopping AI Prose](https://www.anaconda.com/blog/deslopping-ai-prose): una as frases picadas e corte o fecho vazio.

Não aplique limite de vinte palavras por frase.

## Antes e depois

Antes:

> Dado relacional fica no PostgreSQL, um schema por domínio. Domínio não lê tabela de outro: pede por API. A senha de conexão não entra no repositório. O `.env` versionado é exemplo. O valor real fica no cofre.

Depois:

> O dado relacional dos sistemas novos fica no PostgreSQL, com um schema para cada domínio. Quando um domínio precisa de um dado que pertence a outro, o pedido sai pela API de integração, e o schema de origem continua com o time que o modelou. A senha dessa conexão vive no cofre. O arquivo versionado só mostra o formato, com usuário e senha que não existem em ambiente nenhum.

Leia o trecho em voz alta. Se soar como uma sequência de avisos, reescreva.
