# Nella / 涅菈 — Authoritative Character Record

> Recovery audit: `migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md`

```yaml
character_id: PC-NELLA
name: Nella
zh_name: 涅菈
race: human
age: approximately 22
controller:
  mode: pl_pc
  player_voice: 蟬
alignment:
  law_chaos: chaotic
  good_evil: neutral
concept: locksmith-family infiltration / courier / scout / gray-work character
record_status: authoritative_recovered_with_unfinalized_fields
recovery_status: exhaustive_2026-09-16
```

## Attributes

```yaml
attributes_raw:
  STR: 9
  DEX: 17
  SKI: 16
  CON: 15
  RES: 14
  INT: 16
  WIS: 14
  CHA: 13
  SPI: 13
adjustments:
  STR: -2
  DEX: 2
  SKI: 2
  CON: 1
  RES: 1
  INT: 2
  WIS: 1
  CHA: 0
  SPI: 0
adjustment_sum: 7
attributes_total:
  STR: 7
  DEX: 19
  SKI: 18
  CON: 16
  RES: 15
  INT: 18
  WIS: 15
  CHA: 13
  SPI: 13
```

## Derived values

```yaml
bases:
  combat: 44
  athletic: 53
  operation: 51
  perception: 46
  knowledge: 49
  interaction: 41
resistances:
  anti_toxin: 31
  control: 30
  transform: 30
  breath: 34
  magic: 33
special_checks_before_other_modifiers:
  fortitude: 75
  mental: 70
  soul: 65
resources:
  hp: 23/23
  sp: 19/19
  cp_reserve: 23
```

## Creation CP ledger

```yaml
base_starting_cp: 200
adjusted_starting_cp: 230
creation_spent_cp: 210
creation_reserve_cp: 20
checkpoint_01_award_cp: 3
current_cp_reserve: 23
```

Recovered final skill / feat ledger:

```yaml
匕首: 2
閃避: 2
武器嫻熟: 1
及時備戰: 1
快速反射: 2
躲藏: 3
潛行: 3
解除裝置: 3
開鎖: 3
手上功夫: 3
搜索: 3
翻滾: 2
脫逃術: 2
隱密: 2
靈巧手指: 3
熟練手法: 1
聆聽: 2
偵察: 2
生存: 1
警覺: 2
自救: 2
耐久: 2
繩技: 2
估價: 2
唬騙: 2
偽造文書: 2
調查員: 2
欺詐: 1
地方知識: 1
搜集資訊: 1
```

## Languages

```yaml
通用語:
  level: 3
  source: free_creation_grant
additional_languages:
  status: no_recovered_evidence
```

## HP / SP creation evidence

```yaml
creation_reward_roll_recovered:
  hp: "1d8 = 7"
  sp: "1d4 = 4"
extra_hp_sp_purchase: none_recovered
final:
  hp: 23
  sp: 19
```

The recovered reward is consistent with the final total without requiring an invented extra HP/SP purchase.

## Equipment recovery boundary

```yaml
starting_magic_template: "+3 / +4 / +5 three-item template"
provisional_item_shell_candidate:
  - dagger
  - cloak
  - boots
exact_item_to_bonus_mapping: unresolved_not_finalized
exact_affixes: unresolved_not_finalized
```

The dagger/cloak/boots shell is not strong enough recovery evidence to become exact current equipment authority. Elian's invisibility cloak used in Session 1 is a borrowed Elian-owned item and must not be confused with Nella's starting equipment.

## Established session capabilities / knowledge

- Historical tail resolution used `athletic 53 + Hide 30 + synergy 20 = 103`, d100 `14`, success by `89`.
- Oren tail succeeded; Elian's cloak was later returned unused.
- No automatic romance/trust fact exists. New attraction or affect may only be established by 蟬 in PL+PC mode from the point of decision forward.
- Nella legitimately knows Elian's later spoken bardic/family disclosure; the earlier OOC/IC ambiguity does not retroactively establish prior knowledge.

## Character direction / current Andor thread

- Interested in gaps, routes and omissions; no magical spy omniscience.
- Moderate-high information risk tolerance, low pointless exposure.
- Current thread remains with Elian at the bard-academy departure boundary unless 蟬 later chooses otherwise.

## Provenance / closure

```yaml
recovery_sources:
  - prior_chat_character_creation_log
  - sessions/2026-09-15_session-1_runtime-migration.md
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
  - deterministic_D100_attribute_formulas
  - git_history_recovery_audit
recovery_exhausted:
  full_creation_ledger: recovered
  raw_stats_and_adjustments: recovered
  complete_skill_feat_list: recovered
  languages: recovered_to_available_evidence
  equipment_exact_mapping_and_affixes: unresolved_not_finalized
  starting_money: no_recovered_evidence
```
