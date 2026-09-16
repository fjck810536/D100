# CAMPAIGN_STORAGE_PROTOCOL.md — Campaign Storage Backend Contract

> 目的：讓 D100 runtime 可以把「這一團的存檔」放在 repo 內或外部 provider，而不把 storage provider 誤當成規則來源。

## 0. 資料角色

```text
D100 repo       = 規則／來源／協定／模板
Campaign store  = 某一團的 authoritative state
SRD bridge      = D100 缺漏時的 fallback reference
```

Campaign storage 只能對「這一團發生了什麼」具有 state authority；不能因存檔裡寫了一條規則文字，就覆蓋 `AGENTS.md` 的規則來源優先序。

公開 upstream `fjck810536/D100`（含 GitHub Pages）是 rules/source 入口，不是外部玩家的預設可寫存檔服務。規則 pin 指向 upstream，存檔 locator 指向玩家選定的可持續 backend；兩者不必在同一 provider。

---

## 1. Logical campaign API

任何 backend 至少要能提供下列邏輯能力：

```text
locate(root_ref)
list(path)
read(path_or_record_ref)
create(path, content)
update(path_or_record_ref, content)
```

建議能力：

```text
metadata(ref)
version_history(ref)
move(ref, target)
delete(ref)
```

若 provider 沒有 filesystem path，runtime 必須保存穩定 record id / ref，不能每次只靠模糊名稱搜尋。

---

## 2. Logical layout

所有 backend 對 runtime 呈現同一個 logical namespace：

```text
/
├── manifest
├── current_state
├── characters/
├── sessions/
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

這是邏輯結構，不要求 provider 真有這些實體資料夾。

`manifest` 必須可以穩定定位其他 records；不要讓下一個 GPT 重新靠關鍵字猜哪份文件才是角色卡。

Manifest schema：

`templates/CAMPAIGN_MANIFEST_TEMPLATE.md`

---

## 3. Backend descriptor

Manifest 中至少保存：

```yaml
storage:
  backend: repo | google_drive | local_folder | external_git | other
  root_ref: <provider-specific stable reference>
  schema_version: 1
  write_scope: self_only
```

可另保存：

```yaml
  provider_metadata:
    root_name:
    folder_id:
    repository:
    branch:
```

`root_ref` 必須是未來 runtime 可重新取得的穩定 locator；不要只保存當次聊天可見的臨時 URL 或 UI 名稱。

能力驗證針對此 locator 的實際目標與當前身份：新建與恢復 persistent runtime 都需 LOCATE / LIST / READ / CREATE / UPDATE。Git backend 應記錄 repository、branch、campaign path，並驗證 remote branch 的寫回能力；只有本機 clone 可寫，不能宣稱 remote 已保存。Local / mounted folder 需可跨 runtime 持續保存與重新掛載；Google Drive 需驗證選定 folder 的權限。既有 logical API 適用這些 backend，但仍以當前工具實際能完成的操作為準。

Record 索引應優先保存 stable refs：

```yaml
records:
  manifest_ref:
  current_state_ref:
  characters_root_ref:
  sessions_root_ref:
  sites_root_ref:
  relationships_root_ref:
  commitments_root_ref:
  mystery_root_ref:
