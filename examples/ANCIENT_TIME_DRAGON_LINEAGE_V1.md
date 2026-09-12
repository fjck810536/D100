# 上古時空龍 Ancient Time Dragon — D100 Lineage Conversion v1

> 狀態：`[LINEAGE_CONVERTED_V1]`
>
> 目的：在**不使用亞黛兒／卡蘭德／莎緹拉作平衡標尺**的前提下，先把 Dragon #359 的 Ancient Time Dragon 完整轉成可運作的 D100 怪物。
>
> 之後才能另做 `[ENCOUNTER_CALIBRATION]`。
>
> 來源：Mike McArtor, *Time Dragon: A Wyrm for the Ages*, Dragon #359 (2007)。
>
> 方法：`90_srd_bridge/MONSTER_CONVERSION_PIPELINE.md`。

---

# 0. 來源衝突先保留

Dragon #359 Ancient 列：

```text
HD 89d12+2403
printed hp: 2,931
```

但公式平均值：

```text
89×6.5 + 2403 = 2,981.5
```

因此本檔保留：

```text
[SOURCE_PRINTED] 2931
[SOURCE_DERIVED] 2981.5
```

不擅自假裝兩者一致。

AC OCR 也有衝突。來源列 Ancient：

```text
AC81
touch3
flat-footed80
size -8
haste dodge +1
```

由 AC 算術可反推出：

```text
natural armor = +78
10 -8 +78 +1 = 81
```

部分 OCR 顯示 `+89 natural`，與 AC81 / touch3 / flat-footed80 不相容，因此本檔使用：

```text
[SOURCE_DERIVED] natural armor +78
[SOURCE_OCR_UNCERTAIN] +89 不採用
```

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
Slow Aura: Ancient+, 100 ft, 10 source tactical rounds/day
Ravaging Time breath
Time Expulsion breath
Frightful Presence
Sorcerer casting CL31
DR 20/—（由 Very Old 階段取得並保留）
```

不具有 Great Wyrm 的 `Time Apotheosis`。

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

RES 由三豁免 chassis：

```text
73 - CONmod27 = 46
47 - DEXmod0  = 47
77 - WISmod31 = 46
→ RES 46
```

SPI：天生術士／史詩真龍／時間本質，以 CHA anchor 作 lineage seed：

```text
SPI 69
```

SKI：不把 BAB89 直接抄成 SKI；以 epic true dragon 的自然武器熟練、來源命中輪廓建立：

```text
SKI 25
```

最終 v1：

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

其中 SKI / RES / SPI 仍屬 `[D100_ADAPTATION]`，但已足以形成閉環版本。

---

# 3. 六基礎值

```text
戰鬥 = 13+25+85  = 123
運動 = 13+25+67  = 105
操作 = 69+25+75  = 169
感知 = 69+46+69  = 184
知識 = (69+75)×1.5 = 216
交涉 = 69+75+69 = 213
```

技能傾向：

- 與時間、位面、奧術、歷史直接相關的 Knowledge：視為 monster expertise Lv5 seed；
- 其他來源明列為 class skill 的 Knowledge：至少視為受訓，不套未受訓 -20；
- 語言能力極廣，但具體語言仍依 campaign 世界確認。

---

# 4. 五抗／三特殊

```text
抗毒素 = RES+CON = 113
抗控制 = RES+WIS = 121
抗轉化 = RES×2   = 92
抗噴吐 = RES+DEX = 59
抗魔法 = RES+INT = 115

強韌 = CON×5 = 335
精神 = RES×5 = 230
靈魂 = SPI×5 = 345
```

低抗噴吐是刻意保留的來源弱點：Ancient 的 Ref47 明顯低於 Fort73 / Will77。

標準 Dragon traits 仍保留：

- 對魔法睡眠免疫；
- 對麻痺免疫；
- Time Dragon 對 slow 效果免疫。

---

# 5. 宣告／行動順位

```text
DEX13 → adj0
行動順位 = 13

