# D100 GPT / Agent DM Repository

> 這個 repository 的目標，是讓 GPT／LLM／Agent 在不把 D100 誤讀成 D&D 3.5、CoC 或泛用 d100 的前提下，可靠地主持、測試與維護 D100 跑團。

## 快速開始

第一次進 repo：

```text
START_DM.md
```

`START_DM.md` 只負責 bootstrap；真正的 runtime 契約分散在以下上位文件：

- `AGENTS.md` — D100 Agent 操作契約與來源優先序
- `DATA_ARCHITECTURE.md` — 資料／狀態／module view／Cabinet／AO 的分層
- `RUNTIME_SOCIAL_WORLD_CONTRACT.md` — Alignment、Relationship Graph、Player Layer、Evidence/Causal Graph、秘密預承諾與 world commitments
- `DM_CABINET.md` — AO、圖書館員、讀心者、會計師與其他認知模塊
- `DM_PROTOCOL.md` — 實際主持流程與 Action Palette / Ledger
- `MYSTERY_PROTOCOL.md` — 祕密、認知危害、module clearance、EX、role-safe representation 與 Secret existence/release 分離

不要在 README 或 START_DM 維護第二套規則細節；規則內容應回到 core/source 文件。

---

## 架構一句話

```text
SOURCE DATABASE
→ NORMALIZED / INDEX DATA
→ WORLD / ACTOR / RELATIONSHIP / COMMITMENT / SESSION STATE
→ MYSTERY ROLE-SAFE VIEW
→ CABINET REASONING
→ AO RESOLUTION
→ STATE UPDATE
```

核心原則：

```text
資料不思考。
模塊不各自保存另一份世界真相。
Derived prediction 不是 established fact。
祕密不建立 Mystery 之外的 plaintext 平行資料庫。
秘密可以延遲揭露，但與玩家互動相關的核心因果必須先存在。
Relationship fact、actor belief、Analyst interpretation、Politician forecast 分層。
```

詳細見 `DATA_ARCHITECTURE.md` 與 `RUNTIME_SOCIAL_WORLD_CONTRACT.md`。

---

## 目錄結構

```text
00_core/             D100 curated 核心規則索引
01_skills/           技能／專長索引
02_items/            D100 物品／神器規則索引
90_srd_bridge/       D&D 3.5 SRD 補缺、轉譯與 calibration service
99_open_questions/   尚未解決的規則問題 registry
campaign/            該團目前成立的持久 world state
characters/          PC／重要 NPC state / capability records
examples/            regression tests / 範例，不參與世界決策
sessions/            Session live state／歷史紀錄
sources/             上游規則、raw mirror、角色證據與 GM 補答
templates/           actor / relationship / commitment / site / hazard 等資料 schema
```

### 主要資料來源

`source` 層：

```text
sources/sheet_mirror/          D100 Google Sheet 31/31 tabs raw mirror
sources/CHARACTER_EVIDENCE.md  角色卡／Actual Play 證據層
sources/GM_*.md                GM 補答／暫定／歷史證據
90_srd_bridge/                 外部 D&D 3.5 補缺來源與轉譯方法
```

`00_core/`、`01_skills/`、`02_items/` 是 runtime-friendly curated index，不是獨立人格模塊。

---

## 規則來源層級

衝突時仍依 `AGENTS.md`：

```text
當團明示 house rule
> 上游 D100 Sheet
> repo D100 canon
> clarified GM provisional
> D100 derived
> DM default
> SRD bridge
> raw D&D 3.5 SRD
```

`[GM_UNCERTAIN]`、`[OPEN_QUESTION]` 等狀態不得偽稱正典。

---

## Cabinet 與資料庫的邊界

Cabinet 不是資料庫。

- **圖書館員**：解析來源、版本、provenance、rule hierarchy；在 relationship runtime 中也解析關係事件／Evidence provenance bundle。
- **會計師**：物件持有、流轉、剩餘資源與未實現價值；可提供債務／共有資源等客觀 provenance。
- **碼表**：tactical windows / reactions / cooldowns。
- **沙漏**：world time / schedules / long processes / actor-faction commitments 的時間 view。
- **生態學家**：從 species、mechanical niche、環境、生存條件產生行為傾向。
- **分析師**：從合法證據讀取 S / I / R、alignment/persona/action 張力與 relationship structure，不直接決定行動。
- **政治家**：勢力、利益、承諾、資源、leverage、coalition 與二階反應。
- **詭祕**：classification、clearance、need-to-know、role-safe representation、EX；管理秘密可見度，不等玩家骰完才創造真相。
- **AO**：整合合法 views，裁定世界實際結果。

模塊輸出的是 constraint / hypothesis / proposal；只有實際世界事件或 AO 結算結果才寫回 state。

---

## 常用 State / Schema

### PC / Actor

```text
templates/PC_TEMPLATE.md
templates/CREATURE_WORLD_MODEL_TEMPLATE.md
```

Actor state 應區分：

```text
alignment
presented persona
current affect
belief
preference
constraint
capability
derived proposal
actual action
```

核心：

```text
alignment ≠ persona ≠ affect ≠ belief ≠ preference ≠ action
```

Alignment 是長期倫理／秩序座標與分析輸入，不是逐場戲的行動腳本。

### Relationship Graph

```text
templates/RELATIONSHIP_GRAPH_TEMPLATE.md
```

保存世界中真正成立的：

