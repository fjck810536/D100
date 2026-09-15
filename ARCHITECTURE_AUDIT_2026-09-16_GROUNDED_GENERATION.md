# Architecture Audit — Grounded Generation / Active Completion — 2026-09-16

> Scope: implementation and acceptance audit for the Work-6 Astra method: source resolution → cross-module use → grounded generation → owner adoption → state writeback → role-safe delivery → regression checks.

## Executive result

```yaml
status: PASS_WITH_NO_BLOCKING_FINDINGS
runtime_architecture_adopted: true
andor_state_migrated: true
public_navigation_stabilized: true
source_provenance_preserved_after_reload: true
prior_rolls_rerun: false
checkpoint_rollback: false
```

One transient tooling issue occurred while writing an overlong live-state payload; the blocked calls created no files. The final compact live-state and later map-reference update both succeeded. No world-state workaround is required.

---

## 1. Source resolution audit

### Sheet navigation

Verified `sources/SHEET_INDEX.md` maps all 31/31 source tabs and explicitly requires mirror search before declaring open/default/bridge gaps.

### Low Whisper College

Verified in `sources/sheet_mirror/09_吟遊詩人特殊專長.json.md`:

- the college-selection rule includes 迷惑學院 / 劍歌學院 / 低語學院;
- study must fit story progression or character background;
- Low Whisper members present like ordinary bards, use information/secrets for leverage, conceal true affiliation, and infiltrate power centers.

Result: source-backed identity/style; local Andor contact venue remains generated campaign state.

### Three Councils

Verified in `sources/sheet_mirror/01_world_core.json.md` world/timeline material:

- 魔導學院、鍊金議會、萬神殿 established in year 500;
- Three Councils issue world currency in year 700;
- multiple later interventions/closures/reopenings are present.

Result: institution/history source-backed. Three Andor towers remain a user correction, not raw-source text.

### Andor Imperial Magic Academy

Verified through the Red Wizard Association cross-reference:

```text
紅袍首席可以與安道爾帝國魔法學院的八位席位相互兼任
```

Result:

```text
institution exists = supported
eight seats exist = supported
concurrent office-holding possible = supported
current eight seat holders all Red Wizards = NOT supported
```

This supersedes the earlier incident transcript's intermediate “exact institution not found” conclusion.

### John Academy

Verified timeline entry:

```text
4520年 — 約翰學院成立
```

Result: founding year source-backed; John-in-Andor founder/location relation remains recorded as user correction.

---

## 2. Architecture implementation audit

Updated:

```text
AGENTS.md
DATA_ARCHITECTURE.md
DM_CABINET.md
DM_PROTOCOL.md
RUNTIME_SOCIAL_WORLD_CONTRACT.md
START_DM.md
sessions/README.md
templates/SITE_RECORD_TEMPLATE.md
templates/WORLD_COMMITMENT_TEMPLATE.md
templates/SESSION_STATE_TEMPLATE.md
99_open_questions/README.md
```

New runtime/state artifacts:

```text
campaign/andor_sites.md
campaign/andor_public_map.md
mystery_vault/ANDOR_WHISPERS_CONTACT.md
sessions/2026-09-16_session-1_live-state.md
99_open_questions/librarian_routing_resolution_2026-09-16.md
examples/GROUNDED_GENERATION_REGRESSION.md
```

### Adopted core flow

```text
input-layer classification
→ entity/claim resolution
→ Librarian semantic/cross-reference source package
→ unresolved_lookup vs creative_space split
→ relevant modules actively consume package
→ grounded proposal
→ correct owner decision (PL / AO)
→ early causal commitment where needed
→ role-safe active delivery
→ D100 adjudication
→ authoritative writeback + provenance
→ cache invalidation
→ completion check
```

### Claim dimensions now separated

```text
provenance
fit
status
owner
visibility
recorded_at
effective_from
decision event
```

Adopted generated facts retain `creative-addition` / `legacy-generated` origin after becoming authoritative world state.

---

## 3. Andor migration audit

### Stable sites

```text
SITE-ANDOR-COUNCIL-TOWERS
SITE-ANDOR-IMPERIAL-MAGIC
SITE-ANDOR-JOHN-ACADEMY
SITE-ANDOR-BARD-COLLEGE
SITE-ANDOR-WHISPERS-CONTACT
```

### Public navigation projection

`campaign/andor_public_map.md` provides stable public navigation:

```text
Three Councils      → CENTRAL / 中央環道 → 三塔廣場
Imperial Magic      → ACADEMIC / 學院大街東段 → 星儀廣場北側
John Academy        → ACADEMIC / 學院大街西段 → 墨井廣場南側
Bard Academy        → OLD CITY / 劇場街西段 → 七弦巷口
曲聞會館             → OLD CITY / 劇場街中段 → 鳴鐘拱廊東口
```

