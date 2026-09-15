# SITE_RECORD_TEMPLATE.md — 地點／建築／地下城狀態資料

> 這是資料容器，不是「環境模塊」。Site record 只保存目前成立的場地事實；AO、生態學家、政治家、沙漏、會計師等依職責取得 view。
>
> Site 可以同時包含 source-backed、user-corrected、legacy-generated 與 newly-generated claims。**採用後仍保留各 claim 的來源；generated 不會因寫進 authoritative state 就變成原文。**

```yaml
site_id:
name:
site_type:
source_refs: []
parent_site:
claim_refs: []
adoption_event_ref:
effective_from:
```

## 0. Claim / Provenance / Map Projection

重要設定不要只用一個 `source_refs` 包整棟建築。逐 claim 區分來源、擬合、成立狀態與決定權：

```yaml
claims:
  - claim_id:
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
      supporting_facts: []
      conflicts: []
      unresolved_fields: []
      added_assumptions: []
      judgment: supported | compatible | in-tension | conflicting | unknown
    status: hypothesis | proposed | committed | rejected | superseded
    decision_owner:
    decision_event_ref:
    committed_at:
    effective_from:
    visibility_ref:
```

核心區分：

```text
source_refs = 原文／既有 state 真正支持什麼
contextual_support_refs = 為什麼某項創作與世界相容
generated = true 可以被採用並成為世界事實
adopted generated claim ≠ D100 原文
recorded_at ≠ effective_from
```

地圖投影另記，不把「世界中存在」和「玩家地圖上怎麼標」混成同一件事：

```yaml
map_projection:
  backend_label:
  public_label:
  player_private_labels: []
  navigation_status: known | approximate | exact | hidden
  visibility_ref:
```

### 0.1 Location / World Anchor

一個可作為目的地或解釋其他地點的 site，依 `../DM_PROTOCOL.md` 1.5 接到既有世界參照。`parent_site` 保存直接空間包含關係；組織 affiliation、實際控制者與地理所在分開記錄。

```yaml
location:
  world_anchor_ref: # 既有國家／城市／地域／位面 ref
  placement_summary: # 在哪裡；區域／地形或與已知節點的相對關係
  connection_refs: [] # 已採用的道路／航線／聯絡關係，按需要引用
  claim_refs: [] # 逐項位置 provenance；新增落點／交通保留 generated
```

沿 `parent_site` 或 `world_anchor_ref` 可追到有來源／既有 state 的參照；必要的新中間節點一起定位。移動據點可接位面、活動地域與移動方式；獨立城可接已知地理區域。導航精度依目前用途提供，文化相似或名稱含「灣」的線索留在 fit/proposal，不冒充原文座標。

隔離推演可用相同形狀描述 proposed location；其內容留在 test working context，正式 site 實例依正常 adoption 才更新。

## 1. Construction / Physical State

```yaml
construction:
materials:
layout_summary:
access_points: []
structural_damage:
maintenance_state:
```

## 2. Occupancy / Control

```yaml
current_occupants: []
controller:
claimed_by: []
public_access:
restricted_areas: []
```

## 3. Logistics

```yaml
supplies:
water:
food:
power_or_magic_support:
storage:
external_access:
```

## 4. Security / Movement

```yaml
patrols: []
watch_posts: []
communication_system:
locks_and_barriers: []
hazard_refs: []
```

## 5. Terrain / Environment

```yaml
terrain:
lighting:
weather_or_climate:
air_or_water_conditions:
movement_constraints: []
visibility_constraints: []
```

## 6. Ecology

```yaml
habitat_features: []
food_chain_notes: []
resident_species: []
transient_species: []
decay_or_growth:
```

## 7. Resources / Objects

```yaml
resource_refs: []
item_refs: []
treasure_refs: []
```

## 8. Time-dependent State

```yaml
world_time_last_updated:
next_scheduled_events: []
ongoing_decay: []
ongoing_repairs: []
```

## 9. Secrets

```yaml
secret_refs: []
```

不得在此欄直接複製 Mystery Vault protected payload。

Site 的存在、公開名稱、秘密隸屬、角色是否知道該隸屬是不同命題；秘密 affiliation 可以已 committed，但 public map 仍只顯示普通場所。

## 10. Module Projections

```text
AO        → 物理、空間、建築、實際控制狀態
生態學家   → 棲地、食物、生物活動、日常使用方式
政治家     → 控制權、守衛、組織、合法性、上層／地方聯絡
沙漏       → 巡邏、補給、腐敗、維修、時間事件
會計師     → 資源、財物、供應、未實現價值
圖書館員   → claim provenance、跨條目關係、來源缺口
詭祕       → secret_refs 的合法 representation / visibility
```

Site record 本身不產生策略；例如「守衛今晚應該加強巡邏」必須先由相關模塊推理，再由 AO／orchestrator 寫回新的實際 state。

## 11. Grounded-generation fuse

```text
SOURCE_GAP ≠ 此地點不得存在
來源未寫地址 ≠ 永久沒有地址
生成候選 ≠ 已成立世界事實
有權者採用 + 無硬衝突 → 可以成為 committed site claim
採用後保留 generated / user-correction / source-extraction 的 origin
```
