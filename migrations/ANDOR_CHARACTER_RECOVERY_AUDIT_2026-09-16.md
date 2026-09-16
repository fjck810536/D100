# Andor Character Recovery Audit — 2026-09-16

> Campaign: `D100-TEST-ANDOR-001`
>
> Purpose: exhaust recoverable character-creation state after the original creation working data was not promoted into durable actor masters. This audit distinguishes **recovered established facts** from **deterministic reconstruction**, **superseded drafts**, and fields that were **never actually finalized**.

## 1. Sources exhausted

Recovery searched / cross-checked:

1. current selected campaign actor masters under `campaign_instances/D100-TEST-ANDOR-001/characters/`;
2. legacy root `characters/`, session checkpoint, runtime migration and live-state records;
3. Git commit history, including character-recovery commits and character-creation protocol/regression commits;
4. D100 normalized character-creation rules and GM clarification records;
5. prior character-creation chat logs recoverable from conversation history;
6. connected Google Drive searches for the five PC names plus broad D100 character-sheet searches;
7. uploaded/File Library search for the five PCs and D100 character-card material.

### Search result boundary

- Git history contains **no earlier committed full master card** for Elian, Rook, Aster, Mileia or Nella before the later recovery commits. The missing full cards were never durably committed, rather than later being overwritten by another Git master.
- Google Drive contains D100 templates / older unrelated character sheets, but no discoverable sheet for these five PCs by their names or Andor identifiers.
- File Library contains no separate full actor card for these five PCs.
- Therefore the remaining recoverable creation data comes from prior chat creation logs, cross-checked against current derived totals, session resources, CP awards and current D100 formulas.

## 2. Recovery status vocabulary

```yaml
recovered_established:
  meaning: explicitly finalized in creation/play logs and recovered with corroboration

deterministic_reconstruction:
  meaning: uniquely recomputable from recovered established inputs under current recorded D100 formula

unresolved_not_finalized:
  meaning: exhaustive search indicates the field was never actually finalized; do not keep pretending a lost authoritative value exists

superseded:
  meaning: an earlier draft/build existed but was replaced before the accepted build; it must not be merged into current state
```

`unresolved_not_finalized` is different from `pending_recovery`. The former closes the recovery search until a user supplies new primary evidence.

---

# 3. Rook Hal / Rook・哈爾

```yaml
character_id: PC-ROOK
race: human
age: approximately 27
concept: militia / caravan guard / practical martial traveller
raw_attributes: {STR: 18, DEX: 16, SKI: 17, CON: 14, RES: 13, INT: 12, WIS: 10, CHA: 9, SPI: 7}
adjustments: {STR: 3, DEX: 2, SKI: 2, CON: 1, RES: 0, INT: -1, WIS: -2, CHA: -2, SPI: -3}
adjustment_sum: 0
adjusted_starting_cp: 300
creation_spent_cp: 260
creation_reserve_cp: 40
checkpoint_award_cp: 1
current_cp_reserve: 41
```

Recovered final ledger:

```text
Martial — 126 CP
長劍3、閃避3、格擋3、盾牌3、中甲3、專攻長劍3、武器專精2、及時備戰3、精通先攻2、戰鬥反射2、盲戰1

Survival — 46 CP
耐久3、頑強2、健壯3、強韌加強2、快速反射2

Caravan life — 88 CP
競技3、騎術3、生存3、自救2、聆聽3、偵察3、繩技2、估價1、搜集資訊1、地方知識1
```

Languages:

```text
通用語3 — free creation grant
no additional language was recovered as finalized
```

HP/SP:

```yaml
creation_reward_roll_recovered:
  hp: 3d8 = 3 + 7 + 2 = 12
  sp: 3d4 = 2 + 2 + 1 = 5
final: {hp: 39, sp: 18}
```

The exact HP base decomposition cannot be reconstructed without inventing how every skill/item bonus contributed. Final 39/18 and the reward dice are established; do not reverse-engineer an unsupported intermediate total.

Equipment:

- Final rerun retained the item shell `長劍 / 中甲 / 盾` under the normal three-item starting template.
- Exact assignment of `+3 / +4 / +5` and exact affixes were **not finalized** in the accepted rerun.
- Earlier `+4 長劍 / +3 重甲 / +2 重鋼盾` material belongs to a superseded draft and is not current equipment authority.

---

# 4. Aster Veyn / 艾斯特・維恩

```yaml
character_id: PC-ASTER
race: human
age: approximately 23-24
concept: formally educated, theory-oriented young wizard; not a prodigy
raw_attributes: {STR: 9, DEX: 10, SKI: 11, CON: 10, RES: 17, INT: 18, WIS: 13, CHA: 9, SPI: 13}
adjustments: {STR: -2, DEX: -2, SKI: -1, CON: -2, RES: 2, INT: 3, WIS: 0, CHA: -2, SPI: 0}
adjustment_sum: -4
adjusted_starting_cp: 340
skill_feat_spent_cp: 266
hp_purchase_cp: 24
creation_total_spent_cp: 290
creation_reserve_cp: 50
checkpoint_award_cp: 2
current_cp_reserve: 52
usable_spell_circle: 2
```

