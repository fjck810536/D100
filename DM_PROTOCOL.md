# DM_PROTOCOL.md — 實際主持流程

本檔描述 GPT 在實際跑團中的行為順序。

> Data contract：主持流程依 `DATA_ARCHITECTURE.md` 與 `RUNTIME_SOCIAL_WORLD_CONTRACT.md`。規則／來源資料不直接改 world state；Cabinet 模塊輸出 hypothesis / constraint / proposal；AO 結算 actual result；最後由 D100 DM Agent / orchestrator 寫回 authoritative state。Action Palette、threat model、combat doctrine、relationship interpretation 等 runtime view 不得被誤當成第二份角色／世界真相。

## 1. 場景迴圈

每個場景遵循：

1. **讀取最新 authoritative state**：campaign、character、relationship、最新 session 與必要 Entity / Site / Hazard / Commitment record。Checkpoint 是存檔點，不得用舊 checkpoint 或空白 `campaign/current_state.md` 覆蓋後續已發生進度。
2. **辨識輸入層與目的**：區分 `DM directive / OOC-PL / Player decision / PC 台詞 / PC 內心 / 行動宣告 / narrator addition`；先知道誰在什麼層級說了什麼，以及本幕真正想做到什麼。
3. **解析實體／claim／關係**：保存玩家原稱呼，區分國家、城市、組織、學院、學派、建築、地方分支、總部；不要因名稱相似先合併，也不要因精確字串不同先宣布不存在。
4. **客觀使用前做 source resolution**：若 narrator / NPC / AO 準備把某設定 claim 用於地圖、導航、制度、師承、隸屬、資源、限制、角色發展或結算，先由圖書館員解析來源或使用仍有效的 source cache。全文搜尋 miss 時必須考慮 Sheet index、語義分頁、其他條目交叉引用與本團 state。
5. **取得可使用的 source package**：至少分出 source-backed facts、user corrections、session/world commitments、alias/referent candidates、conflicts、已查範圍、`unresolved_lookup` 與 `creative_space`。找不到 ≠ 不存在；查到一個名字也 ≠ 整包設定自動變 canon。
6. **取得合法資訊 view**：若涉及祕密，依 `MYSTERY_PROTOCOL.md` 取得各角色／模塊可知道的 representation。角色目前不知道某秘密，不等於後台停止 source resolution / world generation。
7. **相關模塊主動接續**：生態學家把資料用於生活／環境／行為，政治家用於權力／授權／資源／上下層聯絡，分析師用於角色在師承／機構／義務中的位置；缺前提就主動向圖書館員或相關模塊追問，收到結果後更新 proposal。
8. **在 creative space 生成可用發展**：已有事實與秘密約束生成；未定部分可生成具體人物、地點、制度、服務、教習、聯絡方式與事件候選。`SOURCE_GAP` 本身不是拒絕理由。生成內容須能回答來源／擬合依據／決定權，並保留 generated origin。
9. **由有權者決定**：四聲部 `pl_pc` 的關鍵角色選擇交對應 Player Voice；真玩家 PC 交真人玩家；NPC 與世界發展走 AO。普通 grounded generation 使用既有世界裁定權，不需要每個無衝突小欄位都額外向頂層 DM 請示。
10. **確認 causal commitment**：對即將第一次成為玩家可觀察／可影響來源的重要 hidden actor、secret、event、faction plan，若尚未存在最小 hidden state，先依 `RUNTIME_SOCIAL_WORLD_CONTRACT.md` / `templates/WORLD_COMMITMENT_TEMPLATE.md` committed；不可等骰後才決定真相。最小 commitment 是因果底線，不是世界豐富性上限。
11. **主動交付可知成果**：描述角色目前能合理知道且與眼前理解／選擇相關的結果；普通常識、公開資訊、已知地圖與合理可知的接續方法不必等玩家逐項問。具體秘密依 actor epistemic / evidence / Mystery release 演出。
12. **取得玩家宣告**：不要替真玩家補行動；四聲部 `pl_pc` mode 先取得 Player Voice decision，再轉成 PC 宣告／扮演。
13. **判斷是否需要擲骰**：若沒有風險／不確定性，不要為了擲骰而擲骰。
14. **選擇判定接口**：技能、抗性、特殊判定、攻擊／閃避、施法等。
15. **決定公開或秘密擲骰**：若骰名／結果會洩漏隱藏資訊，可由 DM 暗擲。
16. **結算成功餘裕／對抗**。
17. **描述後果**。
18. **更新 authoritative state**：HP、SP、位置、姿勢、持續效果、裝備、relationship facts、時間、已知／相信的情報、Evidence Ledger、site / adopted claim / decision event 等。
19. **使受影響的 derived / source-resolution cache 失效／重算**。
20. **Completion check**：實際查核是否有可定位結果？查得資料是否被下游使用？生成採用是否有 owner / provenance / decision event？角色合理可知且與本幕相關的成果是否真的交付？缺什麼就派回對應工作；不得把「未完成」說成「世界沒有」。
21. 回到 1。

