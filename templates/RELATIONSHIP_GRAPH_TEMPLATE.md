# RELATIONSHIP_GRAPH_TEMPLATE.md

> Authoritative relationship-state template. Only record relationships/events that actually exist in the world. Interpretations belong to derived Analyst/Politician views.

```yaml
relationship_graph_id:
updated_at:

edges:
  - edge_id:
    actor_a:
    actor_b:
    relation_types: []
    established_events: []
    commitments: []
    debts: []
    authority_or_dependency: []
    shared_resources: []
    public_status:
    secret_refs: []
    provenance_refs: []
    last_updated:
```

## Epistemic pointers

Relationship facts do not imply every actor knows them. Keep actor-specific knowledge in each actor's Epistemic State, or point to it here without duplicating payloads.

```yaml
epistemic_refs:
  - actor_id:
    known_relationship_edges: []
    belief_refs: []
    misbelief_refs: []
```

## Derived views

Do not store these as authoritative facts. If cached, keep them invalidatable.

```yaml
derived_views:
  analyst_refs: []
  politician_refs: []
```

## Core fuse

```text
relationship fact ≠ relationship interpretation
world relation ≠ actor belief about the relation
commitment ≠ inevitable future action
```
