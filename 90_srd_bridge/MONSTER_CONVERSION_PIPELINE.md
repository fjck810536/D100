# D&D 3.5 → D100 怪物換算流程

> 狀態：`[CONVERSION_REFERENCE]`
>
> 用途：把 3.5 怪物先做成**不針對特定玩家隊伍**的 D100 lineage / 系譜保真版本；完成後才進 encounter calibration。
>
> 上位參考：`COMMON_CONVERSION_REFERENCE.md`、`conversion_rules.md`、D100 core rules。

---

# 0. 原則：先完成物種，再調遭遇

順序固定：

```text
SOURCE PROFILE
→ SEMANTIC DECOMPOSITION
→ LINEAGE CONVERSION
→ CLOSED-LOOP CHECK
→ 可跑的 D100 怪物 v1
→ 最後才做 ENCOUNTER CALIBRATION
```

Lineage conversion 的目標不是平衡，而是保留來源的因果、強弱結構、戰術功能、action economy 與相對耐久。

---

# 1. 來源快照

至少記錄：

```text
來源／版本
體型
HD / HP（印刷值與公式值都保留）
STR DEX CON INT WIS CHA
BAB / attack routine
AC / touch AC / flat-footed AC / components
Fort / Ref / Will
DR / SR / immunity
speed / maneuverability
natural attacks / damage dice
breath / aura / DC / range
spellcasting / CL
special action-economy abilities
round/minute/day timers
CR
生態／戰術
```

來源若有算術矛盾或 OCR 衝突：保留衝突，不偷偷修成單一版本。

標：

```text
[SOURCE_PRINTED]
[SOURCE_DERIVED]
[SOURCE_OCR_UNCERTAIN]
```

---

# 2. 共享六屬性：保留 modifier

```text
m35 = floor((A35 - 10) / 2)
A100 = 13 + 2 × m35
```

目標：

```text
D100 adjustment ≈ 3.5 ability modifier
```

不要 raw score 照抄。

---

# 3. SKI / RES / SPI

## SKI

來源無直接對應。由 BAB / natural weapon proficiency、技能表現、feats、來源「訓練 vs 純力量」比例建立 seed；禁止 `SKI=BAB`。

## RES

```text
Fort chassis = Fort - CON mod
Ref chassis  = Ref  - DEX mod
Will chassis = Will - WIS mod
```

若三者收斂：

```text
RES seed ≈ median(chassis)
```

## SPI

依存在論／靈魂／天生施法本質決定。天生施法者常以 CHA，強精神／靈性生物常以 WIS/CHA 作 seed；構裝、無魂等先寫特殊存在規則。

---

# 4. 技能與熟練

3.5 ranks 不直接等於 D100 level。

若來源有明確 max-rank 投資：

```text
rank ratio = invested ranks / source max ranks
```

| source rank ratio | D100 seed |
|---:|---:|
| 0 | 未受訓 / Lv0 視物種 |
| 0–20% | Lv1 |
| 20–40% | Lv2 |
| 40–60% | Lv3 |
| 60–80% | Lv4 |
| 80–100% | Lv5 |

天生器官可有 `innate proficiency`，不用假裝花過玩家 CP。

---

# 5. d20 機率修正的局部換算

已觀察到：

```text
3.5 +2 skill bonus ≈ D100 +10
```

因此在**純成功率修正層**候選：

```text
3.5 +1 ≈ D100 +5
```

可用於 size attack modifier、dodge bonus、haste +1 attack/AC/Ref、secondary attack -2、circumstance bonus。

不可拿來整包換 raw attribute、HP、damage dice、AC、SR、BAB。

---

# 6. AC 拆層

```text
AC ≠ D100 Dodge
```

拆：

```text
DEX / dodge / size         → Dodge / contact probability
natural armor / armor      → flat mitigation
shield                     → block
DR                         → physical resistance / bypass
miss chance / displacement → independent special defense
```

大型、高 natural armor 怪物常應呈現「容易接觸、難以造成有效傷害」。

## 6.1 Dodge seed

優先參考 touch AC、DEX、dodge、size、movement geometry / maneuverability。

## 6.2 Natural Armor fallback

若沒有 campaign-specific 材料表：

```text
NaturalArmorReduction
≈ ROUND(sqrt(8 × source natural armor bonus))
```

理由：以約 +8 source armor 對齊 D100 重甲約8點級減傷，並讓 epic natural armor 呈 diminishing returns；最終耐久由 closed-loop HP 校正。

這只是 `[CONVERSION_REFERENCE]`。

## 6.3 Explicit DR

來源若有 `DR N/—`，且 damage dice / ability modifier 尺度仍接近：

```text
D100 intrinsic physical resistance seed = N
```

有 bypass 條件就保留語義。多個 DR 不自動相加。

---

# 7. 攻擊

```text
attack = 戰鬥 + innate/weapon proficiency×10 + probability modifiers
```

只有 size 等純概率修正走 `×5`。

來源 secondary natural attack 若 Multiattack 後 -2：

```text
D100 secondary = primary -10
```

## Full Attack 是行動包

`bite + 2 claws + 2 wings + tail` 是一個 `Full Natural Attack Package`，占一個來源等價完整戰術窗口；不是六個免費 D100 general actions。

額外 `standard action` 不能自動取得第二套 full attack，只能做 source standard action 原本可做的事情。

---

# 8. 傷害

若兩邊使用相近 dice 語言且共享 ability modifier 已等價，自然武器 dice 可先保留。

常見龍類 STR 乘數：

```text
bite      1.5×STR adjustment
claw      1.0×STR adjustment
wing      0.5×STR adjustment
tail slap 1.5×STR adjustment
```

