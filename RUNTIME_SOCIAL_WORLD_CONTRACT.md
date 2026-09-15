# RUNTIME_SOCIAL_WORLD_CONTRACT.md — 社會世界／角色關係／秘密預承諾契約

> 狀態：runtime architecture contract。
>
> 目的：讓 D100 世界在玩家沒有注視時仍有自己的狀態、關係與因果；讓分析師、政治家、圖書館員、詭祕、AO 等模塊共享同一資料骨架，而不是各自養一份人物關係或陰謀真相；並明確區分四聲部作為高品質 NPC 與被要求作為 PL+PC 的兩種運作模式。
>
> 本檔與 `DATA_ARCHITECTURE.md`、`DM_CABINET.md`、`DM_PROTOCOL.md`、`MYSTERY_PROTOCOL.md` 同屬 runtime 契約層。若本檔只是補充某一跨模塊資料接口，優先依本檔；若牽涉規則來源、AO 特權或 EX 安全邊界，仍依對應上位契約。

---

# 0. 核心原則

```text
世界先有狀態，玩家再接觸它。
秘密可以延遲揭露，但不能因玩家擲骰後才決定是否存在。
關係事實、角色知識、模塊分析必須分層。
四聲部可以是 NPC；只有明確要求 PL+PC 時才進 Player Layer。
模塊共享資料，不共享一份模糊的「故事直覺」。
```

仍遵守既有總資料流：

```text
SOURCE / RULE DATA
→ NORMALIZED / INDEX DATA
→ AUTHORITATIVE WORLD / ACTOR / RELATIONSHIP / SECRET STATE
→ ROLE-SAFE VIEWS
→ CABINET REASONING
→ AO RESOLUTION
→ ORCHESTRATOR STATE UPDATE
```

任何 Cabinet 輸出若只是 interpretation / forecast / hypothesis，必須停留在 derived view；不能因為講得很有說服力就升格為世界事實。

---

# 1. Alignment 是角色結構資料，不是行動腳本

角色可以保存九宮格陣營：

```yaml
alignment:
  law_chaos: lawful | neutral | chaotic
  good_evil: good | neutral | evil
```

或在 UI / 顯示層合併為：

```text
Lawful Good / Neutral Good / Chaotic Good
Lawful Neutral / True Neutral / Chaotic Neutral
Lawful Evil / Neutral Evil / Chaotic Evil
```

## 1.1 分析師的使用方式

分析師可把 alignment 當作角色的一個長期倫理／秩序座標，但必須與以下資料並讀：

```text
alignment
presented_persona
current_affect
roles / obligations
relationship position
behavior history
epistemic state
```

必須允許：

```text
Chaotic Evil
+ 長期演得友善／體貼
+ 當下情緒穩定
+ 此刻做出善行
```

這些並不自動矛盾。

分析師可以問：

- 角色的公開形象與 alignment 如何共存？
- 某些反覆行為是義務、依戀、策略、形象管理，還是價值真的改變？
- 哪些壓力下 alignment、persona、affect、actual action 會分裂？

分析師不得做：

```text
CE → 現在一定做壞事
LG → 不得失控
CN → 隨機行動
```

Alignment 不要求 RP 擲骰。

## 1.2 Alignment 變動

真玩家 PC 的 alignment 由玩家／GM 明示，不由分析師依幾次行為偷偷重分類。

若長期劇情真的造成 alignment 轉變，必須作為顯式 character-state transition 記錄 provenance / trigger，而不是 derived cache 自動覆寫。

---

# 2. Relationship Graph — 客觀關係事實

關係資料是 authoritative state 的一部分，但不建立「關係人格模塊」。

推薦使用：

```text
templates/RELATIONSHIP_GRAPH_TEMPLATE.md
```

一條 relationship edge 至少可以保存：

```yaml
edge_id:
actor_a:
actor_b:
relation_types: []
established_events: []
commitments: []
debts: []
authority_or_dependency: []
shared_resources: []
public_status:
secret_refs: []
last_updated:
```

## 2.1 只記真正成立的關係事實

例如：

```text
A 曾請 B 吃飯
A 把魔法物品交給 B 暫時持有
A 與 B 約定明日在某地碰面
A 欠 B 50gp
A 是 B 的直屬上司
```

可以進 Relationship Graph。

以下不能直接進 authoritative relationship facts：

```text
A 其實愛上 B
B 一定把 A 當替代父親
A 很可能三天後背叛 B
兩人的關係「本質上」是競爭性的
```

除非這些已由角色／世界事件明確建立；否則只能是分析師／政治家的 derived view。

## 2.2 新角色發展 ≠ 對既有歷史的無證據升格

