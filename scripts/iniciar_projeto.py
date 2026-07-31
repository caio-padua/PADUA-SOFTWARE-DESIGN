# -*- coding: utf-8 -*-
"""Monta a coordenacao de um projeto novo a partir de projeto.yaml.

    python3 scripts/iniciar_projeto.py --validate    so confere o formulario
    python3 scripts/iniciar_projeto.py --dry-run     mostra o que SERIA criado
    python3 scripts/iniciar_projeto.py               cria

Tres modos porque tocar arquivo sem ver antes ja custou caro neste metodo:
--validate antes de dormir, --dry-run na reuniao, o comando limpo so quando
tudo estiver verde. E o Art. 58 da Biblia virando ferramenta.

O QUE ELE GERA

    docs/COORDENACAO/FILA_DE_PRODUCAO.md    a fila, com o cabecalho certo
    docs/COORDENACAO/MATRIZ_DA_EQUIPE.md    ja preenchida com os agentes
    docs/COORDENACAO/CAIXA_DE_RECADOS.md    vazia, com o formato pronto
    docs/COORDENACAO/GLOSSARIO.md           os 47 termos com numero permanente
    docs/COORDENACAO/BLOCOS_PARA_COLAR.md   A, B, C e D com os nomes trocados
    docs/COORDENACAO/FALTA_CONFIGURAR.md    o que so o dono pode fazer
    .env.example                            nomes de variavel, nunca valores
    .gitignore                              com as regras de segredo

O QUE ELE NAO FAZ, E E DE PROPOSITO

    nao cria pasta na nuvem       exige login humano
    nao cria canal de mensagem    idem
    nao gera chave de API         chave gerada por programa vaza por programa

Para essas tres ele escreve FALTA_CONFIGURAR.md, numerado e dizendo o que
cada uma destrava. Conector que resolve metade de um passo e util; prometer o
passo inteiro transforma ajuda em retrabalho.
"""
import argparse
import json
import pathlib
import sys
from datetime import date

try:
    import yaml
except ImportError:
    print("falta a biblioteca pyyaml. Instale com: pip install pyyaml")
    sys.exit(1)

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = pathlib.Path("docs/COORDENACAO")
SCHEMA_SUPORTADO = 1
ESTADOS = ("A FAZER", "AGUARDANDO", "CONCLUIDO")


# ============================================================ VALIDACAO
def validar(cfg):
    """Devolve lista de problemas. Vazia = formulario bom.

    Falha cedo e por escrito: formulario errado descoberto depois de gerar
    dez arquivos custa mais que a checagem.
    """
    p = []

    v = cfg.get("schema_version")
    if v is None:
        p.append("falta schema_version — sem ele o script nao sabe ler formulario antigo")
    elif v != SCHEMA_SUPORTADO:
        p.append(f"schema_version {v} nao suportado (este script le a {SCHEMA_SUPORTADO})")

    for campo in ("empresa", "projeto", "dono", "canal_mensagem"):
        if not str(cfg.get(campo, "")).strip():
            p.append(f"campo '{campo}' vazio")
        elif str(cfg.get(campo)).strip().upper().startswith("NOME D"):
            p.append(f"campo '{campo}' ainda esta com o texto de exemplo")

    pasta = str(cfg.get("pasta_drive", ""))
    if "COLE-AQUI" in pasta or not pasta.strip():
        p.append("pasta_drive nao preenchida")
    elif "/file/d/" in pasta:
        p.append("pasta_drive aponta para um ARQUIVO, nao para uma pasta — "
                 "link de arquivo morre quando o arquivo e substituido")

    conflito = cfg.get("on_conflict", "skip")
    if conflito not in ("skip", "overwrite", "abort"):
        p.append(f"on_conflict '{conflito}' invalido (skip, overwrite ou abort)")

    agentes = cfg.get("agentes") or []
    if not agentes:
        p.append("nenhum agente declarado")

    escritores = [a for a in agentes if a.get("escritor_da_fila")]
    if len(escritores) == 0:
        p.append("nenhum agente com escritor_da_fila: true — a fila precisa de UM dono")
    elif len(escritores) > 1:
        nomes = ", ".join(a.get("nome", "?") for a in escritores)
        p.append(f"mais de um escritor_da_fila ({nomes}) — recurso com dois "
                 "escritores corrompe em silencio")

    vistos = set()
    for i, a in enumerate(agentes, 1):
        for campo in ("nome", "plataforma", "territorio", "nao_toca"):
            if not str(a.get(campo, "")).strip():
                p.append(f"agente {i} sem '{campo}'"
                         + (" — e a coluna que evita a colisao" if campo == "nao_toca" else ""))
        nome = str(a.get("nome", "")).strip().lower()
        if nome and nome in vistos:
            p.append(f"agente '{a.get('nome')}' declarado duas vezes")
        vistos.add(nome)

    for c in cfg.get("chaves_necessarias") or []:
        valor = str(c.get("valor", "")) if isinstance(c, dict) else ""
        if valor:
            p.append(f"chave '{c.get('nome')}' tem VALOR no formulario. "
                     "Nunca. So o nome da variavel — o valor vai no cofre de segredos")
    return p


