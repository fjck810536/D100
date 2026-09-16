# Mileia / 米蕾亞 — Authoritative Character Record

> Recovery audit: `migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md`

```yaml
character_id: PC-MILEIA
name: Mileia
zh_name: 米蕾亞
race: human
age: approximately 25
controller:
  mode: pl_pc
  player_voice: 彌生
alignment:
  law_chaos: neutral
  good_evil: good
concept: Life Domain cleric / healer; temple and poorhouse medical-charity background
record_status: authoritative_recovered_with_unfinalized_fields
recovery_status: exhaustive_2026-09-16
```

## Identity / faith / domain

```yaml
faith:
  canonical_name: Lathander
  zh_name: 晨曦之主
  status: committed
  provenance: explicitly chosen during character creation; recovered after persistence audit
domain:
  - Life Domain / 生命領域
cleric_identity: committed
```

Lathander / Life Domain is a recovered player/PL creation decision, not a later inference from the local Morninghall or from generic Life Domain examples.

## Attributes

```yaml
attributes_raw:
  STR: 9
  DEX: 11
  SKI: 10
  CON: 16
  RES: 16
  INT: 15
  WIS: 19
  CHA: 17
  SPI: 19
adjustments:
  STR: -2
  DEX: -1
  SKI: -2
  CON: 2
  RES: 2
  INT: 1
  WIS: 3
  CHA: 2
  SPI: 3
adjustment_sum: 8
attributes_total:
  STR: 7
  DEX: 10
  SKI: 8
  CON: 18
  RES: 18
  INT: 16
  WIS: 22
  CHA: 19
  SPI: 22
```

## Derived values

```yaml
bases:
  combat: 25
  athletic: 36
  operation: 46
  perception: 56
  knowledge: 57
  interaction: 63
resistances:
  anti_toxin: 36
  control: 40
  transform: 36
  breath: 28
  magic: 34
special_checks_before_other_modifiers:
  fortitude: 80
  mental: 80
  soul: 95
resources:
  hp: 20/20
  sp: 35/35
  cp_reserve: 15
```

## Creation CP ledger

```yaml
base_starting_cp: 200
adjusted_starting_cp: 220
creation_spent_cp: 206
creation_reserve_cp: 14
checkpoint_01_award_cp: 1
current_cp_reserve: 15
```

Recovered final skill / feat ledger:

```yaml
宗教知識: 3
神術: 2
天界語: 1
引導神力: 3
驅散不死: 2
領域: 2
生命門徒: 3
護衛生命: 2
神力祝福: 1
戰鬥施法: 2
魔力擴展: 2
冥想: 3
鋼鐵意志: 2
耐久: 2
頑強: 1
強韌加強: 1
急救: 3
自救: 3
交涉: 2
察言觀色: 2
聆聽: 2
生存: 1
談判專家: 1
警覺: 1
```

Recovered category totals:

```text
core — 44 CP
cleric / Life Domain — 88 CP
defense — 22 CP
temple medicine / social — 52 CP
TOTAL — 206 CP
```

## Spellcasting identity

```yaml
core_levels:
  宗教知識: 3
  神術: 2
usable_spell_circle: 2
next_circle_partial_investment: true
prepared_spell_list: unresolved_not_finalized
named_spell_inventory: unresolved_not_finalized
slot_allocation: unresolved_not_finalized
```

No exact prepared/named spell list survived because none was cleanly finalized in the recovered creation log. Do not infer Zone of Truth or any other specific prepared spell from class identity alone.

## Languages

```yaml
通用語:
  level: 3
  source: free_creation_grant
天界語:
  level: 1
  source: finalized_creation_purchase
```

## HP / SP creation evidence

```yaml
creation_reward_roll_recovered:
  hp: "2d4 = 1 + 1 = 2"
  sp: "2d8 = 8 + 1 = 9"
final:
  hp: 20
  sp: 35
```

Final totals and reward dice are recovered. Other skill/item contributions to the final SP total were not separately preserved and must not be reverse-engineered as fake history.

## Equipment recovery boundary

```yaml
starting_magic_template: "+3 / +4 / +5 three-item template"
exact_item_to_bonus_mapping: unresolved_not_finalized
exact_affixes: unresolved_not_finalized
```

There is insufficient primary recovery evidence to promote a particular provisional staff/shield/holy-symbol/neck mapping into current authority.

## Character direction / current Andor boundary

- Care / medicine / social-presence orientation; does not imply party-mother autopilot.
- Moderate helping-risk tolerance.
- The earlier DM rollback restored Mileia to the immediate post-guild-split point and voided the erroneous south-care-node branch; those VOID facts remain non-canon.
- After that rollback, 彌生 lawfully chose for Mileia to seek the local Lathander temple. Mileia reached `SITE-ANDOR-LATHANDER-MORNINGHALL`, met Cael Arven, identified herself as a Lathander / Life Domain cleric, received a public-area orientation, and discussed her healing / temple / poorhouse-care background.
- Mileia accepted no job and received no automatic local authority. She plans to return for morning prayer and formal introduction before any collaboration.
- Current boundary: leaving / just left the Morninghall with ordinary directions toward nearby lodging. No exact inn, room, price, payment, or overnight stay is established.

## Provenance / closure

```yaml
recovery_sources:
  - prior_chat_character_creation_log
  - recovered_explicit_faith_decision
  - sources/GM_CLARIFICATIONS_2026-09-14_CHARACTER_CREATION.md
  - sessions/2026-09-15_session-1_runtime-migration.md
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-04.md
  - deterministic_D100_attribute_formulas
  - git_history_recovery_audit
recovery_exhausted:
  full_creation_ledger: recovered
  raw_stats_and_adjustments: recovered
  complete_skill_feat_list: recovered
  languages: recovered
  faith_and_domain: recovered
  equipment_exact_affixes: unresolved_not_finalized
  exact_spell_list_and_preparation: unresolved_not_finalized
  starting_money: no_recovered_evidence
```