Map labels are projections of stable site IDs, not parallel world objects.

### Low Whisper local node

A public venue / private-introduction node was committed before first party interaction with that venue. Its local site/geography/services are generated campaign content; Low Whisper identity/style is source-backed; affiliation visibility remains separately controlled.

Exact Low Whisper headquarters is still unresolved. The architecture now treats that as `NON_ASSERTION / unresolved_lookup`, not as a blocker on the local contact path.

### Live-state preservation

`sessions/2026-09-16_session-1_live-state.md` now resumes from:

```text
Mercenary Guild
after Elian registered the document/inventory verification job
```

It preserves:

- Nella's already-resolved Oren tail;
- checkpoint CP awards;
- Mileia's split location;
- Rook/Aster job interest without auto-acceptance;
- night escort still open at last established state;
- no invented post-registration roll.

No rollback to the Grey Antler migration boundary occurred.

---

## 4. Provenance reload audit

After writing the Andor site/map records, they were fetched again from `main`.

Observed persistence:

```text
source-extraction remains source-extraction
user-correction remains user-correction
legacy-generated remains legacy-generated
creative-addition remains creative-addition
stable site IDs remain unchanged
public map labels remain mapped to same site IDs
```

Result: PASS.

This directly covers the “save/reload must not wash generated content into canon” requirement.

---

## 5. Grounded-generation regression run

Using `examples/GROUNDED_GENERATION_REGRESSION.md`:

| Test | Result | Evidence |
|---|---|---|
| G1 exact-name miss does not terminate lookup | PASS | Imperial Magic Academy found via Red Wizard cross-reference |
| G2 local node can coexist with unresolved HQ | PASS | 曲聞會館 committed; HQ not asserted |
| G3 SOURCE_GAP splits lookup vs creative space | PASS | exact map placements generated/adopted after source resolution |
| G4 generated provenance survives reload | PASS | re-fetch of `campaign/andor_sites.md` / public map retains origin kinds |
| G5 user correction stays distinct | PASS | council towers / John-in-Andor recorded separately from source claims |
| G6 NON_ASSERTION does not prohibit new PC development | PASS | social contract explicitly allows new Player Voice development without retroactive proof |
| G7 real deferral requires trigger | PASS | five typed states adopted; DEFERRED requires trigger + reevaluate_with |
| G8 hidden affiliation does not erase public site | PASS | single site ID + public 曲聞會館 projection + separate role-safe affiliation state |
| G9 module boundary is handoff | PASS | Cabinet contract requires prerequisite requests and downstream reuse |
| G10 active information delivery | PASS | DM protocol step 11 requires relevant legal knowledge/actionable route delivery |
| G11 provenance repair does not rewrite rolls | PASS | repair event explicitly preserves rolls/resources and records later repair honestly |
| G12 repeated module use does not multiply source provenance | PASS | one source package / claim source refs remain provenance; module outputs remain views |
| G13 stable site identity with layered labels | PASS | `andor_sites.md` + `andor_public_map.md` share stable site IDs |

---

## 6. Non-regression conclusions

The specific degradation patterns that triggered the redesign are now explicitly invalid runtime behavior:

```text
exact-search miss → “does not exist”
source gap → permanent blank
source checking → no downstream use
module boundary → stop work
minimum commitment → minimum world generation
unconfirmed past feeling → future character-development ban
“not yet” without trigger → indefinite freeze
generated adopted fact → silently becomes source canon
secret affiliation → public location becomes unreachable
old checkpoint → overwrites later live state
```

The new completion criterion is positive, not merely prohibitive:

```text
searched
→ used
→ generated where needed
→ decided by proper owner
→ persisted with provenance
→ delivered role-safely
```

---

## 7. Remaining legitimate open questions

This repair deliberately does not pretend to solve unrelated runtime gaps. Still open include, among others:

- Sense Motive formal source/interface;
- special magic-item activation/duration/transfer rules;
- improvised-signal general interface;
- checkpoint CP scale;
- exact-clock promotion rule;
- OOC/IC renderer classification design (incident remains recorded; no forced retroactive classification);
- ordinary economy calibration;
- exact combat tie handling and other rule gaps already in existing registries.

These do not block the grounded-generation architecture or current Andor resume state.

---

## Final acceptance

```text
Work-6 Astra method implementation: COMPLETE
Andor source-resolution migration: COMPLETE
Grounded world landing: COMPLETE
PL/PC non-regression protection: COMPLETE
Provenance persistence: VERIFIED
Regression suite: PASS
Current session resume point: Mercenary Guild after Elian registration
```
