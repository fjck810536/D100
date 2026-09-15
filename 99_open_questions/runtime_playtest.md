# Runtime Playtest Open Questions

> 本檔收錄實際跑團／壓測中暴露、會影響一般 runtime 一致性的規則或資料契約缺口。
>
> 只收「可泛化的問題」。單一角色尚未填完的裝備詞綴、某次 session 尚未決定的路線等，仍留在 character/session state，不要全部倒進全域 TODO。

---

## P0-RUNTIME-1 — `察言觀色 / Sense Motive` 的正式來源與判定接口

### 觸發案例

Andor Session 1 中，Elian 使用 `察言觀色 Lv2` 讀取 Grey Antler 客人的細微反應。

當時 runtime 暫用：

```text
Interaction 34 + Lv2×10 = 54
```

並以 d100=48 結算成功。

### 已知

- 角色 build 中確實存在 `察言觀色 / Sense Motive Lv2` 的概念；
- `談判專家 / Negotiator` 類能力與 Sense Motive 語義相關；
- 本次判定已作為既成 session history 保留，不回溯重骰。

### 尚缺

目前 repo code search 找不到 `察言觀色` 或 `Sense Motive` 的正式條目，因此仍需確認：

- 正式中文名稱；
- 所屬基值（Interaction？Perception？其他？）；
- 難度；
- LvN 是否標準 `+10/lv`；
- 未購時是否適用一般空丟 -20；
- 與 Bluff / Diplomacy / Negotiator 的關係；
- 是否有主動對抗或只做固定／情境難度。

### 安全處理

在找到來源前：

- 保留本 session 已結算的 54 / d100 48 為 migration-era provisional history；
- 新判定若數值會決定重大結果，優先查 raw Sheet / character evidence；
- 不把「Interaction +10/lv」宣稱為 D100 canon。

---

## P0-RUNTIME-2 — 特殊／DM 魔法物品的 activation、duration、transfer / attunement 接口

### 觸發案例

Elian 的三件特殊物品：

```text
Invisibility Cloak — 3/day
Dimension Door Ring — 3/day
Air-Walk Boots — >=3h/day
```

目前已知道能力概念與資源上限，但缺少完整 runtime interface。

### 目前實際風險

Nella 已持有 Elian 的 cloak，但：

```text
holder ≠ automatically knows how to use
```

若下一幕想啟動，會立刻遇到：

- activation action type；
- command / gesture / intent；
- 是否需要 attunement / owner permission；
- 借用者能否使用；
- duration；
- 中止條件；
- 每日次數如何扣除。

Ring 另缺：

- range；
- passengers / targets；
- activation timing。

Boots 另缺：

- 每日 3h 是否可切段；
- minimum activation duration；
- activation timing。

### 待確認

需要區分：

1. D100 是否已有一般魔法物品啟動／借用通則；
2. 還是這三件屬 DM special item，應各自建立完整 item contract；
3. 若來源只給效果未給接口，DM_DEFAULT 的最小可逆接口應長什麼樣。

### 保險絲

```text
持有 ≠ 會用
知道效果 ≠ 知道啟動方式
DM special item 可以存在 ≠ 可以不寫 runtime interface
```

---

## P1-RUNTIME-1 — 臨時暗號／非語言協作何時需要判定

### 觸發案例

Grey Antler 中 Elian 同時使用：

- 刀叉方向；
- 重複說「工作」；
- 拍 Nella 椅背；
- 把 cloak 交給 Aster；

Nella 最後理解為：注意／尾隨目標。

本次理解已是既成 world event，但不能因此建立通則：

> 任何臨時暗號都自動成功。

### 待討論

需要決定何時：

- 直接依共同情境自動理解；
- 因訊號模糊而只能取得部分意思；
- 需要某種 communication / perception / intelligence / social interface；
- 壓力、距離、遮擋、語言、事前約定是否改變難度；
- PL+PC 模式下是否應讓 Player Voice 自己先說「我有沒有讀懂」，再由 DM 判定 PC 是否具備足夠資訊。

### 保險絲

```text
玩家讀懂暗示 ≠ PC 自動讀懂
PC 很聰明 ≠ 能從不存在的訊號讀出完整指令
明確共同語境可以免骰 ≠ 所有 cryptic signal 都免骰
```

---

## P1-RUNTIME-2 — 調查失敗時的「不完整但不虛假資訊」與 partial success 邊界

### 觸發案例

Elian Search：

```text
56 vs d100 57
fail by 1
```

DM 給出：

- 日期／墨水看起來接近；
- 但不能確認同一來源或因果。

這符合現行 `DM_PROTOCOL.md`「失敗可得到不完整但非虛假資訊」的方向，但尚未定義：

- 這是普遍的 failure consequence 選項；
- near miss 才較適合；
- 哪些資訊應視為本來可直接感知、哪些屬成功才取得；
- 如何避免把失敗敘述成隱性成功；
- `OBSERVED_WEAK` 是否需要正式 Evidence Ledger confidence 欄，還是只在 notes 記弱度。

### 不應直接做

```text
建立一套「D100 差 1 = partial success」的全域規則
```

除非來源或 GM 之後明確採用。

### 目前安全處理

- 失敗不提供虛假資訊；
- 可以只確認表面可見但無法可靠解釋的痕跡；
- 是否給不完整資訊依 action / consequence / perception context 決定，不按固定 margin table 自動發放。

---

## P1-RUNTIME-3 — Save Point / Checkpoint 時的情境式 CP 發放

### 觸發案例

