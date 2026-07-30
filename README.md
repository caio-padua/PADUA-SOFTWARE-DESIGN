# PADUA Software Design

**Cartilha de coordenacao entre agentes de inteligencia artificial que
constroem o mesmo software.**

Este repositorio nao abriga projeto nenhum. Ele contem a **cartilha**: o que
cada agente deve fazer, em que ordem, para que o dono do projeto consiga ver o
predio sendo construido em vez de receber recado de tres pedreiros que nao se
falam.

---

## Para quem e

Para o agente. Claude Code, Replit, Dr. Manus, Lovable, OpenClaw ou qualquer
outro: ao entrar num projeto novo, o agente le esta cartilha **antes** da
primeira acao, e monta a coordenacao do jeito descrito aqui.

E para o dono do projeto, que passa a ter um lugar unico para olhar e responder
"em que pe estamos e quem esta fazendo o que".

---

## O problema que a cartilha resolve

Quatro agentes construindo o mesmo sistema sem se ver produzem um resultado
pior do que um agente sozinho.

O motivo e tecnico e pouco conhecido: o `git` protege contra dois agentes
editando a **mesma linha**. Nao protege contra dois agentes editando o **mesmo
assunto** em linhas diferentes. Nesse caso ele aceita os dois lados sem
conflito, sem avisar ninguem, e o defeito aparece so em producao.

Aconteceu quatro vezes num projeto real. A quarta e a mais instrutiva: dois
agentes escreveram, em paralelo, duas filas de trabalho na mesma pasta, com os
**mesmos numeros significando itens diferentes**. Um recado dizendo "comece o
item 11" ficou impossivel de obedecer, porque naquele arquivo o item 11 estava
marcado concluido e aberto ao mesmo tempo.

Coordenacao tambem e um recurso compartilhado. Recurso compartilhado com dois
escritores corrompe em silencio.

---

## As cinco regras

| Nº | Regra | Por que |
| --- | --- | --- |
| 1 | **Um escritor por recurso** | Fila, planilha, configuracao, envio para a nuvem: um dono cada. Os outros pedem pelo recado. |
| 2 | **Numero de item e identidade permanente** | Nunca se reaproveita, reatribui ou renumera. Trabalho novo recebe numero maior que o ultimo em uso. |
| 3 | **Nada se apaga** | Acrescenta-se. O "como estava antes" e o que permite comparar o pedido com a entrega. |
| 3-A | **Capacidade se le, nao se supoe** | Nome de produto nao e capacidade; lista de ferramentas e. Tres erros de arquitetura nasceram de supor. |
| 4 | **Concluido exige prova** | Marca-se concluido citando o identificador do commit e o arquivo tocado. Nunca por prosa, memoria ou intencao. |
| 5 | **O que esta livre e calculado, nao afirmado** | Uma maquina le a cadeia de dependencias e responde quem pode comecar o que. |

A regra 5 e a que devolve o tempo do ser humano. Sem ela, o dono do projeto
vira mensageiro entre telas de agentes que nao se falam.

---

## A cartilha

Leia nesta ordem.

