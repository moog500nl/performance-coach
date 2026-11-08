# Training Plan — August 10–16, 2026 (Base week 3: front-load the work, hand the heat to the calendar)

```json
{
  "plan_version": "1.0",
  "phase": "Base",
  "phase_week": 3,
  "theme": "Three-day quality block Mon-Wed while it is cool, two firm rest days across the 32C Thu-Fri, then the long ride moves Sat -> Sun to escape the heat. The week's centrepiece is Tuesday's 4x12 at 170W - a diagnostic, not a workout: it answers whether FTP 211 is still real. Sunday's long ride is the priority session and everything from Thursday onward is built to arrive at it fresh.",
  "readiness_at_generation": "P1 SKIP on Aug 8 (ACWR 2.33) - resolved by the scheduled Sunday Aug 9 rest day. HRV 31.0 green (+5.1% vs 7d baseline 29.5), RHR 51 green (-3), sleep 6h51 amber, RI 1.11 green. ACWR is the known layoff artifact and clears to ~1.19 by Sunday under this plan.",
  "load_target_TSS_cycling": "~327",
  "volume_hours_cycling": "~8.0",
  "quality_sessions": 1,
  "long_rides": 1,
  "session_templates": ["AE-1", "SS-5", "AE-2", "AE-4", "AE-3"],
  "progression_vector": "interval_power_validation (4x12 @ 179W failed -> 4x12 @ 170W diagnostic)",
  "load_variance": false,
  "FTP": 211,
  "LTHR": 154,
  "intensity_basis": "Indoor = power (FTP 211 W, per latest.json synced 2026-08-08 16:38). Outdoor = HR only (no power meter on the Condor)."
}
```

**Generated:** 2026-08-08 · FTP **211 W** (set Jun 3) · LTHR 154 · Max HR 170 · Weight **85.3 kg** (Aug 8) · CTL 32.16 / ATL 48.69 / TSB **−16.53** · ACWR 2.33 · data synced **2026-08-08 16:38**

---

## The two structural changes you asked for

**1. The long ride moves to Sunday.** Thursday, Friday and Saturday are 32 °C. Saturday is your normal long-ride slot and a 3-hour outdoor Z2 ride in that heat is not the session you planned — it is a heat-tolerance test with a Z2 label on it. Sunday is the right call.

**2. That breaks the Sunday-rest rule, so the rest moves too.** Sunday has been a locked rest day since 2026-05-17 and it is written into the DOSSIER. This week trades it for **two firm rest days on Thursday and Friday** — which the heat was going to cost you anyway. Net rest days: still two. I have treated this as a **one-week exception**; if you want Sunday-long / Monday-rest to become the standing pattern, say so and I will amend the DOSSIER properly rather than letting it drift.

**Knock-on:** Monday Aug 17 must be a rest day. A long Sunday with no rest either side is how you arrive at next week already tired — and the week of Aug 24 is when the FTP test wants a clean run-up.

---

## The week

| Day | Session | Target | Modality | Duration | Est. TSS |
|-----|---------|--------|----------|----------|----------|
| **Mon Aug 10** | **AE-1 Z2 steady** — week opener, aerobic volume only | 137→139 W · HR 117–127 | 🏠 Zwift | 75 min | ~48 |
| **Tue Aug 11** | **SS-5 4×12 @ 170 W — DIAGNOSTIC** 🔬 the week's one hard session | 170 W · HR 138–148 | 🏠 Zwift | 90 min | ~78 |
| **Wed Aug 12** | **AE-2 Z2 durability** — qualifying session, VI ≤ 1.05 | 139 W flat · HR 117–127 | 🏠 Zwift | 75 min | ~51 |
| **Thu Aug 13** | **REST — firm** 🔥 32 °C | — | Rest | — | 0 |
| **Fri Aug 14** | **REST — firm** 🔥 32 °C | — | Rest | — | 0 |
| **Sat Aug 15** | **AE-4 easy Z2, heat-managed — OPTIONAL** 🔥 32 °C · droppable | HR ceiling 127, cap 131 | 🚲 early outdoor *or* 🏠 Zwift | 60 min | ~35 |
| **Sun Aug 16** | **LONG RIDE — Z2, 3 h 15** (floor 2.5 h, hard stop 3.5 h) — priority session | HR < 131, hard cap 135 | 🚲 Outdoor | **3 h 15** | ~115 |
| **Total** | 5 rides (1 optional) | | **~8.0 h** | **~327 TSS** |