# ============================================================ GERADORES
def cab(cfg, titulo, subtitulo):
    return (f"# {titulo} — {cfg['projeto']}\n\n> {subtitulo}\n>\n"
            f"> Gerado por PADUA Software Design em {date.today().strftime('%d/%m/%Y')}.\n"
            f"> Empresa: {cfg['empresa']} · Dono: {cfg['dono']}\n\n---\n\n")


def gerar_fila(cfg):
    t = cab(cfg, "FILA DE PRODUCAO",
            "Fila unica. Ordenada por PRIORIDADE, nunca por ordem de pedido.")
    t += ("`P0` e so o que causa dano irreversivel. Se desfazer e possivel, nao e P0 —\n"
          "P0 inflacionado deixa de priorizar.\n\n"
          "| Nº | Item | O que e / como sera feito | Responsavel | Depende de | "
          "Estado | Prioridade | Esforco | Em linguagem de leigo |\n"
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")
    escritor = next((a["nome"] for a in cfg["agentes"] if a.get("escritor_da_fila")),
                    cfg["agentes"][0]["nome"])
    t += (f"| 1 | Ler o codigo e preencher esta fila | O escritor da fila le o projeto "
          f"inteiro e substitui esta linha pelos itens reais. | {escritor} | — | A FAZER | "
          f"P0 critico | — | Antes de qualquer coisa, alguem precisa olhar o que ja existe "
          f"e escrever a lista de verdade. |\n\n")
    t += ("Estados possiveis, e nada mais:\n\n"
          "| Estado | Significa |\n| --- | --- |\n"
          "| `A FAZER` | Nada pendente, ou o pendente e do mesmo dono |\n"
          "| `AGUARDANDO` | Ha pendencia de OUTRO dono na cadeia |\n"
          "| `CONCLUIDO` | Entregue, com identificador de commit citado |\n\n"
          "Trabalho novo entra com numero maior que o ultimo em uso. Numero nunca se\n"
          "reaproveita, reatribui nem renumera: todo recado antigo que cita numero\n"
          "passaria a apontar para o item errado.\n")
    return t


def gerar_matriz(cfg):
    t = cab(cfg, "MATRIZ DA EQUIPE",
            "A coluna que evita a colisao e a quarta: o que cada um NAO toca sem avisar.")
    t += ("| Membro | Onde vive | Territorio (decide sozinho) | NAO toca sem avisar |\n"
          "| --- | --- | --- | --- |\n")
    t += (f"| {cfg['dono']} | — | Preco, produto, prioridade, visao, risco aceitavel | "
          f"Nada: decide tudo |\n")
    for a in cfg["agentes"]:
        marca = " **(escritor da fila)**" if a.get("escritor_da_fila") else ""
        t += f"| {a['nome']}{marca} | {a['plataforma']} | {a['territorio']} | {a['nao_toca']} |\n"
    t += ("\n## Regras de convivencia\n\n"
          "1. Ninguem anuncia pronto antes de a mudanca estar na ramificacao principal.\n"
          "   Construido no ambiente local e rascunho; publicado e entrega.\n\n"
          "2. Antes de editar arquivo fora do proprio territorio, avisa pelo recado.\n\n"
          "3. Quem escreve na ramificacao principal atualiza antes.\n\n"
          "4. Um escritor por recurso compartilhado. Recurso com dois donos corrompe\n"
          "   em silencio.\n\n"
          "5. Numero de item e identidade permanente.\n\n"
          "6. Quem escreve NAO confere. O autor le o que quis escrever, nao o que\n"
          "   escreveu.\n")
    return t


def gerar_recados(cfg):
    t = cab(cfg, "CAIXA DE RECADOS",
            "Leia antes de comecar. Escreva depois de entregar. Append-only: recado "
            "novo entra NO TOPO, nada se apaga.")
    t += ("Recado carrega **aviso, risco e pergunta**. NAO carrega estado — estado mora\n"
          "na fila, com o identificador do commit. Prosa e onde a numeracao errada se\n"
          "esconde.\n\n---\n\n"
          "## Para: todos — de: PADUA Software Design — "
          f"{date.today().strftime('%d/%m/%Y')}\n\n"
          f"A coordenacao deste projeto foi montada. Canal: `#{cfg['canal_mensagem']}`.\n\n"
          "- Leia `MATRIZ_DA_EQUIPE.md` antes da primeira acao\n"
          "- Pegue apenas item marcado com o seu nome **e** livre\n"
          "- Achou problema fora do seu territorio? NAO conserte. Escreva aqui\n\n"
          "---\n\n<!-- recado novo entra ACIMA desta linha. Nada se apaga. -->\n")
    return t


def gerar_glossario(cfg):
    dic = json.loads((RAIZ / "dicionario" / "dicionario.json").read_text(encoding="utf-8"))
    t = cab(cfg, "GLOSSARIO",
            "Numero PERMANENTE. `hash` e sempre o mesmo numero, hoje e daqui a dois anos.")
    t += ("Sem numero fixo o marcador nao ensina nada: `(*1)` significaria uma coisa numa\n"
          "mensagem e outra na seguinte. Com numero fixo o dono aprende por **repeticao** —\n"
          "na decima vez ja nao olha a legenda.\n\n"
          f"Congelado em {dic['congelado_em']}. Proximo numero livre: **{dic['proximo_numero']}**.\n\n"
          "| Nº | Termo | O que e | Em linguagem de leigo |\n| --- | --- | --- | --- |\n")
    for termo in dic["termos"]:
        oq = str(termo["oque_e"]).replace("|", "\\|")
        lg = str(termo["leigo"]).replace("|", "\\|")
        t += f"| (*{termo['numero']}) | {termo['termo']} | {oq} | {lg} |\n"
    t += ("\nTermo novo recebe `proximo_numero` e incrementa. Nunca reordene: mudaria o\n"
          "significado de todo marcador ja escrito em mensagem antiga.\n")
    return t


def gerar_blocos(cfg):
    canal = cfg["canal_mensagem"]
    escritor = next((a["nome"] for a in cfg["agentes"] if a.get("escritor_da_fila")),
                    cfg["agentes"][0]["nome"])
    t = cab(cfg, "BLOCOS PARA COLAR",
            "Copie e cole dentro de cada agente. A maioria nao instala plugin, mas "
            "todos leem texto.")
    t += (f"## Bloco A — no primeiro agente ({escritor})\n\n```\n"
          "ANTES DE ESCREVER UMA LINHA DE CODIGO, LEIA A COORDENACAO.\n\n"
          "Voce nao esta sozinho neste projeto. Outros agentes vao trabalhar nos mesmos\n"
          "arquivos que voce, sem falar com voce. O controle de versao aceita dois lados\n"
          "do mesmo assunto SEM apontar conflito, e o defeito so aparece em producao.\n\n"
          "Leia, nesta ordem:\n"
          "  docs/COORDENACAO/MATRIZ_DA_EQUIPE.md\n"
          "  docs/COORDENACAO/FILA_DE_PRODUCAO.md\n"
          "  docs/COORDENACAO/CAIXA_DE_RECADOS.md\n\n"
          f"Voce e o ESCRITOR DA FILA. Primeira tarefa: LEIA O CODIGO deste projeto e\n"
          "substitua a linha de exemplo da fila pelos itens reais. NAO pergunte ao dono\n"
          "o que a fila deve conter — fila montada a partir de pergunta nasce com os\n"
          "itens que ele lembrou; a partir do codigo, com os itens que existem.\n\n"
          "REGRAS:\n"
          "  1. Um escritor por recurso. A fila e sua; os outros pedem pelo recado.\n"
          "  2. Numero de item e identidade permanente.\n"
          "  3. Nada se apaga. Acrescenta-se.\n"
          "  4. Concluido exige identificador de commit que EXISTA no ramo principal.\n"
          "  5. Quem escreve nao confere.\n\n"
          "RESPONDA: quantos itens a fila tem e qual voce comeca.\n```\n\n---\n\n"
          "## Bloco B — em cada agente que chega depois\n\n```\n"
          "ESTE PROJETO TEM COORDENACAO ESCRITA. LEIA ANTES DE AGIR.\n\n"
          "  1. docs/COORDENACAO/CAIXA_DE_RECADOS.md   o que mudou\n"
          "  2. docs/COORDENACAO/MATRIZ_DA_EQUIPE.md   o que e SEU e o que NAO e\n"
          "  3. docs/COORDENACAO/FILA_DE_PRODUCAO.md   o que fazer\n\n"
          "Pegue apenas item marcado com o SEU nome e livre. Se nada estiver livre,\n"
          "escreva no recado em vez de inventar trabalho.\n\n"
          "Achou problema fora do seu territorio? NAO CONSERTE. Escreva no recado e siga\n"
          "o seu item. Consertar fora do territorio e como as colisoes acontecem.\n\n"
          "Ao entregar: mude o Estado citando o identificador do commit, e escreva no\n"
          "recado o que muda PARA OS OUTROS.\n\n"
          "RESPONDA: qual item voce esta comecando.\n```\n\n---\n\n"
          "## Bloco C — quando aparecerem duas listas\n\n```\n"
          "PARE. HA DUAS VERDADES NESTE PROJETO.\n\n"
          "  1. NAO APAGUE nenhuma das listas.\n"
          "  2. Prevalece a que tem verificacao automatica rodando.\n"
          "  3. Os itens da outra entram como numeros NOVOS, maiores que o ultimo.\n"
          "  4. Registre o incidente num arquivo datado. Ele vale mais que a correcao.\n"
          "  5. Confirme por escrito quem e o escritor unico.\n\n"
          "RESPONDA: quantos numeros estavam duplicados.\n```\n\n---\n\n"
          f"## Bloco D — ligar no canal `#{canal}`\n\n```\n"
          f"VOCE FOI LIGADO AO CANAL #{canal}.\n\n"
          "O aviso entre agentes NAO passa mais pelo dono. A VERDADE continua no\n"
          "repositorio; o canal so avisa que ela mudou. NUNCA escreva a fila no canal.\n\n"
          "FORMATO OBRIGATORIO, quatro tipos:\n\n"
          "  [ITEM n] CONCLUIDO — <voce> — commit <hash>\n"
          "  [ITEM n] TRAVADO — <voce> | Espera: item <n> (<agente>)\n"
          "  [DECISAO n] PERGUNTA — <voce> para <dono>\n"
          "  [RISCO] <voce> encontrou, territorio de <outro>\n\n"
          "Postar que esta TRAVADO e obrigatorio: agente parado em silencio parece\n"
          "agente trabalhando.\n\n"
          "NUNCA poste senha, token, chave ou dado de cliente. Mensagem fica gravada e\n"
          "e pesquisavel por todo o espaco de trabalho.\n\n"
          "CONFIRME com UMA linha: nome, territorio, item que comeca.\n```\n")
    return t


def gerar_falta(cfg):
    t = cab(cfg, "FALTA CONFIGURAR",
            "So o dono do projeto faz. Numerado, e cada linha diz o que destrava.")
    t += ("Ordem importa: o passo 1 costuma bloquear varios outros.\n\n"
          "| Nº | O que fazer | Onde | Bloqueia |\n| --- | --- | --- | --- |\n"
          f"| 1 | Criar a pasta `PROJETO {cfg['projeto'].upper()}` na nuvem | "
          f"{cfg['pasta_drive']} | a planilha do dono |\n"
          f"| 2 | Criar o canal `#{cfg['canal_mensagem']}` e convidar CADA aplicativo | "
          "plataforma de mensagem | todo aviso entre agentes |\n")
    n = 3
    for c in cfg.get("chaves_necessarias") or []:
        t += (f"| {n} | Colar `{c.get('nome')}` (so o valor, no cofre) | "
              f"{c.get('onde_colar', 'cofre de segredos')} | {c.get('bloqueia', '—')} |\n")
        n += 1
    t += (f"| {n} | Colar os blocos de `BLOCOS_PARA_COLAR.md` em cada agente | "
          "cada plataforma | o inicio de tudo |\n\n"
          "## Sobre o passo 2\n\n"
          "Conector ligado **nao** significa acesso ao canal. O aplicativo de cada agente\n"
          "precisa ser convidado para dentro dele, um por um. E o passo que mais falta, e\n"
          "o sintoma engana: o agente diz que esta conectado, tenta postar, e nada aparece.\n\n"
          "## Sobre as chaves\n\n"
          "Nenhuma chave e gerada por programa: cada fornecedor exige login humano, e\n"
          "chave gerada por programa e chave que vaza por programa. Cole **so no cofre de\n"
          "segredos** — nunca em conversa, nunca em arquivo versionado.\n")
    return t


def gerar_env(cfg):
    t = ("# Nomes de variavel. NUNCA valores.\n"
         "# Copie para .env e preencha no cofre de segredos da sua plataforma.\n"
         "# Este arquivo E versionado; o .env NAO e.\n\n")
    for c in cfg.get("chaves_necessarias") or []:
        t += (f"# {c.get('onde_colar', 'cofre de segredos')}"
              f" | bloqueia: {c.get('bloqueia', '—')}\n{c.get('nome')}=\n\n")
    return t


def gerar_gitignore(cfg):
    return ("# Segredo nunca entra no repositorio.\n"
            ".env\n.env.*\n!.env.example\n*.pem\n*.key\n"
            "credentials*.json\nservice-account*.json\n\n"
            "# Dependencia e build\nnode_modules/\n__pycache__/\n*.pyc\ndist/\nbuild/\n\n"
            "# Sistema\n.DS_Store\nThumbs.db\n")


ARQUIVOS = [
    (DESTINO / "FILA_DE_PRODUCAO.md", gerar_fila),
    (DESTINO / "MATRIZ_DA_EQUIPE.md", gerar_matriz),
    (DESTINO / "CAIXA_DE_RECADOS.md", gerar_recados),
    (DESTINO / "GLOSSARIO.md", gerar_glossario),
    (DESTINO / "BLOCOS_PARA_COLAR.md", gerar_blocos),
    (DESTINO / "FALTA_CONFIGURAR.md", gerar_falta),
    (pathlib.Path(".env.example"), gerar_env),
    (pathlib.Path(".gitignore"), gerar_gitignore),
]


# ============================================================ PRINCIPAL
def main():
    ap = argparse.ArgumentParser(
        description="Monta a coordenacao de um projeto novo a partir de projeto.yaml")
    ap.add_argument("--validate", action="store_true", help="so confere o formulario")
    ap.add_argument("--dry-run", action="store_true", help="mostra o que SERIA criado")
    ap.add_argument("--arquivo", default="projeto.yaml", help="caminho do formulario")
    args = ap.parse_args()

    caminho = pathlib.Path(args.arquivo)
    if not caminho.exists():
        print(f"nao achei {caminho}. Copie projeto.exemplo.yaml para projeto.yaml.")
        sys.exit(1)

    cfg = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}

    problemas = validar(cfg)
    if problemas:
        print(f"FORMULARIO COM {len(problemas)} PROBLEMA(S):\n")
        for p in problemas:
            print("  " + p)
        print("\nNada foi criado.")
        sys.exit(1)
    print(f"formulario valido: {cfg['projeto']} ({cfg['empresa']}), "
          f"{len(cfg['agentes'])} agentes, on_conflict={cfg.get('on_conflict', 'skip')}")

    if args.validate:
        return

    conflito = cfg.get("on_conflict", "skip")
    criados, pulados, sobrescritos = [], [], []

    for destino, gerar in ARQUIVOS:
        conteudo = gerar(cfg)
        existe = destino.exists()

        if existe and conflito == "abort":
            print(f"\nPAROU: {destino} ja existe e on_conflict=abort. Nada foi alterado.")
            sys.exit(1)
        if existe and conflito == "skip":
            pulados.append(destino)
            continue

        if args.dry_run:
            (sobrescritos if existe else criados).append(destino)
            continue

        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(conteudo, encoding="utf-8")
        (sobrescritos if existe else criados).append(destino)

    rotulo = "SERIA criado" if args.dry_run else "criado"
    print()
    for d in criados:
        print(f"  {rotulo}:      {d}")
    for d in sobrescritos:
        print(f"  {'SERIA sobrescrito' if args.dry_run else 'sobrescrito'}: {d}")
    for d in pulados:
        print(f"  pulado (ja existe, on_conflict=skip): {d}")

    if args.dry_run:
        print("\nNada foi escrito. Tire o --dry-run para criar.")
        return

    print("\nPROXIMOS PASSOS")
    print("  1. Abra docs/COORDENACAO/FALTA_CONFIGURAR.md — e a sua lista")
    print("  2. Cole os blocos de BLOCOS_PARA_COLAR.md em cada agente")
    print("  3. O escritor da fila le o codigo e preenche a fila de verdade")


if __name__ == "__main__":
    main()
