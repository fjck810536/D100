# Social World / Alignment Open Questions

> 本檔是 `99_open_questions/` 的社會世界／角色關係設計缺口 registry。
>
> 這裡只記「已確認值得設計，但尚未決定正式機制」的問題。不得因為列在此處就自行升格成 runtime 正典。

---

## P1-SOCIAL-1 — Alignment 與實際行為之間的浮動／偏移紀錄

### 已確認需求

目前角色 state 已正式保存九宮格 Alignment，且 runtime 契約明確規定：

```text
alignment ≠ presented_persona ≠ current_affect ≠ actual_action
```

分析師可以把 Alignment 當作長期倫理／秩序座標，但不能把 Alignment 當成逐場戲的行動腳本。

尚缺的是：

> 是否需要一個可持續觀察「角色實際行為長期如何靠近、偏離、拉扯其 declared alignment」的浮動紀錄？

這個紀錄若建立，目的應是提供分析師／Player／DM 看見角色發展，而不是自動懲罰角色或強迫扮演。

### 待討論核心問題

1. **資料形狀**
   - 只記事件 evidence？
   - 分別對 `law ↔ chaos`、`good ↔ evil` 維護連續數值？
   - 使用短期／長期兩層？
   - 使用 qualitative tags，例如 `aligned / tension / exception / sustained drift`？

2. **事件權重**
   - 一次情緒失控是否應該幾乎不影響 Alignment？
   - 重複、有代價、可自由選擇的行動是否權重更高？
   - 被控制、被迫、資訊不足、角色誤信造成的行為是否應降權或不計？

3. **Persona / Affect 分離**
   - `presented_persona` 與 `current_affect` 不應直接視為 Alignment drift。
   - 一個 Chaotic Evil 角色可以長期表現溫柔、友善或守禮；分析師應能記錄「呈現」與「倫理取向」的張力，而不是用表面行為立即改標籤。

4. **誰有權改 Alignment**
   - 真人 PC：不得由分析師／DM 靜默改 Alignment；至少需要玩家確認或顯式角色發展事件。
   - 四聲部 PL+PC：由對應 Player Voice ratify / revise。
   - autonomous NPC：可由 AO / Orchestrator 依已發生角色發展更新，但應留下 provenance。

5. **分析師的輸出邊界**
   - 分析師可以回報：`alignment-consistent pattern`、`temporary tension`、`sustained drift candidate`。
   - 分析師不能因單次行為直接宣布角色已換陣營。
   - derived drift cache 必須在新行為、關係、重大秘密揭露、Player reinterpretation 後可失效／重算。

6. **是否需要衰減／歷史窗口**
   - 很久以前的一次例外是否應持續影響現在？
   - 若需要時間衰減，應由世界時間／session 數／重大章節哪一種尺度控制？

### 最低保險絲

未來無論採哪種機制，都應維持：

```text
Alignment 是角色結構資料，不是行動指令。
單一行為 ≠ 陣營改變。
表演得像善人 ≠ Good。
情緒失控 ≠ Chaotic。
服從法律 ≠ Lawful。
違法 ≠ Chaotic。
殘酷 ≠ 單獨足以證明 Evil；必須看選擇、目的、關係與反覆模式。
分析師觀察 drift ≠ 分析師有權重寫角色 Alignment。
```

### 目前暫定 runtime

在正式機制完成前：

- 只保存 declared / ratified Alignment；
- 行為保存在 behavior history / session log；
- 分析師可以做 qualitative derived observation；
- 不維護隱藏的 Alignment 點數；
- 不自動改 Alignment。

### 觸發正式設計的條件

出現以下任一壓測案例時，優先回來處理本題：

- 角色 declared Alignment 與長期行為明顯分離；
- 玩家主動問「角色是不是正在變陣營」；
- 分析師需要比較 persona 與倫理結構，但缺乏歷史尺度；
- autonomous NPC 經重大事件後出現持久價值轉向；
- 不同模塊對「這是例外還是 drift」反覆產生衝突。
