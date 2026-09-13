# TRIGGERED_HAZARD_TEMPLATE.md — 條件式危險／自動裝置資料

> 這是資料 schema，不是「陷阱人格」。吸收 D&D 3.5 Trap 的 Trigger / Reset / Bypass 結構，但所有實際判定與數值仍依 D100。

```yaml
hazard_id:
name:
type:
source_refs: []
location_ref:
agenc y: reactive
```

> `agency` 固定預設為 `reactive`；若物件具有真正自主意志、belief 與目的，應升格為 autonomous Entity，而不是繼續塞在 hazard record。

## 1. Sensors

```yaml
sensors:
  - type: location | proximity | sound | visual | touch | timer | magical | custom
    range:
    limitations: []
    fooled_by: []
```

感測器只取得它真的能取得的訊號。視覺 sensor 不因「是魔法陷阱」就自動看穿隱形；聲音 sensor 也可被沉默、距離、環境噪音等影響，除非條文明文例外。

## 2. Trigger Predicate

```yaml
trigger_predicate:
  description:
  conditions: []
  requires_all: true
```

AO 根據世界狀態判斷 predicate 是否成立；hazard record 自己不決定「為了劇情現在觸發」。

## 3. Effect

```yaml
effect:
  description:
  d100_interface:
  stages: []
  target_rules:
```

每個 stage 都必須回答不同的機械／因果問題；不得因同一效果可被描述成多個詞就機械增加多重防禦骰。

## 4. Timing

```yaml
timing:
  trigger_window:
  delay:
  duration:
  cooldown:
  clock_basis: tactical | world | mixed
```

- `tactical` → 主要由碼表處理。
- `world` → 主要由沙漏處理。
- `mixed` → 分別記 external world time、action windows 等。

## 5. Reset

```yaml
reset:
  type: none | manual | repair | automatic | custom
  condition:
  time_required:
```

## 6. Bypass

```yaml
bypass:
  exists: false
  methods: []
```

## 7. Discoverability / Disable

```yaml
discoverability:
  visible_clues: []
  search_or_detection_interfaces: []
  information_layers:
    existence:
    location:
    classification:
    mechanism:
    disposal:

disable_interface:
  methods: []
  failure_consequences: []
```

## 8. Current State

```yaml
current_state:
  armed: true
  triggered: false
  cooldown_until:
  damaged:
  bypass_active:
```

## 9. Secrets

```yaml
secret_refs: []
```

完整 protected payload 只存在 Mystery Vault；此檔只存合法 view / Secret ID。

## 10. Runtime Projection

```text
圖書館員 → 取得 hazard 規則／來源
詭祕     → 決定哪些 trigger / mechanism 對哪些模塊可見
AO       → 判斷 sensor 與 trigger predicate 在世界中是否成立
碼表     → 處理反應窗、延遲、戰術 cooldown
沙漏     → 處理長時間 timer、repair、automatic reset
會計師   → 若裝置可拆取／消耗／回收，追蹤物件與價值
```
