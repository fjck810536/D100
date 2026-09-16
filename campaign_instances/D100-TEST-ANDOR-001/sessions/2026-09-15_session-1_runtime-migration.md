# Session 1 — Andor / Grey Antler Runtime Migration Snapshot

> 狀態：LIVE TEST SESSION / runtime migration snapshot。
>
> 本檔保存目前真的成立的 role-safe session state。這不是正式 campaign 升格；`campaign/current_state.md` 仍可保持未建立正式 campaign。
>
> Hidden truth 不複製於此；使用 `secret_refs` / `commitment_refs` 連到 Mystery Vault。

```yaml
session_id: D100-TEST-ANDOR-001
date: 2026-09-15
scene: Grey Antler split scene / tail setup
in_combat: false
round: null
world_time: Day 1 afternoon, exact clock unset
runtime_migration_boundary: after Oren Pell exits Grey Antler, before Nella tail resolution

four_voice_control:
  mode: pl_pc
  switched_at: out_of_scene_card_check_before_tail_resolution
  mappings:
    - 鮫島 -> Rook
    - 赫茲 -> Aster
    - 彌生 -> Mileia
    - 蟬 -> Nella
```

## Migration / control note

此前由 DM 直接生成的 Rook / Aster / Mileia / Nella 行為，全部保留為已發生的 **NPC-mode actual actions**；不得事後回填成四聲部 Player choice。

從本次場外宣告起，四聲部切換為 `pl_pc`。之後相關決策必須走：

```text
Player Voice
→ Player decision
→ PC interpretation / declaration
→ DM resolution
```

四名 Player Voice 已對 migration alignment 做第一次 ratification：

```text
鮫島 / Rook   → Lawful Neutral   RATIFIED
赫茲 / Aster  → Neutral Good     RATIFIED
彌生 / Mileia → Neutral Good     RATIFIED
蟬 / Nella    → Chaotic Neutral  RATIFIED
```

Alignment 仍不是行動腳本；若角色經長期劇情發展發生倫理／秩序取向轉變，應以顯式角色發展事件更新。

---

# 1. 當前場景

## 地點 / split state

- Elian：Grey Antler 後院／廁所方向。
- Rook：Grey Antler 餐桌。
- Aster：Grey Antler 餐桌。
- Mileia：Grey Antler 餐桌。
- Nella：已離開 Grey Antler，落後 Oren Pell 約 5–6 秒，尚未結算尾隨。
- Oren Pell：已離店，正在執行既有 next-step commitment。

## 可感知場景基線

Grey Antler 是安道爾南區普通但乾淨的旅店／餐館：熱食、黑麵包、酒、往來工人／旅人／低階辦事者；距 Three Silver Coins 正常步行約 10–15 分鐘。

---

# 2. Secret / Commitment refs

```yaml
secret_refs:
  - SECRET-ANDOR-001
commitment_refs:
  - COMMIT-ANDOR-ACTOR-001
  - COMMIT-ANDOR-ECON-001
  - COMMIT-ANDOR-SILVERCOINS-001
```

Role-safe summary：

- missing copyist / blue-wax box / Academy special-collection restriction now have a committed hidden causal core;
- spell-material price rise has an independent committed economic cause;
- Three Silver Coins confidential clerical job has an independent committed employer/problem core;
- suspicious-man identity / knowledge / intended next step are fixed before tail resolution.

---

# 3. Character control / alignment

| Actor | Current control | Alignment | Status |
|---|---|---|---|
| Rook | 鮫島 PL+PC | Lawful Neutral | ratified |
| Aster | 赫茲 PL+PC | Neutral Good | ratified |
| Mileia | 彌生 PL+PC | Neutral Good | ratified |
| Nella | 蟬 PL+PC | Chaotic Neutral | ratified |
| Elian | human-player PC | Chaotic Neutral | player-declared / ratified |

```text
alignment ≠ presented_persona ≠ current_affect ≠ actual_action
```

---

# 4. Player Layer

> Player Layer 是 meta working data，不是 PC 內心。以下只保存各 Player Voice 對自己 PC 的玩法解讀與目前決策權；可隨遊戲發展修正。

## 鮫島 → Rook

```yaml
agenda:
  - keep Rook grounded in practical road / guard experience
  - do not force leadership merely because he is the fighter
current_interest:
  - understand whether the group is becoming worth staying with
  - keep track of practical risk while others investigate
risk_tolerance: moderate
interpretation_of_pc:
  - values duty, contracts, order, and competent procedure
  - may break from authority if authority loses practical legitimacy, but does not romanticize disorder
current_decision:
  - remain at Grey Antler table for the moment; do not interfere with Nella's tail until new information returns
```

## 赫茲 → Aster

```yaml
agenda:
  - play Aster as a real scholar, not an exposition terminal
  - let curiosity compete with caution
current_interest:
  - understand why Academy access changed
  - find out why he drew attention without walking blindly into Academy
risk_tolerance: low_to_moderate
interpretation_of_pc:
  - fundamentally decent and knowledge-seeking
  - prefers evidence before escalation
current_decision:
  - stay put, preserve cover, and avoid visibly reacting to being watched
```

