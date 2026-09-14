# CHARACTER_CREATION_PROTOCOL.md — 創角／驗卡流程

本檔描述 D100 DM Agent 在「自動創角、協助玩家創角、驗收玩家角卡」時的調度流程。

它不是另一份規則資料庫，也不是新的 Cabinet 人格模塊。

核心原則：

```text
規則／來源由資料層與圖書館員提供
背景生活痕跡由生態學家提出 competence-domain proposal
CP / 前置 / 獎勵骰由無人格 Build Ledger 計算
稀有／世界尺度例外才交 AO 做 plausibility review
秘密背景走 Mystery
最後由 orchestrator 寫入角色 state
```

不得讓 Character Builder 自己發明 D100 規則，也不得把推薦 build 寫成角色「真正人格」。

---

## 0. 何時啟用

遇到以下任一任務時，先讀本檔：

- 自動生成 PC / NPC 玩家式角色卡；
- 協助玩家配點；
- 驗收玩家繳交角卡；
- 重新分配／重建創角 build；
- 檢查起始 CP、語言、施法資格、HP/SP 獎勵、起始裝備是否合法。

創角未完成前，不進入正式場景 runtime；已開始的場景若發現創角基礎錯誤，先凍結 scene state，修完角色卡再恢復。

---

# 1. 模塊與 service 分工

## 圖書館員 — Source Resolver + Candidate Enumerator

創角模式下，圖書館員除了回答「這能力是否合法」，還必須：

1. 從相關 D100 Sheet / normalized index **廣泛列出候選技能／專長**，不能只驗證 Builder 已想到的名字；
2. 對每個候選回傳：
   - 來源；
   - 難度；
   - 當前／目標等級；
   - prerequisite；
   - marginal CP cost；
   - rarity/review flag；
3. 若 3.5 class-related language / class skill / automatic feature 暗示 D100 可能漏掉職業文化資訊，另列 `source_gap_candidate`；
4. 不得把 3.5 class skill 直接升格成 D100 必修。

保險絲：

```text
Lv1–3 不因等級本身降權。
難度1–2 不因「怕太強」自行省略。
Lv4+ / 難度3+ 要回傳並標記 review，不是藏起來。
找不到 ≠ 不存在；找到 ≠ 同層級有效。
```

## 生態學家 — Lived-experience competence proposal

創角模式下，生態學家可根據：

- 年齡；
- 成長環境；
- 家庭／階級；
- 教育；
- 工作；
- 長期旅行方式；
- 組織／教會／學院／軍旅經歷；

提出「這種人生通常會留下哪些能力領域」的可撤回 proposal。

例如：

```text
多年商隊護衛
→ 長途耐力、夜間警戒、道路生存、貨物處理、馬匹、旅店／商路接觸
```

生態學家**不指定技能等級、不計 CP、不直接宣告角色一定會這些能力**；由圖書館員把 competence domain 映射回 D100 候選技能。

## AO — Rare / world plausibility gate

AO 不參與普通 Lv1–3 / 難度1–2 build optimization。

只有出現下列 review flag 時才需要 AO：

- Lv4+；
- 難度3+；
- 三環以上施法者，尤其四環+；
- 年齡／訓練／師承與能力尺度不相稱；
- 稀有種族、組織、特殊世界資源；
- 其他必須回答「這個 proposed character state 在世界中怎麼成立？」的情況。

AO 的輸出是 plausibility constraint / required premise，不是「替玩家選 build」。

## 詭祕 — Secret background gate

秘密血統、秘密師承、隱藏身分、認知危害等依 `MYSTERY_PROTOCOL.md`。

Builder / character state 不建立 plaintext 平行秘密庫。

## 讀心者

只在玩家意圖真的不明時，提出可撤回假說；不得把「玩家可能想走某 build」直接改成角色能力。

## 分析師

不是一般創角推薦的預設模塊。只有當角色概念本身需要身份／關係結構分析時才喚起；不拿 S/I/R 去代替普通生活技能推導。

## 會計師

會計師只接世界內物件的 holder / origin / charges / unrealized value。

**CP 不是世界內財產，不交給會計師。**

起始魔法物品 build 完成後，再把正式持有物交會計師／character state。

## Build Ledger — 無人格 deterministic service

只維護創角 meta accounting：

```text
base_starting_cp
attribute_adjustment_sum
adjusted_starting_cp
bonus_cp
spent_cp
reserved_cp
skill_costs
next_level_costs
qualifying_melee_cp
qualifying_spell_cp
reward_hp_sp_dice
hp_sp_purchase_cost
prerequisite_status
review_flags
```

Build Ledger 不提供角色人格、不決定世界結果、不猜玩家意圖。

---

# 2. 創角八階段

## Pass 1 — 起始配置與概念

取得／確認：

- 起始 CP；
- 起始魔法物品／金錢／補給；
- 種族；
- 名字／概念／背景；
- 是否施法者／職業方向；
- GM／玩家明示 house rule。

若自動創角且沒有另外指定，依目前 GM 補答優先使用：

```text
200 base CP
+3 / +4 / +5 三件起始魔法物品
```

這只是自動模板；玩家／DM 明示覆蓋。

## Pass 2 — 屬性與 derived values

依 `00_core/character_creation.md`：

1. 取得九大屬性；
2. 算 adjustment；
3. 算 adjustment sum 與起始 CP 修正；
4. 算六大技能基礎、五抗、三特殊判定；
5. 記入 Build Ledger。

不要用 D&D 3.5 base attack / save 代替。

## Pass 3 — Hard legality

先滿足「不具備就不能完成角色」的條件：

