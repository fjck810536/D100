# CREATURE_WORLD_MODEL_TEMPLATE.md — 生物／NPC Actor State Record

> 用途：重要 NPC、怪物、龍、異界生物、Boss 等**不能只靠一行 stat block 主持**的對象。
>
> 本檔現在只負責保存 actor state / capability / evidence；不再同時充當生態學家、分析師、戰術 AI 與 AO。資料分層見 `../DATA_ARCHITECTURE.md`。

核心原則：

```text
這是誰／是什麼
→ 現在客觀狀態是什麼
→ 它知道／相信什麼
→ 它能做什麼
→ 模塊可以據此產生可撤回的 derived view
```

而不是：

```text
模板預先決定它現在一定會怎麼行動
```

---

## 0. Identity / Source

```yaml
entity_id:
name:
species:
source_version:
source_reference:
conversion_status:
agency:
  type: autonomous
```

來源標記：

- `[SOURCE_PROFILE]`：外部原始來源直接支持的物種／能力／生態資訊。
- `[D100_ADAPTATION]`：由外部規則轉成 D100 的機械；不是 D100 Sheet 正典。
- `[ENCOUNTER_STATE]`：此個體目前真的成立的世界狀態。
- `[DERIVED_VIEW]`：模塊推理出的暫時 interpretation / forecast。
- `[OPEN_QUESTION]`：來源不足。

同名生物跨版本／homebrew 不得混用。

---

## 1. Species / Body Data

### 身體／感官

```text
體型：
主要移動方式：
飛行／游泳／鑽地：
感官：
呼吸／環境需求：
自然武器：
特殊生理：
```

### 發育／年齡階段

| 階段 | 體型／外觀 | 新增能力 | 行為／認知變化證據 | 備註 |
|---|---|---|---|---|

若生理成熟度與實際經歷年數不同，分開記錄。

### 生態 facts

```text
食性：
活動週期：
棲地：
遷徙／領域性：
社會結構：
繁殖：
收藏／築巢：
天敵／避免對象：
```

這些是生態學家的輸入資料，不是「生態學家已經做出的行為決策」。

---

## 2. Individual State

```yaml
individual_name:
sex_or_gender_if_relevant:
development_stage:
chronological_age_if_known:
current_condition:
position:
altitude:
orientation:
current_hp:
current_sp:
active_effects: []
used_resources: []
cooldowns: []
retreat_status:
```

世界狀態一旦成立，不得因劇情方便偷偷重置。

---

## 3. Stable Evidence about Preferences / Constraints

> 只寫有來源／歷史行為／設定支持的穩定 evidence；不要把模塊推測寫成角色本質。

```yaml
preferences: []
aversions: []
obligations: []
orders: []
taboos: []
resource_constraints: []
```

可記：

```text
通常重視什麼
通常避免什麼
是否願意戰死（若有證據）
既有誓言／職務／命令
長期目標
```

不要只寫「殘忍／聰明／膽小」等無法預測行為的形容詞。

---

## 4. Epistemic State — 它實際知道／相信什麼

NPC／怪物不能讀角色卡。

```yaml
known_facts: []
beliefs: []
misbeliefs: []
uncertainties: []
```

戰鬥／場景中可追加 evidence update：

| 事件 | 能觀察到什麼 | 可合理推論 | 不可直接知道 |
|---|---|---|---|

例：

```text
PC 開啟群體 buff
→ 看見施術後整隊更難命中
→ 可形成「此人可能是支援核心」的 belief
→ 不能直接知道精確範圍、數值與剩餘輪數
```

核心分離：

```text
belief ≠ preference ≠ action
```

某 NPC 可以相信玩家說的是真的，仍因自身利益、命令、恐懼或其他 constraint 拒絕配合。

涉及祕密時只保存此 actor 合法取得的 representation；完整 protected payload 不放這裡。

```yaml
secret_refs: []
```

---

## 5. Action Palette / Capabilities

怪物也要像 PC 一樣建立完整可做事項。

