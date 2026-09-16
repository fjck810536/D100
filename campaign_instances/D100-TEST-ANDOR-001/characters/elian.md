# Elian de Valer / 埃利安・德・瓦雷 — Authoritative Character Record

> Recovery audit: `migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md`

```yaml
character_id: PC-ELIAN
name: Elian de Valer
zh_name: 埃利安・德・瓦雷
race: human
age: approximately 21-24
controller:
  mode: player_pc
alignment:
  law_chaos: chaotic
  good_evil: neutral
concept: runaway fallen / financially weak minor noble; noncaster
record_status: authoritative_recovered_with_unfinalized_fields
recovery_status: exhaustive_2026-09-16
```

## Attributes

```yaml
attributes_raw:
  STR: 16
  DEX: 19
  SKI: 18
  CON: 18
  RES: 12
  INT: 22
  WIS: 14
  CHA: 12
  SPI: 10
adjustments:
  STR: 2
  DEX: 3
  SKI: 3
  CON: 3
  RES: -1
  INT: 5
  WIS: 1
  CHA: -1
  SPI: -2
adjustment_sum: 13
attributes_total:
  STR: 18
  DEX: 22
  SKI: 21
  CON: 21
  RES: 11
  INT: 27
  WIS: 15
  CHA: 11
  SPI: 8
```

## Derived values

```yaml
bases:
  combat: 61
  athletic: 64
  operation: 63
  perception: 46
  knowledge: 63
  interaction: 34
resistances:
  anti_toxin: 32
  control: 26
  transform: 22
  breath: 33
  magic: 38
special_checks_before_other_modifiers:
  fortitude: 90
  mental: 60
  soul: 50
resources:
  hp: 31/31
  sp: 17/17
  cp_reserve: 13
```

## Creation CP ledger

```yaml
base_starting_cp: 200
adjusted_starting_cp: 170
creation_spent_cp: 160
creation_reserve_cp: 10
checkpoint_01_award_cp: 3
current_cp_reserve: 13
```

### Sword / combat — 76 CP

```yaml
長劍: 3
閃避: 3
格擋: 3
專攻長劍: 3
武器專精: 2
及時備戰: 2
翻滾: 2
快速反射: 1
```

### Noble education — 68 CP

```yaml
騎術: 2
交涉: 3
察言觀色: 2
貴族與皇室: 3
歷史: 2
估價: 2
文書解讀: 2
唬騙: 2
談判專家: 1
細緻: 1
```

### Travel / body — 16 CP

```yaml
搜索: 1
偵察: 1
聆聽: 1
攀爬: 1
游泳: 1
平衡感: 1
耐久: 1
頑強: 1
```

## Established skill interfaces used in play

```yaml
Search: 56
Sense_Motive_historical_runtime: 54
Bluff: 54
```

These historical interface values remain valid evidence for the already resolved rolls; do not retroactively rerun them merely because the underlying creation ledger has now been recovered.

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
creation_reward_floor_recovered:
  hp_added: 7
  sp_added: 3
final:
  hp: 31
  sp: 17
```

Final totals are authoritative. Surviving creation evidence does not justify inventing a more detailed intermediate HP/SP decomposition.

## Established equipment

- ordinary longsword;
- invisibility cloak, 3/day, Elian owner/holder, unused 3/3 at the recorded boundary;
- Dimension Door ring, 3/day;
- air-walk boots, at least 3h/day.

Unresolved item-rule interfaces:

```yaml
invisibility_cloak_activation_duration_transfer: unresolved_rule_interface
Dimension_Door_ring_range_targets_activation: unresolved_rule_interface
air_walk_boots_duration_split_activation: unresolved_rule_interface
```

These are missing mechanics, not missing ownership/equipment facts.

## Money / current accounting boundary

- Session 1 started from an established 50 gp cash figure; wagon fare `-1 gp` and meal `-4 gp` produced 45 gp at checkpoint.
- Later bard-hall drinks were purchased without numeric menu prices, and 3 literal silver coins were left on the table at departure.
- Do not invent an exact post-bard-hall remaining gp total until prices are lawfully reconciled.

## Established background

- Human runaway from a fallen / financially weak minor-noble family context; exact title, inheritance structure and family politics remain partly unspecified.
- No prior bardic training.
- Old home/family discouraged bardic arts and expected him to take on intellectual/administrative work around his older brother.
- Elian remembers the older brother as the genuinely more eloquent / charismatic one.
- Elian's stated practical attitude: unfamiliar but useful methods are worth trying; if he cannot do something, use/rely on people who can.
- These later bardic/family facts were spoken aloud to Nella and are valid IC knowledge for her from that disclosure onward.

## Current Andor thread

- Registered the one-day Three Silver Coins document/inventory verification job at the Mercenary Guild.
- Bard-academy thread is paused after departure with Nella.
- `Elian, Three Silver Coins` was used as name/contact-lodging answer without proving a paid room.

## Superseded build fuse

An older approximately-300-CP Elian version with substantially different attributes and HP/SP existed during earlier iteration. It is `superseded` and must never be merged with this accepted 170-CP build.

## Provenance / closure

```yaml
recovery_sources:
  - prior_chat_character_creation_log
  - explicit_player_alignment_and_background_declarations
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
  special_equipment_ownership: recovered
  special_equipment_exact_rule_interfaces: unresolved_rule_interface
  exact_post_bard_hall_money: unresolved_due_unpriced_transactions
```
