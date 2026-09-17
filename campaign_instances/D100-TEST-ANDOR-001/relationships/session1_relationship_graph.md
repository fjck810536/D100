# Andor Session 1 — Relationship Graph

> Normalized authoritative relationship state for `D100-TEST-ANDOR-001`.
>
> This record gathers relational events and durable social-state facts already established in the selected campaign's character/session records. Actor-specific affect and epistemic state remain with the actor/session layers rather than being duplicated here.

```yaml
relationship_graph_id: RELGRAPH-ANDOR-SESSION1-001
campaign_id: D100-TEST-ANDOR-001
updated_at: 2026-09-18
```

## Established events

### REL-001 — Shared arrival

```yaml
participants: [PC-ELIAN, PC-ROOK, PC-ASTER, PC-MILEIA, PC-NELLA]
fact: all five shared farmer-wagon travel into Andor
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
```

### REL-002 — Shared Grey Antler meal

```yaml
participants: [PC-ELIAN, PC-ROOK, PC-ASTER, PC-MILEIA, PC-NELLA]
fact: all five shared a Grey Antler meal; Elian paid 4 gp
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
```

### REL-003 — Possible rendezvous discussed

```yaml
participants: [PC-ELIAN, PC-ROOK, PC-ASTER, PC-MILEIA, PC-NELLA]
fact: the group discussed Three Silver Coins as a possible later rendezvous
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
```

### REL-004 — Elian warns Aster

```yaml
participants: [PC-ELIAN, PC-ASTER]
fact: Elian privately warned Aster that Aster had been watched
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
```

### REL-005 — Cloak handoff chain

```yaml
participants: [PC-ELIAN, PC-ASTER, PC-NELLA]
fact: Elian entrusted his invisibility cloak to Aster; Aster transferred holder-state to Nella in the improvised-signal context
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
```

### REL-006 — Nella tails Oren

```yaml
participants: [PC-NELLA, NPC-OREN-PELL]
fact: Nella independently left Grey Antler after Oren Pell and completed the tail
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
```

### REL-007 — Cloak returned

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Nella carried Elian's cloak without activating it and returned it after the tail
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
```

### REL-008 — Tail report shared

```yaml
participants: [PC-NELLA, PC-ELIAN, PC-ROOK, PC-ASTER, PC-MILEIA]
fact: Nella voluntarily reported her tail observations to the group after returning
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
```

### REL-009 — Aster / Rook guild plan

```yaml
participants: [PC-ASTER, PC-ROOK]
fact: Aster and Rook discussed potentially visiting the Mercenary Guild together after the meal
status_note: current plan candidate at the checkpoint, not a binding contract
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
```

### REL-010 — Elian / Nella enter the bard academy together

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Elian and Nella entered the public bard-academy common hall together
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
```

### REL-011 — Drink sent under both names

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Elian sent a tasteful sweet drink to a young woman/regular under both Elian and Nella's names; she accepted and acknowledged both
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
```

### REL-012 — Coordinated bard-hall social performance

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: after Elian's wink/banter cue, Nella cooperated with the social performance using Elian's wallet and selectively sent drinks to the older patron and other visible post-performance connectors
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
```

### REL-013 — Pair recognized as coordinated participants

```yaml
participants: [PC-ELIAN, PC-NELLA, NPC-ANDOR-BARD-OBSERVER-B]
fact: the older patron visibly noticed the selection pattern and acknowledged Elian and Nella as coordinated participants in the same social field
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
```

### REL-014 — Elian discloses bardic/family background to Nella

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Elian later voluntarily disclosed his bardic/family background aloud to Nella
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
  - campaign_instances/D100-TEST-ANDOR-001/characters/elian.md
  - campaign_instances/D100-TEST-ANDOR-001/characters/nella.md
```

### REL-015 — Bard-academy departure together

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Elian and Nella exited the bard academy into the Old City night together and remained at the same departure point
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
```

### REL-016 — Merchant reconnaissance together

```yaml
participants: [PC-ELIAN, PC-NELLA]
fact: Elian asked Nella to lead a public reconnaissance walk past the two locations from her earlier tail; Nella led the route and the pair completed the public walk without beginning a surveillance operation
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-05.md
```

