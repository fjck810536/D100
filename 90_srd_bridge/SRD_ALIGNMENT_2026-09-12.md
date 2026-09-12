# D100 ↔ D&D 3.5 SRD Alignment / Provenance Report

> 日期：2026-09-12  
> 狀態：`[PROVENANCE_ONLY]`  
> 原則：**本檔只做系譜／來源對齊，不修改 D100 正典。遇到衝突、缺漏或語義不確定時，保留問題，不以 3.5 SRD 覆蓋 D100。**

## 0. 這份文件回答什麼

本輪對齊要分清四件不同的事：

```text
D100 Sheet          = 現行／歷史規則文本
Actual Play         = 規則實際怎麼被角色卡與玩家使用
D&D 3.5 SRD         = 一部分規則的來源／祖型
GM clarification    = 現在桌上要怎麼裁定
```

因此：

- 找到 3.5 同名條目，只能證明「有來源關係的可能／高度可能」。
- D100 已經明文改寫的數字或接口，以 D100 為準。
- 3.5 只能幫我們看出「這句話原本可能在解決什麼問題」，不能自動補回 D100。
- 同名但機械不同，**不得用名稱相似硬補能力**。

衝突與真正需要問 GM 的項目集中放在：

- `90_srd_bridge/OPEN_ALIGNMENT_QUESTIONS.md`

---

## 1. 本輪固定的上游 SRD 快照

### Primary

`Obsidian-TTRPG-Community/DnD-3.5-SRD-Markdown`

固定 commit：

```text
70a6b263e68604d8b2fb931937746161f2b65b58
```

主要用於：

- Basic Rules / Skills / Feats
- Prestige Classes
- Magic Items
- Spells
- Epic / Divine / Psionic SRD 區域

### Verification fallback

`olimot/srd-v3.5-md`

固定 commit：

```text
c7f30a0ce11a579f75456746f278a4c75f67b4c1
```

本輪主要用來交叉確認 Bard `Fascinate` 等文字。

### Conversion provenance

`katekorsaro/dnd3.5e-srd`

仍保留為格式／轉檔來源追查用；本輪沒有遇到需要靠它裁定的文字錯誤。

---

## 2. 對齊標籤

本檔使用以下狀態：

- `[DIRECT_LINEAGE]`：D100 條文與 3.5 SRD 在名稱、功能與敘述骨架上高度一致。
- `[SCALED_ADAPTATION]`：明顯沿用 3.5 內容，但把 d20 數學縮放／重建成 D100。
- `[D100_REWRITE]`：祖型清楚，但 D100 已明文改成自己的機械；**不是衝突**。
- `[MIXED_LINEAGE]`：名稱／概念和 3.5 有關，但能力包不是 3.5 SRD 那一套。
- `[NON_SRD_OR_UNKNOWN]`：在本輪 3.5 SRD corpus 找不到；可能來自非 SRD 3.5、其他版本、其他作品或自創。
- `[ALIGNMENT_QUESTION]`：D100 自身、角色卡與 3.5 系譜之間出現真正需要保留的問題。

---

# 3. 基本技能：大量是 3.5 Skill 的直接 D100 化

## 3.1 整體骨架 `[DIRECT_LINEAGE] [SCALED_ADAPTATION]`

3.5 Skill 系統原本以：

```text
1d20 + skill ranks + ability modifier + modifiers
```

處理固定 DC 或 opposed check。

D100 沒有保留這套核心數學，而是把技能重新放入六大複合分類、技能等級與 D100 判定；但大量技能的：

- 可做的事情
- 動作時間
- 對抗技能
- 失敗後果
- 特殊用途
- 原始 DC 語彙

都保留明顯 3.5 結構。

### 高度可辨識例子

| D100 | 3.5 SRD | 狀態 |
|---|---|---|
| 脫逃術 | Escape Artist | `[DIRECT_LINEAGE]` |
| 騎術 | Ride | `[DIRECT_LINEAGE]` |
| 平衡感 | Balance | `[DIRECT_LINEAGE]` |
| 攀爬 | Climb | `[DIRECT_LINEAGE]` |
| 躲藏 | Hide | `[SCALED_ADAPTATION]` |
| 潛行 | Move Silently | `[SCALED_ADAPTATION]` |
| 跳躍 | Jump | `[SCALED_ADAPTATION]` |
| 游泳 | Swim | `[DIRECT_LINEAGE]` |
| 威嚇 | Intimidate | `[SCALED_ADAPTATION]` |
| 使用魔法裝置 | Use Magic Device | `[D100_REWRITE]` |

