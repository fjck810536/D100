# D&D 3.5 → D100 常用換算參考系統

> 狀態：`[CONVERSION_REFERENCE]`
>
> 用途：提供 GPT／DM 將 D&D 3.5 怪物、法術、技能、環境危險與特殊能力轉譯到 D100 時的共同方法。
>
> **本檔不是 D100 Sheet 正典，也不是「所有數值乘某個倍率」的公式表。**
>
> 上位原則仍依 `AGENTS.md`、`90_srd_bridge/conversion_rules.md` 與 D100 core rules。

---

# 0. 一句話原則

```text
不要換數字。
先換「這個數字在原系統裡負責什麼」，再在 D100 找對應接口。
```

轉譯的目標依優先順序是：

1. **保留因果／語義**：能力做的是同一件事。
2. **保留相對能力結構**：誰強、誰弱、強在哪一層仍然成立。
3. **保留戰術功能**：原本是控制、坦克、玻璃砲、時間操作者，轉完不能變另一種生物。
4. **保留合理的成功率／生存時間**：用概率或 TTK 校準。
5. 最後才考慮是否能保留某個原始數字。

---

# 1. 先判斷這是哪一種換算

每個來源數值先分類。

| 類型 | 例子 | 預設方法 |
|---|---|---|
| 世界事實 | 體型、語言、感官、食性 | 直接保留概念 |
| 共享屬性 | STR / DEX / CON / INT / WIS / CHA | modifier 等價換算 |
| D100 額外屬性 | SKI / RES / SPI | 功能反推，不硬猜 |
| 機率 | attack bonus、DC、save | 先算來源成功率，再校準 D100 |
| 防禦結構 | AC、touch AC、natural armor、DR | 拆成閃避／格擋／鎧甲／抗性／減傷 |
| 時間 | rounds、minutes、cooldown | 先分世界時間 vs 戰術窗口 |
| 移動 | speed、fly maneuverability | 物理速度＋機動性分開 |
| 生存力 | HD / HP | 用 TTK / effective HP 校準 |
| 傷害 | weapon/spell dice | 用「對同階角色造成多少比例」校準 |
| 行動經濟 | standard / move / swift / immediate | 映射為 D100 Action Palette |
| CR / ECL | CR 76 | 只當來源威脅標籤，不直接換數字 |

---

# 2. 共享六屬性：保留 modifier，不直接照抄 raw score

D&D 3.5 的能力調整值：

```text
m35 = floor((A35 - 10) / 2)
```

D100 現行 adjustment 以 13 為中心，角色卡／repo 實作可抽象為：

```text
m100 = ROUND((A100 - 13) / 2)
```

因此最穩的第一個 anchor 不是：

```text
A100 = A35
```

而是先讓：

```text
m100 = m35
```

可使用代表值：

```text
A100_anchor = 13 + 2 × m35
```

這是 `[CONVERSION_REFERENCE]`，不是 D100 canon。

### 常用表

| 3.5 屬性 | 3.5 modifier | D100 anchor |
|---:|---:|---:|
| 8–9 | -1 | 11 |
| 10–11 | 0 | 13 |
| 12–13 | +1 | 15 |
| 14–15 | +2 | 17 |
| 16–17 | +3 | 19 |
| 18–19 | +4 | 21 |
| 20–21 | +5 | 23 |
| 30–31 | +10 | 33 |
| 50–51 | +20 | 53 |
| 66–67 | +28 | 69 |
| 82–83 | +36 | 85 |

### 為什麼這比 raw 直搬安全

例如來源 DEX 10 在 3.5 是：

```text
modifier 0
```

如果直接放進 D100，DEX 10 會得到負 adjustment；這其實把「普通敏捷」誤譯成「低敏捷」。

modifier 等價後：

```text
3.5 DEX 10 → D100 DEX 13
```

才保留來源相對意義。

### 邊界

- 若 D100 已有該角色／種族自己的 canonical 屬性，canonical 優先。
- raw score 的奇偶細節若對來源能力有特殊意義，可在同一 adjustment band 內微調 1 點。
- 超高屬性仍只是來源能力的一部分，不代表所有技能／防禦一起等比例上升。

---

# 3. SKI / RES / SPI：不要假裝 3.5 有一對一欄位

D100 多了三個來源系統沒有的核心屬性，所以必須用**功能反推**。

## 3.1 SKI — 技巧／訓練

不要直接用 BAB 當 SKI。

優先流程：

```text
先決定來源生物應有的 D100 攻擊／操作表現
→ 選擇武器／自然武器熟練等級與專長
→ 反推 SKI
```

若攻擊公式為：

```text
Attack = STR + DEX + SKI + proficiency + other
```

則可反推：

```text
SKI_seed
= Attack_target
- STR
- DEX
- proficiency
- other
```

