# Social / Cognitive Framework Sampling — Open Questions

> 狀態：P1，待研究／待取樣。
>
> 本檔記錄 2026-09-18 對外部 social / cognition / memory framework 的目前態度，以及它們與 D100 既有 Cabinet / state layer 的可能連接點。
>
> **不是採用清單，也不是 runtime 正典。** 目前原則是先偷資料形狀、判定接口與轉換思想；除非後續壓測證明必要，不直接把整套 framework 或新人格 Agent 搬進 D100。
>
> Related：[`social_world.md`](./social_world.md)、[`../DM_CABINET.md`](../DM_CABINET.md)、[`../RUNTIME_SOCIAL_WORLD_CONTRACT.md`](../RUNTIME_SOCIAL_WORLD_CONTRACT.md)、[`../DATA_ARCHITECTURE.md`](../DATA_ARCHITECTURE.md)。

---

## 核心前提

目前要解的不是「替角色建立一個固定好感度系統」，而是：

- 關係可以隨已發生事件改變；
- 暫時情緒、主觀理解、關係尺度與 authoritative relationship fact 不應混成同一層；
- derived interpretation / forecast 不得直接覆寫 authoritative state；
- 若 D100 或 D&D 3.5 已有可用尺度／condition／判定接口，優先查清楚並重用，不先另造一套平行數值系統。

因此任何外部框架都先視為「設計參考／可拆零件」，不是 dependency。

---

## 1. Emotion Engine

### 目前態度

**不採用。**

若 D100 / D&D 3.5 已有足以支撐規則判定的情緒、恐懼、態度或相近 condition，優先沿用現有規則；只有規則真的需要、而現有規則沒有時，才偷少量 **暫態情緒量（temporary affect）**。

LLM 本身可以黑箱生成大部分細膩情緒文本，不需要另外維護一整套 PAD / emotion state 才能扮演角色。

### 只可能偷的部分

```text
規則需要的暫態情緒量
→ 作為判定條件／修正值／觸發條件
→ 不升格為人格或關係真相
```

例如未來若確有必要，可只保存「警戒、恐懼、動搖、壓力」這類會碰到規則的 temporary state；其餘情緒仍由 runtime context 生成。

### 與現有模塊的連結

- **AO / Orchestrator**：只有已發生事件與合法結算能讓 temporary state 寫回需要持續的 state。
- **分析師**：可讀 temporary affect 作為材料，但不得把一次情緒反應直接解釋成永久人格／關係。
- **政治家**：只有當暫態狀態會改變威脅、談判、逃跑、服從等行動條件時才需要讀取。
- **圖書館員**：正式設計前先查 D100 與 3.5 是否已有對應規則，不重造現有尺度。

### 待查

由圖書館員優先反查：

- D100 現有恐懼／士氣／態度／情緒相關規則；
- D&D 3.5 SRD 中可作 fallback 參考的 condition、NPC attitude、Diplomacy / Intimidate 等既有尺度；
- 哪些已被 D100 覆寫，哪些仍可合法作 SRD bridge。

---

## 2. FAtiMA

### 目前態度

**不採用。**

只偷它的：

```text
belief / goal
→ appraisal
→ decision / action proposal
```

不另建一套 FAtiMA emotional architecture。

### 暫定目的

**主要是讓「政治家」更好落地。**

政治家目前擅長輸出 leverage、resource dependency、coalition / conflict incentives、reputation effect、second-order reaction 等 forecast / constraint；FAtiMA 值得偷的是一個很薄的 decision schema，幫它把：

```text
目前利益／目標／信念／關係 evidence
→ 這個事件對 actor 意味著什麼
→ 哪些行動傾向因此上升／下降
→ 交給 AO 的具體 proposal
```

接起來。

這不是讓政治家取得「NPC 真正內心」的 authority，也不是讓 forecast 變成未來必然。

### 與現有模塊的連結

- **政治家**：主要受益者；作為 forecast → actionable proposal 的落地骨架。
- **分析師**：可提供角色結構 interpretation，但不能取代 actor 的 goal / belief，也不能直接指定行動。
- **圖書館員**：提供 relationship evidence bundle / provenance。
- **AO**：決定 proposal 是否在世界因果下實際成立；只有結果能寫回 state。

### 待驗證

- 政治家現有 prompt / contract 是否其實已能穩定完成這一步；
- 若只是補一個輸出 schema 就能解決，就不要新增模塊或長期狀態。

---

## 3. Cognitiv

### 目前態度

**深挖。可能形成真正的認知模組。**

五個候選中，這一項目前最值得研究完整資料流，而不是只偷單一欄位。

### 感興趣的核心

不是「模擬情緒」，而是：

```text
perception
→ subjective encoding
→ memory / association
→ uncertain recall
→ interpretation
→ later behavior input
```

也就是讓：

```text
客觀發生的事
≠ actor 知道的事
≠ actor 記得的事
≠ actor 目前相信的事
≠ 分析師對 actor 的解讀
```

在 runtime 中真的可以分開。

### 與現有模塊的連結

