# Training Plan — August 31 – September 6, 2026 (Act on the FTP answer)

```json
{
  "plan_version": "1.0",
  "phase": "Base",
  "phase_week": 2,
  "theme": "Last week's 4x8 was built to answer the FTP question and it did: 195 W is above MLSS. This week spends that answer. Every intensity target is rebuilt off a working FTP of 190 W, not the stale 211. Sunday takes the long ride as a one-week weather exception; the standing Sunday rest resumes 13 Sept.",
  "readiness_at_generation": "latest.json synced 2026-08-30 09:54. P2 modify - HRV 25.0 red (-20.4% vs 31.4 baseline), RHR 58 amber (+3.9), sleep 7h10m quality 4. Aug 30 long ride NOT ridden (athlete call, endorsed). Start state Aug 31: CTL 30.75 / ATL 29.56 / TSB +1.2, ACWR 0.69 (undertraining).",
  "load_target_TSS_cycling": "~357",
  "volume_hours_cycling": "~8.6",
  "quality_sessions": 2,
  "long_rides": 1,
  "session_templates": ["AE-1", "TH-2", "AE-4", "SS-1", "AE-6"],
  "progression_vector": "ftp_reanchor (working FTP 211 -> 190) + consecutive_day_endurance",
  "FTP_zwift_setting": 211,
  "FTP_working": 190,
  "eFTP": 193.3,
  "LTHR": 154,
  "intensity_basis": "Indoor = power, expressed as % of the Zwift FTP setting 211 so the files land on the intended absolute watts. Outdoor = HR only (no power meter on the Condor)."
}
```

**Generated:** 2026-08-30 · Zwift FTP setting **211 W** (unchanged, leave it) · **Working FTP 190 W** (new) · eFTP 193.3 · LTHR 154 · Max HR 170 · Weight 82.3 kg · data synced **2026-08-30 09:54**

---

## The FTP re-anchor — read this first

Thursday 28 Aug, TH-2 4×8 at 195 W: **194 / 192 / 171 / 174 W.**

Reps 1 and 2 were clean, HR 141–145. Reps 3 and 4 came in **11% low with HR still pinned at 144–145**, and session decoupling was **13.9%** — well past the 10% flag. That is not pacing. That is the signature of working above MLSS: you can rent 195 W for 16 minutes, you cannot own it for 32.

The 26 Aug plan called this branch in advance — *"rep 3 or 4 sags below 185 W → threshold sits nearer eFTP; working FTP drops."* It has been triggered.

| | Old | New |
|---|---|---|
| Prescription FTP | 211 W (set 3 Jun, 88 days stale) | **190 W** |
| eFTP | 195 | 193.3 |
| Threshold reps | 195 W | **185 W** (97%) |
| Sweet spot | "170 W = tempo" | **172 W = sweet spot** (91%) |

The second row of that table is the interesting one. **172 W did not change — its meaning did.** Against 211 it read as 82% and got labelled tempo; against 190 it is 91%, textbook sweet spot. Two months of sessions were mis-labelled because the denominator was wrong, not because you rode them badly.

⚠️ **Do not change your Zwift FTP setting.** Leave it at 211. The `.zwo` files express every target as a percentage of 211 and already resolve to the correct absolute watts. Changing it will scale everything wrong.

---

## Goals audit

*Deficit status: **active** — HRV drop is 1 day (persistence 1), not the sustained >20% that suspends it under SECTION_12 §7.*

| Goal | Target | Now | Rate | Status |
|---|---|---|---|---|
| **Weight** → 80 kg | −0.3 to −0.5 kg/wk | 82.3 kg latest, **82.9 kg 7d avg** — 2.9 kg to go | **−0.56 kg/wk** (28d slope) | 🟢 back in band — was −1.05 on 16 Aug |
| **CTL** → 36–38 by mid-Sept | 36 by ~15 Sept | 30.75 | projects to **34.4** by 6 Sept | 🟡 on track — one more week like this lands 36–37 |
| **FTP** → 230 W | 230 by end 2026 | **190 working** (was 211 nominal) | −21 W on re-anchor | 🔴 the number went *down*. Say it plainly. |
| **Long ride** 3h+ sustained Z2 | duration + HR floor 118 | last: 3h02 on 16 Aug, **94.8% in Z1**; 30 Aug skipped | 0 for 3 attempts | 🔴 **the floor has still never been ridden** |
| **Back-to-back days** | consecutive training days | Sat 5 + Sun 6 pair | 4 straight last week | 🟢 |

**The FTP row needs saying without hedging.** 190 is not a failure — 211 was never measured under load, it came from a June ramp test, and ramp tests over-read for endurance athletes (SECTION_11 §Testing Protocol says exactly this). You have not lost 21 W. You have found out you never had them. Every autumn target now rebuilds off a number that four hard reps actually defended.

---

## The week

