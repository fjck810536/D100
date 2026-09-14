# Andor Session 1 — Runtime Migration Hidden Commitments

> Storage: MYSTERY VAULT / SOFT secret.
>
> Status: normal secrets + hidden causal commitments; **no EX**.
>
> Migration provenance: these commitments were created at the explicit runtime migration boundary after the Grey Antler suspicious-man reactions had already been narrated under the old runtime. They are therefore **retroactive migration commitments**, not a claim that a complete hidden state existed before those earlier narrated reactions. From this file onward, the committed facts below are locked against roll-result retcon.

---

## SECRET-ANDOR-001 — Blue-Wax Transfer Incident

```yaml
secret_id: SECRET-ANDOR-001
classification: normal_secret_pending_label
ex_status: none
commitment_status: committed
migration_provenance: retroactive_runtime_migration_2026-09-15
```

### Truth core

Five days before the current Grey Antler scene, **Miren Vale**, male, age 21, a junior copyist attached to John Academy records work, was assigned to carry a **blue-wax sealed document box** from an Academy special-collections registry annex to an external bonded records office serving the merchant district.

The box contains **access, transfer, and audit records concerning special-collection materials**. It does **not** contain a magical artifact. Several records inside would be politically or institutionally embarrassing if exposed because they show irregular or retrospectively altered access entries involving Academy patrons / external clients.

Miren noticed discrepancies in the records and became afraid he might be blamed for them. He **deliberately diverted from the delivery route and disappeared with the box** rather than completing the handoff. He is currently **alive and hiding in Andor under a false surname**. The box is cached separately from his person somewhere inside the city. Exact room, street, and cache furniture remain mutable surface detail until they become causally relevant.

Miren does not understand the full political network represented by the records. He knows only that the paperwork was altered, that the box proves at least some discrepancy, and that possessing it gives him leverage but also puts him at risk.

### Consequences already in world state

- John Academy tightened access to special collections because the registry trail is incomplete and the institution cannot confidently account for who had access to some materials.
- The public missing-person notice and the document-box recovery notice have different formal origins/signers.
- The missing-person reward is 20 gp.
- The box reward began at 15 gp and was later raised to 40 gp after the receiving records office realized the box contained sensitive access/audit material, not merely routine delivery papers.
- The similar timing / fresh ink between the notices is real; it does not by itself prove a single issuer.

### Knowledge holders

```yaml
knowledge_holders:
  - Miren Vale: knows he diverted with the box; knows records are inconsistent; does not know full implications
  - receiving bonded-records supervisor: knows box and copyist disappeared on same transfer; knows records are sensitive; does not know Miren location
  - Oren Pell: knows the transfer case, missing copyist, reward increase, and sensitivity level in broad terms; does not know the altered entries or Miren location
  - limited John Academy records staff: know a transfer failed and access controls were tightened; knowledge depth varies
```

### Existing evidence visible to players

```yaml
existing_evidence:
  - EVID-ANDOR-001 missing copyist notice, five days
  - EVID-ANDOR-002 blue-wax document box reward 15 -> 40 gp
  - EVID-ANDOR-003 special-collection access restriction changed recently
  - EVID-ANDOR-006 similar-looking fresh date ink between two notices, weak observation
```

### Causal boundary

The following are now fixed and may not be changed because a later roll succeeds or fails:

- the copyist and box are connected through the failed transfer;
- Miren is alive at the migration boundary;
- he deliberately diverted rather than being killed before the transfer;
- the box is a records/audit object, not a magical artifact;
- Academy access restrictions are partly a response to the missing/incomplete registry trail;
- Oren Pell's reactions at Grey Antler derive from his real prior knowledge of this case.

Normal future world events can still change Miren's safety, location, possession of the box, or plans.

---

## COMMIT-ANDOR-ACTOR-001 — Oren Pell