- **Actor epistemic state**：最直接的接口；Cognitiv 類概念可能補足「知道／記得／相信／不確定」之間的動態。
- **分析師**：分析師應讀 actor 的 role-safe 主觀材料，而不是把自己的 interpretation 寫成 actor cognition。
- **圖書館員**：管理來源與 provenance；回答「資訊從哪來」，但不替 actor 決定如何記住它。
- **詭祕**：classification / clearance / need-to-know 必須先於 cognition；認知模組不能藉 memory / association 繞過資訊權限。
- **政治家**：可讀 actor 合法可知的 belief / uncertainty 作為資訊不對稱與二階反應的輸入。
- **AO / Orchestrator**：客觀世界事實仍在 authoritative state；Cognitiv 類資料最多形成 actor-local state / derived state，不得建立平行世界真相。

### 深挖時要回答

1. Cognitiv 的哪些資料是 persistent actor state，哪些只是 derived cache？
2. uncertain recall / interference 是否真的值得機械化，還是 LLM context 已足夠？
3. 如何避免「認知模組」變成另一個偷偷知道世界真相的資料庫？
4. 是否需要獨立模組，或只需擴充 Actor Epistemic State schema？
5. 對 PL+PC，哪些內在 belief / interpretation 必須由 Player Layer 決定，不能由 runtime 自動補完？

---

## 4. ZifaMem

### 目前態度

**不採用整套；偷 `strength / evidence / decay / reinforce`。**

目前主要目的：**讓關係的變化成為可能，而不是把關係一次寫死。**

### 想偷的資料生命週期

```text
evidence exists
→ 有 strength / weight
→ 後續事件可以 reinforce / weaken
→ 很久未被支持的影響可以 decay
→ 新證據可以修正舊理解
```

這些量本身不是 relationship fact。

### 與現有模塊的連結

- **Relationship Graph**：客觀 edge 與「支持這條關係判斷的 evidence」分開；不要直接把 strength 當 edge 真相。
- **圖書館員**：最適合做 evidence / provenance gateway，指出哪些已發生事件正在支持某個關係變化。
- **分析師**：可用 evidence strength 做可撤回 interpretation，例如「持續靠近／裂痕候選」，但不能直接宣布 relationship 已改變。
- **政治家**：可用關係 evidence 與其強弱作 coalition / trust / leverage forecast 的輸入。
- **AO / Orchestrator**：真正發生的關係事件／承諾／決裂／和解等，才依合法 owner 與 world event 寫回 authoritative state。

### 與骰子／D&D 規則的關係

優先只把這套概念用在**需要機械判定的條件**，例如某段經驗是否足以提供判定修正、觸發、知識／恐懼／信任相關的 mechanic。

但不把它限制成「只有骰子才能存在」；若它能安全地支撐 relationship evidence lifecycle，也可以作為非骰子 adjudication 的輸入。

### 待決

- decay 是世界時間、session、章節還是事件驅動？
- 哪些 evidence 根本不應自然 decay（例如正式承諾、公開背叛）？
- reinforce / weaken 是 deterministic rule、AO adjudication，還是只做 qualitative tag？
- 如何避免把 evidence strength 偽裝成「角色真正有多愛／多信任」？

---

## 5. Ensemble / CiF

### 目前態度

**不採用整套 engine；偷 social-state taxonomy，以及尺度／狀態轉換思想。**

目前把它視為「資料庫有哪些社會量值得存在、各類 social state 應該怎麼分層」的參考，而不是約會聊天模組。

### 最值得偷的區分

```text
Relationship
≠ continuous / ordinal social scale
≠ temporary status
≠ actor belief about relationship
≠ analyst interpretation
```

可能有用的 taxonomy 類型包括：

- 較硬的 relationship / role edge；
- 可變的 social scale；
- 暫時 social status；
- 由 event / rule 驅動的 state transition；
- 行動傾向／volition 只作 derived output，不直接變成世界事實。

### 與現有模塊的連結

- **Relationship Graph / social state**：主要受益層；可幫忙決定哪些欄位應是 edge、scale、status、belief。
- **圖書館員**：提供建立／改變 social state 的 evidence 與 provenance。
- **分析師**：讀同一 social state 做 derived interpretation，不另養一份「真正關係」。
- **政治家**：讀 relationship / scale / obligation / reputation 等結構做 coalition、conflict、leverage、second-order forecast。
- **AO / Orchestrator**：state transition 最終仍需由已發生事件／合法結算／合法 owner 決定；不能因尺度過閾值就自動創造未發生的世界事件。

### 3.5 / D100 既有尺度優先審計

**正式設計任何新 social scale 前，先查 3.5 與 D100 本來有哪些尺度。**

尤其先由圖書館員確認：

- D&D 3.5 的 NPC attitude / social skill 相關階梯是否可作 fallback 參考；
- 恐懼、士氣、敵意、友好、影響等是否已有 condition 或判定框架；
- D100 Sheet 是否已有自己的態度／關係／聲望／組織好感／社交技能尺度；
- 哪些 3.5 尺度已被 D100 明確取代，不能重複導入。

