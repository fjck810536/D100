# MIGRATION_REF_ALIAS_REGRESSION.md

> Tests exact legacy campaign-state ref aliases used when migrating immutable/history-heavy records into an isolated selected campaign namespace.

## A1 — Exact alias resolves inside selected campaign

Given selected campaign manifest：

```yaml
storage:
  root_ref: campaign_instances/CAMPAIGN-A
migration:
  ref_alias_policy: exact_only
  ref_aliases:
    campaign/old_sites.md: campaign_instances/CAMPAIGN-A/sites/old_sites.md
```

And a migrated session contains：

```text
campaign/old_sites.md
```

Expected：

```text
resolve exact alias
→ campaign_instances/CAMPAIGN-A/sites/old_sites.md
→ verify target is inside selected CAMPAIGN-A
→ read target
```

Fail if runtime reads root `campaign/old_sites.md` instead.

---

## A2 — No prefix / fuzzy guessing

Manifest aliases only：

```text
campaign/old_sites.md
```

Record asks for：

```text
campaign/old_site.md
campaign/sub/old_sites.md
OLD_SITES
```

Expected：unresolved unless separately indexed.

Fail if runtime performs fuzzy or prefix matching.

---

## A3 — Alias target outside selected namespace is invalid

Selected root：

```text
campaign_instances/CAMPAIGN-A
```

Alias target：

```text
campaign_instances/CAMPAIGN-B/characters/alice.md
```

Expected：reject alias / storage integrity error.

Fail if Campaign A is allowed to read Campaign B mutable actor state through migration alias.

---

## A4 — Unaliased legacy mutable state does not fall back

Migrated record contains：

```text
campaign/deleted_or_unmapped_state.md
```

No exact alias exists.

Expected：

```text
unresolved mutable-state ref
```

not：

```text
read legacy repo root because path exists / once existed
```

Historical prose may mention such a path without triggering a read.

---

## A5 — Repo source refs are not campaign aliases

Migrated site record contains：

```text
sources/sheet_mirror/01_world_core.json.md
00_core/combat.md
90_srd_bridge/...
```

Expected：normal repo-level source/rule lookup.

Fail if campaign aliasing rewrites these into campaign storage.

---

## A6 — Andor active live-state closure

For staged campaign：

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
```

The byte-identical migrated active live-state still contains legacy refs:

```text
sessions/2026-09-15_session-1_checkpoint-01.md
sessions/2026-09-15_session-1_runtime-migration.md
campaign/andor_sites.md
campaign/andor_map_adoption.md
campaign/andor_public_map.md
mystery_vault/ANDOR_SESSION1_MIGRATION.md
mystery_vault/ANDOR_WHISPERS_CONTACT.md
mystery_vault/ANDOR_BARD_HALL_OBSERVERS_01.md
mystery_vault/ANDOR_BARD_HALL_DEPARTURE_01.md
characters/mileia.md
```

Expected：every runtime-relevant mutable-state ref above has an exact manifest alias to a record under：

```text
campaign_instances/D100-TEST-ANDOR-001/
```

Special rollback audit text：

```text
campaign/andor_south_care_node.md
```

must **not** receive an alias because that state was removed/voided. Merely mentioning the deleted path as historical audit text does not trigger a read.

---

## A7 — New writes use current refs

Aliases are migration compatibility, not a reason to keep generating legacy refs forever.

After migration/cutover, a newly written session should directly use：

```text
campaign_instances/CAMPAIGN-A/...
```

or provider-native exact refs.

Fail if new runtime output keeps accumulating root legacy `campaign/`, `characters/`, `sessions/`, or `mystery_vault/` references.
