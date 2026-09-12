# Ancient Time Dragon — D100 換算工作表 v0.1

> 對象：Mike McArtor, *Time Dragon: A Wyrm for the Ages*, Dragon #359 的 **Ancient／上古時空龍**。
>
> 方法：`90_srd_bridge/COMMON_CONVERSION_REFERENCE.md`
>
> 狀態：全部是 `[D100_ADAPTATION_CANDIDATE]`；尚未經實戰 regression 校準。

---

# 1. 來源核心數值 `[SOURCE_PROFILE]`

```text
Age category: Ancient (10)
Size: Colossal+
HD: 89d12+2403 (2931 hp)
STR 83
DEX 10
CON 65
INT 66
WIS 73
CHA 66
Attack +118
Fort +73
Ref +47
Will +77
Land 100 ft
Fly 380 ft (clumsy)
Sorcerer CL 31
SR 85
CR 76
```

能力：

```text
Time Control
Time Stop at will, 1d4 source rounds cooldown (Adult–Wyrm)
Slow 3/day
Draconic Surge 2/day
Time Mastery (continuous haste)
Slow Aura (Ancient+)
Ravaging Time breath
Time Expulsion breath
Frightful Presence
high Knowledge / languages
```

---

# 2. 共享六屬性：modifier 等價轉譯

公式：

```text
m35 = floor((A35 - 10) / 2)
A100_anchor = 13 + 2*m35
```

| 屬性 | 3.5 | 3.5 mod | D100 anchor | D100 adj |
|---|---:|---:|---:|---:|
| STR | 83 | +36 | **85** | +36 |
| DEX | 10 | +0 | **13** | +0 |
| CON | 65 | +27 | **67** | +27 |
| INT | 66 | +28 | **69** | +28 |
| WIS | 73 | +31 | **75** | +31 |
| CHA | 66 | +28 | **69** | +28 |

這比把 raw score 直接照抄更忠實：來源 DEX10 本來是 modifier 0，不應被 D100 解讀成負敏捷。

---

# 3. RES seed：從來源三豁免拆 chassis

來源：

```text
Fort +73 - CON mod +27 = 46
Ref  +47 - DEX mod  +0 = 47
Will +77 - WIS mod +31 = 46
```

三者高度收斂：

```text
46 / 47 / 46
```

因此第一版：

```text
RES seed = 46
```

這是一個非常漂亮的來源訊號：上古時空龍的三豁免差異主要來自能力值，而底層「史詩巨龍抗性 chassis」約在同一量級。

`RES46` 仍不是 canon；它只是目前最有來源依據的 seed。

---

# 4. SPI seed：由存在本質決定

3.5 沒有 SPI。

本生物是：

```text
不因老化死亡的 epic true dragon
+ 天生術士施法
+ 與時間流存在物理／超自然連結
```

第一版採**保守 seed**：

```text
SPI = CHA anchor = 69
```

理由：來源 CHA 是其天生施法與超自然存在感最接近 D100 SPI 的現成 proxy。

候選範圍：

```text
69 ～ 75
```

若 campaign ontology 明確把其「時間本質」視為比魅力／施法更接近靈魂核心，可向 WIS75 靠攏。

目前工作值：

```text
SPI 69
```

---

# 5. SKI seed：先不要從 BAB89 硬搬

來源 BAB89 是 HD progression，不等於 D100 SKI89。

先建立合理攻擊輪廓。

共享屬性部分：

```text
STR85 + DEX13 = 98
```

若：

```text
SKI 20～30
```

則裸戰鬥基礎：

```text
118～128
```

再加自然武器／龍類戰鬥熟練層，普通近戰 attack 可落在大約：

```text
160～175
```

以目前 D100 高階 PC 約 95～110 的 Dodge 作 benchmark，這會使近身後的普通龍擊具有約 85～95% 級命中壓力，符合來源 `Attack +118` 作為 CR76 epic dragon 的「近身後非常難躲」輪廓。

因此第一版：

```text
SKI seed range = 20～30
working seed = 25
```

注意：這不是說「SKI25 = BAB89」；只是用 encounter probability 反推到的工作值。

---

# 6. 第一版九屬性候選

