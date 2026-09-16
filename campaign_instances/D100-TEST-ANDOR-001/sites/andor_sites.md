# Andor Site State — grounded-generation repair

> Authoritative site-state bundle for the active Andor session.
>
> Recorded: 2026-09-16. This repair does **not** mean these buildings appeared in-world on 2026-09-16. `recorded_at` and `effective_from` are separate. Existing player-visible facts are preserved as `legacy-generated`; source-backed and user-corrected claims are recorded separately; newly adopted local details remain marked `creative-addition`.
>
> This file does not duplicate Mystery payload. Hidden affiliations use `secret_refs` / role-safe map projection.

```yaml
bundle_id: ANDOR-SITES-001
status: active
recorded_at: 2026-09-16
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
source_resolution_ref: SOURCE-RESOLVE-ANDOR-INSTITUTIONS-2026-09-16
repair_event_ref: REPAIR-ANDOR-MAP-PROVENANCE-2026-09-16
```

## Source-resolution summary

```yaml
source_facts:
  - D100 Sheet has three councils as major institutions; historical timeline identifies 魔導學院、鍊金議會、萬神殿 and their interventions/restarts.
  - D100 Sheet Low Whisper College exists as a bardic college tradition; members commonly hide their affiliation and operate around information/secrets/power centers.
  - D100 Sheet confirms 安道爾帝國魔法學院 through the 賽爾紅袍協會 cross-reference; it has eight seats capable of being concurrently held by the eight Red Wizard chiefs.
  - D100 Sheet timeline records 約翰學院 founded in year 4520.
  - D100 Sheet timeline records bardic guilds among major continental organizations appearing around year 972; this is contextual support, not proof of the local old-city bard academy.
source_refs:
  - sources/sheet_mirror/01_world_core.json.md#世界觀
  - sources/sheet_mirror/01_world_core.json.md#大陸簡史
  - sources/sheet_mirror/09_吟遊詩人特殊專長.json.md#學院選擇
  - sources/sheet_mirror/09_吟遊詩人特殊專長.json.md#低語學院
user_corrections:
  - CORR-ANDOR-COUNCIL-001: 三大議會在安道爾有三塔；來源檔漏寫不代表塔不存在。
  - CORR-ANDOR-JOHN-001: 約翰在安道爾創立約翰學院。
```

### Entity-resolution correction

Player wording `安道爾法術學院` is retained as spoken wording. For objective world use in this session, Librarian resolution maps it contextually to the source-backed **安道爾帝國魔法學院** unless later dialogue clearly indicates a different institution.

```text
player wording ≠ canonical label rewrite of the transcript
resolved referent = SITE-ANDOR-IMPERIAL-MAGIC
```

Do not merge:

```text
三大議會／魔導學院
安道爾帝國魔法學院
約翰學院
```

They are distinct institutions/entities.

---

# SITE-ANDOR-COUNCIL-TOWERS — 三大議會三塔

```yaml
site_id: SITE-ANDOR-COUNCIL-TOWERS
name: 三大議會三塔
site_type: institutional_complex
status: committed
recorded_at: 2026-09-16
effective_from: pre-session-existing-city-landmark
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
map_projection:
  backend_label: 三大議會三塔
  public_label: 三大議會
  navigation_status: known
  visibility_ref: public-landmark
```

## Claims

### COUNCIL-SITE-001 — 三大議會存在

```yaml
origin_kind: source-extraction
generated: false
source_refs:
  - sources/sheet_mirror/01_world_core.json.md#世界觀
  - sources/sheet_mirror/01_world_core.json.md#大陸簡史
status: committed
```

### COUNCIL-SITE-002 — 三塔存在

```yaml
origin_kind: user-correction
generated: false
source_refs: []
user_correction_ref: CORR-ANDOR-COUNCIL-001
status: committed
effective_from: pre-session-existing-city-landmark
```

### COUNCIL-SITE-003 — 地理落點

```yaml
value: 安道爾中央行政／權力區的可導航大型機構群
origin_kind: legacy-generated
generated: true
contextual_support_refs:
  - council institutional importance in world history
  - earlier player-visible Andor map narration
status: committed
recorded_at: 2026-09-16
effective_from: before current old-city scene
```

