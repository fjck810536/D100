# D100 ↔ D&D 3.5 SRD — Open Alignment Questions

> 日期：2026-09-12  
> 狀態：`[ALIGNMENT_QUESTION]`  
> 原則：**只保留仍會影響 D100 實際裁定、且尚未被 Sheet／Actual Play／GM 補答解掉的問題。不得因 3.5 有答案就自動修改 D100。**

參考：

- `90_srd_bridge/SRD_ALIGNMENT_2026-09-12.md`
- `90_srd_bridge/conversion_rules.md`
- `sources/GM_CLARIFICATIONS_2026-09-12_ROUND2.md`
- `99_open_questions/unresolved_rules.md`

---

# 目前狀態

第二輪 GM 補答後，原本由 3.5 對齊產生的主要缺口已大幅收束。

## 已關閉：製作專長 legacy XP

GM 明確回答：

> 「是卡 CP，最早是消耗 CP。」

因此：

- 製作專長中的「經驗值」是 3.5 legacy wording；
- D100 現行資源是 CP；
- 永久物品採卡 CP／損毀後解放 CP 的現行模型；
- 不建立 D100 XP 資源，也不搬 3.5 XP 公式。

詳見 `sources/GM_CLARIFICATIONS_2026-09-12_ROUND2.md`。

## 已關閉：專注使用哪個 D100 技能

GM 明確回答：

```text
沒有戰鬥施法 → 空丟「戰鬥」-20
戰鬥施法 Lv0 → 戰鬥基礎值
戰鬥施法 LvN → 戰鬥 + Lv×10
```

且 3.5 `Concentration` 可用來判斷哪些干擾情境需要檢定；凡對執行施法造成實際影響者都可能觸發。

`移動施法` 只決定「不影響施法時可移動的最大距離」，不是另一個專注技能。

因此不再問「專注是哪個基本技能」。若未來有洞，只問具體場景／具體門檻。

## 已關閉：`搜集資訊` 是否可由 3.5 補回

GM 回答：**可以。**

因此以 3.5 `Gather Information` 作 reconstruction source，D100 化後使用：

```text
搜集資訊（交涉，難度1）
一般消息：須過10
特定傳聞／物件／地圖：通常須過15～25+
典型耗時：1d4+1 小時
可重試，但每次都耗時，反覆追查可能引起注意
```

D100 原有：

```text
調查員 → 搜集資訊 +10/Lv
地方知識 Lv2+ → 搜集資訊 +10
```

此條目標記為 `[SRD_BRIDGE + GM_PROVISIONAL]`，不要偽稱目前 Google Sheet 中仍存在獨立原始列。

---

# 法術升階：目前採操作性解讀，不再作為阻塞問題

D100 已明確定義：

```text
總施法者等級 = 本身環數×3 + 技能／專長／裝備變動
```

`法術升階` 第一個明文效果：

```text
每技能等級 → 本次搭配法術的施法者等級 +1
```

目前操作性解讀：

```text
本次法術的有效施法者等級
= 原施法者等級 + 法術升階等級
```

凡該法術效果本來吃施法者等級的部分，都用升階後的有效施法者等級計算。

第二句沿用了 3.5 `Heighten Spell` 很相似的「法術等級」措辭，但在沒有實際衝突案例前，**不因這個 legacy wording 再開一個阻塞問題，也不額外把法術環數提高。**

若未來出現明確只吃「法術環數」而不吃「施法者等級」的 D100 效果，再針對那個具體案例向 GM 確認。

---

# 已撤回：不再列為 alignment question

以下只保留 provenance 價值，不再拿去問 GM：

- `迷魂曲` 的 3.5 `Fascinate` 來源；
- 3.5 generic opposed tie rule；
- Take 10 / Take 20；
- 魔射手 / Arcane Archer 同名問題（GM 已確認 D100 魔射手為原創）；
- Warlock／德魯伊結社／吟遊學院等非 SRD 能力包的外部來源考古。

原則：

```text
3.5 有某條規則 ≠ D100 必須保留
D100 沒有某條 3.5 規則 ≠ D100 規則有缺洞
名稱相似 ≠ 機械同源
```

---

# 後續

目前不需要再集中向 GM 詢問「3.5 對齊」本身。

下一階段應把已確認的規則與來源，轉化成 **DM-facing handbook / cognition layer**：教 GPT 遇到情境時如何思考、何時檢索、何時裁定，而不是繼續擴張 provenance 問題表。
