# Architecture Audit — 2026-09-14

> 目的：記錄「早期模塊／資料路徑考古」與第一輪 migration 結果，避免日後又把已拆掉的舊職責接回來。

## 1. 分類結論

### A. D100 source / database

```text
sources/sheet_mirror/
sources/CHARACTER_EVIDENCE.md
sources/GM_*.md
```

這些是資料／證據來源，不是 Cabinet module。

### B. D100 normalized / runtime index

```text
00_core/
01_skills/
02_items/
99_open_questions/
```

這些是規則索引／缺口 registry，不應自行決定 NPC 行為或世界結果。

### C. D&D 3.5 source / bridge

```text
90_srd_bridge/
```

定位：Source Adapter / Conversion Reference / Calibration Service。

禁止升格為第二個 DM 或 Cabinet module。

### D. State / data containers

```text
characters/
campaign/
sessions/
templates/PC_TEMPLATE.md
templates/CREATURE_WORLD_MODEL_TEMPLATE.md
templates/SITE_RECORD_TEMPLATE.md
templates/TRIGGERED_HAZARD_TEMPLATE.md
sources/characters/* dossier
```

這些保存 state、capability、evidence、refs；不應保存平行世界真相或 deterministic behavior policy。

### E. Runtime reasoning / authority

```text
DM_CABINET.md
DM_PROTOCOL.md
MYSTERY_PROTOCOL.md
AGENTS.md
```

- Cabinet 產生 hypothesis / constraint / proposal。
- AO 決定 actual world result。
- Orchestrator 寫回唯一 state。

---

## 2. 第一輪已完成 migration

### 新增共同資料契約

新增：

```text
DATA_ARCHITECTURE.md
```

固定資料流：

```text
SOURCE DATABASE
→ NORMALIZED / INDEX DATA
→ WORLD / SESSION STATE
→ MYSTERY ROLE-SAFE VIEW
→ CABINET REASONING
→ AO RESOLUTION
→ STATE UPDATE
```

### 新增無人格資料 schema

新增：

```text
templates/SITE_RECORD_TEMPLATE.md
templates/TRIGGERED_HAZARD_TEMPLATE.md
```

吸收 D&D 3.5 中值得保留的結構：

- Site / dungeon causal bundle
- Trap sensor / trigger / effect / reset / bypass

但不新增 Site Agent 或 Trap Agent。

### 舊 secrets path 已退休

已修改：

```text
templates/SESSION_STATE_TEMPLATE.md
campaign/current_state.md
campaign/README.md
sessions/README.md
templates/PC_TEMPLATE.md
02_items/artifacts.md
```

方向：

```text
plaintext DM Secrets
→ secret_refs + role-safe representation
```

完整 protected payload 統一由 `MYSTERY_PROTOCOL.md` 管理。

### Creature World Model 已拆腦留殼

`templates/CREATURE_WORLD_MODEL_TEMPLATE.md` 已從：

```text
state + ecology + personality + combat AI + epistemic model + AO-like decision
```

改成：

```text
Actor state + capability + evidence + epistemic state + derived cache slots
```

Combat Doctrine / Threat Model / 分析結果現在只能是 derived view，可因底層 state 改變而失效。

### Character Dossier 已降權

已修改：

```text
sources/characters/README.md
sources/characters/OPERATIONAL_PROFILE_V1.md
characters/README.md
```

現在 Dossier 定義為：

```text
capability cache / evidence projection
```

而不是：

```text
固定角色 AI / deterministic rotation / 真正人格資料庫
```

已 spot-check 亞黛兒、卡蘭德、莎緹拉三份個別 Dossier 的主要段落；目前看到的核心內容主要是數值、Action Palette、能力、物品、live-state 與來源警告，沒有發現需要立即刪除的獨立「角色 AI」。若日後某段開始被 runtime 當成固定戰術腳本，再局部降權即可。

### Bootstrap / Authority 已接線

已修改：

```text
START_DM.md
README.md
AGENTS.md
DM_CABINET.md
DM_PROTOCOL.md
```

