# DATA_ARCHITECTURE.md — D100 Runtime Data Contract

> 狀態：架構契約。目的：把「資料、狀態、推理、裁定」分開，讓現有 Cabinet 模塊共用同一套世界資料，而不是各自養另一份真相。
>
> 社會關係、Alignment、PL/PC 控制與 Secret / World commitment 的跨模塊細則見 `RUNTIME_SOCIAL_WORLD_CONTRACT.md`。
> Campaign 選擇、manifest 與外部／本地 storage backend 邊界見 `BOOTSTRAP_PROTOCOL.md`、`CAMPAIGN_STORAGE_PROTOCOL.md`。

## 0. 一句話原則

```text
SOURCE DATABASE
→ NORMALIZED / INDEX DATA
→ SELECTED CAMPAIGN NAMESPACE
→ WORLD / ACTOR / RELATIONSHIP / COMMITMENT / SESSION STATE
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
同一 campaign 的同一世界事實只應有一個 authoritative state；各模塊取得的是 view。
不同 campaign namespace 互不共享 mutable state，除非經 explicit migration / promotion。
秘密可以延遲揭露，但與互動結果相關的核心因果必須在首次可觀察／可影響前 committed。
來源缺口不是生成禁令；生成採用後也不得冒充原文。
```

---

## 1. Source Database — 來源層

來源層只保存「資料從哪裡來」，不做主持決策。

### D100

```text
sources/sheet_mirror/              上游 Google Sheet raw mirror
sources/CHARACTER_EVIDENCE.md      角色卡／Actual Play 證據
sources/GM_*.md                    GM 補答、暫定、歷史證據
sources/spellbook/                   Spellbook 靜態拆包來源／匯入 provenance
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
- 不把「精確字串沒有命中」直接當作「所有來源都不存在」；應依 `sources/SHEET_INDEX.md`、語義分頁、交叉引用與 state provenance 繼續解析。
- 不把某 campaign storage 裡的自訂筆記冒充 D100 source；campaign storage 只對該團 state 有權威。

---

## 2. Normalized / Index Data — 語義與索引層

目前主要包括：

```text
00_core/
01_skills/
02_items/
03_spells/                           法術 lookup / compact catalog / source-scope index
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

### 2.1 Claim provenance / fit / status / owner 四維分離

任何具有設定含義、會被拿來導航、限制、結算、組織關係或角色發展的 claim，都不要只用一個 `canon / non-canon` 或 `confirmed / unconfirmed` 包辦所有問題。

至少分開：

| 維度 | 內容 |
|---|---|
| provenance | 原文、使用者校正、PL 決定、歷史裁定、creative addition、legacy generated；附來源 refs |
| fit | 支持點、衝突點、已查版本／範圍、未解欄位、追加假設 |
| status | hypothesis / proposed / committed / rejected / superseded |
| owner | 真人 PL、對應四聲部 PL、AO／世界流程、其他合法決定者 |

另保存：

```text
visibility
recorded_at
effective_from
decision_event_ref
```

最小資料形狀：

```yaml
claim_id:
subject_ref:
predicate:
value:
scope:

origin:
  generated: false
  kind: source-extraction | user-correction | pl-decision | creative-addition | legacy-generated
  source_refs: []
  contextual_support_refs: []
  created_by:
  created_at:

fit_review:
  checked_source_versions: []
  checked_state_ref:
  supporting_facts: []
  conflicts: []
  unresolved_fields: []
  added_assumptions: []
  judgment: supported | compatible | in-tension | conflicting | unknown

status: proposed
decision_owner:
decision_event_ref:
committed_at:
effective_from:
visibility_ref:
```

核心：

```text
source_refs 支持「原文寫了什麼」
contextual_support_refs 支持「這項創作為什麼合理」
兩者不可互換
```

同一 site / organization 的不同欄位可以有不同 origin。不要因為「名字在 Sheet 裡」就把整個地理、現任人員、權限、秘密一口氣洗成 canon；也不要因為其中一個欄位是 generated，就把已 source-backed 的部分全部降成生成。

