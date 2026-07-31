#!/usr/bin/env python3
"""
gerar_md.py — Gera DICIONARIO.md a partir de dicionario.json
Idempotente: rodar duas vezes produz o mesmo arquivo.

Uso:
    python3 dicionario/gerar_md.py
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "dicionario.json")
MD_PATH   = os.path.join(os.path.dirname(BASE_DIR), "DICIONARIO.md")


def escapar_pipe(s: str) -> str:
    return str(s).replace("|", "\\|")


def main() -> None:
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    termos    = sorted(data["termos"], key=lambda t: t["numero"])
    proximo   = data.get("proximo_numero", max(t["numero"] for t in termos) + 1)
    total     = len(termos)

    linhas = [
        "# DICIONÁRIO PADAXOR — Termos Técnicos com Número Permanente",
        "",
        "> **Regra central:** o número é identidade permanente.",
        "> `(*3)` significa *API* hoje e daqui a dois anos. Nunca se reordena, nunca se reaproveita.",
        "> Termo novo entra sempre no final — recebe o próximo número livre.",
        "",
        "## Como ler",
        "",
        "| Coluna | O que contém |",
        "| --- | --- |",
        "| **Nº** | Número permanente. Aparece como `(*N)` nas mensagens do Slack e Telegram. |",
        "| **Termo** | A palavra técnica exata, como aparece no código e nas mensagens. |",
        "| **Tradução** | O que o termo significa formalmente, em português direto. (`oque_e` no JSON) |",
        "| **Analogia Clínica** | A mesma ideia explicada com o mundo da clínica — para o CEO entender. (`leigo` no JSON) |",
        "",
        "## Dicionário completo",
        "",
        "| Nº | Termo | Tradução | Analogia Clínica |",
        "| --- | --- | --- | --- |",
    ]

    for t in termos:
        num     = t["numero"]
        termo   = escapar_pipe(t.get("termo", ""))
        traducao = escapar_pipe(t.get("oque_e", ""))
        analogia = escapar_pipe(t.get("leigo", ""))
        linhas.append(f"| ({num}) | **{termo}** | {traducao} | {analogia} |")

    linhas += [
        "",
        f"*Total: **{total}** termos. Próximo número livre: **{proximo}***",
        "",
        "---",
        "",
        "_Gerado automaticamente por `dicionario/gerar_md.py`._",
        "_Para adicionar termos: edite `dicionario/dicionario.json` e rode este script._",
        "_Nunca edite este arquivo manualmente — as mudanças serão sobrescritas._",
    ]

    conteudo = "\n".join(linhas) + "\n"

    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"✅  DICIONARIO.md gerado: {total} termos | próximo número: {proximo}")
    print(f"    Arquivo: {MD_PATH}")


if __name__ == "__main__":
    main()
