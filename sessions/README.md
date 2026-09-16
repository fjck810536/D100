# sessions/

> Legacy root-level session store. 新 bootstrap 架構下，persistent runtime 的 session records 應存在 **selected campaign** 的 logical `sessions/` store；本目錄只在 legacy migration / recovery 明確引用時使用。

每次跑團建立一份 session state / log，讓下一個 GPT 可以從存檔恢復狀態，而不是依賴聊天記憶。

模板：

`templates/SESSION_STATE_TEMPLATE.md`

邏輯命名建議：

```text
<selected-campaign>/sessions/2026-09-12_session-001
```

若同一 session 同時存在 checkpoint、migration snapshot 與 `*_live-state`：

```text
live-state = 當前 role-safe 指標
checkpoint = 歷史存檔點
migration snapshot = 遷移當時狀態
```

不要因檔名日期較早／內容較完整，就用舊 checkpoint 覆蓋 live-state 已經明確列出的後續事件。

## Session 開始

GPT 應讀：

1. `AGENTS.md`
2. `BOOTSTRAP_PROTOCOL.md`
3. `CAMPAIGN_STORAGE_PROTOCOL.md`
4. `DATA_ARCHITECTURE.md`
5. `RUNTIME_SOCIAL_WORLD_CONTRACT.md`
6. `DM_PROTOCOL.md`
7. core rules
8. selected campaign manifest
9. selected campaign house rules（若有）
10. selected campaign current state
11. selected campaign authoritative PC files
12. selected campaign 最新 live session pointer（若有），再依其 refs 補讀 checkpoint / migration / site / commitment
13. 若沒有 live-state，才以該 campaign 最新有效 session snapshot 作 current state
14. 需要秘密內容時，依 `MYSTERY_PROTOCOL.md` 取得該 campaign 合法 view

不得因 repo 根目錄存在其他 session，就把未被 manifest 指向的 session 當成本次團務。

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

並完成 storage write verification。若 backend update 失敗：

```text
不得宣稱已存檔
→ 保留 working state 為 uncommitted
→ 回報哪一個 record / capability 寫入失敗
```

## Session 不是角色主檔

Session 應保存「這一幕發生了什麼／角色目前即時狀態」，不是每次重抄整張角色卡。

因此：

```text
session Search=56
!=
完整 skill build master
```

角色 final build、信仰、領域、語言、完整技能／專長、起始裝備等已成立長期資料，必須存在 selected campaign authoritative character record。不能因為 session 沒重複列出，就當作不存在。

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

若未來需要玩家可見 log，可由同一 campaign state 產生 player-safe projection，而不是把「DM 版 session」當唯一來源後再人工刪秘密。

## Derived reasoning

分析師、生態學家、政治家等模塊若產生昂貴推理，可保存 `derived_refs` 或短期 cache；必須標示它不是 world fact，底層 state 改變時可失效，也不得無標記跨 campaign 重用。

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

若 repair 來源位於 legacy root，必須由 manifest / migration record 明確指出它屬於目前 campaign；不能掃到同名資料就直接吸收。
