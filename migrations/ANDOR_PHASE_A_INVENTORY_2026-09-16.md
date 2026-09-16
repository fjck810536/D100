# Andor Persistent-Test Migration — Phase A Inventory

> Status: INVENTORY COMPLETE / NO MIGRATION EXECUTED
>
> Campaign candidate: `D100-TEST-ANDOR-001`
>
> 本檔只辨識 legacy records 的 campaign ownership、authority type 與未來 migration action。它**不建立** `campaign_instances/D100-TEST-ANDOR-001/`、不移動／刪除既有檔案、不重建角色、不更新 live state。

---

## 0. Inventory conclusion

目前 legacy root 並不是一個可直接整包搬移的 campaign folder。

```text
root characters/      = Andor actor masters + stale recovery manifest
root sessions/        = Andor Session 1 history/current pointer
root campaign/        = Andor site/map state + unrelated empty placeholder current_state
root mystery_vault/   = Andor Mystery records
sources/characters/   = 另一批角色 evidence/cache，非 Andor actor master
```

因此 migration 必須採：

```text
record-by-record ownership + authority classification
```

而不是：

```text
copy campaign/
copy characters/
copy sessions/
copy mystery_vault/
```

---

# 1. Actor records

| Legacy record | Andor ownership | Authority | Migration action | Notes |
|---|---|---|---|---|
| `characters/elian.md` | YES | authoritative actor master, recovered partial | INCLUDE → target `characters/` | `PC-ELIAN`; preserve `pending_recovery`; session checks must not replace master |
| `characters/rook.md` | YES | authoritative actor master, recovered partial | INCLUDE → target `characters/` | `PC-ROOK`; 鮫島 PL+PC |
| `characters/aster.md` | YES | authoritative actor master, recovered partial | INCLUDE → target `characters/` | `PC-ASTER`; 赫茲 PL+PC |
| `characters/mileia.md` | YES | authoritative actor master, recovered partial | INCLUDE → target `characters/` | `PC-MILEIA`; 彌生 PL+PC; Lathander / 晨曦之主 + Life Domain are committed creation facts |
| `characters/nella.md` | YES | authoritative actor master, recovered partial | INCLUDE → target `characters/` | `PC-NELLA`; 蟬 PL+PC |
| `characters/ACTIVE_PC_MANIFEST.md` | YES, historical incident | stale recovery/integrity snapshot | DO NOT use as target current actor index; preserve only as migration evidence if desired | It still says Elian/Rook/Aster/Nella are missing although their actor files now exist |
| `characters/README.md` | NO campaign state | repo protocol/documentation | EXCLUDE | remains repo-level documentation |

## 1.1 Critical actor-master rule

All five current actor files are marked:

```text
authoritative_recovered_partial
```

This means migration may promote these records into the target campaign's actor namespace **without pretending they are original full creation sheets**.

Preserve:

```text
established fields
pending_recovery fields
provenance
controller mode
character_id
```

Do not regenerate missing build fields merely to make the target folder look complete.

### Mileia regression requirement

Target master must retain at minimum:

```text
character_id: PC-MILEIA
faith: Lathander / 晨曦之主
domain: Life / 生命領域
alignment: Neutral Good
```

These are creation-established facts, not post-hoc creative additions.

### Elian regression requirement

Target master must remain the actor authority for permanent build/background/equipment fields.

A live session containing values such as:

```text
Search 56
Bluff 54
HP/SP
```

is only runtime evidence/projection and must not shrink the actor master.

---

# 2. Session records

| Legacy record | Andor ownership | Authority | Migration action | Notes |
|---|---|---|---|---|
| `sessions/2026-09-16_session-1_live-state.md` | YES | CURRENT role-safe session pointer | INCLUDE as active live session | highest session authority for current actor positions / thread boundaries unless a later explicit record is found |
| `sessions/2026-09-15_session-1_checkpoint-01.md` | YES | historical resumable checkpoint | INCLUDE as historical session record | superseded for normal resume by later live state |
| `sessions/2026-09-15_session-1_runtime-migration.md` | YES | historical migration snapshot | INCLUDE as historical session record | earlier than checkpoint/live state; preserves PL+PC transition evidence |
| `sessions/README.md` | NO campaign state | repo protocol/documentation | EXCLUDE | remains repo-level documentation |

