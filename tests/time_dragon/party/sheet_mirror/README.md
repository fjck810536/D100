# Time Dragon character-sheet mirrors

> `[TEST_FIXTURE] [SHEET_MIRROR]`
>
> Scope: `tests/time_dragon/` only. These snapshots are provenance / recovery fallbacks for the Time Dragon combat pressure test. They are **not** global D100 rule authority, **not** selected campaign state, and should not be loaded during normal bootstrap.

Operational test runs should normally read the dossiers in `../`. Use these mirrors when a dossier claim needs source-sheet verification or when rebuilding a dossier.

## Mirror format

The source Google Sheets were exported as XLSX snapshots, then projected into sparse Markdown containing non-empty cells from every tab.

- `V` = literal / cached cell value.
- `F` = formula plus cached value.
- `\n` and `\t` are escaped inside cell text.
- Visual formatting, drawings, charts, comments, row heights, and other presentation-only data are omitted.
- The original Google Sheet remains the live external source; these files are immutable test snapshots, not a sync mechanism.

## Files

### Sathera

- Mirror: `SATHERA_CHARACTER_SHEET.md` (plain readable sparse Markdown)
- Source: https://docs.google.com/spreadsheets/d/190tSepkLnQFWwBV1PkBOkn0ri0ILSUNBWn1mAbLpoCQ/edit
- Source XLSX SHA-256: `25d7c3e8b8b80c917f0c4ad7b0a6fd9af75e2231ce019cc2b3e6cb6b02bcc1d5`
- Mirror SHA-256: `cda5170265a4009aa066c3c7f36af7c4c7c67218173b2705b1f10583e5b626d0`
- Tabs mirrored: `角色紙`, `法術書`, `工作表1` (empty)

### Adele

- Mirror: `ADELE_CHARACTER_SHEET.md.gz.b64`
- Source: https://docs.google.com/spreadsheets/d/1bJ6_bIRoOCI0UUsV4AlHi9YLpWrvXb_0t1nVU0HBHQw/edit
- Source XLSX SHA-256: `22d13f78aa7fc16208b22b4fe985b070d4b32caba7b06468d25f5d6028a4db6b`
- Decoded Markdown SHA-256: `3ae73e3644569f150f5b02942ae93cac64f8aadea38eb4ccd603768997d9b17b`
- Tabs mirrored: `角色紙`, `法術書(法師)`, `法術書(牧師)`, `法術書(吟遊)`, `Helper`, `特殊物件說明`

### Kaland

- Mirror: `KALAND_CHARACTER_SHEET.md.gz.b64`
- Source: https://docs.google.com/spreadsheets/d/14dLjE8hoWg9RForhFzvc6H71WTvYC88O7nr8_SX4EaE/edit
- Source XLSX SHA-256: `eedfc84c39f463b9bb07123af172bf54b10cd4e48eba15821af4ecae2ce947f2`
- Decoded Markdown SHA-256: `a38288a6f7c9d569a4a3085bcd019d0ffe8ff506ebfd9496cbde02616bd86366`
- Tabs mirrored: `腳色紙`, `法術書`, `額外筆記`, `幕間用計算表`, `Crafting log`, `特殊製作物品`, `不常用法術效果`

## Decode compressed mirrors

macOS:

```bash
base64 -D ADELE_CHARACTER_SHEET.md.gz.b64 | gzip -dc > ADELE_CHARACTER_SHEET.md
base64 -D KALAND_CHARACTER_SHEET.md.gz.b64 | gzip -dc > KALAND_CHARACTER_SHEET.md
```

GNU/Linux:

```bash
base64 --decode ADELE_CHARACTER_SHEET.md.gz.b64 | gzip -dc > ADELE_CHARACTER_SHEET.md
base64 --decode KALAND_CHARACTER_SHEET.md.gz.b64 | gzip -dc > KALAND_CHARACTER_SHEET.md
```

The compressed form is deliberate: it preserves the complete sparse snapshot without turning tens of thousands of characters of source-sheet dump into ordinary agent-readable runtime context.
