# Rook Hal / Rook・哈爾 — Authoritative Character Record

> Recovery audit: `migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md`

```yaml
character_id: PC-ROOK
name: Rook Hal
zh_name: Rook・哈爾
race: human
age: approximately 27
controller:
  mode: pl_pc
  player_voice: 鮫島
alignment:
  law_chaos: lawful
  good_evil: neutral
concept: militia-background caravan guard / practical martial traveller
record_status: authoritative_recovered_with_unfinalized_fields
recovery_status: exhaustive_2026-09-16
```

## Attributes

```yaml
attributes_raw:
  STR: 18
  DEX: 16
  SKI: 17
  CON: 14
  RES: 13
  INT: 12
  WIS: 10
  CHA: 9
  SPI: 7
adjustments:
  STR: 3
  DEX: 2
  SKI: 2
  CON: 1
  RES: 0
  INT: -1
  WIS: -2
  CHA: -2
  SPI: -3
adjustment_sum: 0
attributes_total:
  STR: 21
  DEX: 18
  SKI: 19
  CON: 15
  RES: 13
  INT: 11
  WIS: 8
  CHA: 7
  SPI: 4
```

## Derived values

```yaml
bases:
  combat: 58
  athletic: 52
  operation: 38
  perception: 28
  knowledge: 28
  interaction: 19
resistances:
  anti_toxin: 28
  control: 21
  transform: 26
  breath: 31
  magic: 24
special_checks_before_other_modifiers:
  fortitude: 70
  mental: 65
  soul: 35
resources:
  hp: 39/39
  sp: 18/18
  cp_reserve: 41
```

Derived values are deterministic from the recovered raw / adjustment / total attributes under the current D100 formulas; later equipment/effects can modify runtime checks.

## Creation CP ledger

```yaml
base_starting_cp: 200
adjusted_starting_cp: 300
creation_spent_cp: 260
creation_reserve_cp: 40
checkpoint_01_award_cp: 1
current_cp_reserve: 41
```

### Martial — 126 CP

```yaml
長劍: 3
閃避: 3
格擋: 3
盾牌: 3
中甲: 3
專攻長劍: 3
武器專精: 2
及時備戰: 3
精通先攻: 2
戰鬥反射: 2
盲戰: 1
```

### Survival — 46 CP

```yaml
耐久: 3
頑強: 2
健壯: 3
強韌加強: 2
快速反射: 2
```

### Caravan life — 88 CP

```yaml
競技: 3
騎術: 3
生存: 3
自救: 2
聆聽: 3
偵察: 3
繩技: 2
估價: 1
搜集資訊: 1
地方知識: 1
```

## Languages

```yaml
通用語:
  level: 3
  source: free_creation_grant
additional_languages:
  status: no_recovered_evidence
```

`no_recovered_evidence` is not a positive claim that Rook can never have another language if new primary evidence is supplied later.

## HP / SP creation evidence

```yaml
creation_reward_roll_recovered:
  hp: "3d8 = 3 + 7 + 2 = 12"
  sp: "3d4 = 2 + 2 + 1 = 5"
final_creation_or_session_total:
  hp: 39
  sp: 18
```

The exact intermediate HP base decomposition is not safely reconstructable from the surviving record because skill/item contributions were not preserved separately. Do not reverse-engineer one merely to make the arithmetic look complete.

## Equipment recovery boundary

Recovered accepted rerun shell:

```yaml
item_types:
  - longsword / 長劍
  - medium_armor / 中甲
  - shield / 盾
starting_magic_template: "+3 / +4 / +5 three-item template"
exact_bonus_mapping: unresolved_not_finalized
exact_affixes: unresolved_not_finalized
```

Superseded draft evidence such as `+4 長劍 / +3 重甲 / +2 重鋼盾` is not current authority.

## Character direction / current Andor thread

- Practical guard / caravan-guard orientation; contracts, order and competent procedure matter.
- Rejects illegitimate authority; does not require forced party leadership.
- Current Andor thread: remains at Mercenary Guild asking convoy details; convoy interest is pending and has not been accepted/resolved off-camera.

## Provenance / closure

```yaml
recovery_sources:
  - prior_chat_character_creation_log
  - sessions/2026-09-15_session-1_runtime-migration.md
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - deterministic_D100_attribute_formulas
  - git_history_recovery_audit
recovery_exhausted:
  full_creation_ledger: recovered
  raw_stats_and_adjustments: recovered
  complete_skill_feat_list: recovered
  languages: recovered_to_available_evidence
  equipment_exact_affixes: unresolved_not_finalized
  starting_money: no_recovered_evidence
```