INT69 → adj28
宣告順位 = 97
```

結構：

```text
肉體 initiative 普通
＋
極高的資訊後手／宣告優勢
```

時間速度不灌進 DEX，另外由 Time Mastery / Time Stop / Draconic Surge 管。

---

# 6. 體型、空間與 reach

直接保留來源物理尺度：

```text
space: 40 ft
normal reach: 30 ft
bite reach: 40 ft
ravaging-time line: 160 ft × 5 ft
expulsion cone: 80 ft
```

Colossal+ 的來源 size attack / AC modifier `-8` 在純概率層轉成：

```text
D100 size modifier = -40
```

這個 -40 只作用於需要反映「巨大目標／巨大攻擊者」的 contact probability，不去改 raw STR / CON。

---

# 7. 移動與 clumsy flight

來源 printed Ancient speed：

```text
land 100 ft
fly 380 ft (clumsy)
```

來源從 Young Adult `60 / 350` 到 Adult `90 / 380` 的跳升正好對應 Time Mastery 的 haste +30 ft，因此 printed Adult+ speed 已包含 haste。

為避免 double-count：

```text
unhasted lineage land ≈ 70 ft / source move action
unhasted lineage fly  ≈ 350 ft / source move action
```

換成世界物理速度 seed：

```text
base land ≈ 70/6  = 11.7 → 12 ft/s
base fly  ≈ 350/6 = 58.3 → 58 ft/s
```

Time Mastery 常駐後：

```text
active land ≈ 17 ft/s
active fly  ≈ 63 ft/s
```

因此 D100 本怪物採 explicit species movement：

```text
正常狀態：ground 17 ft/s, fly 63 ft/s
Time Mastery 被壓掉的短暫空窗：ground 12 ft/s, fly 58 ft/s
```

## Clumsy geometry

不再額外砍 DEX；直接保留幾何限制：

```text
最低前進速度：至少約當前 fly speed 的 1/2
不可 hover
不可倒飛
不可原地 reverse
每前進約10 ft 才能轉約45°
不可原地轉向
單次轉向上限約45°
向上最大角度45°
爬升速度約半速
向下最大角度45°
下降速度可到雙倍
由下降切回爬升前需有一段水平飛行
```

這些由「碼表」與三維位置追蹤，不化成單一 `-20 Dodge`。

---

# 8. Dodge

來源 touch AC 很低，natural armor 很高，所以 D100 應是：

```text
容易碰到龍體
＋
難以打穿
```

本怪物給 innate `閃避 Lv0`（不承受未受訓 -20，但沒有 Lv bonus）。

```text
運動 105
+ size -40
+ Time Mastery / haste avoidance +5
= Dodge 70
```

Time Mastery 暫時失效時：

```text
Dodge 65
```

Clumsy 的限制另外作用於「這個方向實際能不能轉出去」，不重複砍 Dodge。

---

# 9. Natural Armor / DR

來源 derived natural armor：

```text
+78
```

依 fallback：

```text
NaturalArmorReduction
= ROUND(sqrt(8×78))
≈ 25
```

來源已有：

```text
DR 20/—
```

此能力沒有 bypass，因此 lineage seed 直接保留：

```text
intrinsic physical resistance = 20
```

D100 防禦分層：

```text
Natural armor reduction: 25
Intrinsic physical resistance: 20
普通物理命中合計 flat reduction: 45
```

兩層分開記，方便日後處理：

- armor penetration；
- 物抗穿透；
- 爆擊；
- 特殊無視鎧甲效果。

---

# 10. 自然武器攻擊值

Epic true dragon 給：

```text
自然武器使用 Lv5 [monster innate proficiency]
```

D100 primary：

```text
戰鬥123
+ proficiency50
+ Colossal+ size -40
+ Time Mastery haste attack +5
= 138
```

因此：

```text
Bite primary attack: 138
```

來源 secondary natural attacks 在 Multiattack 後約 -2；轉成 D100 -10：

```text
Claw / Wing / Tail secondary attack: 128
```

若 Time Mastery 被壓掉：

```text
primary 133
secondary 123
```

對自己的 Dodge70：

```text
primary hit ≈ 94.72%
secondary hit ≈ 90.97%
```

和來源 Ancient 自身 `+118 / +116` 打 AC81 幾乎只會 natural-1 miss 的輪廓相近。

---

# 11. 自然武器傷害

Colossal+ epic dragon source dice：

```text
bite 6d6
2 claws 4d8
2 wings 4d6
tail slap 4d8
```

D100 STR adjustment = source STR modifier = +36。

自然武器 Lv5 的 D100 武器技能傷害層：

```text
5×1.5 = +7.5
```

因此：

```text
Bite
= 6d6 + 1.5×36 + 7.5
= 6d6 + 61.5

