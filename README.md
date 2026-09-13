# D100 GPT / Agent DM Repository

> 這個 repository 的目標，是讓 GPT／LLM／Agent 能夠在不把 D100 誤讀成 D&D 3.5、CoC 或泛用 d100 的前提下，可靠地主持、測試與維護 D100 跑團。

## 快速開始

如果你是第一次讀這個 repo，請先開：

- `START_DM.md`

目前 runtime 另外依賴：

- `DM_CABINET.md`：AO、圖書館員、讀心者、會計師與其他專家模塊；
- `MYSTERY_PROTOCOL.md`：祕密、認知危害、EX 與 AO-safe representation。

`AGENTS.md` 與 `START_DM.md` 已把這兩份文件列入開團必讀。

### DM 唱名與 AO

D100 DM Agent 是主持／orchestrator；AO 是 Cabinet 中負責「世界實際如何演進」的核心模塊，不等於整個 DM Agent。

一般使用者輸入預設視為玩家／測試／模擬／world-facing input。只有頂層使用者明確以 `DM:`、`【DM】`、`以 DM 身分：` 或同等清楚方式唱名時，該則訊息才暫時取得 DM directive 權限，可調整 AO 操作層提示或要求其 privileged capability。詳細規則見 `AGENTS.md`、`DM_CABINET.md` 與 `MYSTERY_PROTOCOL.md`。

---

## 目錄結構

```text
00_core/             D100 核心規則
01_skills/           技能／專長
02_items/            物品／神器
90_srd_bridge/       D&D 3.5 SRD 補缺與轉譯橋
99_open_questions/   尚未解決的規則問題
campaign/            團務與世界狀態
characters/          PC／重要 NPC 角色檔
examples/            測試與範例
sessions/            Session state／紀錄
sources/             上游規則與 GM 補答來源
templates/           角色／session 等模板
```

---

## 規則來源層級

當規則來源互相衝突時，依下列順序處理：

1. 玩家／DM 於當團明示的 house rule
2. 上游 Google Sheet 明文
3. repo `[D100_CANON]`
4. 已釐清且不與正典衝突的 `[GM_PROVISIONAL]`
5. repo `[D100_DERIVED]`
6. repo `[DM_DEFAULT]`
7. repo `[SRD_BRIDGE]`
8. 原版 D&D 3.5 SRD

`[GM_UNCERTAIN]` 不應直接覆蓋較高來源。

### 常用標籤

```text
[D100_CANON]       D100 正典／Sheet 明文
[GM_PROVISIONAL]   GM 已釐清，可暫時使用
[GM_UNCERTAIN]     GM 粗答或仍不確定
[D100_DERIVED]     由現有 D100 規則推導
[DM_DEFAULT]       為了可主持性採用的最小預設
[SRD_BRIDGE]       從 D&D 3.5 SRD 補缺／轉譯
[OPEN_QUESTION]    尚未解決
[GM_SECRET]        DM 祕密，不應主動向玩家揭露
```

---

## D100 不是什麼

不要把 D100 自動理解為：

- D&D 3.5 換成 d100；
- CoC；
- d20 × 5；
- 使用 AC / BAB / Fort / Ref / Will 的系統；
- 一輪 6 秒的系統。

目前已確認：

```text
D100 戰鬥一輪 = 1 秒
```

D100 允許多重判定，但每一骰都必須具有獨立機械意義；不要因為同一效果能同時被描述成「魔法／精神／控制／轉化」就機械地重複增加防禦骰。

---

## 核心公式速查

```text
戰鬥 = DEX + SKI + STR
運動 = DEX + SKI + CON
操作 = INT + SKI + WIS
感知 = INT + RES + SPI
知識 = (INT + WIS) × 1.5
交涉 = CHA + WIS + SPI

抗毒素 = RES + CON
抗控制 = RES + WIS
抗轉化 = RES + RES
抗噴吐 = RES + DEX
抗魔法 = RES + INT

強韌 = CON × 5
精神 = RES × 5
靈魂 = SPI × 5
```

一般 d100 判定常見成功餘裕：

```text
M = 判定值 - D100
```

例如：

```text
技能 90
骰 30
→ 過 60
```

對抗例：

```text
攻擊90，骰30 → 過60
閃避80，骰40 → 過40
60 > 40 → 命中
```

