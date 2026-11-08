# Recomposition Plan: 12 October 2026 to 2 May 2027

**Status:** Active. Chosen 11 Oct 2026, after the MDS 120. Replaces the August draft (`post-mds-recomposition-plan-2026-11.md`, renamed to this file), which was parked until the event was done.

**Scope:** One recovery week, then 28 weeks in three phases. Cycling (Zwift) stays the core sport. Resistance training is the second pillar and the session the week is built around.

**Decided 11 Oct:** recomposition route, not a pure cut. Phase 1 starts Mon 19 Oct. Ramp test before any sweet spot work. The gym has a leg press, leg curl and leg extension.
**Revised later the same evening:** bike volume back to 8 to 9 h, three gym sessions from week 4, gym programme rebuilt from the athlete's spreadsheet (sections 5 and 6).
**Deferred:** whether the 80 kg floor becomes a lean-mass floor. Decide at the 3 Jan checkpoint (section 9).

---

## 1. Starting point

| Measure | Value | Source |
|---|---|---|
| Weight | 80.7 kg (29 Sep, last weigh-in before travel) | latest.json |
| Body fat | ~23% (stated 25 Sep; scale 23.1% on 22 Sep) | you / bioimpedance |
| Fat / lean mass | ~18.6 kg / ~62.1 kg | derived from the two lines above |
| Weight since May | 99 kg (5 May) to 80.7 kg; roughly half of it was not fat | history.json, latest.json |
| Logged protein, Jun to 2 Aug | 112 to 132 g/day average; 6 of 79 days at 160 g or more | nutrition.json |
| CTL / eFTP (11 Oct) | 30.0 / 188 W | latest.json |
| FTP setting | 211 W in Zwift and Intervals.icu (set 3 Jun) | latest.json |
| Readiness (11 Oct) | Skip: HRV 27 vs 38 baseline, ACWR 2.19 | latest.json |
| Gym | Machine routine: two upper-body days plus a leg day, RPE 6 to 7 | gym/Revised Gym Routine II.xlsx |

The "skip" and the ACWR of 2.19 are the MDS itself (15.5 h and 408 TSS in the last seven days on top of a cycling-sized chronic load). Expected, and the reason for the recovery week.

**Data gaps to close before 19 Oct:**
- `history.json` stops on 30 Jul. Run `run_history_sync.bat`.
- `nutrition.json` stops on 2 Aug. Export the Cronometer daily summary and servings CSVs into `cronometer/` and run the Cronometer sync.
- Log every gym session in Intervals.icu as a WeightTraining activity with duration and RPE. That puts gym load into ATL and readiness, and lets the nutrition sync tag the day as `gym`.

---

## 2. Where this lands

Projected on 2 May 2027: **~77 to 78 kg at ~18 to 19% body fat**, lean mass up 1 to 1.5 kg (to ~63 kg), fat down ~4.5 kg (to ~14 kg). That is a little better than the August draft (78 kg, 19.5%) because you start about 1 kg leaner.

**15% is the 12-month target.** Holding ~63 kg of lean mass, 15% is about 74 kg, reached with a second cut in autumn 2027. Visible definition in shoulders, arms and upper chest arrives around 18 to 20% once there is muscle underneath; the abdomen comes last.

Expect the scale to rise 1 to 1.5 kg in the first two weeks: glycogen refilling after five months of deficit, plus water from creatine. That is not fat.

---

## 3. Phases

| Phase | Dates | Weeks | Energy | Weight aim (7d avg) | What it is for |
|---|---|---|---|---|---|
| **Recovery** | 12 to 18 Oct | 1 | Maintenance | n/a | Absorb the MDS. Start the protein floor and creatine. |
| **1. Rebuild** | 19 Oct to 3 Jan | 11 | Maintenance, ~2,600 kcal week average (day-type targets in 8.1) | Hold 80.5 to 82.5 kg | Fix protein, learn the leg lifts, harvest novice strength gains, ramp test. Christmas sits at maintenance on purpose. |
| **2. Lean cut** | 4 Jan to 4 Apr | 13 | ~400 kcal/day under maintenance, rides fuelled | Lose 0.3 to 0.4 kg/week, ~4.5 kg in total | Fat loss with the new muscle protected by protein and progressive lifting. |
| **3. Consolidate** | 5 Apr to 2 May | 4 | Maintenance | Hold ~77 to 78 kg | Settle, re-measure, retest, decide on the summer. |