| Arquivo | O que ensina |
| --- | --- |
| [`CARTILHA/00_COLE_ISTO_NO_AGENTE.md`](CARTILHA/00_COLE_ISTO_NO_AGENTE.md) | **Comece aqui.** Tres blocos prontos para colar dentro de qualquer agente, inclusive os que nao instalam plugin |
| [`CARTILHA/01_PASSO_A_PASSO_PROJETO_NOVO.md`](CARTILHA/01_PASSO_A_PASSO_PROJETO_NOVO.md) | O caminho inteiro, numerado, do zero ate o primeiro item em execucao |
| [`CARTILHA/02_QUEM_FAZ_O_QUE.md`](CARTILHA/02_QUEM_FAZ_O_QUE.md) | O que cada agente faz e o que cada um nao toca |
| [`CARTILHA/03_PASTA_NO_DRIVE.md`](CARTILHA/03_PASTA_NO_DRIVE.md) | Como criar a pasta `PROJETO <NOME>`, o que vai dentro e como entregar o link ao dono |
| [`CARTILHA/04_PLANILHA_E_ESPELHO.md`](CARTILHA/04_PLANILHA_E_ESPELHO.md) | Como a planilha e clonada para o repositorio do projeto e como as duas copias nunca divergem |
| [`CARTILHA/05_MODELO_DE_REFERENCIA.md`](CARTILHA/05_MODELO_DE_REFERENCIA.md) | A arquitetura de referencia: o que copiar e o que nao copiar do projeto modelo |
| [`CARTILHA/06_COORDENACAO_NO_SLACK.md`](CARTILHA/06_COORDENACAO_NO_SLACK.md) | Como os agentes se avisam entre si em tempo real, sem o dono no meio |
| [`CARTILHA/07_RITUAL_DE_ENTRADA.md`](CARTILHA/07_RITUAL_DE_ENTRADA.md) | Como um agente novo entra no quadro sem colidir — e como sai |
| [`CARTILHA/08_CONECTORES_E_CAPACIDADE.md`](CARTILHA/08_CONECTORES_E_CAPACIDADE.md) | Ler a lista de ferramentas antes de projetar: tres erros reais e o procedimento |

---

## O que mais tem aqui

| Pasta | Conteudo |
| --- | --- |
| `modelos/` | Modelos em branco dos arquivos de coordenacao, prontos para copiar |
| `scripts/` | Gerador da planilha, gerador do espelho em texto e o conferidor de coerencia |
| `skills/` | Os mesmos procedimentos como comandos do Claude Code |
| `.claude-plugin/` | Metadados para instalar como plugin |

---

## Os quatro arquivos de coordenacao

A cartilha se materializa em quatro arquivos que vivem no repositorio **do
projeto**, nunca numa conversa:

```
docs/COORDENACAO/
  FILA_DE_PRODUCAO.md      <- o que fazer, por quem, em que ordem
  MATRIZ_DA_EQUIPE.md      <- territorio de cada agente e a fronteira
  CAIXA_DE_RECADOS.md      <- aviso entre agentes, append-only
  GLOSSARIO.md             <- toda palavra tecnica, para o dono do projeto
```

O glossario nao e enfeite. Quando o dono do projeto nao e programador, cada
sigla nao explicada e uma decisao que ele nao consegue tomar.

---

## O caminho mais curto: tres blocos para colar

A maioria dos agentes nao instala plugin — Replit, Lovable, Manus e OpenClaw
nao rodam comando do Claude Code. Todos, porem, sabem abrir um endereco na
internet e ler texto. Por isso o uso normal desta cartilha e copiar e colar
um dos tres blocos de [`CARTILHA/00_COLE_ISTO_NO_AGENTE.md`](CARTILHA/00_COLE_ISTO_NO_AGENTE.md):

```
projeto novo
     |
     v
cola o BLOCO A no primeiro agente  ->  ele monta a coordenacao inteira
     |
     v
cola o BLOCO B em cada agente que chega depois
     |
     v
se algum dia aparecerem duas listas  ->  cola o BLOCO C
```

---

## Instalacao como plugin do Claude Code

```
/plugin marketplace add caio-padua/PADUA-SOFTWARE-DESIGN
/plugin install padua-software-design
```

Depois, dentro do projeto novo:

```
/iniciar-projeto
```

---

## Uma advertencia sobre este repositorio ser publico

Esta cartilha e publica de proposito: o metodo tem valor para qualquer pessoa
que coordene varios agentes.

Por isso ela descreve **categorias** de risco — isolamento entre clientes,
senha guardada de dois jeitos, ausencia de teste automatico — e nunca o estado
atual de seguranca de um sistema em producao. Um repositorio publico que
enumera as falhas abertas de um sistema vivo e um mapa para quem quer atacar
aquele sistema.

**Regra para todo agente que escrever aqui:** a licao entra generalizada; o
nome do arquivo vulneravel, a rota exposta e a falha ainda aberta ficam no
repositorio privado do projeto.
