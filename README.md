# D100 — GPT Dungeon Master Rules Repository

這個 repository 的目的，是讓 GPT／其他 LLM 在讀取本 repo 後，可以**以 D100 規則扮演 DM**，而不是退回原版 D&D 3.5、CoC 或其他 d100 系統。

## 最快啟動

如果你的目標只是「把這個 repo 給 GPT，讓它開始當 D100 DM」，直接叫它先讀：

[`START_DM.md`](START_DM.md)

這個入口會告訴模型要讀哪些核心規則、如何恢復 campaign，以及哪些 D&D／CoC 習慣禁止偷帶進來。

## 起始閱讀順序

DM／Agent 開始跑團前，依序閱讀：

1. [`AGENTS.md`](AGENTS.md) — 規則優先序、禁止事項、DM 行為
2. [`DM_PROTOCOL.md`](DM_PROTOCOL.md) — 實際主持流程與資訊控制
3. [`DM_CABINET.md`](DM_CABINET.md) — AO、讀心者、圖書館員、會計師等認知角色；是行為吸引子，不是僵硬 SOP
4. [`00_core/checks.md`](00_core/checks.md) — D100 判定核心
5. [`00_core/character_creation.md`](00_core/character_creation.md) — 九大屬性、技能基礎、CP、HP/SP
6. [`00_core/resistances.md`](00_core/resistances.md) — 五大抗性與強韌／精神／靈魂
7. [`00_core/combat.md`](00_core/combat.md) — 宣告、行動、攻擊、閃避、傷害、1 秒輪
8. [`00_core/magic.md`](00_core/magic.md) — 施法者、法術位、SP、連續施法、法抗
9. [`01_skills/core_skills.md`](01_skills/core_skills.md) — DM 常用技能語義
10. [`02_items/artifacts.md`](02_items/artifacts.md) — 聖器／亞神器／神器的處理邊界
11. [`sources/GM_PROVISIONAL_2026-09-12.md`](sources/GM_PROVISIONAL_2026-09-12.md) — GM 粗答；有方向但尚未完整正典化
12. [`90_srd_bridge/conversion_rules.md`](90_srd_bridge/conversion_rules.md) — D&D 3.5 SRD 只作補缺，不覆蓋 D100
13. [`99_open_questions/unresolved_rules.md`](99_open_questions/unresolved_rules.md) — 尚未有正典答案的規則洞

若只是要立刻開一場短團，至少讀完 1–9；若裁定碰到目前的規則洞，再讀 11–13。

## 有 Campaign 時的追加閱讀

恢復既有團務時，再依序讀：

1. [`campaign/house_rules.md`](campaign/house_rules.md)
2. [`campaign/current_state.md`](campaign/current_state.md)
3. `characters/` 內本場相關角色檔
4. [`sources/characters/README.md`](sources/characters/README.md) 與本場角色 Operational Dossier；現行三人可先讀 [`sources/characters/OPERATIONAL_PROFILE_V1.md`](sources/characters/OPERATIONAL_PROFILE_V1.md)
5. `sessions/` 內最新 session state

角色／session 建檔可直接使用：

- [`templates/PC_TEMPLATE.md`](templates/PC_TEMPLATE.md)
- [`templates/SESSION_STATE_TEMPLATE.md`](templates/SESSION_STATE_TEMPLATE.md)

## 規則狀態標籤

本 repo 使用以下標籤避免 GPT 把推論講成原規則：

- **`[D100_CANON]`**：直接來自目前 D100 Google Sheet。
- **`[D100_DERIVED]`**：由 D100 明文公式或例子直接推出。
- **`[GM_PROVISIONAL]`**：GM 已給出明確方向，但仍是粗答，尚未補成完整條文。
- **`[GM_UNCERTAIN]`**：GM 有記憶／傾向，但自己也不確定。
- **`[GM_UNANSWERED]`**：已提出問題，但 GM 尚未給完整答案。
- **`[GM_SECRET]`**：DM 側知道機制存在，但玩家端不應被揭露完整觸發與效果。
- **`[DM_DEFAULT]`**：原規則未明文時，本 repo 給 GPT 的暫定主持裁定；不是原作者正典。
- **`[SRD_BRIDGE]`**：由 D&D 3.5 SRD 補充概念後轉譯的候選規則。
- **`[OPEN_QUESTION]`**：資料不足，不得私自宣稱已有固定答案。

