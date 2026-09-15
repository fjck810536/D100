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

Librarian checks source-backed Low Whisper identity/style and any directly relevant parent/lineage clues; relevant modules use that package to propose an actionable local teaching/contact path. If headquarters is still unresolved, it remains unresolved **without blocking the local node**.

### Fail

- “This is not confirmed HQ, therefore no useful next step.”
- fixed two-hop limit causes an obvious directly relevant parent relation to be ignored.
- Librarian returns source text but no downstream module uses it.

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

# Completion checklist

A run passes the grounded-generation architecture only if the answer to all five is yes:

```text
1. Did required source/cross-reference work actually occur or use a valid cache?
2. Did downstream modules actually consume the result?
3. Did creative gaps produce concrete proposals where play required them?
4. Did the proper owner decide/adopt key changes and leave provenance/state?
5. Did role-safe, relevant results actually reach the player/PC as information, options, or navigable world state?
```

“Nothing false was stated” is not sufficient if the system also failed to investigate, generate, decide, persist, or deliver.