---

## 🔬 Tuesday is a diagnostic, and it has a pass condition

On Aug 5 the 4×12 at 179 W was logged as **2×12** — 176 W then 163 W, with HR only 132–133 against an expected 138–148. Two explanations fit: heat plus accumulated fatigue, or 179 W simply is not sweet spot for you right now.

Tuesday re-runs the identical session **9 W lower, at 170 W** — 85% of 200, not of 211. Read the result like this:

| Outcome | What it means | What happens next |
|---|---|---|
| **All four reps within 3%, HR settles 138–148, RPE 6–7** | FTP 211 stands; Aug 5 was heat + fatigue | Ladder resumes: 3×15 the following week, test w/c Aug 24 confirms |
| **Power sags again, or HR never reaches 138** | Threshold has drifted below 211 — eFTP 195 was telling the truth | Drop working FTP to ~200 for targets now; the w/c Aug 24 test sets the real number |

**Do not rescue a sagging rep.** A clean failure is a usable answer; a forced pass tells us nothing and costs you Wednesday. Log RPE and feel either way — both feed the read.

---

## 🔥 The heat plan (Thu–Sat, 32 °C)

32 °C is **Tier 2 — active session modification**, and your indoor setup (one fan, no AC) is not a refuge: an uncooled 28 °C room loads you harder than 30 °C outdoors at speed. Only two qualifying outdoor rides in the last 14 days, so your thermal baseline is still thin and absolute tiers apply.

How the week absorbs it:

- **Thursday and Friday take the worst of it as rest days.** Zero training cost — the heat is spending days you were going to spend anyway.
- **Saturday is deliberately small and genuinely optional.** Its only job is to open the legs and give a back-to-back stimulus before Sunday. **HR is the ceiling (127, hard cap 131); power floats down.** Ride before 09:00 outdoors or indoors with the fan on max. Drop it entirely if the room is brutal, if you are behind on fluids, or if you would rather arrive at Sunday completely fresh — nothing in that hour is worth compromising the long ride.
- **Fluids Thu–Sat decide Sunday.** ~750 ml/h with sodium on any ride, starting in the first 15 minutes; keep drinking on the two rest days. Two hot rest days still dehydrate you.
- **If Sunday also turns hot,** start at first light and treat 135 bpm as an absolute stop-sign rather than a guide. The floor is 2.5 h — taking the floor in heat is a pass, not a miss.

---

## Reference zones (FTP 211 W · LTHR 154 · Max HR 170)

**Indoor (Zwift — power):**

| Target | Power | Expected HR |
|--------|-------|-------------|
| Recovery between intervals | ~110 W (52%) | < 120 bpm |
| Easy Z2 (Sat, heat) | ~122 W (58%) | **HR ceiling 127, cap 131** |
| Steady Z2 | 137–139 W (65–66%) | 117–127 · heat ceiling 131 |
| **Sweet spot — diagnostic** | **170 W (80.5%)** | **138–148, hard cap 150** |

**Outdoor (HR-guided — no power meter):**

| Zone | HR guide | Feel |
|------|----------|------|
| Z2 Endurance | 120–131 bpm | Steady, full sentences throughout |
| **Hard ceiling (Sat + Sun)** | **135 bpm** | Above this you are no longer following the plan |

---

## Load model

| Day | TSS | CTL | ATL | TSB (am) | ACWR |
|-----|-----|-----|-----|------|------|
| Sun Aug 9 | 0 | 31.4 | 41.7 | −16.5 | 1.54 |
| Mon | 48 | 31.8 | 42.6 | −10.3 | 1.93 |
| Tue | 78 | 32.9 | 47.7 | −10.8 | 1.90 |
| Wed | 51 | 33.3 | 48.2 | −14.8 | 1.71 |
| Thu | 0 | 32.5 | 41.3 | −14.8 | 1.50 |
| Fri | 0 | 31.8 | 35.4 | −8.7 | 1.33 |
| Sat | 35 | 31.8 | 35.3 | **−3.6** | 0.86 |
| **Sun** | **115** | **33.8** | 46.7 | **−3.5** ← fresh for it | 1.19 |
| Mon Aug 17 | 0 (rest) | 33.0 | 40.0 | −12.9 | **1.02** |