Rules that hold across every phase:

| Rule | Detail |
|---|---|
| Protein floor | 180 g every day, rest days included. Below 160 g is a flag. The single highest-leverage change in the plan. |
| Deficit gates (Phase 2 only) | ACWR 1.3 or higher, TSB below -25, readiness "modify" or "skip", HRV down more than 20% sustained, RHR up 5 bpm sustained: eat to maintenance that day. |
| Sunday | Rest, locked. |
| Not programmed | Walks, extra easy spins, a Zwift group ride you fancy. They are context, not deviations. |
| Measuring | Daily weigh-in judged on the 7d average. Waist once a week in the Intervals.icu abdomen field, same morning routine. Lifting log every session. Photos monthly. Bioimpedance only as a 2 to 4 week trend. |

---

## 4. Recovery week (12 to 18 Oct)

Kept loose on purpose.

- Ride only once HRV is back near baseline (high 30s) and your legs feel normal: 30 to 60 min easy, HR under 130. No intervals.
- Gym is optional: one upper-body session from Thursday at RPE 6, using your current routine. No legs yet. The first leg session is Mon 19 Oct.
- Eat at maintenance from today. No deficit. Protein 180 g.
- Start creatine (5 g a day) this week, so its water weight is in before the Phase 1 baseline.
- Weigh daily again from tomorrow to rebuild the 7d average.
- Close the data gaps in section 1.

---

## 5. Training week (from 19 Oct)

Revised 11 Oct 2026: the bike goes back to 8 to 9 h a week (you asked not to trim Zwift) and the gym goes to three sessions from week 4. The gym programme is fixed; only the weights change. The Zwift sessions are written fresh each week.

| Day | Bike | Gym | Notes |
|---|---|---|---|
| **Mon** | Easy spin 45 min, before the gym | **Gym A** (legs + push), ~50 min | Spin first, never after. |
| **Tue** | Z2, 75 to 90 min | | Easy on purpose; legs are sore from Monday in weeks 1 to 3. |
| **Wed** | Quality, 75 min | | Week 1: Z2. Week 2: cadence session (AE-5). Week 3: ramp test (Wed 4 Nov). Week 4 on: sweet spot, section 7. |
| **Thu** | Optional easy 45 min | **Gym B** (pull + lighter legs), ~50 min | |
| **Fri** | Z2, 60 min | **Gym C** (upper body), ~40 min, from week 4 | Ride or gym first, whichever suits. Stays easy so Saturday is good. |
| **Sat** | Long ride, 2.5 to 3 h | | Z2, fuelled at 60 g carbs/h. |
| **Sun** | Rest | Rest | Locked. |

Weekly load: about 8 h on the bike (6 to 7 h in weeks 1 to 3 while the legs learn to lift) and 2.5 h in the gym. CTL is not a KPI in this plan.

**Rules**
- Quality stays at once a week. All the extra hours are Z2 or easier.
- Legs are never trained the day before the quality ride or the long ride. Friday's gym session has no leg work.
- No quality ride in weeks 1 to 2 (first two leg sessions). Ramp test in week 3, sweet spot from week 4.
- If Monday's legs still bite on Wednesday, ride Wednesday as Z2 and do not progress the session ladder off that week.
- When something has to give (HRV sliding, or the Monday lifts stalling two weeks running): first Friday's ride, then long-ride length, then Gym C. Gym A and B do not give.
- Z2 riding does not interfere much with muscle growth. The cost of the extra hours is food (section 8) and the easy Tuesday.

---

## 6. Gym programme

Your spreadsheet (`gym/Revised Gym Routine II.xlsx`, sheet "Routine") supplies the machines and starting weights. Its three-day rotation is replaced by three fixed sessions on fixed days, so every muscle is trained twice a week, and effort rises to the level muscle growth needs. The sessions are also in the workbook (sheet "Gym A B C") with a log sheet.

### 6.1 The sessions

