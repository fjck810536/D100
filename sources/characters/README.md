# Current Character Operational Dossiers

> 用途：目前三名現行／近現行 PC 的**角色資料快取／能力索引／證據投影**。
>
> 這些檔案不是 Google Sheet 的替代品，也不是獨立「角色 AI」。Google Sheet／角色卡仍是來源；Dossier 的工作是把容易在 DM 模擬中被漏掉的 Action Palette、法術、獨特能力、魔法物品、live state 分層整理。
>
> 資料與模塊分層見 `../../DATA_ARCHITECTURE.md`。

## 角色輪廓封存

- [Operational Profile v1](./OPERATIONAL_PROFILE_V1.md) — 三名角色目前可用的 capability / behavior evidence 摘要；其中任何「解題傾向」都應視為 evidence / derived seed，不是硬編行為腳本。
- [CP Strength Audit v1](./CP_STRENGTH_AUDIT_V1.md) — 三名角色目前可追溯的 CP 投資強度帳，供 encounter calibration 使用；不是角色本人對戰術的偏好。

## 三名角色

1. [莎緹拉](./SATHERA_OPERATIONAL_DOSSIER.md)
   - 術士／阿薩托斯系特殊存在。
   - capability 重點：即刻備戰、一心二用、法術瞬唱、次元／禁空／解析弱點工具、極端劇情能力與大量屬性裝備。

2. [亞黛兒](./ADELE_OPERATIONAL_DOSSIER.md)
   - 黑魔導／白魔導／吟遊多施法體系。
   - capability 重點：即時治療、護罩、戰歌、聖域、星空／萬門改位、回捲回合、每日次數回復、三套法術書與大量特殊物件。

3. [卡蘭德](./KALAND_OPERATIONAL_DOSSIER.md)
   - 法師／變化專精／高階魔法物品製作者。
   - capability 重點：即刻備戰、一心二用、瞬步、空間跳躍、變化系CL、戒指／法杖／卷軸／藥劑、鏡系特殊能力與製作／封禁魔法物品介面。

---

## 戰鬥前固定讀法

每次用角色卡正式跑遭遇時，先建立 encounter snapshot：

```text
A. 永久角色能力
B. 目前裝備及裝備效果
C. 記憶法術 / 已知但未記憶法術
D. Action Palette
E. 每日／每場剩餘次數
F. 當前 TRUE/FALSE buff
G. HP / SP / 法術位 / 儲魔池
H. 連續施法懲罰等 live-session 計數
I. 角色目前實際知道／相信的情報（若 relevant）
```

### 不再由 Dossier 決定的事

```text
這角色下一輪一定怎麼打
這角色真正的人格是什麼
這角色一定把誰視為最高威脅
危機時一定會燒哪個底牌
```

這些應由：

```text
角色 evidence / state
→ 詭祕提供合法 view
→ 分析師／生態學家等產生 hypothesis / proposal
→ AO 結算實際世界行動
```

若昂貴推理需要保存，可做 derived cache；不得回寫成角色卡正典。

## 法術 Effect Index 標準

角色卡列出的法術，代表角色在實際戰鬥／探索中可能使用；因此不能只保存法術名稱。

每個可用法術最終至少應能快速取得：

```text
名稱／來源
環數與學派
施法時間
射程
目標／範圍
持續時間
豁免／抗魔
主要效果
D100 已改寫接口／仍沿 3.5 的部分
Action economy 接口
重要 combo／反制關係
```

目標：角色宣告任何卡上法術時，DM 不是第一次理解它，而是直接取用已整理條目。

## 保險絲

```text
擁有能力 ≠ 已啟動
卡面 TRUE ≠ 所有獨立測試都要繼承
法術書有法術 ≠ 當前一定可直接施放
魔法物品存在 ≠ DM 可以替玩家自動啟動
持有物件 ≠ 角色願意在戰鬥中消耗
熟練玩家模擬 ≠ 只做一個主要動作
capability profile ≠ fixed behavior script
behavior evidence ≠ world fact about future choices
```

當 GPT 同時模擬玩家時，應把每名角色當成**熟悉自己 build 的玩家**，主動檢查瞬唱、即時、自由、一心二用、物品啟動、trigger 與特殊移動窗口；但實際選擇仍由當下 state、知識、偏好與局勢生成，而不是照 Dossier 固定 rotation。
