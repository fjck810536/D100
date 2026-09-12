# 上古時空龍（Ancient Time Dragon）— 空戰壓力測試登錄

> 用途：目前三名 PC（亞黛兒／卡蘭德／莎緹拉）的高階 D100 空戰、時間能力與 Action Economy 壓力測試。
>
> 來源物種模型：`examples/TIME_DRAGON_DRAGON359_MODEL.md`
>
> **版本鎖定：** Mike McArtor, *Time Dragon: A Wyrm for the Ages*, Dragon #359 (September 2007), pp. 36–40。
>
> 本檔不是 D100 Sheet 正典。Dragon #359 原始資料標 `[SOURCE_PROFILE]`；D100 換算候選標 `[D100_ADAPTATION_CANDIDATE]`；本次遭遇個體設定標 `[ENCOUNTER_DEFAULT]`。

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

本次測試正式使用 **Ancient／上古時空龍**，不再使用先前臨時 Adult 個體作為主要敵人。

前面測試曾暫填的：

```text
Attack 112
Dodge 105
```

**全部作廢。** 這兩個值不是 Dragon #359 原始數據，也不是完成的 D100 轉譯。

---

# 2. Dragon #359 Ancient 原始能力值 `[SOURCE_PROFILE]`

> 以下保留來源尺度，用來理解生物能力結構；不可把 3.5 AC / saves / HD / CR 直接當 D100 數值。

| 項目 | Ancient Time Dragon |
|---|---:|
| Size | Colossal+ |
| Hit Dice | 89d12+2403 |
| 平均 HP（3.5來源） | 2931 |
| STR | **83** |
| DEX | **10** |
| CON | **65** |
| INT | **66** |
| WIS | **73** |
| CHA | **66** |
| Land Speed | **100 ft.** |
| Fly Speed | **380 ft. (clumsy)** |
| Sorcerer Caster Level | **31** |
| Spell Resistance | **85** |
| Challenge Rating | **76** |

來源的重要結構是：

```text
肉體 DEX 很低（10）
+
時間控制極強
+
INT / WIS / CHA 極高
+
31級術士施法
```

因此不可把它主持成「因為是時空龍，所以裸 DEX 必定極高」。

---

# 3. D100 排序候選 `[D100_ADAPTATION_CANDIDATE]`

若暫時將 Dragon #359 的屬性值直接帶入 D100 現行 adjustment 公式：

```text
adjustment = ROUND((raw stat - 13) / 2)
```

則：

### 行動順序候選

```text
DEX 10
DEX adjustment = ROUND((10-13)/2) = -2
行動順序候選 = 10 - 2 = 8
```

### 宣告順序候選

```text
INT 66
INT adjustment = ROUND((66-13)/2) = 27
宣告順序候選 = 66 + 27 = 93
```

意義：

- 它的**裸肉體行動順位可能很晚**；
- 但 INT 極高，所以它能在宣告輪看到大量其他單位的宣告後才表態；
- 真正的高速與額外行動應由 `Time Control / Time Mastery / Draconic Surge / Time Stop` 等時間能力進入「碼表」處理，而不是偷偷灌進 DEX。

這兩個數字目前都不是 D100 正典怪物值。

---

# 4. Ancient 已解鎖時間能力 `[SOURCE_PROFILE]`

上古時空龍至少具有：

```text
Time Control
Time Stop
Draconic Surge 2/day
Slow 3/day
Time Mastery
Slow Aura
兩種時間吐息
Sorcerer casting CL 31
Frightful Presence
高階 Knowledge / Speak Language 能力
```

它**沒有** Great Wyrm 才取得的 `Time Apotheosis`。

因此本次上古個體：

- 不能因「時空龍」就每次擲骰偷看兩個可能未來取佳者；
- 不能在戰鬥中隨意回到過去改寫已發生事件；
- 不能偷用 2023 Planescape 5e Time Dragon 的反應／Time Gate 等能力；
- 不能偷用網路 homebrew 的 Temporal Flux / Aura of Time 等同名能力。

---

# 5. Time Stop `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

來源：

- at will；
- Adult ～ Wyrm 兩次 Time Stop 之間需等待 **1d4 個 3.5 rounds**。

Ancient 落在這一區間，所以來源冷卻也是：

```text
1d4 × 3.5 rounds
```

但 D100：

```text
1 round = 1 second
```

因此正式開戰以前必須固定轉譯哲學：

### 世界時間保真

