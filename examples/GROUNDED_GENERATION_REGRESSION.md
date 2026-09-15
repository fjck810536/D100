# Grounded Generation / Active Completion Regression Cases

> Purpose: verify that source checking, modularity, Mystery boundaries, PL+PC ownership and provenance **do not degrade into refusal, permanent blanks, or unused research**.
>
> Run with `examples/ADJUDICATION_TESTS.md` after architecture/model changes.

---

## Test G1 — Exact-name miss must not terminate Librarian work

### Situation

PC says `安道爾法術學院`. Exact repo search returns no exact phrase.

Elsewhere, the Red Wizard Association entry explicitly refers to `安道爾帝國魔法學院` and its eight seats.

### Pass

Librarian:

1. preserves the player's wording;
2. checks semantic index / related organization entries;
3. returns `安道爾帝國魔法學院` as a strong referent candidate with provenance;
4. reports the eight-seat relationship;
5. does **not** infer current seat holders from “can concurrently hold”.

### Fail

```text
exact string miss
→ SOURCE_GAP
→ institution treated as nonexistent / unusable
```

---

## Test G2 — Local node should trigger relevant parent-relation lookup

### Situation

Players find a local Low Whisper contact node and ask how to seek training / introduction.

### Pass

Librarian checks source-backed Low Whisper identity/style and relevant parent/lineage clues; relevant modules consume that package to develop the local path and relevant wider relationships. A missing source address becomes grounded placement work under `DM_PROTOCOL.md` 1.5. If the answer introduces a headquarters city, modules also connect that city to established geography and deliver the relevant knowable location without a second user prompt. A real lookup/access blocker remains specific; useful local work continues alongside it.

### Fail

- “This is not confirmed HQ, therefore no useful next step.”
- fixed two-hop limit causes an obvious directly relevant parent relation to be ignored.
- Librarian returns source text but no downstream module uses it.
- The local node works, so the runtime abandons a relevant parent-location task or leaves its own newly generated city floating outside known geography.

---

## Test G3 — SOURCE_GAP must split into lookup gap vs creative space

### Situation

Canon proves an institution exists but gives no Andor street address.

### Pass

Runtime distinguishes:

```text
unresolved_lookup = source paths still worth checking
creative_space = address/local access details not specified and not conflicting
```

If play needs a destination, relevant modules create a grounded location proposal; AO may adopt it; provenance remains `creative-addition`.

### Fail

- “No address in canon, so nobody can go there.”
- fabricated address is later described as Sheet canon.

---

## Test G4 — Generated adoption must preserve provenance after save/reload

### Situation

A local contact venue is generated, adopted and saved.

### Pass before save

```yaml
origin_kind: creative-addition
generated: true
status: committed
adoption_event_ref: ...
```

### Pass after reload

Same venue/site identity remains stable and retains generated provenance.

### Fail

- reload rerolls venue name/address without an in-world reason;
- reload turns generated claim into `D100_CANON`;
- reload forgets it exists and forces generation again.

---

## Test G5 — User correction is neither raw canon nor disposable chatter

### Situation

User/GM corrects: “三大議會在安道爾有三塔； source file omitted this.”

### Pass

Store as a committed `user-correction` claim with its own provenance. Related source-backed fact “三大議會存在” remains separately source-backed.

### Fail

- throw correction away because Sheet lacks it;
- rewrite correction as though Sheet explicitly contained it;
- mark the entire three-council bundle generated because one field is user-corrected.

---

## Test G6 — `NON_ASSERTION` must not become character-development prohibition

### Situation

There is insufficient evidence that PC B was already romantically attracted to PC A.

Later, B's Player Voice explicitly decides that B **now begins** to feel attraction or chooses to flirt.

### Pass

```text
prior attraction = not asserted
new Player Voice decision = valid present actor development
new PC declaration = allowed
relationship outcome = resolved normally
```

No retroactive claim that earlier ambiguity proved attraction.

### Fail

