# campaign/

這個目錄放**該團目前成立的正典世界狀態**，優先級高於一般 DM default 與 SRD bridge。

建議檔案：

- `house_rules.md` — 本團採用的明示 house rules
- `setting.md` — 世界設定與不可變事實
- `current_state.md` — 當前世界／任務／NPC／Site／Hazard 狀態與 Secret refs

## Secret storage

**不再建議在 `campaign/` 另設 plaintext `secrets.md` 作平行秘密庫。**

祕密、陰謀、認知危害、EX 與 module views 統一交給：

```text
MYSTERY_PROTOCOL.md
```

campaign state 只保存：

```yaml
secret_refs:
  - secret_id: SECRET-...
    view: campaign_safe
```

若某 runtime 尚未實作真正 Vault，可依 `MYSTERY_PROTOCOL.md` 誠實標記 SOFT_EX；仍不得因此把完整 protected payload 任意複製到所有 state 檔。

## GPT 使用規則

開團時先讀：

1. `house_rules.md`
2. `setting.md`（若存在）
3. `current_state.md`（若存在）
4. 最新 session 檔
5. 相關角色檔
6. 需要秘密資訊時，依 Mystery 取得 role-safe representation

如果 campaign 檔案與通用 D100 core 衝突，以 campaign 明示 house rule 為準。

資料與模塊分層見：

```text
../DATA_ARCHITECTURE.md
```

## 不要做

- 不要把玩家猜測寫成 setting fact。
- 不要把 DM 秘密提前移到玩家可見狀態。
- 不要另建會繞過 Mystery 的 plaintext secret store。
- 不要因為聊天裡曾經提過某個可能性，就直接固化成正典。
- 不要把 Cabinet 的預測／人格分析／政治 forecast 寫成 established world fact。
- 新增世界事實時，要能指出它是玩家行動造成、DM 設定、既有 campaign 資料，或 AO 結算後的結果。
