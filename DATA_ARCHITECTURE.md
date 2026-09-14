# DATA_ARCHITECTURE.md — D100 Runtime Data Contract

> 狀態：架構契約。目的：把「資料、狀態、推理、裁定」分開，讓現有 Cabinet 模塊共用同一套世界資料，而不是各自養另一份真相。

## 0. 一句話原則

```text
SOURCE DATABASE
→ NORMALIZED / INDEX DATA
→ WORLD / SESSION STATE
→ ROLE-SAFE MODULE VIEW
→ CABINET REASONING
→ AO RESOLUTION
→ STATE UPDATE
```

核心保險絲：

```text
資料不思考。
模塊不保存自己的世界真相。
AO 不維護另一份平行資料庫。
同一世界事實只應有一個 authoritative state；各模塊取得的是 view。
```

---

## 1. Source Database — 來源層

來源層只保存「資料從哪裡來」，不做主持決策。

### D100

```text
sources/sheet_mirror/              上游 Google Sheet raw mirror
sources/CHARACTER_EVIDENCE.md      角色卡／Actual Play 證據
sources/GM_*.md                    GM 補答、暫定、歷史證據
```

### D&D 3.5

```text
90_srd_bridge/
```

3.5 是補缺／轉譯來源，不是另一個 DM。任何 3.5 內容進 D100 前先經 semantic conversion；不得讓 raw 3.5 數值或 action economy 直接覆蓋 D100。

### Source 層禁止事項

- 不因某來源「看起來合理」就自行決定世界結果。
- 不把 evidence 升格成 canon，除非來源層級允許。
- 不在 source mirror 內修正文義、補缺或偷偷正規化。

---

## 2. Normalized / Index Data — 語義與索引層

目前主要包括：

```text
00_core/
01_skills/
02_items/
90_srd_bridge/* conversion references
```

這一層將來源整理成可檢索、可運算的規則接口，但仍然**沒有世界決策權**。

例如：

```text
00_core/combat.md
```

可以告訴碼表／AO：「即時動作的合法窗口是什麼」。

但它不能自行決定：

> 這個 NPC 現在要不要用即時動作。

---

## 2.5 Character Build Working Data — 創角暫存層

創角／驗卡不是 world runtime；在角色正式接受前，需要一層**暫時的 meta working data**。

由：

```text
CHARACTER_CREATION_PROTOCOL.md
Character Builder / Validator
Build Ledger
```

共同使用。

可暫存：

```text
base / adjusted / bonus CP
候選技能／專長
marginal CP cost
prerequisite status
review flags
qualifying melee/spell CP working ledger
reward HP/SP working rolls
50 / 100 CP counterfactual build
reserve plan candidate
required-player-field checklist
```

這些不是世界事實。

特別區分：

```text
候選技能 ≠ 角色已學會
生態學家 competence proposal ≠ 背景既定事實
review flag ≠ 世界中的標籤
counterfactual build ≠ 角色能力
reserved CP ≠ 世界內貨幣
```

只有創角 final validation 通過後，orchestrator 才把**被接受的結果**投影到 `characters/*.md`：

- 實際屬性／技能／專長；
- final CP ledger snapshot；
- 語言；
- 信仰／領域／師承等已確認身分資料；
- reward HP/SP 結果；
- 起始裝備；
- resolved review provenance。

未採用候選、反事實 build、模塊 proposal 不應混入 authoritative character state。

若創角背景含秘密，working data 也不得建立 plaintext secret payload；照 `MYSTERY_PROTOCOL.md` 使用 Secret ID / role-safe representation。

創角完成後，暫存工作資料可以丟棄；需要留 audit 時只留可追溯的 final ledger / review notes，不保留平行角色版本當「真正角色」。

---

## 3. World / Session State — 唯一世界狀態層

世界中「目前真的成立什麼」只放在 state layer。

主要容器：

```text
campaign/current_state.md
characters/*.md
sessions/*.md
templates/CREATURE_WORLD_MODEL_TEMPLATE.md 的實例
其他 Entity / Site / Hazard record
```

State 可以記錄：

```text
位置
HP / SP
持有物
active effects
NPC 生死
世界時間
勢力狀態
已發生事件
角色目前 beliefs
trigger / cooldown / reset 狀態
```

State 不應保存：

```text
「生態學家認為他下一輪應該逃跑」
「分析師認為他的真正人格是……」
「政治家認為這個國家一定會宣戰」
「Character Builder 曾考慮讓他買某技能」
```

這些屬於 derived reasoning / build working data，不是 world fact。

