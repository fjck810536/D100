# 99_open_questions/

> D100 的正式「未決／待設計／待查證」registry。
>
> 這裡不是規則正典，也不是一般 brainstorm 資料夾。只有已確認會影響 runtime、創角、資料契約或世界一致性的未決問題才放進來。

## 使用原則

```text
open question ≠ current rule
open question ≠ DM permission to improvise permanently
resolved question → move answer into the proper core/protocol/source file
resolved provenance may remain here as a short pointer if useful
```

優先級慣例：

- `P0`：會阻塞或明顯污染目前 runtime / legality / state consistency。
- `P1`：重要設計缺口；目前有安全 fallback，可以繼續跑。
- `P2`：改善品質／便利性；不影響目前正確性。

## Current registries

- `character_creation.md` — 創角、CP、語言、qualifying reward 等未決問題。
- `unresolved_rules.md` — 核心／戰鬥／技能／物品等未決規則。
- `social_world.md` — Alignment、角色行為、社會世界與關係層的待設計問題。

## 與 Architecture Audit 的差異

`ARCHITECTURE_AUDIT_*.md` 記錄 migration 歷史、考古與既有架構債；
`99_open_questions/` 則是目前仍需要回答的 active design / rules gap。

不要把同一問題同時維護成兩份平行 TODO。
