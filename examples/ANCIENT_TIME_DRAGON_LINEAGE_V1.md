# 上古時空龍 Ancient Time Dragon — D100 Lineage Conversion v1

> 狀態：`[LINEAGE_CONVERTED_V1]`
>
> 目的：在**不使用亞黛兒／卡蘭德／莎緹拉作平衡標尺**的前提下，先把 Dragon #359 的 Ancient Time Dragon 轉成可運作的 D100 怪物；完成後才進 `[ENCOUNTER_CALIBRATION]`。
>
> 來源：Mike McArtor, *Time Dragon: A Wyrm for the Ages*, Dragon #359 (2007)。
>
> 方法：`90_srd_bridge/MONSTER_CONVERSION_PIPELINE.md`。

---

# 0. 來源衝突與解讀邊界

## HP 印刷值衝突

來源 Ancient 列：

```text
HD 89d12+2403
printed hp: 2,931
```

但公式平均值：

```text
89×6.5 + 2403 = 2,981.5
```

因此保留：

```text
[SOURCE_PRINTED] 2931
[SOURCE_DERIVED] 2981.5
```

## AC OCR 衝突

來源列 Ancient：

```text
AC81
touch3
flat-footed80
size -8
haste dodge +1
```

反推：

```text
natural armor = +78
10 -8 +78 +1 = 81
```

部分 OCR 顯示 `+89 natural`，與 AC81 / touch3 / flat-footed80 不相容，因此：

```text
[SOURCE_DERIVED] natural armor +78
[SOURCE_OCR_UNCERTAIN] +89 不採用
```

## Haste × natural weapon 歧義

3.5 `haste` 原文寫 full attack 時對「weapon he is holding」多一次攻擊；自然武器是否算在內，3.5 RAW 有歧義。

本 Lineage v1 採**保守解讀**：

```text
Time Mastery 不自動多一個 Bite。
```

另保留可切換 interpretation：

```text
[OPTIONAL_RAI] 若團採自然武器也吃 haste extra attack，Full Natural Attack Package 多1次 primary Bite。
```

以下 HP 閉環採保守解讀計算。

---

# 1. Source Profile

```yaml
species: Time Dragon
age_category: Ancient
age_category_index: 10
size: Colossal+
alignment_source: Always Neutral
HD: 89d12+2403
hp_printed: 2931
hp_hd_mean: 2981.5
STR: 83
DEX: 10
CON: 65
INT: 66
WIS: 73
CHA: 66
BAB: 89
grapple: 141
primary_attack: 118
Fort: 73
Ref: 47
Will: 77
breath_DC: 81
frightful_presence_DC: 82
AC: 81
touch_AC: 3
flat_footed_AC: 80
natural_armor_derived: 78
land_speed_listed: 100 ft
fly_speed_listed: 380 ft
fly_maneuverability: clumsy
sorcerer_CL: 31
SR: 85
CR: 76
```

核心能力：

```text
Time Control / immunity to slow
Time Stop at will; Ancient cooldown 1d4 source rounds
Slow 3/day
Draconic Surge 2/day
Time Mastery: continuous haste
Slow Aura: 100 ft, up to10 source rounds/day
Ravaging Time breath
Time Expulsion breath
Frightful Presence
Sorcerer casting CL31
DR20/—
```

沒有 Great Wyrm 的 `Time Apotheosis`。

---

# 2. D100 九屬性

共享六屬性採 modifier 等價：

```text
STR 85
DEX 13
CON 67
INT 69
WIS 75
CHA 69
```

RES 由來源三豁免 chassis：

```text
73 - CONmod27 = 46
47 - DEXmod0  = 47
77 - WISmod31 = 46
→ RES46
```

SPI：天生術士／史詩真龍／時間本質，以 CHA anchor 作 lineage seed：

```text
SPI69
```

SKI：不把 BAB89 直抄；以 epic true dragon 的自然武器熟練與來源命中輪廓建立：

```text
SKI25
```

最終：

```text
STR 85
DEX 13
SKI 25
CON 67
RES 46
INT 69
WIS 75
CHA 69
SPI 69
```

---

# 3. 六基礎值

```text
戰鬥 = 13+25+85 = 123
運動 = 13+25+67 = 105
操作 = 69+25+75 = 169
感知 = 69+46+69 = 184
知識 = (69+75)×1.5 = 216
交涉 = 69+75+69 = 213
```

與時間／位面／奧術／歷史直接相關的 Knowledge 可視為 monster expertise Lv5 seed；其他來源 class-skill Knowledge 至少視為受訓。

---

# 4. 五抗／三特殊

```text
抗毒素 113
抗控制 121
抗轉化 92
抗噴吐 59
抗魔法 115

強韌 335
精神 230
靈魂 345
```

低抗噴吐保留來源 `Ref47` 弱項。

