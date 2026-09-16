# Session 1 — Andor Live State 05

> Current role-safe pointer for `D100-TEST-ANDOR-001`. This supersedes `sessions/2026-09-16_session-1_live-state-04.md` as the active live pointer while preserving it as history.

```yaml
session_id: D100-TEST-ANDOR-001
date_recorded: 2026-09-16
world_time: split-thread chronology
four_voice_control: pl_pc
active_camera: Elian/Nella
prior_live_session_ref: campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-04.md
```

## Current party positions

- Elian: in the merchant-commercial area with Nella after a casual reconnaissance walk past the two locations from Nella's earlier tail. Human player retains all further action control.
- Nella: with Elian, having led the route and completed two Search checks for surveillance geometry. No surveillance operation has started.
- Rook: at the Mercenary Guild; north-road convoy accepted. Signup established; departure has not yet occurred.
- Aster: at the Mercenary Guild; arcane-residue warehouse inspection accepted. Registration established; travel to warehouse has not yet occurred.
- Mileia: completed first Morninghall visit; leaving/has left with ordinary nearby-lodging directions, planning to return for morning prayer. No lodging transaction established.

## Elian / Nella — merchant reconnaissance

```yaml
event_id: EVENT-ANDOR-ELIAN-NELLA-MERCHANT-RECON-001
initiator: PC-ELIAN / human player
route_lead: PC-NELLA / 蟬 PL
status: committed
site_ref: campaign_instances/D100-TEST-ANDOR-001/sites/andor_merchant_recon.md
```

Player instruction / intent:

- Elian jokingly framed the outing as a walk and asked Nella to lead because he did not know the roads well;
- explicit player intent was to circle the two locations Nella discovered during her earlier tail, identify convenient surveillance positions, and include Three Silver Coins if geographically convenient;
- no extra Elian action, infiltration, rental, entry, or surveillance decision was assumed beyond walking the public route with Nella.

### First location

The earlier first stop is now publicly characterized as a commercial message/document office handling message transfer, document delivery, copying and sealed-document services.

```yaml
ROLL-ANDOR-RECON-001:
  actor: PC-NELLA
  interface: 搜索
  value: 76
  d100: 51
  result: success_by_25
```

Result: Nella identified a diagonally opposite ordinary inn whose suitable second-floor street-facing rooms can observe both the office front entrance and the entrance to its side delivery lane. No room has been rented and no cost is established.

### Second location

The earlier second stop's public frontage now establishes a business function involving contracts, bonded/secured documents and commercial record custody. This supports but does not confirm Nella's prior inference that the suspicious man might work there.

```yaml
ROLL-ANDOR-RECON-002:
  actor: PC-NELLA
  interface: 搜索
  value: 76
  d100: 82
  result: fail_by_6
```

Result boundary: no comparably clean fixed surveillance point was found in this pass. The front is open and side lanes are narrow enough that stationary lingering would stand out. Adjacent streets permit a moving observation loop, but it grants no automatic concealment or information.

### Three Silver Coins relation

Ordinary local geography is now stabilized:

- Three Silver Coins is on the edge of the same broader merchant-commercial area;
- roughly 4–5 minutes' walking detour from the first office;
- under roughly 10 minutes from the second building;
- this convenience establishes no causal link among the sites.

## Evidence additions

- `EVID-ANDOR-014`: first office publicly handles messages/documents/copying/sealed delivery — OBSERVED.
- `EVID-ANDOR-015`: suitable rooms in diagonally opposite inn offer useful fixed observation geometry for first office — OBSERVED / reconnaissance success.
- `EVID-ANDOR-016`: second building publicly handles contracts/bonded or secured documents/commercial record custody — OBSERVED.
- `EVID-ANDOR-017`: no comparably clean fixed observation point was found for second building during this pass — OBSERVED / incomplete-search result.
- `HYP-ANDOR-005`: second building may be the suspicious man's normal workplace — INFERRED, not confirmed.

## Independence / knowledge fuses

- no Three Silver Coins connection to Oren / Blue-Wax is created;
- no claim that the suspicious man is currently inside or absent from either building is established;
- no note recipient/content is revealed;
- public business function does not prove employment;
- Elian has not yet chosen whether to rent the surveillance room, continue toward Three Silver Coins, perform moving observation, enter either business, or end the walk;
- Nella may advise, but does not choose Elian's next action.