```text
STR 85
DEX 13
SKI 25   [candidate]
CON 67
RES 46   [candidate]
INT 69
WIS 75
CHA 69
SPI 69   [candidate]
```

---

# 7. D100 六基礎值候選

依 core formula：

```text
戰鬥 = DEX + SKI + STR
     = 13 + 25 + 85
     = 123

運動 = DEX + SKI + CON
     = 13 + 25 + 67
     = 105

操作 = INT + SKI + WIS
     = 69 + 25 + 75
     = 169

感知 = INT + RES + SPI
     = 69 + 46 + 69
     = 184

知識 = (INT + WIS) × 1.5
     = 144 × 1.5
     = 216

交涉 = CHA + WIS + SPI
     = 69 + 75 + 69
     = 213
```

這個輪廓符合來源：

- 肉體技巧不是核心賣點；
- 知識／感知／交涉／施法心智能力極端高；
- 近戰可靠主要來自巨大力量＋龍類熟練，而不是 DEX。

---

# 8. 五抗／三特殊候選

以 `RES46`：

```text
抗毒素 = RES + CON = 113
抗控制 = RES + WIS = 121
抗轉化 = RES × 2   = 92
抗噴吐 = RES + DEX = 59
抗魔法 = RES + INT = 115
```

三特殊：

```text
強韌 = CON ×5 = 335
精神 = RES ×5 = 230
靈魂 = SPI ×5 = 345
```

### 重要：不要看到「抗噴吐59」就急著補高

來源也是：

```text
Fort 73
Ref  47  ← 明顯弱項
Will 77
```

所以 D100 的低抗噴吐可能反而是在忠實保留來源「巨大、硬、聰明，但不是靠敏捷反射防禦」的結構。

若 Time Mastery / magic defense 能改善範圍攻擊生存，應由那個能力另外提供，而不是偷偷拉高 DEX／抗噴吐。

---

# 9. 宣告與行動順位候選

D100 adjustment：

```text
DEX13 → adj 0
INT69 → adj +28
```

所以：

```text
行動順位 seed = 13
宣告順位 seed = 69 + 28 = 97
```

結構：

```text
肉體 initiative 普通
＋
戰術資訊優勢極高
```

真正時間加速由 Time Mastery 等能力處理，不灌進 DEX。

---

# 10. AC 拆解：這隻龍不應該是高 Dodge 坦克

來源 Ancient 的 AC 主要來自**巨量 natural armor**，而 touch defense 很低；同時飛行 maneuverability 是 `clumsy`。

因此 D100 要保留：

```text
容易被「碰到」
≠
容易被「打傷」
```

### 暫定方向

```text
Dodge：中低，靠位置／時間能力改善
Armor / 物抗：極高
DR：保留「20/— 等級的來源結構」，但數值需用 D100 damage benchmark 校準
Temporal defense：Time Stop / Slow / positioning，獨立於 Dodge
```

不要把來源 Natural Armor 全部變成 D100 Dodge。

### Dodge 尚未定值

運動基礎 105 不代表空戰 Dodge105 一定合理。

因為來源另有：

```text
Colossal+
fly clumsy
very low touch defense
```

需要先建立 D100 的體型／飛行機動性修正，再定最終 Dodge。

工作目標：

```text
普通攻擊應相對容易接觸龍體
但有效傷害應被 armor / DR 大量吸收
```

---

# 11. Attack 目標，不直接照抄 +118

來源 `Attack +118` 的資訊價值是：

> 同階戰鬥中，它一旦讓巨大龍體真正貼到你，物理攻擊非常可靠。

D100 第一版 target：

```text
ordinary natural attack ≈ 160～175
```

若 working：

```text
戰鬥基礎 123
+ 自然武器／龍類熟練 40～50
≈ 163～173
```

這個「40～50」目前只是 monster proficiency layer 候選；需要確認是否應用既有武器使用技能、怪物專用熟練，或不另設名稱。

所以此處不登錄一個假 canonical 技能。

---

# 12. HP / armor / DR：先用 TTK，2931 不直接搬

來源：

```text
2931 hp
massive natural armor
DR
SR85
```

這表示它是「多層防禦」而不是純血牛。

