# Andor Persistent-Test Migration Plan

> Status: PLAN ONLY — DO NOT EXECUTE YET.
>
> 目的：把目前散落在 repo root legacy `campaign/`、`characters/`、`sessions/`、`mystery_vault/` 的 Andor 測試團，安全搬成一個完整、可重掛載、與其他團隔離的 `persistent_test` campaign instance。
>
> 本檔不是 migration execution record；目前不得因它存在就移動、刪除或重新解釋任何 Andor state。

## 0. Target

預定 target semantics：

```yaml
campaign_id: D100-TEST-ANDOR-001
runtime_mode: persistent_test
storage:
  backend: repo
  root_ref: campaign_instances/D100-TEST-ANDOR-001
  write_scope: self_only
  promotion_allowed: explicit_only
```

實際 `ruleset.ref` 應在 migration 執行時，以使用者選定／核准的 D100 ref 寫入；本計畫不先假定。

---

## 1. Why migration is needed

目前 legacy root state 存在已知完整性問題：

```text
campaign/current_state.md
→ 仍可能描述「尚未建立實際 campaign」

sessions/*Andor*
→ 實際已保存 Andor live state / checkpoints / migration snapshots

characters/*
→ 部分 PC 為事後 recovered authoritative_partial records

創角 working history / sessions
→ 曾保存但沒有即時 promotion 的角色資料
```

因此 migration 不能採：

```text
copy root folders wholesale
```

而要先辨識每筆 record 是否真的屬於 Andor、它是 master / live delta / checkpoint / recovery evidence / unrelated legacy data。

---

## 2. Known Andor actor set

目前至少需要盤點：

```text
Elian / 埃利安
Nella
Rook
Aster
Mileia / 米蕾亞
```

Actor inclusion 必須由 Andor session / creation provenance 驗證，不因 root `characters/` 出現其他檔案就全部搬入。

### Critical recovery regression

Mileia：

```text
faith = Lathander / 晨曦之主
domain = Life / 生命領域
```

必須存在 target campaign authoritative character master；不得只留在 migration notes 或 session。

Elian：

- target character master 必須保存 migration 執行時可恢復的完整 established build；
- session 中的 Search / Bluff / HP / SP 只是 live/runtime evidence，不得取代 master；
- `pending_recovery` 欄位在 migration 前若仍無可靠來源，保留 pending_recovery，不重新生成。

---

## 3. Legacy source classes to inventory

執行 migration 前，逐項建立 inventory：

### Actor records

```text
characters/*.md
sources/characters/* relevant dossiers/evidence
character-creation finalization / audit refs
```

### Session records

```text
sessions/*Andor*
latest *_live-state
checkpoint(s)
migration snapshot(s)
```

分類：

```text
live-state = current role-safe pointer
a checkpoint = historical
migration snapshot = historical recovery state
```

不可用較完整的舊 checkpoint 覆蓋後續 live-state。

### World/site records

只搬與 Andor campaign 已建立 world state 有關的 site / map / organization instance records。

Repo source canon 本身不搬：

```text
sources/sheet_mirror/
00_core/
01_skills/
90_srd_bridge/
```

### Mystery / commitments

- inventory Andor-specific secret refs / commitments；
- 完整 payload 仍依 `MYSTERY_PROTOCOL.md`；
- 不因 migration 方便建立 plaintext duplicate secret store。

---

## 4. Migration phases

### Phase A — Inventory only

```text
list candidate legacy records
→ classify campaign ownership
→ classify authority type
→ record provenance
→ NO state move/write yet
```

Required output：一份 migration inventory table。

### Phase B — Build target namespace

建立：

```text
campaign_instances/D100-TEST-ANDOR-001/
├── manifest.md
├── current_state.md
├── characters/
├── sessions/
├── sites/
├── relationships/
├── commitments/
└── mystery/
```

在 source records 未驗證前，target 不開始 scene runtime。

### Phase C — Actor master reconstruction

對每名 PC：

```text
existing authoritative character record
→ creation audit / explicit PL-user declarations
→ Andor session established facts
→ source-backed recovery evidence
→ explicit legacy migration refs
```

建立 target character master，保留：

```text
established
pending_recovery
provenance
live delta boundary
```

不得因 migration 重新創角。

### Phase D — Current world/session pointer

```text
latest valid Andor live-state
+ character masters
+ Andor-specific site/commitment refs
→ target current_state / active_live_session_ref
```

舊 checkpoint 保留歷史身份。

### Phase E — Readback regression

關閉 migration working context後重新從 target manifest 啟動：

```text
manifest
→ current_state
→ all PC masters
→ live session
→ refs
```

至少驗證：

- Mileia 信仰／領域可直接從 actor master 取得；
- Elian 不因 live session 欄位少而縮卡；
- Nella / Rook / Aster 控制模式與既定 actor state 可恢復；
- active camera / location / HP/SP / CP 不倒退；
- Andor sites / commitments 不混入其他測試；
- Mystery role-safe views 正常。

### Phase F — Cutover

只有 Phase E 全通過後：

```text
mark target manifest initialized / persistence clean
→ declare Andor selected campaign root
```

Legacy root records先**不刪除**；標記 migrated / superseded refs，等另一次 cleanup 決策。

---

## 5. Explicit non-goals

此次 migration 不做：

- 重骰任何歷史判定；
- 重建玩家未決定的角色設定；
- 把 recovered partial 偽裝成 original full sheet；
- 將 Andor 升格成正式 main campaign；
- 清理其他 unrelated legacy test data；
- 更新 D100 ruleset；
- 修改世界 canon 以配合 migration。

---

## 6. Stop conditions

遇到以下任一項，停止 cutover：

```text
無法唯一識別最新 Andor live-state
actor master 與 session established facts 有未解硬衝突
Mileia required identity fields 無法可靠回收
manifest refs 無法重新讀取
write/readback verification 失敗
Mystery record ownership 不明
候選 legacy record 可能屬另一個 campaign
```

不要用「看起來最像」消除 storage ambiguity。

---

## 7. Success condition

Migration 完成的判準不是「檔案搬進新資料夾」，而是：

```text
new chat / new agent
→ read D100 repo
→ choose Load Game
→ resolve D100-TEST-ANDOR-001 manifest
→ load exact actor masters + current state + live session
→ resume Andor without chat memory
```

且同時：

```text
另一個 campaign instance 可以存在
→ 不讀到 Andor actor / site / mystery state
```

這兩件事都成立才算 migration 成功。