```text
關係 edge
已發生事件
承諾
債務
權力／依賴
共有資源
```

不保存分析師的「真正感情」解讀或政治家的未來預測。

### World Commitment

```text
templates/WORLD_COMMITMENT_TEMPLATE.md
```

採：

```text
lazy generation, early commitment
```

不必提前生成整座城市，但當某 hidden actor / secret / event 第一次即將可被玩家觀察或影響時，先鎖定足以支撐因果的最低限度 truth core、knowledge、goal、constraint、reaction cause、next step。

骰子決定的是：

```text
discovery / interference / consequence
```

不是：

```text
這個真相原本到底存不存在
```

### Evidence / Epistemic

玩家／PC 建立的是 Evidence Graph：

```text
OBSERVED
INFERRED
CONFIRMED
DISPROVEN
```

每個 actor 另外保存自己的 known facts / beliefs / misbeliefs。

Hidden Causal Graph 與角色 Evidence Graph 必須分開。

### Site

```text
templates/SITE_RECORD_TEMPLATE.md
```

地點是因果／資源／生態／控制狀態資料，不需要「地下城人格模塊」。

### Triggered Hazard / Object

```text
templates/TRIGGERED_HAZARD_TEMPLATE.md
```

吸收 3.5 Trap 的 `Sensor → Trigger → Effect → Reset / Bypass` 結構，但實際數值與判定仍依 D100。

### Session

```text
templates/SESSION_STATE_TEMPLATE.md
```

追：

- live state / Action Ledger；
- `four_voice_control.mode: npc | pl_pc`；
- Actor Epistemic Matrix；
- Evidence Ledger；
- Relationship refs；
- World Commitment refs；
- Secret refs；
- derived cache refs。

四聲部可以是高品質 autonomous NPC；只有使用者／DM 明確要求四聲部作為 PL+PC 時，才進入：

```text
Player Voice
→ Player decision
→ PC declaration / roleplay
→ DM resolution
```

不要把 NPC mode 的行為事後稱成玩家選擇。

---

## 祕密與 EX

所有秘密統一依 `MYSTERY_PROTOCOL.md`。

普通 campaign / character / session state 只保存：

```yaml
secret_refs:
  - secret_id: SECRET-...
    view: role_safe
```

不要另建：

```text
DM Secrets:
<完整 plaintext payload>
```

Secret 的兩件事必須分開：

```text
SECRET EXISTS
≠
SECRET IS REVEALED
```

核心真相可以早已存在、影響世界、被 NPC 知道，而玩家完全不知道。

如果 runtime 只有單一 LLM context、同一 context 已看過完整 payload，只能誠實標為 `SOFT_EX`；真正 `HARD_EX` 需要 storage / context / tool boundary。

---

## D&D 3.5 的位置

3.5 是：

```text
source adapter
semantic reference
conversion / calibration service
```

不是第二個 DM，也不是 Cabinet module。

可吸收其成熟資料結構，例如：

- Trap 的 Trigger / Reset / Bypass / Sensor
- Dungeon / Environment 的 site causal bundle
- Intelligent Item 的 autonomous agency 概念
- NPC attitude 作 relationship primitive
- Bluff 中「相信 ≠ 願意服從」的區分

但不得 raw 搬：

- AC / BAB / Fort / Ref / Will
- CR / HD
- d20 DC
- 6 秒 round action economy
- class progression

轉譯方法見 `90_srd_bridge/`。

---

## Character Dossiers

`sources/characters/*_OPERATIONAL_DOSSIER.md` 是 capability cache / evidence projection，不是固定行為 AI。

它們可以幫 runtime 快速取得：

```text
Action Palette
法術 effect index
物品
資源
live-state distinction
玩家已證實的使用偏好
```

但「下一輪一定怎麼打」「真正人格」「最高威脅目標」等應由當下合法 state 與 Cabinet 重新推理；若 cache 必須標 `derived` 並可失效。

---

## 缺規則時

依 `AGENTS.md` 與 `99_open_questions/`：

```text
先查 raw D100 source
→ curated rules
→ GM provisional / evidence
→ open question registry
→ 真缺資料才進 3.5 SRD bridge
→ 必要時做最小可逆裁定
```

不得拿熟悉的 3.5／CoC 習慣自動補成 D100 正典。

---

## Regression

架構或模型大改後跑：

```text
examples/ADJUDICATION_TESTS.md
```

創角流程改動另跑：

```text
examples/CHARACTER_CREATION_REGRESSION.md
```

典型跑偏包括：

- 自動使用 SAN / Fort / Ref / Will；
- 把 D100 一輪當 6 秒；
- raw 搬 3.5 數值；
- 高偵察創造不存在的視覺資訊；
- world data 升格成 AO instruction；
- Cabinet prediction 被寫成 established world fact；
- session / campaign / dossier 成為 Mystery 的旁路；
- Relationship fact / actor belief / derived interpretation 混層；
- Alignment 被當成逐場行動腳本；
- 四聲部 PL+PC mode 仍跳過 Player Layer；
- NPC mode 行為被事後稱為玩家偏好；
- 玩家骰點好壞反向決定 hidden truth 原本是什麼；
- 每種資料類型都新增一個人格模塊。

最終目標：

```text
少數真正會思考的模塊
+ 多個乾淨、無人格、可查詢的資料／狀態服務
+ 一個在玩家沒看著時仍有自己的關係、時間與因果的世界
```