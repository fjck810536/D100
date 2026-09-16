# Session 1 — Andor / Grey Antler — Checkpoint 01

> SAVE POINT / resumable checkpoint.
>
> This checkpoint supersedes the earlier migration snapshot for normal session resume. It preserves role-safe state only; hidden payload remains in Mystery Vault refs.

```yaml
session_id: D100-TEST-ANDOR-001
date: 2026-09-15
checkpoint: 01
scene: Grey Antler regroup after Nella tail
in_combat: false
round: null
world_time: Day 1 afternoon, roughly 8-10 minutes after Nella left Grey Antler; exact clock unset
four_voice_control:
  mode: pl_pc
  mappings:
    - 鮫島 -> Rook
    - 赫茲 -> Aster
    - 彌生 -> Mileia
    - 蟬 -> Nella
```

---

## 1. Current scene / locations

All five PCs are back at the Grey Antler table.

- Elian returned from the rear / privy direction, dropped the fake-drunk act, resumed normal conversation.
- Rook remains at the table.
- Aster remains at the table and is considering visiting the mercenary guild with Rook instead of approaching John Academy immediately.
- Mileia remains at the table; she is still inclined to find a temple / medical institution later.
- Nella returned from the tail and reported what she actually observed.
- Oren Pell is no longer in the tavern and is somewhere in the merchant district; exact hidden state is Mystery-gated.

No external confrontation, alarm, or combat is active at the save point.

---

## 2. Secret / commitment refs

```yaml
secret_refs:
  - SECRET-ANDOR-001
commitment_refs:
  - COMMIT-ANDOR-ACTOR-001
  - COMMIT-ANDOR-ECON-001
  - COMMIT-ANDOR-SILVERCOINS-001
  - mystery_vault/ANDOR_SESSION1_CHECKPOINT_01.md
```

Role-safe summary:

- missing copyist / blue-wax box / Academy special-collection restriction retain their committed hidden causal core;
- Oren's previously committed report-route has now produced a world-state update;
- spell-material price rise remains independent;
- Three Silver Coins confidential clerical job remains independent.

---

## 3. Character control / Alignment

| Actor | Control | Alignment | Status |
|---|---|---|---|
| Rook | 鮫島 PL+PC | Lawful Neutral | ratified |
| Aster | 赫茲 PL+PC | Neutral Good | ratified |
| Mileia | 彌生 PL+PC | Neutral Good | ratified |
| Nella | 蟬 PL+PC | Chaotic Neutral | ratified |
| Elian | human-player PC | Chaotic Neutral | player-declared / ratified |

```text
alignment ≠ presented_persona ≠ current_affect ≠ actual_action
```

No Alignment drift score exists.

---

## 4. PC live resources

| PC | HP | SP | CP reserve after checkpoint award | Location / state |
|---|---:|---:|---:|---|
| Rook | 39/39 | 18/18 | 41 | Grey Antler table; no active effect |
| Aster | 30/30 | 52/52 | 52 | Grey Antler table; cautious about Academy approach |
| Mileia | 20/20 | 35/35 | 15 | Grey Antler table; no active effect |
| Nella | 23/23 | 19/19 | 23 | Grey Antler table; tail completed |
| Elian | 31/31 | 17/17 | 13 | Grey Antler table; 45 gp |

### Checkpoint CP award — `[GM_PROVISIONAL]`

No canonical fixed save-point CP formula was found in the current repo. This checkpoint uses a conservative situational award and records it as a calibration sample rather than a universal rule.

| PC | CP before | Award | CP after | Scene basis |
|---|---:|---:|---:|---|
| Elian | 10 | +3 | 13 | initiated investigation, maintained social cover, coordinated warning / follow-up |
| Nella | 20 | +3 | completed a restrained tail and returned actionable observations without escalation |
| Aster | 50 | +2 | maintained cover, handled improvised cloak transfer, adapted plan under uncertainty |
| Rook | 40 | +1 | maintained cover and practical group stability |
| Mileia | 14 | +1 | maintained cover and social stability |

These awards are granted and should not disappear merely because the future calibration rule changes. Future checkpoints may use a revised scale once the GM convention is clarified.

---

## 5. Item state

### ITEM-ELIAN-CLOAK-001

```yaml
owner: Elian
holder: Elian
uses_per_day: 3
used_today: 0
remaining: 3
active: false
checkpoint_note: Nella returned the cloak after the tail; it was never activated
```

Activation / duration / borrower interface remains unresolved.

### ITEM-ELIAN-RING-001

```yaml
owner: Elian
holder: Elian
uses_per_day: 3
used_today: 0
remaining: 3
```

Dimension Door; range / targets / activation unresolved.

### ITEM-ELIAN-BOOTS-001

Air-walk >=3h/day; unused today; duration splitting / activation unresolved.

### Money

Elian: **45 gp**.

---

## 6. Roll ledger

| Roll | Interface | Target | d100 | Result | Consequence |
|---|---|---:|---:|---|---|
| ROLL-001 | Elian Search board | 56 | 57 | fail by 1 | weak / non-confirming observation only |
| ROLL-002 | Elian Sense Motive / reaction read | 54 | 48 | success +6 | suspicious-man reaction pattern observed |
| ROLL-003 | Elian Bluff / fake-drunk cover | 54 | 16 | success +38 | cover works; private warning delivered |
| ROLL-004 | Nella tail / concealment route `[RUNTIME_PROVISIONAL]` | 103 | 14 | success +89 | clean initial tail; target not positively aware of her |

