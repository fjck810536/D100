# D100 Character Evidence / Actual Play Archaeology

> 本檔是角色卡逆向工程的證據層，不是 Google Sheet 正典的替代品。
>
> 角色卡可以揭露「規則實際怎麼被模板與玩家使用」，也會保留舊版本、個案 house rule、劇情改造、模板 bug。除非另有 Sheet / Patch / GM 明確支持，不能把單一卡片上的公式直接升格成 `[D100_CANON]`。

## 0. 證據標籤

- `[CHARACTER_EVIDENCE]`：一張或多張角色卡直接可觀察到的數值、公式、欄位或使用方式。
- `[PLAY_CONVENTION]`：在多張獨立角色卡、跨角色或跨版本中反覆出現，且未與現行 Sheet / Patch 衝突的實戰慣例。
- `[HISTORICAL_RULE_EVIDENCE]`：舊團／舊版角色卡揭露當時的規則實作；用來研究版本演化，不自動覆蓋現行規則。
- `[LEGACY_TEMPLATE_BEHAVIOR]`：較可能屬舊模板、copy-paste、舊公式或歷史殘留的欄位／文字。
- `[CHARACTER_FINAL_CANON]`：GM 明確指定某角色卡是該角色結局後的最終、恆定狀態。這個標籤只對該角色成立，不是全域規則。
- `[NPC_WORLD_CANON]`：舊 PC 已成為當前世界中的背景 NPC；其結局後身分、關係、職位、持有物與已發生事件仍屬世界狀態。

### 使用優先序

規則問題：

```text
現行 Sheet / Patch
> 已整理的 D100_CANON
> 已釐清 GM_PROVISIONAL
> PLAY_CONVENTION
> 單卡 CHARACTER_EVIDENCE
> HISTORICAL_RULE_EVIDENCE / LEGACY_TEMPLATE_BEHAVIOR
```

角色／世界狀態問題：

```text
當團 GM 明示
> CHARACTER_FINAL_CANON / NPC_WORLD_CANON
> 角色卡其他歷史快照
```

**不要用新版規則自動重算、覆寫 `[CHARACTER_FINAL_CANON]`。** 如果一張 END 卡和 2026 規則公式不同，先把差異視為版本差異，而不是把角色的既定最終狀態洗掉。

---

## 1. 目前樣本

### 現行／近現行角色卡

1. **莎緹拉** — Google Sheet 角色卡
   - source: `https://docs.google.com/spreadsheets/d/190tSepkLnQFWwBV1PkBOkn0ri0ILSUNBWn1mAbLpoCQ/htmlview`
2. **亞黛兒** — D100 v1.3
   - source: `https://docs.google.com/spreadsheets/d/1bJ6_bIRoOCI0UUsV4AlHi9YLpWrvXb_0t1nVU0HBHQw/htmlview`
3. **卡蘭德** — D100 v1.3
   - source: `https://docs.google.com/spreadsheets/d/14dLjE8hoWg9RForhFzvc6H71WTvYC88O7nr8_SX4EaE/htmlview`

### 上一團／舊版角色卡

4. **約翰** — v1.2 舊團角色卡 `[HISTORICAL_RULE_EVIDENCE] [NPC_WORLD_CANON]`
5. **喀爾烏斯** — `END / 恆定角色卡` `[HISTORICAL_RULE_EVIDENCE] [CHARACTER_FINAL_CANON] [NPC_WORLD_CANON]`

GM 已明確說明：上一團的角色在結局後成為重要背景 NPC；其中**喀爾烏斯的 END 卡是角色最終、恆定形態**。

---

# 2. 已高度穩定的 operational rules

## 2.1 屬性 adjustment 的延伸公式 `[PLAY_CONVENTION]`

多張 v1.2 / v1.3 / END 卡使用同一公式：

```text
adjustment = ROUND((current raw stat - 13) / 2)
```

`current raw stat` 可包含基礎值、裝備與臨時屬性變動；adjustment 會依當前 raw stat 重算。

例：

```text
DEX 30 → (30 - 13) / 2 = 8.5 → 9
CON 32 → (32 - 13) / 2 = 9.5 → 10
CHA 34 → (34 - 13) / 2 = 10.5 → 11
```

此證據補足了創角表只列到較低屬性區間的問題。

## 2.2 六大複合技能使用「raw stat + adjustment」後的總屬性 `[PLAY_CONVENTION]`

角色卡實作反覆顯示：

