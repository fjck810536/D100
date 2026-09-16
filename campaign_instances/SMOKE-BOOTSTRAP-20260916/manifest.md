# Smoke Campaign Manifest

```yaml
schema_version: 1
campaign_id: SMOKE-BOOTSTRAP-20260916
campaign_name: Bootstrap Smoke Test
runtime_mode: persistent_test
party_mode: solo
world_resolution_mode: full
character_bootstrap_mode: assisted
ruleset:
  repository: fjck810536/D100
  ref: fc868904c4d9ded6d2f408ee25001dac5b2a70d5
  version_policy: pinned
storage:
  backend: repo
  root_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916
  schema_version: 1
  write_scope: self_only
  promotion_allowed: explicit_only
records:
  manifest_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916/manifest.md
  current_state_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916/current_state.md
  characters_root_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916/characters
  sessions_root_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916/sessions
indexes:
  characters:
    PC-SMOKE: campaign_instances/SMOKE-BOOTSTRAP-20260916/characters/smoke.md
  active_live_session_ref: campaign_instances/SMOKE-BOOTSTRAP-20260916/sessions/live.md
bootstrap_status:
  storage_capability_verified: true
  manifest_readback_verified: false
  ruleset_ref_verified: true
  initialized: false
persistence:
  status: uninitialized
```
