# Training Plan, September 7 to 13, 2026 (Move the long ride indoors)

```json
{
  "data_source_fetched": true,
  "json_fetch_status": "success",
  "plan_version": "1.0",
  "phase": "Base",
  "phase_week": 2,
  "theme": "The 185W anchor test passed on power and was inconclusive on heart rate, because the file shipped with 4-minute recoveries instead of the template's 2. That gets corrected, not escalated. The headline change is Saturday: the long ride moves indoors so the HR floor is enforced by a power target rather than by willpower. It has failed four attempts outdoors.",
  "readiness_at_generation": "latest.json synced 2026-09-06 16:49. P2 modify: HRV 20.0 red (-28.3% vs 27.9 baseline, persistence 1 day), sleep 6h49 quality 3 amber. RHR 51 green, ACWR 0.91 green, TSB +5.1 green, RI 0.74. Sep 6 long ride NOT ridden (athlete call, endorsed). Start state Sep 7: CTL 30.0 / ATL 24.9 / TSB +5.1.",
  "load_target_TSS_cycling": "~304",
  "volume_hours_cycling": "~7.25",
  "quality_sessions": 2,
  "long_rides": 1,
  "session_templates": ["AE-1", "TH-2", "AE-4", "SS-1", "AE-3"],
  "progression_vector": "long_ride_execution (modality change: outdoor to indoor to enforce the HR floor)",
  "polarization_ratio": 0.84,
  "load_variance": false,
  "FTP_zwift_setting": 211,
  "FTP_working": 190,
  "eFTP": 192.5,
  "LTHR": 154,
  "max_HR": 170,
  "validation_protocol": "URF_v5.1",
  "confidence": "high"
}
```

**Generated:** 2026-09-06 · Zwift FTP setting **211 W** (unchanged, leave it) · **Working FTP 190 W** · eFTP 192.5 · LTHR 154 · Max HR 170 · Weight 81.7 kg (7d avg 82.1) · data synced **2026-09-06 16:49**

---

## Today's call was right

Two days off the bike, HRV at 20 against a 27.9 baseline, 6h49 of poor sleep, and a 3-hour outdoor ride on the card. Not riding was the correct read of the signals. No debt is owed and nothing is being "made up" this week.

One thing worth knowing before Monday: the HRV series is **sawtooth, not a slide**.

| Sep 1 | Sep 2 | Sep 3 | Sep 4 | Sep 5 | Sep 6 |
|---|---|---|---|---|---|
| 32 | 27 | 24 | **36** | 29 | **20** |

Thirty-six two days ago rules out an accumulating fatigue trend. RHR is 51, the lowest reading of the week, and green. TSB is +5.1, ACWR 0.91. You are not fatigued. You had a bad night. Those are different problems with different answers, and the answer to the second one is to sleep and then train.

---

## What Thursday's 4x8 actually told us

This was the session built to test the 190 W anchor. Here is what came back.

| Rep | Power | Avg HR | Decoupling |
|---|---|---|---|
| 1 | 184 W | 130 | 7.0% |
| 2 | 183 W | 133 | 7.5% |
| 3 | 183 W | 135 | 5.3% |
| 4 | **181 W** | 136 | 5.4% |

Spread across four reps: **1.6%**. Session decoupling **5.4%**, down from 13.9% at 195 W the week before. EF 1.26, up from 1.17. On the power criterion the 30 Aug decision table is unambiguous: *"Four reps within 3% → 190 W is the right anchor."*

**But the heart rate did not show up.** TH-2 is specified to reach 90 to 92% of HRmax by the final reps. That is **153 to 156 bpm** for you. Rep 4 averaged 136 and peaked at 143. You finished a threshold session 13 beats below where a threshold session is supposed to finish.

Before concluding that 185 W is too soft, look at the file I sent you:

```
<SteadyState Duration="480" Power="0.8768">   <- 8 min at 185 W
<SteadyState Duration="240" Power="0.4976">   <- 4 min at 105 W
```

**The recoveries were 240 seconds. The TH-2 template calls for 120.** The whole mechanism of a Seiler 4x8 is incomplete recovery: you start rep 2 still carrying rep 1, and cardiac output ratchets up across the set. Four minutes at 105 W hands most of that back. That was my error in building the file, not a fitness readout.

So the verdict is: **190 W holds, and the test repeats on Tuesday with the recoveries the template specifies.** Same watts, half the rest. If HR climbs into the 148 to 156 band on reps 3 and 4 with power still flat, the anchor is confirmed and correctly placed. If HR still tops out around 140 at flat power, then 185 W genuinely is submaximal and we raise it. One variable changes. That is the point.