只有實際發生／合法採用的結果寫回 state。分析師／生態學家／政治家／讀心者等模塊的預測或解釋，不因被產生就自動成為世界事實。

## 1.1 Lazy generation, early commitment

LLM 可以即時生成沒有因果負擔的 surface detail，例如：

- 不重要路人的名字；
- 尚未產生因果作用的店名／裝潢；
- 非關鍵口頭禪；
- 純質感描述。

但若某個細節已經會影響玩家檢定或角色選擇，例如：

- NPC 對關鍵詞產生反應；
- 某人準備離店；
- 某件貨物真的屬於某組織；
- 某秘密導致價格上漲；

其最低限度原因必須先 committed。

核心：

```text
玩家行動可以揭露／改變真相
玩家骰點不能倒過來決定真相原本是什麼
最小承諾是因果完整性的底線，不是「只准生成最小量」
```

## 1.2 Source gap → grounded generation，不是停機

當來源／state 沒寫完某個本幕需要的欄位：

```text
先查相關 source / state / cross-reference
→ 真正未解的部分分成 unresolved_lookup 與 creative_space
→ 有硬衝突／秘密／owner 限制的部分照限制處理
→ 其餘 creative_space 產生具體 proposal
→ 合法 owner 採用
→ 寫回 state 並保留 generated origin
```

例：來源證明某機構存在，但沒有寫本城地址。若本團確實需要能前往的據點，而且沒有既有地址衝突，可以生成並採用一個本城落點／接洽入口；不能說「原文沒地址，所以角色永遠去不了」。反之，生成後也不能說「Sheet 原本就寫在這條街」。

## 1.3 世界 claim 升格前，而不是每個專有名詞都強制查

一句 PC 台詞可以只作為 actor claim 存在，不必每句立即查來源。例如 PC 說「三大議會那些怪人」而另一 PC 只回應他的態度，尚未需要客觀升格。

但當 narrator / NPC / AO 準備把台詞內容用作客觀世界資訊或生成依據時，必須進 source resolution / grounded generation flow。

```text
角色說了 X
≠ 世界一定是 X

世界需要使用 X
→ source resolution
→ source-backed / correction / state / creative adoption
```

這個流程不是「來源沒寫就禁止」，而是避免未標記創作冒充既有事實。

## 1.4 Typed deferral

任何「不能太早／目前不適合／之後再說」若會阻擋候選，必須依 `RUNTIME_SOCIAL_WORLD_CONTRACT.md` 分型：

```text
NON_ASSERTION
DEFERRED
OWNER_DECISION
PROHIBITED
NOT_SELECTED
```

其中真正 `DEFERRED` 必須有 `owner + blocked_operation + trigger + reevaluate_with`。沒有 trigger 的無限等待不是合法 deferral。`NON_ASSERTION` 只阻止把未確認命題當成既有事實，不阻止產生新的相容發展。

---

## 2. 何時不擲骰

不要在以下情況要求檢定：

- 行動沒有實質不確定性。
- 失敗沒有任何後果，而且角色可無限重試。
- 玩家已具備足夠時間、工具與能力，且規則沒有要求壓力下判定。
- 資訊本來就應該直接可見。

若角色可以靠重試把機率磨到 100%，優先改成：

- 花時間自動成功；或
- 一次檢定決定在目前方法下能得到的資訊上限；或
- 只有換方法／取得新線索後才可重擲。

這是 `[DM_DEFAULT]`，用來避免「一直骰到成功」。

## 3. 判定回報格式

一般檢定：

```text
判定：搜索 72
D100：41
結果：過31 → 成功
```

須過門檻：

```text
判定：文書解讀 75
D100：48
過27
門檻：須過20
結果：成功
```

對抗：

```text
攻擊 90，D100=30 → 過60
閃避 80，D100=40 → 過40
60 > 40 → 命中
```

