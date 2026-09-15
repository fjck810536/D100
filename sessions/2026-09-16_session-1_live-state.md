# Session 1 — Andor Live State

> Current role-safe pointer. Earlier checkpoint and migration files remain history, not current-state replacements.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
scene: Old City / Theatre Street, Elian and Nella approaching the public bard academy before first entry
world_time: Day 1 after evening; later than the Mercenary Guild scene by an ordinary walk; exact clock unset
four_voice_control: pl_pc
```

## Current party positions

- Elian: Old City / Theatre Street, with Nella, approaching `SITE-ANDOR-BARD-COLLEGE`; has not entered yet.
- Nella: with Elian at the same location.
- Rook: remained at the Mercenary Guild when Elian/Nella departed.
- Aster: remained at the Mercenary Guild when Elian/Nella departed.
- Mileia: split earlier toward the south-district chapel / dispensary; has not silently rejoined.

## Current refs

```yaml
prior_state_refs:
  - sessions/2026-09-15_session-1_checkpoint-01.md
  - sessions/2026-09-15_session-1_runtime-migration.md
site_state_ref:
  - campaign/andor_sites.md
public_map_ref:
  - campaign/andor_public_map.md
  - campaign/andor_map_adoption.md
commitment_refs:
  - mystery_vault/ANDOR_SESSION1_MIGRATION.md
  - mystery_vault/ANDOR_WHISPERS_CONTACT.md
runtime_incident_refs:
  - OOC-AMBIG-ANDOR-001
```

## Established state before leaving the Guild

- Nella's tail of Oren resolved successfully; she observed his message/office route, returned, and returned Elian's cloak unused.
- Checkpoint 01 CP awards remain actual history: Elian 13, Rook 41, Aster 52, Mileia 15, Nella 23 reserve after award.
- Elian registered the one-day document/inventory verification job. He gave `Elian, Three Silver Coins` as the clerk-requested name/contact-lodging answer. This does not itself prove a room booking or payment.
- Rook showed interest in the two-day convoy job but had not accepted it.
- Aster showed interest in the arcane-residue identification job but had not accepted it.
- The 18 gp overnight escort remained open at last established Guild state.

## Events since the prior live pointer

1. Elian returned to the Guild clerk and asked where the bard/poet academy was.
2. The public destination was established in the Old City / Theatre Street area. Current stabilized public navigation is:

```text
SITE-ANDOR-BARD-COLLEGE
OLD CITY
劇場街西段 → 七弦巷口
```

3. Elian chose to go see the Old City evening activity.
4. PL+PC split decisions at departure:
   - 鮫島 / Rook: intended to remain at the Guild and ask further details about the normal convoy job before deciding; no acceptance is yet resolved.
   - 赫茲 / Aster: intended to ask whether the arcane-residue job can be handled tomorrow and potentially register if compatible, then later seek Mileia/church; no registration/result is yet resolved.
   - 蟬 / Nella: decided to accompany Elian to the Old City / Theatre Street.
5. Elian and Nella left the Guild and walked toward the Old City.
6. During the walk, Elian openly discussed people who hide in corners versus behind clothing/masks/performance and said he wanted inspiration and would be pleased to encounter people of the Low Whisper tradition.
7. Elian's private intention also includes interest in useful information exchange and, if an opportunity arises, learning bardic techniques. This remains Elian's internal/player-authorized state and is not automatically known by Nella.
8. The road/streetscape shifted from practical commercial goods toward food/drink, books, instrument parts, paper/ink, ornaments, masks, performance notices and entertainment-oriented traffic as they entered the Old City social ecology.
9. Elian and Nella reached the core Theatre Street area: small theatres, a larger performance venue, taverns and the public bard-academy destination are now nearby / in view-range as ordinary urban landmarks.
10. No new D100 roll has occurred since Elian's Guild registration.
11. Elian then answered the prior bardic-study question aloud while walking with Nella. Player-authorized background facts now established:
   - Elian had not previously studied bardic arts.
   - In his old home/family environment, he was not allowed/encouraged to study those things.
   - His family expected him to help shoulder some of the intellectual/administrative burden around his older brother rather than pursue bardic training.
   - In Elian's own recollection, his older brother was the sibling who was genuinely eloquent and charismatic.
   - Elian's present stated attitude is pragmatic: if an unfamiliar technique can be used and is useful, he is willing to try it; if he cannot do it himself, he is willing to rely on people who can.
12. The statements in event 11 were spoken aloud to Nella. They are therefore part of Nella's legitimate IC knowledge from this point forward, regardless of the unresolved renderer origin of the earlier question.

## Elian player-authorized background additions

```yaml
origin_kind: player-decision / player-authored-backstory
status: committed
claims:
  - no prior bardic training
  - family/old-home environment discouraged or prevented bardic study
  - family expected Elian to carry intellectual/administrative work alongside or around his older brother
  - Elian remembers his older brother as more naturally eloquent/charismatic
  - Elian currently values useful methods over identity purity and is willing to delegate to capable people
```

These facts do not by themselves specify the exact family title, political history, inheritance order, brother's current status, or the precise reason the family opposed bardic study. Those remain uncommitted unless later established.

## OOC / IC ambiguity preserved, with current disclosure boundary

`OOC-AMBIG-ANDOR-001` remains preserved as a renderer/runtime incident: the earlier generated question about whether Elian had previously studied bardic arts may originally have been 蟬 speaking as PL/OOC but rendered as Nella IC dialogue.

However, Elian has now voluntarily answered that topic aloud in Nella's presence. Therefore:

```text
Do not use the old ambiguous utterance as proof of earlier Nella IC knowledge, attraction, intimacy, or relationship state.
Do treat Elian's newly spoken answer as current Nella IC knowledge from this point onward.
Do not retroactively invent any earlier Nella knowledge beyond what was actually established.
Future Player Voice decisions may freely create new Nella affect/intention from the current point; NON_ASSERTION is not a prohibition.
```

## Low Whisper / site knowledge boundary

- D100 source-backed fact: Low Whisper College/tradition exists and commonly conceals affiliation.
- Campaign state: a public Old City venue `SITE-ANDOR-WHISPERS-CONTACT` / 曲聞會館 exists and has ordinary public services; its non-public organizational relation is Mystery-gated.
- Elian currently knows/has spoken about the Low Whisper concept/tradition.
- Do **not** automatically give Elian or Nella the venue's non-public relation merely because backend state contains it.
- The public bard academy and 曲聞會館 are separate stable sites; do not silently merge them.

## Resume boundary

Resume **on Theatre Street before Elian and Nella enter the bard academy or initiate a new conversation with a site/NPC**, immediately after Elian's spoken family/bardic disclosure.

At resume:

- Elian controls his own next action.
- 蟬 controls Nella's important PL+PC choices.
- Nella may legitimately respond to the newly spoken disclosure, but her reaction/affect is not precommitted by the DM.
- Rook/Aster/Mileia remain off-camera with only the intentions/events actually established above; do not auto-resolve their pending plans merely because time passed off-camera.
- Public ordinary environment can be described without a roll.
- If a specific NPC/site reaction will materially depend on hidden knowledge or affiliation, establish/confirm the relevant minimum commitment before the reaction/roll.

## Provenance / navigation

Use:

- `campaign/andor_sites.md` for source/generated/user-correction splits and stable site IDs.
- `campaign/andor_map_adoption.md` for authoritative exact public-navigation claims.
- `campaign/andor_public_map.md` for player-safe map projection.
- `99_open_questions/librarian_routing_resolution_2026-09-16.md` for the resolved Librarian-routing incident and corrected source-resolution conclusions.
