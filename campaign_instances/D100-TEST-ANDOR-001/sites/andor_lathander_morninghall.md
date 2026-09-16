# Andor — Lathander Morninghall / 晨曦之主・晨光堂

> Ordinary public temple site established during Mileia's Session 1 route after the DM rollback. This file is a campaign creative addition grounded to Mileia's established faith and D100 Life Domain canon; it is not claimed to be pre-existing Sheet canon.

```yaml
site_id: SITE-ANDOR-LATHANDER-MORNINGHALL
public_name_zh: 晨曦之主・晨光堂
public_name_en: Lathander Morninghall
origin_kind: creative-addition
status: committed
recorded_at: 2026-09-16
location:
  district: Andor east district
  route_hint: 朝日街末段
public_function:
  - Lathander worship
  - public prayer and morning rites
  - blessings
  - basic healing and clergy consultation
  - ordinary traveler reception
night_status: reduced staff / night watch only
```

## Grounding

- `characters/mileia.md` establishes Mileia as a Life Domain cleric devoted to **Lathander / 晨曦之主**.
- `[D100_CANON] sources/sheet_mirror/10_牧師領域.json.md` explicitly lists Lathander among solar deities compatible with the Life Domain and describes the Life Domain as healing, sustaining life, caring for those in need, and opposing death/undead forces.
- The exact existence, name, east-district location, architecture, staffing and local customs of this Andor temple are campaign-generated facts adopted here.

## Public visual identity

- East-facing main entrance.
- Rising-sun emblem displayed openly over the entrance and within the hall.
- Warm-toned stone and pale plaster; designed to take strong morning light.
- At night only the entrance, side aisle and a few interior lamps remain lit.
- The building is a functioning urban temple rather than a monumental cathedral.

## Ordinary etiquette

- A visiting cleric of the same faith is not treated as an anonymous lay visitor once she identifies herself, but neither is she automatically granted local authority.
- A same-faith cleric may recognize the public iconography and ordinary devotional layout without a roll.
- Local clergy may ask name, home temple/training background, travel purpose, and whether the visitor needs lodging, worship access, healing supplies, or professional contact.
- Exact local hierarchy, named superior clergy, specialized rites and any exceptional privileges are not globally precommitted by this file.

## Current night-duty NPC commitment

### Cael Arven / 凱爾・阿文

```yaml
npc_id: NPC-ANDOR-MORNINGHALL-CAEL
origin_kind: creative-addition
status: committed
role: junior ordained cleric on night duty
alignment: good-oriented; exact law-chaos unset
faith: Lathander
knowledge_floor:
  - ordinary Morninghall procedures
  - who is currently on duty
  - basic local congregation and temple services
  - how visiting same-faith clergy are received
current_goal: finish night watch, keep the hall orderly, route genuine needs appropriately
hidden_agenda: none established
```

Cael is not a quest-giver by default and has no automatic link to Low Whisper, Oren, blue-wax, missing copyist, Three Silver Coins, guild work or other active mystery threads.

## Fuses

- Do not reuse any VOID facts from `MILEIA-LINE-ROLLBACK-2026-09-16`.
- Do not import generic chapel/dispensary customs from the deleted south-care-node scene.
- Mileia's own Lathander knowledge may justify recognizing ordinary faith symbols and norms; local Andor-specific facts must come from this site/NPC or later evidence.
