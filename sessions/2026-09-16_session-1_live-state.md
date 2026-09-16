# Session 1 — Andor Live State

> Current role-safe pointer. Earlier checkpoint/migration/live revisions remain history, not current-state replacements.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
scene: DM rollback pause; Mileia restored to the immediate post-split point while other threads retain their current state
world_time: split-thread chronology; Mileia pointer restored to her immediate post-guild-split moment; other threads retain their established local positions
four_voice_control: pl_pc
active_camera: none
```

## Current party positions

- Elian: just outside / leaving `SITE-ANDOR-BARD-COLLEGE` after the first common-hall social pass. His thread is intentionally paused here.
- Nella: with Elian at the same departure point unless 蟬 later chooses otherwise. Her thread is intentionally paused here.
- Rook: off-camera at Mercenary Guild; pending convoy questions not auto-resolved.
- Aster: off-camera at Mercenary Guild; pending arcane-residue scheduling/registration not auto-resolved.
- Mileia: **rewound by DM directive to the immediate post-split boundary after the Mercenary Guild scene.** She has just separated from the others. No post-split destination arrival, local observation, NPC contact, volunteering, or local religious/medical-system knowledge is established.

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
  - MILEIA-LINE-ROLLBACK-2026-09-16
```

## Stable prior state

- Nella's Oren tail succeeded and was reported; no hidden causal truth was promoted from the evidence.
- CP reserves remain: Elian 13, Rook 41, Aster 52, Mileia 15, Nella 23 unless explicitly spent later.
- Elian registered the one-day document/inventory verification job at the Mercenary Guild; `Elian, Three Silver Coins` was used as name/contact-lodging answer, without proving a paid room.
- Rook's convoy interest and Aster's arcane-residue interest remain pending, not accepted/resolved by off-camera time.
- Elian player-authored backstory additions remain committed: no prior bardic training; old home/family discouraged it; older brother remembered as more eloquent/charismatic; Elian values useful methods and delegation.
- Mileia's recovered authoritative character facts remain valid: she is a Life Domain cleric/healer who worships **Lathander / 晨曦之主**, with alignment NG. These facts predate the voided Mileia scene and are not part of the rollback.

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

## DM rollback — Mileia thread

DM directive `MILEIA-LINE-ROLLBACK-2026-09-16`:

- Mileia's personal timeline is rewound to **the immediate moment after the party split at the Mercenary Guild**.
- All Mileia post-split narration generated after the erroneous camera cut is **VOID / NON-CANON**.
- The voided material creates **no** world facts, NPCs, site facts, local customs, Mileia epistemic state, relationship edges, evidence, commitments, obligations, or resource changes.
- In particular, any generated chapel/dispensary pairing, the NPC `Teren`, cloth-carrying/volunteering, patients/visitors, local care-routing practices, and the idea that Mileia learned a local principle about "handoff" or night staffing are void and may not be reused as premises.
- `campaign/andor_south_care_node.md` has been removed from the authoritative branch.
- Historical Git commits/chat text may still contain the voided material for audit/history, but they are **not authoritative state and must never be promoted back into play** unless the DM later independently re-establishes a fact.
- Mileia's recovered character-creation facts in `characters/mileia.md`—including Lathander / 晨曦之主, Life Domain, cleric/healer identity, alignment and established stats/resources—remain valid because they predate the erroneous scene.

## Resume boundary — Mileia reset

If/when the camera returns to Mileia, resume at **the immediate moment after she split from the party following the Mercenary Guild scene**, before she has reached or evaluated any church, chapel, temple, dispensary, healer, clergy member, or related site.

At resume:

- 彌生 controls Mileia's next destination/action.
- Before generating or resolving faith-related environment, load `characters/mileia.md` and use her established Lathander / Life Domain identity as an actual premise; source-resolve additional setting claims as needed.
- No voided post-split Mileia scene detail may be reused, echoed as memory, or treated as previously observed common knowledge.
- Rook and Aster remain at their pending Mercenary Guild boundaries; no off-camera resolution is added.
- Elian/Nella remain paused after bard-academy departure; no hidden follow-up occurs off-camera unless separately committed and later surfaced lawfully.
