# D100-TEST-ANDOR-001 — Campaign Manifest

```yaml
schema_version: 1
campaign_id: D100-TEST-ANDOR-001
campaign_name: "Andor Session 1 Persistent Test"
created_at: "2026-09-16"

runtime_mode: persistent_test
party_mode: agent_pl_pc
world_resolution_mode: full
character_bootstrap_mode: import

ruleset:
  repository: fjck810536/D100
  ref: fc868904c4d9ded6d2f408ee25001dac5b2a70d5
  version_policy: pinned

source_policy:
  d100: primary
  srd_bridge: fallback
  raw_dnd35: last_resort

storage:
  backend: repo
  root_ref: campaign_instances/D100-TEST-ANDOR-001
  schema_version: 1
  write_scope: self_only
  promotion_allowed: explicit_only
  provider_metadata:
    branch: bootstrap-campaign-storage-v1

records:
  manifest_ref: campaign_instances/D100-TEST-ANDOR-001/manifest.md
  current_state_ref: campaign_instances/D100-TEST-ANDOR-001/current_state.md
  characters_root_ref: campaign_instances/D100-TEST-ANDOR-001/characters
  sessions_root_ref: campaign_instances/D100-TEST-ANDOR-001/sessions
  sites_root_ref: campaign_instances/D100-TEST-ANDOR-001/sites
  relationships_root_ref: campaign_instances/D100-TEST-ANDOR-001/relationships
  commitments_root_ref: campaign_instances/D100-TEST-ANDOR-001/commitments
  mystery_root_ref: campaign_instances/D100-TEST-ANDOR-001/mystery

indexes:
  characters:
    PC-ELIAN: campaign_instances/D100-TEST-ANDOR-001/characters/elian.md
    PC-ROOK: campaign_instances/D100-TEST-ANDOR-001/characters/rook.md
    PC-ASTER: campaign_instances/D100-TEST-ANDOR-001/characters/aster.md
    PC-MILEIA: campaign_instances/D100-TEST-ANDOR-001/characters/mileia.md
    PC-NELLA: campaign_instances/D100-TEST-ANDOR-001/characters/nella.md
  active_live_session_ref: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md

four_voice_control:
  mode: pl_pc
  mappings:
    - player_voice: 鮫島
      character_id: PC-ROOK
    - player_voice: 赫茲
      character_id: PC-ASTER
    - player_voice: 彌生
      character_id: PC-MILEIA
    - player_voice: 蟬
      character_id: PC-NELLA

bootstrap_status:
  storage_capability_verified: true
  manifest_readback_verified: false
  ruleset_ref_verified: true
  initialized: false

persistence:
  last_verified_at: null
  status: uninitialized
  last_error: null

migration:
  status: staged_phase_d_ref_normalization
  legacy_source_refs:
    - migrations/ANDOR_PHASE_A_INVENTORY_2026-09-16.md
    - sessions/2026-09-16_session-1_live-state.md
    - characters/elian.md
    - characters/rook.md
    - characters/aster.md
    - characters/mileia.md
    - characters/nella.md
  last_migration_ref: migrations/ANDOR_PHASE_A_INVENTORY_2026-09-16.md
  ref_alias_policy: exact_only
  ref_aliases:
    characters/elian.md: campaign_instances/D100-TEST-ANDOR-001/characters/elian.md
    characters/rook.md: campaign_instances/D100-TEST-ANDOR-001/characters/rook.md
    characters/aster.md: campaign_instances/D100-TEST-ANDOR-001/characters/aster.md
    characters/mileia.md: campaign_instances/D100-TEST-ANDOR-001/characters/mileia.md
    characters/nella.md: campaign_instances/D100-TEST-ANDOR-001/characters/nella.md
    sessions/2026-09-15_session-1_runtime-migration.md: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
    sessions/2026-09-15_session-1_checkpoint-01.md: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
    sessions/2026-09-16_session-1_live-state.md: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
    campaign/andor_sites.md: campaign_instances/D100-TEST-ANDOR-001/sites/andor_sites.md
    campaign/andor_map_adoption.md: campaign_instances/D100-TEST-ANDOR-001/sites/andor_map_adoption.md
    campaign/andor_public_map.md: campaign_instances/D100-TEST-ANDOR-001/sites/andor_public_map.md
    campaign/andor_lathander_morninghall.md: campaign_instances/D100-TEST-ANDOR-001/sites/andor_lathander_morninghall.md
    mystery_vault/ANDOR_BARD_ACADEMY_PATRON_01.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_ACADEMY_PATRON_01.md
    mystery_vault/ANDOR_BARD_HALL_DEPARTURE_01.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_HALL_DEPARTURE_01.md
    mystery_vault/ANDOR_BARD_HALL_OBSERVERS_01.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_BARD_HALL_OBSERVERS_01.md
    mystery_vault/ANDOR_SESSION1_CHECKPOINT_01.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_SESSION1_CHECKPOINT_01.md
    mystery_vault/ANDOR_SESSION1_MIGRATION.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_SESSION1_MIGRATION.md
    mystery_vault/ANDOR_WHISPERS_CONTACT.md: campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_WHISPERS_CONTACT.md
```

## Migration ref rule

Inside records loaded through this selected campaign manifest, the exact legacy state refs above resolve to the target paths above before any root/global mutable-state lookup. Unaliased external campaign-state paths are unresolved; they do not authorize fallback to legacy root state.

Repo-level D100 source/rule refs such as `sources/`, `00_core/` and `90_srd_bridge/` remain repo source refs and are not remapped.

> Staging fuse: this manifest is not the selected/cutover campaign until target-path readback and migration regression pass. Root legacy records remain untouched.