Claw
= 4d8 + 36 + 7.5
= 4d8 + 43.5

Wing
= 4d6 + 0.5×36 + 7.5
= 4d6 + 25.5

Tail slap
= 4d8 + 1.5×36 + 7.5
= 4d8 + 61.5
```

最終擲骰依 D100 小數取整規則處理。

---

# 12. Full Natural Attack Package

這是一個特殊的**完整戰術行動包**，不是六個免費一般動作。

正常 Time Mastery 狀態：

```text
2 × Bite   （haste 額外一個 primary strike）
2 × Claw
2 × Wing
1 × Tail Slap
```

共 7 個 hit instances。

使用條件：

- 消耗本秒的一般／完整攻擊窗口；
- 不能同時再做不相容的完整移動；
- 只允許很小幅度的戰鬥 reposition；
- 若幾何位置無法讓器官接觸目標，對應攻擊不能硬生成。

`Draconic Surge` 的額外 standard-equivalent action **不能再買一整套 Full Natural Attack Package**；它可以買：

- 單次 Bite / Claw / Tail；
- 一個 standard-equivalent spell / SLA；
- 或完整移動窗口。

---

# 13. HP：closed-loop lineage calibration

## 13.1 Source self-damage

Time Mastery / haste full attack：

```text
2 bite:  (6d6+54) ×2 → avg 75×2
2 claw:  (4d8+36) ×2 → avg 54×2
2 wing:  (4d6+18) ×2 → avg 32×2
1 tail:  (4d8+54)    → avg 72
raw avg = 394
```

DR20/— 對 7 個 hit instances：

```text
394 - 20×7 = 254
```

來源 self-hit 約95%，所以：

```text
expected source self-damage ≈ 241.3 / full routine
```

來源 self-TTK：

```text
using printed HP2931  → 12.15 routines
using HD mean2981.5   → 12.36 routines
```

## 13.2 D100 self-damage

在 flat physical reduction45 後：

```text
Bite avg82.5 → 37.5 effective ×2
Claw avg61.5 → 16.5 effective ×2
Wing avg39.5 → 0 effective ×2
Tail avg79.5 → 34.5 effective ×1
```

乘自己的命中率：

```text
expected D100 self-damage ≈ 132.44 / full routine
```

因此：

```text
2931 source path → HP ≈ 1609
2981.5 source path → HP ≈ 1636
```

Lineage range：

```text
1610–1640 HP
```

本 v1 取中間且方便追蹤的 working value：

```text
HP = 1620
```

這不是 encounter balance；它只保留「這條龍大約要承受十餘套自己的 hasted full attack 才會倒」的來源耐久輪廓。

---

# 14. SP / 法術資源

來源：

```text
Sorcerer CL31
```

Lineage：

```text
自身環數：9
總施法者等級：31
```

解讀：

```text
9環基礎27
+ innate caster potency 4
=31
```

術士法術位：

```text
ring×2 + CHA adj
= 18 + 28
= 46
```

因此：

```text
法術位 = 46/46
```

Monster 沒有玩家 CP 投資史，因此 SP 先取 D100 最低 base：

```text
RES46 + RESadj17 = 63
```

所以：

```text
SP = 63/63
```

若日後 source spell-capacity reconstruction 證明應有額外資源，再以來源補，不因 Boss 身分先加。

術士施法主複合值：

```text
交涉 = 213
```

零連續施法懲罰時，9環：

```text
213 + 10×(31/3) - 90
≈ 226.33
→ working casting value 226
```

一般 n 環：

```text
約 316.33 - 10n - continuous penalty
```

連續施法懲罰照 D100 正常追蹤，不因怪物是 Boss 免除。

### Spell repertoire

來源只給「as Sorcerer CL31」，沒有替每一隻 Ancient 個體固定 spells known。

所以：

> spell repertoire 是**個體實例化／NPC loadout**，不是數值換算缺口。

在正式遭遇前必須預先選好，不能戰鬥中看到玩家行為才聲稱「牠剛好會那招」。

---

# 15. Spell Resistance

來源：

```text
SR85
```

D100 已由屬性得到：

```text
抗魔法115
```

Lineage v1 規則：

```text
SR85 不再額外變成第二個 +85 barrier。
```

法術是否穿透，走 D100：

- 抗魔法115；
- 法術穿透；
- 高等法術穿透；
- 相關 spell interface。

保留來源 invariant：

```text
對來源 CR76 級 peer caster，SR85 約是60%可穿透的 gate。
```

之後 encounter calibration 若 D100 peer caster 明顯偏離，再調專用 SR modifier；v1 不 double-count。

---

# 16. Time Mastery

Ancient 常駐。

不是額外 standard action。

D100 v1：

```text
persistent; cannot voluntarily suppress
若被 dispel：到龍下一個正常 action window 開始自動恢復
無需動作
```

效果：

```text
attack checks +5
Dodge / reflexive avoidance +5
active movement 使用 17 ft/s ground, 63 ft/s fly
Full Natural Attack Package 多 1 次 primary Bite
免疫 slow（物種能力）
```

不提供：

```text
第二個 general action
第二次施法
第二套 full attack
```

---

# 17. Draconic Surge

```text
2/day
```

特殊快速啟動，從未來借一個來源 standard/move action。

D100：

```text
Draconic Surge remaining: 2/2
```

啟動後本 tactical window 額外取得其一：

```text
A. 1個 standard-equivalent action
   - 單次自然武器攻擊
   - 一個一般 spell / SLA
   - 其他來源 standard action

