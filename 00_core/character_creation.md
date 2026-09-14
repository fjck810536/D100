# 角色建立與基礎數值

> 本檔是創角機械的 runtime-friendly normalized index。流程調度、模塊分工與自動 build 停止條件見 `../CHARACTER_CREATION_PROTOCOL.md`。

## 1. 起始配置 `[D100_CANON]`

一般起始 CP 常見為：

- 200 CP
- 250 CP
- 300 CP

DM 可依團期望難度與強度調整。

來源表亦提供常見起始魔法物品加值：

| 起始 CP | 三件起始魔法物品常見加值 |
|---|---|
| 200 | +3 / +4 / +5 |
| 250 | +4 / +5 / +6 |
| 300 | +5 / +6 / +7 |

起始魔法物品詞綴可依角色建立需求配置；最終仍由 DM 決定。

角色背景可由 DM 額外給 50 CP；繪製角色外貌可由 DM 額外給 10 CP。

### 自動創角預設 `[GM_PROVISIONAL]`

若沒有玩家／DM 另行指定，自動創角目前優先採：

```text
200 base CP
+3 / +4 / +5 三件起始魔法物品
```

這與上游 200 CP 常規配置一致，但只是自動模板；明示配置優先。

**200 是基準起始 CP，不是所有角色最後固定 200 CP。** 還要經第 3 節的 adjustment sum 修正。

來源補答：`../sources/GM_CLARIFICATIONS_2026-09-14_CHARACTER_CREATION.md`。

## 2. 九大屬性 `[D100_CANON]`

擲 9 組 `4D6` 取得九大屬性：

- STR — 力量
- DEX — 敏捷
- SKI — 技巧
- CON — 體質
- RES — 抗力
- INT — 智力（偏 IQ）
- WIS — 智慧（偏 EQ）
- CHA — 魅力
- SPI — 精神

來源作者個人允許起始 4D6 任意分配並可重骰；DM 可自行決定是否採用。

## 3. 屬性調整值與起始 CP 修正 `[D100_CANON + PLAY_CONVENTION]`

以 13 為 0。來源表列例：

| 屬性 | 調整值 |
|---:|---:|
| 7–8 | -3 |
| 9–10 | -2 |
| 11–12 | -1 |
| 13 | 0 |
| 14–15 | +1 |
| 16–17 | +2 |
| 18–19 | +3 |

多張實際角色卡將這條延伸為：

```text
adjustment = ROUND((current raw stat - 13) / 2)
```

因此高於 19 的屬性也依同一 operational formula 延伸；角色卡證據見 `../sources/CHARACTER_EVIDENCE.md`。

將九大屬性 adjustment 加總：

- 總和 > 10：每超過 1 點，扣 10 起始 CP。
- 總和 < 10：每少 1 點，增加 10 起始 CP。

```text
adjusted_starting_cp
= base_starting_cp - (adjustment_sum - 10) × 10
```

上式只是將 Sheet 的兩段規則寫成同一代數式。

## 4. 屬性總值 `[D100_CANON]`

創角表原文要求先把「九大屬性數值與其各自調整值進行加總」，再計算六大技能基礎與五抗。

因此 normalized runtime 使用：

```text
屬性總值 = current raw stat + adjustment
```

例如：

```text
DEX raw 18
adjustment +3
DEX總值 = 21
```

**六大技能基礎與五抗使用屬性總值，不是只用 raw stat。**

三種特殊判定例外，見第 7 節。

## 5. 六種主要技能基礎值 `[D100_CANON + PLAY_CONVENTION]`

```text
戰鬥 = DEX總值 + SKI總值 + STR總值
運動 = DEX總值 + SKI總值 + CON總值
操作 = INT總值 + SKI總值 + WIS總值
感知 = INT總值 + RES總值 + SPI總值
知識 = ROUNDDOWN((INT總值 + WIS總值) × 1.5)
交涉 = CHA總值 + WIS總值 + SPI總值
```

其中知識基值的 `ROUNDDOWN` 由多張角色卡 operational evidence 交叉確認；不能外推成全系統所有小數都向下取整。

專長／技能通常在這些基礎值上加技能等級與其他修正。

例：擅長鎧甲 Lv3 的相關檢定可使用：

```text
戰鬥基礎值 + 3×10
```

但仍應以個別技能條文為準。

