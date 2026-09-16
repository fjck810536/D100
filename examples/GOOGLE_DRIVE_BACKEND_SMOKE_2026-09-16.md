# Google Drive Backend Smoke Test — 2026-09-16

> Test scope: live capability / stable-ID / move / read / update / readback only. No campaign data migrated.

## Environment observation

The active Google Drive connection behaved as OAuth / delegated rather than direct service-account mode for native document creation.

Observed:

```text
create native Google Doc with parent_folder_id
→ rejected with explicit provider error
```

Therefore the backend must support:

```text
create native document in default Drive parent
→ get exact file ID + current parent
→ move same file ID into selected campaign root
→ verify parent
```

This matches `storage_backends/GOOGLE_DRIVE.md` section "Move after create".

---

## Smoke sequence

Temporary root:

```text
D100_BACKEND_SMOKE_TEST_2026-09-16
```

Temporary manifest-like document:

```text
D100 manifest smoke 2026-09-16
```

Sequence executed:

```text
1. CREATE root folder
2. CREATE native Google Doc
3. GET metadata -> exact file ID + original parent
4. MOVE same file ID into smoke root
5. WRITE content marker v1
6. READ exact document ID -> v1 confirmed
7. LIST smoke root -> same exact document ID present
8. UPDATE same document ID v1 -> v2
9. READ exact document ID -> v2 confirmed
10. DELETE temporary document
11. DELETE temporary root folder
```

---

## Results

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

The update did not create a second manifest-like document. The exact same Drive document ID was edited in place.

This validates the core storage contract needed for a Google Drive campaign backend in the current connected environment.

---

## Important connector-specific cleanup note

For the current connector, the normal folder URL form:

```text
https://drive.google.com/drive/folders/<ID>
```

was not accepted by the generic delete action, while a generic Drive file-ID URL form using the same folder ID was accepted by the provider delete path.

This is a connector invocation detail, not a campaign schema rule. Runtime should prefer provider-native stable IDs and capability-tested delete semantics instead of assuming URL shapes are interchangeable.

---

## Not yet tested

This smoke test does **not** yet prove:

- full D100 campaign initialization with all child collections;
- Mileia-like full character finalization on Drive;
- multi-session reload across a completely fresh chat/agent;
- ambiguous-manifest handling with real duplicate files;
- write-permission revocation failure behavior;
- Mystery clearance separation / HARD_EX;
- ruleset migration.

Those remain covered by the planned regressions in `storage_backends/GOOGLE_DRIVE.md` and `examples/BOOTSTRAP_REGRESSION.md`.

---

## Cleanup

All temporary Drive objects created by this smoke test were deleted after verification. No existing user Drive files were modified.