| Gym A, Monday (legs + push) | Sets x reps | Start | Gym B, Thursday (pull + lighter legs) | Sets x reps | Start | Gym C, Friday (upper body, from week 4) | Sets x reps | Start |
|---|---|---|---|---|---|---|---|---|
| Leg Press | 3 x 8 to 10 | 80 kg | Chest Press | 3 x 8 to 10 | 35 kg | Shoulder Press | 3 x 8 to 10 | 27 kg |
| Lying Leg Curl | 3 x 10 to 12 | 30 kg | Assisted Chin | 3 x 6 to 10 | 30 kg assist | Seated Cable Row | 3 x 10 to 12 | 30 kg |
| Incline Chest Press | 3 x 8 to 10 | 25 kg | Low Row | 3 x 10 to 12 | 45 kg | Lateral Raise | 3 x 12 to 15 | light |
| Lat Pulldown | 3 x 10 to 12 | 55 kg | Leg Extension | 3 x 12 to 15 | set in session 1 | Reverse Fly | 2 x 15 | 12.5 kg |
| Triceps Dip | 2 x 10 to 12 | 70 kg | Lying Leg Curl | 2 x 12 to 15 | 25 kg | Biceps Curl | 2 x 12 to 15 | 10 kg |
| Abdominals | 2 x 15 | 40 kg | Seated Calf Raise | 3 x 12 to 15 | 30 kg | Cable Triceps Pushdown | 2 x 12 to 15 | set in session 1 |

Notes from your sheet that still apply: leg press session 1 is calibration (a weight you could do ~14 reps with, stop at 10); Hack Squat or Belt Squat can stand in when the leg press is busy; chin assist comes down 2.5 kg when you hit 3 x 10; curls never to failure; back extension can rotate in for Low Row if your lower back wants it; 3 s lowering on calf raises. Hip mobility (glute bridges, clamshells, side-lying raises, bird-dog, the three stretches) moves to rest days at home, 10 minutes.

Dropped from the sheet: Wide Press (fourth chest press), Machine Row (overlaps Low Row), Hip Thrust (marked not available), DB Step-ups (MDS-specific), Hip Abduction (covered by clamshells).

Rest between sets: 2 min on leg press, presses, pulldown, chin and rows; 60 to 90 s on the rest.

### 6.2 Progression

Weight is the only variable that changes week to week. Sets and effort change on the dates below and nowhere else.

| Weeks | Dates | Sessions | Sets | Working RPE | Rule |
|---|---|---|---|---|---|
| 1 to 3 | 19 Oct to 8 Nov | A and B | 2 | 7 | Learn the leg lifts. Real soreness after sessions 1 and 2, dropping sharply from session 3. No weight increases. |
| 4 to 11 | 9 Nov to 3 Jan | A, B and C | 3 (2 where the table says 2) | 8; last set of the small exercises 9 (curls stay at 8) | Double progression: when you reach the top of the rep range on every set, add the smallest step next session. Legs 5 kg, upper body 2.5 kg. |
| 12 to 24 | 4 Jan to 4 Apr (cut) | A, B and C | 3 | 8 | Hold the weights and add reps; do not chase load in a deficit. Lifts holding is the proof you are losing fat, not muscle. If recovery suffers, drop Gym C before dropping weight. |
| 25 to 28 | 5 Apr to 2 May | A, B and C | 3 | 8 | Add load again at maintenance. Retest leg press and chest press 8RM in week 28. |

Volume at full programme (hard sets per week): chest 8 plus dips, back 12, shoulders 6 direct plus pressing, quads 6, hamstrings 5, biceps 2 direct plus 9 pulling sets, triceps 4 plus 6 pressing sets, calves 3. That is the middle of the productive range.

Log every session in Intervals.icu as a WeightTraining activity with duration and RPE (so it counts toward training load), and the weights and reps in the workbook log or the activity notes.

---

## 7. Cycling

**FTP is unsettled.** The Zwift and Intervals.icu setting is 211 W; the late-August working number was ~190 W; eFTP on 11 Oct is 188 W. A ramp test settles it instead of more argument.

| Weeks | Dates | Bike |
|---|---|---|
| 1 to 2 | 19 Oct to 1 Nov | Z2 only, 125 to 140 W or HR under ~130 (Z2 on either FTP number). Week 2 Wednesday is a cadence session (AE-5, high-cadence blocks within Z2). Long ride 2 h in week 1, 2.5 h from week 2. Mon and Thu spins are Z1. |
| 3 | Wed 4 Nov | **Zwift ramp test.** 48 h after Gym A; keep that Monday at RPE 7. If your legs are not fresh, move it to Fri 6 Nov. Afterwards Zwift updates its FTP; set the same number in Intervals.icu so latest.json carries it. From then on every .zwo is built against the tested number and the 190/211 split ends. |
| 4 to 11 | 9 Nov to 3 Jan | Wednesday tempo or sweet spot only: 2 x 20 or 3 x 15 at 88 to 92% of the tested FTP. No threshold, no races yet. |
| 12 to 24 | 4 Jan to 4 Apr | One true quality session a week, the rest easy. Options: sweet spot 3 x 15, threshold 4 x 8 at ~97% with 2 min recoveries, or a Zwift race (category D/C). Racing suits a cut: short, motivating, and it keeps FTP honest. |
| 28 | Wed 28 Apr | Ramp test to anchor FTP for the summer. |

