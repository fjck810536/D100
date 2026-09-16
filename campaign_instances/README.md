# campaign_instances/

Repository-local campaign storage backend 的預設根目錄。

這個目錄不是新的世界正典；它只是當使用者選擇 `storage.backend: repo` 時，用來放**彼此隔離的 campaign save instances**。

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

Repo-local backend 只是第一個可直接落地的 provider；未來 Google Drive / local folder / external Git 應向 runtime 呈現相同 logical namespace。
