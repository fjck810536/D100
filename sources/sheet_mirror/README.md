# D100 Google Sheet Canon Mirror

此目錄是上游 `D100專長表` 的**唯讀來源鏡像**，snapshot date：`2026-09-12`。

- Source Sheet ID: `1d4nl6ByhbEtOhutjlB6FYrMVzglKG7I5DuanO0l4Mww`
- Source status: `[D100_CANON]`
- Google Sheet 僅做唯讀匯出；沒有修改內容、分享設定或權限。
- 鏡像由匯出的 `.xlsx` 逐格讀取，保留原值、公式、換行、錯字、舊 D&D 3.5 用語與表格遺留內容；`null` 代表空白儲存格。
- **鏡像層不負責修正來源。** 若來源本身矛盾，應依 repo 的優先序、Patch note 與 open questions 顯式處理，不可偷偷正規化。

## 使用方式

實際跑團時，優先使用 `00_core/`、`01_skills/`、`02_items/` 等已整理規則；當需要：

- 核對原文；
- 查尚未整理進核心文件的職業／專長／物品／詞綴；
- 判斷某條規則是否其實已存在於 Sheet；
- 檢查版本衝突或來源 provenance；

再由 `sources/SHEET_INDEX.md` 導航到本目錄的對應 mirror。

**在把問題標成 `[OPEN_QUESTION]` 或向 GM 追問以前，先搜尋本目錄。**

## 31 tabs → mirror files

| # | Google Sheet tab | Mirror |
|---:|---|---|
| 1 | 創角色須知 | `00_character_creation.json.md` |
| 2 | 施法者創角須知 | `00_character_creation.json.md` |
| 3 | 種族與其調整 | `00_character_creation.json.md` |
| 4 | 世界觀 | `01_world_core.json.md` |
| 5 | 大陸簡史 | `01_world_core.json.md` |
| 6 | 基本專長 | `02_基本專長.json.md` |
| 7 | 一般專長 | `03_一般專長.json.md` |
| 8 | 製作專長 | `04_製作專長_to_超魔專長.json.md` |
| 9 | 超魔專長 | `04_製作專長_to_超魔專長.json.md` |
| 10 | 高級專長 | `05_高級專長_to_傳奇專長.json.md` |
| 11 | 傳奇專長 | `05_高級專長_to_傳奇專長.json.md` |
| 12 | 德魯伊結社 | `06_德魯伊結社.json.md` |
| 13 | 法師學派專精 | `07_法師學派專精.json.md` |
| 14 | 術士 | `08_術士.json.md` |
| 15 | 吟遊詩人特殊專長 | `09_吟遊詩人特殊專長.json.md` |
| 16 | 牧師領域 | `10_牧師領域.json.md` |
| 17 | 特殊職業1 | `11_特殊職業1.json.md` |
| 18 | 特殊職業2 | `12_特殊職業2.json.md` |
| 19 | 特殊職業(武僧) | `13_特殊職業_武僧_.json.md` |
| 20 | 特殊職業(warlock) | `14_特殊職業_warlock_.json.md` |
| 21 | 狩獵任務 | `15_狩獵任務.json.md` |
| 22 | 魔法物品價格表 | `16_魔法物品價格表.json.md` |
| 23 | 詞墜(依物品分類) | `17_詞墜_依物品分類_.json.md` |
| 24 | 一般詞綴 | `18_一般詞綴.json.md` |
| 25 | 高階詞綴 | `19_高階詞綴.json.md` |
| 26 | 素材詞綴 | `20_素材詞綴.json.md` |
| 27 | 永恆聖器詞綴 | `21_永恆聖器詞綴.json.md` |
| 28 | Patch note | `22_Patch_note_to_FATE特規.json.md` |
| 29 | FATE特規 | `22_Patch_note_to_FATE特規.json.md` |
| 30 | 戰鬥流程 | `01_world_core.json.md` |
| 31 | 法師範例 | `01_world_core.json.md` |

## 判讀原則

1. 原始 mirror 是 provenance layer，不是已整理的 Player Handbook。
2. Patch note 與較新的明文若和舊條目衝突，依 `sources/SHEET_INDEX.md` 與 repo precedence 處理。
3. 表內仍可能存在 3.5 頁碼、技能名稱、舊公式或未同步欄位；保留它們是為了可追溯性，不代表可無條件套用。
4. 若 curated core 與 mirror 看似衝突，先確認是否為 Patch note、整理錯誤或尚未釐清的版本差異，再決定是否更新核心文件。
