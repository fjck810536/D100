# Ancient Time Dragon — Source Notes

> 狀態：`[SOURCE_BOOK_NOTE] [DEFERRED]`
>
> 用途：保存 Dragon #359 原書本身的數值／算術差異與來源解讀備忘。這些項目不是目前的 D100 conversion bug；除非後續實戰或 regression 顯示對應欄位確實有問題，否則不主動重開換算。

## Ancient HP 原書註記

Dragon #359 的 Ancient Time Dragon 列印為：

```text
HD 89d12+2403
printed HP 2931
```

若單純以 `d12` 平均值 6.5 計算：

```text
89 × 6.5 + 2403 = 2981.5
```

因此兩條資訊都保留：

```text
[SOURCE_PRINTED] 2931
[SOURCE_DERIVED_ARITHMETIC] 2981.5
```

目前不判定原書哪一條「應被修正」，也不因此改寫來源 stat block。

在目前採用的保守 3.5 haste／natural-weapon 解讀下，若用來源時空龍自己的完整自然武器 routine 做 self-TTK 參考：

```text
printed HP 2931  → 約 15.50 套 full attack
HD mean 2981.5   → 約 15.77 套 full attack
```

這個 `15.50–15.77` 只標記為**原書來源耐久參考帶**。

目前處理原則：

```text
先存檔，不為此單獨調整 D100 HP。
若之後實戰／regression 顯示 HP 或 TTK 有異常，
再回頭檢查：
- printed HP 路徑
- HD arithmetic 路徑
- haste × natural weapon 解讀
- D100 closed-loop HP 換算
```

換句話說：

> **來源差異先保存；問題真的出現時再解。**
