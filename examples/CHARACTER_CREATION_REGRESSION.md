# Character Creation Regression — 2026-09-14

> 用途：壓測 Character Builder / Validator 是否又退化成「只買核心技能、怕 review、剩大量 CP 就收工」。
>
> 本檔不是 world state，不建立角色真相；只提供流程 regression cases。

---

## Test 1 — 低屬性角色的補償 CP 不能被白白囤積

給定：

```text
base CP = 200
九屬性 adjustment sum = -4
```

則：

```text
adjusted starting CP = 340
```

期望：

- Builder 不因核心職業能力買完就停止；
- 應進行背景／六面向候選掃描；
- 應進行 50 / 100 CP counterfactual pass；
- 若最後仍大量保留 CP，應是 deliberate reserve，不是沒搜尋。

失敗訊號：

```text
只花約 70–100 CP
其餘 200+ CP 無 reserve plan
```

---

## Test 2 — Lv3 不是稀有技能

給定一個難度1技能目前 Lv2，背景高度相關，CP 足夠。

期望：

```text
Lv2 → Lv3
```

應被正常列入候選，不因 `Lv4+ 稀有` 而降低推薦權重。

只有：

```text
Lv4+
```

才因 mastery rarity 產生 review flag。

---

## Test 3 — 難度3+ 是 review，不是隱藏候選

給定：

- 某難度3能力與角色概念高度相關；
- 前置已滿足；
- CP 足夠。

期望：

- 圖書館員仍回傳候選；
- 標記 `difficulty_rarity_review`；
- AO／GM 可要求背景前提；
- 不得因 review 而直接從候選池消失。

---

## Test 4 — 施法核心技能可非同步預購

法師：

```text
奧術知識3
黑魔導3
黑魔力2
```

期望：

```text
usable spell circle = 2
```

角色合法；兩項 Lv3 表示下一環進度。

禁止：

```text
因核心技能不同級而判整張卡非法
```

---

## Test 5 — 種族送難度2語言可滿足施法門檻

給定：

```text
角色已有 高等精靈語 Lv1（難度2，種族贈送）
職業 = 法師
```

期望：

- caster language gate 通過；
- Builder 可推薦龍語，但不能強制再買；
- 通用語 Lv3 照常免費取得。

---

## Test 6 — 法師學派是推薦，不是必填

二環法師：

期望：

- `通才` 合法；
- Builder 可記 `預定學派方向`；
- 若正式 `學派專精` 有三環／難度3前置，二環時不能購買；
- 不因未選學派退件。

---

## Test 7 — 牧師只有核心技能仍不算完整角卡

給定：

```text
宗教知識2
神術2
難度2語言 Lv1
```

但沒有：

```text
神祇／宗教
領域
```

期望：

- mechanics 可計算；
- `player_submission_required` 仍未通過；
- 角卡不能標 final accepted。

---

## Test 8 — 背景要產生能力候選

背景：

```text
多年商隊護衛
```

期望生態學家至少提出 competence domains：

```text
長途耐力
夜間警戒
道路生存
貨物／行李處理
馬匹／騎乘
旅店／商路人際接觸
```

再由圖書館員映射 D100 候選，例如：

```text
耐久
警覺／聆聽／偵察
生存／自救
繩技／估價
騎術／騎乘相關
搜集資訊／地方知識
```

禁止生態學家直接指定「一定要買到 LvN」。

---

## Test 9 — 3.5 class skill 不得直接升格必修

給定 Ranger 的 3.5 class skill evidence。

期望：

```text
Survival / Track / Nature / Spot ...
→ source_gap / culture candidate
```

不是：

```text
遊俠必須生存1
```

除非 D100／GM 另有 hard gate。

---

## Test 10 — Reward HP/SP 必須在 qualifying build 後處理

期望順序：

```text
技能／專長定稿
→ qualifying melee/spell CP
→ reward dice
→ base HP/SP
→ extra HP/SP purchase
```

若 build 大改並跨越新 reward threshold，舊獎勵不能無條件沿用。

若 qualifying 分類不確定：

- 保留 open question；
- 使用可證明的最低 qualifying floor；
- 不把總技能 CP 全部塞入某池。

---

## Test 11 — 六面向 breadth scan

自動角色完成核心 build 後至少掃：

```text
戰鬥
生存
工作／專業
社交
知識
興趣／人格表現
```

期望：

- 不要求六面平均；
- 但若角色只有職業核心一塊，Builder 必須再產生候選；
- 背景可以合理說明某些面向為空。

---

## Test 12 — 大量 reserve CP 不是自動失敗

給定自動角色剩餘 >30% CP。

期望：

1. 強制再跑一次 candidate enumeration；
2. 跑 50 / 100 CP counterfactual；
3. 若仍決定保留，可通過，但留下 `reserve_plan`。

`30%` 是 warning signal，不是硬性消費門檻。

玩家本人主動選擇存 CP 時，不應強迫玩家把 CP 花掉。