Recovered final ledger:

```text
Core + language — 52 CP
奧術知識3、黑魔導3、黑魔力2、龍語1

Mage toolkit — 148 CP
戰鬥施法3、魔力擴展3、高級魔力擴展1、冥想3、法術穿透3、法術熟稔2、辨識法術3、魔法物品學3、魔法天賦2、魔法陣基礎學2、施法免材2、移動施法2、使用魔法裝置2、魔力延展2

Defense — 24 CP
鋼鐵意志2、耐久2、自救2

Scholar / life — 42 CP
細緻2、文書解讀2、搜索2、估價2、歷史2、地方2、專業〔抄寫／書記〕2
```

Spellcasting identity:

- `奧術知識3 / 黑魔導3 / 黑魔力2` → usable circle 2; the Lv3 entries are partial investment toward circle 3.
- Final build is a **generalist / no formal school specialization** at this boundary.
- No exact known/prepared spell list, slot allocation or grimoire contents were ever finalized in the recovered creation log. Those fields are `unresolved_not_finalized`, not a missing hidden spell list.

Languages:

```text
通用語3 — free creation grant
龍語1 — finalized optional purchased language
```

HP/SP:

```yaml
creation_reward_roll_recovered:
  hp: 2d4 = 1 + 3 = 4
  sp: 2d8 = 5 + 8 = 13
hp_purchase:
  cp: 24
  hp_added: 18
final: {hp: 30, sp: 52}
```

The creation log preserves the final totals and the 24-CP HP purchase; the exact contribution of all other SP/HP modifiers should not be reverse-engineered beyond the preserved data.

Equipment:

- Final rerun retained the shell `staff / ring / head item` under the normal three-item template.
- Exact `+3 / +4 / +5` assignment and affixes were not finalized.
- Earlier provisional `+4 staff〔儲魔+3〕 / +3 ring〔隱形+2〕 / +2 headband〔光亮+1〕` is superseded and must not be promoted.

---

# 5. Mileia / 米蕾亞

```yaml
character_id: PC-MILEIA
race: human
age: approximately 25
concept: Life Domain cleric / healer; temple and poorhouse medical-charity background
faith: Lathander / 晨曦之主
domain: Life Domain / 生命領域
raw_attributes: {STR: 9, DEX: 11, SKI: 10, CON: 16, RES: 16, INT: 15, WIS: 19, CHA: 17, SPI: 19}
adjustments: {STR: -2, DEX: -1, SKI: -2, CON: 2, RES: 2, INT: 1, WIS: 3, CHA: 2, SPI: 3}
adjustment_sum: 8
adjusted_starting_cp: 220
creation_spent_cp: 206
creation_reserve_cp: 14
checkpoint_award_cp: 1
current_cp_reserve: 15
usable_spell_circle: 2
```

Recovered final ledger:

```text
宗教知識3、神術2、天界語1、引導神力3、驅散不死2、領域2、生命門徒3、護衛生命2、神力祝福1、戰鬥施法2、魔力擴展2、冥想3、鋼鐵意志2、耐久2、頑強1、強韌加強1、急救3、自救3、交涉2、察言觀色2、聆聽2、生存1、談判專家1、警覺1
```

Recovered category totals:

```text
core — 44 CP
cleric / Life Domain — 88 CP
defense — 22 CP
temple medicine / social — 52 CP
TOTAL — 206 CP
```

Spellcasting identity:

- `宗教知識3 / 神術2` → usable circle 2 with partial circle-3 investment.
- Lathander / Life Domain was explicitly chosen at creation; it is not inferred from later site play.
- No exact prepared spell list, named spell inventory or slot allocation was finalized. These are `unresolved_not_finalized`.

Languages:

```text
通用語3 — free creation grant
天界語1 — finalized optional purchased language
```

HP/SP:

```yaml
creation_reward_roll_recovered:
  hp: 2d4 = 1 + 1 = 2
  sp: 2d8 = 8 + 1 = 9
final: {hp: 20, sp: 35}
```

Equipment:

- A normal three-item `+3 / +4 / +5` starting allocation was part of the accepted creation template.
- Exact item-to-bonus mapping and affixes were never cleanly finalized in the recovered final log. Do not resurrect provisional equipment as canon.

---

# 6. Nella / 涅菈

```yaml
character_id: PC-NELLA
race: human
age: approximately 22
concept: locksmith-family infiltration / courier / scout / gray-work character
raw_attributes: {STR: 9, DEX: 17, SKI: 16, CON: 15, RES: 14, INT: 16, WIS: 14, CHA: 13, SPI: 13}
adjustments: {STR: -2, DEX: 2, SKI: 2, CON: 1, RES: 1, INT: 2, WIS: 1, CHA: 0, SPI: 0}
adjustment_sum: 7
adjusted_starting_cp: 230
creation_spent_cp: 210
creation_reserve_cp: 20
checkpoint_award_cp: 3
current_cp_reserve: 23
```

Recovered final ledger:

