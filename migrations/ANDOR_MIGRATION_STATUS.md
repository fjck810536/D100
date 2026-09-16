# Andor Migration Status

> Current short-status pointer after explicit merge and cutover.

```yaml
campaign_id: D100-TEST-ANDOR-001
source_form: legacy_root_scattered_state
target_root: campaign_instances/D100-TEST-ANDOR-001
runtime_mode: persistent_test

phase_A_inventory: PASS
phase_B_namespace_build: PASS
phase_C_actor_master_verification: PASS
phase_D_ref_alias_closure: PASS
phase_E_fresh_load_readback: PASS
post_merge_fresh_load: PASS

storage_valid: true
manifest_initialized: true
persistence_status: clean
ready_for_explicit_cutover: true

cutover: true
main_merged: true
merge_commit: a1625f591c9eba20410ec24f3abb89bf7a27a631
post_merge_verification_ref: migrations/ANDOR_POST_MERGE_READBACK_2026-09-16.md
legacy_root_modified: false
legacy_root_cleanup_authorized: false
```

## Current authority

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
→ current_state.md
→ exact actor masters / active live session / site / Mystery refs
```

The repo-local provider is now `main`.

Do not use root `campaign/current_state.md` as Andor current state.

Do not use `characters/ACTIVE_PC_MANIFEST.md` as the current actor index; it remains stale historical recovery evidence.

## Critical regression status

```text
Mileia Lathander / Life Domain direct actor-master reload: PASS
Elian master not shrunk to session projection: PASS
Rook/Aster/Nella PL+PC mapping reload: PASS
Morninghall exists without silently moving Mileia: PASS
exact migrated ref aliases close active runtime refs: PASS
Google Drive full fresh-load backend smoke: PASS
main post-merge fresh-load: PASS
```

## Legacy cleanup boundary

Legacy root records remain available as audit/history. Cutover does not authorize deleting or rewriting them.

```text
cutover complete ≠ legacy cleanup authorized
```
