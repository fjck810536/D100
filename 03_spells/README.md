# D100 Spell Lookup

本目錄是 D100 的法術查找／創角候選索引。法術資料可以同時包含基本來源與擴充來源；**來源是否被收錄**與**本次創角是否允許讀取**是兩件不同的事。

## 1. Source scope

創角／自動創角預設：

```text
spell_source_scope = basic_only
```

只把 `source_access.kind == basic` 的法術，以及基本來源的職業／環數資料送進候選池。

自然語言可切換 scope。這是**語意擬合**，不是固定提示詞 parser：

```text
「我要讀萬法」
「萬法模式」
「擴充全開」
「所有書都可以」
→ all
```

`all` = 開啟所有已收錄法術來源。**「萬法」在這裡是操作別名，不等於《萬法大全》。**

若使用者指定書名：

```text
「讀霜燃」
「這隻可以用完美奧術」
「加開萬法大全」
→ selected
→ 基本 + 指定來源
```

若語意明確要求「只讀某書」，才排除基本；若有排除語意（例如「全部都可以但不要死者之書」），先全開再排除。

若沒有足夠訊號，回到 `basic_only`；不要為了猜測把擴充池偷偷打開。

## 2. 查詢與創角權限不同

一般查詢法術時可以搜尋完整 index，並回報來源；source scope 主要限制：

- 自動創角候選枚舉；
- 協助創角推薦；
- 隨機／自動配置起始法術；
- 任何會把「可查」直接轉成「可選」的流程。

因此即使目前是 `basic_only`，玩家直接問「法力吸收是什麼？」仍可查到該法術；但 Builder 不應主動把《萬法大全》的法力吸收放進基本創角候選。

## 3. Index schema

`index/A.jsonl` … `index/Z.jsonl` 每列一個法術，主要欄位：

```text
spell_id / entry_id
name_zh / name_en
source_access
levels
level_text_raw
level_source_annotations
school / subschool / descriptors
components / casting_time / range / target / area / effect
duration / saving_throw / spell_resistance
additional_costs
description_zh / description_en
source_pages
parse_confidence
review
provenance
```

來源層保留：

```text
explicit_sources
inferred_sources
raw_source_labels
```

不要把推測來源覆寫成明確來源。

## 4. Basic / expansion / unresolved

```text
basic
  → 沒有擴充來源標記，且沒有強來源提示；預設可進創角池。

expansion
  → 原資料已有 source relation；預設不進基本創角池。

unresolved_expansion
  → source relation 漏失，但標題／等級前綴等位置有強來源提示；
    預設不進基本創角池，讀萬法時可見，並保留 review flag。
```

這是保守的 near-fit，不要求來源解析 100% 完美。

## 5. 職業／環數的來源也要分層

有些基本法術會在同一條 `等級` 文字中附上擴充書新增／修改的職業或環數，例如：

```text
善良 4【完美神力：榮譽領域 4】
```

這時法術本體仍可屬基本，但 `完美神力` 的新增環數不得在 `basic_only` 創角時使用。

因此 index 同時保留：

```text
levels                    原資料庫已正規化的等級
level_text_raw             原始等級行
level_source_annotations   近似擷取出的 source-scoped 變體
```

若三者衝突，以 raw/provenance 進 review，不要靜默假裝已完全解析。

## 6. D100 semantic conversion

本索引是 **source / normalized lookup data**，不是「所有 3.5 數字已自動變成 D100 規則」。

施法時間、回合、距離、豁免、法抗等若與 D100 runtime 發生機械衝突，仍依：

```text
00_core/magic.md
90_srd_bridge/
D100 source hierarchy
```

做語義轉譯。
