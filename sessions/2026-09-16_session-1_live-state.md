# Session 1 — Andor Live State

> Current role-safe pointer. Earlier checkpoint and migration files remain history, not current-state replacements.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
scene: public bard academy common hall / bar, Elian observing audience interest patterns; Nella remains near performance area
world_time: Day 1 after evening; exact clock unset
four_voice_control: pl_pc
```

## Current party positions

- Elian: inside `SITE-ANDOR-BARD-COLLEGE`, at the common-hall bar with two beers; currently watching several patrons who reacted to a private-instruction conversation.
- Nella: inside the same public hall, seated nearer the performance area; Elian earlier asked her to watch the show and notice anything worthwhile.
- Rook: remained at the Mercenary Guild when Elian/Nella departed; later intentions not auto-resolved.
- Aster: remained at the Mercenary Guild when Elian/Nella departed; later intentions not auto-resolved.
- Mileia: split earlier toward the south-district chapel / dispensary; has not silently rejoined.

## Current refs

```yaml
prior_state_refs:
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - sessions/2026-09-15_session-1_runtime-migration.md
site_state_refs:
  - campaign/andor_sites.md
  - campaign/andor_map_adoption.md
public_map_ref:
  - campaign/andor_public_map.md
commitment_refs:
  - mystery_vault/ANDOR_SESSION1_MIGRATION.md
  - mystery_vault/ANDOR_WHISPERS_CONTACT.md
  - mystery_vault/ANDOR_BARD_HALL_OBSERVERS_01.md
runtime_incident_refs:
  - OOC-AMBIG-ANDOR-001
```

## Established earlier state

- Nella's tail of Oren resolved successfully; she observed his message/office route, returned, and returned Elian's cloak unused.
- Checkpoint 01 CP reserves remain: Elian 13, Rook 41, Aster 52, Mileia 15, Nella 23.
- Elian registered the one-day document/inventory verification job at the Mercenary Guild. `Elian, Three Silver Coins` was given as name/contact-lodging answer; this does not itself prove a room booking or payment.
- Rook had interest in the two-day convoy job but had not accepted it.
- Aster had interest in the arcane-residue identification job but had not accepted it.
- The 18 gp overnight escort remained open at last established Guild state.

## Events after leaving the Guild

1. Elian asked for the bard/poet academy and chose to visit the Old City evening scene.
2. PL+PC split at departure:
   - 鮫島 / Rook stayed at the Guild and intended to ask more about the normal convoy job before deciding.
   - 赫茲 / Aster stayed at the Guild and intended to ask whether the arcane-residue job could be done tomorrow, possibly register if compatible, then later seek Mileia/church.
   - 蟬 / Nella chose to accompany Elian.
3. On the walk Elian talked about people hiding in corners versus behind attractive clothes, masks, songs and dance; he openly said he wanted inspiration and would welcome encountering people of the Low Whisper tradition.
4. Elian's private/player-authorized intention also includes useful information exchange and, if possible, learning bardic techniques. Nella does not automatically know this private portion.
5. Elian later voluntarily told Nella aloud that:
   - he had not previously learned bardic arts;
   - his old home/family environment did not allow/encourage it;
   - he had instead been expected to shoulder intellectual/administrative work around his older brother;
   - in Elian's memory his older brother was the genuinely eloquent, charismatic one;
   - Elian's present attitude is pragmatic: if a method is usable/useful he will try it; if he cannot do it himself, he will use people who can.
6. Elian and Nella entered the public bard academy without going directly to the reception desk. Elian chose the most natural public waiting/social area rather than announcing a formal purpose.
7. The public common hall visibly supports ordinary visitors, students, performers and patrons: seating, public performances, posted lessons, private instruction inquiries, drinks and light food. This is ordinary site state, not a hidden clue network.
8. Elian offered to get drinks, asked Nella what she wanted, and went to the bar. Nella remained near the performance area rather than following him.
9. Elian ordered two beers, drank from his own, and noticed an academy staff member discussing private instruction with a middle-aged visitor. Publicly audible fragments established that short-term/private instruction can exist outside formal enrollment, subject to what the student wants and whether a teacher accepts.
10. Elian also noticed that some nearby patrons briefly reacted to that discussion. No coordinated surveillance pattern was established from passive observation alone.
11. Before Elian's active attempt to interpret those patrons, minimum hidden actor commitments were written in `ANDOR_BARD_HALL_OBSERVERS_01.md`; the roll cannot retroactively decide who they are or what they wanted.

## Elian background / actor-state additions

```yaml
origin_kind: player-decision / player-authored-backstory
status: committed
claims:
  - no prior bardic training
  - family/old-home environment discouraged or prevented bardic study
  - family expected Elian to carry intellectual/administrative work around his older brother
  - Elian remembers his older brother as more naturally eloquent/charismatic
  - Elian currently values useful methods over identity purity and is willing to delegate to capable people