先把 3.5 約六秒 round 換成世界秒數，再讓「碼表」切成 D100 一秒輪。

### 戰術節奏保真

將來源 round 視為 action window，轉成 D100 對應戰術窗口，而不是直接乘六。

**戰鬥途中禁止因平衡需要切換兩套算法。**

---

# 6. Time Mastery `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

Adult 起即獲得，Ancient 當然持有。

來源意義：時空龍持續處於類似 `haste` 的時間加速狀態；即使被壓掉，也會自行恢復。

D100 不可只把這句轉成：

```text
DEX +N
```

因為它本質上首先是 **action economy / 時間流速能力**。

正式轉譯時「碼表」至少要回答：

- 外界 1 秒中它能得到哪些行動窗口？
- 額外窗口可做一般動作、自由動作、施法、移動中的哪些？
- 與 Draconic Surge 是否疊加？
- Time Stop 內 Time Mastery 如何計時？
- 其他生物的 buff / debuff 倒數是否跟隨外界時間、個體主觀時間或效果原文？

---

# 7. Draconic Surge `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

Old 起增加為 **2/day**；Ancient 因此是：

```text
Draconic Surge: 2/day
```

來源概念是從未來借取額外 standard / move action。

這不是攻擊加值，也不是 DEX 加值；D100 必須轉成額外 action window。

「碼表」要獨立追蹤：

```text
Draconic Surge remaining: 2/2
```

並記錄每一次究竟增加了哪種行動權。

---

# 8. Slow Aura — Ancient 的質變能力 `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

Ancient 起取得。

來源範圍：

```text
10 ft × age category
```

Ancient 為第 10 年齡階，因此：

```text
Slow Aura radius = 100 ft
```

來源效果：

- 每一 3.5 round 由時空龍以 free action 決定是否維持；
- 每日總共可維持 10 個 3.5 rounds；不必連續；
- 生物若在自己的 round 開始時位於 aura 內，**自動受到 slow；no save**。

這個能力在 D100 中不能簡化成固定 `-20`。

真正要由「碼表」處理的是：

```text
誰在某一秒開始時位於 100 ft 內？
→ 該個體的時間流被怎樣改變？
→ 本秒哪些 action windows 消失／延後／改變？
→ 離開 aura 後效果何時終止？
→ Slow Aura 的每日 10 rounds 如何由 3.5 時間轉成 D100？
```

開場 ledger：

```text
Slow Aura source uses: 10 rounds total [3.5 scale; D100 conversion pending]
Slow Aura active: false
```

它不會因為 NPC 是 Boss 就免費常駐；要依來源決定何時啟用並消耗總額。

---

# 9. 兩種吐息 `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

## Ravaging Time

時間侵蝕線：

- 生物被老化／侵蝕並承受 Constitution 層面的損害；
- 物體 hardness 下降。

D100 候選思路：

```text
存在狀態／生理時間被改寫 → 抗轉化候選
若另有獨立肉體承受階段 → 強韌候選
```

不可因原版是 Fortitude 就直接翻成 D100 強韌。

## Time Expulsion

把目標送往未來，使其暫時從目前時間線消失，等待世界時間追上。

D100 候選思路：

```text
時序／存在位置被改寫 → 抗轉化候選
```

不可因原版是 Will 就直接翻成抗控制。

兩種吐息的 D100 判定值、範圍、recharge 都尚未定案。

---

# 10. 個體性格／生態 `[SOURCE_PROFILE + ENCOUNTER_DEFAULT]`

物種層：

- 幾乎不會因年老自然死亡；
- 多半獨居；
- 偏好偏遠巢穴、半遊牧；
- 不需要頻繁獵殺活物；
- 對魔法、知識、藝術以及測量時間的器具特別有收藏興趣；
- 不喜歡為無意義戰鬥冒險；
- 真正決定開打時會積極使用最強手段快速結束；
- 被壓過時會撤；
- **不自願戰到死。**

本次個體人格：

- 對時間／空間異常具有專業興趣；
- 對陌生高階施法者先判斷是否構成持續性威脅；
- 不以殺死所有 PC 為必要勝利條件；
- 使對手失能、驅逐、隔離或迫使撤退都可接受；
- 若發現 `次元錨／禁空／其他永久拘束時間移動的效果` 真的能威脅自己，會顯著提高該施法者 threat priority；
- 若風險高於收益則離開。

---

# 11. 開戰前知識邊界 `[ENCOUNTER_DEFAULT]`

它合理知道：

