# D&D 3.5 → D100 怪物換算流程

> 狀態：`[CONVERSION_REFERENCE]`
>
> 用途：把 3.5 怪物先做成**不針對特定玩家隊伍**的 D100 lineage / 系譜保真版本；完成後才進 encounter calibration。
>
> 上位參考：`COMMON_CONVERSION_REFERENCE.md`、`conversion_rules.md`、D100 core rules。

---

# 0. 原則：先完成物種，再調遭遇

順序固定為：

```text
SOURCE PROFILE
→ SEMANTIC DECOMPOSITION
→ LINEAGE CONVERSION
→ CLOSED-LOOP CHECK
→ 可跑的 D100 怪物 v1
→ 最後才做 ENCOUNTER CALIBRATION
```

禁止反過來先看當前 PC 數值，再把所有怪物數字調成「剛好能打」。

Lineage conversion 的目標不是平衡，而是：

1. 保留來源能力做的事情；
2. 保留來源強弱結構；
3. 保留來源戰術與 action economy；
4. 保留大致成功率與相對耐久；
5. 讓換算結果能在 D100 自己的規則中閉環。

---

# 1. 先建立來源快照

至少記錄：

```text
來源／版本
體型
HD / HP（印刷值與公式值都保留）
STR DEX CON INT WIS CHA
BAB / attack routine
AC / touch AC / flat-footed AC / AC components
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

若來源本身有算術矛盾或 OCR 衝突：

> **保留衝突，不偷偷修成單一版本。**

另標：

```text
[SOURCE_PRINTED]
[SOURCE_DERIVED]
[SOURCE_OCR_UNCERTAIN]
```

---

# 2. 共享六屬性：保留 modifier

3.5：

```text
m35 = floor((A35 - 10) / 2)
```

D100 anchor：

```text
A100 = 13 + 2 × m35
```

目的是：

```text
D100 adjustment ≈ 3.5 ability modifier
```

這比 raw score 照抄更能保留來源尺度。

---

# 3. SKI / RES / SPI

## SKI

來源沒有直接對應。

先由：

- BAB / natural weapon proficiency；
- 技能表現；
- source feats；
- 怪物在來源中的「訓練 vs 純力量」比例

建立 seed。

不要寫：

```text
SKI = BAB
```

## RES

可拆來源 save chassis：

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

依存在論／靈魂／天生施法本質決定。

常用 proxy：

- 天生施法者：CHA；
- 強精神／靈性生物：WIS / CHA；
- 神性／外在者：另保留特殊本質；
- 構裝／無魂：不要硬套普通生物 SPI。

---

# 4. 技能與熟練：使用「相對熟練度」而非 ranks 直搬

3.5 skill ranks 不直接等於 D100 skill level。

若來源有明確 max-rank 投資，可先用：

```text
rank ratio = invested ranks / source max ranks
```

候選：

| source rank ratio | D100 skill seed |
|---:|---:|
| 0 | 未受訓 / Lv0 視物種而定 |
| 0–20% | Lv1 |
| 20–40% | Lv2 |
| 40–60% | Lv3 |
| 60–80% | Lv4 |
| 80–100% | Lv5 |

怪物的天生器官（爪、牙、尾）可以有 `innate proficiency`，不需要假裝牠花 CP 學過人類課程。

---

# 5. d20 機率修正的局部換算

D100 已觀察到：

```text
3.5 +2 skill bonus ≈ D100 +10
```

所以在**純成功率修正層**，可用：

```text
3.5 +1 ≈ D100 +5
```

適用候選：

- size attack modifier；
- dodge bonus；
- haste 的 +1 attack / AC / Reflex；
- secondary attack -2；
- circumstance bonus。

不適用：

- raw attribute；
- HP；
- damage dice；
- AC 整包；
- SR 整包；
- BAB 整包。

---

# 6. AC 必須拆成多層防禦

```text
AC
≠ D100 Dodge
```

拆：

```text
DEX / dodge / size        → Dodge / contact probability
natural armor / armor     → flat mitigation
shield                    → block layer
DR                        → physical resistance / bypass rule
miss chance / displacement→ independent special defense
```

## 6.1 Dodge seed

優先參考：

- touch AC；
- DEX；
- dodge bonus；
- size modifier；
- movement geometry／maneuverability。

大型高 natural armor 怪物應常呈現：

```text
容易接觸
＋
難以造成有效傷害
```

## 6.2 Natural Armor → flat mitigation fallback

兩個系統沒有一對一公式。

若沒有 campaign-specific 材料表，可用 diminishing-return seed：

```text
NaturalArmorReduction
≈ ROUND(sqrt(8 × source natural armor bonus))
```

理由：

- 以來源約 +8 armor bonus 對齊 D100 重甲約 8 點級減傷作普通裝甲 anchor；
- epic natural armor 不線性膨脹成 +70～100 點 flat DR；
- 最終耐久仍由 closed-loop HP 校正。

此公式是 `[CONVERSION_REFERENCE]`，不是 D100 canon。

## 6.3 explicit DR

若來源本身已有：

```text
DR N/—
```

且轉換後仍保留相近 damage dice / ability-modifier 尺度，可先：

```text
D100 intrinsic physical resistance = N
```

有 bypass 條件的 DR：保留 bypass 語義，不只保留數字。

若多個來源 DR 疊在同一怪物上，依來源規則確認是否實際堆疊；不要自動相加。

---

# 7. 攻擊

來源 Attack 的用途是建立**命中概率輪廓**。

D100：

```text
attack = 戰鬥 + innate/weapon proficiency×10 + probability modifiers
```

體型等 d20 probability modifier 才走 `×5`。

## 7.1 Primary / secondary

若來源 secondary natural attack 使用 Multiattack 後 -2：

```text
D100 secondary = primary -10
```

## 7.2 Full Attack 是「行動包」

不要把來源：

```text
bite + 2 claws + 2 wings + tail
```

拆成六個免費 D100 一般動作。

它應成為一個特殊的：

```text
Full Natural Attack Package
```

占用一個來源等價的完整戰術窗口。

額外 `standard action` 不能自動再取得一整套 full attack；只能做來源 standard action 原本能做的事情。

---

# 8. 傷害

若來源與 D100 都使用：

- 相同自然武器 dice 語言；
- 共享能力 adjustment 已等價；

則自然武器 dice 可以先保留為 seed。

STR 乘數保留來源語義：

```text
bite:      1.5 × STR adjustment
claw:      1.0 × STR adjustment
wing:      0.5 × STR adjustment
tail slap: 1.5 × STR adjustment
```

再加 D100 武器／自然武器熟練傷害層。

所有小數依 D100 現行取整規則在最終結果處理。

---

# 9. Closed-loop HP：用來源怪物打來源自己

這是**Lineage mode** 最重要的耐久校準方法。

不要先拿玩家 DPR。

先算來源：

```text
source_expected_damage_per_full_routine
```

其中包含：

- source hit probability；
- source DR；
- full attack package；
- persistent haste 等固定狀態。

然後：

```text
source_self_TTK
= source_HP / source_expected_damage_per_full_routine
```

再用已換算的 D100 怪物打自己的 D100 防禦：

```text
D100_expected_self_damage
```

最後：

```text
HP_D100_lineage
= source_self_TTK × D100_expected_self_damage
```

這會讓：

> 「來源版本大約要承受幾套自己的完整攻擊才倒」

在 D100 仍近似成立。

### 為什麼這比 HP 比例縮放好

因為它會把：

- Dodge；
- armor；
- DR；
- damage scale；
- action package

一起納入。

若來源印刷 HP 與 HD 平均值衝突：兩種都算，保留一個 lineage range，再選 working value。

---

# 10. Save / DC：Self-save Anchor

當沒有中立 benchmark 時，可用來源生物**自己的 save 對自己的 DC**當封閉參考。

先算：

```text
p_source = P(d20 + source_save >= source_DC)
```

再挑 D100 的**語義正確**防禦，例如：

- 抗轉化；
- 抗控制；
- 抗噴吐；
- 強韌；
- 精神；
- 靈魂。

若 D100 使用「須過 M」：

```text
margin = Defense - d100
```

則第一個門檻 seed：

```text
M ≈ Defense - 100 × p_source
```

再依 natural critical / edge rule 微調。

重點：

> Fort / Ref / Will 只提供來源成功率；D100 防禦接口仍由效果語義決定。

---

# 11. SR：不要和抗魔法重複計算

來源 Spell Resistance 是 spell penetration gate。

Lineage conversion 預設：

1. 先用轉譯後 `RES + INT` 建 D100 抗魔法；
2. 讓 D100 原本的法術穿透／高等法術穿透接口處理；
3. **不要同時又把 SR85 加成 +85 的第二道牆。**

保留一個來源 invariant：

```text
peer-tier caster penetration probability
```

必要時 encounter calibration 再調專用 SR modifier。

預設 lineage v1 不 double-count SR。

---

# 12. Caster Level / slots / SP

## 12.1 ring / total caster level

來源 spell level 能直接決定大致環級。

D100：

```text
base total caster level = ring ×3
```

來源 CL 高於此值的部分可保留為 innate caster-level potency。

## 12.2 spell slots

依 D100 職業公式直接算。

例如術士：

```text
法術位 = ring×2 + CHA adjustment + explicit modifiers
```

## 12.3 Monster SP fallback

若怪物沒有 CP／裝備歷史，不能假裝存在玩家角色的 CP 投資獎勵。

最低 lineage seed 用 D100 基礎 SP：

```text
SP_seed = RES + RES adjustment
```

若來源明確具有異常高持續施法能力，再另設 source-backed bonus。

## 12.4 施法判定

照 D100 spellcasting core：

```text
casting
= class primary composite
+ 10×(total caster level/3)
- continuous casting penalty
- spell ring×10
```

怪物也要追連續施法懲罰。

---

# 13. Movement：先拆掉來源已內建 buff

3.5 stat block 的 listed speed 有時已包含：

- haste；
- stance；
- template；
- age-stage effect。

若來源能力已內建在 printed speed 中：

> **先反推出 unbuffed speed，再在 D100 重新套 buff。**

否則會 double-count。

世界速度 seed：

```text
ft/s ≈ source move-action ft / 6
```

這是「沙漏」的物理速度。

飛行 maneuverability 另外保存成幾何限制，不直接再扣 DEX。

---

# 14. 兩個時鐘

## 沙漏：world time

處理：

- 實際秒數；
- 旅行／飛行距離；
- 被送去未來多久；
- 中毒多久；
- NPC 何時抵達。

## 碼表：tactical windows

處理：

- full attack package；
- extra standard/move；
- cooldown 等幾個自己的 turn；
- time stop private turns；
- immediate / free / quickened windows。

## 混合型能力

至少同時記：

```text
external_world_time
subjective_time
action_windows
cooldown_basis
```

---

# 15. Haste / Slow 類效果

## Haste 類

保留來源本質：

- 速度增加；
- 小幅 attack / dodge / reflexive bonus；
- full attack 多一個 primary strike；
- **不是額外一個完整 general action。**

若來源是 `+1` 機率修正，D100 seed 可用 `+5`。

## Slow 類

保留來源本質：

- 速度減半；
- 小幅 attack / dodge / reflexive penalty；
- 限制一輪 action package；
- 不可 full attack；
- 抑制 haste / extra-strike cadence。

D100 精確 action restriction 應寫成能力自己的 Action Palette 規則，不只是 `-20`。

---

# 16. Recharge / uses

```text
1/day, 2/day, 3/day
```

通常直接保留世界日。

`1d4 rounds` 要先分類：

- 生理／物理等待 → 沙漏；
- 「隔 N 個自己的 turn」 → 碼表。

吐息若來源設計意義是「每隔幾個 turn 才能再吐」，Lineage combat 預設保留 tactical cadence；另記世界時間語義。

---

# 17. Frightful Presence / HD gates

3.5 常以 HD 判斷哪些生物會受龍威影響。

D100 沒有 HD，因此 Lineage mode 不硬造一個 `HD→CP` 公式。

保留：

```text
只影響明顯低於該怪物 lineage tier 的生物；
peer-tier / higher-tier 不自動套用低階恐慌規則。
```

真正 encounter 時再以 campaign tier / CP / NPC rank 映射。

---

# 18. CR

CR 只保留 threat tier，不換成 D100 數字。

```text
CR → source role / source tier
```

它可以協助 SR peer benchmark、frightful-presence tier gate，但不直接決定 HP / attack / damage。

---

# 19. 完成 Lineage Conversion 的最低條件

一隻怪物可以標：

```text
[LINEAGE_CONVERTED_V1]
```

至少要有：

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
known OPEN items（只能是不影響基本運作的 loadout 類）
```

完成後才可以：

```text
→ [ENCOUNTER_CALIBRATION]
```

拿特定 PC 隊伍調整命中率、控制率、TTK 與 encounter pacing。
