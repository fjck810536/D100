# 上古時空龍（Ancient Time Dragon）— 空戰壓力測試登錄

> 用途：目前三名 PC（亞黛兒／卡蘭德／莎緹拉）的高階 D100 空戰、時間能力與 Action Economy 壓力測試。
>
> 來源物種模型：`examples/TIME_DRAGON_DRAGON359_MODEL.md`
>
> 換算方法：`90_srd_bridge/COMMON_CONVERSION_REFERENCE.md`
>
> 目前換算工作表：`examples/ANCIENT_TIME_DRAGON_CONVERSION_WORKSHEET.md`
>
> **版本鎖定：** Mike McArtor, *Time Dragon: A Wyrm for the Ages*, Dragon #359 (September 2007), pp. 36–40。

本檔不是 D100 Sheet 正典。來源資料標 `[SOURCE_PROFILE]`；換算候選標 `[D100_ADAPTATION_CANDIDATE]`；完成實戰校準後才可標 `[ENCOUNTER_CALIBRATED]`。

---

# 1. 本次個體 `[ENCOUNTER_DEFAULT]`

```yaml
species: Time Dragon
source: Dragon #359
age_category: Ancient
zh_age_category: 上古
sex: 未指定
chronological_age: 未知；不得由 Ancient 反推實際歲數
alignment_source: Always Neutral
initial_attitude: 冷淡、警戒、非嗜殺
encounter_role: 高階空戰／時間流／action-economy 壓力測試
```

本次正式使用 **Ancient／上古時空龍**。

前面測試曾暫填的：

```text
Attack 112
Dodge 105
```

全部作廢。

---

# 2. Dragon #359 Ancient 原始輪廓 `[SOURCE_PROFILE]`

```text
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
Sorcerer CL31
SR85
CR76
```

來源身份：

```text
巨大、天然甲極厚
普通 DEX，但不是以肉體敏捷為核心
極高 INT / WIS / CHA
高階術士
時間控制專家
不戀戰
```

---

# 3. 目前 D100 九屬性工作值 `[D100_ADAPTATION_CANDIDATE]`

共享六屬性不再 raw 直搬，而使用 modifier-equivalent anchor。

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

理由與計算見 `ANCIENT_TIME_DRAGON_CONVERSION_WORKSHEET.md`。

其中：

- `RES46` 來自 Fort / Ref / Will 拆掉來源能力 modifier 後的共同 chassis `46 / 47 / 46`；
- `SPI69` 暫以其天生術士／史詩龍的 CHA 作保守 proxy；
- `SKI25` 是依來源近戰可靠性反推的工作值，不是 BAB89 直接換算。

---

# 4. 目前 D100 基礎值候選

```text
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
```

這些是換算工作值，不是 D100 monster canon。

`抗噴吐59` 暫不主動補高，因為來源 Reflex +47 本來就是三豁免的明顯弱項。

---

# 5. 防禦結構：不要做成高 Dodge 坦克

來源 AC 大量來自 natural armor，且 touch defense 很低；飛行 maneuverability 為 `clumsy`。

因此 D100 目標是：

```text
相對容易碰到龍體
+
很難造成有效傷害
+
時間能力提供位置／節奏防禦
```

而不是：

```text
Dodge 200
```

目前仍待 encounter calibration：

```text
Dodge
Armor / 物抗
DR
HP
自然武器最終 Attack
自然武器 Damage
SR 特殊層
```

---

# 6. Ancient 已解鎖能力 `[SOURCE_PROFILE]`

```text
Time Control
Time Stop
Slow 3/day
Draconic Surge 2/day
Time Mastery
Slow Aura
Ravaging Time breath
Time Expulsion breath
Sorcerer casting CL31
Frightful Presence
high Knowledge / languages
```

**沒有** Great Wyrm 的 `Time Apotheosis`。

禁止混入：

- 5e Planescape Time Dragon abilities；
- Pathfinder 同名生物；
- 網路 homebrew；
- Great Wyrm 才有的 possible-future reroll / combat-independent time travel。

---

# 7. Time Mastery — continuous haste，不是額外完整 action

這一點已依 conversion reference 修正。

來源是：

```text
continuous haste
```

所以第一版只保留：

```text
movement boost
attack cadence / extra strike within attack action
small attack / avoidance / reaction benefit
```

