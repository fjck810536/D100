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

## Current runtime resources

The current session snapshot establishes:

```yaml
hp: 20/20
sp: 35/35
cp_reserve: 15
```

These are live-session values and may change through play.

## Capability-record recovery status

The repository currently lacks the original full final character instance that should have been written at character-creation completion. Therefore:

```yaml
recovery_status:
  identity_core: recovered
  faith_and_domain: recovered
  alignment: recovered
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
