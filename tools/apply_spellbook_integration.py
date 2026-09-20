#!/usr/bin/env python3
"""Apply the minimal D100 documentation wiring for 03_spells.

Idempotent: every insertion is guarded by a stable marker/string.
Fails loudly if the expected current architecture has drifted, rather than
silently inserting text in the wrong location.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, needle: str, replacement: str, marker: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        print(f"skip {path}: marker already present")
        return
    if needle not in text:
        raise SystemExit(f"integration needle not found in {path}: {needle[:80]!r}")
    p.write_text(text.replace(needle, replacement, 1), encoding="utf-8")
    print(f"patched {path}")


# AGENTS: make the lookup contract discoverable for spell creation/query tasks.
patch(
    "AGENTS.md",
    "若場景涉及神器、3.5 轉譯或規則洞，再讀：",
    """若任務涉及施法角色的起始法術、協助／自動創角法術候選、或法術查找，再讀：\n\n- `03_spells/README.md`\n- `03_spells/manifest.json`\n\n創角法術候選必須先經 `spell_source_scope`：預設只讀基本；「讀萬法」及近似的全開語意代表所有已收錄來源；指定書名則只加開指定來源。這是語意擬合，不是固定提示詞比對。`萬法`（操作別名）不得誤解成《萬法大全》（單一來源書）。\n\n若場景涉及神器、3.5 轉譯或規則洞，再讀：""",
    "`spell_source_scope`：預設只讀基本",
)

# START_DM: add on-demand navigation.
patch(
    "START_DM.md",
    "- `sources/SHEET_INDEX.md` — Sheet 語義導航；世界／組織／學院／技能來源查核時優先用來找正確 raw tab。",
    """- `03_spells/README.md` / `03_spells/manifest.json` — 法術查找與創角 source scope。施法角色創角／起始法術配置時必讀；預設 basic-only，「讀萬法」近似語意 = 全來源，指定書名 = 基本 + 指定來源。\n- `sources/SHEET_INDEX.md` — Sheet 語義導航；世界／組織／學院／技能來源查核時優先用來找正確 raw tab。""",
    "`03_spells/README.md` / `03_spells/manifest.json`",
)

# DATA_ARCHITECTURE: register source provenance and normalized spell index.
patch(
    "DATA_ARCHITECTURE.md",
    "sources/GM_*.md                    GM 補答、暫定、歷史證據",
    """sources/GM_*.md                    GM 補答、暫定、歷史證據\nsources/spellbook/                   Spellbook 靜態拆包來源／匯入 provenance""",
    "sources/spellbook/                   Spellbook",
)
patch(
    "DATA_ARCHITECTURE.md",
    "02_items/\n90_srd_bridge/* conversion references",
    """02_items/\n03_spells/                           法術 lookup / compact catalog / source-scope index\n90_srd_bridge/* conversion references""",
    "03_spells/                           法術 lookup",
)

# CHARACTER_CREATION_PROTOCOL: source-gated spell enumeration.
patch(
    "CHARACTER_CREATION_PROTOCOL.md",
    "4. 不得把 3.5 class skill 直接升格成 D100 必修。",
    """4. 不得把 3.5 class skill 直接升格成 D100 必修。\n5. 若角色會施法，先讀 `03_spells/catalog/` 依 `spell_source_scope` 過濾，再做法術候選廣搜；需要具體法術內容時才進 `03_spells/index/`。不得先讓 Builder 看全部擴充法術，再靠提示自己不要選。""",
    "不得先讓 Builder 看全部擴充法術",
)
patch(
    "CHARACTER_CREATION_PROTOCOL.md",
    "---\n\n# 2. 創角八階段",
    """---\n\n## 1.1 法術來源 Scope — Spell Candidate Gate\n\n法術庫可以完整收錄基本與擴充來源；**可查詢**與**本次創角可作為候選**分開。\n\n預設：\n\n```text\nspell_source_scope = basic_only\n```\n\n語意解析採近似擬合，不要求固定提示詞：\n\n```text\n「我要讀萬法」／「萬法模式」／「擴充全開」／「所有書都可以」等近似語意\n→ all\n→ 所有已收錄來源\n\n「讀霜燃」／「這隻可以用完美奧術」／「加開萬法大全」等指定書名語意\n→ selected\n→ 基本 + 指定來源\n\n「只看基本」／「不要擴充」等\n→ basic_only\n```\n\n若明確說「只讀某書」，可以把 basic 也排除；若明確說「全開但不要某書」，採 all 再 exclude。歧義不足以確定時維持 `basic_only`，不偷偷放寬。\n\n術語保險絲：\n\n```text\n萬法      = 操作別名，表示 all\n萬法大全  = 一個具體來源書名；只指定它時不等於 all\n```\n\n一般法術查詢不受創角 source scope 阻擋；玩家直接查某個擴充法術時仍可讀取並回報來源。scope 主要限制自動創角、協助創角推薦、起始法術配置與其他「可查 → 可選」流程。\n\n實作與來源清單見 `03_spells/README.md`、`03_spells/manifest.json`。\n\n---\n\n# 2. 創角八階段""",
    "## 1.1 法術來源 Scope — Spell Candidate Gate",
)
patch(
    "CHARACTER_CREATION_PROTOCOL.md",
    "- GM／玩家明示 house rule。",
    """- GM／玩家明示 house rule。\n- 若為施法角色：本次 `spell_source_scope`；未明示時固定 `basic_only`。""",
    "本次 `spell_source_scope`；未明示時固定",
)
patch(
    "CHARACTER_CREATION_PROTOCOL.md",
    "→ 配置起始魔法物品／法術／資源\n→ final validation",
    """→ 配置起始魔法物品／法術／資源（法術候選先經 `spell_source_scope`）\n→ final validation""",
    "配置起始魔法物品／法術／資源（法術候選先經",
)

# magic core: define the operational boundary next to starting spells.
patch(
    "00_core/magic.md",
    "德魯伊／牧師：\n\n- 到達該環後自動習得該環所有基礎法術。\n- 若是專長升階或萬法大全等額外來源法術，仍可能需要法術書輔佐。",
    """德魯伊／牧師：\n\n- 到達該環後自動習得該環所有基礎法術。\n- 若是專長升階或萬法大全等額外來源法術，仍可能需要法術書輔佐。\n\n### 8.1 法術查找與創角來源範圍 `[D100_CANON data + DM interface]`\n\n完整法術查找資料見 `../03_spells/`。法術是否存在於 D100 法術庫，與本次創角是否允許把它放進候選池，是兩件事。\n\n```text\n預設創角                    → basic_only\n「讀萬法」及近似全開語意    → all\n指定某一本來源書            → basic + 指定來源\n```\n\n語意採近似擬合，不要求固定提示詞完全一致。`萬法` 是全來源操作別名；《萬法大全》是具體來源書，兩者不得混淆。一般查詢可以讀完整法術庫並回報來源；source scope 主要限制創角／自動創角的候選枚舉。""",
    "### 8.1 法術查找與創角來源範圍",
)
