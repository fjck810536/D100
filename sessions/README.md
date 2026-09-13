# sessions/

每次跑團建立一份 session state / log，讓下一個 GPT 可以從檔案恢復狀態，而不是依賴聊天記憶。

模板：

`templates/SESSION_STATE_TEMPLATE.md`

命名建議：

```text
sessions/2026-09-12_session-001.md
```

## Session 開始

GPT 應讀：

1. `AGENTS.md`
2. `DATA_ARCHITECTURE.md`
3. core rules
4. `campaign/house_rules.md`
5. campaign current state（若存在）
6. PC files
7. 最新 session
8. 需要秘密內容時，依 `MYSTERY_PROTOCOL.md` 取得合法 view

## Session 結束

至少記錄：

- PC HP / SP / 長期狀態
- CP、金錢、物品變動
- 已揭露情報
- Secret refs / 已改變的 classification 或 release 狀態
- 未完成事件
- NPC 生死／態度／belief／位置
- Site / Hazard live state 變動
- 世界時間
- 本次出現的臨時裁定與 open questions

## 隱藏資訊

Session 可以保存「秘密擲骰結果」與合法的 role-safe representation，但**不得作為另一個 Mystery Vault**。

禁止：

```text
把完整 DM secret / EX payload 直接寫進所有 session log
為了讓下一個 GPT 看得到而複製一份 plaintext 秘密
讓 session log 成為能繞過 classification / clearance 的旁路
```

應使用：

```yaml
secret_refs:
  - secret_id: SECRET-...
    view: session_safe
```

若 repo 未來需要玩家可見 log，可由同一 state 產生 player-safe projection，而不是把「DM 版 session」當唯一來源後再人工刪秘密。

## Derived reasoning

分析師、生態學家、政治家等模塊若產生昂貴推理，可保存 `derived_refs` 或短期 cache；必須標示它不是 world fact，底層 state 改變時可失效。
