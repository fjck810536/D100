# Current Campaign State

> 尚未建立實際 campaign。本檔先作為 GPT DM 的持久狀態入口。
>
> 只記目前真的成立的 world state 與合法的 Mystery / Relationship / Commitment references；完整 secret payload 不放在這裡。架構見 `../DATA_ARCHITECTURE.md`、`../RUNTIME_SOCIAL_WORLD_CONTRACT.md`、`../MYSTERY_PROTOCOL.md`。

## Campaign

```text
名稱：未設定
模式：一般 D100
當前世界時間：未設定
當前地點：未設定
```

## Party

目前無角色檔。

## Control Mode

```yaml
four_voice_control:
  mode: npc
  mappings: []
```

> 預設 `npc`。只有 DM／使用者明確要求四聲部作為 PL+PC 時才切 `pl_pc`；切換後依 session state 保存 Player Layer working data。

## Active Quests

目前無。

## Important NPCs

目前無。

## Known Facts

目前無。

## Relationship refs

```yaml
relationship_refs: []
```

> 客觀關係 facts 放 Relationship Graph；不要把分析師解讀或政治家 forecast 塞進這裡。

## Evidence refs

```yaml
evidence_refs: []
```

> Evidence status 使用 `OBSERVED / INFERRED / CONFIRMED / DISPROVEN`。玩家推論不因被反覆談論而自動升格為世界真相。

## Secret refs

```yaml
secret_refs: []
```

> 只放 Secret ID 與 current-state 合法取得的 role-safe representation；不得建立平行 `DM Secrets` plaintext 區。

## World Commitment refs

```yaml
commitment_refs: []
```

> 重要 hidden actor / event / secret 在第一次可觀察／可影響前以最小 causal commitment 鎖定；完整未授權 truth core 不重複抄進本檔。

## Site / Hazard refs

```yaml
site_refs: []
hazard_refs: []
```

## Derived refs

```yaml
derived_refs:
  analyst: []
  politician: []
  ecology: []
  other: []
```

> Derived view 可失效，不是 Known Fact。

## Open Threads

目前無。

---

建立正式 campaign 後，這裡只記「目前仍成立的狀態」；完整歷史留在 `sessions/`。Cabinet 對未來行為的推測、政治預後、relationship interpretation、戰術建議或人格分析若需要 cache，必須另標 derived，不可混進 Known Facts。

核心分層：

```text
world / relationship fact
≠ actor epistemic state
≠ evidence inference
≠ Analyst interpretation
≠ Politician forecast
```