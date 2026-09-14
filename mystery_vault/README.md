# mystery_vault/

> D100 DM 的祕密／hidden causal state 保存區。此目錄實作 `MYSTERY_PROTOCOL.md` 中的 MYSTERY VAULT 概念。
>
> 目前 repo / 單一 LLM context 無法提供真正的工具或 context 硬隔離，因此這裡保存的內容預設只能誠實視為 **SOFT secret / SOFT_EX-capable storage**；不得聲稱未授權模塊在資訊層面真的看不到。

規則：

- ordinary `campaign/current_state.md`、`sessions/*.md`、`characters/*.md` 不複製完整 hidden truth；只保存 `secret_refs` / `commitment_refs` 與合法 role-safe representation。
- 世界核心因果、hidden actor identity floor、NPC relevant knowledge、原定 next step 等，一旦在玩家首次可觀察／可影響前 committed，可保存在本區。
- `roll outcome` 可以改變發現、干預與後果；不得倒過來決定 committed truth 原本是什麼。
- 若某項資料未達 EX，只是普通秘密，也可以在本區保存；Vault 不等於 EX。
- 任何從舊 runtime 遷移而來、不是事前建立的 commitment，必須明確標 `migration_provenance`，不得偽稱當時早已有完整 hidden state。
