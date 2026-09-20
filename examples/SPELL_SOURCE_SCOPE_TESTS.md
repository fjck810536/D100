# Spell Source Scope Regression

目的：防止創角時把「完整可查法術庫」誤當成「預設全部可選」。

| Input intent | Expected scope |
|---|---|
| 未提來源，請自動創一名法師 | `basic_only` |
| 我要讀萬法 | `all` |
| 萬法模式開一下 | `all` |
| 擴充都算 | `all` |
| 這隻可以讀霜燃 | `selected: 霜燃之書` + basic |
| 我要讀萬法大全 | `selected: 萬法大全` + basic；**不是 all** |
| 只看基本 | `basic_only` |
| 全部都可以，但不要死者之書 | `all - 死者之書` |

## Required behavior

1. 語意近似擬合，不要求字串完全一致。
2. 無足夠訊號時不得默認擴充全開。
3. 一般查詢某個擴充法術不受 creation scope 阻擋，但必須回報來源。
4. `unresolved_expansion` 不得漏進 `basic_only`。
5. 基本法術若只在 `level_source_annotations` 有擴充書新增職業／環數，`basic_only` 不得採用該擴充變體。