CTL 32.2 → **33.8** (+1.6). The shape matters more than the total: Thursday and Friday's rest drops TSB from −15 to **−3.6**, so you hit Sunday's long ride the freshest you have been for a long ride since June.

**ACWR resolves itself this week.** It reads 1.9 mid-week purely because the near-empty holiday weeks are still shrinking the 28-day denominator — then falls to 1.19 by Sunday and **1.02 by Monday** as those weeks roll out of the window. That is the artifact expiring on schedule, and it is what clears the way for the test in the week of Aug 24. HRV, RHR and sleep keep full authority throughout; the artifact excuse applies to ACWR only.

---

## What the data said (and how the week answers it)

| Signal | Reading | Response in this plan |
|--------|---------|----------------------|
| Aug 5 SS-5 | 4×12 planned, 2×12 executed; rep 2 sagged 176→163 W at HR 132 | Tuesday re-runs it 9 W lower as a pass/fail diagnostic |
| eFTP vs set FTP | 195.4 vs 211 (set Jun 3, 66 days old) | Diagnostic first; formal test w/c Aug 24 when ACWR is back in band |
| Power curve 28d | 1200s −1.2%, 3600s −0.6%, 5s +25% | Endurance power flat — Z2 volume + one honest quality session, no more |
| Durability | 7d N=2, 28d N=3 — below alert minimums (needs 3 / 5) | Wednesday rides as a qualifying session; Monday may also qualify |
| Aug 8 long ride | 2h56 at avg HR 125, 95% at/below Z2, 21 s above Z3 | Execution is not the problem — duration is. Sunday goes to 3h15 |
| ACWR | 2.33 alarm | Projected to 1.02 by Aug 17 with no intervention — artifact, not exposure |
| Weight | 85.3 kg, 28d slope −0.56 kg/wk, body fat 25.7% | Below the 88–90 kg target — eat maintenance, fuel Tuesday and Sunday properly |
| Heat | 32 °C Thu/Fri/Sat, thermal baseline thin | Two rest days placed on the worst of it; long ride relocated to Sunday |

---

## Goals audit (vs DOSSIER §1 / §8)

| Goal | Target | Now | This week's contribution | Status |
|------|--------|-----|--------------------------|--------|
| **Weight** | 88–90 kg by Oct | 85.3 kg | Maintenance eating; no deficit | **Met — hold, don't cut** 🟢 |
| **FTP** | 230 W by year-end | 211 W (set Jun 3) | Tuesday resolves whether 211 is real; test w/c Aug 24 | Diagnostic in progress 🟡 |
| **CTL** | 50–60 by Sep (re-anchor to 40–45 recommended) | 32.2 | +1.6 to ~33.8 | Climbing; the re-anchor decision is still open 🟡 |
| **Long ride** | 3–4 h by Aug | 2 h 56 (Aug 8) | Sunday at **3 h 15** | Rebuilding, on track 🟢 |
| **Multi-day resilience** | Tolerate consecutive loaded days | Mon–Wed block + Sat/Sun back-to-back | Two blocks this week | 🟢 |

Pack-loaded walking was removed from the plan on 2026-08-08 and is no longer audited.

---

## Nutrition note

`Deficit status: paused — readiness_decision "skip" on Aug 8 (P1 ACWR 2.33), and weight is already below the October target`

Eat at maintenance. Two specifics that matter this week: **Monday evening decides Tuesday's interval quality** (carbohydrate, and hydrate past thirst), and **Saturday evening decides Sunday's long ride**. On the two 32 °C rest days, keep drinking — hot rest days still dehydrate.

---

## Files

| Day | Zwift file |
|-----|-----------|
| Mon Aug 10 | `2026-08-10_Mon_AE1_Z2_75min.zwo` |
| Tue Aug 11 | `2026-08-11_Tue_SS5_4x12_SweetSpot_170W_diagnostic.zwo` |
| Wed Aug 12 | `2026-08-12_Wed_AE2_Z2_75min_durability.zwo` |
| Sat Aug 15 | `2026-08-15_Sat_AE4_Easy_Z2_60min_heat.zwo` |

All four assume **FTP 211 W is set in Zwift**. If you change Zwift's FTP the percentages re-scale and Tuesday's 170 W diagnostic stops being 170 W — leave it at 211 until after the test.
