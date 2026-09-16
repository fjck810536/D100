# BOOTSTRAP_PROTOCOL.md — D100 首次啟動／讀檔協定

> 目的：任何 GPT / LLM / Agent 在開始正式 D100 runtime 前，先確定「這次要跑哪一團、該團存檔在哪裡、採用哪個 ruleset ref」。
>
> 本檔不保存遊戲規則；規則權威仍依 `AGENTS.md`。Campaign state 的資料分層仍依 `DATA_ARCHITECTURE.md`，backend 映射依 `CAMPAIGN_STORAGE_PROTOCOL.md`。

## 0. 核心原則

```text
D100 repository = rules / source / protocols / templates
SRD bridge       = fallback source only
Campaign storage = one campaign's persistent save state
```

公開 upstream `fjck810536/D100` 與其 GitHub Pages 是規則／來源入口；能公開讀取，不表示玩家或當前 Agent 能把存檔寫回該 repository。`ruleset.repository` 與 `storage.root_ref` 分別解析，不從前者推定後者。

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

任何角色完成 final validation 後，必須立即寫入該 campaign 的 authoritative character store，並以 exact record ref readback 驗證；不得只留在聊天、build working data 或 session log。

### D. 團務存放位置

Wizard 結尾必問：

```text
你希望這一團的團務資料儲存在哪個可以被未來 GPT / Agent 反覆讀取與更新的位置？
```

支援方式由 `CAMPAIGN_STORAGE_PROTOCOL.md` 決定。

先依當前環境可用能力，提供玩家能持續 READ / CREATE / UPDATE 的選項：

| 選項 | 選定位置與驗證 |
|---|---|
| Google Drive | 玩家指定的單一 campaign folder；依 `storage_backends/GOOGLE_DRIVE.md` 驗證 connector 與權限 |
| 自己的 Git repository | 指定 repository、可寫 branch 與 campaign path；確認能把 create / update 持久化到該 remote |
| local / mounted folder | 指定可持續保存、未來 runtime 可重新掛載的實際路徑；確認檔案讀寫能力 |
| repo-local | 僅在玩家明確選定且有寫入權限的 repository 使用 `campaign_instances/<campaign-id>/` |

Git / folder 選項沿用 storage protocol 的 logical API；列出名稱不代表當前環境已有可用 adapter。一次性 scratch 或唯讀 clone 不能當成可持續存檔後端。

外部玩家預設使用自己的 backend。公開 upstream 的 `campaign_instances/` 不是公共存檔服務；只有玩家明確選定它，且當前身份對該 repository／branch／namespace 確有 READ + CREATE + UPDATE 權限時，才可使用其中新選定的獨立 namespace。GitHub Pages 只有入口用途，沒有 campaign 寫入能力。

若指定位置缺少能力，保留已選的 A/B/C，指出缺少哪個操作，並引導改選當前可用的 backend 或接通該位置；驗證通過後接續初始化。

---

## 3. Storage capability check

建立新 campaign 與讀檔恢復 persistent runtime 前，對 **selected storage 的具體 root／當前身份** 至少驗證：

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

檢查的是工具能力與目標位置的實際權限，不只是「有 GitHub／Drive connector」。READ 成功、公開可見、能 fork／提 PR、能寫本機 clone，都不代表對選定 remote branch 有 CREATE + UPDATE；已存的 capability flag 也不取代本次驗證。

需要寫入探測時，只在已選定且有授權的 campaign namespace 使用 probe record，不修改其他團或既有 authoritative state。Capability check 不代表具體 save 已建立；初始化與重要寫入仍需 exact-ref readback。

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

### Stable refs

Manifest 必須保存 provider 可重讀的 stable refs，而不是只有人類名稱：

```yaml
storage:
  root_ref: <stable-root-locator>
records:
  manifest_ref: <stable-record-ref>
  current_state_ref: <stable-record-ref>
  characters_root_ref: <stable-record-ref>
  sessions_root_ref: <stable-record-ref>
```

重要角色可再保存：

```yaml
indexes:
  characters:
    <character_id>: <exact-character-record-ref>
```

禁止把「全域搜尋名字 → 第一個命中」當正常載入流程。

### 規則版本

沿用 exact commit SHA / release ref；人類易讀的版本名稱只補充顯示，最終 immutable pin 是 **完整 commit SHA**：

```yaml
ruleset:
  repository: fjck810536/D100
  ref: <commit-sha-or-release-ref>
  resolved_commit_sha: <full-commit-sha>
  version_label: null  # optional: 真實 tag / release 名稱；沒有則留空
  version_policy: pinned
```

