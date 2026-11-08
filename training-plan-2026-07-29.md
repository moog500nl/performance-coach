# Training Plan — July 29 – August 2, 2026 (Re-entry block: maximum safe cycling load, 4 days on / 1 off)

```json
{
  "plan_version": "2.1",
  "phase": "Base",
  "phase_week": 1,
  "theme": "Athlete request: cycling only, hardest safe week available. Four consecutive riding days off an 18-day layoff, then firm Sunday rest. v2.1 swaps Wed and Thu — Wednesday is warm (25–28°C) so it goes outdoor Z2, and the week's only quality session moves to Thursday indoors. Load, structure and ceiling are otherwise unchanged. Loaded walking deferred at athlete request, not cancelled.",
  "readiness_at_generation": "P3 GO — 6 green, 0 amber, 0 red. HRV 30.0 (+1.4% vs 7d baseline), RHR 49 (-3), sleep 7h26m, TSB +18.0, ACWR 0.0.",
  "load_target_TSS_cycling": "~295",
  "volume_hours_cycling": "~7.6",
  "quality_sessions": 1,
  "long_rides": 1,
  "loaded_walks": 0,
  "FTP": 211,
  "LTHR": 154,
  "intensity_basis": "Indoor = power (FTP 211 W, set Jun 3). Outdoor = HR only (no power meter on the Condor)."
}
```

**Generated:** 2026-07-28 · **Revised 2026-07-28 (v2.1 — heat swap)** · FTP **211 W** (set Jun 3) · LTHR 154 · Max HR 170 · Weight 87.8 kg (logged Jul 15) · CTL 26.1 / ATL 8.1 / TSB **+18.0** · ACWR 0.0 · data synced **2026-07-28 18:02**

> ⚠️ **Data discrepancy:** you report your last ride as **Jul 14**; Intervals.icu's newest ride is **Jul 11** (Amsterdam, 70.3 km, 171 TSS). Nothing between Jul 12 and Jul 20 exists in the data except a walk on Jul 13. A Jul 14 ride therefore never uploaded, and CTL 26.1 is marginally understated (~0.5 CTL at most — it does not change any number below). Worth chasing in Garmin Connect. `history.json` is also stale since Jul 3 — run `run_history_sync.bat`.

---

## What changed in v2.1

Wednesday is warm (25–28 °C), and your indoor setup is one fan and no air conditioning. Doing the week's only hard session in a hot room is the worst version of that session: HR hits the 150 cap early, power sags to protect it, and you get the fatigue of a quality day without the stimulus. Your Jun 18 indoor ride drifted 8.3% in a heatwave — that's the failure mode.

**So Wednesday and Thursday swap.** Wednesday goes outdoors at Z2, where 25–28 °C with a breeze is fine and the aerobic work is unaffected. The sweet spot moves to Thursday, indoors, back to normal conditions.

**Nothing else moves.** Same four days, same ~295 TSS, same 3.5 h Saturday, same Sunday rest. The one structural consequence is that the quality session now sits **48 h before the long ride instead of 72 h**, with an easy Friday between them. That's the dossier's normal spacing pattern and it's fine — but it makes Friday's gate matter more than it did, and Friday is now the first place fatigue can show up. See the gates.

Peak ACWR moves from 1.30 to **1.31** — a rounding-level difference from the reordering, not a real change in exposure.

---

## Why the two indoor sessions stay indoor

You asked for outdoor, and two of four rides are. The other two are indoor for concrete reasons, not preference:

- **Thursday's sweet spot needs power precision.** 85% FTP by heart rate on flat Amsterdam roads is guesswork, and heat-elevated HR makes it worse guesswork.
- **Friday's steady ride is the only session that can produce a durability reading.** It needs ≥60 min steady with power at VI ≤ 1.05. Your durability metric has **0 qualifying rides in 7 days and 1 in 28** — outdoor rides have no power meter, so they can never qualify.

---

## Reference zones (FTP 211 W · LTHR 154 · Max HR 170)

**Indoor (Zwift — power):**

| Target | Power | Expected HR |
|--------|-------|-------------|
| Recovery between intervals | ~116 W (55%) | < 120 bpm |
| Steady Z2 | 137–141 W (65–67%) | ~117–125 bpm |
| **Sweet spot** | **179 W (85%)** | **138–148 bpm, hard cap 150** |

