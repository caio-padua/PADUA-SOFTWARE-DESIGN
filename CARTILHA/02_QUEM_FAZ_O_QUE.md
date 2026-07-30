# 02 — QUEM FAZ O QUE

> A coluna que evita a colisao e a terceira: **o que nao toca sem avisar**.
> As outras sao contexto.

---

## Os papeis

| Agente | Onde vive | Territorio natural | NAO toca sem avisar |
| --- | --- | --- | --- |
| **Dono do projeto** | — | Preco, produto, prioridade, visao, decisao de negocio e decisao clinica | Nada: decide tudo |
| **Dr. Claude** | claude.ai | Arquitetura, especificacao escrita antes do codigo, auditoria | Nao commita: le e especifica |
| **Dr. Code** | Claude Code | Servidor, banco, infraestrutura, autenticacao, coordenacao da fila | Telas e site |
| **Dr. Replit** | Replit | Telas do sistema, logica de negocio, rotas da aplicacao | Banco em producao, configuracao de infraestrutura |
| **Dr. Lovable** | Lovable | Site institucional, vitrine, telas publicas | Servidor e banco: consome, nunca altera |
| **Dr. Manus** | Manus | Missao inteira de ponta a ponta: varredura, auditoria, teste de carga | Publicar em producao direto |
| **OpenClaw** | agente proprio | Frente atribuida caso a caso, registrada na matriz do projeto | O que a matriz do projeto nao deu a ele |

O papel de coordenador da fila e **um so** por projeto. Registre quem e na
matriz do projeto, na primeira linha.

---

## O que todo agente faz, sem excecao

### Ao entrar no projeto

```
1  le docs/COORDENACAO/CAIXA_DE_RECADOS.md
2  le docs/COORDENACAO/FILA_DE_PRODUCAO.md
3  roda o conferidor de coerencia
4  pega item marcado como SEU e livre
```

Nunca pegue item que nao esta na sua lista de livres. Se parece que nao ha
nada, escreva no recado em vez de inventar trabalho.

### Ao entregar

```
1  muda o ESTADO do item na fila para CONCLUIDO
2  cita o identificador do commit e o arquivo tocado
3  acrescenta linha no historico: como estava, como ficou, por que, prova
4  escreve no recado o que muda PARA OS OUTROS
```

### Ao encontrar problema fora do seu territorio

Nao conserte. Escreva no recado, com o numero do item se houver, e siga o seu.
Consertar fora do territorio e como a primeira, a segunda e a terceira colisao
aconteceram.

---

## As tres regras de convivencia

1. **Ninguem anuncia pronto antes de estar na ramificacao principal.**
   Construido no ambiente local e rascunho; publicado e entrega.

2. **Antes de editar arquivo fora do proprio territorio, avisa.**

3. **Quem escreve na ramificacao principal atualiza antes.**
   Sincronizar por cima desfaz correcao que esta funcionando em producao.

---

## O que nunca fazer

| Nunca | Por que |
| --- | --- |
| Criar uma segunda fila porque a primeira esta em outro lugar | Foi exatamente assim que a quarta colisao aconteceu |
| Renumerar itens para "organizar" | Todo recado antigo que cita numero passa a apontar para o item errado |
| Marcar concluido sem identificador de commit | Anunciar sem prova destroi a confianca na fila inteira |
| Atribuir um item a dois agentes | Recurso com dois donos corrompe em silencio |
| Responder no lugar do dono sobre preco ou produto | Nao e territorio de agente nenhum |
| Apagar linha, recado ou historico | Nada se apaga. Acrescenta-se. |
