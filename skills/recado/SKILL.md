---
name: recado
description: Escreve na caixa de recados do projeto para avisar os outros agentes de uma entrega, um risco encontrado ou uma pergunta. Use depois de entregar um item, ao encontrar um problema que e territorio de outro agente, ou quando o usuario pedir para avisar outro agente.
---

# Escrever na caixa de recados

A caixa de recados existe para o aviso entre agentes deixar de passar pelo ser
humano. Ela vive em `docs/COORDENACAO/CAIXA_DE_RECADOS.md`, dentro do
repositorio, e nao numa conversa.

## Antes de escrever

Pergunte-se se o que voce quer dizer e **estado** ou **aviso**.

| E estado | E aviso |
| --- | --- |
| "Terminei o item 15" | "O item 15 revelou que o rebrand tem uma segunda metade" |
| "O item 12 esta liberado" | "Achei uma rota sem filtro de empresa; e territorio seu" |

Estado vai para a coluna `Estado` da fila, com o identificador do commit.
Aviso vai para o recado. Se voce escrever estado em prosa, a numeracao errada
se esconde ali.

## Formato

```markdown
## Para: <agente> — de: <voce> — <data> <hora> <fuso>

<uma frase dizendo o que mudou para quem le>

- **Item <numero>**: <o que foi feito, com nome de arquivo>
  Prova: commit `<identificador>`
- **Consequencia para voce**: <o que o destinatario pode ou deve fazer agora>

<se houver risco ou pergunta, uma linha para cada>
```

Recado novo entra **no topo**. Nada se apaga.

## Regras que evitam o recado inutil

| Regra | Motivo |
| --- | --- |
| Cite o numero do item, sempre | Recado sem numero obriga o leitor a adivinhar |
| Cite o identificador do commit ao anunciar entrega | Sem prova, e afirmacao |
| Confira o numero na fila antes de citar | Numero citado de memoria e a origem da quarta colisao |
| Diga a consequencia para quem le, nao so o que voce fez | O destinatario quer saber o que muda para ele |
| Um recado por assunto | Recado com tres assuntos e lido pela metade |

## O erro classico

Um recado ja disse "o Dr. Lovable pode comecar o item 12" enquanto, na tabela
logo abaixo do proprio recado, o item 12 pertencia a outra pessoa e era outra
coisa. O autor escreveu o recado numa numeracao e a tabela noutra.

**Antes de citar um numero, abra a fila e confirme o que aquele numero e hoje.**