**Outdoor (HR-guided — no power meter):**

| Zone | HR guide | Feel |
|------|----------|------|
| Z2 Endurance | 120–131 bpm | Steady, full sentences throughout |
| **Hard ceiling (Wed + Sat)** | **135 bpm** | Above this you are no longer following the plan |

---

## The week

| Day | Session | Target | Modality | Duration | Est. TSS |
|-----|---------|--------|----------|----------|----------|
| **Wed Jul 29** | **Z2 endurance** ☀️ — warm-day ride, flat route, no surges, no segments | 120–131 bpm | 🚲 Outdoor | 90 min | ~50 |
| **Thu Jul 30** | **SS-5 4×10 Sweet Spot @ 179 W** — the week's only quality; ladder restarts one rung down | 179 W / HR cap 150 | 🏠 Zwift | 81 min | ~74 |
| **Fri Jul 31** | **Steady Z2 durability benchmark** 137→141 W, VI ≤ 1.05 — pre-loads Saturday *and* measures vs Jul 9 | 137–141 W | 🏠 Zwift | 75 min | ~51 |
| **Sat Aug 1** | **LONG RIDE — Z2, 3.5 h** on tired legs. The week's centrepiece | < 131 bpm, cap 135 | 🚲 Outdoor | **3.5 h** (3 h floor) | ~120 |
| **Sun Aug 2** | **Rest — firm, non-negotiable** | — | Rest | — | 0 |
| **Total** | 4 rides (2 outdoor, 2 indoor), 4 consecutive days | | **~7.6 h** | **~295 TSS** |

### Load model — where the ceiling binds

| Day | TSS | CTL | ATL | TSB | ACWR |
|-----|-----|-----|-----|-----|------|
| Wed | 50 | 26.7 | 14.1 | +12.6 | 0.53 |
| Thu | 74 | 27.8 | 22.7 | +5.1 | 0.82 |
| Fri | 51 | 28.4 | 26.7 | +1.6 | 0.94 |
| **Sat** | **120** | **30.5** | **40.0** | **−9.5** | **1.31** ← ceiling |
| Sun | 0 | 29.8 | 34.3 | −4.5 | 1.15 |

CTL 26.1 → **~29.8** in five days, finishing with TSB near neutral. A +3.7 CTL week — better than any single week of your pre-holiday block, and it flips the ramp rate from −4.74 to positive in one go.

**The one thing that breaks this model:** Saturday drifting. Jul 11's ride averaged **132 bpm** — above the Z2 ceiling. Repeat that for 3.5 h and Saturday becomes ~150 TSS, ACWR hits **1.40**, and you've bought an amber Monday instead of a strong August. The discipline on Saturday *is* the safety margin.

### ☀️ Wednesday heat notes (25–28 °C)

Warm, not dangerous — no structural change needed, but three things:

- **Ride before ~11:00 or after ~19:00** if the day allows. Mid-afternoon adds heat load for no training benefit.
- **HR governs, speed does not.** At 25–28 °C your HR sits 3–7 bpm higher for the same effort. Hold 120–131 bpm and accept that you're going slower than the same ride in May. Chasing your usual average speed is how a Z2 ride becomes tempo.
- **Fluid: ~750 ml/h with sodium**, and start drinking in the first 15 minutes. You haven't ridden in over two weeks — your fluid habits are as rusty as your legs, and Thursday's session runs on how well you rehydrate tonight.

---

## What the data said (and how the week answers it)

