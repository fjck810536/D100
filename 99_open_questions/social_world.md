# Social World / Alignment Open Questions

> 本檔是 `99_open_questions/` 的社會世界／角色關係設計缺口 registry。
>
> 這裡只記「已確認值得設計，但尚未決定正式機制」的問題。不得因為列在此處就自行升格成 runtime 正典。

---

## P1-SOCIAL-1 — Alignment 與實際行為之間的浮動／偏移紀錄

### 已確認需求

目前角色 state 已正式保存九宮格 Alignment，且 runtime 契約明確規定：

```text
alignment ≠ presented_persona ≠ current_affect ≠ actual_action
```

分析師可以把 Alignment 當作長期倫理／秩序座標，但不能把 Alignment 當成逐場戲的行動腳本。

尚缺的是：

> 是否需要一個可持續觀察「角色實際行為長期如何靠近、偏離、拉扯其 declared alignment」的浮動紀錄？

這個紀錄若建立，目的應是提供分析師／Player／DM 看見角色發展，而不是自動懲罰角色或強迫扮演。

### 待討論核心問題

1. **資料形狀**
   - 只記事件 evidence？
   - 分別對 `law ↔ chaos`、`good ↔ evil` 維護連續數值？
   - 使用短期／長期兩層？
   - 使用 qualitative tags，例如 `aligned / tension / exception / sustained drift`？

2. **事件權重**
   - 一次情緒失控是否應該幾乎不影響 Alignment？
   - 重複、有代價、可自由選擇的行動是否權重更高？
   - 被控制、被迫、資訊不足、角色誤信造成的行為是否應降權或不計？

3. **Persona / Affect 分離**
   - `presented_persona` 與 `current_affect` 不應直接視為 Alignment drift。
   - 一個 Chaotic Evil 角色可以長期表現溫柔、友善或守禮；分析師應能記錄「呈現」與「倫理取向」的張力，而不是用表面行為立即改標籤。

4. **誰有權改 Alignment**
   - 真人 PC：不得由分析師／DM 靜默改 Alignment；至少需要玩家確認或顯式角色發展事件。
   - 四聲部 PL+PC：由對應 Player Voice ratify / revise。
   - autonomous NPC：可由 AO / Orchestrator 依已發生角色發展更新，但應留下 provenance。

5. **分析師的輸出邊界**
   - 分析師可以回報：`alignment-consistent pattern`、`temporary tension`、`sustained drift candidate`。
   - 分析師不能因單次行為直接宣布角色已換陣營。
   - derived drift cache 必須在新行為、關係、重大秘密揭露、Player reinterpretation 後可失效／重算。

6. **是否需要衰減／歷史窗口**
   - 很久以前的一次例外是否應持續影響現在？
   - 若需要時間衰減，應由世界時間／session 數／重大章節哪一種尺度控制？

### 最低保險絲

未來無論採哪種機制，都應維持：

```text
Alignment 是角色結構資料，不是行動指令。
單一行為 ≠ 陣營改變。
表演得像善人 ≠ Good。
情緒失控 ≠ Chaotic。
服從法律 ≠ Lawful。
違法 ≠ Chaotic。
殘酷 ≠ 單獨足以證明 Evil；必須看選擇、目的、關係與反覆模式。
分析師觀察 drift ≠ 分析師有權重寫角色 Alignment。
```

### 目前暫定 runtime

在正式機制完成前：

- 只保存 declared / ratified Alignment；
- 行為保存在 behavior history / session log；
- 分析師可以做 qualitative derived observation；
- 不維護隱藏的 Alignment 點數；
- 不自動改 Alignment。

### 觸發正式設計的條件

出現以下任一壓測案例時，優先回來處理本題：

- 角色 declared Alignment 與長期行為明顯分離；
- 玩家主動問「角色是不是正在變陣營」；
- 分析師需要比較 persona 與倫理結構，但缺乏歷史尺度；
- autonomous NPC 經重大事件後出現持久價值轉向；
- 不同模塊對「這是例外還是 drift」反覆產生衝突。

---

## P1-SOCIAL-2 — 施法者、武裝人員、社會身分與組織如何嵌入世界常規／常識／潛規則

### 已確認需求

目前 runtime 已能建立：

- 個別角色能力；
- 組織與地點；
- Relationship Graph；
- Actor epistemic state；
- Alignment／persona／affect 等角色層資料。

但還缺一個更上位的 **social-position / world-common-sense layer**，用來回答：

> 一個世界裡的人看到「施法者、持械者、傭兵、神職者、貴族、商人、官員、學院成員、外地人、冒險者、罪犯嫌疑者」時，通常知道什麼、預期什麼、可以做什麼、不能明說但大家默認什麼？

這不是要做固定偏見表，而是讓世界具有可重複、可推理的社會常識與制度摩擦。

### 需要分開的層次

#### 1. Formal rule / law

例如：

- 哪些場所可以／不可以公開攜帶武器；
- 哪些法術需要許可、登記、執照或特定組織身分；
- 城門、學院、神殿、商會對武裝者／施法者的正式規定；
- 哪些組織有合法拘束、搜查、徵用、決鬥、治療、施法或持械權限。

