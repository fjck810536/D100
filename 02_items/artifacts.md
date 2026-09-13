# 聖器／亞神器／神器

> 本檔是 D100 artifact 規則索引，不是神器人格模塊。D&D 3.5 只作 bridge / source reference，轉譯細節回到 `../90_srd_bridge/`。神器若具有自主意志，依 `../DATA_ARCHITECTURE.md` 的 Entity Agency 處理。

## 1. D100 已確認存在神器級分類 `[D100_CANON]`

來源表至少出現：

- 聖器
- 亞神器
- 神器

另在「永恆聖器詞綴」來源文字中出現「次神神器」稱呼。兩種中間級名稱是否完全同義，目前為 `[OPEN_QUESTION]`。

## 2. 幻夢境不複製神器級物品 `[D100_CANON]`

`夢境潛入` 明文：幻夢境會擬似主位面角色的一般素質、物品與技能，但**聖器、亞神器、神器除外**。

因此神器級物品至少具備一項現行世界規則：

> 它們不能被一般幻夢境擬似物品機制複製。

DM 不得把它們當普通 +X 魔法物品處理。

## 3. 神聖灰燼與神器級詞綴 `[D100_CANON]`

「永恆聖器詞綴」來源說明：

> 從聖器、次神神器、神器被破壞後殘餘得到的神聖灰燼，可在 +10 魔法物品上附上一個聖器／次神器／神器等級詞綴；此詞綴不計入兌換加值、不計入物品詞綴上限、不帶有一般加值。

這表示 D100 的神器級效果可以是一個**越過普通魔法物品加值經濟的特殊規則層**。

## 4. 已有神器級詞綴例 `[D100_CANON]`

現行「永恆聖器詞綴」包括例如：

- `奪命`：爆擊後要求強韌檢定；失敗可立即死亡。
- `聖輝`／`邪典`：陣營限制、額外傷害、抗噴吐、抗魔法與抗性穿透。
- `星空`：讓使用者軀體轉瞬傳送至星界，一輪內無視大部分法術／攻擊。
- `幽影`：靈體化並可召喚影龍。
- `瞬動`：可使用時間停止。
- `昇環`：提升施法者等級並視作環數提升。
- `吉兆`：每日額外重骰。

因此：

> **D100 神器級內容本來就允許普通戰鬥規則以外的特殊例外。** `[D100_DERIVED]`

## 5. 不要假設神器「免疫一般規則」 `[DM_DEFAULT]`

神器可以有特殊規則，但例外應來自神器條文本身。

不要因為物品被叫做神器就自動宣布：

- 無法偵測
- 無法解除
- 無法破壞
- 無視所有抗性
- 自動命中
- 自動控制

若需要這些性質，寫進該神器 statblock。

## 6. Artifact Agency

神器首先是 Entity / Item，不是預設人格。

```yaml
agency:
  type: none | reactive | autonomous
```

- `none`：普通神器物件，由會計師追持有／流轉、圖書館員讀規則、AO處理世界效果。
- `reactive`：依 trigger 回應，接 `TRIGGERED_HAZARD_TEMPLATE.md` 類型的 sensor / predicate / effect / reset 結構。
- `autonomous`：具有自身感官、belief、preference、目的與行動能力；視為 actor，可進入分析師／生態學家／政治家等 pipeline，同時仍可被會計師追蹤其物件身分。

`持有神器` 不等於 `神器意志屬於持有者`。

## 7. 調查神器的分層 `[DM_DEFAULT]`

面對一件外觀樸素的古代神器，不要一次檢定全知。

### 物理層

- 搜索：裝訂、機關、隱藏頁、材質異常
- 估價：年代、工藝、珍稀性

### 魔法物品層

- 魔法物品學：物品結構、異常加值、是否超出一般製作框架
- 辨識法術：目前作用中的法術／靈光結構
- 魔法陣基礎學：巨型陣式／幾何結構

### 文本層

- 文書解讀：看懂古文字
- 奧術／宗教／位面知識：理解內容脈絡

### 危險作用層

依真正效果選：

- 精神灌注 → 精神
- 強制意志 → 抗控制
- 形態改寫 → 抗轉化
- 抽魂 → 靈魂
- 法抗／穿透 → 抗魔法

## 8. 神器的多階段效果 `[DM_DEFAULT]`

範例：古魔法書內同時有強大精神力與轉化機制。

合理寫法：

```text
閱讀／理解觸發
→ 精神灌注（精神判定）
→ 若灌注建立模板，才啟動轉化
→ 抗轉化
```

兩個判定代表兩個因果階段。

不要僅因它是「魔法神器」再額外塞一個無條件抗魔法。

## 9. D&D 3.5 Artifact Bridge `[SRD_BRIDGE]`

3.5 artifact 可以提供：

- minor / major artifact 概念
- 特殊啟動條件
- 特殊副作用
- 特殊摧毀條件
- intelligent item / special purpose / Ego 等 agency 設計參考
- Detect Magic 的 artifact aura 概念

但這些都是 source / schema inspiration，不是 D100 canon。

若需要具體換算或 3.5 規則細節，回到：

```text
../90_srd_bridge/conversion_rules.md
```

不得讓 `02_items/artifacts.md` 變成第二份 3.5 規則庫。

## 10. Overwhelming 不等於位面級範圍 `[SRD_BRIDGE]`

3.5 的 `Overwhelming` 描述的是靈光**強度**，不是自動代表靈光大小與整個位面相同。

若某件 D100 神器另外設定：

> 神器效應／靈光與整個物質位面共延展

那是神器本身的特殊條目，而不是 artifact 分類的通則。

## 11. 位面級背景與探測 `[DM_DEFAULT]`

若神器的魔法存在真的與整個位面重疊：

- 探測能力可能成功知道「有魔法」。
- 但在任何局部區域都看到同一背景時，未必能定位神器本體。
- 書本位置的讀數可能與背景沒有差分。

應區分：

```text
偵測存在 ≠ 定位來源 ≠ 理解機制
```

## 12. 建議神器 statblock `[DM_DEFAULT]`

```md
# 名稱

entity_id:
狀態：神器／亞神器／聖器
agency: none | reactive | autonomous
外觀：
已知來源：
source_refs: []

## 可被調查的資訊
- 搜索：
- 估價：
- 魔法物品學：
- 辨識法術：
- 知識：

## Trigger / Activation

## 主效果

## 防禦接口

## 成功結果

## 失敗結果

## 持續／階段

## 抗魔法互動

## 遮蔽／偵測例外

## 可否複製

## 摧毀／封印條件

## 持有／流轉
item_holder_ref:
resource_state:

## Secret refs
secret_refs: []
```

完整 protected payload 依 `MYSTERY_PROTOCOL.md` 保存；statblock 只取合法 view。

若 `agency: reactive`，Trigger / Activation 可另接 `templates/TRIGGERED_HAZARD_TEMPLATE.md`。

若 `agency: autonomous`，另外建立其 actor belief / preference / capability state，而不是把「智能神器」硬塞成物品備註文字。
