# -*- coding: utf-8 -*-
"""Marca termos tecnicos com (*n) e monta a legenda da mensagem.

Uma fonte so: dicionario/dicionario.json. Slack, Telegram, e-mail e qualquer
canal futuro IMPORTAM daqui. Nunca reescreva a marcacao no seu canal: duas
implementacoes divergem e o (*24) passa a significar duas coisas.

O NUMERO E PERMANENTE. Foi congelado uma unica vez, em ordem alfabetica, em
31/07/2026. Termo novo entra com numero maior que o ultimo, nunca reordenando.

Por que permanente: o dono do projeto aprende por REPETICAO. Se hash e sempre
(*24), na decima vez ele ja nao olha a legenda. Numero por mensagem — que era
como estava — ensina nada, porque (*1) significa uma coisa hoje e outra amanha.

Uso:
    from anotar import anotar
    texto, legenda = anotar("o commit df4c998 fechou o item")
"""
import json
import pathlib
import re

_DIC = json.loads(
    (pathlib.Path(__file__).parent / "dicionario.json").read_text(encoding="utf-8")
)

# Termo mais longo primeiro: assim "AI Gateway" e casado antes de "API",
# e nao sobra um pedaco marcado no meio do outro.
_TERMOS = sorted(_DIC["termos"], key=lambda t: len(t["termo"]), reverse=True)


def anotar(texto, so_primeira=True):
    """Devolve (texto_marcado, linhas_da_legenda).

    so_primeira=True marca apenas a primeira aparicao de cada termo na
    mensagem. Marcar todas polui: numa frase com tres 'commit' o leitor ve
    (*24) tres vezes e para de ler.

    Na legenda entram SO os termos que apareceram. Legenda com o dicionario
    inteiro ninguem le.
    """
    usados = {}
    resultado = texto

    for t in _TERMOS:
        # \b nao funciona com termo que tem espaco ou underline no meio,
        # entao a fronteira e checada na mao.
        padrao = re.compile(
            r"(?<![\w-])" + re.escape(t["termo"]) + r"(?![\w-])",
            re.IGNORECASE,
        )
        if not padrao.search(resultado):
            continue
        usados[t["numero"]] = t
        marca = f"\\g<0>(*{t['numero']})"
        resultado = padrao.sub(marca, resultado, count=1 if so_primeira else 0)

    legenda = [
        f"(*{n}) {usados[n]['termo']} — {usados[n]['leigo']}"
        for n in sorted(usados)
    ]
    return resultado, legenda


def termo_por_numero(numero):
    """Consulta reversa: o dono do projeto ve (*24) num texto antigo e quer saber."""
    for t in _DIC["termos"]:
        if t["numero"] == numero:
            return t
    return None


def proximo_numero_livre():
    """Numero a usar ao acrescentar termo. Nunca reaproveite numero em uso."""
    return max(t["numero"] for t in _DIC["termos"]) + 1


if __name__ == "__main__":
    exemplo = (
        "O commit df4c998 fechou o item 10. O RLS ainda falta, e sem "
        "empresa_id o multi-tenant nao fecha. O AI Gateway ja conta o consumo, "
        "mas o ledger precisa de dry-run antes."
    )
    texto, legenda = anotar(exemplo)
    print(texto)
    print()
    print("LEGENDA")
    for linha in legenda:
        print("  " + linha)
    print()
    print("total no dicionario:", len(_DIC["termos"]),
          "| proximo livre:", proximo_numero_livre())
