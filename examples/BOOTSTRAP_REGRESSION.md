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

---

## T19 — Public entry resolves main once, not a floating pin

Given: 玩家從 Pages／main 啟動新團，未指定版本；建立時 HEAD=A，之後 HEAD=B；沒有 release tag。

Expected:
- `ruleset.ref=A`、`resolved_commit_sha=A`，均保存完整 commit SHA；`version_label` 可留空，前台可顯示短 SHA。
- 初始化與重載的規則／協定／模板讀取都使用 A；若啟動曾讀 main，按 A 重讀 runtime 所需文件。
- 存檔 backend 另行選定；不因 ruleset 指向 upstream 而推定 storage。

Fail if: pin 寫成 `main`／`latest`，每次重解 HEAD，或為了沒有 tag 阻擋新團。

---

## T20 — Release label is not the immutable pin

Given: 玩家選擇 release tag `v-test`，指向 commit A；分別測 lightweight 與 annotated tag。建立後 tag 移到 B 或被刪除，但 A 仍可讀。

Expected:
- 建立時保存原 ref／可選顯示名稱與 `resolved_commit_sha=A`；annotated tag 解到 commit，不保存 tag object SHA 作 pin。
- 重載仍讀 A，標籤變動不更新 campaign pin，也不阻擋讀取仍可用的 A。

Fail if: 把 tag 當 immutable，或讀今天的 tag 指向而默默改成 B。

---

## T21 — Existing manifests keep their version and state

Given: 舊 manifest 只有完整 SHA `ref=A`，沒有新欄位；另測只有 release ref 的舊 manifest。

Expected:
- SHA-only manifest 直接載入 A，不需補欄位，不改既有 state。
- Release-only manifest 用建立時的版本證據確認 A，再依 explicit migration 補記；證據不足時請求原始 SHA 或明確選擇 migration。
- 若兩個 SHA 欄位互相矛盾，先釐清 manifest／migration，不猜版本。

Fail if: 為了新欄位強制升級舊團，或把 release 今天指向的 B 當作原始 A。

---

## T22 — Public upstream is not a public save service

Given: 外部玩家能讀 upstream／Pages；對 upstream 有 READ，但沒有 CREATE / UPDATE。已完成 A/B/C，要求「存 repo-local」。

Expected:
- 解釋 upstream 只提供規則／來源，取得玩家自己的 Git repo、Drive 或持久 folder locator。
- 保留 A/B/C；對選定目標驗證能力，成功後接續初始化與 readback。
- 不寫 upstream `campaign_instances/`，不選取 upstream 既有團，也不把 Pages 當存檔 API。

Fail if: 只回「不能」而沒有可接續的 backend 路徑，或憑公開可讀／有 connector 宣稱存檔成功。

---

## T23 — Explicitly writable upstream namespace still works

Given: 使用者明確選定 upstream 中新的獨立 namespace；當前身份對該 repository／branch 有完整 LOCATE / LIST / READ / CREATE / UPDATE 能力。

Expected: 完成正常 repo-local 初始化與 exact-ref readback，只寫 selected namespace；既有 campaign state 不變。

Fail if: 把「公開 upstream 非預設 storage」擴張成全面禁止有權使用者的 repo-local backend。

---

## T24 — Check the actual storage target, not generic tool access

Given variants:
- 可 fork／提 PR／寫本機 clone，但不能寫 selected remote branch。
- 同一帳號的 repository A 可寫，selected repository B／branch 唯讀。
- local folder 當前可寫，但只是不可跨 runtime 保存的 scratch。
- 玩家自己的 Git remote，或可持續保存並重新掛載的 folder，具備完整 logical API。

Expected: 前三種保留 wizard 選項並取得可用持久 backend；最後一種完成初始化與 exact-ref readback。Git locator 記錄 repository／branch／campaign path，local locator 指向持久路徑。

Fail if: 本機寫檔成功被說成 remote 已保存，或提供了 backend 名稱就宣稱 adapter 可用。

---

## T25 — Reload rechecks target permissions

Given: manifest 的 `storage_capability_verified=true`，但這次身份只有 READ，或 UPDATE 權限已被撤回。

Expected: 顯示缺少的操作，保留選定 campaign，恢復權限或明確遷移後續跑；不把舊 flag 當本次驗證。任何 probe 只在選定且授權的 namespace，不改既有 authoritative state。

Fail if: 先進 persistent scene 再發現不能存、默默改寫 upstream，或自行降成 dry-run。

---

## T26 — An unavailable pin does not fall back to main

Given: manifest pin=A，但目前無法讀取 A；main=B 可讀。

Expected: 回報 A 的存取問題，提供恢復存取或 explicit migration 路徑；不宣稱已載入 A，也不自動用 B 主持。

---

## T27 — External writable storage completes onboarding

Given: 公開 upstream 僅 READ；玩家選定自己的 Drive campaign folder，當前 connector 對此 root 具完整 logical API，且 readback 成功。

Expected:
- 規則仍來自 upstream 的 immutable SHA；manifest／current state／角色主檔只寫所選 Drive root。
- 保存 exact root／record IDs；重載依這些 refs，規則與存檔各自解析。
- 完成 bootstrap 後能進正常 runtime；無須 fork D100 或取得 upstream 寫權。

Fail if: 因 upstream 不可寫而阻擋已具可用 storage 的玩家，或把 Drive save text 升格為規則來源。