再加 D100 自然武器／武器熟練傷害層。

---

# 9. Closed-loop HP：來源怪物打來源自己

先算：

```text
source_expected_damage_per_full_routine
```

包含 source hit probability、DR、full attack、固定狀態。

```text
source_self_TTK
= source_HP / source_expected_damage_per_full_routine
```

再用 D100 版本打自己的 D100 防禦：

```text
D100_expected_self_damage
```

最後：

```text
HP_D100_lineage
= source_self_TTK × D100_expected_self_damage
```

因此 Dodge、armor、DR、damage scale、action package 會一起進耐久換算，而不是只做 HP 比例縮放。

來源印刷 HP 與 HD mean 衝突時兩條都算，形成 lineage range。

---

# 10. Save / DC：Self-save Anchor

沒有中立 benchmark 時：

```text
p_source = P(d20 + source_save >= source_DC)
```

先挑語義正確的 D100 防禦（抗轉化／抗控制／抗噴吐／強韌／精神／靈魂）。

若 D100 用「須過 M」：

```text
margin = Defense - d100
M ≈ Defense - 100×p_source
```

再依 natural-face rule 微調。

Fort/Ref/Will 只給來源成功率，不決定 D100 接口名字。

---

# 11. SR：避免 double-count

Lineage 預設：

1. 用轉譯後 `RES+INT` 建 D100 抗魔法；
2. 讓 D100 法術穿透／高等法術穿透處理；
3. 不再把 `SR85` 額外變成第二個 +85 barrier。

保留 `peer-tier caster penetration probability` 作 invariant；必要時 encounter calibration 才調專用 SR modifier。

---

# 12. Caster Level / slots / SP

來源 spell level 決定大致環級；D100：

```text
base total caster level = ring×3
```

來源 CL 超過此值可保留為 innate caster-level potency。

法術位依 D100 職業公式。

怪物沒有 CP／裝備史時，最低 SP lineage seed：

```text
SP_seed = RES + RES adjustment
```

有 source-backed 高持續施法能力再加，不因 Boss 身分先補。

施法判定照 D100：

```text
class primary composite
+10×(total caster level/3)
-continuous casting penalty
-spell ring×10
```

怪物同樣追連續施法懲罰。

---

# 13. Movement：先拆來源已內建 buff

3.5 listed speed 有時已含 haste／stance／template／age effect。若已內建，先反推 unbuffed speed，再在 D100 重新套，避免 double-count。

世界速度 seed：

```text
ft/s ≈ source move-action ft / 6
```

maneuverability 另外保存成幾何限制，不再扣一次 DEX。

---

# 14. 兩個時鐘

## 沙漏：world time

實際秒數、旅行／飛行距離、被送去未來多久、中毒、增援、NPC 行程。

## 碼表：tactical windows

full attack package、extra standard/move、cooldown 等自己的 turn、time stop private turns、immediate/free/quickened windows。

混合效果至少記：

```text
external_world_time
subjective_time
action_windows
cooldown_basis
```

---

# 15. Haste / Slow

## Haste

來源核心：

- 速度增加；
- +1 attack / dodge AC / Reflex 類概率修正；
- 不是額外一個完整 standard/general action。

D100 機率 seed：

```text
+1 source ≈ +5 D100
```

### Haste 額外攻擊要保留版本語義

3.5 spell text 寫的是 full attack 時對「weapon he is holding」多一次攻擊，因此**自然武器是否取得額外一擊有 RAW 歧義**。

所以通用轉譯流程不得自動寫：

```text
所有 hasted natural-weapon creature 都多1次 primary strike
```

而應記：

```text
manufactured/held weapon → 依來源明文加1 attack
natural weapon → [SOURCE_INTERPRETATION_REQUIRED]
```

保守 Lineage 預設：不加；若來源、版本或團規明確採自然武器也適用，再增加一個 primary natural strike，並重新跑 HP / DPR closed loop。

## Slow

保留：

- 速度減半；
- attack / dodge / reflexive penalty；
- 限制一輪 action package；
- 不可 full attack；
- 抑制 haste 類 cadence。

不要只翻成 `-20`。

---

# 16. Recharge / uses

`1/day, 2/day, 3/day` 通常直接保留世界日。

`1d4 rounds` 先分類：

- 生理／物理等待 → 沙漏；
- 隔 N 個自己的 turn → 碼表。

吐息若來源設計是「隔幾個 turn 才能再吐」，Lineage combat 預設保留 tactical cadence，另記世界時間語意。

---

# 17. Frightful Presence / HD gate

D100 無 HD，不硬造 `HD→CP`。

Lineage 保留：

```text
只影響明顯低於該怪物 lineage tier 的生物；
peer-tier / higher-tier 不自動吃低階恐慌規則。
```

Encounter 時再接 campaign tier / CP / NPC rank。

---

# 18. CR

CR 只保留 source threat tier，不直接換 HP / attack / CP。

可協助 SR peer benchmark 與 frightful-presence tier gate。

---

# 19. Lineage Conversion 完成條件

要標 `[LINEAGE_CONVERTED_V1]`，至少有：

```text
九屬性
六基礎值
五抗／三特殊
HP / SP
attack / dodge
armor / physical resistance / DR
natural attack damage
size / reach / movement
spellcasting resources
Action Palette
special ability interfaces
save thresholds
world-time / tactical-time timers
source conflicts
```

允許尚未實例化的，只能是：

- 個體 spell loadout；
- 個體人格／巢穴／收藏；
- 特定 encounter tuning。

完成後才進：

```text
[ENCOUNTER_CALIBRATION]
```
