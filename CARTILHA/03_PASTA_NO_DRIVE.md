# 03 — A PASTA NO GOOGLE DRIVE

> A pasta do Drive e a janela do dono do projeto. E onde ele ve o predio sendo
> construido sem precisar entender de obra.

---

## Nome da pasta

```
PROJETO <NOME>
```

Maiuscula, espaco simples, sem parentese, sem data. O nome do projeto e a
identidade permanente da pasta.

---

## O que vai dentro

| Arquivo | Para que |
| --- | --- |
| `<NOME>_LINHA_DE_PRODUCAO_aa.mm.dd.xlsx` | A planilha. E o unico arquivo que o dono edita. |
| `<NOME>_ARQUITETURA_aa.mm.dd.pdf` ou `.md` | O desenho do sistema, para ele ver o predio |
| `HISTORICO/` | Versoes anteriores da planilha. Nada se apaga. |

Nada mais. Pasta com vinte arquivos deixa de ser janela e volta a ser deposito.

---

## Como entregar o link ao dono

Entregue o link **da pasta**, nunca o do arquivo.

| Tipo de link | O que acontece quando o arquivo e substituido |
| --- | --- |
| Link do arquivo | Morre. O identificador antigo passa a responder "nao encontrado" |
| Link da pasta | Continua funcionando. O dono acha o arquivo novo lá dentro |

Aconteceu de verdade: um agente substituiu a planilha, o identificador antigo
morreu, e o link que o dono tinha guardado parou de abrir.

Ao entregar, diga em duas linhas: **o que ele vai encontrar** e **o que ele
deve fazer lá**. Nunca entregue link sem dizer para que serve.

---

## As quatro regras da pasta

### 1. Um agente so sobe arquivo para a pasta

Sempre o mesmo. Dois agentes subindo arquivo de mesmo nome para a mesma pasta
se sobrescrevem em silencio.

### 2. Nunca substitua a planilha com o dono escrevendo nela

Antes de subir, confira a data de modificacao do arquivo que esta lá:

| Situacao | O que significa | O que fazer |
| --- | --- | --- |
| Data de modificacao **igual** a de criacao | Ninguem editou ainda | Pode substituir |
| Data de modificacao **maior** que a de criacao | O dono ja escreveu ali | NAO substitua. Pergunte. |

Sobrescrever a resposta do dono e o pior erro possivel nesta pasta: ele
respondeu uma decisao que so ele pode responder, e a resposta desaparece.

### 3. Versao antiga vai para HISTORICO, nao para a lixeira

Mesmo nome-base, data no sufixo. A versao de data maior e a vigente; as
menores ficam como historico legivel.

### 4. Gere a planilha com biblioteca que o Google consegue abrir

Cuidado real e ja observado: alguns geradores em JavaScript escrevem, dentro do
arquivo, um pedaco de metadados de "matriz dinamica" que **nenhuma celula usa**.
O arquivo abre no Excel e no LibreOffice, e o conversor do Google recusa com
`UNSUPPORTED_CONVERSION`.

Sintomas de arquivo que vai falhar no Google:

| Sinal | Como conferir |
| --- | --- |
| Existe `xl/metadata.xml` e nenhuma celula com `vm=` ou `cm=` | Abrir o `.xlsx` como pacote compactado e listar o conteudo |
| Todos os pedacos sem compressao (`STORED`) | Idem |
| Ausencia de `xl/sharedStrings.xml` | Idem |

Se o arquivo tiver esses tres sinais, gere de novo com outra biblioteca antes
de entregar ao dono. Entregar arquivo que nao abre custa a confianca dele na
ferramenta inteira.

### Recomendacao

Depois de subir, converta para **planilha nativa do Google**
(`Arquivo > Salvar como Planilhas Google`). A partir daí:

- nunca mais depende de conversao
- o dono e os colaboradores comentam celula por celula
- da para proteger intervalo: deixar so `Observacao` e `HISTORICO` editaveis

---

## O que o dono faz nessa pasta, e so isso

| Ele faz | Ele nao precisa fazer |
| --- | --- |
| Marcar `Estado` quando quiser | Entender como a planilha e gerada |
| Responder a coluna de decisoes | Copiar texto entre telas de agentes |
| Escrever em `Observacao` | Lembrar quem estava fazendo o que |
