---
name: conferir-fila
description: Diz o que cada agente pode comecar agora, lendo a cadeia de dependencias da fila de producao por inteiro. Use quando alguem perguntar "o que eu faco agora", "em que pe estamos", "quem esta travado", "o que esta livre", ou antes de comecar qualquer tarefa num projeto que tem fila.
---

# Conferir a fila antes de agir

Nunca responda "o que fazer agora" de memoria nem por leitura rapida. Calcule.

## O que rodar

```
python3 scripts/conferir_coerencia.py
```

Saida limpa significa: nenhum numero repetido, nenhum estado brigando com a
cadeia de dependencias, e a lista de quem pode comecar o que.

## Por que a cadeia se le por inteiro

Um passo so da falso positivo. Exemplo real: o item 21 depende do 20, que
depende do 19, que e do dono do projeto. Olhando um passo, o 21 parece travado
pelo 20, do mesmo agente, e portanto liberado para ele organizar. Olhando a
cadeia inteira, o 21 espera uma decisao humana e nao vai sair hoje.

## Os dois erros que importam

| Erro | Consequencia |
| --- | --- |
| Item que espera outro agente sem estar marcado `AGUARDANDO` | O dono comeca e colide. E o acidente que a fila existe para evitar. |
| Item marcado `AGUARDANDO` com a cadeia inteira limpa | Esconde trabalho livre. Um agente fica parado achando que esta bloqueado. |

Item travado apenas pela propria fila do mesmo agente nao e erro em nenhum dos
dois estados: e ordem de trabalho dele, e ele decide.

## Se o conferidor acusar divergencia

Corrija o **dado**, nao o conferidor — a menos que voce prove que a regra do
conferidor esta errada. Numa ocasiao a regra estava mesmo errada: ela olhava um
passo da cadeia em vez da cadeia inteira. Provar primeiro, corrigir depois.

Toda correcao de estado gera linha no historico: data, quem, numero, campo,
como estava, como ficou, por que mudou, prova.

## Ao terminar

Diga ao usuario, em tabela: o que esta livre para cada agente, e o que esta
travado e por quem. Nao entregue a saida crua do script.