「目前不能證明角色早已愛上某人」只限制**對過去／既有狀態的斷言**，不等於「角色現在不能開始產生新情緒、意向或行動」。

```text
沒有既有 romance fact
≠ 禁止 attraction candidate
≠ 禁止 flirtation candidate
≠ 禁止未來形成 romance
```

對真玩家 PC 與 `pl_pc` 四聲部：

```text
合法 Player Voice decision
→ 可以從當下建立新的 actor affect / preference / intention
→ PC 可以據此宣告新行動
→ 世界結算後留下事件／關係事實
```

不需要先找到「角色以前已經有同種感情」的證據，才允許新感情出現。

對 NPC：分析師／生態學家可以提出新發展 proposal；AO 依合法 actor state、情境與世界因果決定是否採用。分析師的 hypothesis 本身仍不等於 NPC 真正內心。

例如：

```text
分析師：Nella 可能被 Elian 吸引 → hypothesis only
蟬｜PL：我決定 Nella 現在開始被吸引 → 新 actor state 可以成立
蟬｜PL：Nella 調情 → PC declaration / event
Elian 是否被吸引 → 仍由 Elian 的玩家／合法效果決定
雙方是否已成戀人 → 仍需真正成立的雙方事件／承諾，不自動升格
```

`OOC_AMBIGUOUS` 事件不得因後來允許新發展，就回收成先前的 IC 情感證據。

---

# 3. Epistemic Matrix — 誰知道什麼

Relationship Graph 不取代角色原本的 Epistemic State。

每個 actor 仍分開保存：

```yaml
known_facts: []
beliefs: []
misbeliefs: []
```

必要時可加二階知識：

```yaml
beliefs_about_others_knowledge:
  - subject:
    proposition_ref:
    belief:
```

核心保險絲：

```text
世界是真的 ≠ 角色知道是真的
A 知道 ≠ B 知道
知道某事 ≠ 相信某人
相信某事 ≠ 願意配合
```

地點／組織亦同：

```text
世界中某 site 已存在
≠ 公開地圖一定標出其秘密身分
≠ PC 知道它隸屬哪個組織
≠ NPC 知道其全部功能
```

可以存在「公開場所 + 隱藏 affiliation」；世界後台先有同一 site，前台依 actor knowledge / visibility 顯示不同標籤，不為不同角色建立平行世界。

---

# 4. Evidence Ledger — 玩家看到的是證據圖，不是真相圖

調查型 runtime 應把線索至少區分：

```text
OBSERVED    角色直接觀察到
INFERRED    由觀察推導，但尚未確認
CONFIRMED   已由可靠來源／交叉證據確認
DISPROVEN   後續證據否定
```

推薦記錄：

```yaml
evidence_id:
proposition:
status: OBSERVED | INFERRED | CONFIRMED | DISPROVEN
observed_by: []
source_refs: []
related_secret_refs: []
notes:
```

玩家／角色得到的是 **Evidence Graph**。

AO／Mystery 可以持有 **Causal Graph**。

兩者不可混寫：

```text
Evidence Graph = 角色目前有什麼理由相信什麼
Causal Graph   = 世界實際發生了什麼、哪些事情真的互為因果
```

一條推論被角色重複談很多次，不會因此自動升格為世界真相。

---

# 5. 圖書館員、分析師、政治家的 Relationship Data Pipeline

三者共用同一 Relationship Graph / Epistemic Matrix / event history，但職責不同。

## 5.1 圖書館員 — provenance / history / retrieval gateway

圖書館員可以回答：

```text
這段關係由哪些已發生事件建立？
哪個角色檔／session／secret ref 支持這件事？
某承諾是在何時形成、是否已履行？
某情報是 observed、inferred 還是 confirmed？
```

它不擁有另一份 relationship database；只負責從 authoritative state / history 找 provenance 與合法 view。

## 5.2 分析師 — actor / relationship structure

分析師取得合法 view 後，可產生：

```text
S / I / R interpretation
alignment tension
persona / action discrepancy
self-image / other-image
attachment / rivalry / dependency structure
rupture points
```

全部屬 derived cache。

分析師不得把未揭露秘密當作角色心理證據；也不得把自己的解讀寫回「真正人格」。

## 5.3 政治家 — leverage / coalition / second-order effects

政治家取得合法 view 後，可產生：

```text
leverage
resource dependency
alliance / conflict incentives
reputation effects
faction reaction
second-order consequences
```

同樣只屬 forecast / constraint。

## 5.4 前端／預後段資料鏈

推薦理解為：

