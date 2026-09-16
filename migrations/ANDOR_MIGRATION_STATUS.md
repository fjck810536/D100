# Andor Migration Status

> This is the short current-status pointer. Detailed design/history remain in the Phase A / plan / Phase E documents.

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

storage_valid: true
manifest_initialized: true
persistence_status: clean
ready_for_explicit_cutover: true

cutover: false
main_merged: false
legacy_root_modified: false
legacy_root_cleanup_authorized: false
```

## Current authority

For migration verification on this feature branch：

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
→ current_state.md
→ exact actor masters / live session / site / Mystery refs
```

Do not use root `campaign/current_state.md` as Andor current state.

Do not use `characters/ACTIVE_PC_MANIFEST.md` as current actor index; it is stale historical recovery evidence.

## Critical regression status

```text
Mileia Lathander / Life Domain direct actor-master reload: PASS
Elian master not shrunk to session projection: PASS
Rook/Aster/Nella PL+PC mapping reload: PASS
Morninghall exists without silently moving Mileia: PASS
exact migrated ref aliases close active runtime refs: PASS
Google Drive full fresh-load backend smoke: PASS
```

## Cutover gate

The target is a valid initialized save, but explicit cutover remains false because：

```text
feature branch is still Draft PR #1
main has not been merged
legacy root records remain audit/history
no global campaign selection is performed automatically
```

When cutover is explicitly approved, update provider/cutover metadata for the merged storage location and run one final post-merge manifest fresh-load before declaring the migration complete.
