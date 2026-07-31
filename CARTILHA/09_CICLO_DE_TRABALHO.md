# 09 — O CICLO DE TRABALHO EM SETE ESTAGIOS

> Desenhado pelo dono do projeto em 30/07/2026. Um item NUNCA vai do pedido
> direto a producao.
>
> O estagio que quase todo time pula e o 5, e e o que mais paga: **quem
> escreve nao confere**.

---

## O ciclo

```
1  ARQUITETURA    um agente propoe o desenho, ESCRITO
        |
2  VIABILIDADE    os outros dizem o que quebra na pratica
        |
3  CONSENSO       divergencia resolvida por escrito, com o motivo
        |
4  PRODUCAO       UM escreve. Um so
        |
5  CONFERENCIA    OUTRO agente confere. Nunca o que escreveu
        |
6  CORRECAO       volta ao 4 se falhou. Sem vergonha
        |
7  CONCLUSAO      estado muda na fila, citando o identificador do commit
```

---

## Estagio a estagio

### 1 — ARQUITETURA

O desenho vira arquivo antes de virar codigo. Conversa se perde; arquivo fica.

O documento traz: o que sera feito, o que NAO sera, de que depende, e as
decisoes ja tomadas **com o motivo de cada uma**. O motivo importa mais que a
decisao: sem ele o proximo agente nao sabe se pode mudar.

### 2 — VIABILIDADE

Os outros agentes atacam o desenho. Nao para concordar: para achar o que
quebra na pratica.

Peca explicitamente:

```
a) O que falta neste desenho que voce ja sentiu falta na pratica?
b) Alguma decisao esta errada? Qual, e por que?
c) Tem peca que da para gerar sozinho e nao foi listada?
d) O que voce faria diferente?
```

**Discordancia com fundamento vale mais que concordancia.** Num caso real, o
revisor achou uma falha de idempotencia que o autor nao tinha visto — o script
sobrescreveria em silencio na segunda rodada.

### 3 — CONSENSO

Divergencia se resolve por escrito, dizendo o que entra, o que nao entra, **e
por que**. Quem propos o que foi recusado precisa ler o motivo, nao so o "nao".

Aceitar tudo nao e consenso: e ausencia de revisao.

### 4 — PRODUCAO

**Um agente escreve.** Dois escrevendo o mesmo assunto e a origem de toda
colisao — o controle de versao aceita os dois lados sem apontar conflito
quando eles editam linhas diferentes do mesmo problema.

### 5 — CONFERENCIA — o estagio que quase todo mundo pula

**Quem escreveu nao confere.** Nunca.

Nao e desconfianca: e que o autor le o que quis escrever, nao o que escreveu.

O conferidor checa tres coisas, nesta ordem, e **nao** a beleza do codigo:

| Confere | Por que primeiro |
| --- | --- |
| Citou o identificador do commit, e ele existe? | sem prova nao e entrega, e afirmacao |
| Mudou o estado na fila, ou so avisou em prosa? | prosa e onde o numero errado se esconde |
| Respeitou o territorio, ou "aproveitou para arrumar"? | foi assim que tres colisoes nasceram |

Evidencia real do valor deste estagio, num unico projeto e numa unica noite:

- o autor ia corrigir um item; o revisor ja tinha resolvido melhor
- o revisor achou uma falha de idempotencia que o autor nao viu
- o autor achou que a guarda de um endpoint protegia; ela checava uma variavel
  que o proprio guardado controla
- o conferidor automatico do dicionario pegou tres termos duplicados **do
  proprio autor do conferidor**

Quatro achados que uma cabeca sozinha nao teve.

### 6 — CORRECAO

Volta ao estagio 4. Sem drama e sem justificativa longa: corrige e segue.

Registra-se no historico o que estava e o que ficou — nao para culpar, mas
porque o "como estava antes" e o unico jeito de comparar o pedido com a
entrega.

### 7 — CONCLUSAO

Estado muda na fila **citando o identificador do commit**. Se o identificador
nao existe no ramo principal, o item nao esta concluido — por mais que funcione
na maquina de quem escreveu.

Construido no ambiente local e rascunho. Publicado e entrega.

---

## Quando pular estagios

Item pequeno e reversivel pode ir do 1 ao 7 em minutos, com os estagios 2 e 3
resumidos a uma linha no recado.

**O estagio 5 nunca se pula.** Nem em item pequeno, nem com pressa, nem quando
"e obvio". Foi sempre no obvio que passou.

---

## A camada de comunicacao que sustenta o ciclo

O ciclo so funciona se o dono do projeto conseguir acompanhar sem perguntar.
Quatro pecas, e cada uma tem um lugar so:

| Peca | Onde vive | Guarda o que |
| --- | --- | --- |
| **A fila** | repositorio | a verdade: o que fazer, por quem, em que estado |
| **O recado** | canal de mensagem | o aviso de que algo mudou |
| **O dicionario** | repositorio, `dicionario/` | o significado dos termos, com numero permanente |
| **O historico** | banco ou arquivo datado | todo relatorio ja enviado, para consulta |

### Regras da camada

1. **A verdade mora no repositorio.** O canal so avisa que ela mudou. Fila
   dentro do canal e a copia numero tres, e copia tres foi a colisao que
   originou este metodo.

2. **O relatorio le da FILA, nunca da planilha do dono.** Ele edita a planilha;
   ler de la faria o robo avisa-lo de coisa que ele mesmo escreveu.

3. **So posta se algo mudou.** Aviso periodico que as vezes diz "nada novo"
   vira ruido, e em dois dias ninguem le. Ai o canal morre.

4. **Grava o historico no `finally`.** O registro acontece mesmo se o envio
   falhar. Relatorio que nao chegou ainda assim existiu.

5. **Dois canais, um dicionario.** Mensageria e correio podem ser dois; a
   tabela de termos e uma so, importada. Dois dicionarios fazem o mesmo
   marcador significar duas coisas — e ai a ferramenta feita para ensinar
   passa a ensinar errado.

6. **Numero de termo e permanente**, igual a numero de item. E o que permite
   aprender por repeticao: na decima vez o leitor ja nao olha a legenda.

### Formato da mensagem

```
[<PROJETO> — HHhMM]  N itens andaram

ITEM <n> — <titulo>
  <estado antigo> -> <estado novo>   <agente>   commit(*n) <hash>
  EM MIUDOS: <uma frase da coluna "em linguagem de leigo" da fila>

TRAVADO HA MAIS DE 24H
  Item <n> — espera <quem>

LEGENDA
  (*n) <termo> — <analogia curta>
```

Na legenda entram **so** os termos que apareceram. Legenda com o dicionario
inteiro ninguem le.

Marca-se apenas a **primeira** aparicao de cada termo: tres marcadores iguais
na mesma frase poluem e o leitor para de ler.

### Postar na hora, sem esperar o ciclo

- item P0 mudou de estado
- dois agentes tocaram o mesmo arquivo
- algo travou esperando decisao do dono

### Nunca postar

Segredo, chave, token. Dado de cliente ou paciente. A fila inteira. Estado sem
identificador de commit. Mensagem confirmando que o robo rodou.

---

## RESUMO EM 1 LINHA

Sete estagios entre o pedido e a conclusao, com quem escreve nunca conferindo
o proprio trabalho — o unico estagio que nao se pula — sustentados por quatro
pecas de comunicacao em que a verdade mora no repositorio, o canal so avisa, o
dicionario tem numero permanente e o historico se grava mesmo quando o envio
falha.
