# 07 — RITUAL DE ENTRADA DE UM AGENTE NOVO

> O momento em que um agente novo entra e o de **maior risco de colisao** de
> todo o projeto: ele nao conhece o territorio de ninguem, e a boa vontade
> dele e justamente o que faz estrago.
>
> Este capitulo existe para que entrar seja um procedimento, e nao uma
> apresentacao.

---

## Os sete passos, na ordem

```
1  o dono decide que o agente entra           (so ele decide)
2  o agente LE a cartilha                     (blocos B e D)
3  o agente DECLARA o que consegue fazer      (nao se supoe)
4  o escritor da fila desenha o territorio    (para nao sobrepor ninguem)
5  o dono convida o aplicativo no canal       (o passo que sempre falta)
6  o agente confirma no canal, em uma linha
7  primeiro item: pequeno e reversivel        (nunca um P0)
```

---

## Passo 1 — Quem decide a entrada

**So o dono do projeto.** Nenhum agente convida outro agente. Entrada de
membro novo muda o desenho da equipe, e isso nasce do dono.

## Passo 2 — O agente le antes de agir

Blocos B e D do [capitulo 00](00_COLE_ISTO_NO_AGENTE.md). Nao explique a
cartilha por conversa: mande ele ler. Explicacao verbal se perde; arquivo lido
fica.

## Passo 3 — O agente DECLARA a capacidade. Ninguem supoe.

Este passo existe por causa de um erro real e caro.

Um agente coordenador declarou que os outros agentes **nao conseguiam
conversar entre si**, e desenhou a coordenacao inteira em volta dessa
limitacao. Todos tinham conector de mensageria. A limitacao foi **suposta**, e
nunca verificada. Limitacao suposta vira arquitetura errada.

Pergunte ao agente novo, e exija resposta por escrito:

| Pergunta | Por que importa |
| --- | --- |
| Consegue ler um endereco cru na internet? | Define se ele le a cartilha sozinho ou precisa de texto colado |
| Consegue escrever no repositorio, ou so ler? | Define se ele commita ou entrega na doca |
| Tem conector de mensageria para o canal do projeto? | Define se ele avisa os outros ou depende do dono |
| Consegue rodar comando e ver a saida? | Define se ele mesmo confere a coerencia da fila |
| Tem acesso a nuvem de arquivos do dono? | Define quem sobe a planilha |
| Consegue instalar plugin ou habilidade? | Define se usa comando ou bloco colado |

Nao aceite "acho que sim". Peca demonstracao: se ele diz que le endereco cru,
mande ler um e devolver a primeira linha.

## Passo 4 — O territorio se desenha para NAO sobrepor

Quem desenha e o escritor unico da fila. A regra e uma:

> **Territorio novo se recorta do que ninguem tem, nunca do que alguem ja tem.**

Se o agente novo faz algo que outro ja faz, uma de duas coisas tem de ficar
explicita:

| Situacao | Solucao |
| --- | --- |
| Os dois fazem a mesma coisa | Um dos dois perde aquele territorio, por escrito, na matriz |
| O novo produz e outro publica | Modelo de doca: o novo entrega arquivo, o dono do territorio commita |

O modelo de doca resolve quase todo caso e evita disputa: quem produz nao
publica, quem publica nao produz.

Escreva na matriz, numa linha de **VAGA** ja existente. E preencha as quatro
colunas, principalmente a terceira: **o que ele NAO toca sem avisar.**

### Sobre as linhas de vaga

Mantenha linhas de vaga com rotulo (`VAGA 1 — a definir`), nunca em branco de
verdade. Motivo tecnico: os scripts leem a matriz varrendo ate a primeira
celula vazia, e uma linha em branco no meio cortaria em silencio tudo o que
vem abaixo dela.

## Passo 5 — Convidar o aplicativo para dentro do canal

Conector ligado **nao** significa acesso ao canal. O aplicativo do agente
precisa ser convidado, um por um, para dentro do canal do projeto.

E o passo que mais falta, e o sintoma engana: o agente diz que esta conectado,
tenta postar, e nada aparece.

## Passo 6 — A confirmacao de uma linha

O agente novo posta no canal:

```
[ENTRADA] <nome> — <plataforma>
Territorio: <o que e meu>
Nao toco: <o que nao e meu>
Comecando: item <numero>
```

Se ele nao consegue postar isso, o passo 5 nao foi feito. Nao siga.

## Passo 7 — O primeiro item e pequeno e reversivel

**Nunca de um item P0 a um agente que acabou de entrar.**

O primeiro item nao serve para produzir: serve para ver se ele segue o
protocolo. Escolha algo com estas tres marcas:

| Marca | Por que |
| --- | --- |
| Reversivel | Se ele errar, desfaz-se sem dano |
| Escopo fechado | Nao precisa negociar fronteira no primeiro dia |
| Verificavel | Da para conferir a entrega sem depender da palavra dele |

Confira, na primeira entrega dele, tres coisas — e nao a qualidade do codigo:

```
1  citou o identificador do commit?
2  mudou o estado do item na fila, ou so avisou em prosa?
3  respeitou o territorio, ou "aproveitou para arrumar" o que nao era dele?
```

Errar as tres na primeira entrega nao e falta de talento: e falta de leitura
da cartilha. Mande ler de novo antes do segundo item.

---

## O que NUNCA fazer ao receber um agente novo

| Nunca | Consequencia |
| --- | --- |
| Deixar entrar sem territorio escrito | Ele conserta o que nao e dele com a melhor das intencoes |
| Supor o que ele consegue fazer | Arquitetura desenhada em cima de limitacao inexistente |
| Dar um P0 de primeira | O item mais critico do projeto na mao de quem nao conhece a casa |
| Deixar dois agentes com o mesmo territorio | Recurso com dois donos corrompe em silencio |
| Pular o convite ao canal | Ele fica invisivel e ninguem entende por que |
| Explicar a cartilha por conversa | Conversa se perde. Arquivo lido fica |

---

## Quando um agente SAI

Sair tambem e ritual, e mais curto:

```
1  o dono decide a saida
2  os itens dele voltam para a fila como A FAZER, com dono novo
3  a linha dele na matriz NAO se apaga: marca-se "saiu em <data>"
4  linha no historico: quem saiu, quando, e para quem foram os itens
5  o aplicativo dele sai do canal
```

A linha na matriz nao se apaga porque o historico do projeto cita o nome dele.
Apagar quebra a leitura de tudo o que ele entregou.

---

## RESUMO EM 1 LINHA

Agente novo entra por procedimento e nao por apresentacao: o dono decide, o
agente le e **declara** o que consegue fazer, o territorio se recorta do que
ninguem tem, o aplicativo e convidado ao canal, e o primeiro item e pequeno e
reversivel — porque a primeira entrega serve para testar o protocolo, nao o
talento.
