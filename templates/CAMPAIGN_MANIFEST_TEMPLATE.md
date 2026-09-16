# Campaign Manifest Template

> 每一團的唯一啟動索引。這不是世界設定本文，而是告訴 runtime：這是哪一團、規則版本是什麼、存檔在哪、角色與 state 應去哪裡讀。

```yaml
schema_version: 1

campaign_id: CAMPAIGN-REPLACE-ME
campaign_name: ""
created_at: ""

runtime_mode: persistent_campaign   # persistent_campaign | persistent_test | isolated_dry_run

party_mode: solo                    # solo | multiplayer | agent_pl_pc | digital_npc
world_resolution_mode: full         # full | quick
character_bootstrap_mode: assisted  # assisted | import | auto | deferred

ruleset:
  repository: fjck810536/D100
  ref: ""                         # commit SHA / release ref captured at campaign creation
  version_policy: pinned            # pinned | explicit_migration_only

source_policy:
  d100: primary
  srd_bridge: fallback
  raw_dnd35: last_resort

storage:
  backend: ""                      # repo | google_drive | local_folder | external_git | other
  root_ref: ""
  schema_version: 1
  write_scope: self_only
  promotion_allowed: explicit_only

records:
  current_state_ref: ""
  characters_root_ref: ""
  sessions_root_ref: ""
  sites_root_ref: ""
  relationships_root_ref: ""
  commitments_root_ref: ""
  mystery_root_ref: ""

four_voice_control:
  mode: npc                         # npc | pl_pc
  mappings: []

bootstrap_status:
  storage_capability_verified: false
  ruleset_ref_verified: false
  initialized: false

migration:
  legacy_source_refs: []
  last_migration_ref: null
```

## Required invariants

```text
campaign_id is unique within the selected storage root
ruleset.ref is explicit before scene runtime starts
storage.root_ref is stable and re-readable
write_scope is self_only
persistent_test cannot implicitly promote into another campaign
records point to this campaign's own namespace
```

## Notes

- `isolated_dry_run` 通常不需要真正建立 manifest；若建立，只能作 working descriptor，不可因此取得 writeback 權限。
- `multiplayer` 目前可記錄，但 runtime 必須標示 unsupported，不能假裝已有多使用者身份隔離。
- provider-specific file / folder ids 可放入 `storage.provider_metadata` 或 `records.*_ref`；不要只依檔名搜尋。
