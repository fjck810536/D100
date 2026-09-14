# characters/

每名 PC／重要 NPC 建議使用獨立 Markdown 檔，作為角色的 state / capability record。

建立 PC 時複製：

`templates/PC_TEMPLATE.md`

重要 NPC／怪物可使用：

`templates/CREATURE_WORLD_MODEL_TEMPLATE.md`

命名例：

```text
characters/alice.md
characters/bob.md
```

資料分層見：

```text
../DATA_ARCHITECTURE.md
../RUNTIME_SOCIAL_WORLD_CONTRACT.md
```

## DM 規則

- 角色檔內的實際數值、能力、Alignment、持有物與 established state 優先於聊天記憶。
- Alignment 是長期倫理／秩序座標與分析輸入，不是逐場戲的行動腳本；`alignment ≠ presented_persona ≠ current_affect ≠ action`。
- HP、SP、持續效果等即時變化可先記在 session state，session 結束再回寫需要永久保存的角色狀態。
- 不要替玩家補未選專長、未學技能、未持有裝備。
- 若角色檔缺少 P0 數值（例如目前未決的基礎移動），不要默認套 D&D 數值；先依該團 house rule 或已知角色表處理。
- 角色目前知道／相信什麼存 epistemic state；世界真相不等於角色知道真相。
- 客觀關係 facts 放共享 `Relationship Graph`；角色檔只保留 `relationship_refs`，不要把整張關係網複製進每張角卡。
- 分析師／生態學家／政治家的推測不能直接寫成角色「真正人格」或 established relationship fact。
- combat doctrine、threat model、relationship interpretation、political forecast、未來行動預測若需要 cache，必須標 derived 並可失效。
- 完整祕密／EX payload 不直接寫進角色檔；只保存 `secret_refs` 與該角色檔合法取得的 role-safe representation。
- 真玩家 PC 的角色檔不能替玩家預決定下一步行動。
- 四聲部若處於 `pl_pc` mode，Player Layer 屬 session/meta working data，不寫進角色檔當作 PC 內在心理；若處於 `npc` mode，也不要事後從 NPC 行為反推虛構的玩家偏好。