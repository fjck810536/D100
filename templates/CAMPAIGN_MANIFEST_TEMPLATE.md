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
  resolved_commit_sha: ""          # full immutable commit SHA; resolve release/tag to commit
  version_label: null               # optional display tag/release name; never the immutable pin
  version_policy: pinned            # pinned | explicit_migration_only

source_policy:
  d100: primary
  srd_bridge: fallback
  raw_dnd35: last_resort

storage:
  backend: ""                      # repo | google_drive | local_folder | external_git | other
  root_ref: ""                     # stable campaign root locator
  schema_version: 1
  write_scope: self_only
  promotion_allowed: explicit_only
  provider_metadata: {}

records:
  manifest_ref: ""                 # stable provider ID / path for this manifest when applicable
  current_state_ref: ""
  characters_root_ref: ""
  sessions_root_ref: ""
  sites_root_ref: ""
  relationships_root_ref: ""
  commitments_root_ref: ""
  mystery_root_ref: ""

indexes:
  characters: {}                    # optional: character_id -> stable record ref
  active_live_session_ref: null

four_voice_control:
  mode: npc                         # npc | pl_pc
  mappings: []

bootstrap_status:
  storage_capability_verified: false
  manifest_readback_verified: false
  ruleset_ref_verified: false
  initialized: false

persistence:
  last_verified_at: null
  status: uninitialized             # uninitialized | clean | uncommitted | degraded
  last_error: null

migration:
  status: null
  legacy_source_refs: []
  last_migration_ref: null
  ref_alias_policy: none            # none | exact_only
  ref_aliases: {}                   # exact legacy state ref -> exact selected-campaign record ref
```

## Required invariants

```text
campaign_id is unique within the selected storage root
ruleset.ref is explicit before scene runtime starts
new manifests store ruleset.resolved_commit_sha as the immutable full commit SHA for rules/protocol reads
legacy full-SHA ruleset.ref remains a valid immutable pin without new fields (see bootstrap protocol)
storage.root_ref is stable and re-readable
storage.root_ref is independently selected, not inferred from ruleset.repository or public visibility
selected storage identity/target has verified LOCATE/LIST/READ/CREATE/UPDATE capabilities
write_scope is self_only
persistent_test cannot implicitly promote into another campaign
records point to this campaign's own namespace
manifest_ref / record refs use provider-stable locators when available
character master lookup prefers character_id -> exact record ref, not global title search
```

## Legacy ref alias invariant

Migration may preserve immutable historical record text while remapping old campaign-state paths through exact manifest aliases.

Example：

```yaml
migration:
  ref_alias_policy: exact_only
  ref_aliases:
    campaign/old_sites.md: campaign_instances/CAMPAIGN-X/sites/old_sites.md
```

Rules：

```text
alias match must be exact
alias target must resolve inside the selected campaign namespace
alias is for campaign-state refs, not D100 source/rule refs
unaliased external mutable-state ref is not allowed to silently fall back to another campaign/root
legacy provenance text may remain literal history and does not automatically trigger a state read
```

This allows byte-identical migrated records to preserve audit history without making the selected campaign depend on legacy root state.

## Notes

- Ruleset 解析、舊 release-only manifest 相容與 explicit migration 依 `BOOTSTRAP_PROTOCOL.md` 第 4 節；既有 full-SHA manifest 不需只為補欄位而改寫。`version_label` 可省略；無 tag 時顯示短 SHA、保存完整 SHA，`main` 不作 immutable pin。
- Git storage 的 `provider_metadata` 記錄 repository / branch / campaign path；`root_ref` 與所有 records 指向玩家選定的可寫 namespace。公開 upstream／Pages 不自動提供 campaign 寫權。
- `isolated_dry_run` 通常不需要真正建立 manifest；若建立，只能作 working descriptor，不可因此取得 writeback 權限。
- `multiplayer` 目前可記錄，但 runtime 必須標示 unsupported，不能假裝已有多使用者身份隔離。
- provider-specific file / folder ids 放入 `storage.provider_metadata`、`records.*_ref` 或 `indexes`；不要只依檔名搜尋。
- Google Drive backend 的 creation / self-reference / readback 順序見 `storage_backends/GOOGLE_DRIVE.md`。
- Repo-local backend 的 instance root 見 `campaign_instances/README.md`。
