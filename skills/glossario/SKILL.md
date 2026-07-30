---
name: glossario
description: Acrescenta uma palavra tecnica ao glossario do projeto, em ordem alfabetica, com explicacao para quem nao e programador. Use quando usar um termo tecnico novo com o usuario, quando ele perguntar o que uma palavra significa, ou quando ele pedir para acrescentar algo ao glossario.
---

# Acrescentar palavra ao glossario

O glossario existe porque o dono do projeto decide, e nao se decide sobre o que
nao se entende. Cada sigla nao explicada e uma decisao que ele nao consegue
tomar.

## Quando acrescentar, sem esperar pedido

Toda vez que voce usar um termo tecnico com o usuario pela primeira vez. Nao
espere ele perguntar: quem pergunta o significado de uma palavra ja perdeu
tempo, e quem nao pergunta finge que entendeu.

## As cinco colunas

| Coluna | Como preencher |
| --- | --- |
| Palavra | O termo como ele aparece na pratica |
| Sinonimos e como aparece | Os outros nomes da mesma coisa, inclusive a sigla e o jargao |
| O que e | Uma frase tecnica, correta, sem analogia |
| Em linguagem de leigo, com analogia | A analogia. Tire do mundo do usuario, nao do mundo da computacao |
| Para que serve | Amarre a um item real da fila. Termo sem uso concreto nao gruda |

## Como escolher a analogia

Tire do mundo real do usuario. Se ele e medico, use clinica, prontuario,
exame, receita. Se e advogado, use processo, peticao, prazo.

Exemplos que funcionaram com um usuario medico:

| Termo | Analogia usada |
| --- | --- |
| hash | Impressao digital de um documento: unica, e nao bate mais se o documento foi adulterado |
| RLS | A tranca da porta, nao o aviso "por favor nao entre". O aviso depende da boa vontade; a tranca nao |
| append-only | O prontuario: nao se apaga a evolucao de ontem, escreve-se a de hoje embaixo |
| idempotente | O botao do elevador: apertar dez vezes nao chama dez elevadores |
| token | A pulseira do hospital: identifica-se uma vez na recepcao e depois so mostra a pulseira |
| mock | O manequim de treinamento: serve para ensaiar, e e perigoso se alguem tratar como paciente |

A analogia tem de ser **honesta**. Analogia bonita que ensina errado e pior do
que nenhuma: o usuario vai decidir com base nela.

## Ordem alfabetica

Normalize o acento antes de comparar, senao a palavra acentuada cai no fim da
lista — o computador ordena pelo numero interno da letra, e letra acentuada tem
numero alto.

Nunca mantenha a ordem a mao: ela desanda na terceira insercao. Deixe o script
ordenar.