### 2.2 Grounded generation adoption path

來源資料約束生成，但未定部分允許創作。合法資料流是：

```text
source / selected campaign state / user correction
→ Librarian source package
→ unresolved lookup 與 creative space 分開
→ relevant modules 形成具體 proposal
→ 合法 owner 決定
→ AO / PL adoption event
→ orchestrator 寫回 selected campaign 唯一 authoritative state
```

保險絲：

```text
SOURCE_GAP ≠ PROHIBITED
沒有原文地址 ≠ 世界永久沒有地址
proposal ≠ committed fact
committed generated fact ≠ source text
生成 origin 在採用後仍保留
```

若後來找到新原文：追加 source / fit review；不要抹掉「當初這個欄位是如何生成／採用」的歷史。若發生實質衝突，做局部 migration / supersede，不靜默重寫。

---

## 2.3 生成工作資料與隔離推演

跨模塊生成可在本次 working context 共用一份 proposal：新實體 refs、需要補齊的關係、接手模塊、來源回覆、候選比較與更新結果。它是 `derived/proposed` 工作資料；來源事實、候選假設及實際採用維持各自 provenance。地理與組織依賴的交接及完成方式依 `DM_PROTOCOL.md` 1.5，無需增加人格模塊或平行世界資料庫。

隔離測試的 working context 標記 `execution_mode: isolated_dry_run`、`baseline_ref` 與 `writeback: false`。`selected_proposal` 表示該次推演推薦，claim 仍為 `proposed`，`adoption_event_ref: null`；它不新增 campaign/session/actor/Mystery state，也不更新正式地圖、角色知情或 runtime fact cache。詳見 `DM_PROTOCOL.md` 1.6。

`examples/` 的測例與推演輸出屬測試資料，不能經搜尋、摘要、恢復 context 或 source package 變成某團已存在的地點／關係。正式採用要有另一次明確的 owner 決定與當時 state 核對。

### 2.4 Campaign Namespace / Storage Boundary

Persistent runtime 必須先有 selected campaign namespace。邏輯上：

```text
D100 repository
= immutable-ish rules / sources / protocols / templates

selected campaign storage
= mutable authoritative state for exactly one campaign instance
```

每一個 persistent campaign 對 runtime 至少呈現：