`ROLL-004` is preserved as actual session history. The exact skill-stacking interface should not be generalized beyond this resolved event without source confirmation.

---

## 7. Evidence Ledger

Previously established:

| ID | Proposition | Status |
|---|---|---|
| EVID-ANDOR-001 | Academy-related male copyist, 21, missing five days; reward 20 gp | OBSERVED |
| EVID-ANDOR-002 | blue-wax sealed document box reward changed 15 -> 40 gp | OBSERVED |
| EVID-ANDOR-003 | special collections recently require internal introduction | OBSERVED |
| EVID-ANDOR-004 | several low-level spell-material prices rose, some around +30% | OBSERVED |
| EVID-ANDOR-005 | confidential documents/accounts job at Three Silver Coins | OBSERVED |
| EVID-ANDOR-006 | missing-copyist and box notices have similar-looking fresh timing/ink | OBSERVED, weak note |
| EVID-ANDOR-007 | Grey Antler man paused subtly at missing-copyist topic | OBSERVED |
| EVID-ANDOR-008 | same man reacted subtly to 40 gp box topic | OBSERVED |
| EVID-ANDOR-009 | same man looked once at Aster | OBSERVED |

New from Nella's completed tail and report to the table:

| ID | Proposition | Status | Observed by |
|---|---|---|---|
| EVID-ANDOR-010 | target traveled from Grey Antler toward the merchant district | OBSERVED | Nella; later reported to group |
| EVID-ANDOR-011 | target entered a commercial message / document-handling office carrying a folded paper | OBSERVED | Nella; later reported to group |
| EVID-ANDOR-012 | target exited that office without the folded paper | OBSERVED | Nella; later reported to group |
| EVID-ANDOR-013 | target then entered another commercial office building | OBSERVED | Nella; later reported to group |
| HYP-ANDOR-004 | second building may be the target's normal workplace | INFERRED | Nella; shared with group as an inference |

Do **not** promote the following to player fact at this checkpoint:

- exact identity of either office;
- recipient or wording of the folded note;
- whether the note was a report about the party;
- Oren's employer / true role.

---

## 8. Actor epistemic state

### Elian

Knows the earlier public evidence, suspicious-man reactions, and Nella's full player-visible tail report (EVID-ANDOR-010..013 + HYP-ANDOR-004). Does not know the target's hidden identity/employer or message content.

### Aster

Knows he was privately warned someone had watched him; knows Academy access anomaly and spell-material anomaly; now also knows Nella's reported tail observations. He is considering delaying direct Academy contact and checking mercenary work with Rook.

### Rook

Knows the group was running a cover around the suspicious stranger; knows Nella tailed him and returned with merchant-district observations. Does not know hidden causal truth.

### Mileia

Knows the same broad cover context and Nella's returned report. Does not know hidden causal truth.

### Nella

Knows everything she directly observed on the tail plus the prior improvised signal context. Does not know exact office identities, message content, or hidden truth.

---

## 9. Relationship fact updates

Existing relationship facts remain valid.

New objective facts:

- `REL-007`: Nella used Elian's entrusted cloak as carried equipment only; she did not activate it and returned it after the tail.
- `REL-008`: Nella voluntarily reported the tail observations to the group after returning.
- `REL-009`: Aster and Rook discussed potentially visiting the mercenary guild together after the meal; this is a current plan candidate, not a binding contract.

No automatic facts are created for trust, romance, loyalty, or friendship depth.

---

## 10. Player Layer / current intentions

### 鮫島 → Rook

Current intention: willing to go to the mercenary guild after the meal; does not assume party leadership.

### 赫茲 → Aster

Current intention: willing to inspect mercenary-guild work with Rook; does not commit to accepting a job yet; prefers not to approach John Academy immediately.

### 彌生 → Mileia

Current intention: later seek a temple / medical institution; currently prefers not to split before Nella's report is absorbed. At checkpoint the report has arrived, so next destination remains open to fresh decision.

### 蟬 → Nella

Tail objective completed. Current next action is unset; she has returned to the group and relinquished the cloak.

---

## 11. Open questions / temporary rulings active at checkpoint

- `P0-CREATE-1` qualifying melee/spell CP classification unresolved.
- `P1-SOCIAL-1` Alignment / behavior drift ledger design unresolved; no hidden drift score.
- `P0-RUNTIME-1` Sense Motive source/interface unresolved.
- `P0-RUNTIME-2` special magic-item activation/duration/transfer interface unresolved.
- `P1-RUNTIME-1` improvised nonverbal communication interface unresolved.
- `P1-RUNTIME-2` investigation failure / incomplete-information boundary unresolved.
- `P2-RUNTIME-1` coarse world time -> exact clock commitment unresolved.
- checkpoint CP award scale/cadence is currently `[GM_PROVISIONAL]` and should be formalized if repeated.

---

## 12. Save-point state / next resume

Resume from the Grey Antler table **after Nella has returned and finished reporting**.

The party has not yet chosen a unified next destination.

Current visible options include, but are not limited to:

- Rook + Aster visiting the mercenary guild;
- Mileia seeking temple / medical contacts;
- investigating one or both merchant-district locations from Nella's tail;
- contacting Three Silver Coins;
- approaching John Academy later or indirectly;
- ordinary lodging / supplies / independent errands.

Do not force these hooks into one plot.

```text
SAVE POINT 01 COMPLETE
```
