# 06 — COORDENACAO NO SLACK

> Este capitulo existe porque uma premissa anterior estava errada.
>
> A primeira versao desta cartilha afirmava que os agentes nao conseguiam
> conversar entre si, e que qualquer aviso teria de passar pelo dono do
> projeto. Isso era falso: quando TODOS os agentes tem conector de Slack, o
> Slack passa a ser o canal direto entre eles, e o dono sai do meio.
>
> A licao vale mais que a correcao: **antes de declarar uma limitacao,
> pergunte se a ferramenta existe.** Limitacao suposta vira arquitetura
> errada.

---

## O papel do Slack, e o que ele NAO e

| O Slack e | O Slack NAO e |
| --- | --- |
| A caixa de recados em tempo real entre agentes | A fila de trabalho |
| O lugar onde o dono ve a obra andando pelo celular | A fonte de verdade de nada |
| O canal de pergunta ao dono quando algo trava | Lugar de guardar decisao |

**Regra que nao se negocia:** a verdade mora no repositorio. O Slack apenas
avisa que ela mudou. Fila dentro do Slack seria a terceira copia da fila — e
copia numero tres foi exatamente a colisao que originou esta cartilha.

---

## O desenho

```
        repositorio do projeto  =  A VERDADE
        (fila, matriz, historico, glossario)
                    |
      cada agente le antes de agir, escreve depois
                    |
                    v
        canal unico no Slack  =  O AVISO
                    |
        +-----------+-----------+
        v           v           v
   Dr. Replit   Dr. Lovable   Dr. Manus   ...
                    |
                    v
            o dono, no celular
        (le, decide o que e dele, responde)
```

Um canal so por projeto. Nao um por agente, nao um por assunto. Canal por
agente recria o problema: o aviso deixa de ser visto por quem precisava ver.

---

## O formato da mensagem

Mensagem de agente no canal tem prefixo entre colchetes. O prefixo e o que
permite achar, filtrar e nao confundir aviso com conversa.

Quatro tipos, e nada mais:

### Entrega

```
[ITEM 37] CONCLUIDO — <agente> — commit <identificador>
Arquivo: <caminho do arquivo tocado>
Libera: item <numero> (<agente que estava esperando>)
```

Sem o identificador do commit, nao e entrega: e afirmacao. Nao poste.

### Travado

```
[ITEM 18] TRAVADO — <agente>
Espera: item <numero> (<agente dono da pendencia>)
```

Postar que esta travado e obrigatorio. Agente parado em silencio parece
agente trabalhando.

### Pergunta ao dono

```
[DECISAO <numero>] PERGUNTA — <agente> para <dono>
<a pergunta, em uma frase>
Trava: item <numero>
```

Uma pergunta por mensagem. Bateria de perguntas nao e respondida.

### Risco encontrado fora do proprio territorio

```
[RISCO] <agente> encontrou, territorio de <outro agente>
<o que e, em uma frase>
Sugestao: item novo na fila
```

Nao conserte o que e de outro. Poste e siga o seu.

---

## Uma conversa por item

Toda mensagem sobre o item 37 vai como resposta na mesma conversa da primeira
mensagem sobre o item 37. Assim o historico do item fica junto, e nao
espalhado por trezentas mensagens do canal.

---

## O que NAO se posta

| Nao poste | Por que |
| --- | --- |
| "Comecei a trabalhar" | Ninguem precisa. Poste quando terminar ou travar |
| Bom dia, obrigado, entendido | Canal de aviso enche e deixa de ser lido |
| A fila inteira, ou trechos dela | A fila esta no repositorio. Cite o numero |
| Estado sem identificador de commit | Anunciar sem prova destroi a confianca no canal |
| Segredo, senha, token, chave de API | Nunca, em nenhuma circunstancia, em nenhum canal |
| Dado de cliente ou de paciente | Canal de trabalho nao e lugar de dado pessoal |

As duas ultimas linhas nao sao estilo: sao seguranca. Mensagem de Slack fica
gravada, e e pesquisavel por qualquer pessoa do espaco de trabalho.

---

## O que o dono faz no canal

| Ele faz | Ele deixou de fazer |
| --- | --- |
| Le no celular quando quiser | Abrir a tela de cada agente, uma por uma |
| Responde `[DECISAO]` quando aparecer | Copiar texto entre telas |
| Interrompe se algo esta indo para o lado errado | Lembrar quem estava fazendo o que |

Se o dono ainda precisa levar recado de um agente para outro, o canal existe
no papel e nao na pratica.

---

## Resumo diario

Um agente, sempre o mesmo — o escritor da fila — posta uma vez por dia:

```
[RESUMO <data>]
Andaram: item <n>, item <n>
Travados: item <n> (espera <agente>), item <n> (espera decisao <n>)
Livres agora: <agente> tem <n> e <n> | <agente> tem <n>
Decisao mais urgente para o dono: <numero e uma frase>
```

Os numeros vem do conferidor de coerencia, nunca de memoria.

---

## Como ligar um agente no canal

```
Passo A  ->  o dono cria UM canal para o projeto
Passo B  ->  o dono liga o conector de Slack em cada agente
Passo C  ->  o dono convida o aplicativo de cada agente para o canal
Passo D  ->  o dono cola o bloco do capitulo 00 em cada agente
Passo E  ->  cada agente confirma no canal com uma mensagem de uma linha
```

O passo C e o que quase sempre falta. Conector ligado nao significa acesso ao
canal: o aplicativo precisa ser convidado para dentro dele, um por um.

---

## O erro que este capitulo evita

Sem formato acordado, o canal vira conversa. Conversa nao se filtra, nao se
audita e nao se obedece: e nela que o numero errado se esconde, exatamente
como aconteceu quando um recado citou um item usando uma numeracao e a tabela
logo abaixo usava outra.

Prefixo entre colchetes, quatro tipos, uma conversa por item, prova sempre. O
canal deixa de ser bate-papo e passa a ser instrumento.
