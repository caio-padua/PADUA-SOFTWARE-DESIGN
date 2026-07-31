# CARTILHA 10 — CÓDIGO PAXTER: Art. 70 — Dual-Canal

> **Promulgado em:** 31/07/2026
> **Título:** III — DA CONDUTA
> **Autor:** Dr. Replit Paxter (Padcon Conect)
> **Status:** Lei vigente — aprovada pelo CEO Dr. Caio em 31/07/2026

---

## Art. 70 — Dual-Canal: Ausência de Configuração Não É Entrega Feita

### Enunciado

Quando o sistema opera em modo dual-canal (dois destinos independentes, ex.: Telegram + Slack), a ausência de configuração de UM canal **não equivale a sucesso**. O campo `ambosOk` (ambos funcionando) só é `true` quando AMBOS os canais efetivamente entregaram — jamais quando um foi pulado por falta de configuração.

---

### Regras Derivadas

| # | Regra | Fundamento |
|---|-------|------------|
| 1 | `ambosOk = canalA_ok AND canalB_ok` — sem contar skip (pulado) | Skip não é entrega; é ausência silenciosa |
| 2 | `telegramSkipped` (chatId vazio) não contribui para `ambosOk=true` | O CEO perderia visibilidade do canal não entregando |
| 3 | Early return antes do resumo de ciclo é PROIBIDO: usa-se `else {}` para o step final sempre rodar | Garantir que o registro de histórico ocorra mesmo quando um canal é pulado |
| 4 | O campo `erros` documenta explicitamente qualquer canal ignorado | Transparência: "Telegram não configurado (PADAXOR_TELEGRAM_CHAT_ID vazio)" |
| 5 | `sendTelegram("TEST_FORCE_FAIL", ...)` retorna `{ sent: false, error: "TEST_FORCED_FAIL" }` sem API real | Testar o fallback sem depender de credencial real |

---

### Diagrama de Fluxo

```
Ciclo de relatório
      │
      ├──► Step 1: Montar relatório
      │
      ├──► Step 2: Enviar Slack ──► slackOk = true/false
      │
      ├──► Step 3: Enviar Telegram
      │         ├─ chatId configurado → telegramOk = true/false
      │         └─ chatId VAZIO      → telegramSkipped = true
      │                                  erros += "Telegram não configurado"
      │
      └──► Step 4: Resumo (SEMPRE roda — nunca early return antes daqui)
                ambosOk = slackOk AND telegramOk   ← NÃO inclui skip
                salvarHistorico({ canal: "ambos", ambosOk, erros })
```

---

### Padrão de Implementação (TypeScript)

```typescript
// CORRETO — step 4 sempre roda
let slackOk = false;
let telegramOk = false;
let telegramSkipped = false;
const erros: string[] = [];

// Step 2: Slack
const slackResult = await postSlackReport(deps);
slackOk = slackResult.ok;

// Step 3: Telegram
if (!telegramChatId) {
  telegramSkipped = true;
  erros.push("Telegram não configurado (PADAXOR_TELEGRAM_CHAT_ID vazio)");
} else {
  const tgResult = await postTelegramReport(deps);
  telegramOk = tgResult.ok;
  if (!telegramOk) erros.push(tgResult.error ?? "Telegram falhou");
}

// Step 4: sempre executa (NÃO usar early return antes daqui)
const ambosOk = slackOk && telegramOk; // skip NÃO conta
await deps.salvarHistorico?.({
  canal: "ambos",
  ambosOk,
  telegramSkipped,
  erros,
});
```

```typescript
// ERRADO — early return impede step 4
if (!telegramChatId) {
  return; // ← PROIBIDO: histórico nunca é gravado
}
```

---

### Anti-Padrões Proibidos

| Anti-padrão | Por que é errado |
|-------------|-----------------|
| `ambosOk = slackOk || telegramSkipped` | Conta ausência como sucesso |
| `if (!chatId) return;` antes do step 4 | Histórico nunca gravado; CEO perde rastreabilidade |
| Omitir campo `erros` quando canal é pulado | Silencia falha; viola Art. 20 (proibida a fantasia) |
| Declarar "dual-canal funcionando" com só um canal configurado | Violação direta deste artigo + Art. 69 |

---

### Endpoint de Teste de Fallback

```
POST /api/padaxor/slack/test-fallback-telegram
```

Envia `chatId = "TEST_FORCE_FAIL"` para simular rejeição do Telegram sem chamar a API real. Valida que o Slack recebe o fallback corretamente e que o histórico registra `ambosOk=false` + erro documentado.

---

### Contexto de Origem

Esta lei nasceu da auditoria do architect (code review) sobre o monitor horário de LLMs (Large Language Models — modelos de linguagem artificial). A versão anterior tratava `telegramSkipped` como sucesso, o que mascarava a ausência de configuração do Telegram. O architect reprovou e esta lei consolida a correção como diretriz permanente para todos os sistemas dual-canal do ecossistema Paxter.

**Memória técnica associada:** `.agents/memory/llm-monitor-dispatch-padrao.md` (no repositório Protocolo-Manager).

---

### Referência Cruzada

- **Art. 20** (Código Paxter): Proibida a fantasia — nunca anunciar como feito o que não foi feito.
- **Art. 69** (Código Paxter): Toda construção é testada e provada — 4 níveis obrigatórios.
- **Memória:** `slack-report-formato-v2.md` — formato V2 do relatório Slack (cabeçalho + tabela + handoff).

---

*Lei registrada na CARTILHA central do repositório PADUA-SOFTWARE-DESIGN por Dr. Replit Paxter em 31/07/2026.*