| Day | Session | Target | Modality | Duration | Est. TSS |
|---|---|---|---|---|---|
| **Mon 31 Aug** | **AE-1 steady Z2** — reopening ride | 135 W · HR 117–127 · RPE 3–4 | 🏠 Zwift | 75 min | 48 |
| **Tue 1 Sep** | **TH-2 Seiler 4×8 @ 185 W** ⚡ the anchor test | 185 W · HR 143–152 · RPE 6–8 | 🏠 Zwift | 78 min | 72 |
| **Wed 2 Sep** | **AE-4 active recovery** | 120 W · HR <115 · RPE 2–3 | 🏠 Zwift | 50 min | 26 |
| **Thu 3 Sep** | **SS-1 sweet spot 3×15 @ 172 W** ⚡ | 172 W · HR 132–142 · RPE 6–7 | 🏠 Zwift | 86 min | 75 |
| **Fri 4 Sep** | **REST — standing** | — | Rest | — | 0 |
| **Sat 5 Sep** | **AE-1 Z2 primer** | 132 W · HR 115–125 · RPE 3 | 🏠 Zwift | 60 min | 36 |
| **Sun 6 Sep** | **AE-6 fast-finish long ride** 🔑 priority | **HR floor 118**, ceiling 131 · finish 2×10 @ 132–140 | 🚲 Outdoor | 2h45–3h | ~100 |
| **Total** | 6 rides | | | **~8h35** | **~357** |

### Projected load

| Date | TSS | CTL | ATL | TSB | ACWR |
|---|---|---|---|---|---|
| Mon 31 | 48 | 31.1 | 32.2 | −1.1 | 0.84 |
| Tue 1 | 72 | 32.1 | 37.9 | −5.8 | 1.10 |
| Wed 2 | 26 | 31.9 | 36.2 | −4.3 | 1.25 |
| Thu 3 | 75 | 32.9 | 41.7 | −8.8 | 1.28 |
| Fri 4 | 0 | 32.1 | 35.7 | −3.6 | 1.04 |
| Sat 5 | 36 | 32.2 | 35.7 | −3.5 | 1.15 |
| **Sun 6** | 100 | **34.4** | 44.9 | −10.5 | **1.44** |

**On that 1.44.** It breaches the 1.3 gate and I am not going to pretend otherwise — but read *why*. ACWR is a ratio, and its denominator is a 28-day window with a nine-day holiday hole punched through it. The absolute numbers it is describing are modest: peak ATL 44.9, peak TSB −10.5, a week of 8h35. You ran ATL 44.0 and TSB −10.6 on 17 Aug with no ill effect. This is arithmetic, not overreach.

Said once, as agreed: **if Sunday morning's readiness comes back `modify` or worse, drop the fast finish and ride the floor only.** That is the whole contingency.

---

## ⚡ Tuesday is the test of the new number

4×8 at 185 W. The question is not whether you can ride 185 W — you rode 194 twice last week. **The question is whether rep 4 looks like rep 1.**

| Outcome | Reading | Next |
|---|---|---|
| Four reps within 3%, RPE 6–8, HR 143–152 | 190 W is the right anchor | Build volume off it — 4×10 the week after |
| Rep 4 sags below 175 W again | Threshold is nearer 180 | Drop once more. Say so, don't grind. |
| All four at RPE ≤5 | 190 is too soft | We go back up — flag it |

Abort rule: can't hold 175 W on rep 3 → stop the set, spin easy, log it. Thursday and Sunday both need you.

---

## 🚲 Sunday — the floor, third attempt

Three long rides in a row have been ridden as Z1. 16 Aug: 3h02, avg HR **110** against a 131 ceiling, 2h52 of it below Z1. 30 Aug: not ridden. This is now the single most behind-schedule item in the whole plan, and it is the most MDS-transferable thing on the list.

- **HR floor 118, ceiling 131.** If your 30-minute average is under 118, lift the pace. That is the instruction, not a suggestion.
- **Fast finish:** last 45 min, **2 × 10 min at HR 132–140**, 5 min easy between.
- Duration floor 2h15, target 2h45–3h.
- No power meter on the Condor — HR is the whole instrument.

---

## Schedule note

**Sunday 6 Sept is a one-week exception**, taken because next weekend's weather put the long ride there. The DOSSIER rule — *Sunday structural rest, non-negotiable as of 2026-05-17, long ride on Saturday* — is **unchanged and resumes 13 Sept**. Friday 4 Sept keeps its standing rest.

---

## Reference zones — rebuilt off working FTP 190 W

| Zone | Power (working 190) | as % of Zwift 211 | HR (LTHR 154) | Used this week |
|---|---|---|---|---|
| Z1 recovery | <105 W | <50% | <111 | recoveries, Wed |
| Z2 endurance | 105–150 W | 50–71% | 111–131 | Mon, Sat, Sun main |
| Z3 tempo | 151–171 W | 72–81% | 132–142 | Sun fast finish |
| Sweet spot | 167–179 W | 79–85% | 138–147 | **Thu 3×15 @ 172 W** |
| Z4 threshold | 180–200 W | 85–95% | 143–154 | **Tue 4×8 @ 185 W** |
| Z5 VO₂max | 201–228 W | 95–108% | 155+ | — |