| Signal | Reading | Response in this plan |
|--------|---------|----------------------|
| TSS last 7 days | **0** — last recorded ride Jul 11 | Four riding days: frequency rebuilds after a layoff, not any single big session |
| CTL / TSB | 26.1 (was 31.0 on Jul 5) / **+18.0** | Fresh, not fatigued — why a 295-TSS week is available at all |
| Readiness | P3 GO, 6/6 green. HRV 30 (+1.4%), RHR 49 (−3), sleep 7h26m | Green light genuinely supports the aggressive version |
| HRV pattern (7d) | 26 → 29 → 29 → 28 → 28 → **37** → 30 | Rising, not a sawtooth. Two ~4.5 h nights (Jul 22, 24) fully resolved — travel, not stress |
| Ramp rate | −4.74 | A +3.7 CTL week reverses it without a spike |
| Durability metric | 0 qualifying rides in 7d (need 3), 1 in 28d (need 5) | Friday is purpose-built to qualify; benchmarks against Jul 9 (avg HR 123 @ 137 W) |
| Jul 8 sweet spot (3×15) | Executed well before the break | Restart at 4×10 with an earned extension — back past 3×15 by mid-August |
| Jul 11 long ride | 70 km, **avg HR 132** — above Z2 ceiling | Saturday's hard cap is 135 bpm; that ride's intensity is exactly what breaks this week's model |
| Jun 18 indoor ride | 8.3% HR drift in a heatwave | Why Wednesday's quality session moved outdoors and became Z2 |
| Weight | 87.8 kg, last logged Jul 15 | Already inside the October target. Weigh in Wednesday — 13 days blind |

---

## Goals audit (vs DOSSIER §1 / §8)

| Goal | Target | Now | Required rate | This week's contribution | Status |
|------|--------|-----|---------------|--------------------------|--------|
| **Weight** | 88–90 kg by Oct | 87.8 kg (Jul 15) | — | Maintenance; 7.6 h riding | **Already met** 🟢 |
| **CTL** | 50–60 by Sep | 26.1 | +2.7/wk to reach 50 by Sep 30 | ~295 TSS → CTL **~29.8** (+3.7) | Best week available, still short 🟡 |
| **FTP** | 230 W by year-end | 211 W (Jun 3) | ~+1 W/wk | 4×10 @ 85%; ladder → 4×12 → 3×15, retest late Aug | Restarting on schedule 🟢 |
| **Long ride** | 3–4 h by Aug | 3.5 h (Jun 25) | +15 min / 2 wks | Saturday 3.5 h on 3-days-loaded legs | Holding, harder version 🟢 |
| **MDS multi-day resilience** | Tolerate 5 consecutive stages, 8 kg pack | **0 trial weekends** | 2–3 by Sept | 4 consecutive riding days — partial transfer | Behind 🔴 |
| **Pack-loaded walking** | 8 kg / 120 min by mid-July | **6 kg / ~70 min, once (Jul 7)** | +1 kg or +15 min / 2 wks | **None — deferred at athlete request** | Behind, now deferred 🔴 |

### The walk: deferred, and what that costs

You asked to drop it and this plan drops it — your call, and the cycling week is better for having Friday as a ride. But two 🔴s trigger the flag rule, so once, plainly:

**Pack-loaded walking is the only goal here where being behind actually threatens the event.** One loaded walk (6 kg, Jul 7) against a target of 8 kg / 120 min by mid-July, with roughly **10 weeks** to MDS. Cycling builds the aerobic engine that makes 5.5 km/h feel easy; it builds **nothing** for foot, ankle, hip and lower-back tolerance under a pack, and blisters are the #1 DNF cause in multi-day treks. This week's four riding days do buy real multi-day resilience. They buy zero pack conditioning.

Deferring one week is fine. Deferring three is not. The ramp still fits if it restarts w/c Aug 3:

| Window | Pack | Longest walk |
|--------|------|--------------|
| w/c Aug 3 | 7 kg | 90 min |
| w/c Aug 10 | 8 kg | 120 min |
| w/c Aug 17 | 8 kg | 150 min |
| w/c Aug 24 | 8 kg | **Trial weekend #1** — 2×120 min back-to-back |
| w/c Aug 31 – Sep 14 | 8 kg | Build to 3 h+, **trial weekends #2 and #3** |
| w/c Sep 21 | 8 kg | Taper |

From mid-August that means some Saturday long rides get replaced by long loaded walks — the dossier already permits it. Tell me when you want that block built.

**On CTL 50–60 by September:** even at this week's maximum, nine weeks averaging 300 TSS lands you at **~39** by Sep 30, not 50. Reaching 50 needs sustained ~390 TSS weeks starting immediately, at 52, off a layoff. Recommend re-anchoring the dossier target to **40–45 by mid-September**. Costs nothing that matters — MDS is a walking event.

---

## Nutrition note

`Deficit status: active — all gates clear (ACWR 0.0, TSB +18.0, readiness "go"; no suspension trigger)`

