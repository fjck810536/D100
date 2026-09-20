#!/usr/bin/env python3
from __future__ import annotations

import json, re
from pathlib import Path

DOMAIN_TOKEN_RE = re.compile(r"([\u4e00-\u9fff]{1,16}領域)")
FULLWIDTH_DIGIT_TRANS = str.maketrans("０１２３４５６７８９", "0123456789")

def load_registry(root: Path) -> dict:
    return json.loads((root/"03_spells/domain_circle_registry.json").read_text(encoding="utf-8"))

def vocab(reg):
    spec=reg["spellbook_domains"]
    names={x["name"] for x in spec.get("domains",[])}
    names.update(x["name"] for x in spec.get("observed_additions",[]))
    return names, dict(spec.get("aliases",{}))

def canon_domain(raw, reg):
    hits=DOMAIN_TOKEN_RE.findall(raw or "")
    if not hits: return None
    names,aliases=vocab(reg)
    base=hits[-1][:-2].strip()
    base=aliases.get(base,base)
    return base if base else None

def recover(raw, reg):
    s=(raw or "").translate(FULLWIDTH_DIGIT_TRANS)
    out=[]
    for m in DOMAIN_TOKEN_RE.finditer(s):
        d=canon_domain(m.group(1),reg)
        if not d: continue
        tail=s[m.end():m.end()+32]
        lm=re.search(r"[^0-9]{0,20}([0-9])(?:\s*級)?",tail)
        if not lm: continue
        lv=int(lm.group(1))
        if 0<=lv<=9:
            out.append({"kind":"domain","class":f"{d}領域","domain":d,"level":lv,
                        "note":"recovered_from_raw_level_text","raw_class":m.group(1)})
    uniq=[]; seen=set()
    for x in out:
        k=(x["domain"],x["level"])
        if k not in seen: seen.add(k); uniq.append(x)
    return uniq

def normalize_existing(level, reg):
    c=level.get("class","")
    d=canon_domain(c,reg)
    if not d:
        z=dict(level); z.setdefault("kind","class"); return z
    z=dict(level)
    z.update({"kind":"domain","class":f"{d}領域","domain":d,"raw_class":level.get("raw_class",c)})
    return z

def process_record(rec,reg):
    levels=[normalize_existing(x,reg) for x in rec.get("levels",[])]
    existing={(x.get("domain"),x.get("level")) for x in levels if x.get("kind")=="domain"}
    added=False
    for x in recover(rec.get("level_text_raw",""),reg):
        k=(x["domain"],x["level"])
        if k not in existing:
            levels.append(x); existing.add(k); added=True
    rec["levels"]=levels
    flags=list(rec.get("review",{}).get("flags",[]))
    if levels and "no_normalized_spell_levels" in flags:
        flags.remove("no_normalized_spell_levels")
    if added and "domain_level_recovered_from_registry" not in flags:
        flags.append("domain_level_recovered_from_registry")
    rec.setdefault("review",{})["flags"]=flags
    return rec

def main():
    root=Path(".")
    reg=load_registry(root)
    review=[]
    repaired=0
    domain_records=0
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ip=root/"03_spells/index"/f"{letter}.jsonl"
        if not ip.exists(): continue
        records=[]
        for line in ip.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            rec=json.loads(line)
            before=json.dumps(rec.get("levels",[]),ensure_ascii=False,sort_keys=True)
            rec=process_record(rec,reg)
            after=json.dumps(rec.get("levels",[]),ensure_ascii=False,sort_keys=True)
            if before!=after: repaired+=1
            if any(x.get("kind")=="domain" for x in rec.get("levels",[])): domain_records+=1
            records.append(rec)
            if rec.get("review",{}).get("flags"):
                review.append({
                    "spell_id":rec["spell_id"],"entry_id":rec["entry_id"],
                    "name_zh":rec["name_zh"],"name_en":rec["name_en"],
                    "source_access":rec["source_access"],
                    "level_text_raw":rec.get("level_text_raw",""),
                    "flags":rec["review"]["flags"],
                    "issues":rec["review"].get("issues",[])
                })
        ip.write_text("\n".join(json.dumps(r,ensure_ascii=False,separators=(",",":")) for r in records)+"\n",encoding="utf-8")
        cp=root/"03_spells/catalog"/f"{letter}.jsonl"
        compact=[]
        for r in records:
            compact.append({
                "spell_id":r["spell_id"],"name_zh":r["name_zh"],"name_en":r["name_en"],
                "access":r["source_access"]["kind"],"sources":r["source_access"]["sources"],
                "levels":[[x.get("class"),x.get("level")] for x in r.get("levels",[])],
                "domains":[[x.get("domain"),x.get("level")] for x in r.get("levels",[]) if x.get("kind")=="domain"],
                "level_raw":r.get("level_text_raw",""),"level_source":r.get("level_source_annotations",[]),
                "school":r.get("school"),"subschool":r.get("subschool"),
                "descriptors":r.get("descriptors",[]),"review":bool(r.get("review",{}).get("flags"))
            })
        cp.write_text("\n".join(json.dumps(r,ensure_ascii=False,separators=(",",":")) for r in compact)+"\n",encoding="utf-8")
    rp=root/"03_spells/review/source_and_parse_review.jsonl"
    rp.write_text("\n".join(json.dumps(r,ensure_ascii=False,separators=(",",":")) for r in review)+"\n",encoding="utf-8")
    mp=root/"03_spells/manifest.json"
    manifest=json.loads(mp.read_text(encoding="utf-8"))
    manifest["domain_circle_registry"]="03_spells/domain_circle_registry.json"
    manifest["domain_normalization"]={"repaired_spell_records":repaired,"spell_records_with_domain_levels":domain_records}
    manifest["review_record_count"]=len(review)
    mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"repaired_spell_records":repaired,"spell_records_with_domain_levels":domain_records,"review_records":len(review)},ensure_ascii=False))

if __name__=="__main__":
    main()
