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
2. core rules
3. `campaign/house_rules.md`
4. campaign current state（若存在）
5. PC files
6. 最新 session

## Session 結束

至少記錄：

- PC HP / SP / 長期狀態
- CP、金錢、物品變動
- 已揭露情報
- 未完成事件
- NPC 生死／態度／位置
- 世界時間
- 本次出現的臨時裁定與 open questions

## 隱藏資訊

如果 repo 會直接分享給玩家，不要把 DM secrets 與玩家可見 log 放同一個公開檔案。可以另設私人 branch／私人 DM state；本 repo 目前為 private，但仍應維持資料層級清楚。