## 6. 五大抗性 `[D100_CANON + PLAY_CONVENTION]`

```text
抗毒素 = RES總值 + CON總值
抗控制 = RES總值 + WIS總值
抗轉化 = RES總值 + RES總值
抗噴吐 = RES總值 + DEX總值
抗魔法 = RES總值 + INT總值
```

個別技能／物品／效果再加自己的修正。

語義與使用詳見 `resistances.md`。

## 7. 三種特殊判定 `[D100_CANON + PLAY_CONVENTION]`

三種特殊判定明文**不計 adjustment**：

```text
強韌 = current raw CON × 5 + 額外特殊修正
精神 = current raw RES × 5 + 額外特殊修正
靈魂 = current raw SPI × 5 + 額外特殊修正
```

這三者不是五大抗性的替代名稱。

角色卡證據顯示：如果 raw stat 本身因裝備／永久／臨時效果改變，使用當前 raw；但不把由該 raw 導出的 adjustment 再乘一次。

## 8. 技能 CP `[D100_CANON]`

每一級的 CP 成本：

```text
該級成本 = 2^(等級) × 技能難度
```

難度1例：

| 等級 | 該級成本 |
|---:|---:|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

若直接取得 Lv3（不是先買 Lv0），累計：

```text
2 + 4 + 8 = 14 CP
```

Lv0 是一個真實的「已購但沒有 Lv1 加值」狀態，用來免除未受訓時的 -20。

```text
未購 ≠ 已購 Lv0
```

Lv0 不是購買 Lv1+ 時必須額外再付的一級。

## 9. 創角稀有度與前置 `[GM_PROVISIONAL]`

本輪 GM 補答明確區分兩條軸：

```text
Lv1–3：正常創角自由範圍
Lv4+：極為稀有／罕例 → review
```

以及：

```text
難度1–2：正常創角自由範圍
難度3+：能力本身稀有／特殊 → review
```

`review` 不是禁止購買，而是需要可信服背景／世界前提。

不得把 `Lv4+ 稀有` 過度解讀成 `Lv3 也最好少買`。

### prerequisite graph

能力若有明文前置，必須在購買當下已經滿足，例如：

- 其他技能／專長；
- 最低等級；
- 屬性門檻；
- 施法環數；
- 職業／領域／種族等。

不能先買後補前置。

詳見 `../sources/GM_CLARIFICATIONS_2026-09-14_CHARACTER_CREATION.md`。

## 10. 跑團中學習技能 `[D100_CANON]`

創角後新學／升級技能通常需要：

- CP
- 時間
- 金錢／老師

基本技能表提供學習時間與費用：

### 難度3以下

```text
時間 = 消耗總 CP × 0.5 週
金額 = 全部週數 × 10 gp × 難度
```

### 難度4以上

來源表記為：

```text
時間 = 消耗總 CP × 難度 × 1週（或2週）
金額 = 全部週數 × 10 gp × 難度^2
```

其中「1週（或2週）」的具體選擇條件仍待整理 `[OPEN_QUESTION]`。

### 書籍自學

僅難度3以下：

```text
時間 = 消耗總 CP × 1週
```

### 忘記技能

```text
時間 = 學習該技能時間的一半
```

## 11. 語言創角規則 `[D100_CANON + GM_PROVISIONAL]`

語言本身的難度與熟練機制見 `../01_skills/core_skills.md`。

目前創角補答：

```text
所有創角角色免費取得 通用語 Lv3
```

施法者另需：

```text
至少一門難度2語言 Lv1+
```

來源可為種族／背景／模板贈送或花 CP 購買。

如果種族已送一門難度2語言，就已滿足施法文化門檻，不需再買固定職業語言。

法師龍語、牧師天界／深淵／煉獄語、德魯伊德魯伊語等是**基本模板推薦**；真正 hard gate 是「任一難度2語言 Lv1」。

## 12. 施法者創角接口 `[D100_CANON + GM_PROVISIONAL]`

施法職業的核心技能、法術位與判定詳見 `magic.md`。

### 核心技能可非同步預購

施法者可以先把下一環的一部分核心技能升級；這是合法 build。

```text
可用法術環數
= 該施法體系所有必要核心技能等級的最低值
```

例如：

```text
法師：奧術知識3 / 黑魔導3 / 黑魔力2
→ 可用環數仍是 2
```

### 高環 review