Do not change the Zwift FTP setting by hand before the 4 Nov test.

**Long ride:** 2.5 to 3 h in Z2, fuelled from hour one (60 g carbs/h, 500 to 750 ml/h), indoors by default over the winter. On the trainer a fixed Z2 wattage keeps it out of Z1. Fuelled properly it does not eat into Sunday's recovery or Monday's legs.

FTP 230 W is realistic after the deficit, not during it. At 78 kg, 211 W is already 2.7 W/kg.

---

## 8. Nutrition

### 8.1 Daily targets by day type

| Day type (Cronometer label) | Phase 1 kcal | Phase 2 kcal | Phase 3 kcal | Protein | Carbs (Ph1 / Ph2 / Ph3) | Fat (Ph1 / Ph2 / Ph3) |
|---|---|---|---|---|---|---|
| Gym Day (Mon/Thu, with or without an easy ride) | 2,765 | 2,310 | 2,620 | 180 g | 320 / 240 / 295 g | 85 / 70 / 80 g |
| Z4 Quality (Wed) | 2,660 | 2,265 | 2,555 | 180 g | 305 / 240 / 290 g | 80 / 65 / 75 g |
| Long Z2 (Sat) | 2,820 | 2,405 | 2,715 | 180 g | 345 / 275 / 330 g | 80 / 65 / 75 g |
| Z2 Easy | 2,505 | 2,110 | 2,420 | 180 g | 255 / 190 / 245 g | 85 / 70 / 80 g |
| Rest Day | 2,370 | 2,015 | 2,265 | 180 g | 210 / 155 / 195 g | 90 / 75 / 85 g |

The recovery week uses the Phase 1 column. Revised down ~200 kcal per row on 2026-10-11 (athlete agreed): the June logs point to a current maintenance of ~2,400 to 2,600, below the formula estimate. Each kcal figure equals 4 x protein + 4 x carbs + 9 x fat, so Cronometer shows no mismatch. Carbs are total carbs (Cronometer set to Total Carbs, not net). Carbs flex with the training day; protein stays fixed and fat moves only slightly. **Calibration:** after the first two weeks (expect +1 to 1.5kg from glycogen refill and creatine), the 7d average should hold flat. Rising more than ~0.2 kg/week: drop every row by 150. Falling more than ~0.2 kg/week: add 150. The Phase 2 and 3 columns are recalculated from the measured maintenance before 4 Jan 2027. Phase 2 rides stay fuelled on the bike (60 g/h on anything over 90 minutes): the deficit comes from the daily total, not from starving sessions.

Maintenance is still an estimate. At 8 to 9 h on the bike the week average will sit nearer 2,750 than the ~2,600 this table gives, because Friday becomes a Z2 Easy day and Saturday is longer; the calibration rule above settles it. Three weeks of complete Cronometer logging (19 Oct to 8 Nov) will confirm it.

`nutrition.json` day types: gym = `gym`, quality = `z4_quality`, long = `long_z2`, easy = `z2_easy`, rest = `rest`.

### 8.2 Closing the protein gap on a pescatarian diet

Four to five feedings of 35 to 45 g. A template that reaches 180 g without meat:

| Feeding | Example | Protein |
|---|---|---|
| Breakfast | 300 g skyr or 0% Greek yoghurt with berries and oats, 2 eggs | ~45 g |
| Mid-morning or post-gym | Whey (or pea/soy) shake, 35 g powder, in milk | ~35 g |
| Lunch | 200 g cooked lentils or chickpeas plus 150 g tofu, or a tin of tuna or sardines on rye | ~35 to 40 g |
| Dinner | 180 g white fish, salmon or prawns, or 200 g tempeh, with grains and veg | ~40 to 45 g |
| Evening | 200 g cottage cheese or quark, or a casein shake | ~25 g |