不得把「法律存在」直接等同「人人遵守」或「執法一致」。

#### 2. Social convention / etiquette

例如：

- 進室內是否應卸武器、封劍、把法杖放桌邊；
- 在公共場合施法是否像拔刀一樣具有威嚇意味；
- 神職者、傭兵、學院法師、貴族護衛各自有哪些可辨識禮節；
- 正式場合怎麼介紹自己的組織、階級、師承、雇主。

這些可以在不同城市、階級、文化、組織之間不同。

#### 3. Common knowledge / default expectation

需要回答：

- 一般市民對施法者到底知道多少；
- 普通人能不能分辨法師、牧師、術士、魔法物品使用者；
- 看見鎧甲／武器時能推知多少職業身分；
- 哪些組織標誌、制服、徽章是「人人看得懂」，哪些只有圈內人知道；
- 哪些魔法能力屬常識，哪些是專業知識；
- PC 是否需要知識檢定，還是本來就應免費知道。

核心原則：

```text
世界常識 ≠ 玩家必須擲骰才能知道
專業知識 ≠ 人人都知道
```

#### 4. Unwritten rule / 潛規則

例如：

- 某些地區雖法律允許持械，但陌生武裝隊伍仍會被店家提高警戒；
- 某些學院表面開放，實際上沒有內部介紹就很難取得真正資源；
- 傭兵工會、商會、神殿、貴族家臣之間有哪些「大家不寫下來但都懂」的交換規則；
- 某些法術合法，但當眾使用會被視為挑釁、失禮或非常可疑；
- 某些組織可用關係避開一般程序，但不代表法律上真的有豁免。

潛規則應是世界 state / culture / institution 的產物，不是 DM 臨場為了卡玩家而捏出的隱形牆。

#### 5. Social position / role bundle

角色可能同時具有多重位置：

```text
施法者
+ 武裝人員
+ 外地人
+ 貴族出身
+ 某組織成員
+ 某宗教信徒
+ 被雇用中的護衛
```

需要決定：

- 這些身分如何疊加；
- 哪些是公開可見，哪些需自報／查證；
- 哪些提供合法權利，哪些只提供社會期待；
- 衝突時哪個身分優先；
- actor 對角色的反應應如何讀取這些位置，而不是直接從 class / alignment 推導人格。

#### 6. Organization-specific norms

組織不應只有：

```text
名稱 + faction attitude
```

還應能逐步建立：

- entry norms；
- internal hierarchy；
- visible markers；
- privileges；
- obligations；
- taboo；
- procedural expectations；
- informal shortcuts；
- outsiders commonly know；
- insiders only know。

但這些應優先作為資料／state schema，不必再新增一個人格 Agent。

### 待討論資料形狀

可能需要比較：

1. **World baseline + local overrides**
   - 世界一般常識一層；
   - 城市／文化／組織覆寫。

2. **Role tags + expectation bundle**
   - `caster`、`armed`、`clergy`、`noble`、`guild_member` 等 tag；
   - 每個 tag 連到 role-safe 的社會期待。

3. **Institution / Site policy**
   - 讓學院、城門、旅店、商會、神殿各自有 formal / informal policy。

4. **Actor-specific deviation**
   - 個別 NPC 可以不認同社會常規；
   - 但「他偏離常規」必須先有一個可比較的常規基線。

### 最低保險絲

```text
職業／能力標籤 ≠ 人格。
施法者 ≠ 自動受敬畏／恐懼。
持武器 ≠ 自動可疑／犯罪。
組織成員 ≠ 自動服從組織。
社會常規 ≠ 法律。
法律 ≠ 實際執法。
常識 ≠ 專業知識。
潛規則 ≠ DM 臨場阻止玩家的理由。
地方文化可以覆寫世界 baseline，但需留下 provenance。
NPC 反應應由其知識、利益、關係與當地常規共同產生，不由 class tag 單獨決定。
```

### 目前暫定 runtime

在正式社會常識層完成前：

- 對普通可預期的社會常識，DM 優先直接提供，不要求無意義檢定；
- 法律／組織規則若會實際限制玩家選擇，應在首次影響前 commit，而不是事後生成；
- 個別 NPC 可以有不同反應，但不得把個別反應倒寫成全社會常規；
- 若某項「人人應該知道」的常識第一次被提出，先標記其 scope（world / region / city / organization / subculture）；
- 重大潛規則若影響因果，需進 world / site / organization state，而不是只留在 DM 敘事記憶。

### 觸發正式設計的條件

出現以下任一情況時優先回來處理：

- PC 問「帶著劍進這裡正常嗎？」、「一般人看到法師會怎麼想？」；
- 不同 DM／module 對同一身分產生互相矛盾的社會反應；
- 組織／城市開始需要反覆使用同一套正式與非正式程序；
- 玩家需要判斷「這是常識、專業知識，還是秘密」；
- social position 開始影響雇用、價格、通行、執法、聲望或談判。