```text
戰鬥 = STR總值 + DEX總值 + SKI總值
運動 = DEX總值 + SKI總值 + CON總值
操作 = INT總值 + SKI總值 + WIS總值
感知 = INT總值 + RES總值 + SPI總值
知識 = (INT總值 + WIS總值) × 1.5
交涉 = CHA總值 + WIS總值 + SPI總值
```

其中 `屬性總值 = current raw stat + adjustment`。

## 2.3 五抗也使用 adjustment 後的屬性總值 `[PLAY_CONVENTION]`

多張角色卡公式顯示五抗不是只拿 raw stat 相加，而是使用已含 adjustment 的屬性總值，再加技能／物品／臨時修正。

因此像：

```text
抗毒素 = RES總值 + CON總值 + 其他修正
```

與角色卡實際數值一致。

## 2.4 強韌／精神／靈魂不把 adjustment 再乘一次 `[PLAY_CONVENTION]`

角色卡實作顯示核心骨架為：

```text
強韌 = current raw CON × 5 + 額外特殊修正
精神 = current raw RES × 5 + 額外特殊修正
靈魂 = current raw SPI × 5 + 額外特殊修正
```

這裡的 `current raw` 可以包含基礎／裝備／臨時屬性變動，但**不把由屬性導出的 adjustment 再算進去**。

例如角色 raw CON 22、adjustment +5、另有特殊 +10：

```text
強韌 = 22 × 5 + 10 = 120
```

不是 `(22 + 5) × 5`。

## 2.5 Lv0 是真實的「已購技能」狀態 `[D100_CANON support + PLAY_CONVENTION]`

亞黛兒、卡蘭德以及舊團角色卡都存在明確 `Lv0` 技能；空白與 `0` 不是同一狀態。

角色卡 CP 公式反覆顯示：

```text
Lv0 cost = difficulty × 2^0 = difficulty
Lv1 cost = difficulty × 2
```

因此 Lv0 正好是 Lv1 的一半，並和 Sheet 的技能 CP 公式相互支持。

推薦資料結構仍為：

```yaml
skill:
  acquired: false
  level: 0
```

- `acquired: false` → 未購／空丟，通常有 -20
- `acquired: true, level: 0` → 已購 Lv0，移除空丟 -20，但沒有等級加值
- `acquired: true, level: n` → 正常 LvN

## 2.6 知識基值的 ×1.5 使用 ROUNDDOWN `[PLAY_CONVENTION]`

多張新舊角色卡模板明確使用：

```text
ROUNDDOWN((INT總值 + WIS總值) × 1.5)
```

因此 `.5` 在**知識基值建立這一步**是向下取整。

注意：這只回答「知識基值」的 operational implementation；**不能因此外推所有傷害、施法、攻擊公式的小數都一律 ROUNDDOWN**。全域小數時點仍看 Patch note 與未決規則。

## 2.7 法師施法實作 `[CHARACTER_EVIDENCE → PLAY_CONVENTION]`

卡蘭德等角色卡與 Sheet 公式吻合：

```text
一般法師施法者等級 = 自身環數 × 3
法師法術位 = 環數 × 2 + INT adjustment + 其他修正
施法判定基值 = 感知 + 10 × (施法者等級 / 3) + 其他修正
```

法師學派專精的實際卡片也反覆出現：

```text
該學派施法者等級 += 專精Lv × 3
```

例如一般施法者等級 15、變化專精 Lv4：

```text
15 + 4×3 = 27
```

這與 Sheet「學派專精每級 +3 該學派施法者等級」一致。

## 2.8 多施法體系與共用法術位確實有 Actual Play 實作 `[CHARACTER_EVIDENCE]`

亞黛兒角色卡同時實際維護多個施法體系，並存在 `法術格共通`、基本法術位、共用位、已轉／可轉等欄位。

這證明多施法職不是只有 Sheet 上的理論設計；實戰角色卡會追蹤各體系與共用法術位。

但單一角色卡不能解決所有施法主屬性／共用位轉換細節，仍需能力條文與其他角色交叉驗證。

---

# 3. 疊骰（doubles）是可被系統監聽的骰面事件

## `[PLAY_CONVENTION]`

多張彼此不同的角色卡、特殊技能、劇情能力與物品都存在：

```text
若 D100 出現疊骰 → 觸發該能力自己的效果
```

因此可以安全推定：

```text
roll
→ 判斷是否為疊骰（11 / 22 / 33 ...）
→ 若目前有技能／物品／劇情規則監聽疊骰
→ 觸發該條文自己的效果
```

**不能外推成：**

```text
疊骰 = 全域大成功
疊骰 = 全域大失敗
疊骰 = 固定數值 bonus
```

