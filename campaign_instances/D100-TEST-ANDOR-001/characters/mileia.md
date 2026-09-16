# Mileia / 米蕾亞 — Authoritative Character Record

> Recovered authoritative PC state after `CHARACTER-STATE-PROMOTION-INCIDENT-2026-09-16`.
> This file records only facts that are already established. Missing build details must be recovered, not invented.

```yaml
character_id: PC-MILEIA
name: Mileia
zh_name: 米蕾亞
controller:
  mode: pl_pc
  player_voice: 彌生
alignment:
  law_chaos: neutral
  good_evil: good
concept: 生命領域牧師 / 補師
record_status: authoritative_recovered_partial
recovery_date: 2026-09-16
```

## Identity / faith / training

```yaml
identity_and_training:
  deity_or_faith:
    canonical_name: Lathander
    zh_name: 晨曦之主
    status: committed
    provenance: user-declared during character creation; recovered 2026-09-16 after persistence audit
  domain:
    - Life Domain / 生命領域
  cleric_identity:
    status: committed
    description: 生命領域牧師 / 補師
```

### Provenance boundary

- Mileia's faith in **Lathander / 晨曦之主** and her **Life Domain / 生命領域** were explicitly established during character creation. They are not a 2026-09-16 creative addition.
- D100 Sheet canon independently supports Lathander as an example deity associated with the Life Domain, but the reason these fields are authoritative for Mileia is the prior player/PL creation decision, not inference from the domain list.
- Do not replace these fields with `unknown`, `NON_ASSERTION`, or a newly generated deity merely because an older session snapshot omitted them.

## Established attributes and derived values

```yaml
attributes_total:
  STR: 7
  DEX: 10
  SKI: 8
  CON: 18
  RES: 18
  INT: 16
  WIS: 22
  CHA: 19
  SPI: 22
bases:
  combat: 25
  athletic: 36
  operation: 46
  perception: 56
  knowledge: 57
  interaction: 63
resources:
  hp: 20/20
  sp: 35/35
  cp_reserve: 15
```

These values are established runtime character data. Exact raw-vs-adjustment decomposition is still pending recovery.

## Established character direction

- Care / medicine / social-presence orientation; does not imply party-mother autopilot.
- Moderate helping-risk tolerance.
- **Current rollback boundary:** Mileia has just separated from the party after the Mercenary Guild split. No post-split travel, local site arrival, local NPC contact, volunteering, or newly learned local religious/medical practice is established.
- Exact availability/preparation of Zone of Truth or any other specific spell is not established by this recovered minimum card unless separately recovered from the original build record.

## Capability-record recovery status

The repository currently lacks the original full final character instance that should have been written at character-creation completion. Therefore:

```yaml
recovery_status:
  identity_core: recovered
  faith_and_domain: recovered
  alignment: recovered
  attributes_total_and_bases: recovered
  hp_sp_cp_live_values: recovered_from_session
  full_creation_ledger: pending_recovery
  raw_stats_and_adjustments: pending_recovery
  complete_skill_feat_list: pending_recovery
  languages: pending_recovery
  spell_list_and_preparation: pending_recovery
  equipment: pending_recovery
```

`pending_recovery` means **the established record was lost or not promoted into the current authoritative character layer**. It does not mean the character canonically lacks those facts.

## Runtime fuse

When a scene or query depends on a `pending_recovery` character field:

1. search authoritative character records and creation audit/history;
2. search current/prior session records and explicit user/PL decisions;
3. recover established facts with provenance;
4. only after recovery sources are exhausted may the field be reported as unresolved.

Never silently convert `record missing` into `character fact never established`.
