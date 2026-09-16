# Andor Persistent-Test Migration Plan

> Status: PHASE B STAGING IN PROGRESS — NO CUTOVER.
>
> 目的：把目前散落在 repo root legacy `campaign/`、`characters/`、`sessions/`、`mystery_vault/` 的 Andor 測試團，安全搬成一個完整、可重掛載、與其他團隔離的 `persistent_test` campaign instance。
>
> Phase A inventory 已完成：`migrations/ANDOR_PHASE_A_INVENTORY_2026-09-16.md`。
>
> Target namespace 可以在 feature branch staging，但在 Phase E fresh-load regression 通過前，不得宣告 cutover，也不得刪除／覆寫 legacy root records。

## 0. Target

預定 target semantics：

```yaml
campaign_id: D100-TEST-ANDOR-001
runtime_mode: persistent_test
storage:
  backend: repo
  root_ref: campaign_instances/D100-TEST-ANDOR-001
  write_scope: self_only
  promotion_allowed: explicit_only
```

Migration staging pins the effective ruleset to the current `main` state at branch divergence:

```text
fc868904c4d9ded6d2f408ee25001dac5b2a70d5
```

This preserves the campaign's existing rules/source state while the bootstrap/storage architecture is developed on a feature branch. Storage architecture changes are not treated as silent game-rule upgrades.

---

## 1. Why migration is needed

目前 legacy root state 存在已知完整性問題：

```text
campaign/current_state.md
→ 仍描述「尚未建立實際 campaign」且不是 Andor current state

sessions/*
→ 實際保存 Andor live state / checkpoints / migration snapshots

characters/*
→ 五名 Andor PC 均已有 recovered-partial actor masters
→ 舊 ACTIVE_PC_MANIFEST 已過時，只能作 recovery-incident evidence

campaign/andor_*
→ 保存 Andor site/map state

mystery_vault/ANDOR_*
→ 保存 Andor Mystery records
```

因此 migration 不能採：

```text
copy root folders wholesale
```

而要依 Phase A inventory 逐 record 處理。

---

## 2. Known Andor actor set

Target actor set：

```text
Elian / PC-ELIAN
Rook / PC-ROOK
Aster / PC-ASTER
Mileia / PC-MILEIA
Nella / PC-NELLA
```

All five current actor masters are `authoritative_recovered_partial`.

Migration must preserve both:

```text
established facts
pending_recovery boundaries
```

### Critical recovery regressions

Mileia：

```text
faith = Lathander / 晨曦之主
domain = Life / 生命領域
```

must be available from target actor master without session reconstruction.

Elian：

- target actor master remains the permanent build/background authority;
- session Search / Bluff / HP / SP values are live/runtime evidence, not a replacement card;
- `pending_recovery` fields remain pending rather than being regenerated.

---

## 3. Phase A — Inventory complete

Authoritative inventory：

```text
migrations/ANDOR_PHASE_A_INVENTORY_2026-09-16.md
```

Key decisions already established：

```text
characters/ACTIVE_PC_MANIFEST.md
→ historical stale recovery snapshot, not target actor index

campaign/current_state.md
→ generic stale placeholder, EXCLUDE as Andor current state

sources/characters/*
→ unrelated repo-level evidence/cache, do not migrate as Andor actors

campaign/andor_lathander_morninghall.md
→ committed post-rollback site record
→ does not by itself advance Mileia actor position/knowledge/contact
```

---

## 4. Phase B — Build target namespace

Target：

```text
campaign_instances/D100-TEST-ANDOR-001/
├── manifest.md
├── current_state.md
├── characters/
├── sessions/
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

Phase B staging rules：

```text
legacy records remain untouched
actor/session/site/Mystery files may reuse exact existing blob content
new manifest/current_state are staging pointers
manifest initialized=false until readback regression
cutover=false
```

Staging `current_state.md` is synthesized from valid actor/live/site refs. It must not copy root `campaign/current_state.md`.

### Morninghall fuse

`SITE-ANDOR-LATHANDER-MORNINGHALL` may exist in target world state because it was committed after the rollback.

But until explicit later actor/session evidence exists:

```text
Morninghall exists
!= Mileia arrived there
!= Mileia met Cael
!= Mileia knows local Morninghall facts
```

---

## 5. Phase C — Actor-master verification

After target namespace exists：

```text
manifest indexes.characters
→ exact target actor ref
→ read five actor masters
```

Verify：

- exact `character_id` matches manifest index；
- source and target recovered-partial actor blobs/content are unchanged unless migration explicitly edits refs only；
- Mileia faith/domain intact；
- Elian actor master retains established background/items/check data and pending recovery boundaries；
- controllers / PL+PC mappings intact；
- no actor master is reconstructed from session prose.

---

## 6. Phase D — Current world/session pointer normalization

Target active state should derive from：

```text
latest valid Andor live-state
+ target actor masters
+ target site refs
+ target Mystery refs
```

Historical checkpoint/migration snapshots remain historical.

Any copied active live-state / site projection that still points to legacy root campaign paths must be normalized or resolved through explicit migration refs before cutover. Legacy path provenance may remain as history, but current runtime pointers must resolve inside the selected campaign namespace where appropriate.

---

## 7. Phase E — Readback regression

Close migration working assumptions and reload from only：

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
```

Then：

```text
manifest
→ current_state
→ exact PC masters
→ active live session
→ sites / relationship / commitment / Mystery-safe refs
```

Required regressions：

- Mileia faith/domain directly available from actor master；
- Elian does not shrink to session projection；
- Nella / Rook / Aster control mode and established actor state recover；
- active camera / thread boundaries / HP/SP/CP do not roll backward；
- Morninghall world existence does not silently move Mileia；
- target refs do not accidentally load another campaign；
- Mystery role-safe refs resolve normally；
- no runtime dependency on chat memory.

---

## 8. Phase F — Cutover

Only after Phase E passes：

```text
mark manifest bootstrap initialized=true
mark persistence clean
record readback verification
→ declare D100-TEST-ANDOR-001 selected campaign root
```

Legacy root records remain initially for audit/history and may later be marked superseded/migrated. Cleanup is a separate explicit decision.

---

## 9. Explicit non-goals

Migration does not：

- reroll historical checks；
- recreate player-unchosen character facts；
- turn recovered partial cards into fake original full sheets；
- promote Andor to a formal main campaign；
- clean unrelated legacy test data；
- alter D100 combat/mechanical rules；
- alter Mystery classification to simplify storage；
- infer actor experience from site existence.

---

## 10. Stop conditions

Stop before cutover if：

```text
latest Andor live-state cannot be uniquely identified
actor master conflicts with later established session facts
manifest/record refs cannot be re-read
write/readback verification fails
Mystery ownership is ambiguous
legacy record may belong to another campaign
current target still depends on ambiguous global search
```

Do not solve ambiguity by picking the newest-looking file.

---

## 11. Success condition

```text
new chat / new agent
→ read D100 repo
→ choose Load Game
→ resolve target manifest
→ load exact actor masters + current state + live session
→ resume Andor without chat memory
```

and simultaneously：

```text
another campaign namespace can coexist
→ no Andor actor/site/Mystery state crosses into it
```

Only then is migration complete.