標準 Dragon traits：

- 魔法睡眠免疫；
- 麻痺免疫；
- Time Dragon 對 slow 效果免疫。

---

# 5. 宣告／行動順位

```text
DEX13 → adj0 → 行動順位13
INT69 → adj28 → 宣告順位97
```

時間速度不灌進 DEX，另由時間能力管理。

---

# 6. 體型、空間、reach

```text
space: 40 ft
normal reach: 30 ft
bite reach: 40 ft
ravaging-time line: 160 ft ×5 ft
expulsion cone: 80 ft
```

Colossal+ 來源 size modifier `-8` 在純機率層轉：

```text
D100 size modifier = -40
```

只作用於 contact probability，不修改 raw STR / CON。

---

# 7. 移動與 clumsy flight

來源 printed Ancient：

```text
land100 ft
fly380 ft (clumsy)
```

Young Adult `60/350` → Adult `90/380` 的 +30 跳升與 Time Mastery / haste 一致，因此 Adult+ printed speed 已含 haste；不重複再加。

反推 un-hasted：

```text
land ≈70 ft/source move
fly  ≈350 ft/source move
```

世界速度 seed：

```text
base:   ground12 ft/s, fly58 ft/s
hasted: ground17 ft/s, fly63 ft/s
```

D100 explicit species movement：

```text
正常：ground17, fly63 ft/s
Time Mastery 短暫被壓掉：ground12, fly58 ft/s
```

Clumsy 不再砍 DEX，而是保留幾何限制：

```text
最低前進約半速
不可hover／倒飛／原地reverse
每前進約10ft才可轉約45°
不可原地轉向
單次轉向上限約45°
爬升角≤45°且半速
下降角約≤45°且可雙倍速度
由下降切回爬升前需一段水平飛行
```

---

# 8. Dodge

來源 touch AC 很低、natural armor 很高，因此轉成：

```text
容易接觸龍體
＋
難以打穿
```

給 innate `閃避 Lv0`（無未受訓 -20，也沒有 Lv bonus）：

```text
運動105
+ size -40
+ Time Mastery haste avoidance +5
= Dodge70
```

Time Mastery 暫時失效：

```text
Dodge65
```

Clumsy 另由空間幾何判斷，不重複扣 Dodge。

---

# 9. Natural Armor / DR

來源 natural armor：

```text
+78
```

fallback：

```text
NaturalArmorReduction
= ROUND(sqrt(8×78))
≈25
```

來源 DR20/— 直接保留為：

```text
intrinsic physical resistance20
```

所以：

```text
Natural armor reduction25
Intrinsic physical resistance20
普通物理命中合計 flat reduction45
```

兩層分開記，讓 armor penetration / 物抗穿透各自作用。

---

# 10. 自然武器攻擊

Epic true dragon：

```text
自然武器使用 Lv5 [monster innate proficiency]
```

Primary：

```text
戰鬥123
+ proficiency50
+ size -40
+ Time Mastery attack +5
=138
```

Secondary（來源 Multiattack 後 -2 → D100 -10）：

```text
128
```

所以：

```text
Bite138
Claw/Wing/Tail128
```

Time Mastery 被壓掉：

```text
primary133
secondary123
```

對自己的 Dodge70：

```text
primary hit ≈94.72%
secondary hit ≈90.97%
```

和來源 `+118/+116` 打 AC81 的高命中輪廓相近。

---

# 11. 自然武器傷害

Colossal+ source dice：

```text
bite6d6
claw4d8
wing4d6
tail slap4d8
```

D100 STR adjustment = +36；自然武器 Lv5 傷害層 `+7.5`：

```text
Bite = 6d6 +61.5
Claw = 4d8 +43.5
Wing = 4d6 +25.5
Tail = 4d8 +61.5
```

最終小數依 D100 取整規則。

---

# 12. Full Natural Attack Package

保守 3.5 解讀：

```text
1 Bite
2 Claws
2 Wings
1 Tail Slap
```

共6個 hit instances。

這是一個完整戰術行動包，不是六個免費 general actions。

使用：

- 消耗本秒一般／完整攻擊窗口；
- 不可同時做不相容的完整移動；
- 幾何位置碰不到的器官不能硬生成攻擊。

`[OPTIONAL_RAI]` 若團採 haste 可給 natural weapon 額外攻擊：再加1次 primary Bite。

Draconic Surge 的額外 standard-equivalent action不能購買第二套 Full Attack；只可單次自然武器／spell／SLA 或 move。

---

# 13. HP：closed-loop lineage calibration

## Source self-damage（保守 haste 解讀）

來源完整自然武器 routine：

```text
Bite avg75
2 Claws avg54×2
2 Wings avg32×2
Tail avg72
raw avg319
```

DR20/— 對6次命中：

```text
319 -20×6 =199
```