B. 1個完整 movement window
```

不能用 A 取得第二套 Full Natural Attack Package。

可與 Time Mastery 同時存在。

---

# 18. Time Stop

```text
at will
activation: standard-equivalent general action
Ancient cooldown: 1d4 normal dragon action windows
```

一次 Time Stop：

```text
1d4+1 private action windows
= 2–5 private windows
```

碼表同時記：

```text
external world time: 不正常前進／近似停滯
subjective dragon time: 2–5完整私人窗口
cooldown: Time Stop 結束後才開始數 normal windows
```

Time Stop 期間：

- 其他生物不能被龍直接 attack / spell-target；
- 他人與其攜帶物不能直接被操作成傷害；
- 龍可以 reposition；
- 可以 self-buff；
- 可以召喚／設置在時間恢復後才影響他人的持續區域或障礙；
- 可以用 Draconic Surge，但照常消耗 2/day；
- private windows **不計入**下一次 Time Stop 的 1d4 normal-window cooldown。

這個能力是「碼表」的 private branch，不是瞬間傳送。

---

# 19. Slow 3/day

來源 slow 的核心：

```text
standard OR move（不能兩者都做）
不能 full attack
attack / AC / Ref -1
speed half
```

D100 v1 slow status：

```text
movement speed ×0.5
attack -5
Dodge / reflexive avoidance -5
本 tactical window 只能執行 1 個 major package
不可 Full Natural Attack Package
不可取得 haste 類 extra-strike cadence
```

若來源個體 SLA DC 依標準 CHA 計算：

```text
DC = 10 + spell level3 + CHAmod28 = 41 [SOURCE_DERIVED]
```

Ancient 自己 Will77 對 DC41 僅 natural failure 風險，約95% resist。

語義防禦用：

```text
抗轉化92
```

self-save anchor：

```text
須過 -3 ≈ 95% self-resist
```

所以 Slow 3/day：

```text
抗轉化須過 -3 → resist
失敗 → 套 slow status
```

自然大失敗／大成功仍依 D100 全域規則處理。

---

# 20. Slow Aura

Ancient 新能力。

```text
radius: 100 ft
maintenance: free action / shared tactical window
pool: 10 tactical windows/day
need not be consecutive
save: none
```

每個生物在自己的正常 action window 開始時：

```text
若位於 aura 100 ft 內
→ 自動套用 slow status
```

Time Dragon 本身免疫 slow。

碼表：

```text
Slow Aura active: false/true
Slow Aura pool: 10/10
```

Time Stop private windows 中，其他生物沒有正常 action window，因此不額外消耗「為了影響他人」的 aura pool；回到 shared timestream 後再計。

沙漏另記來源大約具有「一分鐘級」總世界時間語意，但戰鬥資源以 10 tactical windows 控制。

---

# 21. Breath Weapon 共通

Colossal+：

```text
Ravaging Time line: 160 ft ×5 ft
Time Expulsion cone: 80 ft
```

來源龍吐息：

```text
recharge 1d4+1 source rounds
```

Lineage combat 採 tactical cadence：

```text
使用任一吐息後
→ shared Breath Recharge = 1d4+1 dragon normal action windows
```

兩種吐息共用這個呼吸／器官 recharge，不各自開獨立計時器。

---

# 22. Ravaging Time

Ancient age category10：

```text
命中後自動 age +10 years（若該生物會老化）
CON damage 10
Fortitude half
object hardness -10
source DC81
```

老化十年本身：

```text
no save
```

肉體時間侵蝕的 D100 防禦：

```text
抗轉化
```

來源 Ancient 自己 Fort73 對 DC81：

```text
需要8+ → 65% save
```

D100 self-save anchor：

```text
Defense92
M = 92 - 65 = 27
```

因此 v1：

```text
Ravaging Time：抗轉化須過27
成功：CON damage 5
失敗：CON damage 10
```

年齡 +10 年不因此 save 消失；來源本來就是 no save aging + Fort half CON damage。

物件：

```text
hardness / 結構性減傷 seed -10
```

若 D100 物件沒有 hardness 值，AO 依實際材料把「永久降低10級來源硬度」轉成結構損傷，不替物件硬造生物 save。

---

# 23. Time Expulsion

來源 Ancient：

```text
Will DC81 negates
失敗：被扔到未來 10 source rounds
期間 effectively does not exist
```

這裡採**沙漏／世界時間保真**，因為「未來多久」就是能力本體，不只是 buff cadence：

```text
10 × 6 sec = 約60秒
```

語義防禦：

```text
抗轉化92
```

來源 Ancient 自己 Will77 對 DC81：

```text
需要4+ → 85% save
```

D100 self-save anchor：

```text
M = 92 - 85 = 7
```

所以：

```text
Time Expulsion：抗轉化須過7
成功：留在目前時間
失敗：從 shared world timeline 移除約60秒
```

失敗者：

```text
subjective time ≈ 0
不能行動
不能被目前時間中的效果指定
世界其他事件照常前進
約60秒後 timestream catches up，重新存在
```

這是「沙漏」事件，不把它縮成10個 D100 秒。

---

# 24. Frightful Presence

Ancient age category10：

```text
radius = 30 ft ×10 = 300 ft
source DC82
```

來源 Ancient Will77 對 DC82：

```text
需要5+ → 80% self-save
```

D100 語義：恐怖／心智承載 → `精神230`。

self-save anchor：

```text
M = 230 - 80 = 150
```

所以 lineage v1：

```text
Frightful Presence radius 300 ft
精神須過150
```

成功：

```text
24小時內對同一條龍的 frightful presence 免疫
```

失敗：

- 明顯低階／minion-tier：panic 類狀態；
- 仍屬戰鬥者但低於本龍 lineage tier：shaken / fear 類狀態。

來源 HD gate 不硬換成 CP；peer-tier / higher-tier 的 eligibility 到 encounter calibration 才接 campaign tier。

---

# 25. Crush / Tail Sweep

Colossal+ epic dragon 可以保留巨大龍體特殊攻擊。

## Crush

```text
area / body attack
source damage seed: 6d6 + 1.5×STRmod
D100 damage seed: 6d6 +54
```

來源 save 以 dragon breath DC 級別處理；Ancient 自己 Ref47 對 DC81 只有 natural-success 級機會。

D100 reflex-like interface：

```text
抗噴吐59
self-anchor 約5% success
→ 須過54
```

失敗：

```text
承受 crush damage + pinned/壓制語義
```

成功：避開主要身體落點。

## Tail Sweep

保留來源半圓大範圍尾掃的空間效果。

```text
damage seed: 4d6 +54
抗噴吐須過54：依來源語義減免／避開
```

具體可掃到哪些體型仍依來源 size restriction，不能拿來掃同等 Colossal+ 生物。

---

# 26. Spell / time effects 的 Action Palette

正常 shared tactical window：

```text
General / full package: 1
Free actions: 2（D100 基本；須相容）
Immediate / special quick windows: 依能力
Movement: explicit species movement
```

可選 general package：

```text
Full Natural Attack Package
單次自然武器＋合法移動
Breath Weapon
Time Stop
Slow
Sorcerer spell
Crush / Tail Sweep（若幾何成立）
其他來源 standard-equivalent action
```

特殊：

```text
Slow Aura maintenance → free
Draconic Surge → special quick activation, 2/day
Time Mastery → passive
Time Stop → 建立 private-window branch
```

DM 必須維護 action ledger，不能把這隻龍降格成「每秒一個爪擊」。

---

# 27. 開戰 Ledger v1

```text
Ancient Time Dragon