- 自己的時間能力；
- 常見高階時間／空間奧術；
- 31級術士施法層級應具備的廣泛奧術知識；
- 自己親眼觀察或成功辨識的 PC 效果。

它**不能讀角色卡**，因此 T=0 不知道：

- 亞黛兒的激勵戰歌確切提供 `閃避 +85`；
- 卡蘭德每個戒指、藥劑與卷軸的效果及剩餘次數；
- 莎緹拉持有 `次元錨／禁空／解析弱點` 等具體法術；
- PC 下一秒的宣告。

NPC 的 INT66 代表極高推理與學習能力，不等於全知。

---

# 12. Ancient Time Dragon Action Palette `[SOURCE_PROFILE → D100_ADAPTATION PENDING]`

正式戰鬥 Ledger 至少要有：

```text
自然武器／飛行
兩種吐息
Sorcerer casting CL31
Time Control
Time Stop: available / cooldown
Slow: 3/day
Draconic Surge: 2/day
Time Mastery: persistent
Slow Aura: inactive/active + remaining daily duration
Frightful Presence
移動／朝向／高度
已觀察到的 PC 能力
當前 threat model
撤退路線
```

不能再使用：

```text
一般動作：爪擊
```

代表整隻怪物。

---

# 13. 三維位置與「碼表」狀態 `[ENCOUNTER_STATE]`

正式重跑採新的 T=0；以前 regression run 的傷害、箭矢、鎖定目標與位置**全部不繼承**。

開戰前需另外建立：

```text
T = 0.000 s
Ancient Time Dragon: x/y/z、朝向、速度向量
亞黛兒: x/y/z、朝向、速度向量
卡蘭德: x/y/z、朝向、速度向量
莎緹拉: x/y/z、朝向、速度向量
```

「碼表」負責：

- 宣告與行動順位；
- 一般／自由／即時／瞬唱／觸發窗口；
- Time Mastery；
- Draconic Surge；
- Time Stop 形成的內嵌時間區段；
- Slow Aura 造成的個體時間差；
- 同一秒內的因果順序。

「沙漏」不負責逐秒戰鬥細節；它處理戰鬥前後較大尺度的移動、抵達、世界狀態變化與後續影響。

---

# 14. 尚未完成的 D100 數值 `[OPEN_QUESTION / D100_ADAPTATION]`

正式數值戰以前仍需建立：

```text
D100 HP / SP
D100 攻擊／閃避
D100 物抗／法抗
五抗
強韌／精神／靈魂
自然武器傷害
吐息 D100 判定與效果
31級術士法術表／法術資源轉譯
飛行每秒位移
Time Stop 時長與冷卻
Time Mastery action economy
Slow 的 D100 行動效果
Slow Aura 的 D100 時間換算
Draconic Surge 的 D100 action window
```

禁止直接把以下 3.5 數值當成 D100：

```text
AC 81
SR 85
CR 76
Fort / Ref / Will
BAB / grapple
89 HD / 2931 source HP
```

來源數值可以用來**理解相對能力層級**，但不能偷當轉換公式。

---

# 15. 本次遭遇的戰術原則 `[ENCOUNTER_DEFAULT]`

這隻上古時空龍不是固定腳本 Boss。它每秒重新根據已知資訊判斷：

```text
能否不用打？
↓
若要打，誰最能限制我的時間／空間能力？
↓
能否用 Time Stop / Slow Aura / spell positioning 建立不對稱？
↓
能否用失能、隔離、Time Expulsion 結束對方戰鬥能力？
↓
PC 新能力曝光 → 更新 threat model
↓
永久拘束風險或收益不足 → 撤退
```

它不會：

- 故意前三輪只普通爪擊；
- 因為「Boss 還沒半血」而不用時間能力；
- 因為知道玩家角色卡所以完美 counter；
- 為了劇情堅持戰到 0 HP。

---

# 16. 重跑前最低條件

正式重跑上古時空龍遭遇以前，同時準備：

1. 亞黛兒／卡蘭德／莎緹拉三人的 encounter snapshot；
2. 三人的 Action Palette 與本輪 Action Ledger；
3. 本檔 Ancient Time Dragon Action Palette；
4. T=0 三維位置；
5. Time Stop / Time Mastery / Slow Aura / Draconic Surge 的 D100 時間轉譯；
6. 雙方只依實際觀察形成 threat model。

缺其中任何一項，都先標記為測試中的待轉譯項，不以臨時「Boss 數字」掩蓋缺口。
