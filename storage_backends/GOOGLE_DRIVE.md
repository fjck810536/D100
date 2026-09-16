# Google Drive Campaign Storage Backend

> Status: backend design v0. This file maps the generic contract in `CAMPAIGN_STORAGE_PROTOCOL.md` onto Google Drive semantics. It does not change D100 rule authority.

## 0. Backend identity

```yaml
storage:
  backend: google_drive
  root_ref: <campaign-root-folder-id-or-url>
  schema_version: 1
  write_scope: self_only
```

`root_ref` must resolve to one campaign root folder. Do not use a broad parent folder containing many campaigns as the selected campaign root.

---

## 1. Required capabilities

A runtime may declare the Google Drive backend writable only after verifying these operations against the selected root:

```text
LOCATE  get metadata for root folder
LIST    list root / child folder contents
READ    read manifest and state record text
CREATE  create folder / record
UPDATE  update an existing record while preserving its stable Drive file ID
```

Useful optional capabilities:

```text
MOVE
VERSION_HISTORY
DELETE
```

If any required capability is unavailable, persistent runtime must not pretend the campaign is writable.

---

## 2. Physical layout

Recommended Drive layout:

```text
D100 - <campaign-name>/                  # root folder; root_ref points here
├── manifest                             # canonical manifest record
├── current_state                        # canonical current-state record
├── characters/                          # folder
├── sessions/                            # folder
├── sites/                               # folder
├── relationships/                       # folder
├── commitments/                         # folder
└── mystery/                             # folder / protected records
```

Native Google Docs are acceptable for text-heavy records. Stored Markdown/text files are also acceptable if the active environment can reliably create, read and replace them in place.

Do not mix providers inside one campaign unless a future manifest schema explicitly supports composite storage.

---

## 3. Stable IDs, not titles

Google Drive titles are human-facing labels, not authoritative locators.

After creation, record the Drive IDs / stable URLs in the manifest:

```yaml
storage:
  backend: google_drive
  root_ref: <root-folder-id>
  provider_metadata:
    root_name: "D100 - Example Campaign"

records:
  manifest_ref: <manifest-file-id>
  current_state_ref: <current-state-file-id>
  characters_root_ref: <characters-folder-id>
  sessions_root_ref: <sessions-folder-id>
  sites_root_ref: <sites-folder-id>
  relationships_root_ref: <relationships-folder-id>
  commitments_root_ref: <commitments-folder-id>
  mystery_root_ref: <mystery-folder-id>
```

Character / session collection members should likewise keep stable IDs in the relevant index/current-state refs when they become important runtime records.

Forbidden recovery shortcut:

```text
search Drive globally for "Mileia"
→ take first hit
→ treat as current character master
```

Correct pattern:

```text
selected root_ref
→ manifest_ref
→ characters_root_ref / explicit character ref
→ read exact record
```

---

## 4. Bootstrap creation order

Avoid the manifest chicken-and-egg problem by using the root folder as the first stable locator.

Recommended creation sequence:

```text
1. Create / select campaign root folder.
2. Capture root folder ID as storage.root_ref.
3. Create child collection folders.
4. Create current_state record.
5. Create manifest record with all observed IDs.
6. Re-read manifest by exact ID.
7. Run capability verification.
8. Mark bootstrap_status.initialized=true only after readback succeeds.
```

During step 5 the manifest can record its own ID only after the provider returns it. Therefore the implementation may:

```text
create manifest skeleton
→ receive manifest file ID
→ update manifest once with records.manifest_ref
→ read back and verify
```

This one-time self-reference update is expected and is not a duplicate manifest.

---

## 5. Read sequence

Load Game with a Drive root should resolve in this order:

```text
root_ref
→ list root / locate canonical manifest
→ read manifest
→ verify campaign_id + ruleset.ref + backend
→ follow exact record IDs
→ current_state
→ character masters
→ latest live session pointer
→ referenced site / relationship / commitment / Mystery-safe records
```

Once `records.manifest_ref` is known, later runs should prefer the exact manifest ID over title matching.

If more than one candidate `manifest` exists in the root and no exact manifest ID is available, stop and report storage ambiguity instead of choosing by modified time.

---

## 6. Safe update semantics

### Existing native Google Doc

Use an in-place content update against the same document ID. Do not create a replacement document on every save.

### Stored raw text / Markdown

Use an in-place file-content replacement preserving the same Drive file ID when the backend supports it.

### Move after create

Some Drive connection modes may create a native Google Doc in My Drive root before it can be moved into the selected campaign folder. If so:

```text
create record
→ read metadata / current parent
→ move same file ID into selected campaign folder
→ verify parent
→ save ID in manifest
```

Do not work around this by leaving state records scattered in My Drive and relying on global search.

---

## 7. Write verification

A state mutation is not considered persisted merely because an update action was attempted.

After important writes, verify at least:

```text
same record ID still exists
record is under expected campaign root / collection
content or revision reflects the intended update
```

For session-end / character-finalization boundaries, readback is mandatory.

Failure state:

```yaml
persistence:
  status: uncommitted
  failed_record_ref: <id>
  failure_reason: <reason>
```

Do not silently continue as though save succeeded.

---

## 8. Revision history

Google Drive revision history can be used for:

- accidental overwrite recovery;
- migration audit;
- provenance investigation;
- comparing current and immediately previous save states.

It is **recovery evidence**, not a second current-state authority.

Do not choose an older revision as current merely because it contains more fields.

---

## 9. Mystery boundary

Putting a record under `mystery/` does not itself create information security.

`MYSTERY_PROTOCOL.md` still controls:

```text
classification
clearance
need-to-know
role-safe projection
EX handling
```

If the active model/context can read the full Drive document, storage location alone cannot make that payload HARD_EX. The backend must report the real protection boundary.

---

## 10. Capability notes for current ChatGPT-style Drive environments

A compatible Drive connector may expose operations equivalent to:

```text
create folder
list folder
get file/folder metadata
create native document
move/rename Drive file
read document text
edit native document in place
read revision history
```

That is sufficient in principle for the required campaign backend contract.

However connector availability is environment/account dependent. `BOOTSTRAP_PROTOCOL.md` therefore requires live capability checking instead of assuming Google Drive always exists.

---

## 11. Regression cases

The Google Drive backend is not ready for production until these pass:

### GDRIVE-01 Character persistence

```text
create campaign
→ finalize cleric with deity/domain
→ write character master
→ start session
→ end runtime
→ load campaign from root_ref
→ deity/domain remain available without session reconstruction
```

### GDRIVE-02 Stable update

```text
update current_state 3 times
→ exactly one current_state master record ID remains authoritative
→ no current_state (1) / (2) duplicate chain
```

### GDRIVE-03 Campaign isolation

```text
Campaign A: Mileia
Campaign B: different Mileia or no Mileia
→ load A then B
→ no actor/session/site state crosses roots
```

### GDRIVE-04 Ambiguous manifest

```text
root contains two manifest candidates
+ no exact manifest_ref
→ runtime stops with ambiguity
→ runtime does not choose newest automatically
```

### GDRIVE-05 Failed write

```text
update permission removed
→ write fails
→ runtime reports uncommitted
→ does not claim save success
```
