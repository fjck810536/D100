# characters/

> Legacy root-level character store. 新 bootstrap 架構下，這個目錄不再代表「所有團共用的角色主檔」。
>
> Persistent runtime 的 authoritative PC / important NPC records 應存在 **selected campaign** 的 logical `characters/` store；provider 與 root 由 campaign manifest 決定。此 root 目錄只在 legacy migration / recovery 明確引用時使用。

每名 PC／重要 NPC 建議使用獨立 Markdown／record，作為角色的 state / capability master。

建立 PC 時使用：

`templates/PC_TEMPLATE.md`

重要 NPC／怪物可使用：

`templates/CREATURE_WORLD_MODEL_TEMPLATE.md`

邏輯命名例：

```text
<selected-campaign>/characters/alice
<selected-campaign>/characters/bob
```

資料分層見：

```text
../BOOTSTRAP_PROTOCOL.md
../CAMPAIGN_STORAGE_PROTOCOL.md
../DATA_ARCHITECTURE.md
../RUNTIME_SOCIAL_WORLD_CONTRACT.md
```

## DM 規則

- 先確認 campaign manifest；角色 master 的權威只屬於該 selected campaign。
- 角色檔內的實際數值、能力、Alignment、持有物與 established state 優先於聊天記憶與同團 session 投影。
- Alignment 是長期倫理／秩序座標與分析輸入，不是逐場戲的行動腳本；`alignment ≠ presented_persona ≠ current_affect ≠ action`。
- HP、SP、持續效果等即時變化可先記在同團 session state，session 結束再回寫需要永久保存的角色狀態。
- 不要替玩家補未選專長、未學技能、未持有裝備。
- 若角色檔缺少 P0 數值（例如目前未決的基礎移動），不要默認套 D&D 數值；先依該團 house rule 或已知角色表處理。
- 角色目前知道／相信什麼存 epistemic state；世界真相不等於角色知道真相。
- 客觀關係 facts 放該團共享 `Relationship Graph`；角色檔只保留 `relationship_refs`，不要把整張關係網複製進每張角卡。
- 分析師／生態學家／政治家的推測不能直接寫成角色「真正人格」或 established relationship fact。
- combat doctrine、threat model、relationship interpretation、political forecast、未來行動預測若需要 cache，必須標 derived 並可失效。
- 完整祕密／EX payload 不直接寫進角色檔；只保存 `secret_refs` 與該角色檔合法取得的 role-safe representation。
- 真玩家 PC 的角色檔不能替玩家預決定下一步行動。
- 四聲部若處於 `pl_pc` mode，Player Layer 屬 session/meta working data，不寫進角色檔當作 PC 內在心理；若處於 `npc` mode，也不要事後從 NPC 行為反推虛構的玩家偏好。
- 不得因名稱相同就跨 campaign 讀取另一團角色 master。

## Character-state recovery fuse

角色檔缺檔或缺欄位時，**不得**直接推論「該事實從未建立」。特別是已經完成創角並進入正式 runtime 的 PC，`missing record` 是資料完整性事件，不是角色世界事實。

處理順序固定為：

```text
1. 讀取 selected campaign manifest 指向的 characters/<pc> master。
2. 若檔案／欄位缺失，查同一 campaign 的創角 finalization / audit / explicit PL or user declarations。
3. 查同一 campaign 最新與歷史 sessions 中的 established character facts。
4. 查 source-backed character evidence / prior authoritative migration records。
5. 若 manifest 指明 legacy recovery refs，再查那些 legacy records；不得自行擴大到其他 campaign。
6. 找到既有建立事實 → 以原 provenance 回收進 selected campaign character master。
7. 只有完成上述 recovery search 仍無證據，才可標 unresolved / unknown。
```

禁止以下錯誤轉換：

```text
record missing -> fact never established
field omitted from live-state -> player never chose it
chat context absent -> character canon absent
other campaign has same-named PC -> reuse that PC state
```

`pending_recovery` 的語義是「已建立角色資料可能遺失／尚未回收到目前 authoritative layer」，不是 `NON_ASSERTION`、`PROHIBITED`，也不是允許重新生成互相衝突的新設定。

對牧師、誓約角色、結社角色等 Pass 7 必填身分欄位，若角色已正式開跑但 authoritative record 缺失，視為 **character-state integrity failure**：先回收，不要在場景內重新問玩家一次，也不要生成替代答案。