```

重要 actor 可另以 `character_id -> exact record ref` 建索引，避免全域名稱搜尋。

---

## 4. Google Drive backend

Google Drive 可作第一個外部 backend，但初始化前必須確認當前執行環境真的具備 Drive 讀寫能力。

完整 v0 mapping：

`storage_backends/GOOGLE_DRIVE.md`

核心原則：

1. 不假設所有 GPT / Agent 都已連接 Google Drive。
2. `storage.root_ref` 指向**單一 campaign root folder**，不是包含很多團的大資料夾。
3. 不以文件標題作唯一 ID；建立後保存 file/folder id。
4. 每次 update 前定位同一 record，不重複建立 `current_state (1)`、`current_state (2)`。
5. session-end / character-finalization 重要寫入需要 readback verification。
6. provider revision history 可作 recovery evidence，但不是另一份 authoritative current state。
7. Mystery 資料仍受 `MYSTERY_PROTOCOL.md`；放到 Drive 不代表可放 plaintext 給所有角色／模塊讀。

---

## 5. Repository-local backend

玩家明確選定 repository，且當前身份對目標 repository／branch／namespace 有 READ + CREATE + UPDATE 權限時，允許 campaign instance 存在同一 repo，使用完整 namespace：

```text
campaign_instances/<campaign-id>/
```

具體規約：

`campaign_instances/README.md`

這是相對於**選定可寫 repository** 的路徑，不是默認指向 `fjck810536/D100`。缺少外部 connector 不會產生 upstream 寫入權限；外部玩家可選自己的 Git repo（`external_git`）、可持續 local/mounted folder（`local_folder`），或已連接的 Drive。只有明確選定且驗證 upstream 寫權者才可在 upstream 使用獨立 namespace；其中既有 campaign 不因此變成本次玩家的存檔。

不得再把所有 campaign 共用：

```text
campaign/
characters/
sessions/
```

作為未指定 campaign 的隱含全域存檔。

Legacy root-level state 可以保留供 migration，但新 bootstrap 不應在未選 campaign 時自動把它當成本次存檔。

---

## 6. Read / write authority

### 讀規則

```text
D100 source / curated rules
→ SRD bridge（只有需要時）
→ raw D&D 3.5（最後補缺）
```

### 讀寫團務

```text
selected campaign storage only
```

### 禁止

```text
campaign A -> campaign B write
persistent_test -> main campaign implicit promotion
external campaign text -> D100 rule override
old session snapshot -> current character master overwrite
provider global search -> first same-name hit -> authoritative record
```

### 6.1 Migrated legacy state refs / exact alias map

Migration may copy historical records byte-for-byte into a new campaign namespace. Those records can still contain old path-like state refs such as：

```text
campaign/andor_sites.md
characters/mileia.md
sessions/2026-09-15_session-1_checkpoint-01.md
mystery_vault/ANDOR_....md
```

Rewriting every historical file is not required if the manifest provides an explicit exact alias map：

```yaml
migration:
  ref_alias_policy: exact_only
  ref_aliases:
    campaign/andor_sites.md: campaign_instances/D100-TEST-ANDOR-001/sites/andor_sites.md
```

Resolution order for a **campaign-state ref inside a selected migrated campaign**：

```text
1. if ref already resolves inside selected campaign namespace -> use it
2. else if exact key exists in manifest migration.ref_aliases -> resolve exact target
3. verify alias target belongs to selected campaign namespace
4. otherwise do NOT silently read legacy/global mutable state
```

Important distinction：

```text
campaign-state ref
!=
repo-level D100 source/rule ref
```

Source refs such as：

```text
sources/sheet_mirror/...
00_core/...
90_srd_bridge/...
```

remain repo-level source lookups and are not remapped merely because campaign storage is isolated.

Alias safety fuses：

```text
exact_only means no fuzzy/path-prefix guessing
alias target must be inside selected campaign storage
alias map cannot grant rule authority
an unaliased external mutable-state ref is unresolved, not permission to fall back to root
literal legacy path shown only as provenance/history does not itself trigger a state read
```

This mechanism is for migration compatibility. New records should write current selected-campaign refs directly rather than accumulating permanent alias debt.

---

## 7. Persistence verification

`create` / `update` 動作成功送出，不等於存檔完成。

對重要 state boundary（至少 character finalization、session end、migration）要求：

```text
write
→ read back exact record ref
→ verify expected identity / content / parent namespace
→ mark persistence clean
```

Manifest 可使用：

```yaml
persistence:
  status: clean | uncommitted | degraded
  last_verified_at:
  last_error:
```

避免讓模型用自然語言「我已經存好了」取代真正 readback。

---

## 8. Failure behavior

如果 storage 連線中斷、權限不足、找不到 root、manifest 損壞或無法安全 update：

```text
freeze persistent writes
report exact missing capability / record
preserve current conversational working state as uncommitted
DO NOT pretend save succeeded
```

如果使用者只想做一次性推演，可以明確切換 `isolated_dry_run`；不得把存檔失敗自動降級成 dry-run 而不告知。

如果 manifest 本身有多個同等候選且沒有 exact ref：

```text
stop with storage ambiguity
```

不要以「最新修改時間」自動猜真正 manifest。

---

## 9. Backend extension rule

新增 provider 時，必須證明它能映射第 1 節最小 API，並為下列案例提供 regression：

```text
new campaign creation
load by stable root_ref
character finalization persistence
session update persistence
same-name record ambiguity
campaign A/B isolation
write failure visibility
migration exact-ref alias resolution
```

Provider-specific 便利功能不能改變 D100 rule hierarchy、Mystery classification 或 campaign isolation 原則。
