# 上游 D100 Google Sheet 索引

上游正典：

`https://docs.google.com/spreadsheets/d/1d4nl6ByhbEtOhutjlB6FYrMVzglKG7I5DuanO0l4Mww/edit`

建立與更新本 repo 時僅做**唯讀查閱／匯出**，沒有修改任何 Sheet 內容、分享設定或權限。

## 1. Source mirror 狀態

截至 `2026-09-12`，Google Sheet 的 **31 / 31 個 tabs 已完整建立 raw canonical mirror**：

- 導覽：`sources/sheet_mirror/README.md`
- 資料：`sources/sheet_mirror/*.json.md`
- 來源標記：`[D100_CANON]`

mirror 是 provenance layer：逐格保存來源值、公式、換行、錯字、舊 3.5 術語與表格遺留內容，不在 mirror 階段偷偷修正。

> **重要：在把規則標成 `[OPEN_QUESTION]`、套用 `[DM_DEFAULT]`／`[SRD_BRIDGE]`，或向 GM 追問以前，先搜尋 `sources/sheet_mirror/`。**

實際跑團仍優先閱讀已整理的 `00_core/`、`01_skills/`、`02_items/`；raw mirror 用來補完未整理內容與核對原文。

## 2. Tab 清單與 mirror 導航 `[D100_CANON source map]`

| # | Tab | Mirror |
|---:|---|---|
| 1 | 創角色須知 | `sheet_mirror/00_character_creation.json.md` |
| 2 | 施法者創角須知 | `sheet_mirror/00_character_creation.json.md` |
| 3 | 種族與其調整 | `sheet_mirror/00_character_creation.json.md` |
| 4 | 世界觀 | `sheet_mirror/01_world_core.json.md` |
| 5 | 大陸簡史 | `sheet_mirror/01_world_core.json.md` |
| 6 | 基本專長 | `sheet_mirror/02_基本專長.json.md` |
| 7 | 一般專長 | `sheet_mirror/03_一般專長.json.md` |
| 8 | 製作專長 | `sheet_mirror/04_製作專長_to_超魔專長.json.md` |
| 9 | 超魔專長 | `sheet_mirror/04_製作專長_to_超魔專長.json.md` |
| 10 | 高級專長 | `sheet_mirror/05_高級專長_to_傳奇專長.json.md` |
| 11 | 傳奇專長 | `sheet_mirror/05_高級專長_to_傳奇專長.json.md` |
| 12 | 德魯伊結社 | `sheet_mirror/06_德魯伊結社.json.md` |
| 13 | 法師學派專精 | `sheet_mirror/07_法師學派專精.json.md` |
| 14 | 術士 | `sheet_mirror/08_術士.json.md` |
| 15 | 吟遊詩人特殊專長 | `sheet_mirror/09_吟遊詩人特殊專長.json.md` |
| 16 | 牧師領域 | `sheet_mirror/10_牧師領域.json.md` |
| 17 | 特殊職業1 | `sheet_mirror/11_特殊職業1.json.md` |
| 18 | 特殊職業2 | `sheet_mirror/12_特殊職業2.json.md` |
| 19 | 特殊職業(武僧) | `sheet_mirror/13_特殊職業_武僧_.json.md` |
| 20 | 特殊職業(warlock) | `sheet_mirror/14_特殊職業_warlock_.json.md` |
| 21 | 狩獵任務 | `sheet_mirror/15_狩獵任務.json.md` |
| 22 | 魔法物品價格表 | `sheet_mirror/16_魔法物品價格表.json.md` |
| 23 | 詞墜(依物品分類) | `sheet_mirror/17_詞墜_依物品分類_.json.md` |
| 24 | 一般詞綴 | `sheet_mirror/18_一般詞綴.json.md` |
| 25 | 高階詞綴 | `sheet_mirror/19_高階詞綴.json.md` |
| 26 | 素材詞綴 | `sheet_mirror/20_素材詞綴.json.md` |
| 27 | 永恆聖器詞綴 | `sheet_mirror/21_永恆聖器詞綴.json.md` |
| 28 | Patch note | `sheet_mirror/22_Patch_note_to_FATE特規.json.md` |
| 29 | FATE特規 | `sheet_mirror/22_Patch_note_to_FATE特規.json.md` |
| 30 | 戰鬥流程 | `sheet_mirror/01_world_core.json.md` |
| 31 | 法師範例 | `sheet_mirror/01_world_core.json.md` |

## 3. Curated core 已覆蓋的主要區域

- `創角色須知` → `00_core/character_creation.md`
- `施法者創角須知` → `00_core/magic.md`
- `基本專長` 核心索引 → `01_skills/core_skills.md`
- `一般專長` 的 DM 核心接口 → `01_skills/core_skills.md`、combat/magic/resistance files
- `戰鬥流程` → `00_core/combat.md`
- `永恆聖器詞綴` 的神器級語義 → `02_items/artifacts.md`
- `Patch note` 核心更動 → 各 core 與 open questions

其餘 tab 雖已在 raw mirror 中完整可查，**不代表都已轉寫成 curated player-facing / DM-facing 規則章節**。後續整理應以 mirror 作來源，不必再依賴即時讀取 Google Sheet。

## 4. Patch note 已確認的重要規則

### v1.1

- 總施法者等級：`本身環數×3 + 其他技能／專長／裝備變動值`
- 近戰／法術 CP 投資獎勵 HP/SP 可累算
- CP 額外購買 HP/SP 時，不把獎勵 HP/SP 算進該基礎門檻
- 所有擲骰結果（技能、攻擊、傷害等）有小數時，`>= 0.5` 一律進位

### v1.2

- 加入充能球系統
- 裝備系統增加詞綴上限；神器／次神器不受一般限制
- 新增特殊通貨
- 特殊通貨判定無法用 CP 重骰
- 增加高階技能／專長

### v1.2 nerf

- 快速射擊不可與多重射擊累算
- 燕返改為判定後仍需分別做三次武器使用檢定
- 崇高石價值修正

### v1.3 buff

- 法術專精調整
- 武器使用公式中的魔法武器變動改為 `魔法物品加值 / 2`

## 5. 版本衝突處理

如果舊 tab 條文與 Patch note 明文衝突：

```text
較新的 Patch note > 舊條文
```

若核心 tab 已把 Patch note 修改整合進最新文字，直接使用最新文字；不要重複套用同一修正。

若 curated core 與 raw mirror 看似衝突，先檢查：

1. 是否是 Patch note 已覆寫舊條文；
2. 是否是 core 整理錯誤；
3. 是否是來源本身矛盾；
4. 是否已有 `[GM_PROVISIONAL]` 釐清。

仍無法確定才標 `[OPEN_QUESTION]`。

## 6. 來源狀態標籤

repo 使用：

- `[D100_CANON]`
- `[D100_DERIVED]`
- `[GM_PROVISIONAL]`
- `[GM_UNCERTAIN]`
- `[GM_UNANSWERED]`
- `[GM_SECRET]`
- `[DM_DEFAULT]`
- `[SRD_BRIDGE]`
- `[OPEN_QUESTION]`

raw mirror 內容屬 `[D100_CANON]` 來源文本；對其做出的推論仍需另行標示，不可因為「從正典推導」就冒充原文。