因此 SKI 是「補出來源的技術輪廓」，不是 BAB 的另一個名字。

## 3.2 RES — 泛用抵抗底盤

若來源有 Fort / Ref / Will，可先把 ability modifier 拆掉，觀察共同的 save chassis：

```text
Fort_chassis = Fort - CON_mod
Ref_chassis  = Ref  - DEX_mod
Will_chassis = Will - WIS_mod
```

如果三者接近，可取中位數作 `RES_seed` 的**第一個量級參考**：

```text
RES_seed ≈ median(Fort_chassis, Ref_chassis, Will_chassis)
```

但這不是定案公式；最後仍要看 D100 五抗是否產生合理輪廓。

如果來源三豁免差異很大，不要硬壓成一個 RES；差異可由：

- DEX / CON / WIS；
- 專長；
- 種族免疫；
- 特殊抗性；
- 特定效果加減值

共同表現。

## 3.3 SPI — 精神／靈魂本質

3.5 沒有可靠的 SPI 等價物。

預設只建立 ontology seed：

- 普通凡人／動物：由 WIS / CHA 與設定判斷；
- 天生施法者／龍／外在者：可由主要施法屬性、CHA 或 WIS 作 seed；
- 神性／靈魂高度實體化生物：可高於普通心智能力；
- 構裝體、無魂體、分散意識生物：不要硬塞一般 SPI，先寫特殊存在規則。

SPI 必須標 `[D100_ADAPTATION]`，除非來源或 campaign 已經給答案。

---

# 4. 固定 DC：先保留成功率，再換 D100 門檻

一般 3.5 d20 check（不考慮特殊 natural 1/20 條款）可先算：

```text
需要骰值 r >= DC - bonus
```

成功率：

```text
p35 = 成功的 d20 面數 / 20
```

常用心算：

| 需要 d20 | 約成功率 |
|---:|---:|
| 2+ | 95% |
| 5+ | 80% |
| 8+ | 65% |
| 10+ | 55% |
| 11+ | 50% |
| 15+ | 30% |
| 18+ | 15% |
| 20 | 5% |

D100 固定門檻若使用：

```text
margin = T - d100
需要 margin >= M
```

忽略大成功／大失敗的邊界效果時：

```text
p100 ≈ clamp((T - M) / 100)
```

因此可以反推：

```text
M ≈ T - 100 × p_target
```

重點：

> **不要單獨把 DC18 翻成某一個 D100 數字。**
>
> DC 的意義只存在於「DC18 對 bonus +X 是幾成成功」。

---

# 5. 攻擊 vs 防禦：AC 必須拆開

3.5 AC 把多種不同東西壓在一個數字裡；D100 不應整包搬運。

## 5.1 AC 拆解

大致映射：

| 3.5 成分 | D100 候選 |
|---|---|
| DEX / dodge bonus | 閃避／運動／位置 |
| size modifier | 體型、命中難度、機動性修正 |
| natural armor | 鎧甲／物抗／實體減傷 |
| armor bonus | 鎧甲／物抗 |
| shield bonus | 格擋／盾牌 |
| deflection | 魔法防護／特殊迴避層 |
| miss chance / displacement | 獨立特殊防禦，不塞進普通閃避 |
| DR | 物理減傷／特定穿透條件 |

因此：

> **巨大、天然甲極厚、touch AC 很低的怪物，在 D100 應該是「容易碰到但難打穿」，而不是高閃避。**

## 5.2 3.5 攻擊成功率

一般 weapon attack 有 natural 1/20 邊界時，可近似：

```text
p_hit35 = clamp((21 - (AC - attack_bonus)) / 20, 0.05, 0.95)
```

但若來源 AC 主要是 natural armor，而 D100 已把它拆成 mitigation，**不要拿完整 AC 去校準 D100 Dodge**。

優先用：

- touch AC；
- DEX / dodge component；
- 飛行 maneuverability；
- 明確 miss chance

判斷「實際避開攻擊」能力。

## 5.3 D100 攻擊／閃避 margin 對抗參考表 `[MODEL_TABLE]`

以下是假設：

- 攻擊先成功才進閃避；
- 攻防都以 `score - d100` 比 margin；
- 不處理特殊大成功／大失敗；
- margin 平手不列入命中；
- 攻防 score 大致在 100 以上時。

用完整 100×100 骰面枚舉得到約略：

| Attack - Dodge | 命中率約 |
|---:|---:|
| -50 | 12% |
| -40 | 18% |
| -30 | 24% |
| -20 | 32% |
| -10 | 40% |
| 0 | 50% |
| +10 | 59% |
| +20 | 68% |
| +30 | 75% |
| +40 | 82% |
| +50 | 87% |
| +60 | 92% |
| +70 | 95% |

