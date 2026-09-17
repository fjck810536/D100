# Time Dragon combat pressure test

> `[TEST_FIXTURE]` This subtree is opt-in test data, not campaign authority and not a global D100 source layer.

Purpose: preserve the Time Dragon conversion / encounter pressure-test bundle together with the party snapshots used to exercise it.

## Layout

- `encounter/` — Time Dragon source notes, conversion lineage/model, worksheet, and encounter material.
- `party/` — Sather(a), Adele, and Kaland operational snapshots and CP calibration used by this test.
- `party/sheet_mirror/` — read-only text mirrors of the three Google Sheets used by the test.

## Fuse

Normal D100 bootstrap must not read this subtree. Values that look like `current`, `live`, HP/SP, buffs, missing actors, or party status are scoped to this test fixture only. They must never be resolved as the selected campaign current state.
