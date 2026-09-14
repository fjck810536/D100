# PC_TEMPLATE.md

> 複製本檔建立 `characters/<name>.md`。DM 每次需要角色數值時以角色檔為準，不要靠聊天記憶猜。
>
> 本檔是角色 state / capability record，不是人格模塊。完整祕密不直接塞進角色檔；需要時用 Mystery Secret ref。架構見 `../DATA_ARCHITECTURE.md`。
>
> 創角／驗卡流程見 `../CHARACTER_CREATION_PROTOCOL.md`。創角 meta accounting 可以保存在角色檔，但不得誤當世界內財產。

```yaml
name:
player:
race:
concept:
current_cp:      # 目前可用／未花 CP
 total_cp:       # 角色目前總 CP 尺度；若團內有其他定義請註明
agency:
  type: autonomous
```

## 創角帳本 / Creation Ledger

> Build Ledger 的 final snapshot。CP 是 meta build resource，不是角色在世界中攜帶的貨幣。

```yaml
creation_ledger:
  base_starting_cp:
  attribute_adjustment_sum:
  attribute_cp_modifier:
  adjusted_starting_cp:
  background_bonus_cp:
  other_bonus_cp:
  spent_cp:
  reserved_cp:
  qualifying_melee_cp:
  qualifying_spell_cp:
  reward_rolls:
    melee_hp:
    melee_sp:
    spell_hp:
    spell_sp:
  hp_purchase_cp:
  sp_purchase_cp:
  reserve_plan:
```

若 qualifying melee/spell 分類仍有未決項，保留 provenance / uncertainty，不要把總技能 CP 硬塞進其中一池。

## 創角審核摘要

```yaml
creation_review:
  hard_legality: pending   # pending | pass | fail
  required_player_fields: []
  review_flags: []
  resolved_review_notes: []
```

`review_flags` 只表示需要背景／世界尺度審查，不表示非法。完成審核後仍可保留 resolved note 作 provenance。

## 九大屬性

| 屬性 | raw 值 | 調整值 | 總值（raw+adjustment） |
|---|---:|---:|---:|
| STR |  |  |  |
| DEX |  |  |  |
| SKI |  |  |  |
| CON |  |  |  |
| RES |  |  |  |
| INT |  |  |  |
| WIS |  |  |  |
| CHA |  |  |  |
| SPI |  |  |  |

## 六大技能基礎

> 使用 `00_core/character_creation.md` 的屬性總值公式，不要只用 raw stat。

```text
戰鬥 =
運動 =
操作 =
感知 =
知識 =
交涉 =
```

## 五大抗性

```text
抗毒素 =
抗控制 =
抗轉化 =
抗噴吐 =
抗魔法 =
```

## 三特殊判定

```text
強韌 =
精神 =
靈魂 =
```

## 生存資源

```text
基礎HP：
最終HP： / 
基礎SP：
最終SP： / 
臨時HP：
移動：         # 若角色表已有實際值直接填；不要由未決公式自行猜
```

## 戰鬥

```text
行動順序值（DEX + mod）：
宣告順序值（INT + mod）：
閃避：
格擋：
盾牌：
鎧甲：
物抗：
法抗：
火抗：
冰抗：
電抗：
酸抗：
光抗：
暗抗：
其他：
```

## 武器

### 武器 1

```text
名稱：
武器使用技能：
攻擊判定：
基礎傷害：
爆擊：
射程：
詞綴：
其他：
```

## 技能／基本專長

| 名稱 | 分類 | 難度 | 等級 | CP成本 | 最終判定 | 前置狀態 | 備註 |
|---|---|---:|---:|---:|---:|---|---|

## 一般／高級／傳奇專長

| 名稱 | 難度 | 等級 | CP成本 | 前置狀態 | 效果摘要 |
|---|---:|---:|---:|---|---|

## 語言

| 語言 | 難度 | 等級 | 來源 | CP | 備註 |
|---|---:|---:|---|---:|---|
| 通用語 | 1 | 3 | 創角免費 | 0 | `[GM_PROVISIONAL]` 創角模板 |

> 施法者創角須至少有一門難度2語言 Lv1+；可由種族／背景／模板／CP 購買取得。詳見 `../01_skills/languages.md`。

## 身分／訓練來源

> 只填角色概念真正需要的欄位；不要為了格式強迫每人都有教團／師承。

```yaml
identity_and_training:
  deity_or_faith:
  domain:
  oath_or_code:
  order_or_circle:
  teacher_or_school:
  training_start_age:
  training_history:
  other_required_rp:
```

牧師至少需要明示真實信仰／神祇與領域。高環施法者若有 review，這裡應能追溯其訓練來源。

## 施法

```yaml
spellcasting:
  tradition:
  core_skills: []
  usable_circle:
  next_circle_partial_investment: []
  total_caster_level:
  casting_main_base:
  spell_slots:
  memory_slots:
  sequential_cast_penalty:
  difficulty2_language_gate: pass
  school_or_specialization:
```

> `usable_circle` 取該施法體系必要核心技能等級最低值。核心技能可以先非同步預購下一環，不因不同級而整張卡非法。

### 已知／已抄寫法術

| 法術 | 環數 | 體系 | 備註 |
|---|---:|---|---|

### 當前記憶

| 法術 | 環數 |
|---|---:|

## 魔法物品

| 物品 | 加值 | 詞綴 | 調頻 | 使用次數／資源 | 來源 |
|---|---:|---|---|---|---|

## Action Palette cache

> 可由技能／專長／物品／當前狀態重建。若在此保存，是方便 runtime 的 capability cache，不是另一份規則來源。

```text
一般動作：
自由動作：
即時／反應：
瞬唱：
並行能力：
移動能力：
觸發式能力：
物品啟動：
每日／每場／充能資源：
```

## 狀態

```text
姿勢：
持續增益：
持續減益：
DOT：
控制／轉化進度：
靈魂／精神狀態：
藥水負荷：
```

## Epistemic State

> 只記角色目前實際知道／相信／誤信的內容，不記分析師眼中的「真正人格」。

```yaml
known_facts: []
beliefs: []
misbeliefs: []
```

## Preferences / Constraints

> 用於 NPC／模擬角色時，可記穩定且有 evidence 的偏好與義務；真玩家 PC 不應被這區替玩家預決定行動。

```yaml
preferences: []
constraints: []
```

核心分離：

```text
belief ≠ preference ≠ action
```

## Secret refs

```yaml
secret_refs: []
```

只放角色檔合法取得的 Secret ID / role-safe representation。完整 protected payload 依 `MYSTERY_PROTOCOL.md` 管理。

## 背景與已知情報

## DM 注意

- 角色檔內實際數值／持有能力優先於聊天記憶。
- 擁有能力 ≠ 已啟動；持有物件 ≠ 願意消耗。
- 真玩家控制 PC 時，角色檔不能替玩家決定「通常會做什麼」。
- 若保存 combat doctrine / threat model 等推理，只能標為 derived cache，不能寫成 established character truth。
- 秘密資料透過 Mystery refs 連接，不建立平行 plaintext DM secret 區。
- 創角 review flag ≠ 世界真相；它是驗卡 provenance / administrative metadata。