---

## Goals audit

*Deficit status: **active**. The HRV drop is 1 day (persistence 1), not the sustained breach that suspends the deficit under SECTION_12 section 7. The rate, however, is a separate problem: see the weight row.*

| Goal | Target | Now | Rate | Status |
|---|---|---|---|---|
| **Weight** to 80 kg | -0.3 to -0.5 kg/wk | 81.7 kg latest, **82.1 kg 7d avg**, 2.1 kg to go | **-0.80 kg/wk** (28d slope) | 🔴 **too fast**, past the -0.6 flag |
| **CTL** to 36-38 by mid-Sept | 36 by ~15 Sept | 30.0 | projects to **32.0** by 13 Sept | 🔴 **the target will be missed** |
| **FTP** to 230 W | 230 by end 2026 | 190 working, defended cleanly at 185 W x 4 | anchor confirmed on power | 🟡 held, not yet moving |
| **Long ride** 3h+ sustained Z2 | duration plus **HR floor 118** | 16 Aug: 3h02 at 94.8% Z1. 30 Aug and 6 Sep: not ridden | **0 for 4 attempts** | 🔴 the single most behind item |
| **Back-to-back days** | consecutive training days | Mon+Tue and Wed+Thu pairs this week | 3 straight last week | 🟢 |

### The two red rows that need saying plainly

**CTL 36 to 38 by mid-September is not going to happen.** You are at 30.0 with nine days left. Closing that gap needs roughly 400 TSS a week, sustained, which is a 30% ramp on a week you just under-delivered by half. I am not going to build that plan and you should not want it. The realistic landing is **CTL 32 to 33 by 15 September**.

Here is why I am not treating that as a crisis. DOSSIER section 8 says it in your own words: *"Cycling CTL beyond ~40 buys steadily less transfer to it. Long-ride duration and consecutive-day resilience remain the primary progression vectors for this event; CTL is a supporting metric, not the objective."* You are five weeks from a five-day walking event. A CTL number you buy by cramming in September is worth less to October than one 3-hour ride actually ridden at the right intensity. Which brings us to the row below it.

**The weight rate is the row I would fix first.** -0.80 kg/wk is well past your own -0.6 flag, and it is not a coincidence that it sits next to a red HRV reading, a 6h49 night, and two skipped long rides in three weeks. SECTION_12 section 7 says to investigate under-fuelling as a contributing factor when HRV drops. I would rather you arrive in October at 81 kg and fuelled than at 80.0 kg and hollow. Ease the deficit back into the -0.3 to -0.5 band, protect protein, and fuel Saturday properly (60 g carbs/hour from hour one, not from when you feel hungry).

Worth noting for planning: the deficit ends at 80 kg on the 7d average **or three weeks before the event, whichever comes first**. If MDS is mid-October that gate closes around 25 September. At a corrected -0.4 kg/wk you will be near 81 kg by then, so the floor probably will not be reached before the gate closes. That is the right outcome, not a failure. Tell me the exact MDS dates and I will put the gate on the calendar precisely.

---

## The week

| Day | Session | Target | Modality | Duration | Est. TSS |
|---|---|---|---|---|---|
| **Mon 7 Sep** | **AE-1 steady Z2**, reopening ride | 135 W · HR 117-127 · RPE 3-4 | 🏠 Zwift | 75 min | 45 |
| **Tue 8 Sep** | **TH-2 Seiler 4x8 at 185 W, 2 min recoveries** ⚡ the retest | 185 W · **HR should reach 148-156 by rep 4** · RPE 7-8 | 🏠 Zwift | 68 min | 70 |
| **Wed 9 Sep** | **AE-4 active recovery** | 120 W · HR under 115 · RPE 2-3 | 🏠 Zwift | 50 min | 26 |
| **Thu 10 Sep** | **SS-1 sweet spot 2x18 at 172 W** ⚡ | 172 W · HR 138-147 · RPE 6-7 | 🏠 Zwift | 66 min | 58 |
| **Fri 11 Sep** | **REST**, standing | | Rest | | 0 |
| **Sat 12 Sep** | **AE-3 long durability, INDOORS** 🔑 the priority | 133 to 148 W stepped · **HR floor 118** · RPE 4-5 | 🏠 Zwift | 175 min | 105 |
| **Sun 13 Sep** | **REST**, structural rest resumes | | Rest | | 0 |
| **Total** | 5 rides | | | **~7h15** | **~304** |

