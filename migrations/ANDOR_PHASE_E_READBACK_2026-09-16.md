# Andor Persistent-Test Migration — Phase E Readback

> Status: PASS / TARGET SAVE VALID / NOT YET CUT OVER TO MAIN
>
> Campaign: `D100-TEST-ANDOR-001`
>
> This regression treats the target manifest as the only campaign entrypoint. Legacy root state remains present for audit but is not used as current authority.

---

## 1. Entry point

Fresh-load entry：

```text
campaign_instances/D100-TEST-ANDOR-001/manifest.md
```

Manifest readback established：

```yaml
campaign_id: D100-TEST-ANDOR-001
runtime_mode: persistent_test
party_mode: agent_pl_pc
world_resolution_mode: full
ruleset_ref: fc868904c4d9ded6d2f408ee25001dac5b2a70d5
write_scope: self_only
promotion_allowed: explicit_only
```

No root `campaign/current_state.md` or `characters/ACTIVE_PC_MANIFEST.md` was used to choose current state or actor masters.

---

## 2. Current-state readback

Exact manifest ref resolved：

```text
campaign_instances/D100-TEST-ANDOR-001/current_state.md
```

Recovered current boundaries：

```text
Elian   = bard-academy departure boundary
Nella   = with Elian at that departure boundary unless 蟬 later chooses otherwise
Rook    = Mercenary Guild; convoy thread pending
Aster   = Mercenary Guild; arcane-residue thread pending
Mileia  = latest live-state immediate post-guild-split actor boundary
active_camera = none
four_voice_control = pl_pc
```

Morninghall world existence is listed as a site ref but current state explicitly preserves：

```text
Morninghall exists
!= Mileia arrived there
!= Mileia met Cael
!= Mileia acquired local Morninghall knowledge
```

PASS.

---

## 3. Actor-master exact-ref readback

Manifest character index resolved all five actor masters by exact campaign-local ref.

| Character | Target blob SHA | Readback result |
|---|---|---|
| PC-ELIAN | `c92a75d4ebc8a72af1b31d24032c8e4975f0fe98` | PASS |
| PC-ROOK | `788d9fa20a1162f51b9b7f6c023fda4bf1162c34` | PASS |
| PC-ASTER | `ddf78a3ec2b7e5da8784467f34796260376dedf0` | PASS |
| PC-MILEIA | `495515aa9a824be579dd75abf62aec02663864f3` | PASS |
| PC-NELLA | `ea101165342766b1ccca2a6491cd50e0346fc5c5` | PASS |

These SHAs are byte-identical to the intended legacy actor masters. Migration did not regenerate or paraphrase character cards.

### Mileia critical regression

Exact target actor master directly recovered：

```text
faith = Lathander / 晨曦之主
domain = Life Domain / 生命領域
alignment = Neutral Good
record_status = authoritative_recovered_partial
```

No session reconstruction or chat memory was needed.

**PASS.**

### Elian critical regression

Exact target actor master retained：

```text
full established attribute/base/resistance block
Search 56
historical Sense Motive 54
Bluff 54
established equipment
established noble/bardic-family background
pending_recovery boundary
```

The live session does not replace this master with a small runtime projection.

**PASS.**

### PL+PC actor mapping

Readback confirmed：

```text
Rook   -> 鮫島 / LN / HP39 SP18 CP41
Aster  -> 赫茲 / NG / HP30 SP52 CP52
Mileia -> 彌生 / NG / HP20 SP35 CP15
Nella  -> 蟬 / CN / HP23 SP19 CP23
Elian  -> human player / CN / HP31 SP17 CP13
```

**PASS.**

---

## 4. Session collection readback

Target session collection contains exactly the intended Session 1 records：

```text
2026-09-15_session-1_runtime-migration.md
2026-09-15_session-1_checkpoint-01.md
2026-09-16_session-1_live-state.md
```

Their copied blob SHAs match legacy source records.

Authority ordering remains：

