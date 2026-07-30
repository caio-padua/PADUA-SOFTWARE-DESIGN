# 00 — COLE ISTO NO AGENTE

> Este e o arquivo que o DONO DO PROJETO usa. Os outros capitulos sao para o
> agente ler; este e para ser copiado e colado dentro do agente.
>
> Existe porque a maioria dos agentes nao instala plugin: Replit, Lovable,
> Manus e OpenClaw nao rodam comando do Claude Code. Todos, porem, sabem abrir
> um endereco na internet e ler texto. Como esta cartilha e publica, o endereco
> cru funciona para qualquer um deles.

---

## Bloco A — projeto NOVO, ainda sem coordenacao

Cole no primeiro agente do projeto. Um agente so recebe este bloco: e ele que
vira o escritor da fila.

```
ANTES DE ESCREVER UMA LINHA DE CODIGO, LEIA A CARTILHA DE COORDENACAO.

Voce nao esta sozinho neste projeto. Outros agentes de IA vao trabalhar nos
mesmos arquivos que voce, sem falar com voce. Ja aconteceu quatro vezes de
dois agentes consertarem o mesmo arquivo em linhas diferentes, o git aceitar
os dois lados SEM CONFLITO, e o sistema quebrar em producao.

Leia estes cinco enderecos, na ordem, inteiros:

https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/01_PASSO_A_PASSO_PROJETO_NOVO.md
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/02_QUEM_FAZ_O_QUE.md
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/03_PASTA_NO_DRIVE.md
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/04_PLANILHA_E_ESPELHO.md
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/05_MODELO_DE_REFERENCIA.md

Depois execute os 12 passos do capitulo 01, nesta ordem, sem pular:

  1  registre em uma frase o que eu pedi, com as minhas palavras
  2  LEIA O CODIGO deste projeto antes de me perguntar qualquer coisa
  3  pergunte apenas as duas coisas que o codigo nao responde
  4  crie a pasta PROJETO <NOME> no Google Drive
  5  entregue o link DA PASTA para mim (nunca link de arquivo)
  6  crie docs/COORDENACAO/ NESTE repositorio, com os quatro arquivos
  7  gere a planilha e o espelho em texto
  8  suba a planilha para a pasta do Drive
  9  rode o conferidor de coerencia
  10 escreva o primeiro recado dizendo que a fila existe
  11 monte um bloco por agente com o recorte dele
  12 me diga UM proximo passo, nao uma lista

Os modelos em branco dos quatro arquivos estao em:
https://github.com/caio-padua/PADUA-SOFTWARE-DESIGN/tree/main/modelos

Os tres scripts estao em:
https://github.com/caio-padua/PADUA-SOFTWARE-DESIGN/tree/main/scripts

REGRAS QUE VALEM DESDE AGORA, SEM EXCECAO:

  1. Um escritor por recurso. Voce e o escritor da fila neste projeto.
     Os outros agentes escrevem no recado, nao na fila.
  2. Numero de item e identidade permanente. Nunca reaproveite, nunca
     reatribua, nunca renumere. Trabalho novo recebe numero maior que o
     ultimo em uso.
  3. Nada se apaga. Acrescenta-se.
  4. Concluido exige prova: identificador do commit e arquivo tocado.
     Nunca por prosa, memoria ou intencao.
  5. O que esta livre e calculado pelo conferidor, nao afirmado por voce.

NAO ME PERGUNTE o que a fila deve conter. Descubra lendo o projeto.
NAO ME MANDE uma lista de perguntas. Uma por vez, com default recomendado.
NAO ANUNCIE nada como pronto sem o identificador do commit.

RESPONDA, quando terminar, apenas isto:
  - o link da pasta do Drive
  - quantos itens a fila tem e quantos estao livres agora
  - a saida do conferidor de coerencia
  - o UM proximo passo que depende de mim
```

---

## Bloco B — agente ENTRANDO num projeto que ja tem coordenacao

Cole em todo agente que chega depois do primeiro.

```
ESTE PROJETO TEM COORDENACAO ESCRITA. LEIA ANTES DE AGIR.

Outros agentes de IA trabalham nos mesmos arquivos que voce. A coordenacao
nao passa por mim: ela mora no repositorio.

Leia, nesta ordem, dentro deste repositorio:

  1. docs/COORDENACAO/CAIXA_DE_RECADOS.md   <- o que mudou desde a ultima vez
  2. docs/COORDENACAO/MATRIZ_DA_EQUIPE.md   <- o que e seu e o que NAO e
  3. docs/COORDENACAO/FILA_DE_PRODUCAO.md   <- o que fazer, por quem

Depois rode:

  python3 scripts/conferir_coerencia.py

Ele responde quais itens estao livres para VOCE comecar agora.

REGRAS:

  1. Pegue apenas item marcado com o SEU nome e livre. Se nada estiver
     livre, escreva no recado em vez de inventar trabalho.
  2. Achou problema fora do seu territorio? NAO CONSERTE. Escreva no
     recado e siga o seu item. Consertar fora do territorio foi como tres
     colisoes aconteceram.
  3. Ao entregar: mude o Estado do item citando o identificador do commit,
     acrescente linha no historico (como estava, como ficou, por que,
     prova) e escreva no recado o que muda PARA OS OUTROS.
  4. Voce NAO edita a estrutura da fila. Quem edita e o escritor unico,
     nomeado na primeira linha da matriz. Peca pelo recado.
  5. Nada se apaga. Numero de item nunca se reaproveita nem se renumera.

A cartilha completa, se precisar do porque de alguma regra:
https://github.com/caio-padua/PADUA-SOFTWARE-DESIGN

RESPONDA apenas: qual item voce esta comecando, e o numero dele.
```

