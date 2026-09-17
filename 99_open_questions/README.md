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
- `social_cognition_frameworks.md` — 外部 social / cognition / memory framework 的取樣評估；追蹤 Cognitiv、Ensemble/CiF、ZifaMem、FAtiMA、Emotion Engine 與現有 Cabinet / state layer 的可能接口，以及 D100 / 3.5 既有尺度審計。
- `economy.md` — 平民／勞工／專業者收入、基本生活開銷、可支配所得與日常經濟常識基線。
- `runtime_playtest.md` — 實際跑團暴露出的 runtime interface / timing / investigation 缺口；只收可泛化問題，不收單一 session 尚未填完的普通 state。

## Resolved incident records

以下可以保留完整考古／對話，**但不再代表 active open question**：

- `librarian_routing_incident_2026-09-15.md` — 原始事故／對話保存；檔內的 `OPEN` 是當時的歷史狀態。
- `librarian_routing_resolution_2026-09-16.md` — 已採用的修正：active source resolution、cross-reference、grounded generation、typed deferral、provenance、active delivery 與 completion contract。

若兩者對「目前 runtime 應怎麼做」描述不同，以 resolution 與已更新的 `AGENTS.md / DATA_ARCHITECTURE.md / DM_PROTOCOL.md / DM_CABINET.md / RUNTIME_SOCIAL_WORLD_CONTRACT.md` 為準。

特別注意：原 incident 的中間結論「未找到安道爾法術學院完整機構名」已被更深的 cross-reference 查核推翻；目前 source-backed referent 是 `安道爾帝國魔法學院`，來源在世界觀 mirror 的 `賽爾紅袍協會` 條目。

## 與 Architecture Audit 的差異

`ARCHITECTURE_AUDIT_*.md` 記錄 migration 歷史、考古與既有架構債；
`99_open_questions/` 則是目前仍需要回答的 active design / rules gap。

不要把同一問題同時維護成兩份平行 TODO。
