# Dicionario com numero permanente

Marca termo tecnico com `(*n)` e monta a legenda so com o que apareceu.
Uma fonte, todos os canais: Slack, Telegram, e-mail, relatorio.

## A regra que faz isso funcionar

**O numero e identidade permanente.** `hash` e `(*24)` hoje e daqui a dois anos.

Sem isso o marcador nao ensina nada. Numero por mensagem — que foi a primeira
implementacao — faz `(*1)` significar uma coisa numa mensagem e outra na
seguinte. O dono do projeto nunca aprende, porque nunca repete.

Com numero fixo ele aprende por **repeticao**: na decima vez que vir `(*24)`
ja nao precisa olhar a legenda. Esse e o unico motivo de o numero existir.

## As tres regras

| Regra | Por que |
| --- | --- |
| Numero nunca se reordena | mudaria o significado de todo marcador ja escrito em mensagem antiga |
| Numero nunca se reaproveita | mesmo motivo |
| Termo novo recebe `proximo_numero` | e so incrementa |

## Como usar

```python
from anotar import anotar
texto, legenda = anotar("o commit df4c998 fechou o item")
```

Devolve o texto marcado e as linhas da legenda. So a **primeira** aparicao de
cada termo e marcada — marcar todas polui e o leitor para de ler.

## Antes de publicar qualquer mudanca

```
python3 conferir_dicionario.py
```

Pega termo duplicado, numero repetido e buraco na numeracao. Na primeira
geracao ele pegou tres duplicatas reais: RLS, multi-tenant e webhook.

## Acrescentar termo

1. `proximo_numero` do JSON e o numero dele
2. Preencha os quatro campos: `oque_e`, `leigo`, `serve`, `sinonimos`
3. Incremente `proximo_numero`
4. Rode o conferidor

A analogia do campo `leigo` sai do mundo do dono do projeto — clinica,
prontuario, obra — nunca do mundo da computacao. E tem de ser **honesta**:
analogia bonita que ensina errado e pior que nenhuma, porque ele vai decidir
com base nela.