## 彌生 → Mileia

```yaml
agenda:
  - keep care, medicine, and social presence active without turning into party-mother autopilot
  - notice who is being harmed, frightened, or excluded
current_interest:
  - make sure the table does not turn suspicion into reckless harm
  - understand the group's emerging bonds without forcing intimacy
risk_tolerance: moderate_when_someone_needs_help
interpretation_of_pc:
  - good-oriented, care-first, but not institutionally rigid
  - faith is part of her life rather than a command menu
current_decision:
  - remain with Rook and Aster and maintain normal social cover
```

## 蟬 → Nella

```yaml
agenda:
  - play through gaps, omissions, routes, doors, and people who do not want to be noticed
  - do not magically understand every hint or become a flawless spy
current_interest:
  - test whether the departing man actually leads somewhere useful
  - preserve plausible deniability and avoid escalating a weak clue into a confrontation
risk_tolerance: moderate_high_for_information, low_for_pointless_exposure
interpretation_of_pc:
  - independent, opportunistic, gray-work comfortable, not malicious by default
  - values freedom of movement and information more than institutional legitimacy
current_decision:
  - attempt to acquire and maintain the tail; cloak remains unused unless a later Player decision activates it through a resolved interface
```

---

# 5. PC / actor live resources

| Actor | HP | SP | Current location | Important live resource/state |
|---|---:|---:|---|---|
| Rook | 39/39 | 18/18 | Grey Antler table | no active effect |
| Aster | 30/30 | 52/52 | Grey Antler table | warned that someone watched him |
| Mileia | 20/20 | 35/35 | Grey Antler table | no active effect |
| Nella | 23/23 | 19/19 | outside Grey Antler | holds Elian invisibility cloak, not activated |
| Elian | 31/31 | 17/17 | rear / privy direction | 45 gp; cloak temporarily out of possession |

---

# 6. Evidence Ledger

| Evidence ID | Proposition | Status | Observed by | Notes |
|---|---|---|---|---|
| EVID-ANDOR-001 | John Academy-related male copyist, 21, missing for five days; reward 20 gp | OBSERVED | Elian + anyone who read board | public notice |
| EVID-ANDOR-002 | blue-wax sealed document box reward changed 15 -> 40 gp | OBSERVED | Elian + board readers | public notice |
| EVID-ANDOR-003 | John Academy special collections recently require internal introduction | OBSERVED | Elian + board readers | public notice |
| EVID-ANDOR-004 | several low-level spell-material buy prices rose, two around +30% | OBSERVED | Elian + board readers | public notice / market |
| EVID-ANDOR-005 | confidential documents/accounts job meets at Three Silver Coins | OBSERVED | Elian + board readers | public notice |
| EVID-ANDOR-006 | missing-copyist notice and box notice have similar-looking fresh date ink / timing | OBSERVED_WEAK | Elian | Search 56 vs d100 57 near-fail; cannot confirm shared issuer |
| EVID-ANDOR-007 | Grey Antler man paused subtly at missing-copyist topic | OBSERVED | Elian | Sense Motive success |
| EVID-ANDOR-008 | same man reacted subtly to 40 gp box topic | OBSERVED | Elian | Sense Motive success |
| EVID-ANDOR-009 | same man looked once at Aster | OBSERVED | Elian | reason unknown to PCs |
| HYP-ANDOR-001 | copyist / box / special-collection restriction may be connected | INFERRED | Elian | not confirmed in player view |
| HYP-ANDOR-002 | spell-material price rise belongs to same incident | INFERRED/LOW | possible table speculation | no confirming evidence |
| HYP-ANDOR-003 | Three Silver Coins job belongs to same incident | UNSUPPORTED | none | keep separate from evidence graph |

> `OBSERVED_WEAK` is migration notation only; canonical Evidence Ledger status remains OBSERVED, with weakness in notes.

---

# 7. Actor Epistemic Matrix

## Elian

Known / observed：EVID-ANDOR-001..009 as personally encountered, except details he did not directly inspect may be conversationally shared.

Beliefs / active hypotheses：HYP-ANDOR-001; considers Academy approach risky; recognizes suspicious man as worth tracking.

Does not know：hidden truth of SECRET-ANDOR-001, Oren's identity/employer, whether Nella will keep tail.

## Aster

Known：spell-material price anomaly; Academy access restriction; Elian privately warned him "你被人盯上了"; Elian advised delaying Academy approach.

Belief：someone in Grey Antler may have taken interest in him / the table.

Does not know：why, target identity, hidden case truth.

## Rook

Known：Elian was performing a cover act; table is handling some suspicious situation; Nella left after target left.

Does not automatically know Elian–Aster whispered wording or hidden causal truth.

## Mileia

Known：same broad cover-action context; Nella left; table is dealing with a potentially suspicious stranger.

Does not automatically know full whispered warning.

## Nella

Known：Elian's signaling indicated the departing man as a target worth following; she has Elian's cloak; the man left shortly before her.

Does not know：cloak activation rules; Oren's true identity; hidden case truth.

## Oren Pell