```

Exact family title, inheritance order, brother's present status and the exact family reason for opposing bardic study remain uncommitted.

## Current roll ledger

### ROLL-ANDOR-BARD-001 — audience-interest read

```yaml
actor: Elian
intent: keep attention on patrons who reacted to the private-instruction conversation and infer what kinds of things interest them
interface: 察言觀色 / Sense Motive historical runtime value
value: 54
provenance: RUNTIME_PROVISIONAL (formal source/interface remains open)
d100: 56
margin: -2
result: ordinary failure by 2
cp_reroll_declared: false
```

Result boundary:

- failure does not create false motives;
- Elian may retain directly visible behavior patterns;
- he does not yet get a confident read of underlying motives from this roll;
- a legal CP reroll remains a player choice if the player elects to spend 1 CP under the standing reroll rule.

## Player-visible observations relevant to ROLL-ANDOR-BARD-001

```yaml
EVID-BARD-001:
  status: OBSERVED
  proposition: the young woman near the performance area has looked toward private-instruction/referral talk more than once

EVID-BARD-002:
  status: OBSERVED
  proposition: the older patron at the far side of the bar has paid attention both to performances and to people involved in private arrangements

EVID-BARD-003:
  status: OBSERVED
  proposition: other glances in the room still include ordinary room-scanning/noise; Elian has not established a shared coordinated purpose among observers
```

Do not promote hidden motives from the commitment file into Elian's knowledge unless later evidence/rolls establish them.

## OOC / IC ambiguity preserved

`OOC-AMBIG-ANDOR-001` remains a renderer/runtime incident concerning the earlier generated question about whether Elian had studied bardic arts. Elian later answered the topic aloud voluntarily, so Nella legitimately knows the newly spoken answer from that later point. The old ambiguous utterance still cannot be used as proof of earlier Nella IC knowledge, attraction, intimacy or relationship state.

## Low Whisper / site knowledge boundary

- Low Whisper College/tradition exists in source-backed D100 material and commonly conceals affiliation.
- `SITE-ANDOR-WHISPERS-CONTACT` / 曲聞會館 exists as a separate public Old City venue with ordinary services; any additional non-public relation is Mystery-gated.
- The public bard academy and 曲聞會館 are separate stable sites; do not silently merge them.
- Elian currently knows/has spoken about the Low Whisper concept/tradition, but backend knowledge does not automatically reveal local hidden affiliations to him or Nella.

## Resume boundary

Resume at the bard-academy bar immediately after resolving `ROLL-ANDOR-BARD-001` (54 vs d100 56, fail by 2), before Elian chooses whether to spend CP, approach anyone, continue passive observation, return to Nella, or do something else.

At resume:

- Elian controls his own next action and CP spending.
- 蟬 controls Nella's important PL+PC choices.
- Public ordinary environment can be described without a roll.
- Specific hidden motives/affiliations stay behind committed actor/Mystery state until legitimately observed or inferred.
- Rook/Aster/Mileia remain off-camera without auto-resolution of their pending plans.