```text
歷史事件／provenance
        ↓
當前 Relationship Graph + Epistemic Matrix
        ↓
分析師 relationship interpretation
政治家 political / social prognosis
        ↓
AO 只在實際世界需要演進時整合
        ↓
Orchestrator 寫回真的發生的事件
```

分析師與政治家不直接互相寫對方的 cache，也不讓圖書館員替它們預測未來。

---

# 6. 四聲部控制模式：NPC vs PL+PC

四聲部可以合法地作為高品質 autonomous NPC。

只有在使用者／DM 明確要求「四聲部是玩家＋PC」「四聲部作為 PL&PC」「讓四聲部玩家一起跑」或同等意思時，才切換到 PL+PC 模式。

Session state 建議保存：

```yaml
four_voice_control:
  mode: npc | pl_pc
  mappings:
    - player_voice:
      pc_id:
```

## 6.1 NPC mode

```text
DM / AO / actor pipeline
→ autonomous actor proposal
→ actual NPC action
```

四聲部可以被直接當高品質 NPC 扮演。

不要事後把 DM 生成的 NPC 行為反過來稱為「四聲部玩家偏好」。

## 6.2 PL+PC mode

資料流必須改成：

```text
Player Voice
→ Player decision / agenda
→ 該 Player 對自己的 PC 作 interpretation
→ PC declaration / roleplay
→ DM adjudication
→ world response
```

Player Layer 可以暫存：

```yaml
player_layer:
  agenda: []
  current_interest: []
  risk_tolerance:
  interpretation_of_pc: []
  intended_play: []
```

這些是 player-side working data，不是 PC 的世界內心理狀態。

### PL+PC 保險絲

在 PL+PC mode 下：

- DM 不應直接替四聲部 PC 補關鍵選擇；
- 讀心者只能猜玩家意圖，不能取代玩家決策；
- 生態學家／分析師可以提供 proposal，但 player voice 可以拒絕；
- PC 合理性不是強制最佳化器；玩家可以明知冒險仍選擇冒險；
- 若 player voice 沒理解另一角色的暗示，不應由 DM 為了劇情順暢自動補成「PC 理解了」。

---

# 7. Secret / World Commitment — lazy generation, early commitment

## 7.1 核心規則

```text
秘密可以晚寫細節，但核心真相必須在第一次可觀察／可影響前 committed。
```

這不是要求一開始生成整座城市所有居民。

而是：當某個 NPC、事件、秘密、裝置第一次可能因玩家行動而被觀察、改變、檢定、追蹤時，與該互動結果相關的最小 hidden state 必須先固定。

推薦使用：

```text
templates/WORLD_COMMITMENT_TEMPLATE.md
```

最小 commitment 可以只有：

```yaml
commitment_id:
commitment_status: committed
truth_core:
involved_entities: []
knowledge_holders: []
misbelief_holders: []
existing_evidence: []
actor_goals: []
actor_constraints: []
world_clock: []
mutable_surface_details: []
secret_refs: []
```

## 7.2 什麼必須先鎖

若一名可疑 NPC 已經會因玩家說出某個詞而停下湯匙，那麼在那個反應發生前至少要知道：

```text
他是誰／最低限度身份
他知道什麼
為什麼這個詞會引發反應
他原本的目標／下一站
他有哪些相關 constraint
```

不必提前寫：

```text
他襪子的顏色
巷口店家的名字
沒有因果重要性的口頭禪
玩家尚未接觸的室內裝潢
```

這些 surface detail 可以即時生成，只要不反向改寫核心因果。

## 7.3 禁止骰後定真相

禁止：

```text
玩家跟蹤成功
→ 才決定此人其實是重要間諜

玩家跟蹤失敗
→ 才決定此人原來只是普通路人
```

正確：

```text
先 committed hidden actor state
→ 玩家決定是否調查
→ 骰子只決定玩家發現／影響多少
```

## 7.4 最小承諾是底線，不是生成上限

`lazy generation, early commitment` 不得被解讀成「能不生成就永遠不生成」。

```text
已成立事實 → 約束新生成
來源未描述的可創作部分 → 可以提出具體候選
合法 owner 採用 → 可以成為新的 authoritative state
影響檢定的既存秘密 → 必須在檢定前固定
```

世界需要可走的地點、人物、制度、服務、師承或聯絡方式時，在不衝突且權限允許的情況下應完成足以支持互動的因果骨架，而不是把來源空白永久保留成不可進入的空洞。

---

# 8. Secret existence 與 Secret release 分離

Mystery 管理的是：

```text
誰可以知道
知道多少
何時能揭露
用哪種 representation
```

不是：

```text
玩家查到這裡時才要不要創造秘密
```

因此：

```text
SECRET EXISTS
≠
SECRET IS REVEALED
```

