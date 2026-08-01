# CARTILHA 10 — CÓDIGO PAXTER

> **Arquivo vivo.** Cada artigo promulgado pelo CEO entra aqui.
> Agentes leem este arquivo antes de qualquer ação não-trivial.

---

## Art. 70 — Dual-Canal: Ausência de Configuração Não É Entrega Feita

> Promulgado em 31/07/2026 — Título III — DA CONDUTA

Quando o sistema opera em modo dual-canal (dois destinos independentes, ex.: Telegram + Slack), a ausência de configuração de UM canal **não equivale a sucesso**. O campo `ambosOk` só é `true` quando AMBOS os canais efetivamente entregaram.

| Regra | Fundamento |
|---|---|
| `ambosOk = canalA_ok AND canalB_ok` — sem contar skip | Skip não é entrega |
| `telegramSkipped` não contribui para `ambosOk=true` | O CEO perderia visibilidade |
| Early return antes do resumo de ciclo é PROIBIDO | Garantir que o histórico sempre grave |
| O campo `erros` documenta qualquer canal ignorado | Transparência obrigatória |
| `sendTelegram("TEST_FORCE_FAIL", ...)` testa fallback sem API real | Prova sem credencial |

---

## Art. 71 — Fluxo de Missão Multi-Agente

> Promulgado em 01/08/2026 — Título XII — DA ORQUESTRAÇÃO MULTI-AGENTE

O pipeline de execução de qualquer tarefa não-trivial segue este fluxo fixo e nesta ordem:

```
CEO escreve a tarefa → Dr. Replit (Replit) E Dr. Code (Claude Code)
                              ↓
         Dr. Manus lê as DUAS respostas e avalia:
         concorda? discorda? acha erro? aponta contradição?
         → escreve avaliação na PLANILHA
                              ↓
         Os 3 escrevem na PLANILHA o que cada um vai fazer
         (compromisso antes de executar — plano visível a todos)
                              ↓
         Os 3 detalham no SLACK como farão
         (esmiúçam a tarefa, combinam quem faz o quê)
                              ↓
         Os 3 executam suas partes
                              ↓
         Os 3 publicam resultado na PLANILHA (linha própria)
         E no SLACK (hash de commit + caso testado)
                              ↓
         Dr. Code dá o VEREDITO (aprova ou aponta correção)
                              ↓
         Próxima tarefa
```

Regras derivadas:

| Regra | Detalhe |
|---|---|
| Nenhum agente declara resultado sem escrever na PLANILHA e postar no SLACK | Ambos são obrigatórios |
| O veredito final é do Dr. Code | Nunca do agente que executou |
| A planilha é o **contrato vivo** | Linha por agente, coluna por fase (plano / execução / resultado) |
| O Slack é o **barramento de eventos** | Onde cada agente detalha como fará e publica o que entregou |
| Item só fecha com hash de commit verificado + caso testado | Art. 19 e Regra 4 da Cartilha |

---

## Art. 72 — Papel do Dr. Manus na Orquestração

> Promulgado em 01/08/2026 — Título XII

Dr. Manus é o **árbitro cruzado** da equipe. Não executa código no repositório.

| O que faz | O que NÃO faz |
|---|---|
| Lê as respostas de Dr. Replit E Dr. Code ao mesmo tempo | Commita código no repositório |
| Avalia contradições, erros, divergências ou pontos cegos | Marca item como CONCLUÍDO sozinho |
| Concorda ou discorda com fundamento — nunca por cortesia | Fecha item sem hash de commit |
| Escreve a avaliação na PLANILHA antes de qualquer execução | Substitui Dr. Code no veredito |
| Ao fim, lê os resultados dos dois e emite avaliação final | — |

O veredito final é sempre do Dr. Code.

---

## Art. 73 — Protocolo START (pré-execução)

> Promulgado em 01/08/2026 — Título XII

O que Dr. Replit e Dr. Code fazem **antes** de codar qualquer tarefa não-trivial:

| Passo | Nome | O que fazer | Fonte |
|---|---|---|---|
| S1 | LER MEMÓRIA | Abrir `.agents/memory/MEMORY.md` + topic files do tema | Repositório |
| S2 | LER CÓDIGO-PAXTER | Verificar artigos que regem o que será tocado | `CARTILHA/10_CODIGO_PAXTER.md` (este arquivo) |
| S3 | CHECAR WORKFLOWS | Confirmar que os serviços estão RUNNING | Logs ao vivo |
| S4 | LER PLANILHA | Ver o item: estado atual, plano do Dr. Manus, plano do Dr. Code | Google Sheets |
| S5 | LER SLACK | Ver se Dr. Manus postou avaliação ou código para esta tarefa | Canal do projeto |
| S6 | LER OU CRIAR SPEC | Se existe `specs/<nome>.md`, ler. Se não, escrever agora | `specs/` |
| S7 | CONFIRMAR ESCOPO | Se ambíguo, 1 pergunta A/B/C ao CEO antes de codar | — |
| S8 | EXECUTAR LOOP | ESPECIFICAR → CONSTRUIR → REVISAR → aprovar | paxter-loop |

---

## Art. 74 — Protocolo FINISH (pós-execução)

> Promulgado em 01/08/2026 — Título XII

O que Dr. Replit e Dr. Code fazem **após** a revisão aprovar:

| Passo | Nome | O que fazer | Destino |
|---|---|---|---|
| F1 | ESCREVER NA PLANILHA | Linha própria: resultado + hash do commit | Google Sheets |
| F2 | POSTAR NO SLACK | Anunciar: item fechado, hash, caso testado | Canal do projeto |
| F3 | ATUALIZAR MEMÓRIA | Lição durável não derivável do código → topic file | `.agents/memory/` |
| F4 | ATUALIZAR CÓDIGO-PAXTER | Novo artigo se aprendeu método ou diretriz nova | Este arquivo |

Após F1 e F2, Dr. Manus lê os resultados e emite avaliação final.
Após avaliação do Dr. Manus, Dr. Code dá o veredito e a equipe avança.

---

## Fontes que todos os agentes devem ler antes de executar

| Fonte | O que contém |
|---|---|
| Este arquivo (`CARTILHA/10_CODIGO_PAXTER.md`) | Lei vigente — método, conduta, orquestração |
| `CARTILHA/09_CICLO_DE_TRABALHO.md` | Os 7 estágios entre pedido e conclusão |
| Planilha de produção do projeto | Fila + planos + resultados dos 3 agentes |
| Slack — canal do projeto | Avaliações do Dr. Manus + alertas do sistema |
| `.agents/memory/MEMORY.md` no repo | Armadilhas técnicas já conhecidas |