**不自動得到第二個一般動作，也不能因此同秒多施放一個普通法術。**

真正額外 standard / move action 來自 `Draconic Surge`。

---

# 8. Draconic Surge `[D100_ADAPTATION_CANDIDATE]`

來源 Ancient：

```text
2/day
extra standard OR move action
```

第一版 D100：

```text
2/day
→ 本秒額外取得 1 個一般動作或完整移動 action window
```

碼表：

```text
Draconic Surge remaining: 2/2
```

---

# 9. Time Stop `[D100_ADAPTATION_CANDIDATE]`

來源核心：施法者取得數個只有自己能行動的 rounds。

Encounter mode v0.1 優先保留**戰術窗口數**：

```text
1d4+1 source rounds
→ 2～5 private action windows
```

Ancient cooldown：

```text
1d4 source rounds
→ 等待 1d4 個龍自己的正常 action windows
```

不機械 ×6，也不把 Time Stop 解釋成免費 12～30 個 D100 actions。

若未來跑 world-time strict mode，再另建版本。

---

# 10. Slow Aura `[D100_ADAPTATION_CANDIDATE]`

來源：

```text
radius = 10 ft × age category
Ancient category 10 → 100 ft
10 rounds/day total
每回合 free action 維持
開始 turn 時在 aura 中 → automatically slow, no save
```

Encounter mode v0.1：

```text
radius 100 ft
10 tactical windows/day
不必連續
```

沙漏仍保留來源世界語意「約一分鐘總量」；碼表則用 10 個戰術維持窗口。

D100 `slow` 精確效果仍待轉譯。

---

# 11. 移動 `[D100_ADAPTATION_CANDIDATE]`

來源 world-speed seed：

```text
Land 100 / 6 ≈ 16.7 ft/s
Fly 380 / 6 ≈ 63.3 ft/s
```

這只給沙漏／世界速度。

戰鬥位置還要另外處理：

- clumsy maneuverability；
- Time Mastery；
- Draconic Surge；
- Time Stop reposition；
- dive / turn / climb。

---

# 12. 兩種吐息

## Ravaging Time

來源 Ancient：

```text
老化10年
CON damage 10，Fort half
物體 hardness -10
```

D100 第一版可先把 `CON damage 10` 當 seed，但最終防禦接口仍需按效果語義決定，不因來源 Fort 就直接翻成強韌。

## Time Expulsion

來源：

```text
失敗 → 被送往未來10 source rounds
```

這同時牽涉戰術窗口與世界時間，暫時保持 `[OPEN_QUESTION]`：

```text
10 tactical windows?
約60 world seconds?
或雙時計同時保存？
```

正式重跑前要固定，戰鬥途中不可改算法。

---

# 13. 個體人格／threat model

本次個體：

- 對時間／空間異常有專業興趣；
- 不以殺光 PC 為勝利條件；
- 失能、驅逐、隔離、迫退都可接受；
- 開打後會優先使用真正有效能力，不保留「Boss phase」；
- 發現永久拘束／封鎖時間能力的效果時，提高該來源的 threat priority；
- 風險高於收益就撤；
- 不戰到死。

它可以學習 PC 能力，但**不能讀玩家角色卡**。

INT69／宣告順位97代表高推理與資訊優勢，不代表全知。

---

# 14. T=0 Ledger

```text
HP: PENDING
SP: PENDING
Position: encounter start決定
Facing: encounter start決定
Altitude: encounter start決定

Time Mastery: persistent
Time Stop: available
Time Stop cooldown: 0
Slow: 3/3
Draconic Surge: 2/2
Slow Aura: inactive
Slow Aura pool: 10 tactical windows
Breath recharge: PENDING

Observed PC abilities: none beyond visible prebuffs
Threat priorities: not yet resolved
Retreat route: DM world model must establish
```

---

# 15. 下一步

正式重跑前只剩三個主要缺口：

1. 用三名 PC 真實輸出回推 `HP / armor / DR`；
2. 用 PC Attack / Dodge 做 `natural attack / Dodge` 概率校準；
3. 完成 Slow、Time Expulsion、SR／法術穿透的 D100 接口。

完成後才把本檔從 `[D100_ADAPTATION_CANDIDATE]` 提升為 `[ENCOUNTER_CALIBRATED]`。
