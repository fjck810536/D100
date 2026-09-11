# D100 — GPT Dungeon Master Rules Repository

這個 repository 的目的，是讓 GPT／其他 LLM 在讀取本 repo 後，可以**以 D100 規則扮演 DM**，而不是退回原版 D&D 3.5、CoC 或其他 d100 系統。

## 起始閱讀順序

DM／Agent 開始跑團前，依序閱讀：

1. [`AGENTS.md`](AGENTS.md) — 規則優先序、禁止事項、DM 行為
2. [`DM_PROTOCOL.md`](DM_PROTOCOL.md) — 實際主持流程與資訊控制
3. [`00_core/checks.md`](00_core/checks.md) — D100 判定核心
4. [`00_core/character_creation.md`](00_core/character_creation.md) — 九大屬性、技能基礎、抗性、特殊判定、CP
5. [`00_core/combat.md`](00_core/combat.md) — 宣告、行動、攻擊、閃避、傷害、1 秒輪
6. [`00_core/magic.md`](00_core/magic.md) — 施法者、法術位、SP、連續施法、法抗
7. [`01_skills/core_skills.md`](01_skills/core_skills.md) — DM 常用技能語義
8. [`02_items/artifacts.md`](02_items/artifacts.md) — 聖器／亞神器／神器的處理邊界
9. [`90_srd_bridge/conversion_rules.md`](90_srd_bridge/conversion_rules.md) — D&D 3.5 SRD 只作補缺，不覆蓋 D100
10. [`99_open_questions/unresolved_rules.md`](99_open_questions/unresolved_rules.md) — 尚未有正典答案的規則洞

若只是要立刻開一場短團，讀完 1–7 即可開始。

## 規則狀態標籤

本 repo 使用以下標籤避免 GPT 把推論講成原規則：

- **`[D100_CANON]`**：直接來自目前 D100 Google Sheet。
- **`[D100_DERIVED]`**：由 D100 明文公式或例子直接推出。
- **`[DM_DEFAULT]`**：原規則未明文時，本 repo 給 GPT 的暫定主持裁定；不是原作者正典。
- **`[SRD_BRIDGE]`**：由 D&D 3.5 SRD 補充概念後轉譯的候選規則。
- **`[OPEN_QUESTION]`**：資料不足，不得私自宣稱已有固定答案。

## 規則來源與優先序

目前上游正典是 Google Sheet **「D100專長表」**：

`https://docs.google.com/spreadsheets/d/1d4nl6ByhbEtOhutjlB6FYrMVzglKG7I5DuanO0l4Mww/edit`

此 repo 是為 GPT 跑團建立的**獨立 Markdown 鏡像／規則介面**。建立本 repo 時，上游 Sheet 僅被唯讀查閱，沒有修改內容或分享設定。

衝突時採用：

1. 使用者／該團明示 house rule
2. 上游 D100 Sheet 明文
3. 本 repo 的 `[D100_CANON]` 鏡像
4. 本 repo 的 `[D100_DERIVED]`
5. 本 repo 的 `[DM_DEFAULT]`
6. `[SRD_BRIDGE]`
7. 原版 D&D 3.5 SRD

**不得用較低順位規則覆蓋較高順位。**

## D100 不是什麼

D100 不是「把 D&D 的 d20 改成 d100」。目前系統具有：

- 九大屬性：STR / DEX / SKI / CON / RES / INT / WIS / CHA / SPI
- 六種技能基礎值
- 五大抗性
- 強韌／精神／靈魂三種特殊判定
- 百分骰與「過多少」成功餘裕
- 對抗檢定
- CP 購買技能與 CP 重骰
- 先宣告、後行動的戰鬥結構
- **每輪只有 1 秒**
- 自訂法術位、SP、連續施法懲罰、抗性與穿透
- 大量自訂專長、職業、詞綴與神器級內容

因此 DM 不得機械套用 3.5 的 BAB、AC、三豁免、6 秒輪、標準／移動動作經濟、CR、HD 或法術 DC。

## Repo 狀態

目前版本定位為 **DM-ready core v0.1**：足以主持調查、一般技能、戰鬥、施法、抗性與超自然效果；職業專屬能力、完整詞綴、完整法術庫與所有世界觀內容仍以來源 Sheet／之後的 Markdown 移植為準。