Thursday is deliberately 2x18 rather than last week's 3x15. It is 16 TSS lighter and it is lighter on purpose: everything this week is arranged so that Saturday happens.

### Projected load

| Date | TSS | CTL | ATL | TSB |
|---|---|---|---|---|
| Mon 7 | 45 | 30.4 | 27.8 | +2.6 |
| Tue 8 | 70 | 31.3 | 33.8 | -2.5 |
| Wed 9 | 26 | 31.2 | 32.7 | -1.5 |
| Thu 10 | 58 | 31.8 | 36.3 | -4.5 |
| Fri 11 | 0 | 31.1 | 31.1 | -0.1 |
| **Sat 12** | 105 | **32.8** | 41.7 | **-8.8** |
| Sun 13 | 0 | 32.0 | 35.7 | -3.7 |

Peak ACWR **1.28**, inside the 1.3 gate. Peak TSB -8.8, milder than last week's plan. Nothing here needs a warning.

---

## 🔑 Saturday: the change that matters

Four attempts at the long ride. One ridden, at 94.8% Z1 against a 118 floor. Two not ridden at all. That is not a fitness problem, because your CTL is 30 and your TSB is positive: a 3-hour Z2 ride is well inside what you can do. It is an execution problem, and it has the same shape every time.

Outdoors on the Condor you have no power meter. HR is the only instrument, it is a lagging one, and the road keeps handing you reasons to soft-pedal. Add weather and a Saturday morning mood and the failure modes stack up: ride it too easy, or do not ride it.

**So this week it goes on Zwift.** At a fixed 133 W the trainer will not let you ride Z1. The floor stops being something you have to remember and becomes something the equipment enforces. 175 indoor minutes is the honest equivalent of about 3.5 outdoor hours, because indoors there is no coasting and more thermal load.

The structure, progressive so the last hour is the hard-earned one:

| Block | Duration | Power | Expected HR |
|---|---|---|---|
| Warm-up | 15 min | ramp 105 to 131 W | building |
| Block 1 | 55 min | 133 W | 117-125 |
| Block 2 | 55 min | 137 W | 120-128 |
| Block 3 | 25 min | 143 W | 124-132 |
| Finisher | 15 min | 148 W | 128-136 |
| Cool-down | 10 min | ramp down | |

**Fuel it like the event it is training for.** 60 g carbs per hour starting in hour one, 500 to 750 ml fluid per hour, fan on maximum from minute zero. Given the weight row above, this is the ride where under-fuelling would cost you the most.

If Saturday morning readiness comes back `modify` or worse: **drop the finisher and the block 3 step-up, ride 150 minutes at 133 to 137 W.** Duration is the goal, the step-ups are the garnish. Said once.

Outdoors remains available if Saturday is beautiful and you want it. But then it is a bonus ride on top of a floor you have already proved you can hold, not the fifth attempt at proving it.

---

## Reference zones, working FTP 190 W

| Zone | Power (working 190) | as % of Zwift 211 | HR (LTHR 154) | Used this week |
|---|---|---|---|---|
| Z1 recovery | under 105 W | under 50% | under 111 | Wed, recoveries |
| Z2 endurance | 105-150 W | 50-71% | 111-131 | Mon, Sat |
| Z3 tempo | 151-171 W | 72-81% | 132-142 | Sat finisher edge |
| Sweet spot | 167-179 W | 79-85% | 138-147 | **Thu 2x18 at 172 W** |
| Z4 threshold | 180-200 W | 85-95% | 143-154 | **Tue 4x8 at 185 W** |
| Z5 VO2max | 201-228 W | 95-108% | 155+ | |

⚠️ **Do not change your Zwift FTP setting.** Leave it at 211. Every `.zwo` expresses targets as a percentage of 211 and already resolves to the right absolute watts.

---

## Protocol compliance

| Gate | Requirement | This plan | |
|---|---|---|---|
| Session composition | 2 structured, 1 long Z2 | TH-2, SS-1, AE-3 | ✅ |
| Hard-day spacing | 48h between hard sessions | Tue and Thu | ✅ |
| Intensity distribution | Z3+ under 20% | 70 of 434 min = **16.1%** | ✅ |
| Z1-Z2 share | at least 75% | **83.9%** | ✅ |
| ACWR | 0.8 to 1.3 | peak **1.28** | ✅ |
| Progression vectors | one per week | long_ride_execution only | ✅ |
| Back-to-back hard days | prohibited unless TSB above 0 | none scheduled | ✅ |

The Tuesday recovery change is a **correction back to the TH-2 template specification**, not a progression vector. The prescribed intensity, interval count, and duration are all unchanged from last week.
