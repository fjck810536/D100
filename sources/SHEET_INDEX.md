# 上游 D100 Google Sheet 索引

上游正典：

`https://docs.google.com/spreadsheets/d/1d4nl6ByhbEtOhutjlB6FYrMVzglKG7I5DuanO0l4Mww/edit`

建立本 repo 時僅做**唯讀查閱**，沒有修改任何 Sheet 內容、分享設定或權限。

## 1. Tab 清單 `[D100_CANON source map]`

1. 創角色須知
2. 施法者創角須知
3. 種族與其調整
4. 世界觀
5. 大陸簡史
6. 基本專長
7. 一般專長
8. 製作專長
9. 超魔專長
10. 高級專長
11. 傳奇專長
12. 德魯伊結社
13. 法師學派專精
14. 術士
15. 吟遊詩人特殊專長
16. 牧師領域
17. 特殊職業1
18. 特殊職業2
19. 特殊職業(武僧)
20. 特殊職業(warlock)
21. 狩獵任務
22. 魔法物品價格表
23. 詞墜(依物品分類)
24. 一般詞綴
25. 高階詞綴
26. 素材詞綴
27. 永恆聖器詞綴
28. Patch note
29. FATE特規
30. 戰鬥流程
31. 法師範例

## 2. 目前已鏡像進 repo 的範圍

### 核心已覆蓋

- `創角色須知` → `00_core/character_creation.md`
- `施法者創角須知` → `00_core/magic.md`
- `基本專長` 核心索引 → `01_skills/core_skills.md`
- `一般專長` 中 DM 核心接口 → `01_skills/core_skills.md`、combat/magic/resistance files
- `戰鬥流程` → `00_core/combat.md`
- `永恆聖器詞綴` 的神器級語義 → `02_items/artifacts.md`
- `Patch note` 核心更動 → 各 core 與 open questions
- `種族與其調整` 的部分範例 → 用於核對五抗與特殊能力語義

### 尚未完整鏡像

下列內容仍需後續分批移植；GPT 不可假裝 repo 已經包含完整原文：

- 全種族細節
- 世界觀
- 大陸簡史
- 製作專長
- 完整一般專長
- 超魔專長
- 高級／傳奇專長
- 德魯伊結社
- 法師學派專精
- 術士完整能力
- 吟遊詩人特殊專長
- 牧師領域
- 特殊職業
- 狩獵任務
- 完整魔法物品價格
- 全詞綴資料庫
- FATE 特規
- 法師範例

## 3. Patch note 已確認的重要規則

### v1.1

- 總施法者等級改為：`本身環數×3 + 其他技能／專長／裝備變動值`
- 近戰／法術 CP 投資獎勵 HP/SP 可累算
- CP 額外購買 HP/SP 時，不把獎勵 HP/SP 算進該基礎門檻
- **所有擲骰結果（技能、攻擊、傷害等）有小數時，>=0.5 一律進位**

### v1.2

- 加入充能球系統
- 裝備系統增加詞綴上限；來源說明「神器與次神器」不受一般限制
- 新增特殊通貨
- **特殊通貨判定無法用 CP 重骰**
- 增加高階技能／專長

### v1.2 nerf

- 快速射擊不可與多重射擊累算
- 燕返改為判定後仍需分別做三次武器使用檢定
- 崇高石價值修正

### v1.3 buff

- 法術專精調整
- 武器使用公式中的魔法武器變動改為 `魔法物品加值 / 2`

## 4. 版本衝突處理

如果舊 tab 條文和 Patch note 明文衝突：

```text
較新的 Patch note > 舊條文
```

但若核心 tab 顯然已把 Patch note 的修改整合進最新文字，直接使用最新核心 tab；不要重複套用修正兩次。

## 5. 來源引用原則

repo 內每個規則盡量標示：

- `[D100_CANON]`
- `[D100_DERIVED]`
- `[DM_DEFAULT]`
- `[SRD_BRIDGE]`
- `[OPEN_QUESTION]`

如果之後把整個 tab 逐條轉成 Markdown，建議保留：

```yaml
source_sheet: D100專長表
source_tab: 基本專長
source_status: D100_CANON
```

如此 GPT 才能知道哪一段是真的來源、哪一段是整理者推論。