Gates are open, but **do not run a deficit this week.** Two reasons, and the second is the one that matters for what you've asked for:

- At 87.8 kg you're **already inside the 88–90 kg October target**. The 28-day slope of −2.34 kg/week is far past the protocol's 0.3–0.5 kg/week and risks lean mass — which is what carries an 8 kg pack for five days.
- **A 295-TSS week off a layoff is not a weight-loss week.** Section 12's integration rule is explicit: training load overrides the diet plan. Under-fuel this block and Saturday falls apart, Thursday's intervals sag, and the ceiling argument becomes moot.

Actions: **weigh in Wednesday morning** (the 87.8 reading is 13 days old and post-holiday), eat at **maintenance**, and restart deliberate in-session fuelling — you haven't fuelled a ride in over two weeks. Thursday and Saturday both need carbs on the bike; Saturday needs ~60 g/h. Wednesday's warm ride needs the fluid and sodium noted above.

---

## Workout files

**Live for this week:**

- **Thu sweet spot:** [`2026-07-30_Thu_SS5_4x10_SweetSpot_211_reentry.zwo`](../workouts/2026-07-30_Thu_SS5_4x10_SweetSpot_211_reentry.zwo) — includes the earned extension (interval 4 → 12 min) and a marked 3×10 bail-out
- **Fri durability:** [`2026-07-31_Fri_AE2_Z2_75min.zwo`](../workouts/2026-07-31_Fri_AE2_Z2_75min.zwo)
- **Wed rain fallback:** reuse [`Monday-AE1-Steady-Z2-75min.zwo`](Monday-AE1-Steady-Z2-75min.zwo)
- **Sat rain fallback:** reuse [`Saturday-AE3-Indoor-Fallback-175min.zwo`](Saturday-AE3-Indoor-Fallback-175min.zwo) — 175 indoor min ≈ 3.5 outdoor h
- Wed and Sat outdoors need no file — HR-paced.

**Superseded — safe to delete from `C:\Zwift Coach\workouts\`:**

- `2026-07-29_Wed_SS5_4x10_SweetSpot_211_reentry.zwo` (v2.0 — same session, wrong day)
- `2026-07-30_Thu_AE2_Z2_75min.zwo` (v1.0 — replaced by the Friday file)

---

## Decision gates — this is where "safely" lives

The plan sits on the line, so the gates are not garnish. Each one is a real stop.

- **Wednesday: the discipline gate, not a readiness gate.** It's a Z2 ride in warm weather — nothing to assess, everything to restrain. **Hard ceiling 135 bpm.** After 15+ days off, the first ride back always feels better than it should for the first 30 minutes; the failure mode is a "reintroduction" ride that quietly becomes tempo and costs you Thursday. If the legs feel genuinely flat instead, ride 60 min and stop — no penalty.
- **Thursday morning gate (before the only quality session).** Green or single amber → 4×10 as written. Two ambers, or HRV below ~27 → drop to 3×10 (the file marks the bail-out). HRV red / RHR +5 → skip the intervals entirely, ride Friday's steady file instead, and the week lands at ~230 TSS. **The first hard session after a layoff is the highest-risk moment of the block** — the one place where being wrong is expensive.
- **Thursday's earned extension.** Interval 4 may go to 12 min *only if* interval 3 held steady power with HR under 145. That is the sole permitted addition all week.
- **Friday now matters more than it did.** With the swap, Friday is the only easy day between quality and the long ride, and it's the first place accumulated fatigue shows. RHR +5 over baseline, or HRV under ~27 → **skip Friday entirely** and go into Saturday fresh. Losing 51 TSS is cheap; arriving at a 3.5 h ride already cooked is not. If you do ride it, protect VI ≤ 1.05 — surges void the durability measurement.
- **Saturday is the load dial and the discipline test.** 3.5 h target, 3 h floor, **hard stop at 3.5 h**. HR under 131, absolute cap 135. Rain → the 175-min indoor fallback. If Friday's gate came back amber, ride 3 h.
- **Sunday: rest. Firm.** No "I feel great" spin. The four-day block only works because Sunday closes it.
- **Two ambers on any morning = that day drops to Z2 or rest.** At 295 TSS on 15+ days of detraining, the difference between a strong August and a lost fortnight is whether you honour that rule on a day you feel fine.