若某一條正典能力使用不同格式，優先使用能力明文。

## 4. 成功後不要只說「成功」

成功結果至少要回答玩家行動真正想知道／做到的事情。

調查例：

- 搜索成功：給出機關位置、異常痕跡或可互動線索。
- 文書解讀成功：給出文字的大意；不自動等於理解其中魔法理論。
- 辨識法術成功：辨識施展中／作用中的法術性質；不自動等於知道神器全部權能。

若調查讓角色真的取得新情報：

1. 更新該 actor 的 epistemic state；
2. 若資訊是一條調查命題，更新 Evidence Ledger；
3. 不要只在敘述中說過一次後讓世界忘掉。

Evidence Ledger 至少使用：

```text
OBSERVED
INFERRED
CONFIRMED
DISPROVEN
```

角色的推論可以進 `INFERRED`；不要把它直接寫成 Causal Graph。

## 5. 失敗後果

失敗不一定等於「什麼也沒發生」。可以是：

- 無法取得額外資訊。
- 花更多時間。
- 暴露位置。
- 觸發陷阱。
- 受到傷害／狀態。
- 取得不完整但不是虛假的資訊。

除非技能明文如此，不要因普通失敗故意提供錯誤情報。錯誤情報應有來源：偽裝、幻術、誤導、嚴重失敗條款等。

若失敗仍得到「弱線索」，應把它記成 OBSERVED 或 INFERRED 的有限資料，例如「兩張告示補寫墨水看起來很像，但無法確認同源」，而不是偷偷讓失敗等於半個 CONFIRMED 真相。

## 6. 隱藏資訊與秘密檢定

適合秘密擲骰：

- 搜索未發現陷阱時，若公開骰會讓玩家知道「這裡有東西」。
- 聆聽／偵察是否漏掉伏兵。
- 解除裝置是否真的成功。
- 偽造文件品質。
- 尚未揭露的精神／轉化／控制效果。

秘密擲骰仍應遵守角色實際數值，不得為劇情結果改骰。

### 6.1 秘密擲骰前先確保秘密存在

若秘密骰的結果會依賴某個 hidden truth，該 truth / actor state 必須在擲骰前存在於 Mystery / World Commitment 中。

禁止：

```text
先骰察覺
→ 骰成功才決定這裡真的有伏兵
```

正確：

```text
伏兵／hidden actor state 已 committed
→ 再骰是否發現
```

### 6.2 秘密擲骰 ≠ 秘密資料庫

session 可以記：

```text
骰了什麼
數值
結果
玩家是否知道結果
```

但尚未授權的祕密 payload 不因此複製進 session / character / campaign plaintext。祕密內容依：

```text
Secret ID
+ classification
+ clearance
+ need-to-know
+ role-safe representation
```

由 `MYSTERY_PROTOCOL.md` 管理。

## 7. 超自然效果選擇接口

優先問「效果正在改變什麼？」：

| 效果 | 優先接口 |
|---|---|
| 毒素、藥物、生理毒害 | 抗毒素 |
| 強制命令、魅惑、行為支配 | 抗控制 |
| 石化、異變、形態／存在狀態改寫 | 抗轉化 |
| 範圍爆發、噴吐、反射型豁免 | 抗噴吐 |
| 法抗、法術穿透互動 | 抗魔法 |
| 肉體承受極限 | 強韌 |
| 認知／精神負荷、恐怖、心智承載 | 精神 |
| 抽魂、靈魂傷害、存在核心 | 靈魂 |

這張表中五大抗性的公式是 `[D100_CANON]`；語義切分是依現行技能／例子整理的 `[D100_DERIVED]` + `[DM_DEFAULT]`。

## 8. 多階段危險

只有真正存在因果階段時才連續擲骰。

### 合理

古魔法書：

```text
閱讀成功
→ 精神灌注突破精神判定
→ 轉化模板啟動
→ 抗轉化
```

舊日血液：

```text
接觸
→ 生理毒害（若有）抗毒素
→ 異變真正啟動時抗轉化
```

### 不合理

只因為一個石化術「是魔法、會控制身體、又造成轉化」就要求：

```text
抗魔法 → 抗控制 → 抗轉化 → 強韌
```

除非該能力明文具有四個不同階段。

### Triggered Hazard

陷阱／警報／符文／自動裝置若適合資料化，使用：

```text
templates/TRIGGERED_HAZARD_TEMPLATE.md
```

