# BOOTSTRAP_REGRESSION.md

> 用來測試首次啟動、讀檔、persistent test 與 campaign storage 隔離。若任一案例失敗，不應進入正式 scene runtime。

## T1 — First run must stop at menu

Given:
- GPT / Agent 第一次讀 repo；
- 沒有 selected campaign pointer。

Expected first player-facing output:

```text
D100

1. 新遊戲
2. 讀取存檔
```

Fail if:
- 直接生成酒館／城市／任務；
- 自動載入 root-level legacy session；
- 假設使用者要繼續 Andor 或其他舊團。

---

## T2 — New solo campaign

Player choices:

```text
新遊戲
一人團
完整模式
協助建立角色
```

Expected:
- 尚未開始 scene；
- 詢問 campaign storage；
- storage capability verified；
- manifest created；
- ruleset ref pinned；
- character finalization target points to this campaign's character store。

---

## T3 — Unsupported multiplayer

Player selects multiplayer.

Expected:
- 明確標示目前 unsupported；
- 不假裝已有多人身份隔離；
- 可要求改選其他 party mode。

---

## T4 — Persistent test is not dry-run

Given:

```yaml
runtime_mode: persistent_test
```

Expected:
- 可建立角色、session、site、commitment；
- 可跨聊天重新讀取；
- write_scope=self_only；
- 不修改其他 campaign state。

Fail if:
- 因為名稱含 test 就不保存角色卡；
- 把它降級成 `writeback:false`；
- 自動把內容升格到 main campaign。

---

## T5 — Isolated dry-run remains no-write

Given:

```yaml
execution_mode: isolated_dry_run
writeback: false
```

Expected:
- 完整推演可以發生；
- 不新增／更新 campaign、character、session、map、Mystery state。

Fail if persistent-test 規則讓 dry-run 開始寫檔。

---

## T6 — Mileia faith survives campaign reload

Regression target for `CHARACTER-STATE-PROMOTION-INCIDENT-2026-09-16`.

At character finalization establish at least:

```text
Mileia
faith = Lathander / 晨曦之主
domain = Life / 生命領域
```

Then:

```text
write authoritative character master
verify readback
end session
switch chat / agent
load same campaign from manifest
```

Expected:
- faith/domain recovered from exact authoritative character record；
- 不需要從舊聊天猜測；
- 不需要從 session 反推；
- session snapshot 不是角色主檔。

---

## T7 — Elian full card does not shrink to session projection

Given:
- authoritative Elian card contains full established build；
- live session only mentions Search / Bluff / HP / SP。

Reload campaign.

Expected:
- runtime first reads character master then live state delta；
- omitted session fields do not become unknown / absent；
- old checkpoint cannot overwrite current master or later live state。

Fail if:

```text
session Search=56
→ runtime pretends this is enough to reconstruct the whole build
```

---

## T8 — Campaign A / B isolation

Create two campaign manifests using same D100 ruleset.

Expected:

```text
Campaign A character/state write
!=
Campaign B character/state write
```

Search or bootstrap must not merge same-named NPC / PC solely because both use the same repository source.

---

## T9 — Ruleset and save authority stay separate

Campaign storage contains a note claiming a rule different from D100 canon.

Expected:
- campaign note may be treated as campaign house rule only if explicitly adopted by authorized user/DM；
- otherwise it cannot override D100 rule hierarchy merely because it is in the save store。

Meanwhile current HP / SP / location from campaign state remain authoritative for that campaign.

---

## T10 — Provider unavailable

Player chooses Google Drive but runtime has no valid Drive read/write capability.

Expected:
- initialization stops before scene runtime；
- reports unavailable backend capability；
- offers another supported storage location if available。

Fail if:
- claims save was created；
- silently stores only in chat；
- silently writes into D100 repo root legacy folders。

---

## T11 — Root legacy state is not an implicit campaign

Given:
- repo root still contains historical `campaign/`、`characters/`、`sessions/`；
- no selected campaign manifest exists for this runtime。

Expected:

```text
D100

1. 新遊戲
2. 讀取存檔
```

Fail if:
- runtime chooses the most recently modified root session；
- runtime assumes root characters are the user's current party；
- runtime says "繼續上次" without a selected campaign pointer。

---

## T12 — Character finalization requires master write + readback

Given a newly finalized PC with:

```text
attributes
skills / feats
alignment
CP ledger
languages
faith/domain/training if applicable
HP/SP result
starting equipment
```

Expected:

```text
final validation
→ write selected-campaign character master
→ read back exact record ref
→ verify identity and required fields
→ only then discard creation working data
```

Fail if:
- working data is discarded before successful readback；
- only session summary is saved；
- required identity fields disappear after chat switch。

---

## T13 — Same-name characters do not cross campaigns

Given:

```text
Campaign A: character_id=PC-MILEIA, name=Mileia
Campaign B: name=Mileia, different record or no matching character_id
```

Expected:
- loading A follows A manifest/index exact ref；
- loading B follows B manifest/index exact ref；
- global title search does not select A's Mileia while B is active。

---

## T14 — Google Drive exact-ID load

Given a Drive campaign root with manifest refs:

```yaml
records:
  manifest_ref: <id-m>
  current_state_ref: <id-s>
indexes:
  characters:
    PC-MILEIA: <id-c>
```

Expected load:

```text
root_ref
→ exact manifest
→ exact current state
→ exact PC-MILEIA record
```

Fail if runtime globally searches file titles and uses the first matching result。

---

## T15 — Important write must be verified

Given:
- session-end or character-finalization update reports success；
- follow-up readback cannot find expected content / parent / stable record ID。

Expected:

```yaml
persistence:
  status: uncommitted
```

Runtime reports save failure and does not claim persistence success。

---

## T16 — Ambiguous manifest blocks load

Given:
- selected storage root contains two plausible manifest records；
- no exact `manifest_ref` is available。

Expected:
- stop with storage ambiguity；
- ask user / migration logic to resolve once；
- do not choose newest modified file automatically。

---

## T17 — Ruleset pin does not silently float

Create campaign at D100 ref A. Later repo head becomes ref B.

Expected:
- campaign manifest still points to A；
- runtime reports migration/update need if B is requested；
- it does not silently switch campaign ruleset to B。

---

## T18 — Quick mode does not change rule authority

Given:

```yaml
world_resolution_mode: quick
```

Expected:
- source-resolution effort may be reduced；
- SRD bridge may be used more aggressively where D100 is truly incomplete；
- rule hierarchy remains:

```text
D100 > SRD bridge > raw D&D 3.5
```

Fail if quick mode makes raw 3.5 equal or superior to D100 canon。
