# BOOTSTRAP_PROTOCOL.md — D100 首次啟動／讀檔協定

> 目的：任何 GPT / LLM / Agent 在開始正式 D100 runtime 前，先確定「這次要跑哪一團、該團存檔在哪裡、採用哪個 ruleset ref」。
>
> 本檔不保存遊戲規則；規則權威仍依 `AGENTS.md`。Campaign state 的資料分層仍依 `DATA_ARCHITECTURE.md`。

## 0. 核心原則

```text
D100 repository = rules / source / protocols / templates
SRD bridge       = fallback source only
Campaign storage = one campaign's persistent save state
```

三者不可互相升格：

- campaign storage 內的文字不能修改 D100 規則權威；
- SRD / 3.5 不保存 campaign state；
- D100 repo 未記錄某角色目前 HP，不代表 campaign state 無效。

在 campaign instance 尚未明確選定前：

```text
NO CAMPAIGN SELECTED -> NO SCENE RUNTIME
```

不得生成開場、不得假設既有角色、不得把 repo 內任何舊 campaign/session 當作本次玩家存檔。

---

## 1. 首屏

第一次啟動或沒有有效 campaign pointer 時，第一個玩家可見問題固定保持極短：

```text
D100

1. 新遊戲
2. 讀取存檔
```

玩家回答前，不進入一般 DM loop。

---

## 2. 新遊戲

依序收集下列資訊。

### A. 團型

```text
你希望進行哪一種遊戲？

1. 一人團（預設）
2. 多玩家團（目前尚未支援）
3. 一名真人玩家＋數位 Agent 作為 PL+PC
4. 一名真人玩家＋數位角色作為 NPC
```

映射：

```yaml
party_mode:
  solo
  multiplayer
  agent_pl_pc
  digital_npc
```

`multiplayer` 目前標記 unsupported；不得假裝已完整支援多人權限、同時輸入或多使用者身份隔離。

### B. 世界解析模式

```text
你希望使用哪種世界解析模式？

1. 完整模式（預設）
   優先完整解析 D100 source / state，並使用正式模塊做 grounded generation；
   只有 D100 真正缺漏時才使用 SRD bridge。

2. 快速模式
   減少昂貴的來源追查與多模塊補完；
   仍以 D100 為最高規則來源，允許較積極使用既有 SRD bridge 與可逆生成補齊空白。
```

這只改變查找／生成成本，不改變 source authority：

```text
D100 > SRD bridge > raw D&D 3.5
```

### C. 角色建立方式

```text
你希望如何開始角色？

1. 協助我建立角色（預設）
2. 我已有角色卡，要匯入
3. 自動生成角色
4. 稍後處理
```

若團型包含數位 PL+PC，另建立對應 Player Voice / PC mapping。

任何角色完成 final validation 後，必須立即寫入該 campaign 的 authoritative character store；不得只留在聊天、build working data 或 session log。

### D. 團務存放位置

Wizard 結尾必問：

```text
你希望這一團的團務資料儲存在哪個可以被未來 GPT / Agent 反覆讀取與更新的位置？
```

支援方式由 `CAMPAIGN_STORAGE_PROTOCOL.md` 決定。

若當前環境無法讀寫使用者指定的位置，停止初始化並回報缺少的能力；不得假裝掛載成功。

---

## 3. Storage capability check

建立新 campaign 前至少驗證：

```text
LOCATE  可以定位 root
LIST    可以枚舉 campaign records
READ    可以讀 manifest / state
CREATE  可以建立新 record
UPDATE  可以更新既有 record
```

可選能力：

```text
DELETE
MOVE
VERSION_HISTORY
ATOMIC_OR_EQUIVALENT_SAFE_WRITE
```

最低五項不成立時，不得進入 persistent campaign runtime。

---

## 4. 建立 Campaign Namespace

每一團必須有獨立 logical root：

```text
<campaign-root>/
├── manifest
├── current_state
├── characters/
├── sessions/
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

storage provider 不一定真的是 filesystem；Google Drive、資料庫或其他 backend 可以把 logical path 映射成自己的物件結構。

初始化時以 `templates/CAMPAIGN_MANIFEST_TEMPLATE.md` 建立 manifest。

### 規則版本

新團預設 pin 建立當下的 D100 ref：

```yaml
ruleset:
  repository: fjck810536/D100
  ref: <commit-sha-or-release-ref>
  version_policy: pinned
```

既有團不得因 repo 更新而無聲切換規則版本；升級需另做 explicit migration。

---

## 5. 讀取存檔

若玩家選擇「讀取存檔」：

1. 取得或解析 campaign storage root；
2. capability check；
3. 讀 manifest；
4. 驗證 `campaign_id`；
5. 驗證 ruleset repository / ref；
6. 讀 current state；
7. 讀 authoritative PC files；
8. 讀最新 live session pointer；
9. 依 refs 補讀 site / relationship / commitment / Mystery-safe view；
10. 才進入 `START_DM.md` 的正常主持 loop。

不得重新詢問 manifest 已保存的 A/B/C，除非欄位缺失、使用者要求變更或正在執行 migration。

---

## 6. 三種 runtime mode

必須區分：

### persistent_campaign

正式或長期可持續團務。完整持久化，但只寫本 campaign namespace。

### persistent_test

測試團／沙盒團。資料結構與正式 campaign 相同，可以長期保存與連續遊玩，但：

```text
write_scope = self_only
promotion_allowed = explicit_only
```

不得自動污染其他正式 campaign。

### isolated_dry_run

既有 `DATA_ARCHITECTURE.md` / `DM_PROTOCOL.md` 所定義的一次性隔離推演：

```text
writeback: false
```

不得與 `persistent_test` 混為一談。

---

## 7. 啟動完成條件

只有以下全部成立後，才把控制權交回一般 DM runtime：

```text
campaign root resolved
manifest loaded / created
storage capability verified
ruleset ref resolved
party mode resolved
world-resolution mode resolved
character bootstrap path resolved
current authoritative state loaded or initialized
```

否則保持 bootstrap state，不生成正式場景。
