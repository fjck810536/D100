# 創角未決規則地圖

> 本檔只記「已知存在但尚缺完整來源／分類」的創角問題，避免 Character Builder 為了完成角卡而自行補規則。

---

## P0-CREATE-1 近戰／法術 qualifying CP 的精確分類

上游創角表明文存在：

```text
近戰相關 CP 投資
法術相關 CP 投資
```

並以其門檻決定 reward HP/SP。

角色卡證據也顯示：

```text
總技能 CP
≠ qualifying melee CP
≠ qualifying spell CP
```

但目前尚缺完整可追溯的「每個技能／專長到底算入哪一池」分類表。

### 安全處理

- 有角色卡／明文 evidence 的分類直接使用；
- 只能確定部分時，先維護可證明的 qualifying floor；
- 不把所有 `戰鬥` 分類技能機械地視為近戰 CP；
- 不把施法者持有的所有技能機械地視為法術 CP；
- 不把總技能 CP 全塞入其中一池。

若後續 build 跨過 reward threshold，依新增 qualifying investment 補足應得獎勵。

---

## P0-CREATE-2 CP → raw/basic stat 的正式換算

GM 已明確說明：CP 可以用來填補「基礎數值」與 HP/SP 缺口。

HP/SP 的 CP 換算已由上游 Sheet 明文。

但目前尚未定位到可安全使用的：

```text
CP → 九大 raw/basic stat
```

正式公式／成本曲線／上限。

### 安全處理

在找到 Sheet、角色卡 evidence 或 GM 明確公式前：

- 可以告知此用途存在；
- 不自行幫自動角色買 raw stat；
- 不自行假設 `1 CP = 1 stat` 或其他比例；
- 需要補洞時優先使用已有明文的技能、HP/SP 或保留 CP。

---

## P1-CREATE-1 語言 Lv0–LvN 的精確熟練度描述

已知：

- 語言通常不做一般技能檢定；
- 等級表示熟練度；
- 施法文化門檻只需要難度2語言 Lv1；
- 創角免費通用語 Lv3。

未知：

```text
Lv0 / Lv1 / Lv2 / Lv3 ...
各自精確能做到什麼程度？
```

例如：

- 是否能日常對話；
- 是否能閱讀專業文獻；
- 是否接近母語；
- 是否包含讀寫能力。

在完整表被找到前，不要自行套 CEFR 或「Lv3=母語級」之類固定對照。

---

## P1-CREATE-2 施法者語言門檻的世界內機制

GM 已確定 mechanical creation gate：

```text
施法者至少一門難度2語言 Lv1+
```

但目前尚未固定其世界內單一解釋：

- 高階術式術語？
- 位面／神學／奧術教育？
- 古代文獻閱讀？
- 魔法傳統身份？

因此 Builder 可以依角色文化解釋，但不要宣稱所有施法者都因同一理由需要該語言。

---

## P1-CREATE-3 其他職業文化何時升格成 hard gate

`90_srd_bridge/CHARACTER_CREATION_CLASS_CULTURE.md` 已整理 3.5 class skill / automatic feature / oath / tradition 線索。

目前確定升格的只有已有 D100／GM 支持的項目，例如：

- 施法者難度2語言；
- 牧師信仰＋領域；
- 技能／專長明文 prerequisite。

其他像：

```text
遊俠應有追蹤／生存文化
盜賊通常技能面很寬
聖騎士需要誓約／教團
德魯伊需要結社／傳承
```

目前可能是 `required RP candidate` 或 `review candidate`，不能自動全部升格 hard gate。

後續遇到實際玩家角卡案例再逐項確認。

---

## P1-CREATE-4 大量 reserve CP 的合理尺度

目前 protocol 使用：

```text
>30% remaining CP
```

作為**重新搜尋候選的 warning signal**，不是規則門檻。

尚未確定是否需要依：

- 角色 CP 總量；
- 職業／施法環數；
- campaign 成長速度；
- 玩家是否刻意存 CP；

設定更好的 heuristic。

在有更多創角樣本前，不把 30% 寫成合法性規則。
