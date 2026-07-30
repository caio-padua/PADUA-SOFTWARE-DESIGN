# 08 — CONECTORES E CAPACIDADE

> Este capitulo nasceu de tres erros do MESMO tipo, cometidos na mesma
> madrugada, pelo mesmo agente. O padrao e sempre este:
>
> **afirmar o que uma ferramenta faz sem ler a lista de ferramentas dela.**
>
> Duas vezes o erro foi supor que a ferramenta NAO conseguia. Uma vez foi
> supor que ela CONSEGUIA. O terceiro custou dinheiro e tempo do dono do
> projeto, que instalou um conector inutil para o problema dele.

---

## A regra

```
antes de projetar em cima de uma ferramenta:
    LEIA A LISTA DE FERRAMENTAS DELA
        |
        +-- tem a ferramenta que o passo exige?  ->  projete
        |
        +-- nao tem?                             ->  diga isso, e procure outra
```

Nome de produto nao e capacidade. Descricao de catalogo nao e capacidade.
**Lista de ferramentas e capacidade.**

---

## Os tres erros, para nao repetir

| Nº | O que foi afirmado | A verdade | Custo |
| --- | --- | --- | --- |
| 1 | "Os agentes nao conseguem conversar entre si; todo aviso passa pelo dono" | Todos tinham conector de mensageria | Arquitetura desenhada em volta de limitacao inexistente. Se o dono tivesse acreditado, continuaria sendo o mensageiro |
| 2 | "Este conector de nuvem resolve o DNS do dominio" | O conector expunha armazenamento, banco de borda, funcoes e busca em documentacao. **Nenhuma ferramenta de DNS** | O dono instalou um conector que nao resolvia o problema dele, e quatro itens da fila continuaram travados |
| 3 | "A planilha esta entregue e o dono pode responder" | O arquivo gerado nao abria no leitor de planilha da nuvem | O dono tentou abrir e recebeu erro |

Os tres tem a mesma causa e o mesmo conserto: **conferir na fonte antes de
afirmar.** E a regra mais antiga do metodo, e a mais facil de esquecer quando
se esta com pressa de entregar.

---

## Procedimento antes de recomendar um conector

Um conector nao entra por curiosidade nem por nome bonito. Entra assim:

```
1  qual ITEM da fila esta travado?
2  qual PASSO exato daquele item precisa de automacao?
3  existe conector que expoe FERRAMENTA para aquele passo?
4  LEIA a lista de ferramentas. Nao a descricao: a LISTA.
5  a ferramenta existe?    -> recomende, dizendo qual item destrava
   a ferramenta nao existe? -> diga que nao existe, e nao recomende
6  depois de instalado, CONFIRME lendo a lista de novo antes de prometer
```

O passo 6 e o que faltou no erro numero 2. Instalado nao significa capaz.

---

## O que dizer ao dono do projeto

Ao recomendar:

```
Conector: <nome>
Destrava: item <n> (<o que o item e>)
Ferramenta que faz isso: <nome exato da ferramenta>
O que ele NAO resolve: <a parte que continua manual>
```

A ultima linha e obrigatoria. Conector que resolve metade de um passo e util,
mas prometer o passo inteiro transforma ajuda em retrabalho.

---

## Capacidade nao e binaria

Um conector pode ter a ferramenta e ainda assim nao servir. Confira tambem:

| Pergunta | Exemplo real |
| --- | --- |
| A ferramenta e de leitura ou de escrita? | Um conector de infraestrutura devolvia apenas o NOME das variaveis de ambiente, nunca o valor — leitura sem utilidade para quem precisava do valor |
| O agente tem acesso ao recurso, ou so a conta? | Conector de mensageria ligado nao da acesso ao canal: o aplicativo precisa ser convidado para dentro dele, um por um |
| O escopo cobre o recurso especifico? | Acesso a um repositorio nao e acesso a todos |

---

## Quando NAO instalar

| Nao instale | Por que |
| --- | --- |
| Por curiosidade | Permissao viva e superficie de risco. Um script de envio automatico ja apagou um arquivo do dono sem avisar |
| Porque o nome parece resolver | Nome nao e capacidade |
| Sem um item da fila exigindo | Conector sem uso e permissao parada, e permissao parada e risco parado |
| Com permissao de escrita que nao sera usada esta semana | Escrita nao usada e escrita disponivel para o erro |

**Regra proposta:** conector entra quando um item da fila o exige, e sai
quando o item fecha.

---

## O caso do painel sem interface programavel

Nem todo passo tem conector, e forcar um nao resolve. Alguns paineis nao
oferecem forma programatica de acesso — registradores nacionais de dominio sao
o exemplo classico.

Para esses, o caminho e um agente que **navega na tela**, com o dono olhando.
Nao e gambiarra: e a unica forma honesta quando a automacao nao existe.

Reconhecer isso rapido economiza a busca por um conector que nunca vai
aparecer.

---

## RESUMO EM 1 LINHA

Nome de produto nao e capacidade e descricao de catalogo nao e capacidade: so
a lista de ferramentas e — leia a lista antes de projetar, releia depois de
instalar, e diga sempre em voz alta qual parte do passo continua manual.
