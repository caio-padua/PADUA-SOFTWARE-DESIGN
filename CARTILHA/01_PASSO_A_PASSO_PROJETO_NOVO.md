# 01 — PASSO A PASSO DE UM PROJETO NOVO

> Para o AGENTE ler antes da primeira acao. Doze passos, na ordem.
>
> Regra que vale para todos: **o passo nao esta feito enquanto nao houver prova.**
> Prova e identificador de commit, link que abre, ou saida de script.

---

## O caminho inteiro, de relance

```
1  dono pede o projeto
2  agente coordenador le o codigo (nao pergunta o que ja esta escrito)
3  agente pergunta as DUAS coisas que o codigo nao responde
4  cria a pasta PROJETO <NOME> no Drive
5  entrega o link ao dono
6  cria docs/COORDENACAO/ no repositorio do projeto
7  gera a planilha e o espelho em texto
8  sobe a planilha para a pasta do Drive
9  roda o conferidor de coerencia
10 escreve o primeiro recado avisando que a fila existe
11 avisa cada agente do seu primeiro item liberado
12 diz ao dono UM proximo passo, nao uma lista
```

---

## Passo 1 — O dono pede o projeto

Registre em uma frase o que ele pediu, com as palavras dele. Essa frase vira o
titulo do projeto e nunca se reescreve depois: e o "o que foi pedido" com que
todo o resto vai ser comparado.

## Passo 2 — Leia o codigo antes de perguntar qualquer coisa

Nao pergunte ao dono o que a fila deve conter. Descubra.

| Onde olhar | O que procurar |
| --- | --- |
| `README.md`, `package.json` e equivalentes | O que o projeto diz que e |
| Estrutura de pastas | Rota sem tela, tela sem rota, pasta vazia |
| Banco de dados | Tabela sem vinculo, coluna que deveria existir |
| Variaveis de ambiente | Citada no codigo e ausente na configuracao |
| Testes | Existem? Passam? Se nao existem, e um item da fila |

Uma fila montada a partir de perguntas nasce com os itens que o dono lembrou.
Uma fila montada a partir do codigo nasce com os itens que existem.

## Passo 3 — Pergunte apenas as duas coisas que o codigo nao responde

1. **Quais agentes trabalham neste projeto** e em que plataforma cada um vive.
2. **Qual o territorio de cada um** — e principalmente o que cada um NAO toca
   sem avisar.

Uma pergunta por vez, com um default recomendado. Tudo o mais se descobre.

## Passo 4 — Crie a pasta no Drive

Nome exato: `PROJETO <NOME>` em letra maiuscula, sem parentese, espaco simples.

O detalhe de dentro da pasta esta em [`03_PASTA_NO_DRIVE.md`](03_PASTA_NO_DRIVE.md).

## Passo 5 — Entregue o link ao dono

Entregue o link **da pasta**, nao o do arquivo: link de arquivo morre quando o
arquivo e substituido; link de pasta sobrevive.

Diga, em uma linha, o que ele vai encontrar lá e o que ele deve fazer lá.

## Passo 6 — Crie a coordenacao no repositorio do projeto

```
docs/COORDENACAO/
  FILA_DE_PRODUCAO.md
  MATRIZ_DA_EQUIPE.md
  CAIXA_DE_RECADOS.md
  GLOSSARIO.md
```

Copie os modelos da pasta `modelos/` desta cartilha. **No repositorio do
projeto, nunca aqui.** Esta cartilha nao abriga projeto.

## Passo 7 — Gere a planilha e o espelho em texto

Duas copias, uma fonte:

```
scripts/gerar_planilha.py          ->  planilha .xlsx     (para o dono, no Drive)
scripts/gerar_espelho_markdown.py  ->  espelho .md        (para os agentes, no repo)
```

O espelho e **lido da planilha por script**, nunca digitado. Divergiu, alguem
digitou. Detalhe em [`04_PLANILHA_E_ESPELHO.md`](04_PLANILHA_E_ESPELHO.md).

## Passo 8 — Suba a planilha para a pasta do Drive

Um agente so faz isso, sempre o mesmo. Dois agentes subindo arquivo de mesmo
nome para a mesma pasta se sobrescrevem em silencio, e o dono perde o que
escreveu.

**Nunca substitua a planilha enquanto o dono estiver com ela aberta
respondendo.** Confira antes se a data de modificacao e diferente da data de
criacao: se for, ele ja escreveu ali, e sobrescrever apaga a resposta dele.

## Passo 9 — Rode o conferidor de coerencia

```
python3 scripts/conferir_coerencia.py
```

Tem de sair com codigo zero. Ele pega os tres defeitos que a leitura humana
nao pega:

| Defeito | Consequencia se passar |
| --- | --- |
| Numero de item repetido | Recado citando aquele numero fica impossivel de obedecer |
| Item `A FAZER` que espera outro agente | O dono comeca e colide |
| Item `AGUARDANDO` com a cadeia limpa | Esconde trabalho livre; um agente fica parado sem motivo |

## Passo 10 — Escreva o primeiro recado

Diga que a fila existe, onde ela esta, e que ela e a unica. Se havia outra
lista antes, diga qual prevalece e por que — sem apagar a antiga.

## Passo 11 — Avise cada agente do seu primeiro item liberado

Um bloco por agente, pronto para colar, com:

- o territorio dele e o que ele nao toca
- os itens dele que estao **livres agora**
- os itens dele que estao travados, e por quem
- o que ele deve responder

Nao mande a fila inteira para cada um: mande o recorte dele. Fila inteira e
lida pela metade.

## Passo 12 — Diga ao dono um proximo passo

Um. Nao uma lista. Se ha dez decisoes pendentes, escolha a que destrava mais
itens e apresente so ela.

---

## Ao terminar, confira

- [ ] A pasta do Drive existe e o dono tem o link **da pasta**
- [ ] Os quatro arquivos estao no repositorio do projeto
- [ ] A planilha e o espelho batem, conferido por contagem
- [ ] O conferidor sai com codigo zero
- [ ] Nenhum numero de item aparece duas vezes
- [ ] Cada agente recebeu o recorte dele
- [ ] O dono recebeu **um** passo