來源自身高命中約95%：

```text
expected source self-damage ≈189.05
```

Self-TTK：

```text
printed HP2931 →15.50 routines
HD mean2981.5 →15.77 routines
```

## D100 self-damage

flat reduction45 後：

```text
Bite avg82.5 →37.5 effective
Claw avg61.5 →16.5 effective ×2
Wing avg39.5 →0 ×2
Tail avg79.5 →34.5 effective
```

乘命中率：

```text
expected D100 self-damage ≈96.92 / full routine
```

得到：

```text
printed-source path → HP≈1503
HD-mean path       → HP≈1529
```

Lineage range：

```text
1500–1530
```

v1 working value：

```text
HP1515/1515
```

若團採 `[OPTIONAL_RAI]` haste extra natural strike，需使用另一組 HP closed-loop，不可只加 Bite 而不重算耐久。

---

# 14. SP／法術資源

來源 Sorcerer CL31。

```text
自身環數9
總施法者等級31
```

解讀：9環基礎27 + innate caster potency4。

術士法術位：

```text
9×2 + CHAadj28 =46
```

```text
法術位46/46
```

Monster 無玩家 CP 投資史，SP 取最低 base：

```text
RES46 + RESadj17 =63
```

```text
SP63/63
```

術士施法主複合：交涉213。

9環、連續施法懲罰0：

```text
213 +10×(31/3) -90 ≈226.33
→ working226
```

一般 n 環：

```text
約316.33 -10n - continuous penalty
```

來源只指定「as Sorcerer CL31」，沒有固定每隻 Ancient 的 spells known；spell repertoire 屬個體實例化，必須在遭遇前預選，不能戰鬥中按玩家行為臨時生成。

---

# 15. Spell Resistance

來源 SR85。

D100 已由屬性產生：

```text
抗魔法115
```

Lineage v1 不再額外做第二個 `+85` barrier，避免 double-count。

法術穿透走 D100 原本：抗魔法／法術穿透／高等法術穿透。

保留來源 invariant：來源 CR76 級 peer caster 對 SR85 約60% penetration；之後 encounter calibration 若偏離再調專用 SR modifier。

---

# 16. Time Mastery

Ancient 常駐 continuous haste。

```text
不能自願關閉
被 dispel 後，在龍下一個正常 action window 開始自動恢復
```

D100 v1：

```text
attack +5
Dodge / reflexive avoidance +5
movement 使用 hasted listed speed（17 ground /63 fly ft/s）
```

不提供：

```text
第二個 general action
第二次施法
```

自然武器額外一擊採第0節的 source-interpretation 開關，v1 預設不給。

---

# 17. Draconic Surge

```text
2/day
```

特殊快速啟動，額外取得其一：

```text
A. 1個 standard-equivalent action
   - 單次自然武器
   - spell / SLA
   - 其他來源 standard action

B. 1個完整 movement window
```

不能用 A 取得第二套 Full Natural Attack Package。

---

# 18. Time Stop

```text
at will
activation: standard-equivalent general action
cooldown: 結束後等待1d4個 dragon normal action windows
```

一次：

```text
1d4+1 = 2–5 private action windows
```

碼表分支：

```text
external world time：近似停滯
subjective dragon time：2–5完整私人窗口
cooldown：private branch 結束後才開始
```

期間：

- 不能直接 attack / target 其他 frozen 生物；
- 不能直接改動他人攜帶物造成傷害；
- 可 reposition、自我 buff、召喚／建立恢復時間後生效的區域；
- 可用 Draconic Surge，照常消耗；
- private windows 不計入下一次 Time Stop cooldown。

---

# 19. Slow 3/day

D100 slow status：

```text
movement ×0.5
attack -5
Dodge / reflexive avoidance -5
本 tactical window 只能執行1個 major package
不可 Full Natural Attack Package
取消 haste 類額外攻擊 cadence
```

來源 SLA DC 依標準 CHA 推導：

```text
10 + spell level3 + CHAmod28 = DC41
```

Ancient 自身 Will77 約95% resist。

語義防禦：抗轉化92。

Self-save anchor：

```text
抗轉化須過-3 → 約95% self-resist
```

失敗套 slow status；自然極端骰仍依 D100 全域規則。

---

# 20. Slow Aura

```text
radius100 ft
free action maintenance
pool10 tactical windows/day
不必連續
no save
```

每個生物在自己正常 action window 開始時：

```text
位於100ft內 → 自動 slow
```

Time Dragon 自身免疫。

Time Stop private windows 中其他生物沒有 normal window，因此不因 private branch 額外燒 aura pool；回 shared timestream 再計。

沙漏另保留來源約「一分鐘級」總時間語意，但 combat resource 以10 tactical windows計。

---

# 21. Breath Weapon 共通

