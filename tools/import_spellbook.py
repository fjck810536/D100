#!/usr/bin/env python3
"""
Import Spellbook SQLite into the D100 spell lookup index.

Design goals:
- Keep every spell and its provenance.
- Default character-creation pool = basic source only.
- "讀萬法" (semantic intent, not exact string) = all registered sources.
- A named source opens basic + that source.
- Preserve ambiguous/malformed source metadata as review flags instead of silently
  treating it as basic.
- Keep raw level text because some entries encode expansion-specific class/level
  variants inside the level line rather than in the source relation table.

This importer does NOT convert D&D 3.5 numeric semantics to D100 combat timing.
It creates source/index data only.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sqlite3
from pathlib import Path
from typing import Iterable

KNOWN_SOURCE_HINTS = {
    "萬法大全", "萬法",
    "完美冒險", "完美奧術", "完美巫師", "完美聖鬥士", "完美神力",
    "完美流氓", "完美戰力",
    "風暴之書", "霜燃之書", "沙暴之書", "死者之書",
    "巨龍之書", "巨龍書", "異怪書",
    "荒野族裔", "天命族裔", "好人書",
    "PHB2", "ECS",
    # observed headings in this corpus; kept as raw source labels if no canonical
    # source alias is known.
    "戰鬥英雄", "龍之魔法", "龍之魔力",
}

SOURCE_ALIAS = {
    "萬法": "萬法大全",
}

SOURCE_LIKE_RE = re.compile(
    r"(萬法|完美|PHB\d*|ECS|[^（）()]{1,10}之書|[^（）()]{1,10}大全|"
    r"戰鬥英雄|龍之魔法|龍之魔力)"
)

LEVEL_LINE_RE = re.compile(r"(?:^|\n)等級[：:]\s*([^\n]+)")
FULLWIDTH_PARENS_RE = re.compile(r"[（(]([^（）()]{1,80})[）)]")


def split_source_name(raw: str) -> list[str]:
    """Split obvious combined source labels without inventing new aliases."""
    out: list[str] = []
    for part in re.split(r"[,，]", raw or ""):
        part = part.strip()
        part = re.sub(r"[，,]?\s*兩者有不同\s*$", "", part).strip()
        if not part:
            continue
        part = SOURCE_ALIAS.get(part, part)
        if part not in out:
            out.append(part)
    return out


def extract_level_line(raw_text: str) -> str:
    m = LEVEL_LINE_RE.search(raw_text or "")
    return m.group(1).strip() if m else ""


def source_hints_from_heading(heading: str) -> list[str]:
    hints: list[str] = []
    for token in FULLWIDTH_PARENS_RE.findall(heading or ""):
        token = token.strip()
        if token in KNOWN_SOURCE_HINTS or SOURCE_LIKE_RE.fullmatch(token):
            for canonical in split_source_name(token):
                if canonical not in hints:
                    hints.append(canonical)
    return hints


def source_hints_from_level_prefix(level_line: str) -> list[str]:
    """Catch lines such as '完美奧術：牧師 8，術士/法師 6'."""
    if not level_line:
        return []
    prefix = re.split(r"[：:]", level_line, maxsplit=1)[0].strip()
    if prefix in KNOWN_SOURCE_HINTS or SOURCE_LIKE_RE.fullmatch(prefix):
        return split_source_name(prefix)
    return []


def standalone_source_hint(raw_text: str) -> list[str]:
    """Catch a standalone source line immediately before the school line."""
    lines = [x.strip() for x in (raw_text or "").splitlines()[:4] if x.strip()]
    out: list[str] = []
    for line in lines[1:3]:
        m = re.fullmatch(r"[（(]([^（）()]{1,50})[）)]", line)
        if not m:
            continue
        token = m.group(1).strip()
        if token in KNOWN_SOURCE_HINTS or SOURCE_LIKE_RE.fullmatch(token):
            for canonical in split_source_name(token):
                if canonical not in out:
                    out.append(canonical)
    return out


def level_source_annotations(level_line: str) -> list[dict]:
    """
    Preserve expansion-specific annotations in the raw level line.
    This is intentionally heuristic. It does not replace the raw line.
    """
    if not level_line:
        return []
    out: list[dict] = []

    # Source-prefixed entire level assignment.
    pref = source_hints_from_level_prefix(level_line)
    if pref:
        rest = re.split(r"[：:]", level_line, maxsplit=1)
        out.append({
            "kind": "source_scoped_level_text",
            "sources": pref,
            "text": rest[1].strip() if len(rest) == 2 else level_line,
        })

    # Parenthetical/bracketed source-specific alternatives/additions.
    for left, right in [("（", "）"), ("(", ")"), ("【", "】"), ("[", "]")]:
        pattern = re.compile(re.escape(left) + r"(.{1,160}?)" + re.escape(right))
        for m in pattern.finditer(level_line):
            text = m.group(1).strip()
            hits = []
            for hint in sorted(KNOWN_SOURCE_HINTS, key=len, reverse=True):
                if hint in text:
                    canonical = SOURCE_ALIAS.get(hint, hint)
                    if canonical not in hits:
                        hits.append(canonical)
            if hits:
                out.append({
                    "kind": "source_scoped_level_text",
                    "sources": hits,
                    "text": text,
                })
    # de-dupe
    seen = set()
    deduped = []
    for item in out:
        key = (tuple(item["sources"]), item["text"])
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    return deduped


def fetchall_dict(con: sqlite3.Connection, sql: str, args=()) -> list[dict]:
    return [dict(r) for r in con.execute(sql, args).fetchall()]


def import_spellbook(db_path: Path, out_root: Path) -> dict:
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row

    source_by_entry: dict[str, list[str]] = collections.defaultdict(list)
    raw_source_by_entry: dict[str, list[str]] = collections.defaultdict(list)
    for r in con.execute("""
        SELECT ss.spell_entry_id, s.name
        FROM spell_sources ss
        JOIN sources s ON s.id = ss.source_id
        ORDER BY ss.spell_entry_id, s.name
    """):
        raw_source_by_entry[r["spell_entry_id"]].append(r["name"])
        for source in split_source_name(r["name"]):
            if source not in source_by_entry[r["spell_entry_id"]]:
                source_by_entry[r["spell_entry_id"]].append(source)

    levels_by_entry: dict[str, list[dict]] = collections.defaultdict(list)
    for r in con.execute("""
        SELECT sl.spell_entry_id, c.name AS class_name, sl.spell_level, sl.note
        FROM spell_levels sl
        JOIN classes c ON c.id = sl.class_id
        ORDER BY sl.spell_entry_id, sl.spell_level, c.name, sl.note
    """):
        levels_by_entry[r["spell_entry_id"]].append({
            "class": r["class_name"],
            "level": r["spell_level"],
            "note": r["note"],
        })

    descriptors_by_entry: dict[str, list[str]] = collections.defaultdict(list)
    for r in con.execute("""
        SELECT sd.spell_entry_id, d.name
        FROM spell_descriptors sd
        JOIN descriptors d ON d.id = sd.descriptor_id
        ORDER BY sd.spell_entry_id, d.name
    """):
        descriptors_by_entry[r["spell_entry_id"]].append(r["name"])

    issues_by_entry: dict[str, list[dict]] = collections.defaultdict(list)
    for r in con.execute("""
        SELECT spell_entry_id, issue_type, severity, message
        FROM extraction_issues
        ORDER BY spell_entry_id, id
    """):
        issues_by_entry[r["spell_entry_id"]].append({
            "type": r["issue_type"],
            "severity": r["severity"],
            "message": r["message"],
        })

    records = []
    review_records = []
    source_counts = collections.Counter()
    access_counts = collections.Counter()

    rows = con.execute("""
        SELECT
            sp.id AS spell_id,
            sp.name_zh, sp.name_en, sp.alphabet,
            sp.review_status AS spell_review_status,
            e.id AS entry_id, e.source_key, e.heading,
            e.school, e.subschool, e.components, e.casting_time,
            e.range_text, e.target_text, e.area_text, e.effect_text,
            e.duration, e.saving_throw, e.spell_resistance,
            e.additional_costs, e.description_zh, e.description_en,
            e.pdf_page_start, e.pdf_page_end,
            e.parse_confidence, e.review_status AS entry_review_status,
            e.translation_status, e.translation_method,
            e.raw_text
        FROM spells sp
        JOIN spell_entries e ON e.spell_id = sp.id
        WHERE sp.record_status = 'active'
        ORDER BY sp.alphabet, lower(sp.name_en), sp.name_zh
    """).fetchall()

    for r in rows:
        entry_id = r["entry_id"]
        explicit_sources = list(source_by_entry.get(entry_id, []))
        raw_sources = list(raw_source_by_entry.get(entry_id, []))
        level_line = extract_level_line(r["raw_text"] or "")
        heading_hints = source_hints_from_heading(r["heading"] or "")
        prefix_hints = source_hints_from_level_prefix(level_line)
        standalone_hints = standalone_source_hint(r["raw_text"] or "")

        inferred_sources = []
        for x in heading_hints + prefix_hints + standalone_hints:
            if x not in explicit_sources and x not in inferred_sources:
                inferred_sources.append(x)

        all_sources = explicit_sources + [x for x in inferred_sources if x not in explicit_sources]

        # Access classification.
        # explicit source relations or strong source heading/prefix markers mean
        # expansion-only unless later human review says otherwise.
        if explicit_sources:
            access_kind = "expansion"
        elif heading_hints or prefix_hints or standalone_hints:
            access_kind = "unresolved_expansion"
        else:
            access_kind = "basic"

        # Level-line expansion annotations do NOT automatically make the whole
        # spell expansion-only; a basic spell may have an expansion-added domain
        # or alternate class level.
        level_annotations = level_source_annotations(level_line)

        review_flags = []
        if access_kind == "unresolved_expansion":
            review_flags.append("source_inferred_not_relational")
        if r["spell_review_status"] == "needs_review" or r["entry_review_status"] == "needs_review":
            review_flags.append("upstream_needs_review")
        if issues_by_entry.get(entry_id):
            review_flags.append("upstream_extraction_issue")
        if level_annotations:
            review_flags.append("source_scoped_level_variant_present")
        if not levels_by_entry.get(entry_id):
            review_flags.append("no_normalized_spell_levels")

        record = {
            "spell_id": r["spell_id"],
            "entry_id": entry_id,
            "name_zh": r["name_zh"],
            "name_en": r["name_en"],
            "alphabet": r["alphabet"],
            "source_access": {
                "kind": access_kind,
                "sources": all_sources,
                "explicit_sources": explicit_sources,
                "inferred_sources": inferred_sources,
                "raw_source_labels": raw_sources,
                "default_character_creation": access_kind == "basic",
            },
            "levels": levels_by_entry.get(entry_id, []),
            "level_text_raw": level_line,
            "level_source_annotations": level_annotations,
            "school": r["school"],
            "subschool": r["subschool"],
            "descriptors": descriptors_by_entry.get(entry_id, []),
            "components": r["components"],
            "casting_time": r["casting_time"],
            "range": r["range_text"],
            "target": r["target_text"],
            "area": r["area_text"],
            "effect": r["effect_text"],
            "duration": r["duration"],
            "saving_throw": r["saving_throw"],
            "spell_resistance": r["spell_resistance"],
            "additional_costs": r["additional_costs"],
            "description_zh": r["description_zh"],
            "description_en": r["description_en"],
            "source_pages": [r["pdf_page_start"], r["pdf_page_end"]],
            "parse_confidence": r["parse_confidence"],
            "review": {
                "spell_status": r["spell_review_status"],
                "entry_status": r["entry_review_status"],
                "flags": review_flags,
                "issues": issues_by_entry.get(entry_id, []),
            },
            "provenance": {
                "source_key": r["source_key"],
                "heading": r["heading"],
                "translation_status": r["translation_status"],
                "translation_method": r["translation_method"],
            },
        }
        records.append(record)
        access_counts[access_kind] += 1
        for s in all_sources:
            source_counts[s] += 1
        if review_flags:
            review_records.append({
                "spell_id": r["spell_id"],
                "entry_id": entry_id,
                "name_zh": r["name_zh"],
                "name_en": r["name_en"],
                "source_access": record["source_access"],
                "level_text_raw": level_line,
                "flags": review_flags,
                "issues": issues_by_entry.get(entry_id, []),
            })

    index_dir = out_root / "03_spells" / "index"
    catalog_dir = out_root / "03_spells" / "catalog"
    review_dir = out_root / "03_spells" / "review"
    index_dir.mkdir(parents=True, exist_ok=True)
    catalog_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list[dict]] = collections.defaultdict(list)
    for record in records:
        buckets[record["alphabet"]].append(record)

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        path = index_dir / f"{letter}.jsonl"
        catalog_path = catalog_dir / f"{letter}.jsonl"
        with path.open("w", encoding="utf-8") as f, catalog_path.open("w", encoding="utf-8") as cf:
            for record in buckets.get(letter, []):
                f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
                compact = {
                    "spell_id": record["spell_id"],
                    "name_zh": record["name_zh"],
                    "name_en": record["name_en"],
                    "access": record["source_access"]["kind"],
                    "sources": record["source_access"]["sources"],
                    "levels": [[x["class"], x["level"]] for x in record["levels"]],
                    "level_raw": record["level_text_raw"],
                    "level_source": record["level_source_annotations"],
                    "school": record["school"],
                    "subschool": record["subschool"],
                    "descriptors": record["descriptors"],
                    "review": bool(record["review"]["flags"]),
                }
                cf.write(json.dumps(compact, ensure_ascii=False, separators=(",", ":")) + "\n")

    with (review_dir / "source_and_parse_review.jsonl").open("w", encoding="utf-8") as f:
        for record in review_records:
            f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    sources = sorted(source_counts)
    manifest = {
        "schema": "d100-spell-index-v1",
        "total_spells": len(records),
        "generated_from": db_path.name,
        "source_access_policy": {
            "default": "basic_only",
            "basic_only": "include source_access.kind == basic; ignore source-scoped level variants",
            "selected": "basic + spells/level variants matching selected sources",
            "all": "all spell sources; ambiguous source records remain visible with review flags",
            "semantic_intent": {
                "all_examples": ["我要讀萬法", "萬法模式", "全部法術都看", "擴充全開", "所有書都可以"],
                "selected_examples": ["讀霜燃", "加霜燃之書", "這隻可以用完美奧術"],
                "basic_examples": ["只看基本", "不要擴充", "核心法術就好"],
                "note": "examples are semantic anchors, not exact-string requirements",
            },
            "term_disambiguation": {
                "萬法": "operation alias meaning all registered spell sources",
                "萬法大全": "one concrete source book; selecting it does not imply all sources",
            },
        },
        "access_counts": dict(sorted(access_counts.items())),
        "source_counts": dict(sorted(source_counts.items())),
        "sources": sources,
        "review_record_count": len(review_records),
    }
    (out_root / "03_spells" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("database", type=Path, help="path to spellbook.sqlite")
    ap.add_argument("--out", type=Path, default=Path("."), help="D100 repo/output root")
    args = ap.parse_args()
    manifest = import_spellbook(args.database, args.out)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
