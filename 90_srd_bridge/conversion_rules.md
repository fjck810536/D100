# D&D 3.5 SRD → D100 補缺規則

本檔的目的不是把 D100 還原成 3.5，而是在 D100 內部**真的缺資料**時，安全利用 3.5 SRD 的概念與內容。

常用數值／概率／時間換算方法另見：

- [`COMMON_CONVERSION_REFERENCE.md`](COMMON_CONVERSION_REFERENCE.md)

該檔是 `[CONVERSION_REFERENCE]`，不是 D100 Sheet 正典。

## 1. 優先資料源

### Primary

`Obsidian-TTRPG-Community/DnD-3.5-SRD-Markdown`

固定來源快照見 `SRD_ALIGNMENT_2026-09-12.md`。

用途：結構化 Markdown、技能／專長／法術／怪物索引，適合 GPT 搜索與建立 bridge。

### Verification fallback

`olimot/srd-v3.5-md`

用途：用另一份 Markdown SRD 交叉核對可疑條目。

### Conversion provenance

`katekorsaro/dnd3.5e-srd`

用途：當文字像是轉檔錯誤時，追查 RTF → Markdown 的轉換來源。

非 SRD 的 3.5 內容（例如 Dragon Magazine）必須另外鎖定來源版本，不能因同名能力混入 5e、Pathfinder 或 homebrew。

## 2. 規則優先序

3.5 永遠低於 D100 正典。

```text
D100 house rule / campaign rule
> D100 Sheet
> 本 repo D100 canon
> clarified GM provisional
> D100 derived
> DM default
> SRD bridge
> raw 3.5
```

如果 D100 已經改寫某技能、專長、職業、法術或怪物，就**不能**拿 3.5 原數值覆蓋回去。

## 3. 可以相對安全搬的東西 `[SRD_BRIDGE]`

優先搬「概念」，不是數字：

- 技能用途與可做的事情
- 專長概念與前置樹
- 法術名稱、學派、目標型態、範圍概念
- 裝備種類
- 怪物能力概念、感官、生態、語言
- 環境危險的情境分類
- 狀態概念
- artifact 的特殊規則物件設計哲學
- NPC／怪物的性格、戰術習性與撤退條件

## 4. 不可直接搬的東西

以下必須人工轉譯：

- d20 DC
- attack bonus / BAB
- AC
- Fort / Reflex / Will
- 3.5 class level progression
- hit dice / HP
- Challenge Rating
- spell save DC
- 3.5 action economy
- round-based timing
- caster level 的最終 D100 機械
- attribute prerequisites
- 每輪頻率／recharge

其中**共享能力值 STR/DEX/CON/INT/WIS/CHA 也不建議 raw score 直接照抄**；若沒有 D100 canonical 值，優先使用 `COMMON_CONVERSION_REFERENCE.md` 的 modifier-equivalent anchor。

## 4.1 禁止直搬 ≠ 禁止轉譯：AO 必須完成可結算 adaptation

本節是 anti-paralysis contract。

前節「不可直接搬」禁止的是：

```text
來源數字 / d20 接口
→ 不經語義判斷直接塞進 D100
```

它**不表示**：

```text
來源效果已知
+ D100 有相近功能接口
→ 因沒有現成換算公式而禁止結算
```

若來源效果的功能、對象與因果已足夠明確，AO / orchestrator 應依下列順序完成轉譯：

```text
1. 抽取來源功能：它原本改變什麼？
2. 對應 D100 已存在的功能層：命中／閃避／格擋／鎧甲／抗性／狀態／world-state mutation...
3. 用 D100 現有裝備、技能、法術或概率作 calibration anchor。
4. 產生最小、可逆、可結算的 [SRD_BRIDGE] / [D100_ADAPTATION_CANDIDATE]。
5. 保留 provenance 與 conversion note；之後有更高權威資料時可 supersede。
```

只有在「來源本身不清楚」、「與 D100 硬規則直接衝突」或「多個候選接口會造成實質不同因果且當下沒有任何 calibration anchor」時，才可把精確轉譯標成 unresolved。

即使如此，若場景現在必須結算，仍依 AGENTS.md 的缺規則原則做**最小可逆裁定**；不得把 unresolved_conversion 演成「法術失效／不能使用」。

核心保險絲：

```text
NO RAW COPY ≠ NO CONVERSION
UNKNOWN EXACT VALUE ≠ PROHIBITED EFFECT
SOURCE GAP ≠ RUNTIME STOP
```