### COUNCIL-SITE-004 — 三塔分屬三大議會並有公共接洽入口

```yaml
value:
  - 魔導學院塔：一般公務／學術聯絡與文書接洽入口
  - 鍊金議會塔：一般技術／材料／議會事務接洽入口
  - 萬神殿塔：一般宗教／機構聯絡接洽入口
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - three-council institutional identities in world-core
  - requirement that an established public institution have an actionable ordinary contact path
status: committed
decision_owner: AO/world-resolution
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
```

The exact current officeholders, internal departments, restricted floors and secret functions remain unset until source/state/grounded generation makes them relevant. Public intake does not imply unrestricted access.

---

# SITE-ANDOR-IMPERIAL-MAGIC — 安道爾帝國魔法學院

```yaml
site_id: SITE-ANDOR-IMPERIAL-MAGIC
name: 安道爾帝國魔法學院
site_type: magical_academic_institution
status: committed
recorded_at: 2026-09-16
effective_from: pre-session-existing-institution
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
map_projection:
  backend_label: 安道爾帝國魔法學院
  public_label: 帝國魔法學院
  navigation_status: known
  visibility_ref: public-institution
```

## Claims

### IMPMAGIC-001 — institution existence / eight seats

```yaml
origin_kind: source-extraction
generated: false
source_refs:
  - sources/sheet_mirror/01_world_core.json.md#賽爾紅袍協會
value: 安道爾帝國魔法學院存在，具有八個席位；紅袍八位首席與這八席「可以相互兼任」。
status: committed
```

Fuse:

```text
「可以兼任」≠ 現任八席都是紅袍首席
「可以兼任」≠ 現場一定有紅袍人物
```

### IMPMAGIC-002 — city landing / public reception

```yaml
value: 安道爾正式學術／行政區內有可直接前往的本院主要接待入口
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - source-backed national institution
  - Andor's source-backed high spellcaster political weight
  - earlier player-visible map narration placing a spell academy in the formal academic/administrative side
status: committed
decision_owner: AO/world-resolution
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
```

Precise street, dean, current seat-holders, curriculum and internal security remain unresolved rather than falsely sourced.

---

# SITE-ANDOR-JOHN-ACADEMY — 約翰學院

```yaml
site_id: SITE-ANDOR-JOHN-ACADEMY
name: 約翰學院
site_type: academy
status: committed
recorded_at: 2026-09-16
effective_from: pre-session-existing-institution
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
map_projection:
  backend_label: 約翰學院
  public_label: 約翰學院
  navigation_status: known
  visibility_ref: public-institution
```

## Claims

### JOHN-001 — foundation date

```yaml
origin_kind: source-extraction
generated: false
source_refs:
  - sources/sheet_mirror/01_world_core.json.md#大陸簡史
value: 約翰學院於大陸曆 4520 年成立。
status: committed
```

### JOHN-002 — founder and Andor location

```yaml
origin_kind: user-correction
generated: false
user_correction_ref: CORR-ANDOR-JOHN-001
value: 約翰在安道爾創立約翰學院。
status: committed
```

### JOHN-003 — current local placement

```yaml
value: 安道爾學術區可導航學院落點；已出現在本 session 公開告示／工會地圖語境。
origin_kind: legacy-generated
generated: true
contextual_support_refs:
  - current session public notices and map
status: committed
recorded_at: 2026-09-16
effective_from: before current old-city scene
```

Special-collection restrictions, missing copyist and blue-wax incident retain their separate session/Mystery provenance. Source resolution of the Academy's name/date does **not** turn those session facts into Sheet canon.

---

# SITE-ANDOR-BARD-COLLEGE — 舊城吟遊詩人院館

> Preserves the already player-visible destination instead of replacing it with the newly adopted Low Whisper contact node.

```yaml
site_id: SITE-ANDOR-BARD-COLLEGE
name: 吟遊詩人學院（舊城院館）
site_type: bardic_school_and_performance_institution
status: committed
recorded_at: 2026-09-16
effective_from: before Elian asked the guild clerk for directions
map_projection:
  backend_label: 舊城吟遊詩人院館
  public_label: 吟遊詩人學院
  navigation_status: known
  visibility_ref: public-institution
```