D100 不應：

```text
HP = 2931
```

第一版先定 encounter goal：

```text
三名高階 PC 若能穩定建立有效傷害窗口，
上古時空龍不應被一擊蒸發，
也不應需要數十秒純磨血。

它更可能在自身判斷風險過高以前撤退，
所以「打到0 HP」不是唯一戰鬥終點。
```

待測項：

1. 三名 PC 的單次／每秒有效 DPR；
2. armor / DR 後的成功重擊數；
3. 龍的撤退 threshold；
4. 回復／防護法術。

在完成 benchmark 前：

```text
HP = PENDING
物抗 = PENDING
自然甲／DR = PENDING
```

---

# 13. Spell Resistance：SR85 不換成抗魔法85

目前基礎屬性給：

```text
抗魔法 = 115
```

但來源 `SR85` 是 epic spell resistance，還包含來源 caster-level check 的特殊概率結構。

因此：

```text
抗魔法115 = attribute layer seed
+
是否另有「史詩法抗／SR layer」 = PENDING
```

需要拿亞黛兒／卡蘭德／莎緹拉的實際：

- 施法成功值；
- 法術穿透；
- 高等法術穿透；
- spell level；

做突破率 calibration 後再定。

---

# 14. Caster Level

來源：

```text
Sorcerer CL31
```

D100 不直接稱它為 canon CL31，但 CL31 可以作非常強的 seed。

第一版方向：

```text
最高法術環：9環級／epic source profile
D100 total caster level seed：約31
```

因為 D100：

```text
9環基礎 total caster level = 9×3 = 27
```

來源 CL31 可被理解為：

```text
9環級施法者 + 約4點額外 caster-level potency
```

實際法術位、SP、施法技能與 spell list 仍需另建。

---

# 15. 移動第一版

來源：

```text
Land 100 ft / move action
Fly 380 ft / move action (clumsy)
3.5 round ≈ 6 sec
```

世界速度 seed：

```text
land ≈ 100/6 = 16.7 ft/s
fly ≈ 380/6 = 63.3 ft/s
```

這只負責**沙漏／世界物理速度**。

戰鬥中：

- Time Mastery；
- double move；
- charge；
- dive；
- Time Stop reposition；

要由碼表另外處理。

---

# 16. Time Mastery：重要修正

來源不是「每輪多一個 standard action」。

它是：

```text
continuous haste
```

3.5 haste 的核心戰術效果包含：

- full attack 時多一次攻擊；
- 攻擊／AC／Reflex 小幅改善；
- movement speed 增加；
- **不提供第二個 standard action，也不能因此再施放第二個法術。**

因此 D100 Time Mastery 第一版應轉成：

```text
持續時間加速狀態
+ movement boost
+ attack cadence / extra strike within an attack action
+ small avoidance / reaction benefit
```

而不是：

```text
每秒額外一般動作
```

最終精確值等待 D100 haste / attack-package 對應。

---

# 17. Draconic Surge：真正的額外 action

來源 Ancient：

```text
2/day
swift activation
extra standard OR move action this turn
```

D100 第一版：

```text
2/day
特殊快速啟動
→ 本秒額外取得 1 個「一般動作或完整移動」窗口
```

它可以與 Time Mastery 同時存在，因為來源本來就是兩個不同能力。

碼表必須獨立記：

```text
Draconic Surge: 2/2
```

---

# 18. Time Stop：採「戰術窗口保真」作第一版

來源 spell 的核心不是「角色真的在世界外多活 12～30 秒」，而是：

> 施法者取得數個只有自己能行動的 turn。

因此第一版 Encounter mode：

```text
Time Stop duration:
來源 1d4+1 rounds
→ D100 2～5 個 private action windows
```

外界：

```text
external world time 不正常前進
```

使用者主觀：

```text
取得 2～5 個自己的行動窗口
```

來源 Ancient cooldown：

```text
1d4 rounds between uses
```

第一版同樣採戰術 cadence：

```text
等待 1d4 個「龍自己的正常 action windows」後再次 available
```

不是機械寫成 6d4 D100 seconds。

這是 `[ENCOUNTER_CONVERSION_V0.1]`；若未來要跑嚴格世界物理版，可以另測 world-time mode。

