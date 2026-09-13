# SESSION_STATE_TEMPLATE.md

> 複製為 `sessions/YYYY-MM-DD_session-N.md`。本檔是 GPT 在長團中避免失憶與狀態漂移的主要容器。
>
> 本檔只保存「目前真的成立的 session state」與合法的 Mystery references；不得另建 plaintext DM secret store。架構見 `../DATA_ARCHITECTURE.md`、`../MYSTERY_PROTOCOL.md`。

```yaml
session_id:
date:
scene:
in_combat: false
round:
world_time:
```

## 當前場景

### 地點

### 可見／可聽／可感知資訊

### Secret refs

```yaml
secret_refs: []
```

> 只記 `Secret ID` 與此 session 合法取得的 role-safe view。完整 protected payload 若屬 Mystery Vault，不得複製進 session state。

## PC 即時狀態

| PC | HP | SP | 位置 | 姿勢 | 持續效果 | 備註 |
|---|---:|---:|---|---|---|---|

## NPC / 怪物

| 名稱 | HP | SP | 位置 | 狀態 | 敵對？ | 備註 |
|---|---:|---:|---|---|---|---|

> NPC 的 belief / knowledge 若需要持久化，記錄實際 belief state 或對應 Entity ref；不要把分析師／生態學家的暫時推測寫成既定人格真相。

## 戰鬥順位

### 行動順序

```text
1.
2.
3.
```

### 宣告順序

```text
1.  # 早宣告
2.
3.  # 晚宣告
```

## 本輪宣告

| 角色 | 宣告 | 動作類型 | 是否已執行 |
|---|---|---|---|

## 即時／瞬唱使用權

| 角色 | 法術瞬唱 | 即時動作種類 | 已用？ |
|---|---|---|---|

## DOT / Buff / Debuff

| 對象 | 效果 | 來源體系 | 剩餘輪數/時間 | 每輪處理 |
|---|---|---|---|---|

> 注意：D100 戰鬥一輪 = 1 秒。

## 連續施法追蹤

| 施法者 | 上次成功法術 | 環數 | 目前連續施法懲罰 |
|---|---|---:|---:|

## 藥水負荷

| 角色 | 最近5輪計入數量 | CON承受上限 | 是否需抗毒 |
|---|---:|---:|---|

## 隱藏判定

| 對象 | 判定 | 數值 | D100 | 結果 | 玩家知道嗎？ |
|---|---|---:|---:|---|---|

> 「秘密擲骰」不等於「秘密 payload」。骰值與結果可放 session state；其背後尚未授權的秘密內容仍只以 `secret_refs` 連接 Mystery。

## 調查資訊階梯

### 物件／事件：

- 存在：
- 定位：
- 分類：
- 理解：
- 處置：

### 玩家目前已取得

## 神器／詛咒／轉化進度

| 對象 | 機制／Secret ref | 階段 | 已觸發 | 已知資訊 |
|---|---|---:|---|---|

## Triggered Hazard / Object State

| Hazard ref | Armed | Triggered | Cooldown / Reset | 備註 |
|---|---|---|---|---|

> 詳細結構見 `TRIGGERED_HAZARD_TEMPLATE.md`；session 只追 live state，不重複整份 statblock。

## 本次臨時裁定

| 問題 | 裁定 | 標籤 | 下次是否需確認 |
|---|---|---|---|

可用標籤：

- `[D100_CANON]`
- `[D100_DERIVED]`
- `[DM_DEFAULT]`
- `[SRD_BRIDGE]`
- `[OPEN_QUESTION]`

## Derived cache refs

```yaml
derived_refs: []
```

> 可連到 combat doctrine、threat model、political forecast 等昂貴推理結果，但 derived cache 不是 world fact；底層 state 改變時必須失效／重算。

## 世界狀態改變

## 戰利品／CP／金錢變動

## Session 結束快照

### PC

### NPC

### 未完成事件

### 下次開場必讀
