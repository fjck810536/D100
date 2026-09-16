# campaign_instances/

Repository-local campaign storage backend 的路徑約定；相對於玩家**明確選定且可寫的 repository**。

這個目錄不是新的世界正典；它只是當使用者選擇 `storage.backend: repo` 時，用來放**彼此隔離的 campaign save instances**。

公開 upstream `fjck810536/D100` 提供 rules/source；這裡不是外部玩家共用的存檔服務。能瀏覽 GitHub／Pages 不代表能寫入。使用 upstream 中的新 namespace，需明確選定並驗證當前身份對目標 repository／branch 的 READ + CREATE + UPDATE 權限；不能從「有 connector」「能 fork／提 PR」或「本機 clone 可寫」推定。

外部玩家通常應將存檔放在自己的 Git repo、Google Drive，或可持續保存與重新掛載的 local/mounted folder。依 `CAMPAIGN_STORAGE_PROTOCOL.md` 驗證 selected root 的能力並保存 stable refs，`ruleset.repository` 仍可指向 upstream。一次性 scratch 不構成持久 backend。

邏輯形狀：

```text
campaign_instances/
├── <campaign-id-a>/
│   ├── manifest.md
│   ├── current_state.md
│   ├── characters/
│   ├── sessions/
│   ├── sites/
│   ├── relationships/
│   ├── commitments/
│   └── mystery/
└── <campaign-id-b>/
    └── ...
```

## 核心規則

- 每一團必須有自己的 `campaign_id` 與 manifest。
- Runtime 未先選定 manifest 前，不得掃描本目錄後自行猜「最新那團」。
- 只讀寫 selected campaign root。
- `persistent_test` 與正式 `persistent_campaign` 可使用完全相同結構；差別寫在 manifest 的 `runtime_mode` / `promotion_allowed`，不是靠資料缺失區分。
- 不得將 `campaign_instances/<A>/characters/` 的角色主檔拿去補 `<B>` 的 session。
- 根目錄舊 `campaign/`、`characters/`、`sessions/`、`mystery_vault/` 屬 legacy storage，須經 migration 才進入這裡。

## 建立新 instance

依：

- `BOOTSTRAP_PROTOCOL.md`
- `CAMPAIGN_STORAGE_PROTOCOL.md`
- `templates/CAMPAIGN_MANIFEST_TEMPLATE.md`

建立。

各 backend 向 runtime 呈現相同 logical namespace；Google Drive mapping 見 `storage_backends/GOOGLE_DRIVE.md`，Git / folder 依既有 logical API 驗證實際可用性。能力不足時保留 wizard 選項並改選／接通可寫位置，再接續初始化。