原則：

```text
現有 D100 rule > 新造 social scale
合法 SRD bridge > 無必要的平行系統
外部 framework taxonomy = 參考，不是來源權威
```

---

## 暫定優先順序

目前研究順序：

1. **Cognitiv：深挖。** 先判斷它究竟值得形成認知模組，還是只需擴充 Actor Epistemic State。
2. **Ensemble / CiF：拆 taxonomy。** 但在造尺度前先完成 D100 / 3.5 既有尺度審計。
3. **ZifaMem：拆 evidence lifecycle。** 優先服務「關係可以改變」與有規則需要的可判定條件。
4. **FAtiMA：只驗 decision schema 是否能補政治家落地。**
5. **Emotion Engine：最低優先。** 除非現有 D100 / 3.5 規則確實缺少必要的暫態情緒機械量，否則不做。

---

## 成功條件

這批研究只有在能讓現有架構更薄、更清楚時才值得採用。

```text
不增加不必要 Agent
不建立平行世界真相
不把 interpretation / forecast 升格成 fact
不把暫態情緒寫成永久人格
不把 evidence strength 寫成「真正感情值」
不重造 D100 / 3.5 已有尺度
讓關係可以因已發生事件而改變
讓 actor 的主觀認知可以和客觀世界安全分離
讓政治家的 forecast 更容易落成 AO 可處理的 proposal
```

---

## 待解決疑難

### Relationship Graph 的「客觀事實 only」是否過窄？

`RUNTIME_SOCIAL_WORLD_CONTRACT.md` 的 Relationship Graph 規則是在 2026-09-15 建立 social-world contract 時先做出的防污染設計：分析師／政治家的心理與關係推論不得因為「看起來合理」就直接寫回 authoritative relationship fact。這條原則原本主要在阻止 **derived interpretation → world fact** 的偷渡。

但在目前對 Cognitiv、ZifaMem、Ensemble / CiF 的重新取樣後，出現新的疑問：**「不是客觀事件」不代表它只能是 derived hypothesis。** 某些主觀社會狀態可能本身就是合法、持久、由 actor owner 建立的 actor-local state，例如：

```text
Nella 對 Elian：覺得有趣
```

這不是外部分析師猜測，也不是「兩人已經有某種客觀關係」；但它又比一次性 prose 更像應被持久化、可供後續 cognition / decision / social-state transition 使用的資料。

目前需解的不是「能不能有感情線」，而是**這類資料究竟屬於哪一層、由誰擁有、如何變動，以及 Relationship Graph 是否只應保存硬事件。**

待決問題：

1. Relationship Graph 是否維持目前定位，只保存 event / role / commitment / debt / dependency / shared-resource 等較硬的 authoritative relation；主觀 impression / affect / preference 永遠留在 actor card / actor-local state？
2. 或者應把 Relationship 擴成有型別的 social-state 容器，在同一資料骨架中明確區分：`objective edge`、`actor-local impression`、`social scale`、`temporary status`、`derived interpretation`？
3. `trust`、`attraction`、`interest`、`loyalty`、`friendship depth` 這類詞，不應只用「不能自動成立」處理；它們各自應被分類成 actor state、relationship state、social scale、commitment，還是 derived view？
4. 對 PL+PC，Player Voice 明示的內在 impression／preference 應如何取得 authoritative actor-state 身分；對 NPC，AO 採用的 cognition / affect proposal 又如何留下 provenance？
5. ZifaMem 的 `strength / evidence / decay / reinforce` 應作用在 evidence、actor-local impression、social scale，還是多層皆可？哪些量可 decay，哪些一旦成立就應只靠新事件轉換？
6. Ensemble / CiF 的 taxonomy 能否解開「客觀關係」與「主觀社會狀態」目前擠在同一個 Relationship 詞彙下的問題？
7. Cognitiv 若形成 actor cognition layer，`覺得有趣` 這類 social impression 是否應首先屬於 cognition，而 Relationship Graph 只持有對它的 pointer / provenance？
8. D100 / D&D 3.5 若已有 NPC attitude、態度／聲望／關係尺度，哪些可以直接承擔上述 social scale，而不另造新值？
9. 待上述分類完成後，是否應回頭重寫 `RUNTIME_SOCIAL_WORLD_CONTRACT.md` §2.1 與 `RELATIONSHIP_GRAPH_TEMPLATE.md`：把重複的「不能／不得自動」提示，改成更明確的 `type / owner / provenance / transition` schema，而不是靠負面 prompt 維持邊界？

### 目前暫存做法

在這個問題解完以前，先採最小、可回退做法：

```text
已發生的客觀互動事件
→ Relationship Graph

明確由 actor owner 成立的主觀 impression / affect
→ actor-local state / character record

分析師／政治家推論
→ derived view
```

Andor 目前的 `Nella → Elian：覺得有趣` 暫存在 Nella 的 actor record；不把它硬升格成 relationship edge，也不把它視為被禁止的發展。

**本節只是待解問題登記，不在此直接修改 runtime contract。**