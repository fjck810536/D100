# WORLD_COMMITMENT_TEMPLATE.md

> Hidden world-state commitment template. Use when an NPC, event, mystery, hazard, faction plan, or other causal object is about to become observable or affectable. Commit the minimum causally relevant truth before resolving player interaction.

```yaml
commitment_id:
commitment_status: committed
created_at:
commit_before_event_ref:

truth_core:
involved_entities: []
knowledge_holders: []
misbelief_holders: []
existing_evidence: []
secret_refs: []

actor_goals: []
actor_constraints: []
planned_actions: []
world_clock: []

mutable_surface_details: []
provenance_refs: []
```

## Minimum hidden actor state

When a specific actor's reaction can materially affect play, commit at least:

```yaml
actor_state:
  identity_floor:
  relevant_knowledge: []
  relevant_beliefs: []
  current_goal:
  current_constraints: []
  intended_next_step:
  reaction_causes: []
```

`identity_floor` may be coarse. It only needs enough detail to prevent a later roll from deciding retroactively what the actor was.

## Evidence / causal separation

```yaml
causal_refs: []
evidence_refs: []
```

Players may only have evidence refs. The causal refs remain role-safe / Mystery-gated.

## Mutable surface details

These may be generated later if they do not rewrite committed causality, for example:

- incidental clothing color;
- shop names not previously relevant;
- room decoration;
- minor dialogue texture;
- unimportant bystander names.

## Anti-retcon fuse

```text
roll outcome may change discovery / interference / consequence
roll outcome must not decide what the committed truth had always been
```
