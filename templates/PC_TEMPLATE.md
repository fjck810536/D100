# PC_TEMPLATE.md

> 複製本檔建立 `characters/<name>.md`。DM 每次需要角色數值時以角色檔為準，不要靠聊天記憶猜。
>
> 本檔是角色 state / capability record，不是人格模塊。完整祕密不直接塞進角色檔；需要時用 Mystery Secret ref。架構見 `../DATA_ARCHITECTURE.md`。

```yaml
name:
player:
race:
concept:
current_cp:
total_cp:
agency:
  type: autonomous
```

## 九大屬性

| 屬性 | 值 | 調整值 |
|---|---:|---:|
| STR |  |  |
| DEX |  |  |
| SKI |  |  |
| CON |  |  |
| RES |  |  |
| INT |  |  |
| WIS |  |  |
| CHA |  |  |
| SPI |  |  |

## 六大技能基礎

```text
戰鬥 =
運動 =
操作 =
感知 =
知識 =
交涉 =
```

## 五大抗性

```text
抗毒素 =
抗控制 =
抗轉化 =
抗噴吐 =
抗魔法 =
```

## 三特殊判定

```text
強韌 =
精神 =
靈魂 =
```

## 生存資源

```text
HP： / 
SP： / 
臨時HP：
移動：         # 若角色表已有實際值直接填；不要由未決公式自行猜
```

## 戰鬥

```text
行動順序值（DEX + mod）：
宣告順序值（INT + mod）：
閃避：
格擋：
盾牌：
鎧甲：
物抗：
法抗：
火抗：
冰抗：
電抗：
酸抗：
光抗：
暗抗：
其他：
```

## 武器

### 武器 1

```text
名稱：
武器使用技能：
攻擊判定：
基礎傷害：
爆擊：
射程：
詞綴：
其他：
```

## 技能／基本專長

| 名稱 | 分類 | 難度 | 等級 | 最終判定 | 備註 |
|---|---|---:|---:|---:|---|

## 一般／高級／傳奇專長

| 名稱 | 等級 | 效果摘要 |
|---|---:|---|

## 施法

```text
施法職：
最高環數：
總施法者等級：
施法主屬性：
法術位：
記憶法術位：
連續施法懲罰：
```

### 已知／已抄寫法術

| 法術 | 環數 | 體系 | 備註 |
|---|---:|---|---|

### 當前記憶

| 法術 | 環數 |
|---|---:|

## 魔法物品

| 物品 | 加值 | 詞綴 | 調頻 | 使用次數／資源 |
|---|---:|---|---|---|

## Action Palette cache

> 可由技能／專長／物品／當前狀態重建。若在此保存，是方便 runtime 的 capability cache，不是另一份規則來源。

```text
一般動作：
自由動作：
即時／反應：
瞬唱：
並行能力：
移動能力：
觸發式能力：
物品啟動：
每日／每場／充能資源：
```

## 狀態

```text
姿勢：
持續增益：
持續減益：
DOT：
控制／轉化進度：
靈魂／精神狀態：
藥水負荷：
```

## Epistemic State

> 只記角色目前實際知道／相信／誤信的內容，不記分析師眼中的「真正人格」。

```yaml
known_facts: []
beliefs: []
misbeliefs: []
```

## Preferences / Constraints

> 用於 NPC／模擬角色時，可記穩定且有 evidence 的偏好與義務；真玩家 PC 不應被這區替玩家預決定行動。

```yaml
preferences: []
constraints: []
```

核心分離：

```text
belief ≠ preference ≠ action
```

## Secret refs

```yaml
secret_refs: []
```

只放角色檔合法取得的 Secret ID / role-safe representation。完整 protected payload 依 `MYSTERY_PROTOCOL.md` 管理。

## 語言

## 背景與已知情報

## DM 注意

- 角色檔內實際數值／持有能力優先於聊天記憶。
- 擁有能力 ≠ 已啟動；持有物件 ≠ 願意消耗。
- 真玩家控制 PC 時，角色檔不能替玩家決定「通常會做什麼」。
- 若保存 combat doctrine / threat model 等推理，只能標為 derived cache，不能寫成 established character truth。
- 秘密資料透過 Mystery refs 連接，不建立平行 plaintext DM secret 區。
