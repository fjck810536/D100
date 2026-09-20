# 領域與結社註冊表

本檔是 D100 的制度層入口。**法術詞條保持來源唯讀**；領域／結社只在此處註冊與掛接反向法術索引。

## Canonical domain identity

本輪以英文 domain identity、實際 domain spell list、來源書三重對照，將朋友工具的 **87 個來源標籤**整理為 **83 個真正的 canonical domain identities**。來源標籤仍全部保留供溯源，不能反向改寫法術原文。

```text
source label ≠ canonical domain identity
中文近似 ≠ 同一領域
同一英文 domain 的不同書版本 ≠ 兩個新領域
```

## 本輪抓出的主要碰撞

- `神譴 / 憤怒` → Wrath；保留 BoED / Spell Compendium 版本差異。
- `瘋狂 / 狂亂` → Madness。
- `契約 / 誓約` → Pact。
- `社會 / 溝通` → Community。
- `侏儒 / 守護` → Gnome；`守護領域` 的原詞條自己註明 `Gnome Domain`，視為來源誤譯標籤。
- `冥土 / 黑帝斯` → Hades planar domain。
- `工匠領域` → Artifice；`工藝` → Craft。**兩者不可合併。**
- `寒冷` → Cold；`隆冬` → Winter。**兩者不可合併。**

因此已刪除舊的粗糙 alias：`榮譽→榮耀`、`工匠→工藝`、`機械→機械界`、字元級 `砂→沙`、`寒冷→隆冬`。只保留完整 domain label 的安全解析。

## D100 專長狀態

領域可以先註冊、先有法術表，再逐步補 D100 領域專長。`domain_feat_status: pending` 不等於領域不存在。現有 D100 十個已實作領域仍獨立保留；不要把 Healing→Life、Magic→Arcana、Sun→Light、Storm→Tempest、Repose→Grave 等近似概念自動合併。

## 反向索引

完整 canonical domain → spell 關聯見 `../03_spells/domain_spell_map.json`。每條關聯保留原 `source_domain_labels / raw_class_labels / spell_sources`，所以 Wrath、Madness、Community 等不同書版本仍可追來源。

## 歷史地層

部分法術比 3e 的 Domain 制度更老。例如 `Surelife` 在 1e/2e 已作為 wu jen 法術存在，3e/3.5 才被收進 Repose Domain；因此「法術譜系」與「Domain 身份」分開保存。

## 德魯伊結社

目前 D100 上游明確存在：大地結社、牧人之環結社、夢境之環結社、月亮結社；大地結社含凍土、海岸、荒原、森林、草原、山脈、沼澤、地底八個環境法術表。Spellbook 掃描沒有找到額外 `結社 / 之環 / Circle` 等級標記，因此不憑空新增。


## 領域專長調整工程

擴充領域已進入五階專長建置。設計規約見 `domain_feat_adaptation_protocol.md`，完整 provisional 機械見 `domain_feat_catalog.json`，可讀版見 `domain_feats_expansion.md`。

目前 83 個 imported canonical domains 中，Knowledge / Trickery / War 直接沿用既有 D100；其餘 80 個皆已有 D1–D5 provisional 專長。這些條目是可壓測的 D100 adjustment，不冒充上游 Sheet 原文。
