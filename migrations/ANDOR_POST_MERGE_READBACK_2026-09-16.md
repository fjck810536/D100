# Andor Post-Merge Fresh-Load Verification — 2026-09-16

```yaml
campaign_id: D100-TEST-ANDOR-001
verification_scope: main_post_merge
merge_commit: a1625f591c9eba20410ec24f3abb89bf7a27a631
result: PASS
```

## Procedure

Fresh-load was performed from `main` only:

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
→ current_state.md
→ exact actor master directory/index
→ Mileia authoritative master
→ active live session
→ target sites collection
→ target Mystery collection existence / blob identity
```

No feature-branch-only path was required for reload.

## Verified

```yaml
manifest_on_main: PASS
current_state_on_main: PASS
five_actor_masters_on_main: PASS
active_live_session_on_main: PASS
site_collection_on_main: PASS
mystery_collection_on_main: PASS
exact_blob_identity_preserved: PASS
mileia_faith_domain_reload: PASS
legacy_root_required_for_active_reload: false
```

Mileia still reloads directly from the actor master as:

```text
Lathander / 晨曦之主
Life Domain / 生命領域
```

The live session still preserves the Mileia rollback boundary and does not establish post-split arrival/contact merely because the Morninghall site exists.

## Cutover consequence

This verification satisfies the final migration gate for switching the repo-local provider metadata to `main` and setting the Andor manifest `migration.cutover: true`.

Legacy root records are intentionally retained as audit/history and are not cleaned up by this cutover.