- CP 不超支；
- prerequisite graph；
- 種族成本／贈與；
- 免費通用語 Lv3；
- 施法者至少一門難度2語言 Lv1；
- 施法核心技能與目前**可用環數**；
- 所有硬性能力前置；
- 其他 D100 明文門檻。

施法核心允許非同步預購；可用環數取所有必要核心技能的最低等級。

## Pass 4 — Core identity build

建立角色主要玩法，但不要在「能玩」時就停止。

至少回答：

```text
這個角色最常用什麼接口？
主要如何攻擊／施法／支援／調查？
最重要的 2–4 個招牌能力是什麼？
```

法師在此提供：

```text
通才 / 學派方向推薦
```

學派是推薦選項，不是自動必修；正式購買仍驗證其難度與前置。

牧師在此不得只留機械 build，還要進 Pass 7 驗證信仰／領域資料。

## Pass 5 — Life-history enrichment

把背景交給生態學家，取得 competence domains，再由圖書館員映射成 D100 技能候選。

至少檢查六個面向：

```text
戰鬥
生存
工作／專業
社交
知識
興趣／人格表現
```

不是每一面都要強，但自動角色若只剩職業核心，必須再掃一次。

背景不是裝飾文字；應真正影響候選池。

## Pass 6 — Broad candidate + marginal CP search

圖書館員廣泛列出所有高相關合法候選，而不是只看已購技能。

Builder 對每項至少評估：

```text
相關度
當前等級
升下一級 marginal CP
前置成本
難度／稀有旗標
對玩法／背景的新增價值
```

重點：

```text
Lv3 是正常熟練級，不應因 Lv4+ 稀有而連帶壓低。
```

### 反事實 pass

準備停止消費 CP 前，至少問一次：

```text
如果現在必須再花 50 CP，最自然會買什麼？
如果必須再花 100 CP，還有哪些自然候選？
```

若答案仍能快速列出大量高相關、低稀有度、合法能力，表示前一輪 build 停得太早。

`剩餘 CP > 30%` 只是一個觸發反事實搜尋的 warning signal，**不是非法門檻，也不是要求必須花到 70%**。

## Pass 7 — Required RP fields + review flags

把創角輸出分四類：

### A. 自動創角時必填

系統可客觀驗證的硬資料，例如：

- 起始配置；
- 種族／屬性／derived values；
- 語言硬門檻；
- prerequisite；
- usable spell circle；
- CP；
- reward HP/SP。

### B. 玩家繳交角卡時必填

系統不能代選，但角色身分要求明示，例如：

- 牧師神祇／信仰與領域；
- 誓約／教團／結社／傳承；
- 三環以上施法者的教育、師承、年齡／時間背景。

### C. 玩家繳交角卡時存疑

不直接退件，產生 review flag：

- Lv4+；
- 難度3+；
- 高環／稀有世界能力；
- 申報背景與能力輪廓明顯不相稱。

存疑 ≠ 禁止。

### D. 自動創角自由 build

正常自由配置：

- 難度1–2、Lv1–3；
- HP/SP；
- 額外語言；
- 生活／工作／社交／知識能力；
- 下一環部分核心技能預購；
- 法師學派方向推薦；
- 保留 CP。

## Pass 8 — Reward / resources / finalize

順序固定：

```text
技能／專長 build 定稿
→ 統計 qualifying melee/spell CP
→ 擲 reward HP/SP
→ 計算 base HP/SP
→ 額外 CP 購買 HP/SP（若有）
→ 配置起始魔法物品／法術／資源
→ final validation
→ orchestrator 寫入 character state
```

若後續大幅修改 qualifying investment，舊 reward roll 不得無條件沿用；依規則補差額／重建對應 ledger。

目前 qualifying melee/spell CP 的精確技能分類仍是 open question；不確定時不得把總技能 CP 全部塞進 qualifying pool。

---

# 3. 自動角色的停止條件

Character Builder 不應以：

```text
核心技能已買齊
CP 還能存
```

作為停止理由。

可以停止的條件是：

1. Hard legality 完成；
2. 六面向與背景候選已掃描；
3. 高相關、低稀有度候選已被實際評估；
4. 50/100 CP 反事實 pass 不再出現大量明顯優選；
5. 剩餘 CP 若很多，是**有意識保留**，而不是沒搜尋。

自動角色可以大量存 CP，但 Builder 應留下簡短 `reserve_plan`，例如：

```text
準備三環後投資學派專精
準備學某難度3能力，等待 RP 前提成立
保留作冒險中重骰／臨時學習
```

玩家本人則可以單純選擇存 CP；系統不替玩家規定長期 build。

---

# 4. 3.5 缺漏偵測的使用方式

若 D100 自由 CP 化後疑似遺失職業文化資訊，圖書館員可以查：

```text
90_srd_bridge/CHARACTER_CREATION_CLASS_CULTURE.md
```

使用方式：

```text
3.5 evidence
→ source_gap_candidate
→ 對照 D100 Sheet / GM clarification
→ 才決定是 hard gate / required RP / review / optional recommendation
```

禁止：

```text
3.5 class skill
→ 直接變 D100 必修技能
```

---

# 5. 輸出格式

創角完成時至少回報：

```text
Base CP / attribute-adjusted CP / bonus CP
Spent / reserved CP
九屬性 + adjustment
六大基礎 / 五抗 / 三特殊
語言與來源
技能／專長 + 難度 + 等級 + CP
prerequisite status
施法核心與 usable circle（若有）
Required RP fields
Review flags
qualifying melee/spell CP
reward HP/SP rolls
base / final HP/SP
起始魔法物品／資源
reserve plan（自動角色大量存 CP 時）
```

若某欄屬 open question，要保留 provenance / uncertainty，不要用「看起來合理」補成正典。
