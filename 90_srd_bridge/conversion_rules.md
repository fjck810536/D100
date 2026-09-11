# D&D 3.5 SRD → D100 補缺規則

本檔的目的不是把 D100 還原成 3.5，而是在 D100 內部**真的缺資料**時，安全利用 3.5 SRD 的概念與內容。

## 1. 優先資料源

### Primary

`Obsidian-TTRPG-Community/DnD-3.5-SRD-Markdown`

用途：結構化 Markdown、技能／專長／法術／怪物索引，適合 GPT 搜索與建立 bridge。

### Verification fallback

`olimot/srd-v3.5-md`

用途：用另一份 Markdown SRD 交叉核對可疑條目。

### Conversion provenance

`katekorsaro/dnd3.5e-srd`

用途：當文字像是轉檔錯誤時，追查 RTF → Markdown 的轉換來源。

## 2. 規則優先序

3.5 SRD 永遠低於 D100 正典。

```text
D100 house rule / campaign rule
> D100 Sheet
> 本 repo D100 canon
> D100 derived
> DM default
> SRD bridge
> raw 3.5 SRD
```

如果 D100 已經改寫某技能、專長、職業、法術或怪物，就**不能**拿 3.5 原數值覆蓋回去。

## 3. 可以相對安全搬的東西 `[SRD_BRIDGE]`

優先搬「概念」，不是數字：

- 技能的用途與可做的事情
- 專長概念與前置樹
- 法術名稱、學派、目標型態、範圍概念
- 裝備種類
- 怪物能力概念、感官、生態、語言
- 環境危險的情境分類
- 狀態概念
- artifact 的「特殊規則物件」設計哲學

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
- caster level 直接換算
- attribute prerequisites
- 每日次數與 6 秒輪頻率

## 5. 最大時間陷阱：3.5 六秒輪 vs D100 一秒輪

```text
D&D 3.5：1 round = 6 seconds
D100：1 round = 1 second
```

所以：

```text
3.5 lasts 10 rounds
```

絕對不能不思考就寫成：

```text
D100 lasts 10 rounds
```

否則實際時間由 60 秒變 10 秒。

同理：

- regeneration / round
- poison tick / round
- 1/round ability
- recharge / round

直接搬會把頻率提高 6 倍。

## 6. 已觀察到的轉譯模式：+2 → +10 `[D100_DERIVED]`

D100 已有多個由 3.5 paired-skill feat 改寫的例子，例如：

- Athletic 類 → `競技`：攀爬／游泳每級 +10
- Agile 類 → `靈活`：平衡／脫逃術每級 +10
- Alertness 類 → `警覺`：聆聽／偵察每級 +10

這顯示局部存在：

```text
3.5 +2 skill bonus
≈ D100 +10
```

但這只是**觀察到的局部 pattern**，不是「所有 3.5 數字 ×5」。

禁止把：

```text
BAB +4 → D100 +20
AC +8 → D100 +40
spell DC 18 → D100 DC 90
```

當成通則。

## 7. d20 DC → D100「須過 X」候選 `[SRD_BRIDGE]`

D100 已有大量技能條文把難度寫成：

```text
須過5
須過10
須過20
須過25
```

這與 3.5 技能 DC 語彙存在結構上的延續。

因此在**沒有任何 D100 對應值**時，可把：

```text
3.5 DC X
```

作為候選：

```text
D100 成功餘裕須過 X
```

但這仍是 `[SRD_BRIDGE]`，必須先與更多已轉譯技能交叉驗證，不能批次套用成正典。

## 8. 缺漏技能的處理

目前已找到兩個 D100 內部引用但基本技能表未見獨立定義的技能：

### 專注 / Concentration

D100 `戰鬥施法` 明文引用「專注檢定」。

3.5 SRD 有 Concentration，可提供：

- 技能用途
- 觸發情境
- 失敗後果概念

但不能直接決定 D100 的：

- 所屬六大分類
- 難度
- DC 換算

所以目前仍 `[OPEN_QUESTION]`。

### 搜集資訊 / Gather Information

D100 `調查員` 與地方知識明文引用「搜集資訊」。

3.5 SRD 可提供技能用途與一般耗時概念；在正式採納前只可寫候選條目。

候選方向：

```text
搜集資訊
分類候選：交涉
難度候選：1
技能等級：每級 +10
典型耗時：可參考 SRD 的小時級調查
```

不得把候選寫成 `[D100_CANON]`。

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

再為 D100 重新建立：

```text
九屬性（若需要）
戰鬥／運動／操作／感知／知識／交涉
五抗
強韌／精神／靈魂
攻擊判定
閃避／防禦
HP / SP
傷害
特殊能力的 D100 接口
```

不要用 AC、BAB、Fort/Ref/Will 直接換算。

## 10. 法術轉譯

先抽取：

- 學派
- 目標
- 距離
- 範圍
- 成分
- 效果敘述
- 是否允許 Spell Resistance
- 是否有 saving throw
- 持續時間

再回答：

1. D100 使用哪個施法職體系？
2. 幾環？
3. SP／法術位如何消耗？
4. 是否要施法判定？
5. 效果防禦接口是抗噴吐、抗控制、抗轉化、強韌、精神、靈魂還是法抗？
6. 原 3.5 的 rounds 如何換為 D100 1 秒輪？

## 11. Artifact 轉譯

3.5 artifact 可以提供：

- minor / major artifact 概念
- 特殊啟動條件
- 特殊副作用
- 特殊摧毀條件
- 非一般製作物品的定位

但 D100 已經有自己聖器／亞神器／神器與神器級詞綴系統，所以 3.5 分類不可直接取代 D100 分類。

3.5 `Overwhelming aura` 也只能在該團採用 bridge 時使用，不能假裝 D100 Sheet 已經寫了這條。

## 12. LLM 固定提示

任何 GPT 在引用 SRD 時，必須先自問：

> 「這是 D100 已有規則，還是我正從 3.5 補缺？」

若是後者，在規則文件／DM 幕後筆記標記 `[SRD_BRIDGE]`。

**永遠不要把熟悉的 3.5 規則用記憶偷偷補進 D100。**
