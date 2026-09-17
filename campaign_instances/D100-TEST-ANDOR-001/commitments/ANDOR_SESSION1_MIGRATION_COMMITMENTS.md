# Andor Session 1 — Runtime Migration Commitments

> Normalized commitment record extracted from the mixed migration bundle `campaign_instances/D100-TEST-ANDOR-001/mystery/ANDOR_SESSION1_MIGRATION.md`.
>
> The secret truth core `SECRET-ANDOR-001` remains in the Mystery layer. This file preserves the commitment portions so the selected campaign's `commitments/` store is complete without duplicating the protected secret payload as ordinary commitment state.

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
