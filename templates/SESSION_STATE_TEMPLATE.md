# SESSION_STATE_TEMPLATE.md

> 複製為 `sessions/YYYY-MM-DD_session-N.md`。本檔是 GPT 在長團中避免失憶與狀態漂移的主要容器。
>
> 本檔只保存「目前真的成立的 session state」、actor-specific epistemic state refs、relationship/evidence/commitment refs 與合法 Mystery references；不得另建 plaintext DM secret store。架構見 `../DATA_ARCHITECTURE.md`、`../RUNTIME_SOCIAL_WORLD_CONTRACT.md`、`../MYSTERY_PROTOCOL.md`。
>
> 若本 session 接受了 grounded generation / user correction / legacy repair，必須保留來源與採用事件；存檔後重新載入不得把 generated claim 洗成 D100 原文，也不得重抽已採用的地址、身份或關係。

```yaml
session_id:
date:
scene:
in_combat: false
round:
world_time:

four_voice_control:
  mode: npc | pl_pc
  mappings: []

site_refs: []
source_resolution_refs: []
decision_event_refs: []
deferral_refs: []
repair_event_refs: []
```

> `four_voice_control.mode` 只有在使用者／DM 明確要求四聲部作為 PL+PC 時才設為 `pl_pc`；普通情況可保持 `npc`。過去由 DM 直接生成的 NPC mode 行為不得事後回填成 Player choice。

## 當前場景

### 地點

### 可見／可聽／可感知資訊

### Site / map refs

```yaml
site_refs:
  - site_ref:
    current_relation: at | approaching | known | mapped | mentioned
    visible_label:
    visibility_ref:
```

> 世界中 site 存在、玩家地圖上怎麼標、角色是否知道秘密隸屬是三件不同的事。

### Source resolution / claim provenance

```yaml
source_resolution_refs:
  - resolution_id:
    claim_refs: []
    source_refs: []
    user_correction_refs: []
    generated_claim_refs: []
    searched_scope: []
    unresolved_lookup: []
    creative_space: []
```

> 全文搜尋零命中不是 `source missing` 的充分證明；圖書館員若有語義索引／交叉引用路徑，應把實際查讀結果留成 ref。來源缺口與可創作空間分開記。

### Secret refs

```yaml
secret_refs: []
```

> 只記 `Secret ID` 與此 session 合法取得的 role-safe view。完整 protected payload 若屬 Mystery Vault，不得複製進 session state。

### World Commitment refs

```yaml
commitment_refs: []
```

> 只連到已 committed 的 hidden causal state，不在 session plaintext 重複未授權 truth core。詳見 `WORLD_COMMITMENT_TEMPLATE.md`。

### Relationship Graph refs

```yaml
relationship_refs: []
```

> 客觀關係事實留在共享 Relationship Graph；session 只追此幕新增／改變的 edge refs。

## PC 即時狀態

| PC | HP | SP | 位置 | 姿勢 | 持續效果 | 備註 |
|---|---:|---:|---|---|---|---|

## NPC / 怪物

| 名稱 | HP | SP | 位置 | 狀態 | 敵對？ | 備註 |
|---|---:|---:|---|---|---|---|

> NPC 的 belief / knowledge 若需要持久化，記錄實際 belief state 或對應 Entity ref；不要把分析師／生態學家的暫時推測寫成既定人格真相。

## Actor Epistemic Matrix

> 只記角色實際知道／相信／誤信的資訊或其 refs。世界真相本身不等於所有 actor 都知道。

```yaml
actor_epistemic_refs:
  - actor_id:
    known_fact_refs: []
    belief_refs: []
    misbelief_refs: []
```

## Evidence Ledger

> 玩家／角色建立的是 Evidence Graph，不是 hidden Causal Graph。

| Evidence ID | Proposition | Status | Observed by | Source refs | Related Secret refs |
|---|---|---|---|---|---|

Status 只用：

```text
OBSERVED
INFERRED
CONFIRMED
DISPROVEN
```

普通失敗若取得弱線索，通常應停在 `OBSERVED` 或 `INFERRED`；不要因敘述方便直接寫成 `CONFIRMED`。

## Player Layer（僅 PL+PC mode）

> 這是 meta working data，不是 PC 內在心理。NPC mode 留空。

```yaml
player_layers:
  - player_voice:
    pc_id:
    agenda: []
    current_interest: []
    risk_tolerance:
    interpretation_of_pc: []
    intended_play: []
    current_decision:
```

Player Layer 可以拒絕分析師／生態學家 proposal；DM 不得把 derived recommendation 當成 Player decision。

新感情、意向或角色發展若由對應 PL 明確決定，可以從該時點成為新的 actor state；不需要先證明「角色以前早就有同一感情」。但 Player Layer 決定不自動決定另一名 PC 的內心或雙方關係狀態。

## Typed deferral / non-assertion

> 禁止用沒有狀態轉移語義的「還不能太早／之後再說」長期掛住候選。

```yaml
deferral_refs:
  - deferral_id:
    type: NON_ASSERTION | DEFERRED | OWNER_DECISION | PROHIBITED | NOT_SELECTED
    proposition_or_candidate_ref:
    blocked_operation:
    owner:
    trigger:
    reevaluate_with:
    rule_or_fact_ref:
    last_updated:
```