新團依玩家指定的 SHA／release ref 解析到 commit；annotated tag 需解引用到 commit，而不是保存 tag object SHA。若未指定版本，讀取建立當下的 `main` HEAD **一次**，將該完整 SHA 存入 `ref` 與 `resolved_commit_sha`。`main` 是版本發現入口，不是 pin。

後續讀取規則／協定／模板時使用 `ruleset.repository` 的 `resolved_commit_sha`；先前從 main／Pages 讀取的啟動資料，須按該 SHA 重讀 runtime 所需文件。若無 tag／release，可顯示短 SHA，實際 pin 仍保存完整 SHA；不為了 onboarding 虛構版本號或強制建立 release。

載入相容性：

- 舊 manifest 的 `ref` 已是完整 commit SHA：直接作 immutable pin，缺少新欄位不阻擋載入，也不要求改寫舊存檔。
- 若 `ref` 與 `resolved_commit_sha` 都是完整 SHA，兩者須相同；不一致時先釐清 manifest／migration 紀錄，不自行挑一個版本。
- 已保存 `resolved_commit_sha`：以它載入；tag 被移動／刪除不會改變 pin，版本標籤只作建立時的識別資訊。
- 舊 manifest 只有 release ref：用建立時的 release／commit 紀錄確認原始 SHA，再依明確 migration 補記；若無法確認，詢問原始 SHA 或明確選擇版本 migration。只查今天的 tag 指向，不能證明它是當初版本。
- pin 無法讀取時，回報該 SHA 與缺少的存取能力，提供恢復存取或 explicit migration 路徑，不自動改用 main。

既有團不得因 repo 更新而無聲切換規則版本；升級需另做 explicit migration。

### 初始化 readback

新 campaign 只有在以下都成功後，才能標 initialized：

```text
root 可重新定位
manifest 可由 exact ref 重新讀取
current state 可重新讀取
collection refs 指向同一 campaign root
ruleset immutable commit SHA 可解析並讀取
```

若 provider 建立 manifest 後才知道 manifest 自己的 ID，可做一次 self-reference update，再 readback；這不是建立第二份 manifest。

---

## 5. 讀取存檔

若玩家選擇「讀取存檔」：

1. 取得或解析 campaign storage root；
2. capability check；
3. 由 exact `manifest_ref` 讀 manifest；若尚無 exact ref，僅在 selected root 內解析唯一 manifest；
4. 若存在多個同等 manifest 候選，停止並報 storage ambiguity，不以修改時間猜；
5. 驗證 `campaign_id`；
6. 依第 4 節解析／驗證 ruleset immutable commit SHA，從該 SHA 載入 runtime 所需規則／協定；
7. 讀 exact current-state ref；
8. 讀 authoritative PC masters／character index refs；
9. 讀最新 live session pointer；
10. 依 refs 補讀 site / relationship / commitment / Mystery-safe view；
11. 才進入 `START_DM.md` 的正常主持 loop。

不得重新詢問 manifest 已保存的 A/B/C，除非欄位缺失、使用者要求變更或正在執行 migration。

不得為了「找得到」而跳出 selected root 全域搜尋同名角色／session。

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

`persistent_test` 仍必須保存完整 final character masters、current state、session history、sites／relationships／commitments／Mystery refs；不能因為是測試團就把角色身分資料留在聊天暫存。

### isolated_dry_run

既有 `DATA_ARCHITECTURE.md` / `DM_PROTOCOL.md` 所定義的一次性隔離推演：

```text
writeback: false
```

不得與 `persistent_test` 混為一談。

---

## 7. Persistence boundary

重要 write boundary 至少包含：

```text
campaign initialization
character finalization
session end
explicit migration / promotion
```

這些操作都遵守：

```text
write exact selected-campaign record
→ read back exact record ref
→ verify identity / required content / namespace
→ only then report persisted
```

若 readback 失敗：

```text
persistence.status = uncommitted
```

不得宣稱已存檔，也不得默默用聊天記憶代替 authoritative storage。

---

## 8. 啟動完成條件

只有以下全部成立後，才把控制權交回一般 DM runtime：

```text
campaign root resolved
manifest loaded / created
manifest exact ref / unique resolution verified
storage capability verified
ruleset immutable commit SHA resolved and readable
party mode resolved
world-resolution mode resolved
character bootstrap path resolved
current authoritative state loaded or initialized
persistence readback verified
```

否則保持 bootstrap state，不生成正式場景。

---

## 9. Legacy state

根目錄舊有：

```text
campaign/
characters/
sessions/
mystery_vault/
```

屬 migration 前的 legacy storage，不是 default campaign。

若使用者要讀舊團，先建立／解析對應 legacy migration plan 或 manifest；不要只因最近一份 session 看起來完整就自動選它。
