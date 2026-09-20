# D100 領域專長轉譯規約

> 狀態：`[D100_ADAPTATION_PROVISIONAL]`
>
> 目的：把 3e/3.5 Domain 的 granted power + domain spell identity，轉成符合 D100 現有領域設計語法的五階專長；不把 d20 數字直接搬進 D100，也不修改來源法術詞條。

## 1. 現有 D100 領域的共同骨架

現有生命、詭術、知識、戰爭、光明、奧秘、自然、鍛造、暴風、墳墓領域呈現穩定的五階梯：

| 難度 | D100 常見職責 |
|---|---|
| 1 | 領域身份核心：被動、技能接口、窄用途 granted power |
| 2 | 主動引導神力：單體／小範圍能力、反應、移動、驅散／控制 |
| 3 | 領域掌握：強化、反應、持續防護、條件／環境控制 |
| 4 | 高強度輸出或施法奧義：武器灌注、抗性穿透、強力施法 |
| 5 | 領域顯現／神域／化身：範圍性 capstone |

這個結構與 5e cleric 常見 1/2/6/8/17 級領域特徵高度同構，但 D100 的數值、行動與技能成本以自身規則為準。

## 2. 來源使用規則

```text
3e/3.5 granted power
→ 決定 D1 的功能核心

domain spell list / domain identity
→ 決定 D2–D5 的主題與能力邊界

D100 既有十領域
→ 決定數值預算、使用次數、範圍、持續時間、抗性接口

d20 raw bonus / AC / save DC / HD table
→ 不直接搬
```

禁止因中文名稱相近合併不同領域：Healing ≠ Life、Magic ≠ Arcana、Sun ≠ Light、Storm ≠ Tempest、Repose ≠ Grave、Artifice ≠ Craft ≠ Forge、Cold ≠ Winter。

## 3. 常用 D100 預算

### D1
- 窄技能：常用 `+技能等級×10` 或 floor 到「基礎值＋技能等級×10」。
- 3.5 的 `+1 caster level`：優先轉成「指定法術的總施法者等級＋技能等級」，而不是命中率 ×5。
- 窄免疫可保留，但不得擴張到語義相鄰效果。

### D2–D3
- 主動範圍常見 `技能等級×15~20 ft`。
- 使用次數常見 `技能等級＋相關調整值`。
- 抗性／技能增減通常 `技能等級×10`。
- 轉化 3.5 turn/rebuke 時使用 D100 抗控制／既有驅散接口，不搬 HD 表。

### D4
武器灌注常用：
```text
range = 技能等級×10 ft
duration = 技能等級 minutes
uses = 技能等級×2
penetration ≈ 技能等級×10
extra damage ≈ (技能等級 + SPI調整值)D8
```

施法型 D4 則優先用：
```text
可影響環數 = 技能等級×2
施法判定 + 技能等級×10
或 total caster level + 技能等級
```

### D5
```text
radius ≈ 技能等級×30 ft
duration ≈ 技能等級 minutes
uses ≈ 技能等級
主要增減值 ≈ 技能等級×10~20
```

D5 可以強，但不能藉「領域顯現」偷新增未有來源的致死規則、秘密資訊、人格改寫或世界事實。

## 4. Planar Domain

3.5 的 planar domain 明文比普通 domain 強，並占兩個 domain choices。D100 第一版保留：

```text
domain_choice_cost = 2
alignment requirement = 依來源
planar domain = 創角 review
```

其 D1–D5 仍使用同一難度階梯，避免另建第二套成本系統。

## 5. 狀態標記

- `implemented_existing_d100`：直接使用上游 D100 領域。
- `adapted_provisional`：已可跑，但屬 D100 調整工程，不冒充 Sheet 正典。
- `review_flags`：記錄高影響、版本敏感、製作經濟、位面規則、致死或其他仍需壓測處。

完整機械資料：`domain_feat_catalog.json`。