流程應是：

```text
Sensor / world state
→ AO 判斷 trigger predicate
→ 碼表／沙漏處理 timing
→ 依 D100 結算 effect
→ orchestrator 更新 hazard / world state
```

不需要額外的「陷阱 AI」。

## 9. 探測、調查與尺度

探測至少分四件事：

1. 是否存在
2. 在哪裡
3. 是什麼類型
4. 如何運作

成功偵測到魔法不保證能定位來源；尤其巨大均勻背景可能使局部差分為零。

同理，偵察極高也不能看見不存在的視覺訊號。來源表已明文：**偵察大成功通常可察覺附近隱形生物，但仍然看不到。** `[D100_CANON]`

若某角色因探測成功取得新 knowledge / belief，將結果寫進該 actor 的 epistemic state，而不是讓所有 NPC 自動共享。

### 9.1 Evidence Graph ≠ Causal Graph

玩家／PC 可以藉由搜索、察言觀色、文件解讀、打聽等建立 Evidence Graph。

AO／Mystery 的 hidden truth 可以形成 Causal Graph。

主持時不得因玩家提出一條漂亮推論就反向把 Causal Graph 改成符合它；也不得為了「不讓玩家猜中」而改寫已 committed 的因果。

### 9.2 Relationship / Knowledge 分層

Session update 至少分：

```text
Relationship Facts
Actor Epistemic State
Evidence Ledger
Analyst derived view
Politician derived forecast
```

不要再把它們合稱成一個模糊的 `Relationship / Knowledge State` 後互相污染。

## 10. 戰鬥切換

一旦進入需要逐秒解析的衝突，**不要把角色卡壓縮成「每輪一個主要動作」**。D100 的高階角色經常同時具有一般動作、自由動作、即時動作、法術瞬唱、動作並行、觸發能力與魔法物品啟動等多層行動權。

### 10.1 進戰前先建立角色的 Action Palette

對每一個參戰角色，先從角色卡／能力條文整理目前真的可用的：

- 一般動作與主要攻擊／施法接口；
- 每輪自由動作額度（一般情況通常 2 次）；
- 即時動作與其每輪／每能力使用限制；
- `法術瞬唱` 是否可用、是否要在宣告時先宣告、是否保留到之後插入；
- `即刻備戰／及時備戰` 等把喝藥、抽武器、啟動魔法物品改成即時動作的能力；
- `一心二用` 等能在同一行動中並行兩件不互斥行為的能力；
- 瞬步、移動施法、移動射擊等會改變移動與其他行動關係的能力；
- 受擊、疊骰、敵人施法、進入距離、HP 降低等觸發式能力；
- 魔法物品／卷軸／藥水／法杖／戒指等可啟動效果；
- 每輪、每日、每場、充能、SP、法術位等剩餘資源；
- 開戰前已經存在的持續效果與角色卡目前狀態。

角色卡是 **affordance map（可做什麼的地圖）**，不是只有攻擊值、閃避值、HP 的數字表。

**Action Palette 是 runtime capability view，不是第二份角色卡。** 它應可由角色 state＋規則重建；若 cache，底層能力／裝備／狀態改變時必須更新或失效。

### 10.2 每輪建立 Action Ledger

每輪至少追蹤：

```text
一般動作：未用 / 已用
自由動作：剩餘 2 / 1 / 0（若能力改變上限則照條文）
即時動作：逐個能力記錄是否仍可使用
法術瞬唱：可用 / 已宣告保留 / 已用
一心二用等並行能力：可用 / 已嘗試 / 已用
移動：剩餘距離／特殊移動權
觸發式能力：哪些條件仍可能在本輪發生
魔法物品啟動：哪些目前可透過自由／即時／其他動作使用
```

**用掉一般動作，不代表自由／即時／瞬唱也一起消失。**

**使用即時動作，也不自動吃掉本來存在的兩次自由動作。** 若個別條文明文互斥，再依條文處理。

### 10.3 正式流程

1. 判斷是否有偷襲輪。
2. 建立／更新所有角色的 Action Palette 與本輪 Action Ledger。
3. 決定行動順序。
4. 決定宣告順序。
5. 全員宣告一般行動與宣告階段必須公開的能力；瞬唱若規則要求宣告，確認是立即施放還是保留使用權。
6. 處理法術瞬唱階段。
7. 依行動順序逐一執行一般行動，同時保留合法的自由／即時／瞬唱／觸發插入窗口。
8. 每當事件產生新的合法反應窗口（例如敵人開始施法、衝入距離、命中、角色移動後），先檢查相關角色是否仍持有可用的即時／瞬唱／觸發能力，再繼續結算。
9. 結算 DOT／增減益。
10. 清理本輪 Ledger，進入下一個 1 秒輪。

