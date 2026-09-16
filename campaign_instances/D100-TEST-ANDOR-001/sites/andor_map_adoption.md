# Andor Map Placement Adoption

> Authoritative claim-extension record for exact public navigation details introduced after the broader site bundle in `campaign/andor_sites.md`.
>
> This file does not create duplicate sites. Every claim below attaches to an existing stable `site_id`. `campaign/andor_public_map.md` is the player-safe projection of these adopted placement claims plus the broader site state.

```yaml
record_id: ANDOR-MAP-ADOPTION-001
status: committed
recorded_at: 2026-09-16
adoption_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
decision_owner: AO/world-resolution
origin_kind: creative-addition
```

## MAP-CLAIM-001 — Three Councils public navigation

```yaml
site_id: SITE-ANDOR-COUNCIL-TOWERS
predicate: public_navigation
value:
  zone: CENTRAL
  route: 中央環道 → 三塔廣場
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - campaign/andor_sites.md#SITE-ANDOR-COUNCIL-TOWERS
status: committed
decision_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## MAP-CLAIM-002 — Imperial Magic Academy public navigation

```yaml
site_id: SITE-ANDOR-IMPERIAL-MAGIC
predicate: public_navigation
value:
  zone: ACADEMIC
  route: 學院大街東段 → 星儀廣場北側
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - campaign/andor_sites.md#SITE-ANDOR-IMPERIAL-MAGIC
status: committed
decision_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## MAP-CLAIM-003 — John Academy public navigation

```yaml
site_id: SITE-ANDOR-JOHN-ACADEMY
predicate: public_navigation
value:
  zone: ACADEMIC
  route: 學院大街西段 → 墨井廣場南側
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - campaign/andor_sites.md#SITE-ANDOR-JOHN-ACADEMY
status: committed
decision_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## MAP-CLAIM-004 — Old-city bard academy public navigation

```yaml
site_id: SITE-ANDOR-BARD-COLLEGE
predicate: public_navigation
value:
  zone: OLD CITY
  route: 劇場街西段 → 七弦巷口
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - campaign/andor_sites.md#SITE-ANDOR-BARD-COLLEGE
status: committed
decision_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## MAP-CLAIM-005 — 曲聞會館 public navigation

```yaml
site_id: SITE-ANDOR-WHISPERS-CONTACT
predicate: public_navigation
value:
  zone: OLD CITY
  route: 劇場街中段 → 鳴鐘拱廊東口
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - campaign/andor_sites.md#SITE-ANDOR-WHISPERS-CONTACT
status: committed
decision_event_ref: ADOPT-ANDOR-PUBLIC-MAP-2026-09-16
```

## Projection rule

```text
physical site identity = campaign/andor_sites.md stable site_id
exact public navigation claim = this file
player-safe rendered map = campaign/andor_public_map.md
private actor annotations = actor epistemic layer
```

Changing what an actor knows does not create a new site. Future world events may legitimately rename, move, close or destroy a site, but reload/model changes alone do not reroll these placements.