The shake and the evening quark do most of the work; the rest is roughly what you already eat with the portions turned up.

**Dinners:** recipes are Claude's own (pescatarian, vegetarian nights welcome). High-carb (pasta, grains, legumes) on gym, quality and long-ride days; protein-forward and lower-starch on rest and easy days. Aim for ~40 g protein at dinner.

### 8.3 Supplements

Creatine monohydrate 5 g daily, from the recovery week (well evidenced for strength and lean mass; expect ~1 kg of water in the first two weeks). Vitamin D through the Dutch winter. Whey or a plant protein powder purely as a convenience for the protein floor. Nothing else is needed.

### 8.4 Logging

Log complete days in Cronometer for the first three weeks of Phase 1 so maintenance can be measured, then relax to daily weight plus protein. Export the Cronometer CSVs into `cronometer/` weekly so `nutrition.json` stays current.

**Cronometer settings:** Track Carbs as Total Carbs (not net). Custom Energy Target on, set equal to the macro total. Add Expenditure Above Baseline off (the day-type targets already include training). Third circle on Target. Default target = the Z2 Easy row; the five labels above carry the rest.

---

## 9. Checkpoints

| Date | Check | On track looks like | If not |
|---|---|---|---|
| **Sun 15 Nov** (end of week 4) | 7d weight, waist, protein compliance, lifting log | Weight 80.5 to 82.5 kg; protein at 180 g on 80%+ of days; leg press up 15 to 25% from week 1 | Protein compliance under 60%: the plan pauses here. Nothing else works without it. |
| **Wed 4 Nov** | Ramp test | New FTP set in Zwift and Intervals.icu | Legs not fresh: move to Fri 6 Nov. |
| **Sun 13 Dec** (end of week 8) | Same, plus body fat trend | Body fat trend down ~1 point; all lifts up | Lifts stalling: check sleep, protein and whether Wednesday is costing Thursday. |
| **Sun 3 Jan** (end of Phase 1) | Full re-measure: weight, body fat, lean mass, waist, photos | Body fat down 1 to 1.5 points; all lifts up | Body fat flat but lifts up: extend Phase 1 by three weeks. **Floor decision here** (section 10). |
| **Sun 31 Jan** | Weight rate, lifting log, readiness signals | -0.3 to -0.4 kg/week; lifts held; no gate triggers | Losing faster than 0.6 kg/week: add 200 kcal. Lifts dropping: add 150 kcal and recheck protein. Floor decision deadline. |
| **Sun 28 Feb** | Same | Waist down 2 to 3 cm from January | |
| **Sun 4 Apr** (end of cut) | Weight, body fat, waist, photos | ~77 to 78 kg, ~18 to 19%; lifts at or above January | |
| **Sun 2 May** | FTP (tested 28 Apr), 8RM tests, full re-measure | | Decide: hold, or build through summer and cut again in autumn for 15%. |

---

## 10. Open decision: the 80 kg floor

The DOSSIER floor (80 kg, set 10 Aug) stays in force for now. It does not bite in Phase 1, where energy is maintenance. From Phase 2 it conflicts with the goal, because every route to 15% ends at 73 to 76 kg.

The alternative is a **lean-mass floor**: the scale may go below 80 kg, but the cut pauses if bioimpedance lean mass (2 to 4 week average) falls more than ~1 kg below its value at the end of Phase 1, cross-checked against the lifting log.

Decide at the 3 Jan checkpoint, and at the latest before the 7d average reaches 80 kg in Phase 2 (expected around early February).

---

## 11. Weekly goals audit

Replaces the MDS audit. One row per goal in every weekly plan.

| Goal | Target | Weekly check |
|---|---|---|
| Protein | 180 g/day | Days at or above 180 g (aim: 6 of 7) |
| Lifting | 2 sessions (3 from 9 Nov) | Sessions done; leg press, chest press and lat pulldown vs last week |
| Weight | Phase band or rate | 7d average vs 80.5 to 82.5 kg (Phase 1) or -0.3 to -0.4 kg/week (Phase 2) |
| Waist | Down from Phase 2 | Weekly reading |
| FTP | Tested 4 Nov, then held | Quality session completed at target |

---

## 12. What is not programmed

Walks: you already do them daily; they are part of the maintenance estimate, not a session. Extra Zwift rides you fancy: fine, they are context, and on a cut they buy you food. A third gym day is now in the plan (Gym C, Friday). Anything MDS-related: retired.