```text
一般動作：
自由動作：
即時／反應：
額外行動來源：
移動能力：
法術／類法術：
自然攻擊：
吐息／範圍能力：
被動 aura：
受擊 trigger：
每輪 trigger：
每日／每場資源：
冷卻：
逃生能力：
```

Action Palette 是 capability cache；規則來源仍以 D100／bridge 條文為準。

### 本輪 Ledger

```text
一般動作：未用／已用
自由動作：
即時／反應：
額外行動：
移動剩餘：
冷卻中：
可觸發：
```

碼表負責戰術時間窗；此檔只保存 live state。

---

## 6. D100 Mechanical State

外部怪物先保留概念，再另建 D100 接口。

```text
九屬性（需要才填）：
戰鬥：
運動：
操作：
感知：
知識：
交涉：

抗毒素：
抗控制：
抗轉化：
抗噴吐：
抗魔法：

強韌：
精神：
靈魂：

HP：
SP：
移動：
攻擊：
閃避：
防禦／減傷：
```

### 特殊能力接口

對每個特殊能力逐條回答：

```text
能力造成什麼世界效果？
需要施法／攻擊判定嗎？
目標靠什麼接口抵抗？
是否另有法抗層？
失敗後的具體世界狀態？
持續多久？
是否能被中斷／解除？
```

**禁止直接把 AC、BAB、Fort / Reflex / Will、CR、HD 或 3.5 spell DC ×5。**

轉譯方法見 `../90_srd_bridge/`。

---

## 7. Time Data

如果來源不是 D100，分開：

```text
external world time
subjective time
action windows
cooldown basis
```

- 碼表：tactical windows、reaction、per-turn cooldown。
- 沙漏：物理秒數、旅行、增援、中毒、長期變化。

不要把所有 source round 都機械換成同一個 D100 round 數。

---

## 8. Observable Evidence

把「世界真的有什麼」與「玩家／NPC能發現什麼」拆開。

| 隱藏機制 | 無檢定可見 | 成功觀察可得 | 深度研究才可得 | Secret ref |
|---|---|---|---|---|

玩家若透過實驗、誘導、環境反應找到規律，所得知識必須真的進入其 epistemic state，並提高後續預測能力。

---

## 9. Relations / Organization / Resources

```yaml
faction_refs: []
relationship_refs: []
item_refs: []
site_refs: []
resource_refs: []
```

- 政治家讀勢力、義務、承諾、資源與權力關係。
- 會計師讀物件持有、流轉、剩餘價值。
- 生態學家讀生態、生存與 mechanical niche。

本檔不複製它們各自的平行真相。

---

## 10. Derived Views — 可 cache，但不是 world fact

以下內容可以由 Cabinet 產生並暫存：

```yaml
derived_views:
  combat_doctrine:
    value:
    generated_from: []
    generated_at:
    invalidated_by: []
  threat_model:
    value:
    generated_from: []
    generated_at:
    invalidated_by: []
  analyst_structure:
    value:
    generated_from: []
    generated_at:
    invalidated_by: []
```

例如舊版模板中的：

```text
第一輪傾向
優先擊殺目標
何時用最強能力
何時撤退
```

現在預設都是 derived view，而不是固定人格欄位。

底層資訊一旦改變，例如：

- 受傷
- 收到新命令
- 敵方露出能力
- 發現自己誤判
- 資源耗盡
- 祕密揭露
- 地形改變

舊 view 應失效或重算。

---

## 11. Cabinet Projection

```text
圖書館員 → source / rules / provenance
詭祕     → module-safe information view
生態學家 → species、mechanical niche、environment、survival、behavior tendency
分析師   → roles / self-image / behavioral residual
政治家   → faction / obligation / resource / second-order response
會計師   → held items / resource flow / unrealized value
碼表     → Action Palette / tactical windows
沙漏     → world time / schedules / long processes
AO       → 整合合法 view，裁定實際世界結果
```

所有模塊輸出的 hypothesis / constraint / proposal 都不能直接冒充 world state；只有經實際世界事件／AO 結算後才寫回 state。
