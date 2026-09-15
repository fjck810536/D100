# WORLD_COMMITMENT_TEMPLATE.md

> Hidden world-state commitment template. Use when an NPC, event, mystery, hazard, faction plan, or other causal object is about to become observable or affectable. Commit the minimum causally relevant truth before resolving player interaction.
>
> Commitment is the causal floor, not a generation ceiling. A source gap may enter grounded generation when there is no hard conflict and the proper owner adopts the proposal; the resulting claim keeps its generated provenance.

```yaml
commitment_id:
commitment_status: committed
created_at:
recorded_at:
effective_from:
commit_before_event_ref:
adoption_event_ref:
claim_refs: []

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

## Provenance / adoption

A commitment may contain claims from different origins. Do not label the whole object `canon` or `generated` when the fields differ.

```yaml
claim_provenance:
  - claim_ref:
    origin_kind: source-extraction | user-correction | pl-decision | creative-addition | legacy-generated
    generated: true | false
    source_refs: []
    contextual_support_refs: []
    decision_owner:
    decision_event_ref:
    committed_at:
    effective_from:
    visibility_ref:
```

Rules:

```text
recorded_at ≠ effective_from
later provenance repair ≠ claim was documented earlier
creative-addition adopted by AO/PL may become authoritative state
adopted creative-addition ≠ source text
```

If a previously played scene lacked a provenance/commitment record, repair it honestly as `legacy-generated` / later-recorded instead of fabricating an earlier timestamp.

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

Setting-bearing details may also be generated and adopted when needed—such as a local branch, public contact point, teacher, or service route—provided they do not conflict with established facts, their decision owner is legitimate, and their generated origin is recorded. They are not required to remain permanently blank merely because the source did not enumerate them.

## Deferred / blocked operations

Do not store vague `not yet` as if it were a meaningful state. If an operation is actually waiting, use a typed record or reference:

```yaml
deferral_refs:
  - type: NON_ASSERTION | DEFERRED | OWNER_DECISION | PROHIBITED | NOT_SELECTED
    blocked_operation:
    owner:
    trigger:
    reevaluate_with:
    rule_or_fact_ref:
```

Only `DEFERRED` requires a concrete trigger. `NON_ASSERTION` means “do not assert this unconfirmed proposition as an existing fact”; it does **not** prohibit proposing or creating a compatible new development. `NOT_SELECTED` is not a permanent ban.

## Anti-retcon fuse

```text
roll outcome may change discovery / interference / consequence
roll outcome must not decide what the committed truth had always been
SOURCE_GAP does not authorize retroactive roll-shaped truth
SOURCE_GAP also does not mean grounded generation is forbidden
```