---

## Bloco C — quando um agente ja bagunçou

Cole quando descobrir duas listas, numeros repetidos ou entrega anunciada sem
prova. Nao acuse: corrija o trilho.

```
PARE E LEIA. HA DUAS VERDADES NESTE PROJETO.

Encontrei mais de uma lista de trabalho, ou o mesmo numero de item
significando coisas diferentes. Isso nao e detalhe: um recado dizendo
"comece o item 11" fica impossivel de obedecer quando o item 11 significa
duas coisas.

O que fazer, nesta ordem:

  1. NAO APAGUE nenhuma das listas. Nada se apaga.
  2. Prevalece a lista que tem verificacao automatica rodando.
  3. Os itens da outra lista entram na que prevalece como numeros NOVOS,
     maiores que o ultimo em uso. Nunca como numeros ja existentes.
  4. Registre o incidente num arquivo datado, dizendo o que colidiu com o
     que. Ele vale mais que a correcao: e o que impede a repeticao.
  5. Rode o conferidor de coerencia e so pare quando sair limpo.
  6. Confirme por escrito quem passa a ser o escritor unico da fila.

Por que numero nao se reatribui, e a cartilha explica em detalhe:
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/04_PLANILHA_E_ESPELHO.md

RESPONDA apenas: quantos numeros estavam duplicados, e quem e o escritor
unico a partir de agora.
```

---

## Bloco D — ligar o agente no canal do Slack

Cole em cada agente DEPOIS de convidar o aplicativo dele para o canal. Sem o
convite, o conector esta ligado mas o agente nao alcanca o canal.

```
VOCE FOI LIGADO AO CANAL DE COORDENACAO DESTE PROJETO.

Canal: #<nome-do-canal>

A partir de agora o aviso entre agentes NAO passa mais pelo dono do projeto.
Voce avisa os outros diretamente no canal.

A VERDADE CONTINUA NO REPOSITORIO. O Slack so avisa que ela mudou. NUNCA
escreva a fila, nem trecho dela, dentro do Slack: seria a terceira copia da
fila, e copia numero tres foi a colisao que originou este metodo.

FORMATO OBRIGATORIO. Quatro tipos, prefixo entre colchetes, nada mais:

  [ITEM <n>] CONCLUIDO — <voce> — commit <identificador>
  Arquivo: <caminho tocado>
  Libera: item <n> (<agente que esperava>)

  [ITEM <n>] TRAVADO — <voce>
  Espera: item <n> (<agente dono da pendencia>)

  [DECISAO <n>] PERGUNTA — <voce> para <dono>
  <a pergunta, uma frase>
  Trava: item <n>

  [RISCO] <voce> encontrou, territorio de <outro agente>
  <o que e, uma frase>
  Sugestao: item novo na fila

Toda mensagem sobre um item vai como RESPOSTA na conversa da primeira
mensagem daquele item. Historico do item fica junto, nao espalhado.

NAO POSTE: "comecei a trabalhar", bom dia, obrigado, a fila inteira, estado
sem identificador de commit.

NUNCA POSTE, em nenhuma circunstancia: senha, token, chave de API, dado de
cliente ou de paciente. Mensagem de Slack fica gravada e e pesquisavel por
qualquer pessoa do espaco de trabalho.

Postar que esta TRAVADO e obrigatorio. Agente parado em silencio parece
agente trabalhando.

O formato completo e o porque de cada regra:
https://raw.githubusercontent.com/caio-padua/PADUA-SOFTWARE-DESIGN/main/CARTILHA/06_COORDENACAO_NO_SLACK.md

CONFIRME agora no canal com UMA linha: seu nome, seu territorio, e o numero
do item que voce esta comecando.
```

---

## Ordem de uso dos quatro blocos

```
projeto novo
     |
     v
BLOCO A  no primeiro agente        ->  ele monta a coordenacao inteira
     |
     v
BLOCO B  em cada agente seguinte   ->  ele le a fila e pega o item dele
     |
     v
BLOCO D  em todos                  ->  eles passam a se avisar sem voce
     |
     v
BLOCO C  se aparecerem duas listas ->  corrige o trilho sem apagar nada
```

Quatro blocos. Nada mais para decorar.

---

## Por que isto funciona com agente que nao e Claude Code

| Agente | Instala plugin | Le endereco na internet | Tem conector de Slack | Bloco que usa |
| --- | --- | --- | --- | --- |
| Claude Code | sim | sim | sim | A ou B, mais D |
| Replit | nao | sim | sim | A ou B, mais D |
| Lovable | nao | sim | sim | B, mais D |
| Manus | nao | sim | sim | A ou B, mais D |
| OpenClaw | nao | sim | conferir | A ou B, mais D |

Antes de declarar que um agente nao consegue algo, CONFIRA se a ferramenta
existe nele. A primeira versao desta cartilha afirmou que os agentes nao
conseguiam conversar entre si; todos tinham conector de Slack. Limitacao
suposta vira arquitetura errada.

E por isso que esta cartilha e publica: endereco cru precisa abrir sem senha
para qualquer agente conseguir ler.
