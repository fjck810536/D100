# Spellbook import report — 2026-09-21

靜態拆包後資料庫：

```text
active spells: 2405
```

目前 near-fit source access 分類：

```text
basic:                 637
expansion:            1702
unresolved_expansion:   66
```

`unresolved_expansion` 代表資料庫沒有正式 `spell_sources` 關聯，但標題、來源獨立行或等級前綴出現強來源提示。為避免擴充法術漏進預設創角池，先保守排除；「讀萬法」時仍可讀取。

目前匯入後可見來源標記包含：

```text
萬法大全
完美冒險
完美奧術
完美巫師
完美聖鬥士
完美神力
完美流氓
完美戰力
風暴之書
霜燃之書
沙暴之書
死者之書
巨龍之書 / 巨龍書
異怪書
荒野族裔
天命族裔
好人書
PHB2
ECS
以及原表中可辨識但尚未對齊正式別名的：戰鬥英雄、龍之魔法、龍之魔力
```

資料品質：

- 原 SQLite 自帶 `review_status`、`extraction_issues` 等校訂資料。
- 匯入器另外標記 source inference、source-scoped level variant、缺少 normalized spell levels 等情況。
- 本次產生 review queue 約 250 筆量級；這不阻塞整體 lookup。
- 基本／擴充判定採 near-fit；目標是避免明顯擴充內容默默進 basic pool，而非假裝已完成 100% 書目學校訂。

代表性檢查：

```text
火球術 / Fireball
→ basic

魔法飛彈 / Magic Missile
→ basic

法力吸收 / Absorption
→ 萬法大全 / expansion

火焰步履 / Fire Stride
→ 原 source relation 漏標，但 heading 明示萬法大全
→ unresolved_expansion / 萬法大全

聖光擊 / Holy Smite
→ spell 本體 basic
→ level text 另含「完美神力：榮譽領域 4」
→ basic_only 可讀基本版本，但不應採用擴充領域變體
```