- “We previously said romance was unconfirmed, so B cannot become attracted now.”
- Analyst hypothesis is treated as sufficient to establish B's internal state without Player Voice.
- B's Player Voice decision automatically determines A's feelings.

---

## Test G7 — Real deferral requires a trigger

### Situation

A proposal is described as “not yet / too early.”

### Pass

Runtime classifies it as one of:

```text
NON_ASSERTION
DEFERRED
OWNER_DECISION
PROHIBITED
NOT_SELECTED
```

If `DEFERRED`, it records:

```text
owner
blocked_operation
trigger
reevaluate_with
```

### Fail

A vague “not yet” survives indefinitely without any trigger or rule/fact that could change it.

---

## Test G8 — Hidden affiliation must not make the public site unusable

### Situation

Backend knows a public venue has a hidden organizational affiliation; PC does not know that affiliation.

### Pass

The public venue still appears under its ordinary public label, remains navigable, and can provide ordinary services. Hidden affiliation is released only through legal actor knowledge/evidence/Mystery flow.

### Fail

- hide the entire location because one field is secret;
- reveal secret affiliation automatically because backend has it;
- create two inconsistent parallel sites for “public” and “secret” versions.

---

## Test G9 — Module boundary is a handoff, not a stop sign

### Situation

Politician is asked how a local academy branch gets authorization, but source package does not yet contain parent-organization relation.

### Pass

```text
Politician notices missing premise
→ requests Librarian lookup
→ Librarian returns relation / unresolved_lookup / creative_space
→ Politician updates institutional proposal
→ AO/owner can adopt or reject
```

### Fail

- Politician stops with “not my module.”
- Librarian's answer is produced but never fed back into the politician's proposal.

---

## Test G10 — Active information delivery without omniscience

### Situation

A PC legally knows that an organization has an ordinary public contact route and is currently trying to reach that organization.

### Pass

DM surfaces the relevant ordinary contact route without forcing the player to guess a secret keyword or ask each administrative sub-question.

Specific hidden identity/address/details remain gated by actor knowledge and evidence.

### Fail

- relevant ordinary known information remains hidden because “the player didn't ask exactly.”
- all hidden information is dumped just because the organization is relevant.

---

## Test G11 — Provenance repair must not rewrite roll history

### Situation

A past scene used a setting detail without proper Librarian trace. Later repair finds part source-backed, part user-corrected, part legacy-generated.

### Pass

```text
preserve compatible occurred events
→ repair provenance now
→ mark legacy-generated honestly
→ do not reroll old checks
→ do not claim the source lookup happened before the old roll if it did not
```

### Fail

- rewrite history so that the old source check “always happened”.
- delete compatible past scene solely because provenance was missing.
- reroll resources/checks absent an actual conflicting world fact.

---

## Test G12 — Same source repeated by modules is still one source

### Situation

Librarian, Politician and Analyst all cite the same Sheet line.

### Pass

Provenance remains one underlying source with multiple downstream uses.

### Fail

“Three modules agree” is presented as three independent pieces of evidence that upgrade source certainty.

---

## Test G13 — Stable site identity, layered map labels

### Situation

Backend site has:

```text
site_id = SITE-X
public label = ordinary venue name
private actor note = suspected organization tie
backend truth = hidden affiliation
```

### Pass

All views refer to one stable site ID; labels/knowledge differ by projection.

### Fail

- separate site objects are created for every knowledge state;
- revealing affiliation changes the physical site's identity/address without an in-world reason.

---

## Test G14 — New destination connects to existing world anchors

Test-only fixture: an academy answer introduces `TEST-TOWN` as its main teaching center. No country is assigned. The player asked about training, not the town's country. No access or state conflict blocks placement.

Pass: orchestrator detects the new location dependency; Librarian cross-reads country/geography and academy/culture sources; relevant modules compare grounded placements and return a selected proposal with an existing world anchor, useful regional placement/connection, provenance and role-safe delivery. Follow-up is automatic. A local teaching option can remain available too.

