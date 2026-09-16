# Google Drive Backend Smoke Test — 2026-09-16

> Test scope: live capability, stable-ID semantics, full campaign namespace creation, actor-master/session separation, fresh-load by root/manifest refs, update/readback, and cleanup. No real campaign data migrated.

## Environment observation

The active Google Drive connection behaves as OAuth / delegated rather than direct service-account mode for native document creation.

Observed:

```text
create native Google Doc with parent_folder_id
→ rejected with explicit provider error
```

Therefore the backend must support:

```text
create native document in default Drive parent
→ get exact file ID + current parent
→ move same file ID into selected campaign root / collection
→ verify parent
```

This matches `storage_backends/GOOGLE_DRIVE.md` section "Move after create".

---

## Smoke A — Core provider operations

Temporary root:

```text
D100_BACKEND_SMOKE_TEST_2026-09-16
```

Sequence executed:

```text
CREATE root folder
→ CREATE native Google Doc
→ GET metadata / exact file ID + original parent
→ MOVE same ID into root
→ WRITE v1
→ exact-ID READ v1
→ LIST root
→ UPDATE same ID v1 -> v2
→ exact-ID READ v2
→ DELETE document/root
```

Results:

```yaml
LOCATE: PASS
LIST: PASS
READ: PASS
CREATE: PASS
UPDATE_SAME_ID: PASS
MOVE_SAME_ID: PASS
READBACK_AFTER_UPDATE: PASS
CLEANUP: PASS
```

The update did not create a replacement document. The exact same Drive file ID remained authoritative.

---

## Smoke B — Full persistent-test campaign fresh-load regression

Temporary campaign root:

```text
D100_FULL_CAMPAIGN_SMOKE_2026-09-16
```

Created physical Drive namespace:

```text
root/
├── manifest
├── current_state
├── characters/
│   └── PC-SMOKE-MILEIA
├── sessions/
│   └── live_session
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

All records/folders received stable Drive IDs. `manifest` recorded exact refs for every collection plus:

```text
current_state_ref
character_index.PC-SMOKE-MILEIA
live_session_ref
ruleset_ref
storage_root_ref
```

### Deliberate regression setup

The authoritative character master contained:

```text
character_id = PC-SMOKE-MILEIA
faith = Lathander / 晨曦之主
domain = Life / 生命領域
alignment = neutral_good
full master marker = character-master-v1
```

The live session intentionally contained only a runtime projection:

```text
hp = 17/20
sp = 31/35
Search = 46
```

and explicitly omitted:

```text
faith
domain
alignment
full skill list
```

This reproduces the failure class behind the Mileia incident: a session projection is intentionally incomplete and must never become the whole character.

### Fresh-load simulation

The reload phase was intentionally started from only the campaign `root_ref`:

```text
root_ref
→ LIST root
→ locate the unique manifest
→ READ manifest
→ follow exact current_state_ref
→ follow exact character_index ref
→ follow exact live_session_ref
```

No global Drive search for `Mileia` was used to recover the actor.

Readback recovered:

```text
current state:
  runtime_mode = persistent_test
  location = TEST-CHAPEL
  party includes PC-SMOKE-MILEIA

character master:
  faith = Lathander / 晨曦之主
  domain = Life / 生命領域
  alignment = neutral_good

live session:
  hp = 17/20
  sp = 31/35
  Search = 46
  faith/domain absent by design
```

Therefore:

```text
session projection missing a field
!=
character master missing that field
```

and the fresh-load path successfully recovers permanent actor identity from the exact actor master.

### Full campaign results

```yaml
ROOT_CREATE: PASS
COLLECTION_FOLDERS_CREATE: PASS
MANIFEST_STABLE_ID: PASS
CURRENT_STATE_STABLE_ID: PASS
CHARACTER_MASTER_STABLE_ID: PASS
LIVE_SESSION_STABLE_ID: PASS
EXACT_PARENT_PLACEMENT: PASS
MANIFEST_EXACT_REF_INDEX: PASS
FRESH_LOAD_FROM_ROOT: PASS
CURRENT_STATE_READ_BY_MANIFEST_REF: PASS
CHARACTER_READ_BY_EXACT_ID: PASS
SESSION_READ_BY_EXACT_ID: PASS
MILEIA_FAITH_SURVIVES_SESSION_OMISSION: PASS
MILEIA_DOMAIN_SURVIVES_SESSION_OMISSION: PASS
SESSION_DOES_NOT_REPLACE_CHARACTER_MASTER: PASS
CLEANUP: PASS
```

---

## Cleanup verification

The entire full-smoke root was permanently deleted after readback. Verification used both:

```text
Drive search for D100_FULL_CAMPAIGN_SMOKE_2026-09-16 -> no result
exact root ID metadata lookup -> 404 / not found
```

An accidentally created `relationships-index` subfolder existed only inside the temporary smoke root and was removed with the root. No pre-existing user Drive file was modified.

---

## Connector-specific notes

### Native Doc placement

Current OAuth/delegated connection requires:

```text
create
→ capture ID/current parent
→ move same ID
→ verify parent
```

rather than creating a native Doc directly under `parent_folder_id`.

### Folder deletion

For the current connector, the normal folder URL form was not accepted by the generic delete action, while a Drive file-ID URL form using the same folder ID was accepted. This is a connector invocation detail, not campaign schema.

---

## What is now proven

For the currently connected Google Drive environment, the backend can support the core D100 campaign save contract:

```text
one campaign root
→ stable manifest
→ stable collection refs
→ exact actor master refs
→ session as live delta/projection
→ fresh reload without chat memory
→ in-place persistent update/readback
```

The critical regression target is demonstrated:

```text
Mileia-like cleric identity stored in actor master
+ live session omits deity/domain
→ fresh runtime still recovers deity/domain from actor master
```

---

## Still not proven / intentionally deferred

This test does not claim that every future Drive permission/security case is solved. Remaining dedicated regressions include:

- real permission revocation during a write;
- real duplicate-manifest ambiguity handling;
- multi-session long-running campaign stress;
- Mystery clearance separation / HARD_EX boundaries;
- ruleset migration between pinned refs;
- multi-user multiplayer authority (currently unsupported).

These are separate from the now-passing core campaign-storage/fresh-load path.