疊骰是一級「骰面事件／hook」，而不是已知的全域 success tier。

---

# 4. 移動規則：角色卡證明有版本／模板差異，不能硬寫單一 base

## `[CHARACTER_EVIDENCE + HISTORICAL_RULE_EVIDENCE]`

目前觀察到：

```text
約翰 v1.2：移動 ≈ DEX adjustment
喀爾烏斯 END：移動 = max(DEX adjustment, 1)
亞黛兒 v1.3：移動 = max(DEX adjustment, 1) + 1 + 其他移動修正
卡蘭德 v1.3：移動 = max(DEX adjustment, 1) + 2 + 瞬步／其他移動修正
```

因此目前**不能**把 `+1`、`+2` 或 D&D 30 ft 寫成全域 base movement。

角色卡已回答的是：

1. 實際遊玩確實把移動速度獨立記在卡上；
2. 移動值的模板公式歷史上有變化；
3. 不同角色／模板可能含不同的固定項或來源；
4. 當角色卡已有明確移動值時，應優先使用角色卡的實際值。

仍需要回答：

- v1.3 的 `+1` / `+2` 各自來源是種族、角色、模板版本、特殊規則還是 bug？
- 現行通用角色是否有正式 base movement 欄位／公式？
- `戰鬥流程` 的 `(DEX調整值 + 技能 + 物品) × 5ft` 與角色卡完整移動值如何精確對接？

---

# 5. 歷史角色卡與世界 Canon 的分離

## 5.1 舊版角色卡公式 `[HISTORICAL_RULE_EVIDENCE]`

約翰、喀爾烏斯等上一團角色卡可以用來回答：

- 哪些規則骨架跨版本長期穩定；
- 哪些欄位／公式後來改版；
- 舊版 3.5 遺留用語實際如何被玩家卡片使用；
- 某些現行 Sheet 沒完整說明的機制是否曾存在 actual play 實作。

但它們**不自動覆蓋**較新的 Sheet / Patch。

## 5.2 喀爾烏斯 END `[CHARACTER_FINAL_CANON]`

GM 明確指定喀爾烏斯 END 卡為角色的最終、恆定形態。

因此：

- 卡上的最終 HP / SP（或奧能）、能力值、技能、裝備、特殊身分等，不因 2026 規則公式不同而自動重算；
- 若新團在世界中遇見喀爾烏斯，原則上以 END 卡作為該 NPC 的機械狀態來源，除非 GM 明示後續世界事件改變了他；
- END 卡的**角色狀態**是 `[CHARACTER_FINAL_CANON]`，但其中的**舊版通用公式**仍只是 `[HISTORICAL_RULE_EVIDENCE]`。

## 5.3 舊 PC 成為背景 NPC `[NPC_WORLD_CANON]`

上一團結局後的重要 PC 已成為新團世界的背景 NPC。未來若建立 NPC 資料檔，應優先保留：

- 結局後身分／職位
- 已發生事件
- 關係與組織連結
- 持有的重要資源／物品
- GM 指定的最終卡狀態

而不是把它們只當「舊 build 範例」。

---

# 6. 已觀察到的模板／版本殘留風險

## 6.1 說明文字不一定等於實際公式 `[LEGACY_TEMPLATE_BEHAVIOR]`

至少一張角色卡出現：

- 手打說明文字寫一種施法主屬性；
- 實際法術位數值卻精確吻合另一條現行 Sheet 公式。

因此做角色卡考古時，證據權重建議：

```text
實際試算表公式
> 與公式一致的實際數值
> 手打說明文字
```

若三者衝突，不要偷偷選一個；標記版本殘留或模板 bug。

## 6.2 角色卡中的劇情改造不能回推成創角通則

高階角色可能含：

- 劇情取得技能
- 特殊種族／血脈變化
- 神器／傳奇技能
- 外神／神祇／席次機制
- campaign 專屬 buff / curse

這些內容對該角色可以是真實 canon，但不能因為出現在角色卡，就回推所有新角色都能以同樣方式取得。

---

# 7. 對 repo 的直接操作規則

在新增 `[OPEN_QUESTION]` 或向 GM 追問前：

1. 先搜尋 `sources/sheet_mirror/`；
2. 再看本檔 `sources/CHARACTER_EVIDENCE.md`；
3. 若是舊 PC / NPC 自身狀態，再找該角色的 final / historical card evidence；
4. 仍無答案，再進 `99_open_questions/unresolved_rules.md` 或 3.5 SRD 對齊。

角色卡 evidence 的用途是**縮小問題**，不是把每個角色卡個案寫成全域 D100 正典。
