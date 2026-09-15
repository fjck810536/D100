# Session 1 — Andor Live State

> Current role-safe pointer. Earlier checkpoint/migration/live revisions remain history, not current-state replacements.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
scene: camera cut from Old City bard-academy departure to Mileia on the south-district chapel / dispensary route
world_time: Day 1 night; exact clock unset; split-thread chronology is approximate and must not be silently synchronized beyond established facts
four_voice_control: pl_pc
active_camera: Mileia
```

## Current party positions

- Elian: just outside / leaving `SITE-ANDOR-BARD-COLLEGE` after the first common-hall social pass. His thread is intentionally paused here.
- Nella: with Elian at the same departure point unless 蟬 later chooses otherwise. Her thread is intentionally paused here.
- Rook: off-camera at Mercenary Guild; pending convoy questions not auto-resolved.
- Aster: off-camera at Mercenary Guild; pending arcane-residue scheduling/registration not auto-resolved.
- Mileia: active camera now switches to her south-district chapel / dispensary route. No off-camera outcome has yet been auto-resolved for her.

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
  - mystery_vault/ANDOR_BARD_HALL_DEPARTURE_01.md
runtime_incident_refs:
  - OOC-AMBIG-ANDOR-001
```

## Stable prior state

- Nella's Oren tail succeeded and was reported; no hidden causal truth was promoted from the evidence.
- CP reserves remain: Elian 13, Rook 41, Aster 52, Mileia 15, Nella 23 unless explicitly spent later.
- Elian registered the one-day document/inventory verification job at the Mercenary Guild; `Elian, Three Silver Coins` was used as name/contact-lodging answer, without proving a paid room.
- Rook's convoy interest and Aster's arcane-residue interest remain pending, not accepted/resolved by off-camera time.
- Elian player-authored backstory additions remain committed: no prior bardic training; old home/family discouraged it; older brother remembered as more eloquent/charismatic; Elian values useful methods and delegation.

## Bard academy common-hall events — paused thread

1. Elian and Nella entered the public bard academy and used the ordinary common-hall/performance/bar space without formal registration.
2. Publicly visible site behavior established ordinary performances, drinks/light food, short/private instruction inquiries and post-performance patron/student networking.
3. Elian ordered drinks and observed an academy staff member discussing private instruction with a middle-aged visitor.
4. Before motive-reading, nearby observer identities/goals were minimally committed in `ANDOR_BARD_HALL_OBSERVERS_01.md`.
5. Elian attempted an audience-interest read:

```yaml
ROLL-ANDOR-BARD-001:
  interface: 察言觀色 / historical runtime value
  value: 54
  d100: 56
  result: fail by 2
  cp_reroll_spent: false
```

Failure produced no false motive. Visible behavior remained evidence only.

6. Elian changed method and examined what kinds of people the older patron watched after a performance ended:

```yaml
ROLL-ANDOR-BARD-002:
  interface: 搜索
  value: 56
  d100: 31
  result: success by 25
```

Player-visible conclusion: the older patron disproportionately watches post-performance relationship flow—who approaches whom, who exchanges names/cards, who appears to recruit/connect—rather than simply the best-dressed or loudest audience members. This is an observed pattern; motive remains unconfirmed.

7. Elian earlier sent a tasteful sweet drink to a young woman/regular near the performance area under both Elian and Nella's names; she accepted and acknowledged both. No romance/trust fact was created.
8. Elian then returned to Nella. After a coordinated wink/banter cue, 蟬 chose to have Nella cooperate with a louder social performance using Elian's wallet.
9. Elian's social act—playing an affluent, playful outsider willing to spend on selected social nodes—was resolved as:

```yaml
ROLL-ANDOR-BARD-003:
  interface: 唬騙
  value: 54
  d100: 23
  result: success by 31
```

10. Nella selectively sent drinks to the older patron and other visibly active post-performance connectors rather than randomly treating the whole room. The older patron visibly noticed the selection pattern and acknowledged Elian/Nella as coordinated participants in the same social field. This does not reveal hidden affiliation or create a conspiracy link.
11. Elian quietly told Nella she had only understood half, finished his drink, placed three literal silver coins on the table, announced departure and gave an undirected farewell.
12. `ANDOR_BARD_HALL_DEPARTURE_01.md` commits interpretation boundaries before resolving reactions:
   - three literal silver coins are not an established secret code;
   - the older patron knows `Three Silver Coins` as a public Andor establishment/contact point and can recognize a plausible double reading (tip vs deliberate reference) without certainty;
   - Nella can infer the gesture is intentionally layered, but exact intent remains hers to interpret unless Elian explains it;
   - no Low Whisper/Oren/blue-wax connection is created.
13. Elian visually acknowledged only people with whom eye contact naturally occurred; no extra forced contact was created.
14. Elian/Nella thread now pauses cleanly after they exit into the Old City night. The older patron does not chase them immediately.

## Evidence / knowledge boundary

```yaml
EVID-BARD-001: young woman/regular repeatedly noticed private-instruction/referral talk — OBSERVED
EVID-BARD-002: older patron watches performances plus post-performance social connections — OBSERVED
EVID-BARD-003: no coordinated purpose among background gazes established — OBSERVED
EVID-BARD-004: older patron noticed Elian/Nella's selective drink-sending pattern — OBSERVED
EVID-BARD-005: older patron may have noticed the three-silver-coins departure gesture; any deeper reading is not player-confirmed unless later evidence establishes it — OBSERVED/INFERRED boundary
```

Do not promote commitment-file motives into player knowledge.

## Money / item accounting note

- Elian explicitly leaves **3 silver coins** on the table at departure; those are spent/left behind unless later world events return them.
- Multiple drinks were purchased during this scene. Exact menu prices were not numerically committed in play, so do not invent a precise remaining gp total retroactively. Before a future purchase where exact funds matter, reconcile prices via ordinary site/economy state or GM ruling.
- No CP was spent in the bard hall.

## Low Whisper boundary

- Low Whisper College/tradition exists in source-backed D100 material.
- `SITE-ANDOR-WHISPERS-CONTACT` / 曲聞會館 is a separate public Old City site; any additional non-public relation is Mystery-gated.
- Bard academy != 曲聞會館. Do not silently merge them.
- No bard-hall observer is automatically Low Whisper affiliated.

## OOC / IC incident

`OOC-AMBIG-ANDOR-001` remains preserved. Elian later voluntarily disclosed his bardic/family background aloud, so Nella legitimately knows that later disclosure. The earlier ambiguous renderer line still cannot prove earlier IC knowledge/attraction/intimacy.

## Active resume boundary — Mileia

Resume with **Mileia on the south-district chapel / dispensary route**, at the first ordinary public point where she can see/reach the local religious/medical activity she set out to investigate.

At resume:

- 彌生 controls Mileia's important choices; DM may frame the public environment but must not decide her purpose beyond the already-established chapel/dispensary split.
- Do not retroactively claim she already spoke to clergy, patients, healers or officials.
- Do not auto-resolve Rook/Aster while the camera is on Mileia.
- Elian/Nella remain paused after bard-academy departure; no hidden follow-up occurs off-camera unless separately committed and later surfaced lawfully.
- Public ordinary environment can be described without a roll; meaningful uncertainty/consequence uses D100.