## 3.2 很強的局部倍率：`×5`

一些條目能看到非常漂亮的轉換痕跡。

### 躲藏 / Hide

3.5 常見懲罰：

```text
-5
-10
-20
```

D100 對應條文出現：

```text
-25
-50
-100
```

### 威嚇 / Intimidate

3.5：

```text
體型每差一級 ±4
Bluff synergy +2
```

D100：

```text
體型每差一級 ±20
唬騙 Lv>=2 → +10
```

這表示局部存在：

```text
3.5 數值 ×5 → D100 百分尺度數值
```

但這**絕對不是全系統公式**。尤其 BAB、AC、spell save DC、HP、caster level 都不能照這個倍率搬。

## 3.3 威嚇證明 D100 的 `d100 + bonus` 接口有 3.5 系譜

3.5 Intimidate 對抗的是：

```text
1d20 + level/HD + Wisdom modifier + fear-save modifiers
```

D100 `威嚇` 改成：

```text
1d100 + 人物總HP/3.5 + RES加值 + 對恐懼的豁免加值
```

結構非常接近，但「等級／HD」被 D100 的 HP 等尺度重新建模。

因此：

> D100 存在 `d100 + 加值` 類對抗並不是例外事故；至少部分接口是從 3.5 opposed check 結構轉生而來。

但它仍然**不能被外推成 D100 所有判定的通則**。

---

# 4. 一般專長：`+2 paired-skill feat → +10 / Lv` 是強系譜

3.5 SRD 有大量「兩個技能各 +2」的 General Feat。D100 很多一般專長保留了完全相同的技能配對，再改成每級 +10。

| D100 | 3.5 SRD | 3.5 | D100 | 狀態 |
|---|---|---:|---:|---|
| 競技 | Athletic | Climb/Swim +2 | 攀爬/游泳 +10/Lv | `[SCALED_ADAPTATION]` |
| 靈活 | Agile | Balance/Escape Artist +2 | 平衡/脫逃術 +10/Lv | `[SCALED_ADAPTATION]` |
| 警覺 | Alertness | Listen/Spot +2 | 聆聽/偵察 +10/Lv | `[SCALED_ADAPTATION]` |
| 親和動物 | Animal Affinity | Handle Animal/Ride +2 | 馴養動物/騎術 +10/Lv | `[SCALED_ADAPTATION]` |
| 欺詐 | Deceitful | Disguise/Forgery +2 | 易容/偽造文書 +10/Lv | `[SCALED_ADAPTATION]` |
| 調查員 | Investigator | Gather Information/Search +2 | 搜集資訊/搜索 +10/Lv | `[SCALED_ADAPTATION]` |
| 談判專家 | Negotiator | Diplomacy/Sense Motive +2 | 交涉/察言觀色 +10/Lv | `[SCALED_ADAPTATION]` |
| 魔法天賦 | Magical Aptitude | Spellcraft/UMD +2 | 辨識法術/使用魔法裝置 +10/Lv | `[SCALED_ADAPTATION]` |
| 細緻 | Diligent | Appraise/Decipher Script +2 | 估價/文件解讀 +10/Lv | `[SCALED_ADAPTATION]` |

這一族是目前最乾淨的 D100 ← 3.5 轉譯證據之一。

---

# 5. `專注 / Concentration`：來源很清楚，但 D100 的底層技能缺失

## 5.1 3.5 原型 `[DIRECT_LINEAGE]`

3.5 `Concentration` 是獨立技能，關鍵屬性為 CON；受到傷害、惡劣環境、施法受干擾等會要求檢定。

3.5 `Combat Casting`：

```text
在 defensive casting / grappling / pinned 等情境
Concentration +4
```

D100 `戰鬥施法`：

```text
在防禦、被擒或壓制狀態下施法／類法術能力
專注檢定每級 +10
```

