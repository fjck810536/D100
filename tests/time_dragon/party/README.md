# Time Dragon Test Party — Operational Dossiers

> `[TEST_FIXTURE] [CHARACTER_EVIDENCE]`
>
> Scope: `tests/time_dragon/` only. These files are the party snapshot / capability index used by the Time Dragon combat pressure test. They are not global current PCs, not selected campaign state, and not a replacement for the source Google Sheets.
>
> Data-layer reference: `../../../DATA_ARCHITECTURE.md`.

## Party snapshot

1. [莎緹拉](./SATHERA_OPERATIONAL_DOSSIER.md)
2. [亞黛兒](./ADELE_OPERATIONAL_DOSSIER.md)
3. [卡蘭德](./KALAND_OPERATIONAL_DOSSIER.md)

Additional test evidence:

- [Operational Profile v1](./OPERATIONAL_PROFILE_V1.md)
- [CP Strength Audit v1](./CP_STRENGTH_AUDIT_V1.md)
- [Kaland player clarification](./KALAND_PLAYER_CLARIFICATION_2026-09-13.md)
- [Fixture party status](./CURRENT_CAMPAIGN_STATUS.md)
- [Read-only character-sheet mirrors](./sheet_mirror/)

## Combat snapshot contract

When this test is explicitly selected, build the encounter snapshot from:

```text
A. permanent character capability
B. equipment and item effects
C. prepared / known spells
D. Action Palette
E. daily / encounter uses
F. TRUE/FALSE buffs in the fixture snapshot
G. HP / SP / spell slots / pools
H. continuous-casting and other live counters
I. actor knowledge relevant to this test
```

Capabilities do not prescribe choices. `has ability != ability activated`; `spell known != currently castable`; `item held != player will consume it`.