`GM_PROVISIONAL / GM_UNCERTAIN` 不會自動覆蓋明確的 Sheet 正典；若兩者衝突，應把衝突標出並等待補答／角色卡／原始來源釐清，而不是偷偷選一邊。

## 規則來源與優先序

目前上游正典是 Google Sheet **「D100專長表」**：

`https://docs.google.com/spreadsheets/d/1d4nl6ByhbEtOhutjlB6FYrMVzglKG7I5DuanO0l4Mww/edit`

此 repo 是為 GPT 跑團建立的**獨立 Markdown 鏡像／規則介面**。建立本 repo 時，上游 Sheet 僅被唯讀查閱，沒有修改內容或分享設定。

完整來源 tab 與目前移植狀態見 [`sources/SHEET_INDEX.md`](sources/SHEET_INDEX.md)。

衝突時採用：

1. 使用者／該團明示 house rule
2. 上游 D100 Sheet 明文
3. 本 repo 的 `[D100_CANON]` 鏡像
4. 已釐清且不與正典衝突的 `[GM_PROVISIONAL]`
5. 本 repo 的 `[D100_DERIVED]`
6. 本 repo 的 `[DM_DEFAULT]`
7. `[SRD_BRIDGE]`
8. 原版 D&D 3.5 SRD

**不得用較低順位規則覆蓋較高順位。** `[GM_UNCERTAIN]` 只用來提示追問方向，不應直接當裁定依據。

## D100 不是什麼

D100 不是「把 D&D 的 d20 改成 d100」。目前系統具有：

- 九大屬性：STR / DEX / SKI / CON / RES / INT / WIS / CHA / SPI
- 六種技能基礎值
- 五大抗性
- 強韌／精神／靈魂三種特殊判定
- 百分骰與「過多少」成功餘裕
- 至少一種數字總值式對抗（GM 粗答顯示控制可採 `d100 + 加值`）
- CP 購買技能與 CP 重骰
- 先宣告、後行動的戰鬥結構
- **每輪只有 1 秒**
- 自訂法術位、SP、連續施法懲罰、抗性與穿透
- 大量自訂專長、職業、詞綴與神器級內容

因此 DM 不得機械套用 3.5 的 BAB、AC、三豁免、6 秒輪、標準／移動動作經濟、CR、HD 或法術 DC。

## Repository 結構

```text
D100/
├─ README.md
├─ START_DM.md
├─ AGENTS.md
├─ DM_PROTOCOL.md
├─ DM_CABINET.md
├─ 00_core/
│  ├─ checks.md
│  ├─ character_creation.md
│  ├─ resistances.md
│  ├─ combat.md
│  └─ magic.md
├─ 01_skills/
│  └─ core_skills.md
├─ 02_items/
│  └─ artifacts.md
├─ 90_srd_bridge/
│  └─ conversion_rules.md
├─ 99_open_questions/
│  └─ unresolved_rules.md
├─ sources/
│  ├─ SHEET_INDEX.md
│  ├─ GM_PROVISIONAL_2026-09-12.md
│  └─ characters/
│     ├─ README.md
│     └─ OPERATIONAL_PROFILE_V1.md
├─ campaign/
│  ├─ README.md
│  ├─ house_rules.md
│  └─ current_state.md
├─ characters/
│  └─ README.md
├─ sessions/
│  └─ README.md
├─ templates/
│  ├─ PC_TEMPLATE.md
│  └─ SESSION_STATE_TEMPLATE.md
└─ examples/
   └─ ADJUDICATION_TESTS.md
```

## Regression 測試

[`examples/ADJUDICATION_TESTS.md`](examples/ADJUDICATION_TESTS.md) 收錄一組用來檢查 GPT 是否跑偏的裁定案例，包括：

- 飛箭陷阱
- 舊日支配者血液眷屬化
- 奪心魔抽魂
- 奈瑟瑞爾古魔法書
- 直視希瑞克化身
- 位面級神器魔法背景

換模型、改 DM 指令或修改核心規則後，可重跑這些案例作 smoke test。

## Repo 狀態

目前版本定位為 **DM-ready core v0.1**：已足以主持調查、一般技能、戰鬥、施法、抗性、超自然效果、神器裁定與 session 狀態管理。

但這**還不是 31 個 Sheet tab 的完整逐條離線轉錄版**。職業專屬能力、完整詞綴、完整法術庫、高級／傳奇專長、完整世界觀等，若情境需要而 repo 尚未鏡像，仍應唯讀查上游 Sheet；不得由 GPT 靠 3.5 記憶自行補完。