文字系譜非常明確。

## 5.2 不能直接補的部分 `[ALIGNMENT_QUESTION]`

D100 完整 31-tab mirror 找不到獨立 `專注` 基本技能；實際 GM 記憶則是「戰鬥施法＝專注線的主要承載者」。

因此 3.5 可以告訴我們**用途與祖型**，不能決定：

- D100 專注是哪個六大分類／基值
- 是否仍應以 CON 為核心
- 被傷害時的 D100 具體門檻
- 移動施法與專注如何交互

此問題保留，不補。

---

# 6. `搜集資訊 / Gather Information`：幾乎可確定是來源脫落，但仍不自動重建

3.5 Gather Information 是 CHA 技能：

```text
一般城市消息：DC 10
特定傳聞／物品／地圖：DC 15–25+
典型耗時：1d4+1 小時
可重試，但耗時且可能引人注意
```

3.5 另外明文：

```text
Investigator → Gather Information / Search +2
Knowledge (local) 5 ranks → Gather Information +2 synergy
```

D100 剛好保留：

```text
調查員 → 搜集資訊 / 搜索 +10/Lv
地方知識 → 搜集資訊加值
```

但 31-tab mirror 裡沒有獨立 `搜集資訊` 條目。

結論：

```text
Gather Information 是 D100「搜集資訊」祖型：高度確定
D100 現行正式分類／難度／耗時：仍未知
```

不能因來源清楚就自行補成「交涉、難度1、1d4+1小時」。

---

# 7. 使用魔法裝置 / Use Magic Device

3.5 UMD：

- CHA-based
- trained only
- activate blindly DC25
- scroll：DC `20 + caster level`
- wand：DC20
- 模仿 class feature / race / alignment 等

D100：

```text
使用魔法裝置
分類：感知
難度：2
卷軸：須過 20 + 卷軸環數×5
```

這是很清楚的 `[D100_REWRITE]`：用途祖型直接來自 UMD，但主屬性、技能系統、卷軸難度都已換成 D100。

因此不得把 3.5 的其他 UMD DC 直接補成 D100 DC。

---

# 8. 製作專長：名稱與敘述祖型高度明確，但經濟系統已重寫

## 8.1 對應關係

| D100 | 3.5 SRD | 狀態 |
|---|---|---|
| 調製藥水 | Brew Potion | `[D100_REWRITE]` |
| 抄錄卷軸 | Scribe Scroll | `[D100_REWRITE]` |
| 製造奇物 | Craft Wondrous Item | `[D100_REWRITE]` |
| 製造魔法武器及防具 | Craft Magic Arms and Armor | `[D100_REWRITE]` |
| 製造魔杖 | Craft Wand | `[D100_REWRITE]` |
| 製造權杖 | Craft Rod | `[D100_REWRITE]` |
| 製造長杖 | Craft Staff | `[D100_REWRITE]` |
| 鍛造戒指／項鍊 | Forge Ring | `[D100_REWRITE]` |

3.5 原先用 caster level prerequisites、XP cost、raw material cost、GP 價格與製作時間。

D100 已明確建立自己的：

- 技能難度／技能等級
- 施法環數前置
- CP 卡住／物品損毀後解放
- D100 加值系統
- 詞綴／素材／符文
- D100 製作時間
- 技能等級帶來的成本折扣

所以「3.5 要 CL12 才 Forge Ring，D100 只要求三環」不是要修的衝突，而是**明確重寫**。

## 8.2 真正遺留衝突：`XP / 經驗值` 用語 `[ALIGNMENT_QUESTION]`

D100 製作總則已改成 CP／金錢／時間；但部分製作條文仍保留非常 3.5 的句子，例如：

```text
修復魔法武器、盔甲或盾牌：
支付相當於製造時一半的經驗值、材料費和時間
```

其他少數製作文字也仍提到「經驗值」。

這可能是：

1. 純粹未清理的 3.5 遺留詞；
2. 現行應讀作 CP；
3. 舊版曾有另一種 XP 系統；
4. 某些特殊製作仍真的有獨立 XP 成本。

在 GM / Actual Play 證據出現前，不改。

---