```text
active live-state
> checkpoint for normal resume
> runtime-migration snapshot
```

**PASS.**

---

## 5. Site collection readback

Target site collection contains：

```text
andor_sites.md
andor_map_adoption.md
andor_public_map.md
andor_lathander_morninghall.md
```

All four target blob SHAs match the intended legacy records.

`andor_sites.md` uses repo-level D100 source refs and Secret IDs; it does not require legacy root mutable-state fallback.

**PASS.**

---

## 6. Mystery collection existence / identity readback

Without expanding protected payload, target collection existence and blob identity were verified for：

```text
ANDOR_BARD_ACADEMY_PATRON_01.md
ANDOR_BARD_HALL_DEPARTURE_01.md
ANDOR_BARD_HALL_OBSERVERS_01.md
ANDOR_SESSION1_CHECKPOINT_01.md
ANDOR_SESSION1_MIGRATION.md
ANDOR_WHISPERS_CONTACT.md
```

Target SHAs match the intended legacy Mystery records.

This test verifies storage identity/existence only; it does not weaken Mystery classification or claim HARD_EX isolation.

**PASS.**

---

## 7. Legacy ref alias closure

The byte-identical active live-state still contains historical legacy mutable-state refs. Manifest uses：

```yaml
ref_alias_policy: exact_only
```

Every runtime-relevant mutable-state ref in the active live-state has an exact alias into the selected target namespace：

```text
sessions/2026-09-15_session-1_checkpoint-01.md
sessions/2026-09-15_session-1_runtime-migration.md
campaign/andor_sites.md
campaign/andor_map_adoption.md
campaign/andor_public_map.md
mystery_vault/ANDOR_SESSION1_MIGRATION.md
mystery_vault/ANDOR_WHISPERS_CONTACT.md
mystery_vault/ANDOR_BARD_HALL_OBSERVERS_01.md
mystery_vault/ANDOR_BARD_HALL_DEPARTURE_01.md
characters/mileia.md
```

The deleted/void audit path：

```text
campaign/andor_south_care_node.md
```

has intentionally **no alias** and cannot be restored through fallback.

Repo-level source refs under `sources/`, `00_core/`, `90_srd_bridge/` remain source lookups and are not campaign aliases.

**PASS.**

---

## 8. Cross-campaign/root contamination fuses

Verified target load path uses：

```text
manifest exact actor index
current_state target refs
active-session exact ref
exact legacy alias map for migrated mutable state
```

It does not require：

```text
global same-name actor search
root campaign/current_state.md
stale characters/ACTIVE_PC_MANIFEST.md
sources/characters/CURRENT_CAMPAIGN_STATUS.md
```

`source/characters/CURRENT_CAMPAIGN_STATUS.md` belongs to the separate Sathera/Adele/Kaland/Hansel evidence/cache context and is not imported into Andor.

**PASS.**

---

## 9. Fresh-load result

```yaml
manifest_readback: PASS
current_state_readback: PASS
all_five_actor_exact_refs: PASS
mileia_faith_domain: PASS
elian_master_not_shrunk: PASS
pl_pc_mapping: PASS
session_authority_order: PASS
site_collection: PASS
mystery_record_identity: PASS
legacy_ref_alias_closure: PASS
morninghall_actor_pointer_fuse: PASS
root_legacy_not_current_authority: PASS
chat_memory_required: false
```

---

## 10. Migration status after Phase E

```yaml
phase_A_inventory: PASS
phase_B_namespace_build: PASS
phase_C_actor_master_verification: PASS
phase_D_ref_closure: PASS
phase_E_fresh_load: PASS
storage_valid: true
ready_for_explicit_cutover: true
legacy_root_delete_allowed: false
main_merge_performed: false
```

The target campaign storage is now valid enough to be marked initialized/clean **inside the feature branch**.

That does not automatically select it in another chat, merge the bootstrap branch to `main`, or authorize legacy-root cleanup. Those remain explicit later operations.