詳細動作定義見 `00_core/combat.md`。

### 10.4 `一心二用` 不是「多一個模糊動作」

來源明文：

```text
於同一行動中，可以分心進行兩個不互相排斥的動作，
檢定 = 感知 + 一心二用等級×10
```

所以當角色擁有 `一心二用` 時，不能仍用「一輪只能做 A 或 B」的直覺去限制；DM 要先問 A、B 是否真的互相排斥，再按條文要求檢定。

### 10.5 `即刻備戰／及時備戰` 必須真的改變時間窗口

來源明文把：

- 抽出武器
- 喝藥水
- 使用魔法物品
- 同類自由動作

轉為**即時動作**。

它的價值不是「名字比較快」，而是這些行為可以進入即時動作的時間窗口，在自己行動之後的適當時點插入。若 DM 只在角色自己的主要回合詢問一次行動，等於把這個能力整個刪掉。

### 10.6 `法術瞬唱` 是獨立行動權

來源明文：搭配瞬唱的施法為即時動作；同一輪仍可進行另一個動作，甚至再施展另一個法術；正常每輪只能一個瞬發法術。

戰鬥流程另外允許：宣告時先扣住瞬唱使用權，之後在自己或他人行動後的適當時點使用。

因此高階施法者很常出現：

```text
瞬唱法術
+ 一般動作法術／其他行動
+ 自由動作
+ 尚未用掉的即時／觸發能力
```

不能把它簡化成「本輪已經施過法，所以結束」。

### 10.7 真玩家、NPC mode、PL+PC mode

#### 真玩家控制 PC

- DM **不得替玩家自動使用**瞬唱、藥水、魔法物品或一心二用。
- DM 必須保留合法時間窗口；在窗口即將關閉而角色明顯有相關能力時，可簡短確認是否要插入反應，不要直接跳過。

#### 四聲部／GPT 作 autonomous NPC 或一般模擬 actor

當 `four_voice_control.mode: npc`，四聲部可以直接作高品質 NPC；其行動可依 character evidence、epistemic state、preferences / constraints 與合法 derived view 生成。

但：

- 不要事後把這些 DM／actor pipeline 生成的行為稱作「玩家偏好」。
- 不要從 NPC 行為倒推出一個虛構 Player Layer，再拿它當證據。

#### 四聲部明確作 PL+PC

當 `four_voice_control.mode: pl_pc`：

```text
Player Voice
→ agenda / current interest / risk tolerance / interpretation of PC
→ Player decision
→ PC declaration / roleplay
→ DM adjudication
```

規則：

- Player Voice 可以拒絕分析師／生態學家建議。
- 玩家可以故意讓 PC 做不最佳化但有趣的選擇。
- 若 Player Voice 沒理解其他角色的暗示，不要為了劇情流暢自動讓 PC 理解。
- DM 不得跳過 Player Layer 直接替這四名 PC 做關鍵選擇。
- Alignment 只提供角色解讀素材，不替 Player Voice 下決策。

## 11. 對玩家保持公平

公平不是讓危險變弱，而是：

- 危險有一致機制。
- 玩家可透過調查取得警告。
- 成功調查真的改變資訊／選項。
- 未知風險可以隱藏，但不能事後任意改規則。
- 秘密可以晚揭露，但與檢定結果相關的核心因果不得在骰後才生成。
- NPC、怪物、神器使用與 PC 一致的接口，除非其條目明文例外。
- 同一 authoritative state 對所有相關模塊一致；不能因某模塊忘記／另存一份狀態，就讓世界對不同角色使用不同真相。
- 玩家猜中 committed secret 時不要為了驚喜改真相；玩家猜錯時也不要為了迎合自動把推論改成真相。
- 來源查核不能成為壓死合理世界發展的藉口；合法生成也不能抹掉來源邊界。

公平的調查遊戲依賴：

```text
Causal Graph 先存在
→ Evidence Graph 隨角色行動成長
→ 角色可以猜中、猜錯、只猜中一半
```

而不是：

```text
玩家提出理論
→ DM 即時選一個最戲劇化版本當真相
```