```text
/
├── manifest
├── current_state
├── characters/
├── sessions/
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

provider 可以是 repo-local、Google Drive、本機資料夾、獨立 Git 或其他 backend；state 語義不因 provider 改變。穩定 locator、讀寫能力與 failure behavior 依 `CAMPAIGN_STORAGE_PROTOCOL.md`。

三種生命週期必須分離：

```text
persistent_campaign = 正式／長期團；完整持久化
persistent_test     = 沙盒／測試團；同樣完整持久化，但 write_scope=self_only
isolated_dry_run    = 一次性隔離推演；writeback=false
```

`persistent_test` 不是「比較會存的 dry-run」。只要角色已 final、世界事件已 committed，它就必須和正式團一樣有完整 actor/world/session state；唯一差異是 namespace 與 promotion policy。

根目錄舊有：

```text
campaign/
characters/
sessions/
mystery_vault/
```

在 migration 完成前屬 legacy state location。它們可以被明確 legacy manifest／migration 引用，但**不是未選 campaign 時的隱含全域 current state**。

跨 campaign 規則：

```text
read/write selected campaign only
campaign A state ≠ campaign B state
promotion / import / migration = explicit operation
```

### 2.5 Character Build Working Data — 創角暫存層

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

只有創角 final validation 通過後，orchestrator 才把**被接受的結果**投影到 selected campaign 的 authoritative `characters/` store：

- 實際屬性／技能／專長；
- alignment；
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

## 3. World / Session State — Selected Campaign 唯一世界狀態層

世界中「目前真的成立什麼」只放在**目前 selected campaign** 的 state layer。

主要邏輯容器：

```text
<campaign-root>/manifest
<campaign-root>/current_state
<campaign-root>/characters/*
<campaign-root>/sessions/*
<campaign-root>/sites/*
<campaign-root>/relationships/*
<campaign-root>/commitments/*
<campaign-root>/mystery/*
```

模板仍由 D100 repo 提供：

```text
templates/CREATURE_WORLD_MODEL_TEMPLATE.md
templates/RELATIONSHIP_GRAPH_TEMPLATE.md
templates/WORLD_COMMITMENT_TEMPLATE.md
templates/SITE_RECORD_TEMPLATE.md
...
```

Provider 不一定有實體 filesystem；`<campaign-root>/characters/*` 等表示 logical record class。Manifest 應保存穩定 refs，避免下一個 runtime 靠名稱猜檔。

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
角色 alignment
角色目前 beliefs
Relationship facts / commitments / debts
Evidence Ledger status
world / actor commitments
trigger / cooldown / reset 狀態
adopted claim refs / decision events / site refs
```

State 不應保存：

```text
「生態學家認為他下一輪應該逃跑」
「分析師認為他的真正人格是……」
「政治家認為這個國家一定會宣戰」
「Character Builder 曾考慮讓他買某技能」
```

這些屬於 derived reasoning / build working data，不是 world fact。

### Cross-campaign isolation

任何 state read/write 都必須帶著已解析的 campaign identity。禁止：

```text
campaign A character -> campaign B session
campaign B site -> campaign A current_state
persistent_test -> persistent_campaign implicit promotion
legacy root snapshot -> selected campaign master overwrite
```

若要 import / clone / promote / migrate，建立明確 migration event，保留來源 campaign、record refs、時間與衝突處理；不能用一般 runtime write 偽裝成 migration。

### Relationship facts 與 actor belief 分離

共享 Relationship Graph 只存該 campaign 世界中已成立的 edge / event / commitment。

角色「如何理解那段關係」仍放在各 actor 的 Epistemic State / self-image / derived analysis，不因 relationship edge 存在就自動共享。

### Evidence Ledger

調查所得 proposition 至少區分：

```text
OBSERVED
INFERRED
CONFIRMED
DISPROVEN
```

Evidence status 可以進 state；「這條 evidence 最終代表什麼深層真相」若尚未確認，不得提前升格。

### Recorded time 與 world-effective time 分離

後來補 provenance、site record 或 repair event，不代表該事物在補錄當天才出現在世界裡；同樣不能偽稱它在先前檢定前已經寫進後台。

```text
recorded_at = 何時把資料寫進 campaign store
effective_from = 世界內從何時成立／本次採用如何追溯
```

歷史 commitment 缺口應誠實記為 migration / legacy-generated，而不是偽造舊 timestamp。

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

外部 campaign storage 若承載 Mystery records，也不會因此降低 classification／clearance。Backend capability 與 Mystery visibility 是兩個不同邊界。

### Secret existence 與 Secret release 分離

Mystery Gate 決定誰可以知道、知道多少、何時揭露；它不應等到玩家檢定後才創造核心秘密。

當某個秘密／陰謀／hidden actor state 即將第一次成為玩家可觀察或可影響的因果來源時，應先建立最小 World Commitment / Mystery truth core，再進行角色行動與擲骰。

---

## 5. Module View — Cabinet 只讀取自己的投影

Cabinet 模塊不是資料庫。它們取得同一 selected campaign world state 的不同 view。

### 圖書館員 / Source Resolver

讀取：

```text
source provenance
rule hierarchy
source conflicts
版本
已知 evidence
relationship event provenance
commitment / promise history
entity / institution cross-references
source indexes / semantic navigation
```

輸出：

```text
可引用的規則／來源
可信度／權威層級
尚未解決的缺口
Relationship Graph / Evidence Ledger 的來源鏈
resolved entity / alias candidates
searched scope
unresolved_lookup
creative_space
```

創角模式下可依 `CHARACTER_CREATION_PROTOCOL.md` 額外輸出候選技能／專長與 source-gap candidates；這些仍屬 working proposal，不是角色 state。

圖書館員可以替分析師／政治家解析「這段關係是由哪些已發生事件建立」，但不替它們解讀心理或預測未來。

不決定角色行動或世界結果；但 source resolver 必須把查得資料交成**下游可使用**的 package，不以「找到條目」本身作為完成。

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

若債務／共有資源已成為客觀 relationship fact，會計師可以提供其財務／持有 provenance，但不替分析師解讀「所以兩人感情如何」。

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
actor / faction commitments with time triggers
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
alignment
presented persona
current affect
self-image
roles / obligations
Relationship Graph 的合法 view
Epistemic State
behavior history
```

輸出 S / I / R、alignment tension、relationship interpretation 與 residual；不直接決定下一步行動，也不是一般創角技能推薦的預設來源。

Alignment 不等於行動腳本；分析師必須允許 alignment、persona、affect、actual action 彼此不一致。

### 政治家

讀取：

```text
factions
resources
commitments
Relationship Graph 的合法 view
reputation
threats
known political information
```

輸出利益、leverage、coalition / conflict incentives 與二階反應；不直接改寫 faction / relationship state。

### 詭祕

決定資訊 view、classification、clearance、need-to-know、EX；管理 Secret truth / evidence 的可見度，不決定世界實際發生什麼，也不因玩家骰點創造秘密。

### AO

整合合法 module views 與 selected campaign 世界事實，回答：

> 如果沒有人為了劇情方便作弊，世界現在實際會發生什麼？

創角時只在稀有／世界尺度 review 上提供 plausibility constraints，不參與普通 build optimization。

AO 的輸出經 orchestrator 寫回 selected campaign state。

### 模塊協作不是停止條件

模塊邊界用來分責任、來源、決定權與可見度，不是讓工作在邊界前停止。

```text
模塊發現自己的 proposal 缺來源前提
→ 向圖書館員／相關模塊追問
→ 收到資料
→ 更新自己的 proposal
→ 有權者決定
```

例如政治家需要地方據點與總部關係、分析師需要真實師承／職務、生態學家需要當地生活條件，都可以主動請求前置資料。Orchestrator 負責讓工作有人接、成果有去處。

---

## 6. Derived Cache — 可保存，但必須可失效

某些昂貴推理結果可以 cache，例如：

```text
combat doctrine
current threat model
likely escape route
relationship interpretation
alignment tension analysis
political reaction forecast
likely betrayal
player-intent hypothesis
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

當基礎 state、知識、傷勢、位置、命令、秘密揭露、relationship edge、alignment 明示轉變、玩家重新解釋自己的 PC 或能力狀態改變時，舊 cache 可直接失效。

Derived cache 不得比它所依賴的 evidence 活得更久，也不得跨 campaign namespace 無標記重用。

---

## 7. Actor Data — Alignment、Belief、Preference、Action 分離

對有 agency 的角色／生物／物件，至少區分：

```text
alignment        = 長期倫理／秩序座標；不是當下行動命令
presented_persona = 對外呈現／可觀察形象
current_affect   = 當下情緒／激發狀態
belief           = 它認為世界是什麼
preference       = 它想要／避免什麼
constraint       = 義務、命令、身體、規則、資源限制
proposal         = 模塊推導出的行動候選
actual           = AO 結算後實際發生的行動
```

核心保險絲：

```text
alignment ≠ presented persona ≠ current affect ≠ action
相信某件事 ≠ 願意配合某件事
想做某件事 ≠ 有能力做到
有能力做到 ≠ 會選擇去做
```

這個拆分可承接 D&D 3.5 Bluff 中「相信謊言」與「願不願做違反自身利益的事」的差異，但不直接搬 3.5 數值。

### 7.1 真玩家／PL+PC 的 Player Layer 不屬於 Actor Data

Player agenda / current interest / risk tolerance / interpretation of PC 是 meta working data，不是角色世界內心理。

四聲部在 `pl_pc` mode 時，必須保留：

```text
Player Voice decision
→ PC declaration
```

的中間層；不能把 DM 直接生成的 PC 行動事後稱為玩家選擇。

---

## 7.5 Relationship Graph / Epistemic Matrix

Relationship Graph 使用 `templates/RELATIONSHIP_GRAPH_TEMPLATE.md`。

核心區分：

```text
Relationship Fact       = 世界中真的成立的關係／承諾／債務／事件
Actor Epistemic State   = 這個 actor 知道／相信／誤信什麼
Analyst View            = 對關係與角色結構的 derived interpretation
Politician View         = 對 leverage / coalition / second-order effect 的 forecast
```

不要再用單一 `Relationship / Knowledge State` 混寫以上四層。

---

## 7.6 World Commitment / Early Causal Commitment

當 NPC、事件、秘密、裝置、faction plan 即將第一次成為玩家**可觀察或可影響**的因果來源時，先依 `templates/WORLD_COMMITMENT_TEMPLATE.md` 建立最小 hidden state，並把 commitment 寫入 selected campaign namespace。

原則：

```text
lazy generation, early commitment
```

可以晚生成 incidental surface detail；但與玩家互動結果相關的 `truth_core / relevant knowledge / goal / constraint / intended next step / reaction cause` 必須先 committed。

禁止：

```text
骰成功 → 才決定這個人原來是重要間諜
骰失敗 → 才決定這個人其實只是普通路人
```

骰子只決定發現、干涉與後果，不決定已 committed 的真相「原本是什麼」。

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
Sensor / selected campaign world state
→ AO 判斷 trigger predicate
→ 碼表決定 timing window
→ effect 依 D100 接口結算
→ selected campaign state 更新
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

使用 `templates/SITE_RECORD_TEMPLATE.md`。Site record 除了物理／控制／生態／資源 state，還必須能逐 claim 保留 provenance、generated origin、採用事件、effective time 與 map visibility。

Projection：

```text
AO        → 物理／空間／建築因果
生態學家   → 棲地／食物／生物
政治家     → 控制權／守衛／組織
沙漏       → 巡邏／補給／腐敗／時間演進
會計師     → 資源／財物／供給
圖書館員   → provenance / source gap / cross-reference
詭祕       → 隱藏區域／秘密機制的 view
```

Site instance 屬 selected campaign state；template 與共用世界 source 屬 repo。兩者不可混層。

---

## 11. 3.5 Integration Contract

`90_srd_bridge/` 是：

```text
Source Adapter
Conversion Reference
Calibration Service
```

不是 Cabinet module，也不是 campaign storage backend。

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

### Legacy root-level campaign state

現有根目錄：

```text
campaign/*
characters/*
sessions/*
mystery_vault/*
```

在新 bootstrap/storage 架構下視為 **legacy campaign storage**，不是所有未來團共用的全域 state。

Migration 原則：

```text
先辨識哪些 records 屬於同一歷史 campaign/test campaign
→ 建立該 campaign manifest
→ 建立／選定新 campaign root
→ 依 provenance 搬移或建立 stable refs
→ 驗證 character master / current state / live session / site / Mystery refs
→ 完成後才停止依賴 legacy root paths
```

不得把多個歷史測試團因為都在 repo 根目錄就合併成同一 campaign。

### 應重新定義

```text
templates/CREATURE_WORLD_MODEL_TEMPLATE.md
→ Actor / Creature state record + derived-view slots

sources/characters/*_OPERATIONAL_DOSSIER.md
→ character capability cache / evidence projection
→ 不再是硬編行為腳本

SESSION / CAMPAIGN secrets
→ Mystery Secret ID / role-safe view

Relationship / Knowledge mixed notes
→ Relationship Graph + Actor Epistemic Matrix + Evidence Ledger + derived views
```

### Provenance repair

既有 session 中已經對玩家呈現、但當時沒有留下 Librarian / generation trace 的設定，不直接刪除，也不偽造先前已完成查核：

```text
保留無衝突的既成世界／已發生事件
→ 現在補查來源
→ source-backed 部分補 source refs
→ 使用者校正標 user-correction
→ 舊生成標 legacy-generated
→ 補 repair/adoption event
→ 只在實質衝突處做最小 migration
```

不重骰、不回收已合法花掉的資源、不為了修 provenance 把世界倒回舊 checkpoint。

### 應避免再新增

```text
新的 DM plaintext secret store
新的「某種資料＝一個人格模塊」
模塊各自保存平行 NPC 真相
把 derived prediction 寫成 established fact
把創角候選／counterfactual build 寫成角色既定能力
把 NPC mode 的四聲部行為事後包裝成 Player choice
把新 campaign 寫回未指定的 root-level legacy state
```

---

## 13. Runtime 最小循環

```text
0. Bootstrap：解析 selected campaign manifest / storage root / ruleset ref。若沒有 selected campaign，停留 bootstrap，不進 scene runtime。
1. Orchestrator 只讀 selected campaign relevant authoritative state 與最新 session，而不是用其他 campaign、空白或舊 checkpoint 蓋掉已發生進度。
2. 辨識輸入層與目的：DM / OOC-PL / PC 台詞 / PC 內心 / 行動宣告 / narrator addition。
3. 解析本次要實際使用的 entities / claims / relations；保存原稱呼與可能 alias，不先把玩家用詞正規化成世界真相。
4. 若 narrator / NPC / AO 要把設定 claim 用於地圖、導航、機構關係、限制、資源、角色發展或結算，圖書館員先解析來源或使用仍有效的 source cache；精確搜尋 miss 時改走 Sheet index、語義分頁與交叉引用。
5. 圖書館員交付可使用的 source package：原文／user correction／selected campaign state refs／cross-reference／conflicts／searched scope，並把 `unresolved_lookup` 與 `creative_space` 分開。
6. 詭祕只在需要時產生 role-safe view；角色未知不代表後台停止工作。
7. 相關 Cabinet 模塊使用 source package 形成具體人物／制度／環境／行動 proposal；缺前提就主動向圖書館員／其他模塊追問。
8. 在可創作空間內產生有內容的 grounded proposal。`SOURCE_GAP` 不是拒絕理由；已有事實、硬衝突、Mystery 與 owner 權限仍是約束。
9. PL+PC 關鍵選擇交 Player Voice；NPC／世界發展交 AO。合法 owner 採用後留下 decision event / provenance。
10. 對即將首次可觀察／可影響、尤其會影響檢定的 hidden core 建立／確認最小 World Commitment。最小承諾是因果底線，不是世界生成上限。
11. 主動把角色合理可知、與眼前理解／選擇相關的成果帶入敘事、對話、地圖與可行動入口；具體秘密依 Mystery / epistemic state 交付。
12. 依 D100 結算需要的行動／骰點。
13. Orchestrator 將實際結果與 adopted claims 寫回 selected campaign 唯一 state，包括 relationship / epistemic / evidence / site / world-clock 變化。
14. 任何受影響的 derived cache / source resolution cache 失效或重算。
15. Storage write verification：確認 record update 成功；若 backend 寫入失敗，不得宣稱已存檔。
16. Completion check：查核是否真的有可定位結果、結果是否被下游使用、採用是否有 owner/state record、前台是否有可感知／可行動成果。缺什麼就派回對應工作補完。
```

### 創角最小循環

```text
1. Character Builder 讀 source / normalized rules 與 creation working data。
2. 取得／建立角色 concept 與 alignment。
3. 圖書館員枚舉合法候選與 provenance。
4. 生態學家只在需要時提出 lived-experience competence domains。
5. Build Ledger 計 CP / prerequisite / qualifying pools / reward working values。
6. 稀有或世界尺度 review 才喚起 AO；秘密走 Mystery。
7. final validation。
8. Orchestrator 把完整 accepted final build 寫入 selected campaign authoritative character store。
9. 驗證角色 master record 可重新讀取；再丟棄未採用候選與 counterfactual working data。
```

最終目標：

```text
少數真正會思考的模塊
+ 多個乾淨、無人格、可查詢的資料／狀態服務
+ 每一團有獨立、可重掛載的 authoritative campaign namespace
+ 玩家不在場時仍會演進、但不因玩家骰點反向生成因果的世界
+ 來源查核不壓死創作、創作採用不冒充來源
```
