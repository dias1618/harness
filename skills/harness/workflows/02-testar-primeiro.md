# Workflow — Testar primeiro (tester)

Testes em RED, sem tocar produção.

Antes de escrever, leia `~/.cursor/skills/harness/oficio/tester.md` por inteiro.

## Pré-condição

IU em `PRONTO_PARA_TESTES`. Se a IU tem tela, `.cursor/tecnico/ui/IU-XXX-ui.md` já existe.

## 1. Contexto

Leia `.cursor/memoria/estado.md` e o bloco da **função atual** na seção **Funções por ciclo** da IU. Abra REQ e ADRs só para critérios que essa função cruza. Não leia a IU inteira se o bloco bastar. Código: `glob`/`grep` para achar onde os testes moram; evite ler arquivos grandes inteiros.

## 2. Plano

Grave `.cursor/tecnico/planos-testes/IU-XXX-plano.md` ([plano-testes.md](../templates/plano-testes.md)). Se o plano já existe, não o substitua. Cada critério da função atual tem ao menos um teste. Critério de função futura fica para o ciclo dela.

## 3. Testes

Somente teste unitário da função atual, em classe dentro do projeto, com a ferramenta da linguagem ou do framework. Não escreva teste de função futura. Não crie diretório paralelo, script próprio nem servidor só para o teste. Um comportamento por teste.

## 4. Executar

Rode o comando da IU.

- Falha pelo motivo esperado (a função atual ainda ausente): status `RED` e `LIBERAR_DESENVOLVEDOR`. Teste de função anterior pode passar.
- Falha de compilação ou setup: `BLOQUEADO`. Não entregue RED inválido.

Sucesso do comando neste passo é problema: o teste da função atual tinha de falhar.

## 5. Devolução

Cartão mais a recomendação numa linha: `LIBERAR_DESENVOLVEDOR`, `VOLTA_ARQUITETO` ou `BLOQUEADO`.