# 9. 超魔專長：大部分祖型直接可辨識，D100 已重做資源經濟

| D100 | 3.5 SRD | 核心祖型 | 狀態 |
|---|---|---|---|
| 法術強效 | Empower Spell | variable numeric ×1.5 | `[D100_REWRITE]` |
| 法術增遠 | Enlarge Spell | range ×2 | `[D100_REWRITE]` |
| 法術延時 | Extend Spell | duration ×2 | `[D100_REWRITE]` |
| 法術極效 | Maximize Spell | variable numeric max | `[D100_REWRITE]` |
| 法術瞬唱 | Quicken Spell | extra-fast casting | `[D100_REWRITE]` |
| 法術默發 | Silent Spell | remove verbal | `[D100_REWRITE]` |
| 法術靜發 | Still Spell | remove somatic | `[D100_REWRITE]` |
| 法術升階 | Heighten Spell | raise effective spell level | `[ALIGNMENT_QUESTION]` |
| 法術擴展 | Widen Spell | area expansion | `[D100_REWRITE]` |

D100 還加入：

- 法術射線
- 元素轉換
- 元素擴散
- 聯合／融合施法
- 跨環施法
- 法術疊發
- 法術快速施放

這些不應因為名字類似而硬找 3.5 core SRD 對應。

## 9.1 `Quicken` 差異不是待修 bug

3.5：

```text
free action
one quickened spell / round
slot +4
no AoO
```

D100 `法術瞬唱`：

```text
即時動作
one / round
slot +3
3 SP
no AoO
```

D100 文字非常明確，因此記作 intentional/system rewrite；**不要把 +3 改回 +4。**

## 9.2 `法術升階` 是真正內部語義衝突

3.5 Heighten 明確提升的是：

```text
effective spell level
```

D100 第一行卻說：

```text
每技能等級 → 多追加 1 個施法者等級
```

下一句又說：

```text
所有與法術等級有關的變數，以升階後的法術等級計算
```

這裡同時出現：

```text
caster level
spell level
```

可能是用詞殘留、雙重效果、或 D100 曾修改到一半。**本輪不修，列問題。**

---

# 10. Bard / 吟遊詩人：基礎樂曲有非常強的 3.5 Bardic Music 系譜

3.5 Bardic Music 包含：

- Countersong
- Fascinate
- Inspire Courage
- Inspire Competence
- Suggestion
- Inspire Greatness
- Song of Freedom
- Inspire Heroics
- Mass Suggestion

D100 可辨識出：

| D100 | 3.5 | 狀態 |
|---|---|---|
| 破咒曲 | Countersong | `[D100_REWRITE]` |
| 迷魂曲 | Fascinate | `[ALIGNMENT_QUESTION]` |
| 激發勇氣 | Inspire Courage | `[D100_REWRITE]` |
| 提振技能 | Inspire Competence | `[D100_REWRITE]` |
| 提振戰力 | Inspire Greatness / related | `[MIXED_LINEAGE]` |
| 自由曲 | Song of Freedom | `[D100_REWRITE]` |
| 激發豪情 | Inspire Heroics / related | `[MIXED_LINEAGE]` |

## 10.1 `迷魂曲` 的祖型可回答「為什麼會有比較句」，但不能回答 D100 怎麼算

3.5 Fascinate：

```text
Bard makes a Perform check
Perform check result becomes the DC
Target makes Will save against that DC
```

D100：

```text
吟遊：表演 + Lv×10
目標：抗控制 - Lv×10
若目標檢定結果 >= 吟遊檢定結果 → 迷魂失敗
```

所以 D100 那句「雙方結果比較」不是憑空出現；它很可能是在翻譯：

```text
Perform check result = save target number
```

但 D100 有多種骰制接口，因此仍不知道「檢定結果」具體是：

- raw d100
- 判定總值
- 成功餘裕／過多少
- 另一種舊版角色卡慣例

**保留問題，不拿 3.5 直接決定。**

---

# 11. 3.5 Generic Opposed Check 的 tie 規則：只記祖型，不倒灌

3.5 generic skill opposed check：

```text
高結果勝
平手 → skill modifier 較高者勝
modifier 也相同 → 重骰
```

D100 目前：