用途：若來源顯示某攻擊對同階目標約有 80% 命中，可讓 D100 `Attack - Dodge` 先從約 +40 試跑，再以實戰修正。

這是**校準表，不是新規則**。

---

# 6. Fort / Reflex / Will：翻效果，不翻名字

不要建立：

```text
Fort → 強韌
Ref  → 抗噴吐
Will → 抗控制
```

這種死表。

先問效果實際做什麼：

| 來源效果 | D100 優先候選 |
|---|---|
| 毒素／藥物／生理毒害 | 抗毒素 |
| 強制命令／魅惑 | 抗控制 |
| 石化／異變／存在形態改寫 | 抗轉化 |
| 爆炸／噴吐／面狀閃避 | 抗噴吐 |
| spell resistance / penetration | 抗魔法 |
| 肉體承受極限 | 強韌 |
| 恐怖／認知負荷 | 精神 |
| 抽魂／靈魂剝離 | 靈魂 |

來源 save bonus / DC 只用來回答：

> 「在來源系統裡，這種等級的角色大約多常擋住？」

再用 D100 對應接口校準成相似概率。

---

# 7. SR / Spell Resistance：用穿透概率換，不用 raw SR 換

3.5 SR 是：

```text
caster level check vs SR
```

D100 已有自己的：

```text
抗魔法
法術穿透
高等法術穿透
施法主屬性調整值
```

因此：

1. 先算來源同階施法者突破 SR 的概率；
2. 看 D100 施法者典型的法術穿透與抗魔法接口；
3. 調整怪物 `抗魔法 / 特殊法抗`，直到突破概率接近。

**SR85 ≠ D100 抗魔法85。**

---

# 8. HP / HD / 傷害：用 TTK，不用 raw HP

3.5 高階／epic HP 常比 D100 HP 大一個數量級，直接搬會破壞系統。

## 8.1 生存力目標

先決定來源角色的戰術耐久：

```text
它應該承受幾次「同階重擊」才倒？
它主要靠 HP、armor、DR、miss chance、regeneration 還是免疫活著？
```

可抽象：

```text
TTK_source ≈ source effective HP / peer expected damage per successful action
```

D100 再建立：

```text
D100 HP
+ 鎧甲／物抗
+ 元素抗
+ 格擋
+ 特殊免疫
+ 回復
```

讓**成功重擊次數**接近來源角色的戰術定位。

## 8.2 傷害

不要把：

```text
20d6 → 20d6
```

視為預設。

先看：

```text
source_damage / source_peer_HP
```

再讓 D100 能力對 benchmark 角色造成相近比例的有效傷害。

### 例外：屬性傷害

若來源直接傷害共享屬性（例如 `CON damage`），而 D100 也把該屬性當真實角色資源，**原數值有時可以作第一個 seed**。

仍要檢查：

- D100 屬性尺度；
- 恢復速度；
- 降到 0 的後果；
- 是否在 D100 變得遠比來源致命。

---

# 9. 移動：速度與機動性分開

D&D 3.5 的列示 speed 是「每個 move action 可移動的距離」，系統一輪約 6 秒。

若需要**世界物理速度**的第一個 seed：

```text
D100 ft / second ≈ 3.5 listed speed / 6
```

例如：

```text
fly 380 ft
→ 約 63 ft/s 的單一 move-action 物理速度 seed
```

這不是戰鬥 action economy 的完整換算；來源還可能 double move、run、charge、haste。

### maneuverability 不等於 DEX

`perfect / good / average / poor / clumsy` 應影響：

- 轉向；
- 最小前進量；
- 爬升／俯衝；
- 急停；
- 近距離閃避；
- 狹窄空間。

不要因 `clumsy` 就直接把 DEX 再砍一遍；也不要因速度很快就提高 DEX。

---

# 10. 最重要：時間有兩種時鐘

這是 D100 1 秒輪轉譯 3.5 6 秒輪時最容易出錯的地方。

## 10.1 沙漏：世界時間（world time）

處理：

- 走路／飛行實際速度；
- 分鐘、時、日；
- 燃燒多久；
- 毒素多久發作；
- 建築倒塌、增援抵達；
- 旅程與 NPC 行程。

如果來源 `round` 真正在描述**物理持續時間**，可使用：

```text
1 source round ≈ 6 seconds
→ 6 D100 rounds
```

## 10.2 碼表：戰術窗口（action windows）

處理：

- 一輪能做幾件事；
- extra action；
- once per round；
- reaction / immediate；
- 「維持 N rounds」其實是在限制 N 次戰術輪；
- cooldown 是等 N 個自己的行動窗口。

如果來源 round 真正表示的是：

> 「這個效果給你 N 個 turn / action opportunities」

則優先：

```text
1 source tactical round
→ 1 D100 tactical window
```

**不要乘六。**

## 10.3 混合型：時間魔法

