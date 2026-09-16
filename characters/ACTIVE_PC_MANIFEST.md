# Active PC Manifest

> Runtime integrity manifest for the current Andor test session. An active PC missing an authoritative `characters/*.md` record is a persistence/recovery problem, not evidence that the character fact was never established.

```yaml
manifest_id: ACTIVE-PC-MANIFEST-2026-09-16
status: active
session_ref: sessions/2026-09-16_session-1_live-state.md
```

| PC | Controller | Character record | Integrity status |
|---|---|---|---|
| Elian | human player | missing | P0_RECOVERY_REQUIRED |
| Rook | 鮫島 / PL+PC | missing | P0_RECOVERY_REQUIRED |
| Aster | 赫茲 / PL+PC | missing | P0_RECOVERY_REQUIRED |
| Mileia | 彌生 / PL+PC | `characters/mileia.md` | RECOVERED_PARTIAL |
| Nella | 蟬 / PL+PC | missing | P0_RECOVERY_REQUIRED |

## Meaning of `P0_RECOVERY_REQUIRED`

This status means the active character instance that should exist under the character-state architecture is absent from the repository.

It does **not** mean:

- the PC has no established background;
- omitted identity fields are free creative space;
- a runtime may answer `unknown` without attempting recovery;
- session summaries are a complete substitute for the missing character card.

## Runtime rule

Before resolving a character-dependent query or scene for an active PC:

```text
manifest
→ character record
→ referenced creation / session / decision history
→ recovery if record is absent or partial
→ only then adjudication / narration
```

If the needed field is absent because the character record itself is missing, classify the condition as `STATE_INTEGRITY_GAP`, not `NON_ASSERTION` or `SOURCE_GAP`.

A `STATE_INTEGRITY_GAP` must trigger recovery. It must not silently become grounded generation.
