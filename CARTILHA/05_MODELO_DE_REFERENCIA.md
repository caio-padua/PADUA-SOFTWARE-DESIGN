# 05 — O MODELO DE REFERENCIA

> A arquitetura do projeto modelo e o gabarito. Este capitulo diz o que copiar
> dela e o que **nao** copiar.

---

## O que copiar: o formato da coordenacao

| Peca | Copiar sempre |
| --- | --- |
| Fila unica com numero permanente | sim |
| Coluna `Em linguagem de leigo` | sim, se o dono nao programa |
| Matriz com a coluna "nao toca sem avisar" | sim |
| Caixa de recados append-only no repositorio | sim |
| Historico com "como estava / como ficou / prova" | sim |
| Glossario com analogia do mundo do dono | sim |
| Conferidor de coerencia rodando antes de cada tarefa | sim |
| Pasta `PROJETO <NOME>` no Drive com link de pasta | sim |

---

## O que copiar: as prioridades

A escala de prioridade do modelo, que vale para qualquer projeto com cliente
pagante:

| Nivel | Criterio | Exemplo de categoria |
| --- | --- | --- |
| `P0` | Dano **irreversivel** se faltar | Isolamento entre clientes, senha guardada de forma ambigua, ausencia de copia de seguranca |
| `P1` | Destrava produto ou receita | Porta de entrada faltando, dominio, identidade visual errada |
| `P2` | Modelo comercial | Catalogo, precos, medicao de consumo, cobranca |
| `P3` | Divida tecnica e conforto | Teste automatico, renomeacao interna, documentacao |

Regra de corte: **se desfazer e possivel, nao e P0.** P0 inflacionado deixa de
priorizar.

---

## O que NAO copiar

| Nao copie | Por que |
| --- | --- |
| Os itens do projeto modelo | Cada projeto tem os seus. Item copiado sem existir no codigo e fantasia. |
| O estado de seguranca do modelo | Nunca escreva, num repositorio publico, qual falha esta aberta hoje num sistema vivo |
| Os nomes de arquivo internos do modelo | Servem de exemplo de formato, nao de conteudo |
| A lista de agentes | Cada projeto declara os seus na propria matriz |

---

## A licao central do modelo, em uma frase

O `git` protege contra dois agentes editando a mesma **linha**. Nao protege
contra dois agentes editando o mesmo **assunto** em linhas diferentes.

Toda peca desta cartilha existe para cobrir esse buraco, e cada uma delas
nasceu de um incidente real:

| Peca | Incidente que a originou |
| --- | --- |
| Territorio explicito por agente | Duas correcoes no mesmo arquivo de configuracao, aceitas sem conflito, chave duplicada, build quebrado |
| Um escritor por recurso | Duas filas de trabalho escritas em paralelo na mesma pasta |
| Numero de item permanente | Os mesmos numeros significando itens diferentes em duas filas |
| Concluido exige prova | Entrega anunciada em prosa, sem forma de conferir |
| Estado calculado, nao afirmado | Item marcado como travado quando ja estava livre, escondendo trabalho |
| Link de pasta, nao de arquivo | Planilha substituida, identificador antigo morto, link do dono quebrado |
| Conferir data de modificacao antes de subir | Risco de apagar a resposta que so o dono podia dar |

---

## Como saber que a coordenacao esta funcionando

Tres sinais, em ordem de importancia:

```
1  o dono deixou de copiar texto entre telas
2  nenhum agente pergunta "o que eu faco agora"
3  duas entregas seguidas nao colidiram
```

Se o dono ainda e o fio entre os agentes, a coordenacao existe no papel e nao
na pratica.