現在：

- `START_DM.md` 只負責 bootstrap；
- `AGENTS.md` 把 `DATA_ARCHITECTURE.md` 列入開團必讀並禁止平行 state / plaintext secret store；
- `DM_CABINET.md` 明確規定 Cabinet 只產生 module views / hypotheses / forecasts；
- `DM_PROTOCOL.md` 明確規定 AO 結算後由 orchestrator 寫回 authoritative state，並使 derived cache 失效／重算；
- Action Palette 被定義為可重建的 runtime capability view，不是第三份角色卡。

---

## 3. 從 3.5 保留的好設計

### Triggered object schema

```text
Sensor
→ Trigger Predicate
→ Effect
→ Reset / Cooldown
→ Bypass
```

適用：陷阱、警報器、感應門、符文、自動砲塔、條件式神器。

### Belief ≠ Compliance

吸收 Bluff 的重要語義：

```text
相信對方說的是真的
≠
願意做違反自身利益／命令／人格的事情
```

Actor model 因此拆成：

```text
belief
preference
constraint
proposal
actual action
```

### Site causal bundle

地點類型提供物理／補給／巡邏／生態／控制權 constraints，不需要新 Agent。

### Intelligent Item agency

統一為：

```text
agency: none | reactive | autonomous
```

自主神器／意識載具／寄生體直接進 Actor pipeline，不新增「智能物品模塊」。

### NPC attitude

可作 relationship primitive，但不足以成為獨立模塊。

---

## 4. 明確不新增的「無聊模塊」

以下功能應保持 service / data primitive：

```text
Trap Agent
Site / Dungeon Agent
Relationship Attitude Agent
Conversion Agent 人格
Artifact Agent（除非 artifact 本身在世界內 autonomous）
```

圖書館員、碼表、沙漏、會計師雖然刻意「無聊」，但其窄職責有價值；不要因為想讓它們更有戲而擴張 scope。

---

## 5. 剩餘 migration debt

目前主要是**未來出現實例時的資料清理**，不是核心 runtime 還沒接好。

### A. 個別 artifact / item / NPC 舊實例

若舊實例仍使用：

```text
DM秘密:
```

應改為：

```text
secret_refs:
```

若舊 Creature / NPC record 把 combat doctrine 寫成固定人格真相，改成 derived cache 或 evidence。

### B. campaign / session 歷史檔

目前 campaign 尚未建立正式內容。未來若匯入真實歷史檔，migration 原則是：

```text
保留已發生世界歷史
保留角色實際取得的 knowledge / belief
移除／隔離不應存在於該 view 的 plaintext payload
建立 Secret ID lineage
```

不要為了清架構而刪掉已發生世界歷史。

### C. 個別 Dossier 深層段落

三份個別 Dossier 已完成主要段落 spot-check；不需要為了「格式純潔」先大改。後續只有在實際 runtime 出現以下 failure 時再局部處理：

- dossier 被當固定 action priority；
- 玩家過去偏好被當未來必然；
- secret payload 被直接塞入 dossier；
- derived interpretation 被誤當 established state。

---

## 6. Regression failure signals

若之後又出現以下情況，表示舊架構回流：

- 某個模塊自己維護一份和 world state 不同的「真正 NPC 狀態」。
- session / campaign / dossier 可以繞過 Mystery 讀完整秘密。
- Creature template 自己決定 NPC 下一步。
- 角色 Dossier 被當成固定 rotation。
- 3.5 conversion reference 開始直接主持 D100。
- 每增加一種資料類型就新增一個人格 Agent。
- AO 因為自己有資料庫副本，與其他 module view 不一致。
- derived forecast 被寫成 established fact。

---

## 7. 當前目標狀態

```text
少數真正會思考的模塊
+
多個乾淨、無人格、可查詢的資料／狀態服務
+
單一 authoritative world state
+
Mystery-controlled module views
```

核心 runtime 已完成第一輪接線；後續以實際壓測暴露的 failure 為主，不再為了分類完整繼續造模塊。