HP 1620 / 1620
SP 63 / 63
Spell slots 46 / 46
Continuous casting penalty 0

Action order 13
Declaration order 97

Dodge 70
Natural armor reduction 25
Intrinsic physical resistance 20
Anti-magic 115

Primary natural attack 138
Secondary natural attack 128

Ground 17 ft/s
Fly 63 ft/s (clumsy)

Time Mastery ACTIVE
Time Stop AVAILABLE
Time Stop cooldown 0
Draconic Surge 2/2
Slow 3/3
Slow Aura 10/10, inactive
Breath AVAILABLE
Breath recharge 0

Observed enemy abilities: none
Threat model: empty
Retreat threshold: individual/personality decision, not HP script
```

---

# 28. 目前仍需「實例化」而不是「換算」的項目

這些不阻止本檔成為 `[LINEAGE_CONVERTED_V1]`：

1. **Sorcerer spells known / 個體 spell loadout**  
   來源沒有替每一條 Ancient Time Dragon 固定同一套 known spells；遭遇前必須選好。

2. **個體性格、巢穴、收藏、談判目標**  
   屬於生態學家／個體模板，不是數值換算。

3. **Encounter calibration**  
   還沒有拿任何特定 PC 的命中率、控制率、DPR、法術穿透調整本數值。

因此下一階段才能問：

```text
這個 Lineage v1 對亞黛兒／卡蘭德／莎緹拉是太強、太弱，還是剛好？
```

而不是反過來用三人數值決定「時空龍本來應該是什麼」。