目前 GM 世界尺度：

- 三環已是初始角色中的頂尖／菁英施法者；
- 三環應有可信服的訓練／師承／年齡／教育背景；
- 四環以上必須強 review，不能只因 CP 與屬性足夠就自動生成。

上游施法者年齡表以「約四歲開始啟蒙、無外在變因」作理想／最快進程參考，不代表所有施法者都從四歲開始。

### 法師學派

D100 不強迫法師選學派。

```text
通才：合法
學派專精：可選 build
```

自動創角可以推薦學派方向；正式購買仍照能力條文的難度／環數／前置。

### 牧師信仰與領域

牧師角卡除了機械核心技能，還必須明示：

```text
真正信仰的神祇／宗教
領域
```

領域與信仰必須一致。領域能力是否另外購買仍依能力條文。

## 13. 基礎 HP / SP `[D100_CANON]`

```text
基礎HP = CON + CON調整值 + 獎勵近戰CP + 獎勵法術CP + 技能 + 魔法物品詞綴
基礎SP = RES + RES調整值 + 獎勵近戰CP + 獎勵法術CP + 技能 + 魔法物品詞綴
```

這裡的「獎勵近戰CP／獎勵法術CP」指依第 14 節投資門檻擲出的 HP/SP 獎勵結果，不是直接把 CP 數字加進 HP/SP。

## 14. CP 投資獎勵 HP/SP `[D100_CANON]`

### 近戰相關 CP 投資

| 投資 | 獎勵 |
|---:|---|
| 10 | 1d8 HP + 1d4 SP |
| 30 | 2d8 HP + 2d4 SP |
| 70 | 3d8 HP + 3d4 SP |
| 150 | 4d8 HP + 4d4 SP |
| 300 | 5d8 HP + 5d4 SP |
| 620 | 6d8 HP + 5d4 SP |
| 1020 | 7d8 HP + 6d4 SP |

### 法術相關 CP 投資

| 投資 | 獎勵 |
|---:|---|
| 10 | 1d8 SP + 1d4 HP |
| 30 | 2d8 SP + 2d4 HP |
| 70 | 3d8 SP + 3d4 HP |
| 150 | 4d8 SP + 4d4 HP |
| 300 | 5d8 SP + 5d4 HP |
| 620 | 6d8 SP + 5d4 HP |

注意：來源表近戰與法術在高 CP 檔位的骰數並不完全對稱，禁止自行「修正成一致」。

### 創角順序

```text
技能／專長配置完成
→ 統計 qualifying melee/spell CP
→ 擲獎勵 HP/SP
→ 算基礎 HP/SP
→ 再用 CP 額外購買 HP/SP（若需要）
```

角色卡證據顯示「近戰相關投資／法術相關投資」是獨立 ledger，不等於總技能 CP。

`[OPEN_QUESTION]`：目前尚缺完整「哪些技能精確算進近戰／法術 qualifying investment」的分類表；不確定時不得把總技能 CP 全部硬塞進其中一池。

## 15. 額外購買 HP/SP `[D100_CANON]`

以基礎值倍數提高成本。

HP：

- 基礎 HP ～ 2倍：1 CP / 1 HP
- 2倍 ～ 3倍：2 CP / 1 HP
- 3倍 ～ 4倍：3 CP / 1 HP
- 依此類推

SP 同理。

例：基礎 HP 30：

```text
30–60：1 CP / HP
60–90：2 CP / HP
90–120：3 CP / HP
```

## 16. CP 可以保留 `[GM_PROVISIONAL]`

創角 CP 不要求花完。

可以保留供：

- 日後學習／升級；
- 重骰；
- 未來符合前置後購買能力；
- 其他合法用途。

但自動創角若大量保留 CP，必須先依 `../CHARACTER_CREATION_PROTOCOL.md` 完成候選廣搜與反事實 build pass，確認不是 generator 提前停止。

GM 另指出 CP 可以填補基礎數值缺口；目前 `[OPEN_QUESTION]` 尚未定位到可安全採用的「CP → raw/basic stat」正式換算公式，因此不要自行發明。

## 17. CP 重骰 `[D100_CANON]`

跑團中：

```text
1 CP = 1 次重骰機會
```

但劇情骰、寶藏骰除外。

詳細未決問題見 `checks.md` 與 `../99_open_questions/unresolved_rules.md`。