## 2.1 Current session authority

The active pointer is:

```text
sessions/2026-09-16_session-1_live-state.md
```

It establishes, among other things:

```text
four_voice_control = pl_pc
active_camera = none
Elian/Nella = paused after bard-academy departure
Rook = Mercenary Guild pending convoy thread
Aster = Mercenary Guild pending arcane-residue thread
Mileia = immediate post-guild-split actor boundary in this pointer
```

Older checkpoint/migration records must not overwrite later live-state changes merely because they contain more detail.

---

# 3. Legacy campaign/world records

| Legacy record | Andor ownership | Authority | Migration action | Notes |
|---|---|---|---|---|
| `campaign/andor_sites.md` | YES | authoritative Andor site-state bundle | INCLUDE → target `sites/` | stable site IDs + per-claim provenance |
| `campaign/andor_map_adoption.md` | YES | committed site/navigation claim-extension record | INCLUDE with site/adoption records | not a duplicate site database |
| `campaign/andor_public_map.md` | YES | player-safe projection | INCLUDE as projection/cache ref, NOT second world authority | derives from site state + map adoption |
| `campaign/andor_lathander_morninghall.md` | YES | committed post-rollback site/world record | INCLUDE → target `sites/`, with actor-pointer fuse | does not by itself prove Mileia arrived, observed, met Cael, or updated epistemic state |
| `campaign/current_state.md` | NO as Andor current state | stale generic placeholder | EXCLUDE from target current-state authority | still says “尚未建立實際 campaign” / no party |
| `campaign/house_rules.md` | no Andor-specific rule content | empty generic house-rule template | EXCLUDE as migrated state | target may initialize an empty campaign-specific house-rule record later if schema needs one |
| `campaign/README.md` | NO campaign state | repo documentation | EXCLUDE | remains repo-level documentation |

## 3.1 Root `campaign/current_state.md` is explicitly NOT Andor current state

It currently says:

```text
尚未建立實際 campaign
目前無角色檔
```

while the Andor live session and actor records clearly exist.

Therefore:

```text
campaign/current_state.md
!=
D100-TEST-ANDOR-001 current_state
```

Target `current_state` must be newly constructed from the latest valid Andor live-state + actor masters + valid Andor refs. It must not be copied from this placeholder.

---

# 4. Morninghall ordering / actor-pointer ambiguity

This is the main state-integrity issue found during Phase A.

Commit ordering:

```text
90caea20...  2026-09-16 00:43:27Z
Rollback Mileia thread to post-guild split boundary

fc868904...  2026-09-16 01:35:49Z
Establish Andor Lathander Morninghall
parent = 90caea20...
```

Therefore `campaign/andor_lathander_morninghall.md` is **not** the deleted pre-rollback south-care-node material. It was explicitly created *after* the rollback and marks the Morninghall/site/NPC data as committed.

However, that commit changed only the Morninghall site file; it did not update:

```text
sessions/2026-09-16_session-1_live-state.md
characters/mileia.md
```

So the safe migration interpretation is:

```text
Morninghall site/world record = INCLUDE as committed campaign world state
Mileia current actor position = keep latest live-state pointer
Mileia has visited Morninghall = NOT established by site creation alone
Mileia knows Cael = NOT established by site creation alone
Mileia gained local Morninghall knowledge = NOT established by site creation alone
```

This preserves the committed site without silently converting world existence into actor experience.

If later authoritative session evidence establishes that Mileia actually resumed and arrived there, Phase C/D may update the actor/session pointer explicitly. Until then, do not infer it from the site record.

---

# 5. Mystery records

The following root Mystery records are unambiguously Andor-owned by stable naming and/or live-state refs:

| Mystery record | Ownership | Migration action | Notes |
|---|---|---|---|
| `mystery_vault/ANDOR_BARD_ACADEMY_PATRON_01.md` | Andor | INCLUDE in target Mystery namespace / stable ref migration | payload not expanded during Phase A |
| `mystery_vault/ANDOR_BARD_HALL_DEPARTURE_01.md` | Andor | INCLUDE | directly referenced by current live state |
| `mystery_vault/ANDOR_BARD_HALL_OBSERVERS_01.md` | Andor | INCLUDE | directly referenced by current live state |
| `mystery_vault/ANDOR_SESSION1_CHECKPOINT_01.md` | Andor | INCLUDE as historical Mystery/session state | checkpoint-era record |
| `mystery_vault/ANDOR_SESSION1_MIGRATION.md` | Andor | INCLUDE | directly referenced by current live state |
| `mystery_vault/ANDOR_WHISPERS_CONTACT.md` | Andor | INCLUDE | directly referenced by current live state |
| `mystery_vault/README.md` | repo documentation | EXCLUDE | not campaign payload |

Phase A deliberately does **not** expand or duplicate protected payload.

Migration rule remains:

```text
move/reference exact Andor Mystery records
→ preserve classification / role-safe semantics
→ no plaintext parallel secret store
```

---

# 6. Repo source / dossier records — do not migrate

`sources/characters/` currently contains the separate operational/evidence set for characters such as:

```text
Adele
Kaland
Sathera
```

and `CURRENT_CAMPAIGN_STATUS.md` explicitly refers to that separate active trio plus missing Hansel.

It is not the Andor actor store.

Therefore:

```text
sources/characters/*
→ remain repo-level source/evidence/cache
→ DO NOT copy into Andor campaign characters/
```

The same exclusion applies to shared D100 source/rules:

```text
sources/sheet_mirror/
00_core/
01_skills/
02_items/
90_srd_bridge/
99_open_questions/
templates/
```

These remain referenced by ruleset/source resolution rather than duplicated into campaign storage.

---

# 7. Proposed target mapping — NOT YET EXECUTED

```text
campaign_instances/D100-TEST-ANDOR-001/
├── manifest.md
├── current_state.md                       # NEW synthesized pointer; do not copy legacy placeholder
├── characters/
│   ├── elian.md
│   ├── rook.md
│   ├── aster.md
│   ├── mileia.md
│   └── nella.md
├── sessions/
│   ├── 2026-09-15_session-1_runtime-migration.md
│   ├── 2026-09-15_session-1_checkpoint-01.md
│   └── 2026-09-16_session-1_live-state.md
├── sites/
│   ├── andor_sites.md
│   ├── andor_map_adoption.md
│   ├── andor_public_map.md                 # projection, not authority
│   └── andor_lathander_morninghall.md
├── relationships/
├── commitments/
└── mystery/
    └── exact Andor Mystery records / refs
```

Do not add `ACTIVE_PC_MANIFEST.md` as the new actor index. The new campaign manifest's `actor_index` replaces that role and must point to the five exact target actor records.

---

# 8. Phase B/C preconditions

Before any migration write begins:

```text
[PASS] five Andor actor masters identified
[PASS] latest Andor live-state identified
[PASS] historical session records classified
[PASS] stale root current_state excluded
[PASS] Andor site/map records identified
[PASS] Andor Mystery record ownership identified without payload duplication
[PASS] unrelated sources/characters campaign cache excluded
[PASS] Morninghall ordering issue identified and bounded
```

Remaining before cutover:

```text
- choose/pin migration ruleset.ref
- create target namespace + manifest
- copy/rewrite records without losing provenance
- synthesize target current_state from valid refs
- exact-ref readback of all five PC masters
- verify Mileia faith/domain survive reload
- verify Elian master is not shrunk by session projection
- verify Morninghall existence does not advance Mileia actor pointer without evidence
- verify Mystery refs resolve in target namespace
- fresh-load target campaign from manifest
```

---

# 9. Phase A decision

```yaml
phase: A_inventory
status: complete
safe_to_start_phase_B_namespace_build: true
safe_to_cutover: false
legacy_records_modified: false
andor_state_moved: false
```

Phase B may create a **new isolated target namespace**, but legacy root records should remain untouched until target readback regression passes.