### Armor-bonus 類法術的預設方向

若來源給的是 armor bonus to AC，不要映射成 D100 閃避。先保留它的功能類別：

```text
source armor protection
→ D100 armor / protective-layer semantics
```

數值用來源中的**裝甲保護階級**對照 D100 `擅長鎧甲` 的基礎減傷階級做 calibration，而不是把 AC 數字乘五或塞進命中率。

例如 Mage Armor / Greater Mage Armor 類：

- 是魔法保護層，不要求真的穿鎧甲；
- 不因沒有鎧甲熟練而產生實體鎧甲的技能減值；
- force 性質應保留為 effect tag，讓虛體／穿透等特殊互動能由 AO 判斷；
- 普通版與 Greater 版的相對強弱必須保留；
- 若 D100 尚無專門 force-armor 條目，AO 以最接近的 D100 鎧甲保護階級建立 provisional protective layer，而不是停止結算。

---

## 5. 時間陷阱：不是所有 3.5 round 都 ×6，也不是都 1:1

```text
D&D 3.5：1 round ≈ 6 seconds
D100：1 round = 1 second
```

但來源中的 `round` 可能在描述兩種不同東西。

### A. 世界時間／沙漏

如果效果真正關心的是物理經過時間：

- 行走／飛行速度
- 燃燒
- 毒素發作
- 建築／環境變化
- 增援抵達
- 秒／分鐘／小時級持續

可先按：

```text
1 source round ≈ 6 world seconds
```

再切成 D100 秒數。

### B. 戰術窗口／碼表

如果來源 `N rounds` 真正表示：

- N 個 turn
- N 次 action opportunities
- once per round
- extra action
- 冷卻 N 個自己的回合
- 一個通常維持一場戰鬥 N 輪的資源池

則優先保留**戰術窗口數**，不機械 ×6。

例如來源 `time stop 1d4+1 rounds` 的戰術意義首先是「施法者得到 2～5 個私人行動窗口」，不是自動得到 12～30 個 D100 行動。

### C. 混合型時間魔法

Time Stop / Slow / Haste / Time Expulsion 等至少分記：

```text
external world time
subjective time
action windows
cooldown clock basis
```

不能只記一個 `remaining rounds`。

## 6. 已觀察到的局部轉譯模式：+2 → +10 `[D100_DERIVED]`

D100 已有多個由 3.5 paired-skill feat 改寫的例子，例如：

- Athletic 類 → `競技`：攀爬／游泳每級 +10
- Agile 類 → `靈活`：平衡／脫逃術每級 +10
- Alertness 類 → `警覺`：聆聽／偵察每級 +10

這顯示局部存在：

```text
3.5 +2 skill bonus
≈ D100 +10
```

但這只是**局部 lineage pattern**，不是「所有 3.5 數字 ×5」。

禁止：

```text
BAB +4 → D100 +20
AC +8 → D100 +40
spell DC 18 → D100 DC 90
```

## 7. d20 DC → D100：優先概率等價

舊 bridge 曾使用：

```text
3.5 DC X
→ D100 須過 X
```

作為無資料時的候選。

這個 pattern 在部分 skill lineage 上仍可當快速 seed，但現在更穩的方法是：

1. 算來源 `bonus vs DC` 的成功率；
2. 決定 D100 角色的判定值；
3. 反推「須過多少」或對抗值，使成功率接近。

詳見 `COMMON_CONVERSION_REFERENCE.md`。

所以 **DC 本身沒有單獨的跨系統等價值**。

## 8. 缺漏技能：已釐清的 bridge

### 戰鬥施法 / Concentration

GM 第二輪補答已確認：D100 不另建 Concentration 技能。

```text
未購戰鬥施法：戰鬥 -20
戰鬥施法 Lv0：戰鬥
戰鬥施法 LvN：戰鬥 + Lv×10 + modifiers
```

3.5 Concentration 只提供：

- 哪些干擾情境需要檢定；
- 原本設計在解決什麼問題。

實際骰法使用 D100 `戰鬥施法`。

### 搜集資訊 / Gather Information

GM 已允許由 3.5 reconstruction：

```text
搜集資訊（交涉，難度1）
一般消息：須過10
特定傳聞／物件／地圖：通常須過15～25+
典型耗時：1d4+1 小時
```

並保留：

```text
調查員 → +10/Lv
地方知識 Lv2+ → +10
```

目前標記 `[SRD_BRIDGE + GM_PROVISIONAL]`，不是假裝 Sheet 仍有完整原始列。

