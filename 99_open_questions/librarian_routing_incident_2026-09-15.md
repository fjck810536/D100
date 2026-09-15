# Librarian Routing Incident — 2026-09-15

> Status: OPEN / transcript preserved before runtime redesign.
>
> Purpose: preserve the full discussion that exposed a missing Librarian dispatch / lore-provenance routing step in PL+PC runtime. This file is evidence for later design work; it is **not** itself a finalized runtime rule.

---

## Incident context

The issue emerged during Andor Session 1 after Elian used several setting-specific terms in ordinary PC dialogue, including:

- 低語學派 / 低語學院
- 三大議會
- 安道爾法術學院

The generated scene continued using these terms without a traceable Librarian / Source Resolver dispatch.

---

## Full conversation transcript

### GM

DM:那麼那段進度有個比較尷尬的地方是，生成模式漏掉了這句有可能是蟬作為pl在對我作為pl的場外對話，只是混進台詞。這個可能會在代理pl+pc層面有點小bug?

雖然不是很大，有時候屬於ooc也會發生在實際團裡面，所以我判斷是，可以在待辦事項放一個ooc情況，然後紀錄有發生過的ooc事件。但先不做調整。

而另外一個問題，當我過去說到「低語學院」、「三大議會」「安道爾法術學院」時，有模塊向圖書管員申請調度資料嗎？

### Assistant

對，這裡確實有兩個不同層級的小 bug。

第一個我已經照你的意思**只登記、不修 runtime**。現在在：

`99_open_questions/runtime_playtest.md`

新增：

\[
\boxed{\text{P1-RUNTIME-4 — PL+PC 模式下的 OOC / IC 語句分類與台詞滲漏}}
\]

而這次實例也單獨記成：

```text
OOC-AMBIG-ANDOR-001
```

就是你指出的那句：

> 「不過你說『傳授吟遊詩人的技法』……你以前學過？還是你現在才突然想當一個？」

它現在被標成 `OOC_AMBIGUOUS`：**有可能是蟬作為 PL 在場外問你，卻被 renderer 包成 Nella 的 IC 台詞。**不回溯改場景，也不拿這句去推導 Nella 的關係、心理或角色知識。之後再有類似案例就累積樣本。

---

第二個問題更值得注意。

### 當你提到「低語學派／三大議會／安道爾法術學院」時，有沒有模塊找圖書館員？

**沒有。**

我重新對過這段實際執行。沒有發生：

\[
\text{某模塊}
\rightarrow
\text{Librarian request}
\rightarrow
\text{source lookup}
\rightarrow
\text{provenance response}
\]

而 `DM_CABINET.md` 對圖書館員的定位明明就是 **Source Resolver**：管 Sheet、repo、角色卡、版本歷史、3.5 來源等，回答「我們已經知道什麼／去哪裡知道」，並回傳來源層級與衝突。

所以這段實際上發生的是：

\[
\boxed{
\text{玩家說出設定專有名詞}
\rightarrow
\text{生成器直接把它當作可沿用的世界設定}
}
\]

而不是：

\[
\boxed{
\text{玩家說出專有名詞}
\rightarrow
\text{先判斷它是角色發言／玩家設定／既有 canon？}
\rightarrow
\text{Librarian 查來源}
\rightarrow
\text{AO 決定可用到什麼程度}
}
\]

這造成的污染程度三者還不太一樣。

**「低語學派」其實比較輕。**後來的敘事基本只是「Elian 想找低語學派」「Nella 說如果真的有這種人在這裡……」，所以它還可以維持為：

\[
\text{Elian 知道／相信有這個概念}
\]

而不必推出：

\[
\text{安道爾一定存在低語學派}
\]

但 **「三大議會」「安道爾法術學院」問題比較明顯**。我後來在地圖敘述裡直接生成了：

> 三大議會在中央行政／權力區  
> 安道爾法術學院在正式學術／行政側

這些已經不是單純重述你的台詞，而是在**沒有來源調度的情況下新增世界地理資訊**。

所以你這次抓到的其實是一個很具體的 routing 缺口：

\[
\boxed{
\text{setting-specific proper noun}
\not\Rightarrow
\text{Librarian trigger}
}
\]

我認為正常流程應該是：

