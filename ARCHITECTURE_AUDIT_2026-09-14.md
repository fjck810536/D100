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

`t​​emplates/CREATURE_WORLD_MODEL_TEMPLATE.md` 已從：

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

### Bootstrap 已瘦身

已修改：

```text
START_DM.md
README.md
```

入口文件現在以導航為主，不再重複保存完整 D100 公式與 AO policy。

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

## 5. 尚待第二輪檢查

以下不是目前已確認錯誤，而是仍值得逐檔確認的 migration debt：

### A. 個別 Operational Dossier

```text
sources/characters/ADELE_OPERATIONAL_DOSSIER.md
sources/characters/KALAND_OPERATIONAL_DOSSIER.md
sources/characters/SATHERA_OPERATIONAL_DOSSIER.md
```

需確認是否仍有：

- 固定 action priority
- deterministic combat doctrine
- plaintext secrets
- 把玩家歷史偏好寫成未來必然行動

若只有 capability / effect index / evidence，保留即可。

### B. AGENTS.md boot list

`START_DM.md` 與 `README.md` 已指向 `DATA_ARCHITECTURE.md`；仍可考慮下一輪把 `AGENTS.md` 的開團必讀列表也直接加入它，讓任何不經 START_DM 的 runtime 都不漏讀資料契約。

### C. DM_PROTOCOL.md

目前仍應保留 orchestrator 流程；下一輪只需確認：

- 沒有 secretly owning world state
- 沒有和碼表／沙漏重複成第二個時間模塊
- Action Palette 是 runtime view，不是第三份角色卡

### D. 個別 artifact / item records

確認舊實例是否仍使用：

```text
DM秘密:
```

應逐步改為：

```text
secret_refs:
```

### E. campaign / session 歷史檔

未來若已有真實歷史檔，migration 原則是：

```text
保留歷史事件
移除／隔離不應存在於該 view 的 plaintext payload
建立 Secret ID lineage
```

不要為了清架構而刪掉已發生世界歷史。

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

這是後續所有 repo 清理的判準。
