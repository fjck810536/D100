# Librarian Routing Incident — Resolution 2026-09-16

> Resolves the architecture problem documented in `librarian_routing_incident_2026-09-15.md`.
>
> The original incident transcript remains preserved as historical evidence. Some intermediate findings in that transcript are now superseded by deeper source resolution.

## Resolution status

```yaml
incident: librarian_routing_incident_2026-09-15
status: RESOLVED_IN_ARCHITECTURE
resolved_at: 2026-09-16
implemented_in:
  - AGENTS.md
  - DATA_ARCHITECTURE.md
  - DM_CABINET.md
  - DM_PROTOCOL.md
  - RUNTIME_SOCIAL_WORLD_CONTRACT.md
  - START_DM.md
  - templates/SITE_RECORD_TEMPLATE.md
  - templates/WORLD_COMMITMENT_TEMPLATE.md
  - templates/SESSION_STATE_TEMPLATE.md
  - examples/GROUNDED_GENERATION_REGRESSION.md
```

## Root cause confirmed

The incident was not simply “Librarian did not appear.” The architecture had:

```text
Librarian duty defined
+ source database available
- no reliable trigger before actor/player lore claims were used as objective world facts
- no active-completion contract forcing downstream use of retrieved data
- no grounded-generation path for source gaps
```

A second failure was also confirmed:

```text
exact repo/code-search miss
≠ complete source-resolution miss
```

The runtime must use semantic navigation (`sources/SHEET_INDEX.md`), relevant raw tabs, cross-references, current state and user corrections.

## Corrected source findings

### Low Whisper College

`低語學院` is source-backed D100 material in the bard-college source. Player wording such as `低語學派` may be treated as a referent/alias candidate when context supports it, while preserving the original wording in dialogue history.

### Three Councils

`三大議會` is source-backed D100 world history/institution material.

The fact that Andor has **three council towers** is recorded separately as a user correction, not laundered into raw Sheet provenance.

### Andor Imperial Magic Academy

The earlier incident transcript said the exact institution name had not been found. That intermediate conclusion is **superseded**.

Deeper cross-reference resolution found `安道爾帝國魔法學院` in the `賽爾紅袍協會` entry of `sources/sheet_mirror/01_world_core.json.md`:

```text
紅袍八位首席
can concurrently hold
安道爾帝國魔法學院的八位席位
```

Correct inference:

```text
institution exists
+ eight seats exist
+ concurrent office-holding is possible
```

Not justified:

```text
all current eight seats are Red Wizard chiefs
```

### John Academy

The world timeline source contains John Academy's foundation date. The GM/user correction that John founded it in Andor is retained separately as `user-correction` provenance.

## Adopted routing flow

```text
1. classify utterance layer
   DM / OOC-PL / Player decision / PC dialogue / PC thought / action / narrator

2. extract entities / world claims actually needed by the current task

3. if the system is about to use a claim objectively
   → Librarian source resolution

4. Librarian returns a usable package
   source facts
   user corrections
   state refs
   alias/referent candidates
   cross-references
   conflicts
   searched scope
   unresolved_lookup
   creative_space

5. Mystery produces role-safe views where needed

6. relevant modules consume the package
   and may request further source/module prerequisites

7. creative_space receives grounded proposals
   SOURCE_GAP is not a prohibition

8. proper owner decides
   PL for key PC choices
   AO/world flow for NPC/world developments

9. adopted claim is written to authoritative state
   with origin / fit / owner / decision / effective-time provenance

10. role-safe relevant results are actively delivered to the player/PC

11. completion check verifies
   searched → used → decided → persisted → delivered
```

## Important semantic distinctions now adopted

```text
actor said X ≠ world is X
SOURCE_GAP ≠ PROHIBITED
generated and adopted ≠ source text
NON_ASSERTION ≠ no future development allowed
DEFERRED requires a trigger
NOT_SELECTED ≠ NEVER
module boundary = handoff, not stop sign
```

## Andor migration applied

Current adopted site/provenance repair lives in:

- `campaign/andor_sites.md`
- `mystery_vault/ANDOR_WHISPERS_CONTACT.md`
- `sessions/2026-09-16_session-1_live-state.md`

The repair preserves compatible play history, does not reroll prior checks, and does not pretend the later source audit happened before earlier rolls.

## Regression requirement

Run:

```text
examples/GROUNDED_GENERATION_REGRESSION.md
```

especially after changing model, source routing, Cabinet boundaries, Mystery handling, Player Layer logic, or world-generation policy.

The incident is considered reopened if any of these recur:

```text
exact-name miss ends source search despite obvious semantic/cross-reference routes
source gap is treated as permanent inability to build a usable world detail
generated claims lose provenance after save/reload
retrieved source data is not consumed by downstream modules
role-safe useful results never reach the front end
“not yet” blocks legal development without a trigger
```
