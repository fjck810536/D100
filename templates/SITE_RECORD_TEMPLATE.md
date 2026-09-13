# SITE_RECORD_TEMPLATE.md — 地點／建築／地下城狀態資料

> 這是資料容器，不是「環境模塊」。Site record 只保存目前成立的場地事實；AO、生態學家、政治家、沙漏、會計師等依職責取得 view。

```yaml
site_id:
name:
site_type:
source_refs: []
parent_site:
```

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

## 10. Module Projections

```text
AO        → 物理、空間、建築、實際控制狀態
生態學家   → 棲地、食物、生物活動
政治家     → 控制權、守衛、組織、合法性
沙漏       → 巡邏、補給、腐敗、維修、時間事件
會計師     → 資源、財物、供應、未實現價值
詭祕       → secret_refs 的合法 representation
```

Site record 本身不產生策略；例如「守衛今晚應該加強巡邏」必須先由相關模塊推理，再由 AO／orchestrator 寫回新的實際 state。