---

## 4. Mystery Gate — 所有祕密資料的存取閘門

所有秘密依 `MYSTERY_PROTOCOL.md` 管理。

禁止建立新的 plaintext 平行秘密庫，例如：

```text
DM Secrets:
完整秘密內容……
```

普通 state 只能保存：

```yaml
secret_refs:
  - secret_id: SECRET-...
    view: session_safe
```

或該 state 合法取得的 role-safe representation。

完整 payload 若屬 Mystery Vault，不得為了方便複製進：

- session log
- campaign current state
- character dossier
- creature template
- module scratch state
- source cache
- character-build working data

---

## 5. Module View — Cabinet 只讀取自己的投影

Cabinet 模塊不是資料庫。它們取得同一 world state 的不同 view。

### 圖書館員 / Source Resolver

讀取：

```text
source provenance
rule hierarchy
source conflicts
版本
已知 evidence
```

輸出：

```text
可引用的規則／來源
可信度／權威層級
尚未解決的缺口
```

創角模式下可依 `CHARACTER_CREATION_PROTOCOL.md` 額外輸出候選技能／專長與 source-gap candidates；這些仍屬 working proposal，不是角色 state。

不決定角色行動或世界結果。

### 會計師

讀取：

```text
holder
origin
quantity / charges
ownership
transfer history
unrealized value
```

不負責判斷物件規則，也不決定世界因果。CP 屬創角 meta budget，不進會計師帳；起始物品 final 後才進 holder/origin tracking。

### 碼表

讀取：

```text
action palette
reaction windows
cooldowns
per-round rights
trigger timing
```

維護 tactical clock，不決定角色慾望。

### 沙漏

讀取：

```text
world time
travel / schedules
long-duration effects
reinforcements
patrol / supply / decay
```

維護 world clock，不為故事等待玩家。

### 生態學家

讀取：

```text
species / body / habitat
mechanical niche
survival needs
current environment
current goals
observed behavior
```

輸出可撤回的行為傾向；不把傾向寫成 world fact。

創角模式下亦可讀取年齡、教育、工作、旅行與組織經歷，提出 lived-experience competence domains；不直接指定技能等級或 CP。

### 分析師

讀取：

```text
角色有權被分析的結構證據
self-image
roles / obligations
behavior history
```

輸出 S / I / R 結構與 residual；不直接決定下一步行動，也不是一般創角技能推薦的預設來源。

### 政治家

讀取：

```text
factions
resources
commitments
reputation
threats
known political information
```

輸出利益與二階反應；不直接改寫 faction state。

### 詭祕

決定資訊 view、classification、clearance、need-to-know、EX；不決定世界實際發生什麼。

### AO

整合合法 module views 與世界事實，回答：

> 如果沒有人為了劇情方便作弊，世界現在實際會發生什麼？

創角時只在稀有／世界尺度 review 上提供 plausibility constraints，不參與普通 build optimization。

AO 的輸出經 orchestrator 寫回 state。

---

## 6. Derived Cache — 可保存，但必須可失效

某些昂貴推理結果可以 cache，例如：

```text
combat doctrine
current threat model
likely escape route
relationship interpretation
political reaction forecast
```

但必須標為 derived：

```yaml
derived_view:
  generated_from:
    - state_ref_a
    - state_ref_b
  generated_at:
  valid_until:
  invalidated_by:
```

重要：

```text
Derived cache ≠ world fact
```

當基礎 state、知識、傷勢、位置、命令、秘密揭露或能力狀態改變時，舊 cache 可直接失效。

---

## 7. Actor Data — Belief、Preference、Action 分離

對有 agency 的角色／生物／物件，至少區分：

```text
belief      = 它認為世界是什麼
preference  = 它想要／避免什麼
constraint  = 義務、命令、身體、規則、資源限制
proposal    = 模塊推導出的行動候選
actual      = AO 結算後實際發生的行動
```

核心保險絲：

```text
相信某件事 ≠ 願意配合某件事
想做某件事 ≠ 有能力做到
有能力做到 ≠ 會選擇去做
```

這個拆分可承接 D&D 3.5 Bluff 中「相信謊言」與「願不願做違反自身利益的事」的差異，但不直接搬 3.5 數值。

---

## 8. Entity Agency

物件不再只有「死物 / NPC」二元。

```yaml
agency:
  type: none | reactive | autonomous
```

### none

普通物件。主要由會計師、圖書館員、AO處理。

### reactive

只在條件成立時觸發，例如：神器回應、符文、警報裝置。

接：

