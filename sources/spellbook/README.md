# Spellbook source import

來源：使用者提供的 `Spellbook.exe` 靜態拆包結果。

本次沒有執行原 `.exe`。Nuitka onefile payload 中可直接取得：

```text
data/spellbook.sqlite
spellbook/taxonomy.json
spellbook/seed_fixes.json
```

D100 匯入以 `spellbook.sqlite` 為主，taxonomy / seed fixes 作原資料的解析與校訂背景。原資料本身含 review / extraction issue 記錄；匯入時保留而不洗掉。

## 來源角色

這個 Spellbook 是 D100 法術查找資料來源；其中可以包含基本法術與《萬法大全》、完美系列、環境／族裔類擴充書等來源。

**不要把「收錄於 D100」誤讀成「自動創角預設全部可用」。**

創角 source scope 見：

```text
03_spells/README.md
```

## 重建

```bash
python3 tools/import_spellbook.py /path/to/spellbook.sqlite --out /path/to/D100
```

匯入器不修改 SQLite，只產生 normalized/index data 與 review queue。
