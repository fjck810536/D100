# Andor Public Map Projection — Session 1

> Player-safe / ordinary-public navigation layer for the current Andor city scene.
>
> This is a projection of `campaign/andor_sites.md` plus the authoritative exact-placement claims in `campaign/andor_map_adoption.md`; it is not a second world state. Stable site IDs remain authoritative.

```yaml
map_id: ANDOR-PUBLIC-MAP-001
status: active
recorded_at: 2026-09-16
source_state_refs:
  - campaign/andor_sites.md
  - campaign/andor_map_adoption.md
adoption_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## Navigation spine

For play, use four broad city zones:

```text
CENTRAL — central administration / major public institutions
ACADEMIC — academies, formal scholarship, clerical services
OLD CITY — theatres, performance houses, old inns, guild social routes
SOUTH — ordinary inns, markets, temples/dispensaries, worker traffic
```

These zones are navigation abstractions for the current city, not claims that Sheet canon defines Andor into exactly four municipal wards.

---

## SITE-ANDOR-COUNCIL-TOWERS

**Public map label:** 三大議會（三塔廣場）

**Stable navigation:**

```text
CENTRAL
中央環道 → 三塔廣場
```

The three towers are visually dominant enough to serve as a central landmark once the party is in the central institutional zone.

Provenance:

```text
Three Councils existence/history = source-backed
three towers = user correction
central landmark placement / 三塔廣場 label = MAP-CLAIM-001 creative addition
```

---

## SITE-ANDOR-IMPERIAL-MAGIC

**Public map label:** 帝國魔法學院

**Stable navigation:**

```text
ACADEMIC
學院大街東段 → 星儀廣場北側
```

A visitor seeking ordinary business uses the public reception/gate, not restricted internal facilities.

Provenance:

```text
institution + eight-seat relation = source-backed via Red Wizard cross-reference
public gate = adopted site state
exact city placement = MAP-CLAIM-002 creative addition
```

---

## SITE-ANDOR-JOHN-ACADEMY

**Public map label:** 約翰學院

**Stable navigation:**

```text
ACADEMIC
學院大街西段 → 墨井廣場南側
```

This is the same John Academy already involved in public notices and current session evidence; map stabilization does not add causal links to unrelated hooks.

Provenance:

```text
foundation date = source-backed
John founded it in Andor = user correction
exact city placement = MAP-CLAIM-003 creative addition
```

---

## SITE-ANDOR-BARD-COLLEGE

**Public map label:** 吟遊詩人學院

**Stable navigation:**

```text
OLD CITY
劇場街西段 → 七弦巷口
```

This stabilizes the already player-visible old-city bard-academy destination.

Provenance:

```text
local institution / old-city theatre placement = compatible legacy-generated session fact
七弦巷口 exact landmark = MAP-CLAIM-004 creative addition
```

Do not silently equate this academy with Low Whisper College.

---

## SITE-ANDOR-WHISPERS-CONTACT

**Public map label:** 曲聞會館

**Stable navigation:**

```text
OLD CITY
劇場街中段 → 鳴鐘拱廊東口
```

Public description:

```text
performance / story / message-exchange / private-instructor referral venue
```

Characters who later acquire legal additional knowledge can annotate the same stable site ID in their private notes.

Provenance:

```text
venue + public services = adopted site state
exact placement = MAP-CLAIM-005 creative addition
additional non-public relation = separate role-safe state
```

---

## Current-session public anchors already in use

These remain usable without needing exact street-number simulation:

```text
Mercenary Guild — guild/commercial district anchor
Three Silver Coins — known public establishment / contact point in current play
Grey Antler — south-area inn/restaurant already visited
Temple / dispensary route — south district; Mileia currently headed that way
merchant message/office route — Nella-observed route; not automatically a party-wide public-map landmark
```

## Map projection fuse

```text
site exists in backend ≠ every actor knows every label
public map label ≠ non-public affiliation
private annotation ≠ new physical site
map projection ≠ source text
adopted map point remains stable after reload unless world events actually move/destroy/rename it
```