- 有一般攻擊「成功後才進 dodge，再比過多少」
- 有 `d100 + bonus` 對抗
- 有獨立 save
- 有明文特殊比較

因此不可能假設所有 D100 tie 都沿用 3.5。

這條只能作為 `P0-1 對抗完全平手` 的 provenance 候選，不直接採納。

---

# 12. Natural 1 / 20：D100 已明確走自己的路

3.5 Skill check 明文：

```text
natural 20 ≠ automatic success
natural 1 ≠ automatic failure
```

D100 GM 已釐清：

```text
natural 01 = guaranteed 大成功
natural 00 / 100 = guaranteed 大失敗
```

這是清楚的 `[D100_REWRITE]`，不因 3.5 不同而產生待修問題。

---

# 13. Retry / Take 10 / Take 20：高度可能是「未帶進 D100 的 3.5 通則」

3.5 有完整 generic rules：

- 一般技能可重試，但依技能承擔失敗後果
- Take 10
- Take 20
- Take 20 代表反覆失敗直到成功，並花 20 倍時間

D100 大量技能文字源自 3.5，但目前完整 Sheet mirror 沒找到等價的全域 Take 10 / Take 20 規則。

目前 repo 對無限搜索採 `[DM_DEFAULT]`：同一方法一次骰決定目前資訊上限，只有新方法／新線索／更多合理時間才重骰。

這裡不能假設：

```text
D100 一定保留 Take 10 / Take 20
```

也不能假設：

```text
作者一定刻意刪掉
```

列為來源對齊問題。

---

# 14. Wizard school specialization：只有「八學派＋禁制學派」是強 3.5 系譜

3.5 Wizard 有：

- 八學派
- specialist wizard
- prohibited school(s)
- 額外學派法術位

D100 `法師學派專精` 的頂層結構明顯保留這一祖型。

但是 D100 各學派能力樹：

- 奧術防禦
- 投射防禦
- 王車易位
- 預兆
- 催眠凝視
- 次級鍊金
- 變化師之石
- 等等

並不是 3.5 SRD specialist wizard 的能力包。

本輪在 3.5 SRD 內也找不到 `Arcane Ward / Projected Ward / Minor Conjuration / Benign Transposition / Portent / Hypnotic Gaze` 等同一能力包。

因此：

```text
學派分類祖型：3.5 lineage
學派能力樹：mixed / non-SRD lineage
```

不得因「都是 Abjuration」就用 3.5 規則填 D100 空缺。

---

# 15. 特殊職業與後期職業包：同名搜尋非常容易誤導

## 15.1 魔射手 / Arcane Archer 是警告案例

3.5 SRD Arcane Archer：

- Enhance Arrow
- Imbue Arrow
- Seeker Arrow
- Phase Arrow
- Hail of Arrows
- Arrow of Death

D100 魔射手：

- 奧法箭
- 創造魔法箭
- 奧法射擊
- 虛弱箭
- 爆裂箭
- 防護箭
- 穿刺箭
- 追蹤箭
- 陰影箭
- 纏繞箭
- 誤導箭

它們共享「奧術弓箭手」概念，少數功能也可能同源，但能力包**不是同一個 Prestige Class progression**。

狀態：`[MIXED_LINEAGE]`

規則：**不因 D100 缺一級能力，就去補 3.5 Arcane Archer 的下一級能力。**

## 15.2 本輪 3.5 SRD 找不到的套件 `[NON_SRD_OR_UNKNOWN]`

本輪 primary SRD corpus 搜索沒有找到：

- Warlock / Eldritch Blast / invocations 套件
- Circle of the Moon / Dreams / Shepherd
- College of Glamour / Swords / Whispers
- Storm Sorcery / Shadow Magic / Aberrant Mind / Clockwork Soul / Lunar Sorcery
- Oath of Devotion 這套 subclass package
- 奈瑟瑞爾奧術師
- 咒火使者
- 魔法舞者 Spelldancer

這不代表它們「沒有來源」，只代表：

> **不能用 3.5 core/SRD corpus 來證明或補完。**

它們可能來自非 SRD 3.5 資料、其他版 D&D、其他遊戲或自創；若要追來源，應另開「非 SRD provenance」階段，不能靠記憶硬猜。