Fail: a town name alone; a second equally unanchored new region; an unused list of countries; requiring the player to ask "where is that?"; stopping at "not in source".

## Test G15 — Source replies change the proposal

Test-only source bundle: Country A has a court that supports performance and overseas cultural trade; Country B has major ports and several competing ruling families. A bard academy maintains a teaching center and discreet access to patrons. Neither country is a campaign fact.

Pass: the source bundle informs at least one concrete ecology/institution proposal, an inter-module question receives a sourced response, and the returned proposal visibly uses that response. Compare cultural support, access to power, logistics and added assumptions, then choose a placement. Either A or B may win with a coherent account; agreement alone is not evidence.

Perturbation: add a fixture fact that A excludes all permanent magical teaching institutions. The next run must address that fact and revise location or institutional form; unchanged reuse of the old selection with no accommodation fails. This tests responsiveness, not a hardcoded country answer.

## Test G16 — A name does not impose geography

Hold the test sources and functional description constant; rename `TEST-TOWN` to a name containing "bay", then to a name without it.

Pass: placement still follows the world/cultural evidence. A new bay/port may be creatively proposed and marked generated; name morphology is not reported as proof of a coastline, cardinal direction or real-world map position. Existing authored terrain or location remains authoritative.

## Test G17 — Anchor is not necessarily a nation or fixed building

Fixtures: an independent city in an established coastal region; a moving school within an established plane; a distributed tradition with several known contact centers.

Pass: complete the appropriate region/movement/contact relationships and a usable answer. Preserve each entity's form. Do not force national ownership, a single headquarters, or additional permission checks just to fill a template.

## Test G18 — Isolated selection has no campaign side effects

Run G14 with `execution_mode: isolated_dry_run`, a baseline ref, and `writeback: false`.

Pass: deliver a concrete `selected_proposal`, evidence and generated fields; claims remain `proposed`, `adoption_event_ref` is null. Campaign/session/character/Mystery contents, live pointers, public map, actor knowledge and runtime fact caches remain unchanged. A later normal resume uses the original baseline; searching test output never establishes that the selected town exists.

Fail: "no writeback" becomes refusal to choose; a dry-run recommendation gets an adoption event; test content leaks into a map, saved knowledge or restored world state.

## Test G19 — Location completion and disclosure are separate

Fixture: the backend has a located town and a hidden academy affiliation; the PC can reasonably know the town's ordinary country and public contact route.

Pass: backend location/affiliation work completes through legal views, and the frontend provides the useful knowable country/route. Specific protected affiliation stays with its existing disclosure conditions. Missing generator work is not performed as an NPC's ignorance.

## Test G20 — Adequate world connection permits completion

Fixture: a destination is connected to an established country, has a usable regional description/contact route, and the scene needs an introduction rather than a measured journey. Exact street coordinates and travel hours are not established.

Pass: deliver the rich usable answer and finish the present task. If a later action needs travel duration or a street entrance, resolve it then with the appropriate sources/modules. Neither fixed-hop truncation nor exhaustive atlas generation replaces completion of the actual dependencies.

---

# Completion checklist

A run passes the grounded-generation architecture only if each applicable completion check is satisfied:

```text
1. Did required source/cross-reference work actually occur or use a valid cache?
2. Did downstream modules actually consume the result?
3. Did creative gaps produce concrete proposals where play required them?
4. Did newly introduced entities acquire the necessary world relations, including an existing geographic anchor for a new destination?
5. Did the proper owner decide/adopt key changes and leave provenance/state in normal mode, or select a proposed result with zero authoritative writes in isolated_dry_run?
6. Did role-safe, relevant results actually reach the player/PC (or test requester) as usable information, options, or navigable descriptions?
```

“Nothing false was stated” is not sufficient if the system also failed to investigate, consume results, generate, connect, decide or deliver. Persistence is expected only in normal adopted execution; isolation must complete the reasoning task while preserving its baseline.
