# Current PCs — Operational Profile v1

> 狀態：`[CHARACTER_EVIDENCE] [OPERATIONAL_PROFILE_V1]`
>
> 本檔不是角色卡數值的替代品，也不是固定行為腳本；它是目前三名 PC 的 **capability / behavior evidence cache**。目的：讓 DM／模擬玩家知道角色有哪些解題介面、哪些能力曾被玩家實際重視或迴避，避免把 build 壓扁成單一技能。
>
> 以下「解題傾向」只可作為生態學家／模擬者的 evidence seed。實際行動仍由當下 state、epistemic state、preferences／constraints 與合法 module views 生成；若需要保存戰術推理，應標 `derived` 並可失效。資料分層見 `../../DATA_ARCHITECTURE.md`。

法術 effect index 尚在補完；這不妨礙先封存 capability profile v1。

---

## 莎緹拉

### 一句話 capability profile

```text
高機動奧術控制／空間施法者
+ 外神性質
+ 極端終局能力
```

### 已觀察／可用的解題介面

- 位置與空間：任意門、閃現、飛行、次元錨、禁空等。
- 奧術情報／對策：解析弱點、秘法視力、分析傳送門、射線偏斜等。
- Action economy：即刻備戰 Lv3、一心二用 Lv1、法術瞬唱 Lv3、移動施法 Lv3。
- 大量卷軸、藥水與魔法物品，物品啟動本身是戰術介面。
- 阿薩托斯系特殊能力存在，但極端能力不是普通 rotation。

### Runtime 保險絲

```text
不要只選最高傷害法術。
不要因為持有終局能力就自動使用。
不要漏掉位置控制、瞬唱、即刻備戰與物品。
能力存在 ≠ 預測她一定會用。
```

---

## 亞黛兒

### 一句話 capability profile

```text
多體系施法者
+ 戰場支援／恢復
+ 空間與命運干預
```

### 已觀察／可用的解題介面

- 三施法體系：黑魔導／白魔導／吟遊。
- 支援：HP/SP 治療、護盾、聖域、戰歌、區域恢復。
- 空間：萬門之城、星空領域、移動角色、傳送。
- 命運／時間：旅行的見證、瀆神的本我整輪回捲或重置選擇。
- 資源再生：靈感復歸、神力恩澤等可回復每日能力次數。
- Action economy：即刻備戰、快速／瞬發法術、一心二用、即時治療、瞬間護罩。

### Runtime 保險絲

```text
她的能力輪廓不能被壓成「牧師補血」。
她具有改變隊伍後續 affordance 的能力。
擁有每日能力 ≠ 已啟動；必須讀 live state。
這些能力介面 ≠ 每輪固定優先級。
```

---

## 卡蘭德

### 一句話 capability profile

```text
高階變化／空間法師
+ 魔法物品工程師
+ 大量 contingency 資源
```

### 已觀察／可用的解題介面

- 變化系高有效 CL，並有大量變化、力場、傳送、控制、時間法術。
- Action economy：即刻備戰 Lv3、一心二用 Lv1、瞬步、法術瞬唱／物品啟動窗口。
- 魔法物品：戒指、法杖、項鍊、眼鏡、卷軸、藥劑與各類特殊物件都是 build 的一部分。
- 製作／封禁：能操作詞綴、符文、魔法物品過載／封禁領域等。
- 鏡系／迷霧系特殊能力存在。
- 【幽影的祝福】不是玩家本人認定的「底牌」：玩家表示過去沒有在戰鬥中使用過，且比起兌換一次化實為虛，更想維持戒指的壓制時間。這是**玩家行為／偏好證據**，不是永遠禁止使用的硬規則。
- 【幽影的祝福】背後授予者／本體關係仍待後續確認；使用傾向已由玩家證據更新。

### Runtime 保險絲

```text
不要把他跑成「普通法師每輪放一個法術」。
持有特殊物件 ≠ 願意在戰鬥中消耗。
能用幽影的祝福 ≠ 自動把它當危機底牌；玩家證據顯示有高機會成本。
live-session 的連續施法環數／減值不可自動帶入獨立測試。
玩家歷史偏好是 evidence，不是不可改變的未來行動 script。
```

---

## v1 成熟度

目前已足以封存：

```text
角色身份與核心定位
永久能力
關鍵專長／技能
Action Palette
獨特能力
主要魔法物品與攜帶資源
已知／記憶法術清單
live state 與永久狀態的分離
部分玩家使用偏好 evidence
```

仍在補完：

```text
每一個可用法術的 operational effect index
（施法時間／距離／範圍／持續／豁免／抗魔／主要效果／D100接口／重要combo）
```

完成 effect index 後，目標是：角色宣告任何卡上法術名稱時，DM 不需第一次理解該法術，只需取用已整理的操作條目。

## Data / Reasoning Boundary

```text
角色卡／Dossier
= capability + state + evidence

分析師／生態學家等
= 依當下合法 view 產生 hypothesis / proposal

AO
= 裁定實際世界結果
```

所以本檔不得被解讀為：

```text
角色未來行動的 deterministic policy
真正人格資料庫
固定 rotation
```
