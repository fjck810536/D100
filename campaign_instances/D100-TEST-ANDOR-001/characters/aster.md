# Aster Veyn / 艾斯特・維恩 — Authoritative Character Record

> Recovery audit: `migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md`

```yaml
character_id: PC-ASTER
name: Aster Veyn
zh_name: 艾斯特・維恩
race: human
age: approximately 23-24
controller:
  mode: pl_pc
  player_voice: 赫茲
alignment:
  law_chaos: neutral
  good_evil: good
concept: formally educated theory-oriented young wizard; not a prodigy
record_status: authoritative_recovered_with_unfinalized_fields
recovery_status: exhaustive_2026-09-16
```

## Attributes

```yaml
attributes_raw:
  STR: 9
  DEX: 10
  SKI: 11
  CON: 10
  RES: 17
  INT: 18
  WIS: 13
  CHA: 9
  SPI: 13
adjustments:
  STR: -2
  DEX: -2
  SKI: -1
  CON: -2
  RES: 2
  INT: 3
  WIS: 0
  CHA: -2
  SPI: 0
adjustment_sum: -4
attributes_total:
  STR: 7
  DEX: 8
  SKI: 10
  CON: 8
  RES: 19
  INT: 21
  WIS: 13
  CHA: 7
  SPI: 13
```

## Derived values

```yaml
bases:
  combat: 25
  athletic: 26
  operation: 44
  perception: 53
  knowledge: 51
  interaction: 33
resistances:
  anti_toxin: 27
  control: 32
  transform: 38
  breath: 27
  magic: 40
special_checks_before_other_modifiers:
  fortitude: 50
  mental: 85
  soul: 65
resources:
  hp: 30/30
  sp: 52/52
  cp_reserve: 52
```

## Creation CP ledger

```yaml
base_starting_cp: 200
adjusted_starting_cp: 340
skill_feat_spent_cp: 266
hp_purchase_cp: 24
creation_total_spent_cp: 290
creation_reserve_cp: 50
checkpoint_01_award_cp: 2
current_cp_reserve: 52
```

### Core + language — 52 CP

```yaml
奧術知識: 3
黑魔導: 3
黑魔力: 2
龍語: 1
```

### Mage toolkit — 148 CP

```yaml
戰鬥施法: 3
魔力擴展: 3
高級魔力擴展: 1
冥想: 3
法術穿透: 3
法術熟稔: 2
辨識法術: 3
魔法物品學: 3
魔法天賦: 2
魔法陣基礎學: 2
施法免材: 2
移動施法: 2
使用魔法裝置: 2
魔力延展: 2
```

### Defense — 24 CP

```yaml
鋼鐵意志: 2
耐久: 2
自救: 2
```

### Scholar / life — 42 CP

```yaml
細緻: 2
文書解讀: 2
搜索: 2
估價: 2
歷史: 2
地方: 2
專業〔抄寫／書記〕: 2
```

## Spellcasting identity

```yaml
core_levels:
  奧術知識: 3
  黑魔導: 3
  黑魔力: 2
usable_spell_circle: 2
next_circle_partial_investment: true
school_specialization:
  status: generalist_no_formal_specialization_at_creation_boundary
known_spell_list: unresolved_not_finalized
prepared_spell_list: unresolved_not_finalized
slot_allocation: unresolved_not_finalized
grimoire_contents: unresolved_not_finalized
```

No hidden spell list should be invented during recovery. If play later needs a specific spell, establish it through a lawful new character-development / preparation decision rather than pretending it was recovered.

## Languages

```yaml
通用語:
  level: 3
  source: free_creation_grant
龍語:
  level: 1
  source: finalized_creation_purchase
```

## HP / SP creation evidence

```yaml
creation_reward_roll_recovered:
  hp: "2d4 = 1 + 3 = 4"
  sp: "2d8 = 5 + 8 = 13"
hp_purchase:
  cp_spent: 24
  hp_added: 18
final:
  hp: 30
  sp: 52
```

The 24-CP HP purchase and final totals are established. Other intermediate HP/SP contributions were not preserved separately and must not be fabricated.

## Equipment recovery boundary

Recovered accepted rerun shell:

```yaml
item_types:
  - staff
  - ring
  - head_item
starting_magic_template: "+3 / +4 / +5 three-item template"
exact_bonus_mapping: unresolved_not_finalized
exact_affixes: unresolved_not_finalized
```

Superseded provisional material such as `+4 staff〔儲魔+3〕 / +3 ring〔隱形+2〕 / +2 headband〔光亮+1〕` is not current authority.

## Character direction / current Andor thread

- Scholar orientation; curious but cautious, not an exposition terminal.
- Interested in arcane residue and in understanding Academy access changes / why attention fell on him.
- Current Andor thread: remains at Mercenary Guild asking about residue-work timing and possible registration; no off-camera acceptance/resolution.

## Provenance / closure

```yaml
recovery_sources:
  - prior_chat_character_creation_log
  - sources/GM_CLARIFICATIONS_2026-09-14_CHARACTER_CREATION.md
  - examples/CHARACTER_CREATION_REGRESSION.md
  - sessions/2026-09-15_session-1_runtime-migration.md
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - deterministic_D100_attribute_formulas
  - git_history_recovery_audit
recovery_exhausted:
  full_creation_ledger: recovered
  raw_stats_and_adjustments: recovered
  complete_skill_feat_list: recovered
  languages: recovered
  equipment_exact_affixes: unresolved_not_finalized
  exact_spell_list_and_preparation: unresolved_not_finalized
  starting_money: no_recovered_evidence
```