---

# 16. Cleric domains：部分名稱同源，不代表能力包同源

3.5 SRD domain list 包含：

```text
Air, Animal, Chaos, Death, Destruction, Earth, Evil, Fire, Good,
Healing, Knowledge, Law, Luck, Magic, Plant, Protection, Strength,
Sun, Travel, Trickery, War, Water
```

D100 目前有：

```text
Life, Trickery, Knowledge, War, Light, Arcana, Nature, Forge,
Tempest, Grave ...
```

其中 Knowledge / Trickery / War 等名稱直接重合，Light/Life/Arcana 等與 3.5 概念鄰近，但 D100 的整套領域技能樹、神力、神域等不是 3.5 domain power 的直接搬運。

因此：

```text
領域概念與部分 spell/domain vocabulary：3.5 lineage
D100 領域技能樹：mixed / non-SRD package
```

不得把 3.5 Domain Granted Power 自動塞回 D100。

---

# 17. Magic Items / Artifact：類型祖型清楚，神器分類已分叉

3.5 magic item 類別：

- armor / shields
- weapons
- potions
- rings
- rods
- scrolls
- staffs
- wands
- wondrous items
- cursed / intelligent items
- artifacts

D100 裝備類型、製作分類與 body-slot 思考顯然繼承很多這套 vocabulary。

但 D100 已有自己的：

- 魔法物品加值
- 詞綴上限
- 素材詞綴
- 符文
- 聖器／亞神器／神器
- 永恆聖器詞綴

所以 3.5 的：

```text
minor artifact / major artifact
```

不能取代 D100 分級。

## 17.1 Overwhelming aura

3.5 的 magic/psionic aura strength 系統確實存在 `Faint / Moderate / Strong / Overwhelming`，artifact 也會出現在最高強度脈絡。

D100 Sheet 目前沒有找到「所有神器必定 Overwhelming」的全域條文。

因此：

```text
3.5 artifact aura concept = [SRD_BRIDGE]
D100 artifact universal aura rule = unresolved / not canon
```

這和之前 GM 提過「21st+ / artifact → Overwhelming」的設計來源吻合，但仍不能倒灌成 Sheet 原文。

---

# 18. 時間尺度：這是所有 3.5 搬運的最高風險

```text
D&D 3.5 round = 6 sec
D100 round = 1 sec
```

所以任何：

- N rounds duration
- per-round damage
- regeneration / round
- recharge / round
- once-per-round

都不能純文字搬入。

尤其 D100 的行動經濟本身也已改寫，因此甚至不能簡化為「全部 ×6」。

---

# 19. 法術對齊策略

本輪不批次把 3.5 法術內容倒進 repo。

未來遇到單一 D100 法術需要追來源時，分兩步：

### 來源抽取

保留 3.5 的：

- spell name
- school
- target / area concept
- range concept
- components
- effect idea
- saving throw existence
- spell resistance existence
- original duration intent

### D100 重建

重新決定：

- 哪個施法職體系
- 幾環
- SP / spell slot
- D100 施法檢定
- 抗噴吐 / 抗控制 / 抗轉化 / 抗魔法 / 強韌 / 精神 / 靈魂
- 1 秒輪下的 duration
- D100 damage / resistance math

除非 D100 自己已經明文，不能把 3.5 Save / SR / CL / DC 直接搬。

---

# 20. 本輪結論

最強的 3.5 ancestry 集中在：

```text
基本技能文字
一般專長配對
部分對抗檢定結構
製作專長名稱／物品分類
超魔專長
Bardic Music
Wizard 八學派／專精概念
magic-item vocabulary
```

而 D100 最明顯已獨立成自己的地方是：

```text
D100 多種判定接口
六大技能／五抗／三特殊判定
CP 技能成長
HP/SP
一秒輪
施法者等級與 spell slot / SP economy
詞綴／符文／聖器系統
大量 subclass / special-class ability trees
後期傳奇／外神／自訂能力
```

所以後續 GPT 應該把 3.5 當成：

> **語源、祖型、缺漏線索。**

而不是：

> **D100 沒寫就去 3.5 抄答案。**