```text
玩家／PC 提到專有名詞
        ↓
它只是角色知道／相信／聲稱嗎？
        ↓
若 narrator / AO 要據此生成客觀世界資訊
        ↓
Librarian resolve provenance
        ↓
已有來源 → 讀來源
找不到 → 標 source gap
玩家剛建立 → 判斷是否為 explicit world contribution
        ↓
AO 才能生成／commit 客觀狀態
```

尤其一句 IC 台詞：

> 「三大議會那些高塔裡的怪人」

最低限度只保證：

\[
\boxed{\text{Elian 說了這句}}
\]

未必自動保證：

\[
\boxed{\text{三大議會真的有三座高塔，而且位於某區}}
\]

除非它早就是 canon，或 DM／玩家是在明確建立設定。

所以第二個我會判定為**真實的 Librarian dispatch miss**，不是單純「圖書館員剛好沒出場」。目前我還沒有替你把它寫進 `99_open_questions`，因為你這一則明確要求登記的是 OOC；但如果要登，它應該獨立成類似：

\[
\boxed{\text{P1-RUNTIME-5 — Setting proper noun / lore provenance 的 Librarian 自動調度邊界}}
\]

而不是跟 OOC 混在一起。

---

### GM

這個問題還沒問完：
計畫：
首先我們知道這個台詞沒有任何模塊調度圖書館
那我們要找原因
並且先跑一次調度圖書館後得知的結果

我已知道有幾個答案，但你們不能先從我的答案去反向回推：故不做回答

目標：
找到適當流程

### Assistant — progress note

可以。這次我不把你的已知答案當線索，只從 runtime 本身找。先做兩件事：**追出「什麼情況會喚起圖書館員」的現行路由條件**，再把同一句話重新送進一次圖書館員，看看它實際能回傳什麼、在哪一步應該停。

### Assistant — progress note

我已經找到第一個原因：現行文件只寫「**只召喚需要的 Cabinet 模塊**」「圖書館員負責來源／provenance」，但**沒有定義什麼語句型態會自動把『玩家提到專有名詞』判成需要 Source Resolver**。也就是職責有寫，觸發器沒寫；生成器因此直接把詞當成可用世界詞彙往下接。現在我跑一次真正的 Librarian pass。

### Assistant — progress note

這次真正的 Librarian pass 已經出現一個前面完全漏掉的訊號：`sources/sheet_mirror/` 本身就有 **`09_吟遊詩人特殊專長.json.md`**，以及 **`01_world_core.json.md`**。所以「repo 全文搜尋沒命中」不能當作查無資料；圖書館員的保險絲「找不到 ≠ 不存在」在這裡正好被驗證。我現在直接讀語義上最可能的原始來源。

### Assistant — progress note

調度結果已經很有辨識力了：**低語學院與三大議會都不是空白詞，而是 raw Sheet 正典；「安道爾法術學院」則目前只找到「安道爾」與其他法術／魔導學院概念，沒有找到這個完整專名。**所以問題不是「圖書館員查不到」，而是 orchestrator 根本沒把這句話送給它，而且現行流程還缺一個「玩家台詞中的世界知識 claim 要不要驗證」的中介步驟。

### Assistant

對，現在可以把問題拆得很清楚了，而且這次結果證明：**不能用「玩家說出專有名詞 → 當成設定」；但也不能反過來做成「每個專有名詞都查圖書館員」**。真正需要的是中間那個 routing gate。

### 1. 為什麼當時沒有調度圖書館員

目前架構其實把「圖書館員能做什麼」寫得很完整：它是 Source Resolver，負責 provenance、來源層級、衝突與缺口。`DATA_ARCHITECTURE.md` 也明確規定 Source → State → Module View → AO 的資料流。

但主持流程只寫了：

> 讀 authoritative state → commitment → role-safe view → 描述 → 玩家宣告 → 判定……

沒有一步叫：

> **「玩家／PC 剛剛說出的世界知識，接下來若要被 narrator 當客觀事實使用，先做 provenance resolution。」**

而 `START_DM.md` 又只說「只召喚需要的 Cabinet 模塊」，raw Sheet 是「按需讀」；`SHEET_INDEX.md` 甚至不在最低必讀集裡。

