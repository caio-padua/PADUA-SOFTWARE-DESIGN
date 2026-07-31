# -*- coding: utf-8 -*-
"""Confere o dicionario antes de qualquer canal usar.

Roda em um segundo e pega os tres defeitos que matam a repeticao:

  1. termo duplicado          -> dois numeros para a mesma coisa
  2. numero repetido          -> um numero significando duas coisas
  3. buraco na numeracao      -> sinal de que alguem removeu termo em uso

O defeito 1 aconteceu de verdade na primeira geracao: RLS, multi-tenant e
webhook entraram duas vezes. Foi este conferidor que pegou.
"""
import json
import pathlib
import sys
import unicodedata

d = json.loads(
    (pathlib.Path(__file__).parent / "dicionario.json").read_text(encoding="utf-8")
)
termos = d["termos"]
problemas = []


def chave(t):
    x = unicodedata.normalize("NFKD", t)
    return "".join(c for c in x if not unicodedata.combining(c)).lower()


vistos = {}
for t in termos:
    k = chave(t["termo"])
    if k in vistos:
        problemas.append(f"termo duplicado: '{t['termo']}' nos numeros {vistos[k]} e {t['numero']}")
    vistos[k] = t["numero"]

nums = {}
for t in termos:
    n = t["numero"]
    if n in nums:
        problemas.append(f"numero {n} usado por '{nums[n]}' e '{t['termo']}'")
    nums[n] = t["termo"]

esperado = set(range(1, len(termos) + 1))
faltando = sorted(esperado - set(nums))
if faltando:
    problemas.append(f"buraco na numeracao: {faltando} — alguem removeu termo em uso?")

for t in termos:
    for campo in ("termo", "oque_e", "leigo", "serve"):
        if not (t.get(campo) or "").strip():
            problemas.append(f"termo {t['numero']} ({t['termo']}) sem '{campo}'")

if problemas:
    print(f"DEFEITOS ({len(problemas)}):")
    for p in problemas:
        print("  " + p)
    sys.exit(1)

print(f"coerente: {len(termos)} termos, numeracao 1..{len(termos)} sem buraco nem repeticao")
print(f"proximo numero livre: {d['proximo_numero']}")
