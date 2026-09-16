# Session 1 — Andor Live State 04

> Current role-safe pointer for `D100-TEST-ANDOR-001`. This supersedes `sessions/2026-09-16_session-1_live-state-03.md` as the active live pointer while preserving it as history.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
world_time: split-thread chronology
four_voice_control: pl_pc
active_camera: Elian/Nella boundary
prior_live_session_ref: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-03.md
```

## Current party positions

- Elian: paused just outside / leaving `SITE-ANDOR-BARD-COLLEGE` after the common-hall departure. Human player retains control; no new action has been assumed.
- Nella: paused with Elian at that departure point unless 蟬 later chooses otherwise.
- Rook: at the Mercenary Guild; north-road convoy accepted by 鮫島. Signup is established; departure has not yet occurred.
- Aster: at the Mercenary Guild; arcane-residue warehouse inspection accepted by 赫茲. Registration is established; travel to the warehouse has not yet occurred.
- Mileia: has completed an ordinary first visit to `SITE-ANDOR-LATHANDER-MORNINGHALL`, met night-duty cleric Cael Arven, received a public-area orientation, stated her temple/poorhouse healing background, and agreed to return for morning prayer / formal local-clergy introduction. She has left or is leaving the Morninghall with ordinary directions toward nearby lodging; no lodging transaction, room, price, or exact inn identity is established.

## Mileia — Morninghall first visit

```yaml
event_id: EVENT-ANDOR-MILEIA-MORNINGHALL-FIRST-VISIT-001
owner: 彌生 / PL
status: committed
site_ref: campaign_instances/D100-TEST-ANDOR-001/sites/andor_lathander_morninghall.md
npc_ref: NPC-ANDOR-MORNINGHALL-CAEL
```

Established events:

- Mileia deliberately sought the local Lathander temple after the guild split.
- She reached the public Morninghall and identified herself as Mileia, a Lathander / Life Domain cleric newly arrived in Andor.
- Cael Arven, the already committed junior ordained night-duty cleric, introduced himself and received her as an outside same-faith cleric without granting automatic local authority.
- Mileia said her purpose was to know the local temple, understand how it operates, and learn how to help later without assuming entitlement.
- Cael gave a short orientation limited to public devotional/reception areas; no restricted internal access was granted.
- Mileia described her prior work as primarily healing / temple / poorhouse care, including wounds, patients, ordinary care, and situations requiring divine magic.
- Cael said the Morninghall also handles healing/reception, but did not assign her work that night.
- Mileia agreed to return the next morning for morning prayer and introduction to the appropriate on-duty senior clergy before any professional collaboration.
- Mileia said she had not yet arranged lodging. She preferred an ordinary inn rather than asking the temple to arrange a bed that night.
- Cael offered ordinary public directions toward nearby lodging. Exact inn identity, room availability, price, payment, and stay are not established.

No roll, CP expenditure, HP/SP change, spell preparation, patient contact, volunteering, local authority, or new quest occurred.

## Rollback / anti-reuse fuse

- This new Morninghall visit occurs **after** the DM rollback boundary and is independently established in play.
- VOID facts from the deleted south-care-node branch remain VOID and were not reused.
- Morninghall / Cael facts derive from the committed Morninghall site record, not from the deleted branch.

## Stable refs / independence fuses

- Elian/Nella bard-hall commitments and evidence remain unchanged.
- Rook convoy and Aster residue job remain unchanged.
- Mileia's Morninghall contact has no automatic connection to Blue-Wax, Low Whisper, Three Silver Coins, guild jobs, or other active mystery threads.
- No exact Mileia lodging cost/funds state is created because her starting money remains `no_recovered_evidence`.
