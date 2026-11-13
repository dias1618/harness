# IU-XXX — [título]

## Status

BLOQUEADO | PRONTO_PARA_TESTES | RED | VALIDADO | APROVADO

## Referências

- REQ-XXX
- ADR-XXX, se houver
- Contrato visual, se houver tela

## Objetivo

[O que existe ao final]

## Escopo

- [item]

## Fora de escopo

- [item]

## Tem tela

sim | não

## Limites

- [porta, contexto, o que o domínio não pode conhecer]

## Tradeoff

- Ganha:
- Perde:
- Se o desempenho importa, pode relaxar:
- Não pode relaxar:

## Critérios de aceite

- [ ] [comportamento testável]

## Funções por ciclo

Cada bloco espelha um item da lista em `estado.md`. Um ciclo tester → developer cobre só uma função.

### [nome da função 1]

- Critérios desta função:
- Arquivos prováveis:
- Validação parcial, se couber:

### [nome da função 2]

- Critérios desta função:
- Arquivos prováveis:
- Validação parcial, se couber:

## Testes exigidos

- Unidade:
- Integração:

## Validação

Obrigatório em mudança de código:

- `[testes novos]` — esperado: sucesso
- `[testes preexistentes da área]` — esperado: sucesso
- `[compilação ou análise estática do projeto, se houver]` — esperado: sucesso

Conforme o escopo, quando a unidade os alcançar:

- `[suíte | banco | API | contrato | build]` — esperado: sucesso

Conforme o risco, quando a IU o tiver:

- `[segurança | desempenho | concorrência | migração | compatibilidade]` — esperado: sucesso

Comando ausente ou não executado: `NAO_EXECUTADO`. Isso não aprova.

## Risco

BAIXO | MEDIO | ALTO
