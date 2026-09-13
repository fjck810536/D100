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
```

## DM 規則

- 角色檔內的實際數值、能力、持有物與 established state 優先於聊天記憶。
- HP、SP、持續效果等即時變化可先記在 session state，session 結束再回寫需要永久保存的角色狀態。
- 不要替玩家補未選專長、未學技能、未持有裝備。
- 若角色檔缺少 P0 數值（例如目前未決的基礎移動），不要默認套 D&D 數值；先依該團 house rule 或已知角色表處理。
- 角色目前知道／相信什麼可存 epistemic state；分析師／生態學家的推測不能直接寫成角色「真正人格」。
- combat doctrine、threat model、未來行動預測若需要 cache，必須標 derived 並可失效。
- 完整祕密／EX payload 不直接寫進角色檔；只保存 `secret_refs` 與該角色檔合法取得的 role-safe representation。
- 真玩家 PC 的角色檔不能替玩家預決定下一步行動。
