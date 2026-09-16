# CAMPAIGN_STORAGE_PROTOCOL.md — Campaign Storage Backend Contract

> 目的：讓 D100 runtime 可以把「這一團的存檔」放在 repo 內或外部 provider，而不把 storage provider 誤當成規則來源。

## 0. 資料角色

```text
D100 repo       = 規則／來源／協定／模板
Campaign store  = 某一團的 authoritative state
SRD bridge      = D100 缺漏時的 fallback reference
```

Campaign storage 只能對「這一團發生了什麼」具有 state authority；不能因存檔裡寫了一條規則文字，就覆蓋 `AGENTS.md` 的規則來源優先序。

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

---

## 4. Google Drive backend v0 contract

Google Drive 可作第一個外部 backend，但初始化前必須確認當前執行環境真的具備 Drive 讀寫能力。

建議映射：

```text
Campaign root folder
├── manifest                  Google Doc / text-capable record
├── current_state             Google Doc / text-capable record
├── characters               folder
├── sessions                 folder
├── sites                    folder
├── relationships            folder
├── commitments              folder
└── mystery                  folder or protected records according to Mystery rules
```

重要限制：

1. 不假設所有 GPT / Agent 都已連接 Google Drive。
2. 不以文件標題作唯一 ID；建立後必須保存 file/folder id。
3. 每次 update 前先定位同一 record，不重複建立 `current_state (1)`、`current_state (2)`。
4. provider revision history 可以作 recovery evidence，但不是另一份 authoritative current state。
5. Mystery 資料仍受 `MYSTERY_PROTOCOL.md`；放到 Drive 不代表可放 plaintext 給所有角色／模塊讀。

---

## 5. Repository-local backend

為開發、測試與不具外部 connector 的環境，允許 campaign instance 暫存於同一 repo，但必須有完整 namespace，例如：

```text
campaign_instances/<campaign-id>/
```

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
```

---

## 7. Failure behavior

如果 storage 連線中斷、權限不足、找不到 root、manifest 損壞或無法安全 update：

```text
freeze persistent writes
report exact missing capability / record
preserve current conversational working state as uncommitted
DO NOT pretend save succeeded
```

如果使用者只想做一次性推演，可以明確切換 `isolated_dry_run`；不得把存檔失敗自動降級成 dry-run 而不告知。