### REL-017 — Mileia / Cael first clerical contact

```yaml
participants: [PC-MILEIA, NPC-ANDOR-MORNINGHALL-CAEL]
fact: Mileia met Cael Arven at the Morninghall, identified herself as an outside Lathander / Life Domain cleric, received a public-area orientation, and agreed to return for morning prayer and formal local-clergy introduction
provenance_refs:
  - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-04.md
```

## Edges

```yaml
edges:
  - edge_id: EDGE-ANDOR-ELIAN-NELLA
    actor_a: PC-ELIAN
    actor_b: PC-NELLA
    relation_types:
      - same_party
      - temporary_resource_transfer
      - information_sharing
      - joint_social_action
      - joint_reconnaissance
    established_events:
      - REL-001
      - REL-002
      - REL-003
      - REL-005
      - REL-007
      - REL-008
      - REL-010
      - REL-011
      - REL-012
      - REL-013
      - REL-014
      - REL-015
      - REL-016
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources:
      - ITEM-ELIAN-CLOAK-001 temporary holder transfer, resolved by REL-007
      - Elian funds used for the coordinated bard-hall drink-sending event
    public_status: same adventuring party; publicly appeared as a coordinated pair during the bard-hall social pass
    secret_refs: []
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state.md
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-05.md
    last_updated: 2026-09-18

  - edge_id: EDGE-ANDOR-ELIAN-ASTER
    actor_a: PC-ELIAN
    actor_b: PC-ASTER
    relation_types:
      - same_party
      - private_warning
      - temporary_resource_transfer
    established_events: [REL-001, REL-002, REL-003, REL-004, REL-005]
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources:
      - ITEM-ELIAN-CLOAK-001 temporary holder transfer during REL-005
    public_status: same adventuring party
    secret_refs: []
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
    last_updated: 2026-09-18

  - edge_id: EDGE-ANDOR-ASTER-NELLA
    actor_a: PC-ASTER
    actor_b: PC-NELLA
    relation_types:
      - same_party
      - temporary_resource_transfer
    established_events: [REL-001, REL-002, REL-003, REL-005]
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources:
      - ITEM-ELIAN-CLOAK-001 holder-state transfer during REL-005
    public_status: same adventuring party
    secret_refs: []
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_runtime-migration.md
    last_updated: 2026-09-18

  - edge_id: EDGE-ANDOR-ASTER-ROOK
    actor_a: PC-ASTER
    actor_b: PC-ROOK
    relation_types:
      - same_party
      - joint_plan_candidate
    established_events: [REL-001, REL-002, REL-003, REL-009]
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources: []
    public_status: same adventuring party
    secret_refs: []
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
    last_updated: 2026-09-18

  - edge_id: EDGE-ANDOR-NELLA-OREN
    actor_a: PC-NELLA
    actor_b: NPC-OREN-PELL
    relation_types:
      - surveillance_contact
    established_events: [REL-006]
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources: []
    public_status: null
    secret_refs:
      - SECRET-ANDOR-001
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-15_session-1_checkpoint-01.md
    last_updated: 2026-09-18

  - edge_id: EDGE-ANDOR-MILEIA-CAEL
    actor_a: PC-MILEIA
    actor_b: NPC-ANDOR-MORNINGHALL-CAEL
    relation_types:
      - same_faith_clerical_contact
      - local_contact
    established_events: [REL-017]
    commitments:
      - Mileia agreed to return for morning prayer and formal local-clergy introduction
    debts: []
    authority_or_dependency: []
    shared_resources: []
    public_status: visiting outside cleric received by local night-duty cleric
    secret_refs: []
    provenance_refs:
      - campaign_instances/D100-TEST-ANDOR-001/sessions/2026-09-16_session-1_live-state-04.md
    last_updated: 2026-09-18
```

Pair-specific edges are listed where the surviving campaign record contains more than the shared-party baseline. Multi-actor events remain single event records rather than being duplicated across every possible party pair.