Time Stop、Slow、Haste、時間膨脹等必須至少同時記：

```text
external_world_time
subjective_time
normal_action_windows
extra_or_removed_action_windows
cooldown_clock_basis
```

不能只記一個 `remaining_rounds`。

---

# 11. action economy 對應

不要把 3.5：

```text
standard + move + swift + immediate
```

直接當成 D100 同名槽位。

先抽象成：

```text
主要戰術窗口
移動權
額外／快速窗口
反應窗口
自由小動作
```

再映射 D100：

- 一般動作；
- 自由動作；
- 即時動作；
- 法術瞬唱；
- 一心二用；
- 特殊額外 action window。

### 額外行動能力

來源若明文：

```text
extra standard or move action
```

優先保留為：

```text
額外一般／移動 action window
```

而不是：

```text
DEX +N
```

---

# 12. Caster Level / spell level

來源 Caster Level 不可直接宣告為 D100 總施法者等級 canon，但可以作**強度 seed**。

流程：

1. 保留 spell identity / spell list / maximum spell level；
2. 確認 D100 對應最高環數；
3. 依 D100：

```text
total caster level = ring × 3 + modifiers
```

建立 D100 施法者等級；
4. 來源 CL 用來檢查轉完是否嚴重失真。

例如來源 CL31 的 9th-level caster，不應因轉譯後只剩 D100 CL15 而突然變成中階施法者。

---

# 13. 每日次數／recharge

### 可以近直接保留

```text
1/day
2/day
3/day
```

只要「day」在兩邊都是世界日。

### round recharge

先問：

```text
這是生理／物理冷卻？
還是設計上要求「隔 N 個自己的 turn 才能再用」？
```

前者走沙漏；後者走碼表。

不能看到 `1d4 rounds` 就機械 ×6，也不能機械保持 1d4。

---

# 14. CR：只作威脅輪廓，不換算

3.5 CR 不能直接翻成：

- D100 CP；
- HP；
- 技能值；
- 固定難度。

CR 只保留：

```text
這在來源世界屬於哪個戰力層級？
它是否本來就高於一般 20 級角色？
是單體 boss 還是普通遭遇？
```

真正 D100 encounter calibration 使用：

- PC Action Palette；
- PC 常用攻擊／閃避／抗性；
- PC damage output；
- 控制能力；
- monster TTK；
- monster 對 PC 的成功率。

---

# 15. 三種轉譯模式

每次正式換怪物，先標模式。

## A. Lineage mode — 系譜保真

適合規則考古／一般轉譯：

- 保來源能力結構；
- modifier 等價；
- 概率盡量接近；
- 不針對某隊 PC 特調。

## B. Encounter mode — 遭遇校準

適合真正跑團 boss：

- 以當前 PC 為 benchmark；
- 用命中率、控制成功率、TTK 校準；
- 仍不可改變來源生物的核心身份。

## C. World mode — 世界物理保真

適合追逐、旅行、環境：

- 優先保留秒／尺／里程／時間；
- 戰術 action count 次要。

同一個能力可以同時有 B + C，但必須明確說哪個數字由哪個模式決定。

---

# 16. 常用轉譯工作表

```text
SOURCE
- edition/source:
- role:
- size:
- shared abilities:
- attack / AC decomposition:
- saves / DC:
- HP / DR:
- speed / maneuverability:
- action economy:
- durations / recharge:
- spellcasting:
- ecology / tactics:

D100 SHARED ATTRIBUTES
- STR:
- DEX:
- CON:
- INT:
- WIS:
- CHA:

D100 MISSING ATTRIBUTES
- SKI seed + reason:
- RES seed + reason:
- SPI seed + reason:

PROBABILITY TARGETS
- ordinary attack hit chance:
- signature attack hit/control chance:
- PC resistance chance:
- monster resistance chance:

DEFENSE SPLIT
- dodge:
- block/shield:
- armor/physical resistance:
- DR / immunity:
- spell resistance:

DURABILITY
- desired successful heavy hits to defeat:
- healing/regeneration:
- escape threshold:

TIME
- world-time timers:
- tactical-window timers:
- hybrid timers:

ACTION PALETTE
- normal:
- free:
- immediate:
- spell quickening:
- extra windows:
- triggers:

STATUS
- [SOURCE_PROFILE]
- [D100_ADAPTATION_CANDIDATE]
- [ENCOUNTER_CALIBRATED]
- [OPEN_QUESTION]
```

---

# 17. LLM 保險絲

每次換算前自問：

> **我是在保留來源功能，還是在因為兩個數字看起來很像就硬抄？**

每次換算後再問：

> **這隻怪現在的強項／弱點還和來源是同一個嗎？**

若答案不確定，標 `[D100_ADAPTATION_CANDIDATE]`，用實戰 regression test 校準，不要偽稱 canon。