一個秘密可以：

- 已存在；
- 已有世界效果；
- 已被某些 NPC 知道；
- 玩家完全不知道。

玩家行動控制的是 evidence acquisition / release / interference，不控制秘密是否曾經存在。

---

# 9. World Clock / Actor Commitments

為避免世界只在玩家進場後才開始活，重要 actor / faction / mystery 可以保存：

```yaml
commitments:
  - actor_or_faction:
    planned_action:
    trigger_or_time:
    dependencies: []
    cancel_conditions: []
```

沙漏負責時間／排程 view；政治家可提供 faction forecast；生態學家可提供 actor behavior tendency；AO 最後決定在當下 world state 下實際是否發生。

核心：

```text
schedule / commitment ≠ destiny
```

玩家介入、資訊改變、資源不足、角色死亡等都可以使原 commitment 失效。

---

# 10. Derived Cache Invalidation

以下資料都只能是 derived：

```text
relationship interpretation
alignment tension analysis
political prognosis
threat model
likely betrayal
likely escape route
combat doctrine
player-intent hypothesis
```

至少在以下改變時考慮失效：

```text
新事件
新證據
秘密揭露
關係狀態變化
角色 alignment 明示轉變
角色知識／誤信改變
傷勢／資源／位置改變
組織權力變化
玩家重新解釋自己的 PC
```

Derived cache 不得比它的 evidence 活得更久。

---

# 11. Session Snapshot 的正確分層

DM snapshot 不應再用一個模糊的 `Relationship / Knowledge State` 混在一起。

至少拆成：

```text
A. Relationship Facts         authoritative
B. Actor Epistemic Matrix     authoritative per actor
C. Evidence Ledger            observed/inferred/confirmed/disproven
D. Analyst Relationship View  derived
E. Politician Forecast        derived
F. Player Layer               only in PL+PC mode; meta working data
G. Secret / Commitment refs   hidden state refs, not plaintext duplication
```

---

# 12. Typed Deferral — 「尚未」必須有狀態轉移語義

不得把「不能太早」「現在不適合」「以後再說」當作模糊的長期控制詞。每一個看似 `not yet` 的狀態都必須落到以下型別之一：

| Type | 意義 | 必須能回答 |
|---|---|---|
| `NON_ASSERTION` | 現在不能把未確認命題宣稱為既有事實 | 哪個命題不能升格；**不封鎖候選生成** |
| `DEFERRED` | 某具體操作正在等條件 | owner、blocked_operation、trigger、reevaluate_with |
| `OWNER_DECISION` | 決定權屬特定 PL／AO／其他合法 owner | owner；不是世界禁令 |
| `PROHIBITED` | 規則／既有事實真的禁止具體操作 | rule_or_fact_ref、scope、blocked_operation |
| `NOT_SELECTED` | 此次沒有選某候選 | decision event；不得推成永久禁止 |

保險絲：

```text
NON_ASSERTION ≠ PROHIBITED
沒有 trigger 的 DEFERRED 無效
沒有新規則／事實／權限邊界，不能把合法候選越修越少
NOT_SELECTED ≠ NEVER
hard prohibition 必須明說 prohibition，不用「還不能太早」安撫性包裝
```

重新評估觸發可以包括：

```text
新的 Player Voice decision
新的角色內心／意向明示
新的關係事件
新的世界事件
新的來源／使用者校正
新的角色知識
新的生成需求
原 blocking fact 消失
```

相同依據沒有改變時不必每輪空轉；但一旦底層 state 改變，舊的 non-assertion / derived interpretation 必須可以失效重算。

---

# 13. Anti-patterns

以下情形視為 runtime 偏移：

```text
玩家問到哪裡，核心秘密才生成到哪裡
骰得好就把普通 NPC 升格成關鍵人物
骰得差就把原本可疑人物降成無關路人
把分析師解讀寫成角色真正內心
把政治家預測寫成未來必然事件
把世界關係與角色相信的關係混在一起
NPC mode 的四聲部行為被事後稱為「玩家選擇」
PL+PC mode 下 DM 仍跳過 Player Layer 直接替 PC 做關鍵選擇
Alignment 被當成每場戲的行為指令
「目前未成立 romance」被當成禁止 attraction / flirtation / 新關係事件
來源缺口被當成永久禁止世界生成
沒有 trigger 的「不能太早」無限延宕
```

理想狀態是：

```text
世界先有狀態
角色各自只知道一部分
關係與秘密有 provenance
模塊從同一資料層取得不同 view
玩家不在場時世界仍會往前走
LLM 用來具象化既有因果，也能在未定部分做有據創作
來源、決定權與生成 origin 始終可追溯
```
