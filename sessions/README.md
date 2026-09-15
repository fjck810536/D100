# sessions/

每次跑團建立一份 session state / log，讓下一個 GPT 可以從檔案恢復狀態，而不是依賴聊天記憶。

模板：

`templates/SESSION_STATE_TEMPLATE.md`

命名建議：

```text
sessions/2026-09-12_session-001.md
```

若同一 session 同時存在 checkpoint、migration snapshot 與 `*_live-state.md`：

```text
live-state = 當前 role-safe 指標
checkpoint = 歷史存檔點
migration snapshot = 遷移當時狀態
```

不要因檔名日期較早／內容較完整，就用舊 checkpoint 覆蓋 live-state 已經明確列出的後續事件。

## Session 開始

GPT 應讀：

1. `AGENTS.md`
2. `DATA_ARCHITECTURE.md`
3. `RUNTIME_SOCIAL_WORLD_CONTRACT.md`
4. `DM_PROTOCOL.md`
5. core rules
6. `campaign/house_rules.md`
7. campaign current state（若存在／已正式建立）
8. PC files
9. 最新 `*_live-state.md`（若有），再依其 refs 補讀 checkpoint / migration / site / commitment
10. 若沒有 live-state，才以最新有效 session snapshot 作 current state
11. 需要秘密內容時，依 `MYSTERY_PROTOCOL.md` 取得合法 view

若本幕涉及 world lore / organization / academy / site / affiliation / teacher / authority / service route，依 `START_DM.md` / `DM_PROTOCOL.md` 走 Librarian source resolution；不要只靠 session 散文續寫。

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
- 新增／採用的設定 claim provenance（source / user-correction / creative-addition / legacy-generated）
- decision / adoption / repair refs
- typed deferral / owner-decision refs（若有）

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

## Provenance repair

若舊 scene 已經發生、但後來才發現當時沒有留下 source/generation trace：

```text
保留無衝突的既成事件
→ 現在補 source resolution
→ source-backed / user-correction / legacy-generated 分開
→ 新採用 creative detail 留 adoption event
→ recorded_at 與 effective_from 分開
```

不得偽稱先前已經查過，也不要只因 provenance 缺漏就重骰或倒回 checkpoint。
