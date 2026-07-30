---
name: iniciar-projeto
description: Monta a coordenacao entre varios agentes de IA num projeto novo ou num projeto que ja existe e esta sem fila. Cria a fila de producao, a matriz de territorio, a caixa de recados e o glossario. Use quando o usuario for comecar um projeto com mais de um agente, quando disser que os agentes estao se atropelando, ou quando pedir "iniciar projeto", "montar a coordenacao", "criar a fila".
---

# Iniciar a coordenacao de um projeto

Seu trabalho e montar os quatro arquivos de coordenacao e a primeira fila de
trabalho. Nao e escrever codigo do projeto: e montar o trilho por onde os
agentes vao andar sem se atropelar.

## Antes de qualquer coisa: leia o projeto

Nao pergunte ao usuario o que a fila deve conter. Descubra.

1. Leia o `README.md`, o `package.json` (ou equivalente) e a estrutura de pastas.
2. Procure o que esta pela metade: rota sem tela, tela sem rota, tabela sem
   vinculo, variavel de ambiente citada e ausente.
3. Procure o que e risco irreversivel: dado de cliente sem isolamento, senha
   guardada de dois jeitos, ausencia de copia de seguranca.
4. Rode os testes, se existirem. Se nao existirem, isso e um item da fila.

Uma fila montada a partir de perguntas ao usuario nasce com os itens que ele
lembrou. Uma fila montada a partir do codigo nasce com os itens que existem.

## Pergunte apenas o que nao esta no codigo

Duas coisas nao se descobrem lendo o projeto, e so essas duas se perguntam:

1. **Quais agentes trabalham aqui** e em que plataforma cada um vive.
2. **Qual o territorio de cada um** — e, mais importante, o que cada um NAO
   toca sem avisar.

Pergunte uma coisa por vez. Ofereca um default recomendado.

## Os quatro arquivos

Crie em `docs/COORDENACAO/`. Os modelos estao em `modelos/` deste plugin.

### 1. FILA_DE_PRODUCAO.md

Colunas obrigatorias:

| Coluna | Regra |
| --- | --- |
| Nº | Identidade permanente. Nunca se reaproveita, reatribui ou renumera. |
| Item | Titulo curto. Nunca muda depois de escrito. |
| O que e / como sera feito | Concreto: nome de arquivo, nome de tabela, nome de rota. |
| Responsavel | Um agente. Nunca dois. |
| Depende de | Numero de outro item, ou travessao. |
| Estado | `A FAZER`, `AGUARDANDO`, `CONCLUIDO`. Nada mais. |
| Prioridade | `P0` a `P3`. P0 e so o que causa dano irreversivel. |
| Esforco | Estimativa honesta, ou `decisao` quando depende do dono. |
| Em linguagem de leigo | Obrigatoria se o dono do projeto nao e programador. |

Ordene por prioridade, nunca por ordem em que o pedido chegou.

Distinga `A FAZER` de `AGUARDANDO` com rigor: `AGUARDANDO` significa que a
pendencia e de **outro** agente na cadeia, portanto comecar nao depende do
dono do item. Se a pendencia e da propria fila dele, e `A FAZER`.

### 2. MATRIZ_DA_EQUIPE.md

Para cada agente, quatro colunas: onde vive, o que decide sozinho, **o que
nao toca sem avisar**, e a frente atual.

A terceira coluna e a que evita a colisao. As outras tres sao contexto.

### 3. CAIXA_DE_RECADOS.md

Append-only. Recado novo entra no topo, com data, autor e destinatario.

Recado carrega **aviso, risco e pergunta**. Nao carrega estado: estado mora na
fila. Prosa e onde a numeracao errada se esconde.

### 4. GLOSSARIO.md

Cinco colunas: palavra, sinonimos e como aparece, o que e, explicacao leiga
com analogia, e para que serve — esta ultima amarrada a um item real da fila,
para o termo nao ficar abstrato.

Ordem alfabetica, normalizando acento antes de comparar.

## Depois de criar

1. Rode `scripts/conferir_coerencia.py`. Ele tem de sair limpo.
2. Escreva o primeiro recado, dizendo que a fila existe e onde ela esta.
3. Diga ao usuario **um** proximo passo, nao uma lista.

## O que nunca fazer

| Nunca | Por que |
| --- | --- |
| Marcar item como concluido sem identificador de commit | Anunciar sem prova e fantasia, e destroi a confianca na fila inteira |
| Atribuir um item a dois agentes | Recurso com dois donos corrompe em silencio |
| Renumerar para "organizar" | Todo recado antigo que cita numero passa a apontar para o item errado |
| Apagar linha de item cancelado | Marque o estado; o registro do que foi abandonado tem valor |
| Criar uma segunda fila porque a primeira esta em outro lugar | Foi exatamente assim que a quarta colisao aconteceu |

## Verificacao antes de dizer que terminou

- Os quatro arquivos existem e estao no repositorio, nao numa conversa.
- Nenhum numero de item aparece duas vezes.
- Nenhum item marcado `A FAZER` espera pendencia de outro agente.
- Nenhum item marcado `AGUARDANDO` tem a cadeia inteira limpa.
- O conferidor de coerencia sai com codigo zero.