```text
Triggered Hazard / Object schema
+ 碼表
+ AO
+ 詭祕（如有隱藏機制）
```

### autonomous

具有自身感官、belief、preference、目的與行動能力，例如智能魔法物品、意識載具、寄生體。

它同時是：

```text
Entity / Actor
+ 會計師追蹤的物件（若可被持有）
```

可進入分析師、生態學家、政治家等一般 actor pipeline。

---

## 9. Triggered Hazard / Object Schema

吸收 3.5 trap schema 的乾淨結構，但只保留語義，不直接搬 DC／數值。

```yaml
id:
type:
sensors:
trigger_predicate:
effect:
reset:
cooldown:
bypass:
discoverability:
disable_interface:
current_state:
secret_refs:
```

典型資料流：

```text
Sensor / world state
→ AO 判斷 trigger predicate
→ 碼表決定 timing window
→ effect 依 D100 接口結算
→ state 更新
```

這適用：

- 陷阱
- 警報器
- 感應門
- 符文
- 自動砲塔
- 條件式神器
- 定時裝置
- 魔法守衛

不需要建立「陷阱模塊」。

---

## 10. Site Record

吸收 3.5 dungeon / environment 的因果資料，但不建立「地下城人格」。

```yaml
site_id:
site_type:
construction:
current_occupants:
access:
materials:
supplies:
maintenance:
patrols:
communication:
terrain:
ecology:
decay:
resources:
secret_refs:
```

Projection：

```text
AO        → 物理／空間／建築因果
生態學家   → 棲地／食物／生物
政治家     → 控制權／守衛／組織
沙漏       → 巡邏／補給／腐敗／時間演進
會計師     → 資源／財物／供給
詭祕       → 隱藏區域／秘密機制的 view
```

---

## 11. 3.5 Integration Contract

`90_srd_bridge/` 是：

```text
Source Adapter
Conversion Reference
Calibration Service
```

不是 Cabinet module。

特別保留現行優點：

```text
不要換數字；先換原數字的功能。
AC 拆層。
world time 與 tactical windows 分離。
CR 不直接換 D100 數值。
Lineage conversion 與 Encounter calibration 分開。
```

可以從 3.5 吸收 schema／概念：

- Trigger / Reset / Bypass / Sensor
- Site causal bundle
- Intelligent item agency
- NPC attitude 作 relationship primitive
- belief 與 compliance 分離
- character class culture / class-related language 作缺漏偵測線索

不新增對應人格模塊，也不把 raw 3.5 class skill 直接升格為 D100 hard gate。

---

## 12. Legacy Path Migration

### 應保留但降權為資料／服務

```text
sources/*
00_core/*
01_skills/*
02_items/*
90_srd_bridge/*
99_open_questions/*
examples/*
```

### 應重新定義

```text
templates/CREATURE_WORLD_MODEL_TEMPLATE.md
→ Actor / Creature state record + derived-view slots

sources/characters/*_OPERATIONAL_DOSSIER.md
→ character capability cache / evidence projection
→ 不再是硬編行為腳本

SESSION / CAMPAIGN secrets
→ Mystery Secret ID / role-safe view
```

### 應避免再新增

```text
新的 DM plaintext secret store
新的「某種資料＝一個人格模塊」
模塊各自保存平行 NPC 真相
把 derived prediction 寫成 established fact
把創角候選／counterfactual build 寫成角色既定能力
```

---

## 13. Runtime 最小循環

```text
1. Orchestrator 讀取 relevant state。
2. 圖書館員解析需要的規則／來源。
3. 詭祕產生各模塊合法 view。
4. 只召喚相關 Cabinet 模塊。
5. 模塊輸出 constraint / hypothesis / proposal，不直接寫世界。
6. AO 整合並裁定世界實際結果。
7. Orchestrator 將結果寫回唯一 state。
8. 任何受影響的 derived cache 失效或重算。
```

### 創角最小循環

```text
1. Character Builder 讀 source / normalized rules 與 creation working data。
2. 圖書館員枚舉合法候選與 provenance。
3. 生態學家只在需要時提出 lived-experience competence domains。
4. Build Ledger 計 CP / prerequisite / qualifying pools / reward working values。
5. 稀有或世界尺度 review 才喚起 AO；秘密走 Mystery。
6. final validation。
7. Orchestrator 只把被接受的 final build 寫入 character state。
8. 丟棄未採用候選與 counterfactual working data。
```

最終目標：

```text
少數真正會思考的模塊
+ 多個乾淨、無人格、可查詢的資料／狀態服務
```
