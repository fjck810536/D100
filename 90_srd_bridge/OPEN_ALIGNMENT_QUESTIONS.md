# D100 ↔ D&D 3.5 SRD — Open Alignment Questions

> 日期：2026-09-12  
> 狀態：`[ALIGNMENT_QUESTION]`  
> 原則：**本檔只記錄對齊後真正留下的衝突／缺漏。不得因 3.5 有答案就直接修改 D100。**

參考總圖：

- `90_srd_bridge/SRD_ALIGNMENT_2026-09-12.md`
- `90_srd_bridge/conversion_rules.md`
- `99_open_questions/unresolved_rules.md`

---

## AQ-1 `法術升階`：提升的是施法者等級，還是法術環數？ `P0`

### D100 Sheet

`法術升階` 先寫：

```text
每提升1個技能等級，可以將搭配此專長的法術多追加1個施法者等級。
```

但下一句又寫：

```text
法術效果中所有與法術等級有關的變數……都以升階後的法術等級計算。
```

### 3.5 provenance

3.5 `Heighten Spell` 提高的是 **effective spell level**，不是 caster level。

### 問題

D100 現行真正意圖是哪一種？

1. 每級 `caster level +1`，但法術環數不變？
2. 每級 `spell level/ring +1`，第一句「施法者等級」是誤寫？
3. 兩者都增加？
4. 有另一種 D100 定義？

### 暫時處理

**不改原文，不用 3.5 Heighten 自動修成升環。**

---

## AQ-2 製作條文殘留的「經驗值 / XP」在 D100 代表什麼？ `P0`

### D100 Sheet

製作總則已建立：

```text
永久型魔法物品 → CP + 時間 + 金錢
每多一加值會卡自身 CP
物品永久損毀後釋放 CP
```

但部分 3.5 衍生製作專長仍寫：

```text
修復破損魔法武器／盔甲／盾牌
支付製造時一半的經驗值、材料費和時間
```

其他少數條文也仍出現「經驗值」。

### 3.5 provenance

3.5 item creation 原本確實消耗 XP；修復相關文字也使用 XP / raw material / time 經濟。

### 問題

現行 D100 的「經驗值」應理解為：

1. 未清理的舊 3.5 用語，忽略？
2. 現行應換成 CP？
3. 曾存在舊版 XP 系統，這些條目需要逐項重寫？
4. 特定物品／修復仍真的有另一種 XP 成本？

### 暫時處理

涉及這些 legacy XP 句子時，**不要自行扣 CP，也不要憑空建立 XP 資源**；先標問題。

---

## AQ-3 `專注 / Concentration` 的正式 D100 基值與觸發範圍 `P0`

### D100 evidence

`戰鬥施法` 直接引用「專注檢定」。

GM 記憶：

```text
戰鬥施法 = 實戰中的專注線
完全未購 → 空丟 -20
Lv0 → 移除 -20
LvN → 提供等級加值
```

但 31-tab mirror 沒有獨立 `專注` 基本技能。

### 3.5 provenance

3.5 Concentration 是獨立 CON 技能；Combat Casting 只在 defensive casting / grappling / pinned 等特定情境提供 bonus。

### 問題

1. D100 專注正式基值是哪個六大分類／屬性？
2. 是否仍與 CON 有機械關係，還是已完全 D100 化？
3. 受到傷害、被擒、壓制、防禦施法、移動施法各自何時檢定？
4. `咒法專注`「受到傷害不會中斷專注」證明普通傷害可打斷，那完整觸發條件是什麼？

### 暫時處理

3.5 只提供情境祖型，**不決定 D100 數學**。

---

## AQ-4 `搜集資訊` 的正式 D100 條目 `P0`

### D100 evidence

完整 mirror 沒有獨立 `搜集資訊`，但：

```text
調查員 → 搜集資訊 / 搜索 +10/Lv
地方知識 → 搜集資訊 bonus
```

GM 也認為它應該是實際存在的技能概念。

### 3.5 provenance

3.5 Gather Information：

- CHA-based
- 一般城市消息 DC10
- 特定消息 DC15–25+
- 1d4+1 小時
- 可重試，但耗時並可能引人注意
- Investigator +2
- Knowledge(local) synergy +2

來源關係高度確定。

### 問題

D100 正式版本的：

- 分類？
- 難度？
- 每級加值？
- 基本耗時？
- retry 規則？

### 暫時處理

不得直接寫成「交涉、難度1、1d4+1小時」正典。

---

## AQ-5 `迷魂曲` 的「檢定結果」比較哪個量？ `P0`

### D100 Sheet

```text
吟遊：表演 + Lv×10 檢定
目標：抗控制 - Lv×10 檢定
目標結果 >= 吟遊結果 → 迷魂失敗
```

### 3.5 provenance

3.5 Fascinate：

```text
Bard 做 Perform check
Perform check result 成為目標 Will save 的 DC
```

這非常可能是 D100 比較句的來源。

### 問題

D100 的「結果」究竟是：

1. raw d100？
2. `d100 + value` 的總值？
3. `判定值 - d100` 的成功餘裕？
4. 其他舊版接口？