所以漏點其實是：

\[
\boxed{
\text{Librarian duty 有定義}
\quad+\quad
\text{Source database 有資料}
\quad-\quad
\text{Lore claim trigger 沒定義}
}
\]

還有第二個較小的問題：剛才直接做 repo code search，三個詞全部零結果；但往 `SHEET_INDEX` 做**語義導航**後，馬上找到正確 raw mirror。`SHEET_INDEX` 本來就明寫 31/31 tabs 已完整 mirror，而且「世界觀／大陸簡史」在 `01_world_core`、「吟遊詩人特殊專長」在 `09_吟遊詩人特殊專長`。

所以圖書館員自身還需要遵守：

\[
\boxed{\text{全文搜尋 miss} \neq \text{source miss}}
\]

---

## 2. 現在真的跑一次 Librarian，結果是什麼

結果比剛才我們以為的豐富很多。

| 玩家提到的詞 | Librarian resolution |
|---|---|
| **低語學派** | **有 D100_CANON 高度對應**，Sheet 正式名稱是「低語學院」 |
| **三大議會** | **直接 D100_CANON** |
| **安道爾法術學院** | **複合專名目前未確認**；「安道爾」是 canon，「法術學院／魔導學院」概念存在，但沒有查到這個完整機構名 |

### 低語學院

這個特別漂亮。

`吟遊詩人特殊專長` Sheet 明寫：

> 可從「迷惑學院、劍歌學院、低語學院」選擇進行樂理研究，而且學習必須吻合劇情進展或角色背景。

而低語學院自己的描述也真的就是：

- 表面像普通吟遊詩人；
- 分享新聞、唱歌、講軼事；
- 實際利用知識與魔法揭露秘密；
- 用秘密恐嚇／勒索；
- 常隱藏真正學院身分；
- 混入皇室與權力中心。

所以你剛才講：

> 有的人藏在漂亮衣服、面具、歌曲、舞蹈下。

其實**非常貼近 D100 原 Sheet**。

但 Librarian 應該回傳一個 alias warning：

\[
\text{玩家用詞：低語學派}
\]

\[
\text{Sheet 正式詞：低語學院}
\]

可以判斷高度可能指同一概念，但不能偷偷把兩者永久正規化成 alias，除非後續確認。

---

### 三大議會

這更直接。

Sheet 世界觀本來就反覆寫「三大議會」；暗殺者協會與盜賊協會甚至都有「不碰三大議會有席次人物」的慣例。

大陸簡史還寫了：

\[
500年：
\text{魔導學院＋鍊金議會＋萬神殿建立}
\]

接著：

\[
700年：
\text{三大議會開始發行世界貨幣}
\]

之後一路有介入大陸戰爭、統治半位面、封閉、再分別重啟的歷史。

因此：

> 「三大議會」

可以安全當世界 canon。

可是：

> 「三大議會那些**高塔**裡的怪人」

要拆成：

\[
\boxed{\text{三大議會＝CANON}}
\]

\[
\boxed{\text{高塔＝目前未找到來源；只能先算 Elian 的說法}}
\]

不能因一句角色台詞就替三大議會蓋三座塔。

---

### 安道爾法術學院

Sheet 對**安道爾**本身其實資料很多：

- 奈瑟殘存王族作虛位帝王；
- 上下議院；
- 下議院有實權；
- 下議院實際高度受法師把持；
- 施法者政治權重與一般公民不同；
- 自居奈瑟繼承者。

但是「**安道爾法術學院**」這個完整專名，我這輪沒有找到 canon source。

Sheet 確實另有：

- 「法術學院」這個一般概念；
- 「魔導學院」這個非常重要的組織；

但不能因此做：

\[
\text{安道爾}+\text{法術學院}
\Rightarrow
\boxed{\text{安道爾法術學院一定存在}}
\]

所以先前我把它直接畫進城市地圖，是不應該發生的 objective expansion。

---

## 3. 這讓正確流程變得很清楚

我認為最適合的不是：

\[
\text{Proper noun}
\Rightarrow
\text{永遠召 Librarian}
\]

那會太重。

應該是設一個 **Lore Claim Gate**：