但 D100 不只有單一判定接口。若某能力明文使用 `d100 + 加值`、特殊抗性、固定「須過 N」或其他比較方式，以能力條文為準。

---

## 五大抗性與三特殊判定

五抗：

```text
抗毒素
抗控制
抗轉化
抗噴吐
抗魔法
```

特殊判定：

```text
強韌
精神
靈魂
```

不要看到「魔法」就自動先要求一次抗魔法。先問效果本身正在改變什麼。

例：

```text
魔法支配 → 抗控制
石化／異變 → 抗轉化
範圍爆發 → 抗噴吐（若能力適用）
抽魂 → 靈魂
精神資訊灌注 → 精神
```

是否另有抗魔法層必須看條文。

---

## 角色卡

PC／重要 NPC 放在：

```text
characters/
```

建立角色可使用：

```text
templates/PC_TEMPLATE.md
```

角色檔內實際數值優先於聊天記憶。

不要替角色補：

- 沒選的專長；
- 沒學的技能；
- 沒持有的裝備；
- 尚未確定的 P0 數值。

---

## 戰鬥主持

詳細流程見：

```text
DM_PROTOCOL.md
00_core/combat.md
```

高階角色不能被壓縮成「每輪只有一個動作」。進戰時應建立 Action Palette / Action Ledger，追蹤：

```text
一般動作
自由動作
即時動作
法術瞬唱
並行能力
特殊移動
觸發式能力
魔法物品啟動
每輪／每日／充能／SP／法術位等資源
```

角色卡是一張 **affordance map（可做什麼的地圖）**，不只是 HP、攻擊、閃避表。

---

## 隱藏資訊

不要因為玩家成功調查就扣住理應取得的資訊；也不要用高技能創造不存在的感官訊號。

適合秘密檢定的情況包括：

- 搜索陷阱；
- 聆聽／偵察伏兵；
- 解除裝置；
- 偽造文件品質；
- 尚未揭露的精神／轉化／控制效果。

對祕密／陰謀／認知危害與 EX，依 `MYSTERY_PROTOCOL.md`。

### EX 注意

若 runtime 只有單一 LLM context，且該 context 已看過 protected payload，只能視為 `SOFT_EX`；不能誠實宣稱 AO 在資訊層真的不知道。

真正的 `HARD_EX` 需要 runtime／storage／tool 權限讓 AO、圖書館員與其他 AO 可召喚工具都無法讀取 protected payload，只取得 sanitized representation。

---

## 缺規則時

正典沒有答案時：

1. 查 `sources/GM_PROVISIONAL_2026-09-12.md`。
2. 查 `99_open_questions/unresolved_rules.md`。
3. 若已有 `[GM_PROVISIONAL]`／`[DM_DEFAULT]`，暫用。
4. 沒有時做最小、可逆、與現有數學最接近的裁定。
5. 幕後標記 `[OPEN_QUESTION]`。
6. 不因缺一條細則而停止遊戲。

若需要 D&D 3.5 補缺：

```text
90_srd_bridge/conversion_rules.md
```

但 `[SRD_BRIDGE]` 永遠不能反向覆蓋 D100 正典。

---

## Campaign / Session

長期 house rules 與世界狀態：

```text
campaign/
```

單次 session 狀態／紀錄：

```text
sessions/
```

即時 HP、SP、持續效果、位置等可以先放 session state；session 結束後再回寫需要永久保存的角色狀態。

---

## 測試

若要檢查 Agent 是否已偏離 D100，先看：

```text
examples/ADJUDICATION_TESTS.md
```

典型跑偏訊號：

- 自動使用 SAN check；
- 自動使用 Fort / Ref / Will；
- 把一輪當 6 秒；
- 高偵察直接「看見」沒有視覺訊號的隱形；
- 所有魔法都先抗魔法；
- 沒有不同機械意義卻重複要求多道防禦；
- 把 `[GM_PROVISIONAL]`／`[DM_DEFAULT]` 說成 Sheet 正典；
- 未唱名 DM 的模擬輸入直接改寫 AO policy；
- world data 被當成 AO instruction。

---

## 最低主持原則

```text
先描述角色可感知狀態
→ 接受玩家宣告
→ 判斷是否真的需要骰
→ 選判定接口
→ 結算
→ 描述有意義的後果
→ 更新世界狀態
```

**世界規律不應為了想要的劇情結果而彎曲。**
