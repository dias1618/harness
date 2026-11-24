# Workflow — Descobrir requisitos (architect)

Transformar o pedido em REQ e IU, sem inferir negócio e sem código de produção.

Antes de publicar, leia `~/.cursor/skills/harness/oficio/architect.md` por inteiro.

## 1. Contexto mínimo

1. `.cursor/context/projeto.md`
2. ADRs citados
3. REQ ou IU se for continuação

Não leia o repositório inteiro.

## 2. Perguntar

Se faltar ator, regra testável, exceção ou integração: grave até 3 perguntas em `.cursor/memoria/estado.md`, a mais bloqueante primeiro, no formato de Perguntas abertas do [modelo](../templates/estado.md). Grave `BLOQUEADO` e preencha **Alterado nesta rodada** no [modelo](../templates/estado.md). Não invente alternativa de negócio. Sem alternativa real, deixe `opcoes` vazio. Não escreva as alternativas no cartão. O agente do chat abre o formulário.

Resposta no campo livre vira regra testável em `.cursor/requisitos/REQ-XXX.md` ([requisito.md](../templates/requisito.md)). `Ainda não sei — manter bloqueado` permanece `BLOQUEADO`. Não deixe a decisão só na análise.

## 3. Contrato técnico

Grave `.cursor/tecnico/unidades-implementacao/IU-XXX.md` ([unidade-implementacao.md](../templates/unidade-implementacao.md)).

A IU tem critérios testáveis, **Funções por ciclo** (um bloco por comportamento que a pessoa testa no portão), tipos de teste, risco e a seção Validação. A lista em `estado.md` usa os mesmos nomes. Na Validação, prefira comandos one-shot; se o teste manual da pessoa exigir servidor, documente o comando mínimo e marque `servidor_persiste_ate_teste: sim` só quando inevitável — o agente encerra no portão e a pessoa sobe de novo. Em mudança de código, escreva os testes novos, os testes preexistentes da área e a compilação ou análise estática que o projeto já tiver. Suíte, banco, API, contrato e build entram quando o escopo os alcança. Segurança, desempenho, concorrência, migração e compatibilidade entram quando o risco existir. Placeholder aceitável no comando ainda não descoberto. Comando que ninguém rodar fica `NAO_EXECUTADO` e não aprova. Regravar REQ ou IU já aceitos zera a aprovação que dependia deles.

Limite novo que valha para várias IUs vira ADR em `.cursor/decisoes/ADR/` ([decisao-adr.md](../templates/decisao-adr.md)).

## 4. Status

- `PRONTO_PARA_TESTES` — negócio e contrato bastam para o tester. Se houver tela, o designer ainda precisa do contrato visual antes do tester.
- `BLOQUEADO` — pergunta aberta ou ADR pendente.
- Risco ALTO: grave a pergunta com opções `Aceito o risco | Não aceito`. O pai abre o formulário antes do tester.

## 5. Devolução

Atualize **Último cartão** com **Alterado nesta rodada** conforme o [modelo](../templates/estado.md). Devolva só o cartão de quatro linhas. O pai não recebe o corpo do REQ.