---

# 19. Slow Aura：第一版也採 tactical-duration pool

來源：

```text
radius = 10 ft × age category = 100 ft
up to 10 rounds/day
free action each round to maintain
creatures beginning turn in aura are automatically slowed, no save
```

第一版 Encounter mode：

```text
radius 100 ft
維持池 10 個 tactical windows / day
不必連續
每個本輪開始時仍在 aura 中的生物，套用 D100 slow 對應
```

不用 ×6 變成 60 個戰鬥窗口，因為來源設計意義是「約一場戰鬥的時間資源」。

若將它拿到非戰鬥世界事件中，沙漏可以另記其物理持續時間約一分鐘。

這正是：

```text
碼表：10 個戰術窗口
沙漏：約60秒來源世界意義
```

兩層同時保存。

---

# 20. Ravaging Time breath

來源 Ancient 為第10 age category：

```text
age 10 years (no save)
CON damage 10, Fortitude half
object hardness -10, Fort-like reduction不適用物件
```

D100 第一版因共享屬性尺度已做 modifier 等價，可先測：

```text
命中／暴露：依吐息範圍處理
時間老化10年：敘事效果直接成立（若生物會老化）
CON damage：10 seed
防禦接口：抗轉化／強韌的具體分層待測
```

重要：

```text
「老化10年」與「CON傷害」是兩個來源效果成分，
但不代表要無理由連骰兩次。
```

先建立因果：

```text
時間侵蝕命中
→ 年齡推進
→ 肉體承受／CON damage
```

再決定是否真的需要兩個獨立 D100 判定。

---

# 21. Time Expulsion breath

來源 Ancient：

```text
失敗 → 往未來移動10 source rounds
```

這個效果本質是**從當前時間線移除 N 個戰術輪**。

第一版 Encounter mode：

```text
失敗 → 從當前場景移除10個 D100 tactical windows
```

不是 60 個 D100 行動輪。

但沙漏另記來源的世界時間語意：

```text
約一分鐘後重新同步
```

是否採 10秒還是60秒重新出現，要看此能力最終選擇：

- tactical identity；或
- world-time identity。

**此項目前仍保持 OPEN，不在 v0.1 硬定。**

理由：它不像 buff duration；它直接改變角色「何時重新存在」，世界時間本身就是能力核心。

---

# 22. 第一版可直接帶進下一次戰鬥的部分

可以先使用：

```text
STR 85
DEX 13
SKI 25 [candidate]
CON 67
RES 46 [candidate]
INT 69
WIS 75
CHA 69
SPI 69 [candidate]

戰鬥 123
運動 105
操作 169
感知 184
知識 216
交涉 213

抗毒素 113
抗控制 121
抗轉化 92
抗噴吐 59
抗魔法 115
強韌 335
精神 230
靈魂 345

行動順位 13
宣告順位 97

Draconic Surge 2/day
Slow 3/day
Slow Aura radius 100 ft
Time Mastery = continuous haste identity
```

仍不能假裝已完成：

```text
HP
Dodge
Armor / 物抗
Natural attack final score
Natural attack damage
SR final layer
Spell list / spell slots / SP
Slow 的 D100 精確效果
Time Stop 最終細節
兩種吐息最終抵抗接口
```

---

# 23. 下一輪 regression 要測什麼

這份換算不是靠「看起來合理」就畢業。

下一場正式空戰至少記：

1. 龍的普通攻擊實際命中率是否接近來源定位；
2. PC 是否很容易碰到龍、但難造成有效傷害；
3. 低抗噴吐是否造成合理弱點，還是失真；
4. Time Mastery 是否有存在感但沒有偷變成額外完整 action；
5. Draconic Surge 是否成為真正額外 action spike；
6. Time Stop 2～5 private windows 是否已經過強／過弱；
7. Slow Aura 是否真的在三維空戰中製造 100 ft 區域壓力；
8. 高 INT／WIS 是否表現在戰術決策，而不是讀玩家卡；
9. HP／armor 應該如何依 PC 真實輸出回推。

測完再把 `[candidate]` 收斂成 `[ENCOUNTER_CALIBRATED]`。
