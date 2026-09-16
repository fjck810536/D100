# D100-TEST-ANDOR-001 — Current State

> Authoritative current-state pointer for the selected repo-local persistent-test namespace on `main`.

```yaml
campaign_id: D100-TEST-ANDOR-001
runtime_mode: persistent_test
record_status: active_selected_campaign_state
ruleset_ref: fc868904c4d9ded6d2f408ee25001dac5b2a70d5

world_time: split-thread chronology
active_camera: none

four_voice_control:
  mode: pl_pc
  mappings:
    - 鮫島 -> PC-ROOK
    - 赫茲 -> PC-ASTER
    - 彌生 -> PC-MILEIA
    - 蟬 -> PC-NELLA

party:
  PC-ELIAN:
    actor_ref: campaign_instances/D100-TEST-ANDOR-001/characters/elian.md
    controller: human_player
    current_boundary: just outside / leaving SITE-ANDOR-BARD-COLLEGE after common-hall departure
  PC-NELLA:
    actor_ref: campaign_instances/D100-TEST-ANDOR-001/characters/nella.md
    controller: 蟬_pl_pc
    current_boundary: with Elian at bard-academy departure point unless 蟬 later chooses otherwise
  PC-ROOK:
    actor_ref: campaign_instances/D100-TEST-ANDOR-001/characters/rook.md
    controller: 鮫島_pl_pc
    current_boundary: Mercenary Guild; convoy questions pending and not auto-resolved
  PC-ASTER:
    actor_ref: campaign_instances/D100-TEST-ANDOR-001/characters/aster.md
    controller: 赫茲_pl_pc
    current_boundary: Mercenary Guild; arcane-residue scheduling/registration pending and not auto-resolved
  PC-MILEIA:
    actor_ref: campaign_instances/D100-TEST-ANDOR-001/characters/mileia.md
    controller: 彌生_pl_pc
    current_boundary: immediate post-guild-split actor boundary from latest live-state pointer

active_live_session_ref: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
historical_session_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md

site_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sites/andor_sites.md
  - campaign_instances/D100-TEST-ANDOR-001/sites/andor_map_adoption.md
  - campaign_instances/D100-TEST-ANDOR-001/sites/andor_lathander_morninghall.md
public_map_ref: campaign_instances/D100-TEST-ANDOR-001/sites/andor_public_map.md

mystery_refs:
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_ACADEMY_PATRON_01.md
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_HALL_DEPARTURE_01.md
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_HALL_OBSERVERS_01.md
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_SESSION1_CHECKPOINT_01.md
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_SESSION1_MIGRATION.md
  - campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_WHISPERS_CONTACT.md

runtime_incident_refs:
  - OOC-AMBIG-ANDOR-001
  - MILEIA-LINE-ROLLBACK-2026-09-16

migration_fuses:
  legacy_campaign_current_state_is_not_authority: true
  stale_active_pc_manifest_is_not_current_actor_index: true
  morninghall_site_exists_without_implying_mileia_arrival: true
  session_projection_does_not_replace_actor_master: true
```

## Interpretation boundary

- `campaign/andor_lathander_morninghall.md` was committed after the Mileia rollback and remains a valid Andor world/site record.
- Its existence does **not** establish that Mileia arrived there, met Cael, or acquired local knowledge. Mileia's actor pointer remains at the latest live-state boundary until play advances it.
- Root `campaign/current_state.md` is a stale generic legacy placeholder and is not Andor authority.
- `characters/ACTIVE_PC_MANIFEST.md` is historical recovery-gap evidence, not the current actor index.
- Migrated records may retain literal legacy paths as historical text. Runtime resolution follows manifest `migration.ref_aliases` exactly; unaliased external mutable-state paths do not fall back to root.

## Verification status

```yaml
migration_phase: cutover_complete
storage_valid: true
cutover: true
main_merged: true
legacy_records_modified: false
readback_verified: true
verification_ref: migrations/ANDOR_POST_MERGE_READBACK_2026-09-16.md
```