以及：這只是 `迷魂曲` 的明文特例，還是有一族 Bardic Music 共用？

### 暫時處理

保留 Sheet 明文「要比較」，但不自行選比較算法。

---

## AQ-6 Generic opposed tie 是否曾預期沿用 3.5？ `P1`

### 3.5 provenance

3.5 generic opposed skill check：

```text
高結果勝
平手 → skill modifier 較高者勝
再平 → 重骰
```

### D100 reality

D100 至少有：

- 攻擊成功後才進 dodge，再比「過多少」
- `d100 + bonus` opposed total
- 獨立 saving check
- 特殊能力自己的比較接口

因此 3.5 generic tie rule 無法安全全域套用。

### 問題

需要分開確認：

1. 一般攻擊「過多少」完全相同時？
2. `d100 + bonus` 對抗總值相同時？
3. 真正同時型法術／效果對轟相同時？
4. 是否任何一類保留「modifier 高者勝，再平重骰」的祖型？

### 暫時處理

不採用 3.5 generic tie rule 作全域預設。

---

## AQ-7 Take 10 / Take 20 / generic retry 是被刻意移除，還是轉譯漏失？ `P1`

### 3.5 provenance

3.5 有完整通則：

- 多數技能可 retry
- Take 10
- Take 20
- Take 20 代表反覆嘗試並承受多次失敗、花 20 倍時間

### D100 evidence

D100 大量技能逐句改寫自 3.5，但完整 Sheet mirror 目前沒找到全域 Take 10 / Take 20。

repo 現在對調查重骰採 `[DM_DEFAULT]`：

```text
同一方法一次骰決定目前資訊上限；
新方法／工具／線索／更多合理時間才給新判定。
```

### 問題

1. Take 10 / Take 20 是作者刻意刪除嗎？
2. 還是曾存在於未保存的通則／舊卡？
3. Search/Open Lock/Escape Artist/製作等非資訊技能，是否允許靠時間反覆嘗試到成功？
4. 若允許，D100 如何處理自然 00 大失敗與失敗成本？

### 暫時處理

不導入 Take 10 / Take 20。

---

## AQ-8 `魔射手 / Arcane Archer`：名稱祖型與能力包來源不同 `P2`

### 3.5 SRD

Arcane Archer progression：

```text
Enhance Arrow
Imbue Arrow
Seeker Arrow
Phase Arrow
Hail of Arrows
Arrow of Death
```

### D100

魔射手主要為：

```text
奧法箭
創造魔法箭
奧法射擊
虛弱／爆裂／防護／穿刺／追蹤／陰影／纏繞／誤導箭...
```

### 問題

這裡目前**不是要問「哪套才對」**；D100 現有條文優先。

真正 provenance 問題是：

- D100 魔射手的 Arcane Shot option package 來自哪一版／哪份非 SRD 資料？
- 是否只是名稱借用 3.5 Prestige Class，能力包來自另一來源？

### 暫時處理

若 D100 魔射手未來遇到能力缺口，**禁止用 3.5 Arcane Archer progression 補空格**。

---

## AQ-9 非 3.5 SRD 能力包是否要進第二階段來源考古？ `P2`

本輪 3.5 SRD corpus 找不到／無法支持以下完整能力包：

- Warlock / 邪術師／契術師套件
- 德魯伊 Circle of Moon / Dreams / Shepherd 類套件
- 吟遊學院 Glamour / Swords / Whispers 類套件
- 術士 Storm / Shadow / Aberrant / Clockwork / Lunar 類套件
- 奉獻之誓式能力包
- 奈瑟瑞爾奧術師
- 咒火使者
- 魔法舞者 Spelldancer

### 問題

是否要在 3.5 SRD 對齊結束後另做：

```text
非 SRD 3.5 / 其他 D&D 版本 / 其他來源 provenance archaeology
```

這不是現行規則問題，不影響跑團；純屬來源考古。

---

# 不列為問題的已知 D100 改寫

以下雖然和 3.5 不同，但 D100 已明文，**不要再問是否應該改回 3.5**：

- `法術瞬唱`：3.5 slot +4；D100 slot +3 + 3SP，採 D100。
- D100 自然 `01 / 00` 大成功／大失敗；不採 3.5 skill natural-face 規則。
- D100 一輪 1 秒；不採 3.5 六秒輪。
- D100 使用五抗／三特殊判定；不還原 Fort/Ref/Will。
- `使用魔法裝置` 分類與卷軸門檻已由 D100 重寫；不恢復 3.5 CHA/DC。
- 製作前置、CP lock、詞綴、符文、成本折扣已是 D100 系統；不恢復 3.5 caster-level progression。
- Cleric domain / Wizard school / subclasses 若 D100 已有完整技能樹，以 D100 為準。

---

# GM 問答使用方式

未來若要集中問 GM，優先順序建議：

```text
AQ-1 法術升階
AQ-2 製作 XP 殘留
AQ-3 專注
AQ-4 搜集資訊
AQ-5 迷魂曲
AQ-6 ties
AQ-7 Take10/20/retry
```

`AQ-8 / AQ-9` 是來源考古，不必為了正常跑團優先問。