Actor epistemic state is Mystery-gated; session only records that he has case-relevant prior knowledge and a committed next step.

---

# 8. Relationship Fact Updates

Objective facts only:

- REL-001: all five shared farmer-wagon travel into Andor.
- REL-002: all five shared a Grey Antler meal; Elian paid 4 gp.
- REL-003: group discussed Three Silver Coins as a possible later rendezvous.
- REL-004: Elian privately warned Aster that Aster had been watched.
- REL-005: Elian entrusted invisibility cloak into Aster's hands; Aster transferred holder-state to Nella in context of the improvised signal.
- REL-006: Nella independently left Grey Antler after the suspicious man; tail attempt pending.

Not objective facts："trust", "romantic interest", "loyalty", "friendship depth". Those require actor state / player statement / derived analysis.

---

# 9. Roll Ledger

| Roll | Interface | Target | d100 | Result | State consequence |
|---|---|---:|---:|---|---|
| ROLL-001 | Elian Search board | 56 | 57 | fail by 1 | weak/non-confirming observation only |
| ROLL-002 | Elian Sense Motive / reaction read | 54 | 48 | success +6 | Oren reaction pattern observed |
| ROLL-003 | Elian Bluff / drunk cover | 54 | 16 | success +38 | cover act works; private warning delivered |

No tail roll has yet occurred.

---

# 10. Item state

## ITEM-ELIAN-CLOAK-001

```yaml
owner: Elian
holder: Nella
uses_per_day: 3
used_today: 0
remaining: 3
active: false
```

Known effect：invisibility.

Open rules：activation, duration, sharing/attunement assumptions remain unresolved; holder ≠ user competence.

## ITEM-ELIAN-RING-001

```yaml
owner: Elian
holder: Elian
uses_per_day: 3
used_today: 0
remaining: 3
```

Dimension Door; range / targets / activation unresolved.

## ITEM-ELIAN-BOOTS-001

Air-walk >=3h/day; unused today; duration splitting / activation unresolved.

## Money

Elian: 50 gp start -> -1 gp wagon -> -4 gp Grey Antler meal = **45 gp**.

---

# 11. Human Player meta record

Explicitly established player/runtime preferences in this test:

- wants D100 rather than D&D/CoC substitution;
- wants unnecessary rolls minimized;
- wants world state and secret causality to exist independently of player discovery;
- wants modules tightly coupled through clean shared data, not parallel truths;
- accepts four voices as high-quality NPCs by default, but expects genuine PL+PC layer when explicitly requested;
- wants Alignment available to Analyst without turning Alignment into compulsory acting behavior;
- prefers live migration over restarting this session.

Derived gameplay tendencies may be recorded separately, but must remain revocable and must not be written into Elian's PC psychology.

---

# 12. Module status

- AO: ACTIVE; must resolve future world evolution from committed state, not desired plot outcome.
- Librarian: ACTIVE / provenance gateway; resolves rules and relationship/evidence history.
- Mind-reader: LOW / meta-only; may hypothesize human-player intent, never PC truth.
- Accountant: ACTIVE; tracks Elian money, cloak holder/owner split, item charges.
- Stopwatch: ACTIVE for the 5–6 second departure gap and upcoming tail timing.
- Hourglass: ACTIVE coarse world time; exact city clock still unset.
- Ecologist: LOW; available for lived behavior / environmental constraints.
- Politician: AVAILABLE; current city/faction consequences not yet strong enough to force active forecast.
- Analyst: AVAILABLE; Alignment input is ratified for four PL+PC actors; Elian is now player-declared Chaotic Neutral. Derived relationship/alignment analysis may use declared Alignment without turning it into an action script.
- Mystery: ACTIVE; SECRET-ANDOR-001 + commitment refs exist before tail resolution.
- Orchestrator: ACTIVE; PL+PC switch is now authoritative session control state.
- Character Builder / Build Ledger: SUSPENDED runtime service; unresolved qualifying CP remains technical debt, not active scene blocker.

---

# 13. Open rules / technical debt

- P0-CREATE-1 qualifying melee/spell CP exact classification remains unresolved.
- P1-SOCIAL-1 Alignment / behavior drift ledger design is tracked in `99_open_questions/social_world.md`; no hidden drift score exists yet.
- Elian cloak activation / duration unresolved; now high runtime priority because Nella holds it.
- Dimension Door ring range/targets/activation unresolved.
- Air-walk boots duration splitting unresolved.
- exact world clock unset.
- communication-by-improvised-signal has no formal universal check rule; prior understanding remains an actual event, not a new general rule.
- near-fail Search clue treatment remains DM_DEFAULT-style incomplete-information consequence, not a newly invented universal partial-success mechanic.

---

# 14. Next pending event

```text
Nella leaves Grey Antler ~5–6 seconds after Oren Pell.
Oren's pre-tail identity / knowledge / goal / intended next step are committed.
Oren has not yet identified Nella as a tail at the migration boundary.
蟬 has declared the Player decision: acquire and maintain the tail without pointless exposure.
Next DM resolution may determine whether Nella acquires, keeps, loses, or exposes the tail — but cannot rewrite who Oren had been or why he left.
```