GM 明確補充：過去實際跑團中，DM 會在一次「存檔」／階段性 checkpoint 時，視角色當段情況分別發放一部分 CP。

Andor Session 1 Checkpoint 01 先採用保守 `[GM_PROVISIONAL]` 樣本：

```text
Elian  +3 CP
Nella  +3 CP
Aster  +2 CP
Rook   +1 CP
Mileia +1 CP
```

這一筆是已發放的實際 session reward，不因後續校準而自動撤銷。

### 尚缺

目前 repo 尚未找到固定公式，因此需要確認：

- 每次 save point 是否一定發 CP，還是 DM 視情況才發；
- reward 是否看：參與、角色扮演、風險、推進、情報、戰鬥、創意、失敗中的學習等；
- 個別 CP 差距的合理尺度；
- 一次 checkpoint 常見總量／個人上下限；
- 是否應避免把「骰得成功」本身直接等同更多 CP；
- 是否存在重大章節／任務完成的額外 reward；
- PL+PC 四聲部與真人 PC 是否用完全相同標準。

### 保險絲

```text
checkpoint CP ≠ 成功骰獎金
checkpoint CP ≠ 只有主線推進才有
一次 provisional 分配 ≠ 固定公式
已發放 CP ≠ 後續規則修正時自動回收
```

### 目前安全處理

在舊 DM 慣例尺度尚未恢復前：

- 使用小額、可解釋的個別 situational award；
- 每次留下 before / delta / after；
- 記錄發放理由作為未來校準樣本；
- 不宣稱存在全域固定數學。

---

## P1-RUNTIME-4 — PL+PC 模式下的 OOC / IC 語句分類與台詞滲漏

### 觸發案例

Andor Session 1，Elian 與 Nella 前往舊城／吟遊詩人學院途中，生成了：

> Nella：「不過你說『傳授吟遊詩人的技法』……你以前學過？還是你現在才突然想當一個？」

GM 後續指出：在四聲部 `pl_pc` 模式下，這一句存在另一個合理解讀——它可能是 **蟬作為 Player Voice 對真人 Player 的 OOC 場外詢問**，但生成器把它直接包進了 Nella 的 PC 台詞。

這不是重大世界狀態錯誤，但顯示目前：

```text
Player Voice utterance
PC utterance
OOC table talk
meta interpretation
```

之間缺少可靠的輸出分類／標示層。

### 本次事件紀錄

```yaml
event_id: OOC-AMBIG-ANDOR-001
session: D100-TEST-ANDOR-001
scene: road_to_old_city_bard_college
speaker_layer: 蟬 / Nella
classification: OOC_AMBIGUOUS
observed_problem: possible Player-Voice OOC question rendered as in-character Nella dialogue
retroactive_adjustment: none
```

目前不把這次事件強行重判成 IC 或 OOC；也不因它建立新的客觀關係、信任、親密或角色知識證據。

### 待討論

- PL+PC 生成時是否要先產生 `Player Voice` 決策／OOC，再決定是否轉成 PC 台詞；
- 何時允許 Player Voice 直接對真人玩家 OOC 說話；
- OOC 是否需要顯式標籤（例如 `蟬｜OOC`）或只在有歧義時標；
- 一句話同時含「玩家層詢問」與「PC 可自然說出口內容」時如何處理；
- OOC 事件是否應進獨立 event log，而不是 world Evidence / Relationship Graph；
- OOC 對話可否影響下一個 Player decision，但不得直接變成 PC epistemic state。

### 保險絲

```text
Player Voice 說了 ≠ PC 說了。
OOC table talk ≠ world event。
OOC 理解 ≠ PC 自動知道。
PC 自然能說出口 ≠ 必須把 Player Voice 問句轉成台詞。
OOC 事件可以被記錄，但不得因此污染 Evidence / Relationship Graph。
```

### 目前安全處理

GM 指示：**先記錄，不調整 runtime。**

因此目前：

- 保留既有場景，不做 retroactive rewrite；
- 將本次標成 `OOC_AMBIGUOUS`；
- 不從該句額外推導 Nella 的 IC 心理、關係或知識；
- 未來再次出現相同情況時先記錄案例，等樣本足夠再設計分類接口。

---

## P2-RUNTIME-1 — Coarse world time 何時升格為 exact clock

### 觸發案例

Andor Session 1 目前只有：

```text
Day 1 afternoon
```

尚未建立精確鐘點。

這在普通社交場景可接受，但一旦涉及：

- Academy / 商會營業時間；
- 巡邏班表；
- NPC 約定；
- 日落／宵禁；
- 多個獨立 world clocks；

若太晚才補 exact time，可能造成 retroactive schedule bending。

### 待討論

- 開場是否一定需要 exact time；
- 或只在第一個時間敏感事件前 commit；
- coarse → exact 時如何留下 provenance；
- 沙漏是否負責提示「現在必須升格」，但不自行選擇有利於劇情的時間。

### 建議方向（非正式規則）

```text
lazy precision, early commitment
```

類似 hidden world commitment：不需要一開始決定每分鐘，但在時間首次影響選項／結果前先鎖定。

---

## 不放進本檔的 session-specific incomplete state

以下仍是當前 session / character completion，而不是全域規則待辦本身：

- 四聲部 +3/+4/+5 起始魔法物品的具體詞綴尚未 final；
- Andor 某些 site 的街道／店面細節尚未生成；
- Miren 的具體藏身房間／箱子藏點尚未因果需要；
- Nella 尚未進行下一個 tail roll。

若這些實例暴露出可泛化的規則缺口，再升格進 `99_open_questions/`。
