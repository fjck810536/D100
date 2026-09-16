# Andor Character Recovery Status

```yaml
campaign_id: D100-TEST-ANDOR-001
recovery_audit: migrations/ANDOR_CHARACTER_RECOVERY_AUDIT_2026-09-16.md
status: exhaustive_recovery_complete
selected_campaign_only: true
legacy_root_rewritten: false
exact_actor_readback: PASS
persistence_status: clean
```

## Actor recovery

```yaml
PC-ROOK:
  raw_attributes: recovered
  adjustments: recovered
  full_skill_feat_ledger: recovered
  creation_cp_ledger: recovered
  languages: recovered_to_available_evidence
  exact_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized

PC-ASTER:
  raw_attributes: recovered
  adjustments: recovered
  full_skill_feat_ledger: recovered
  creation_cp_ledger: recovered
  languages: recovered
  usable_spell_circle: recovered
  exact_spell_list_and_preparation: unresolved_not_finalized
  exact_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized

PC-MILEIA:
  raw_attributes: recovered
  adjustments: recovered
  full_skill_feat_ledger: recovered
  creation_cp_ledger: recovered
  faith_and_domain: recovered
  languages: recovered
  usable_spell_circle: recovered
  exact_spell_list_and_preparation: unresolved_not_finalized
  exact_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized

PC-NELLA:
  raw_attributes: recovered
  adjustments: recovered
  full_skill_feat_ledger: recovered
  creation_cp_ledger: recovered
  languages: recovered_to_available_evidence
  exact_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized

PC-ELIAN:
  raw_attributes: recovered
  adjustments: recovered
  full_skill_feat_ledger: recovered
  creation_cp_ledger: recovered
  languages: recovered_to_available_evidence
  special_equipment_ownership: recovered
  special_equipment_exact_rule_interfaces: unresolved_rule_interface
```

## CP continuity cross-check

```text
Rook   creation reserve 40 + checkpoint 1 = current 41  PASS
Aster  creation reserve 50 + checkpoint 2 = current 52  PASS
Mileia creation reserve 14 + checkpoint 1 = current 15  PASS
Nella  creation reserve 20 + checkpoint 3 = current 23  PASS
Elian  creation reserve 10 + checkpoint 3 = current 13  PASS
```

## Meaning of closure

`exhaustive_recovery_complete` does not mean every possible character field now has a value. It means all currently accessible recovery sources have been exhausted and surviving gaps are classified correctly:

- `unresolved_not_finalized` = no final value existed in the recovered creation process;
- `no_recovered_evidence` = no evidence was found, but future primary evidence can still override;
- `unresolved_rule_interface` = the item/fact exists, but its exact mechanics remain a rules question rather than lost actor state.

Do not turn any of those statuses into invented retroactive character facts.