## 9. 怪物轉譯

轉一隻 3.5 怪物時，先保留：

- 體型
- 感官
- 移動方式
- 語言
- 特殊攻擊概念
- 特殊品質概念
- 抗性／免疫概念
- 生態與戰術
- 年齡／階段差異
- NPC 知識邊界與 morale

再為 D100 重新建立：

```text
共享屬性 modifier-equivalent anchors
SKI / RES / SPI seeds
戰鬥／運動／操作／感知／知識／交涉
五抗
強韌／精神／靈魂
攻擊判定
閃避／格擋／鎧甲／DR
HP / SP
傷害
特殊能力的 D100 接口
Action Palette
時間與移動 ledger
```

### AC 必須拆層

來源 AC 不可整個換成 D100 Dodge。

至少分：

```text
DEX / dodge / mobility → 閃避
natural armor / armor → 鎧甲／物抗
shield → 格擋
DR → damage reduction
miss chance / displacement → 特殊防禦
```

巨大、touch AC 很低、natural armor 很高的怪物應該是：

> 容易碰到，但難打穿。

不是「閃避超高」。

## 10. HP / 傷害／CR

### HP

不要直接搬 HD / HP。

優先用：

```text
TTK / successful heavy hits to defeat
```

校準 D100 的：

- HP
- armor
- DR
- resistances
- regeneration / healing
- escape threshold

### 傷害

先比較來源傷害占同階角色 HP 的比例，再決定 D100 傷害。

共享屬性傷害（STR/DEX/CON 等）可把來源數字當 seed，但要檢查 D100 屬性尺度與 0 值後果。

### CR

只保留「來源威脅層級／角色定位」。

不得：

```text
CR → CP
CR → HP
CR → 技能值
```

## 11. 移動

來源 listed speed 是每個 move action 的距離。

如果需要世界物理速度 seed：

```text
ft/s ≈ source listed speed / 6
```

但戰鬥中還要另外處理：

- double move / run
- charge
- haste
- maneuverability
- D100 action economy

`clumsy / poor / average / good / perfect` 是**機動性**，不應直接改寫 raw DEX。

## 12. 法術轉譯

先抽取：

- 學派
- 目標
- 距離
- 範圍
- 成分
- 效果敘述
- 是否允許 Spell Resistance
- saving throw 的原始功能
- 持續時間
- action type

再回答：

1. D100 使用哪個施法職體系？
2. 幾環？
3. SP／法術位如何消耗？
4. 是否要施法判定？
5. 防禦接口是抗噴吐、抗控制、抗轉化、強韌、精神、靈魂還是法抗？
6. 時間是沙漏還是碼表？
7. 原本 action economy 如何映射 D100 Action Palette？

### Caster Level

來源 CL 可以作強度 seed，但最終仍依 D100：

```text
total caster level = ring×3 + modifiers
```

重建。

### Spell Resistance

`SR X` 不直接換成 `抗魔法 X`。

先看來源同階施法者突破 SR 的概率，再用 D100 抗魔法／法術穿透重建。

## 13. Artifact 轉譯

3.5 artifact 可以提供：

- minor / major artifact 概念
- 特殊啟動條件
- 特殊副作用
- 特殊摧毀條件
- 非一般製作物品的定位

但 D100 已有自己的聖器／亞神器／神器與神器級詞綴系統，所以 3.5 分類不可直接取代 D100 分類。

3.5 `Overwhelming aura` 也只能在該團採用 bridge 時使用，不能假裝 D100 Sheet 已經寫了這條。

## 14. 三種換算模式

轉譯前可標：

```text
Lineage mode   = 保來源結構／概率，不針對某隊平衡
Encounter mode = 以當前 PC 命中率、抵抗率、TTK 校準
World mode     = 優先保秒、距離、旅程與物理時間
```

同一生物可以同時用多種 mode，但每個數字要知道自己在保什麼。

## 15. LLM 固定提示

任何 GPT 在引用 3.5 時，必須先自問：

> 「這是 D100 已有規則，還是我正從 3.5 補缺？」

再問：

> 「我是在保留來源功能，還是只因兩個數字看起來相似就硬抄？」

若是 bridge，在規則文件／DM 幕後筆記標記 `[SRD_BRIDGE]`、`[D100_ADAPTATION_CANDIDATE]` 或其他正確狀態。

**永遠不要把熟悉的 3.5 規則用記憶偷偷補進 D100。**