```text
玩家輸入
↓
先分類 utterance layer
DM / OOC-PL / PC台詞 / PC內心 / 行動宣告
↓
抽出其中的 world claims / proper nouns
↓
「這一輪只需要保留成角色說過／相信的內容嗎？」
├─ 是 → 不必查 Librarian
│      寫入 actor epistemic / dialogue 即可
│
└─ 否，narrator / NPC / AO 準備把它當客觀世界資訊使用
       ↓
   Librarian Source Resolution
       ↓
   ┌ EXACT_CANON
   ├ SESSION_COMMITTED
   ├ ALIAS_CANDIDATE
   ├ DERIVED_ONLY
   ├ AMBIGUOUS
   └ SOURCE_GAP
       ↓
   Mystery / role-safe filter（若需要）
       ↓
   AO 才能據此生成客觀世界反應
```

這個 trigger 的核心不是「看見專有名詞」，而是：

\[
\boxed{
\text{系統正準備把一個玩家／角色提出的 claim，
從「他說了」升格成「世界是真的」}
}
\]

**就在升格前調 Librarian。**

---

### 4. 用你那一句實際跑流程

例如 Elian 說：

> 「不論三大議會那些高塔裡的怪人，或者安道爾法術學院那群看不起人的傢伙……」

第一階段完全不用查：

```text
FACT:
Elian 說了這句話。
```

如果 Aster只回答：

> 「你似乎不太喜歡那些地方。」

也不用查。

因為 Aster只是在回應 **Elian 的態度**。

可是如果 narrator 下一句準備寫：

> 「三大議會的三座高塔就在城市中央。」

立刻觸發 Librarian。

結果：

```text
三大議會 → CANON
三座高塔 → SOURCE_GAP
```

所以只能寫已知部分，不能補塔。

又例如 NPC 要說：

> 「安道爾法術學院就在鐘樓東邊。」

也必須先查。

結果：

```text
安道爾 → CANON
施法教育機構概念 → 有來源
「安道爾法術學院」這個具體機構 → UNRESOLVED
地理位置 → UNRESOLVED
```

因此 NPC 除非本身是在**提出 belief / rumor**，否則 narrator 不能讓這句直接變世界事實。

---

## 5. 我現在認為真正缺的不是「圖書館員自動搜尋專有名詞」

而是兩個很小的 orchestrator interface：

\[
\boxed{\text{Lore Claim Classification}}
\]

負責：

> 這只是 actor claim，還是我們準備把它升格成 world fact？

以及：

\[
\boxed{\text{Source Resolution Trigger}}
\]

負責：

> 一旦要升格，就必須先過 Librarian。

這樣圖書館員不會每句都跑，又不會再發生這次的問題。

而且這也順便解決你剛才的 OOC bug：**第一關本來就要先判斷這句到底屬於 PL、PC、DM 還是 narrator。**只要 utterance layer 沒分清楚，後面無論是圖書館員、分析師還是 AO 都可能吃錯資料。

所以我目前會把理想架構壓成：

\[
\boxed{
\text{Utterance classification}
\rightarrow
\text{Lore claim gate}
\rightarrow
\text{Librarian provenance}
\rightarrow
\text{Mystery view}
\rightarrow
\text{AO/world use}
}
\]

而不是單純：

\[
\text{看到專有名詞}\rightarrow\text{查資料庫}
\]

這一輪我**先不修改 runtime 文件**。因為現在我們已經找到了原因、跑完第一次實際調度，也得到一個可測試的候選流程；下一步比較適合拿幾個反例壓它，看這個 gate 會不會太敏感或漏東西，再決定寫進哪個上位契約。

---

## Current design status

No runtime adjustment has been adopted yet.

Candidate architecture under test:

```text
Utterance classification
→ Lore claim gate
→ Librarian provenance
→ Mystery / role-safe view
→ AO / world use
```

Open questions include:

- what counts as a lore/world claim worth routing;
- whether actor claims should ever trigger Librarian before world-use escalation;
- how aliases are represented without silently normalizing player wording;
- how rumor / belief / mistaken lore should be preserved without contaminating world fact;
- whether `SHEET_INDEX.md` should become mandatory navigation for Librarian source resolution;
- how this routing interacts with OOC / PL / PC utterance classification.