### BARD-SITE-001 — current local site

```yaml
value: 位於舊城西側／劇場街附近；晚間仍有排練、演出與社交活動。
origin_kind: legacy-generated
generated: true
contextual_support_refs:
  - already delivered player-visible scene facts
  - sources/sheet_mirror/01_world_core.json.md#大陸簡史 (吟遊詩人公會歷史 only as broad contextual support)
status: committed
```

This local academy is **not automatically the Low Whisper College headquarters or branch**. It can contain ordinary bardic teaching and contacts. Any actual Low Whisper actor/relationship must come from separate state.

---

# SITE-ANDOR-WHISPERS-CONTACT — 曲聞會館

```yaml
site_id: SITE-ANDOR-WHISPERS-CONTACT
name: 曲聞會館
site_type: public_performance_message_and_referral_venue
status: committed
recorded_at: 2026-09-16
effective_from: pre-session-existing-local-venue
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
secret_refs:
  - SECRET-ANDOR-WHISPERS-001
map_projection:
  backend_label: 曲聞會館 / Low Whisper local contact node
  public_label: 曲聞會館
  navigation_status: known
  visibility_ref: public-name-hidden-affiliation
```

## Claims

### WHISPERS-001 — Low Whisper college identity/style

```yaml
origin_kind: source-extraction
generated: false
source_refs:
  - sources/sheet_mirror/09_吟遊詩人特殊專長.json.md#學院選擇
  - sources/sheet_mirror/09_吟遊詩人特殊專長.json.md#低語學院
status: committed
```

### WHISPERS-002 — local venue / geography / ordinary services

```yaml
value: 曲聞會館位於舊城／劇場街社交圈，是公開表演、故事、訊息交換與私人教習引薦場所。
origin_kind: creative-addition
generated: true
contextual_support_refs:
  - Low Whisper source-backed social style
  - existing old-city theatre ecology
status: committed
decision_owner: AO/world-resolution
adoption_event_ref: ADOPT-ANDOR-SITES-2026-09-16
```

### WHISPERS-003 — hidden Low Whisper contact/teaching function

```yaml
origin_kind: creative-addition
generated: true
status: committed
secret_ref: SECRET-ANDOR-WHISPERS-001
visibility_ref: mystery-role-safe
```

Public map / ordinary directions show only **曲聞會館**. Characters with legal knowledge may privately annotate Low Whisper ties. The node is actionable without making the hidden affiliation public: visitors may request a private bard instructor / discreet introduction through ordinary venue services.

The exact Low Whisper headquarters location remains unresolved. This local node is not automatically the HQ.

---

## Independence fuse

The following remain separate unless future actual events create a link:

```text
SECRET-ANDOR-001 blue-wax / Miren incident
COMMIT-ANDOR-ECON-001 material-price rise
COMMIT-ANDOR-SILVERCOINS-001 Three Silver Coins job
SECRET-ANDOR-WHISPERS-001 Low Whisper contact node
Mercenary-guild jobs
Three Councils / Imperial Magic Academy / John Academy institutional map
```

Shared city geography or overlapping social circles are not proof of one conspiracy.

---

## Adoption / repair events

### ADOPT-ANDOR-SITES-2026-09-16

```yaml
owner: AO/world-resolution
adopts:
  - COUNCIL-SITE-004
  - IMPMAGIC-002
  - WHISPERS-002
  - WHISPERS-003
status: committed
reason: make source-backed institutions and a source-compatible hidden bardic network concretely navigable/interactable without laundering generated details into canon
```

### REPAIR-ANDOR-MAP-PROVENANCE-2026-09-16

```yaml
repairs:
  - old player-visible council/academic/old-city geography that had no Librarian trace
  - entity resolution for player wording 安道爾法術學院
  - missing provenance distinction for three towers and John founder/location
method:
  - source-backed claims receive source refs
  - user corrections remain user corrections
  - earlier narration remains legacy-generated where compatible
  - new creative additions are adopted with explicit generated origin
non_effects:
  - no rolls rerun
  - no resources refunded/recharged
  - no existing secrets rewritten
  - no checkpoint rollback
```
