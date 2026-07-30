# 04 — A PLANILHA E O ESPELHO NO REPOSITORIO

> O dono le planilha. O agente le texto. As duas tem de dizer exatamente a
> mesma coisa, e a unica forma de garantir isso e uma nunca ser digitada.

---

## O desenho

```
scripts/gerar_planilha.py
        |
        v
   planilha .xlsx  ------> sobe para PROJETO <NOME> no Drive   (o dono)
        |
        | scripts/gerar_espelho_markdown.py LE a planilha
        v
   espelho .md  ----------> docs/COORDENACAO/ no repositorio   (os agentes)
```

Uma fonte, dois formatos. O espelho **nunca** e escrito a mao.

---

## Por que o espelho existe

Enquanto a fila existir so no Drive, a coordenacao continua passando pelo ser
humano: o agente nao le Drive, entao alguem tem de copiar e colar. O espelho no
repositorio e o que tira o dono do meio.

| Sem espelho | Com espelho |
| --- | --- |
| Agente pergunta ao dono o que fazer | Agente le o arquivo e sabe |
| Dono copia texto entre tres telas | Dono nao copia nada |
| Duas versoes divergem sem ninguem ver | Divergiu = alguem digitou |

---

## A regra de ouro

**Quem muda o conteudo muda os dois, e sempre pelo script.**

Se voce editou o espelho a mao, voce criou uma segunda verdade. Foi assim que a
quarta colisao aconteceu.

---

## Como conferir que as duas batem

Nao confie no olho. Conte.

```python
# conferencia minima: numero de linhas de cada aba contra o espelho
import openpyxl
wb = openpyxl.load_workbook(PLANILHA, data_only=True)
md = open(ESPELHO, encoding="utf-8").read()
# para cada aba: contar linhas da aba e linhas da tabela correspondente no .md
```

Se os numeros nao batem, o espelho esta velho ou alguem digitou nele.

---

## O que a planilha tem de ter

| Aba | Conteudo | Quem edita |
| --- | --- | --- |
| `LINHA DE PRODUCAO` | A fila, ordenada por prioridade | Estado e Observacao: qualquer um. O resto: o escritor unico |
| `MATRIZ DA EQUIPE` | Territorio e fronteira de cada agente | O escritor unico |
| `DECISOES DO <DONO>` | As decisoes que travam trabalho, com o item que cada uma destrava | A coluna de resposta: so o dono |
| `REGRAS DE EDICAO` | Como editar sem quebrar | O escritor unico |
| `HISTORICO` | Append-only: como estava, como ficou, por que, prova | Qualquer um acrescenta |
| `GLOSSARIO` | Toda palavra tecnica, com analogia | Qualquer um acrescenta |
| `LEIA-ME` | Contexto do projeto e nomenclatura | O escritor unico |

---

## A coluna que quase todo mundo esquece

**`Em linguagem de leigo`**, na fila.

Uma linha por item, com analogia tirada do mundo do dono. Se o dono do projeto
nao e programador, essa coluna e a diferenca entre ele decidir e ele confiar no
escuro.

Exemplo de item tecnico traduzido:

> **Isolamento entre clientes no banco** — e a tranca da porta da sala, nao o
> aviso "por favor nao entre". O aviso depende da boa vontade de quem passa; a
> tranca nao.

A analogia tem de ser **honesta**. Analogia bonita que ensina errado e pior do
que nenhuma: o dono vai decidir com base nela.

---

## Numero de item: a regra que nao se negocia

| Regra | Consequencia de quebrar |
| --- | --- |
| Numero nunca se reaproveita | Recado antigo passa a apontar para o item errado |
| Numero nunca se reatribui | Dois agentes obedecem instrucoes diferentes com o mesmo numero |
| Numero nunca se renumera | Todo historico perde a referencia |
| Trabalho novo recebe numero maior que o ultimo em uso | — |

Quando duas filas divergem, prevalece a que tem **verificacao automatica**, e
os itens da outra entram como numeros novos. Nada se perde, nada se renumera.
