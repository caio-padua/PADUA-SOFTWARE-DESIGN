# FILA DE PRODUCAO — <NOME DO PROJETO>

> Fila unica de trabalho. Ordenada por PRIORIDADE, nunca por ordem em que o
> pedido chegou.
>
> `P0` e so o que causa dano irreversivel: dado de cliente vazando, senha
> guardada errado, ausencia de copia de seguranca. Se desfazer e possivel, nao
> e P0.

| Nº | Item | O que e / como sera feito | Responsavel | Depende de | Estado | Prioridade | Esforco | Em linguagem de leigo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | <titulo curto, nunca muda> | <concreto: arquivo, tabela, rota> | <um agente> | — | A FAZER | P0 | <estimativa> | <analogia do mundo do dono> |

Estados possiveis, e nada mais:

| Estado | Significa |
| --- | --- |
| `A FAZER` | Nada pendente, ou o pendente e do mesmo dono (fila propria dele) |
| `AGUARDANDO` | Ha pendencia de OUTRO dono na cadeia. Comecar nao depende dele |
| `CONCLUIDO` | Entregue e conferido, com identificador de commit citado |

Trabalho novo entra com numero maior que o ultimo em uso. Nunca se reaproveita
numero, nunca se renumera: todo recado antigo que cita numero passaria a
apontar para o item errado.