```yaml
commitment_id: COMMIT-ANDOR-ACTOR-001
commitment_status: committed
secret_refs:
  - SECRET-ANDOR-001
migration_provenance: retroactive_runtime_migration_2026-09-15
```

### Minimum hidden actor state

```yaml
actor_state:
  identity_floor: junior clerk / runner employed by the bonded records office that was supposed to receive the blue-wax box
  alignment:
    law_chaos: lawful
    good_evil: neutral
  presented_persona: quiet, ordinary, unobtrusive office worker
  current_affect: wary and mildly alarmed by the Grey Antler conversation
  relevant_knowledge:
    - Miren Vale was the expected courier/copyist on the failed transfer
    - the blue-wax box is missing
    - the public reward was raised from 15 to 40 gp
    - the contents are institutionally sensitive records
  relevant_beliefs:
    - the Grey Antler table may include freelancers or Academy-connected people who have independently noticed the case
    - Aster's appearance marks him as plausibly magic-educated / Academy-adjacent, but Oren does not know his identity
  current_goal: report the unusual public discussion to his supervisor without confronting the table
  current_constraints:
    - not a trained field agent
    - does not want violence or public attention
    - lacks authority to seize people or property
  intended_next_step: leave Grey Antler, walk toward a merchant-district message desk / office route, and send or deliver a short report to his supervisor
  reaction_causes:
    - "missing copyist" directly matches a case he knows
    - "40 gp box" matches the exact revised reward he helped process
    - Aster drew his glance because a young visibly educated mage could plausibly be Academy-connected
```

### Tail-awareness state at migration boundary

At the moment Oren exits Grey Antler, **he has not yet identified Nella as a tail**. This is now fixed as the pre-tail state. Subsequent awareness can change normally through perception, behavior, environment, or rolls.

### What is not committed

- exact street he turns onto after every junction;
- exact appearance beyond previously narrated broad description;
- exact words of the message he will send;
- whether Nella ultimately keeps or loses him;
- whether he later changes plans because of new events.

---

## COMMIT-ANDOR-ECON-001 — Low-Level Spell Material Price Rise

```yaml
commitment_id: COMMIT-ANDOR-ECON-001
commitment_status: committed
secret_refs: []
```

### Truth core

The observed ~30% increase in several low-level spell-material buy prices is **not caused by SECRET-ANDOR-001**.

The immediate cause is a short-term supply disruption: two expected southern supply loads are delayed by transport / inspection problems outside the city, temporarily tightening supply for a few commonly traded components. Merchants are repricing unevenly because they do not all have the same stock or information.

This can be discovered through ordinary market inquiry. Exact caravan names and minor logistics remain mutable until relevant.

---

## COMMIT-ANDOR-SILVERCOINS-001 — Confidential Documents / Accounts Job

```yaml
commitment_id: COMMIT-ANDOR-SILVERCOINS-001
commitment_status: committed
secret_refs: []
```

### Truth core

The private job advertised at **Three Silver Coins** for someone familiar with documents, accounts, and confidentiality is **not part of SECRET-ANDOR-001** at the migration boundary.

It comes from a small merchant concern facing an internal accounts / customs / partnership dispute and needing temporary discreet clerical help. The work may have its own risks and secrets, but it is not secretly the Academy copyist / blue-box case.

Employer name, exact account discrepancy, and the person who will conduct the meeting remain mutable until the job is actually contacted, provided later generation does not retroactively connect it to SECRET-ANDOR-001 without a new world event.

---

## Migration anti-retcon fuse

```text
The three public hooks are not all one plot.
SECRET-ANDOR-001 links the missing copyist, blue-wax box, and special-collection restriction.
The spell-material price rise is currently independent.
The Three Silver Coins clerical job is currently independent.
Oren Pell is a peripheral informed clerk, not retroactively promoted into a mastermind because the players noticed him.
Future events may connect previously independent threads only through new causal events, not by rewriting what they had always been.
```