- `NON_ASSERTION`：目前不能把命題宣稱成既有事實；不封鎖新候選生成。
- `DEFERRED`：真的在等條件；必須有 trigger + reevaluate_with。
- `OWNER_DECISION`：決定權在特定 PL／AO；不是世界禁令。
- `PROHIBITED`：有規則／事實明確禁止，必須有 ref。
- `NOT_SELECTED`：本次沒選，不是永久禁止。

## 戰鬥順位

### 行動順序

```text
1.
2.
3.
```

### 宣告順序

```text
1.  # 早宣告
2.
3.  # 晚宣告
```

## 本輪宣告

| 角色 | 宣告 | 動作類型 | 是否已執行 |
|---|---|---|---|

## 即時／瞬唱使用權

| 角色 | 法術瞬唱 | 即時動作種類 | 已用？ |
|---|---|---|---|

## DOT / Buff / Debuff

| 對象 | 效果 | 來源體系 | 剩餘輪數/時間 | 每輪處理 |
|---|---|---|---|---|

> 注意：D100 戰鬥一輪 = 1 秒。

## 連續施法追蹤

| 施法者 | 上次成功法術 | 環數 | 目前連續施法懲罰 |
|---|---|---:|---:|

## 藥水負荷

| 角色 | 最近5輪計入數量 | CON承受上限 | 是否需抗毒 |
|---|---:|---:|---|

## 隱藏判定

| 對象 | 判定 | 數值 | D100 | 結果 | 玩家知道嗎？ | Commitment ref |
|---|---|---:|---:|---|---|---|

> 「秘密擲骰」不等於「秘密 payload」。骰值與結果可放 session state；其背後尚未授權的秘密內容仍只以 `secret_refs` / `commitment_refs` 連接 Mystery / hidden causal state。
>
> 若判定結果依賴 hidden truth，該 truth 必須在擲骰前已有 commitment ref；不得骰後才決定是否存在。

## 調查資訊階梯

### 物件／事件：

- 存在：
- 定位：
- 分類：
- 理解：
- 處置：

### 玩家目前已取得

> 若這些取得內容會持久影響推理，轉寫到 Evidence Ledger / Actor Epistemic Matrix，不只留在散文。

## 神器／詛咒／轉化進度

| 對象 | 機制／Secret ref | 階段 | 已觸發 | 已知資訊 |
|---|---|---:|---|---|

## Triggered Hazard / Object State

| Hazard ref | Armed | Triggered | Cooldown / Reset | 備註 |
|---|---|---|---|---|

> 詳細結構見 `TRIGGERED_HAZARD_TEMPLATE.md`；session 只追 live state，不重複整份 statblock。

## World / Actor Commitment Updates

| Commitment ref | 變更 | 原因／事件 ref | 是否使舊 derived cache 失效 |
|---|---|---|---|

> commitment 可以因正常世界事件改變／取消；`commitment ≠ destiny`。但不能因玩家骰點好壞反向改寫「先前原本是什麼」。

## Relationship Fact Updates

| Edge ref | 新增／變更的客觀事實 | Provenance event | Secret ref（若有） |
|---|---|---|---|

> 只記客觀成立的事件／承諾／債務／依賴。分析師解讀、政治家預後不要填在這裡。

## Decision / adoption events

| Event ref | Owner | Proposed claim / action | Decision | Effective from | Provenance |
|---|---|---|---|---|---|

> `proposed → committed` 必須有合法 owner。PL+PC 關鍵角色決定屬 Player Layer；NPC／世界發展由 AO flow 採用。普通 grounded generation 不需要逐項向頂層 DM 請示，但不得繞過真正的 owner。

## Provenance repair events

| Repair ref | Old representation | New representation | Reason | Source / correction refs | Affected state |
|---|---|---|---|---|---|

> 後來補錄來源不代表它早先已被查過；後來補存 site 不代表建築在世界時間上剛出現。`recorded_at` 與 `effective_from` 分開。

## 本次臨時裁定

| 問題 | 裁定 | 標籤 | 下次是否需確認 |
|---|---|---|---|

可用標籤：

- `[D100_CANON]`
- `[D100_DERIVED]`
- `[DM_DEFAULT]`
- `[SRD_BRIDGE]`
- `[OPEN_QUESTION]`

## Derived cache refs

```yaml
derived_refs:
  analyst: []
  politician: []
  ecology: []
  threat_models: []
  other: []
```

> 可連到 relationship interpretation、alignment tension、combat doctrine、threat model、political forecast 等昂貴推理結果，但 derived cache 不是 world fact；底層 state / evidence / relationship / secret / alignment / player interpretation 改變時必須失效／重算。

## 世界狀態改變

## 戰利品／CP／金錢變動

## Session 結束快照

### PC

### NPC

### Site / Map refs

### Relationship Facts

### Actor Epistemic State

### Evidence Ledger

### Source / Decision / Repair refs

### Secret / Commitment refs

### Typed deferrals / owner decisions

### Derived views to invalidate / keep

### 未完成事件

### 下次開場必讀

## Completion check

在相關工作結束前，orchestrator 最少核對：

```text
需要的 source / cross-reference 是否真的讀過或有仍有效的 cache？
查得資料是否真的被下游模塊使用？
採用的新 claim 是否有 owner / decision event / provenance？
角色合理可知且與眼前選擇相關的成果是否真的交付？
尚未完成的工作是否被記成未完成，而不是被說成世界沒有？
```