```text
匕首2、閃避2、武器嫻熟1、及時備戰1、快速反射2、躲藏3、潛行3、解除裝置3、開鎖3、手上功夫3、搜索3、翻滾2、脫逃術2、隱密2、靈巧手指3、熟練手法1、聆聽2、偵察2、生存1、警覺2、自救2、耐久2、繩技2、估價2、唬騙2、偽造文書2、調查員2、欺詐1、地方知識1、搜集資訊1
```

Languages:

```text
通用語3 — free creation grant
no additional language was recovered as finalized
```

HP/SP:

```yaml
creation_reward_roll_recovered:
  hp: 1d8 = 7
  sp: 1d4 = 4
extra_hp_sp_purchase: none recovered
final: {hp: 23, sp: 19}
```

For Nella the recovered reward plus recovered base totals are consistent with the final 23/19 without needing an invented extra purchase.

Equipment:

- A normal `+3 / +4 / +5` starting magic-item allocation existed in the accepted template.
- `dagger / cloak / boots` appears in prior provisional shell material, but the exhaustive recovery does not establish an exact final item-to-bonus/affix mapping. Treat that shell as a recovery candidate only, not current equipment authority.
- Elian's invisibility cloak used during Session 1 is a borrowed Elian item, not evidence for Nella's starting cloak.

---

# 7. Elian de Valer / 埃利安・德・瓦雷

```yaml
character_id: PC-ELIAN
race: human
age: approximately 21-24
concept: runaway fallen / financially weak minor noble; noncaster
raw_attributes: {STR: 16, DEX: 19, SKI: 18, CON: 18, RES: 12, INT: 22, WIS: 14, CHA: 12, SPI: 10}
adjustments: {STR: 2, DEX: 3, SKI: 3, CON: 3, RES: -1, INT: 5, WIS: 1, CHA: -1, SPI: -2}
adjustment_sum: 13
adjusted_starting_cp: 170
creation_spent_cp: 160
creation_reserve_cp: 10
checkpoint_award_cp: 3
current_cp_reserve: 13
```

Recovered final ledger:

```text
Sword / combat — 76 CP
長劍3、閃避3、格擋3、專攻長劍3、武器專精2、及時備戰2、翻滾2、快速反射1

Noble education — 68 CP
騎術2、交涉3、察言觀色2、貴族與皇室3、歷史2、估價2、文書解讀2、唬騙2、談判專家1、細緻1

Travel / body — 16 CP
搜索1、偵察1、聆聽1、攀爬1、游泳1、平衡感1、耐久1、頑強1
```

Languages:

```text
通用語3 — free creation grant
no additional language was recovered as finalized
```

HP/SP:

```yaml
creation_reward_floor_recovered:
  hp_added: 7
  sp_added: 3
final: {hp: 31, sp: 17}
```

Equipment established in the accepted rerun / session state:

- ordinary longsword;
- invisibility cloak, 3/day;
- Dimension Door ring, 3/day;
- air-walk boots, at least 3h/day.

Exact activation / duration / target / transfer interfaces remain unresolved rule details, not missing ownership facts.

The older approximately-300-CP Elian build with substantially different attributes / HP-SP is **superseded** and must never be merged into the 170-CP accepted build.

---

# 8. Deterministic reconstruction from recovered attributes

Using `00_core/character_creation.md`, the recovered raw + adjustment sets uniquely reproduce all current six bases. They also allow the following deterministic resistance and special-check values unless later equipment/effect modifiers apply:

| PC | 抗毒素 | 抗控制 | 抗轉化 | 抗噴吐 | 抗魔法 | 強韌 | 精神 | 靈魂 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Rook | 28 | 21 | 26 | 31 | 24 | 70 | 65 | 35 |
| Aster | 27 | 32 | 38 | 27 | 40 | 50 | 85 | 65 |
| Mileia | 36 | 40 | 36 | 28 | 34 | 80 | 80 | 95 |
| Nella | 31 | 30 | 30 | 34 | 33 | 75 | 70 | 65 |
| Elian | 32 | 26 | 22 | 33 | 38 | 90 | 60 | 50 |

These are derived values, not additional remembered claims.

---

# 9. Exhausted unresolved fields

After Git history, sessions, Drive, File Library and recoverable chat creation logs were searched, the following are no longer usefully labeled `pending_recovery`:

```yaml
Aster_exact_spell_list_and_preparation: unresolved_not_finalized
Mileia_exact_spell_list_and_preparation: unresolved_not_finalized
Rook_exact_final_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized
Aster_exact_final_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized
Mileia_exact_final_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized
Nella_exact_final_magic_item_bonus_mapping_and_affixes: unresolved_not_finalized
Rook_additional_languages: no_recovered_evidence
Nella_additional_languages: no_recovered_evidence
Elian_additional_languages: no_recovered_evidence
Rook_starting_money: no_recovered_evidence
Aster_starting_money: no_recovered_evidence
Mileia_starting_money: no_recovered_evidence
Nella_starting_money: no_recovered_evidence
```

`no_recovered_evidence` must not be converted into a positive claim of zero/none if future primary evidence appears.

## 10. Persistence action

The five selected-campaign actor masters should now be expanded from this audit. Legacy root actor files remain audit/history and are not rewritten merely to mirror the selected campaign.