```text
Ravaging Time line160ft×5ft
Time Expulsion cone80ft
```

共享 recharge：

```text
使用任一吐息後 → 1d4+1 dragon normal action windows
```

不是兩個獨立 recharge。

---

# 22. Ravaging Time

Ancient age category10：

```text
age +10 years：no save（若會老化）
CON damage10
Fort half
object hardness -10
source DC81
```

肉體時間侵蝕在 D100 用 `抗轉化`。

來源自身 Fort73 對 DC81：65% save。

```text
Defense92
M = 92-65 =27
```

所以：

```text
抗轉化須過27
成功：CON damage5
失敗：CON damage10
```

年齡+10年不因成功而取消；那部分來源本來 no save。

物件沒有生物 save；hardness / 結構減傷 seed -10，由 AO 按材料落實。

---

# 23. Time Expulsion

來源：

```text
Will DC81 negates
失敗：被扔到未來10 source rounds
期間 effectively does not exist
```

這是「未來多久」本身構成效果，所以 Lineage v1 採**沙漏／世界時間保真**：

```text
10×6 sec ≈60秒
```

語義防禦：抗轉化92。

來源自身 Will77 對 DC81：85% save。

```text
M = 92-85 =7
```

所以：

```text
抗轉化須過7
成功：留在目前時間
失敗：從 shared world timeline 移除約60秒
```

失敗者：

```text
subjective time≈0
不能行動
目前時間中的效果不能指定它
世界照常前進
約60秒後 timestream catches up，重新存在
```

---

# 24. Frightful Presence

Ancient：

```text
radius = 30ft×10 =300ft
source DC82
```

來源自身 Will77 對 DC82：80% self-save。

D100 語義防禦：精神230。

```text
M = 230-80 =150
```

所以：

```text
精神須過150
```

成功：24小時內對同一條龍的 frightful presence 免疫。

失敗：

- 明顯低階／minion-tier：panic 類；
- 仍屬戰鬥者但低於本龍 lineage tier：shaken / fear 類。

來源 HD gate 不硬換成 CP；peer-tier eligibility 到 encounter calibration 才接 campaign tier。

---

# 25. Crush / Tail Sweep

Colossal+ 巨龍特殊攻擊保留。

## Crush

```text
damage seed = 6d6 +1.5×STRadj = 6d6+54
```

來源 Reflex DC 與 breath 級別相當；Ancient 自己 Ref47 對 DC81 只有 natural-success 級機會。

D100：

```text
抗噴吐59，須過54 ≈5% self-avoid
```

失敗：承受 crush + pinned/壓制語義；成功避開主要落點。

## Tail Sweep

```text
damage seed = 4d6+54
抗噴吐須過54：依來源語義減免／避開
```

仍受來源體型限制，不能拿來掃同等 Colossal+ 生物。

---

# 26. Action Palette

Shared tactical window：

```text
General / full package:1
Free actions:2（D100基本，須相容）
Immediate / special quick:依能力
Movement: explicit species movement
```

General choices：

```text
Full Natural Attack Package
單次自然武器＋合法移動
Breath Weapon
Time Stop
Slow
Sorcerer spell
Crush / Tail Sweep
其他來源 standard-equivalent action
```

特殊：

```text
Slow Aura maintenance → free
Draconic Surge → special quick, 2/day
Time Mastery → passive
Time Stop → private-window branch
```

---

# 27. 開戰 Ledger v1

```text
Ancient Time Dragon

HP1515/1515
SP63/63
Spell slots46/46
Continuous casting penalty0

Action order13
Declaration order97

Dodge70
Natural armor reduction25
Intrinsic physical resistance20
Anti-magic115

Primary natural attack138
Secondary natural attack128

Ground17ft/s
Fly63ft/s (clumsy)

Time Mastery ACTIVE
Time Stop AVAILABLE
Time Stop cooldown0
Draconic Surge2/2
Slow3/3
Slow Aura10/10, inactive
Breath AVAILABLE
Breath recharge0

Observed enemy abilities:none
Threat model:empty
```

---

# 28. 已完成 vs 尚需實例化

本檔已完成：

- 九屬性與基礎值；
- 五抗／三特殊；
- HP / SP；
- attack / dodge；
- natural armor / DR；
- 自然武器 damage；
- size / reach / movement；
- spellcasting resource chassis；
- Action Palette；
- Time Mastery / Surge / Stop / Slow / Aura；
- 兩種吐息；
- frightful presence；
- world-time vs tactical-time timers。

尚需「個體實例化」、不是換算漏洞：

1. Sorcerer spells known / 個體 spell loadout；
2. 個體性格、巢穴、收藏、談判目標；
3. encounter calibration。

下一階段才可以用特定 PC 問：

```text
Lineage v1 對這支隊伍實際上太強／太弱／剛好在哪一層？
```
