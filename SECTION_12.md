# **Section 12 — Daily Nutrition & Weight Coaching Protocol (v12.0)**

**Protocol Version:** 12.4 **Last Updated:** 2026-10-11 **Companion to:** SECTION\_11.md (AI Coach Protocol v11.33+) **License:** MIT

---

## **1\. Purpose & Scope**

Section 12 governs daily nutrition coaching: weight trajectory monitoring, macro compliance, carb periodization alignment, and fueling recommendations relative to training load.

Section 11 v11.26 covers **in-ride** fueling (KJ→carbs dosing, absorption limits, W′ depletion). Section 12 covers **off-bike daily nutrition** — strategic diet management in tandem with the training programme.

---

## **1a\. Current Programme Context (from 2026-10-12)**

The athlete is on a body recomposition programme (`recomposition-plan-2026-10-19.md`), not a weight-loss cut. Energy depends on the phase:

| Phase | Dates | Energy | Weight target (7d avg) |
| ----- | ----- | ----- | ----- |
| Recovery | 2026-10-12 to 2026-10-18 | Maintenance | n/a |
| 1\. Rebuild | 2026-10-19 to 2027-01-03 | Maintenance | Hold 80.5 to 82.5 kg |
| 2\. Lean cut | 2027-01-04 to 2027-04-04 | ~400 kcal/day under maintenance | Lose 0.3 to 0.4 kg/week |
| 3\. Consolidate | 2027-04-05 to 2027-05-02 | Maintenance | Hold |

* Day-type kcal, carb and fat targets for each phase: DOSSIER §6 "Daily Targets by Day Type". Weight band and floor: DOSSIER §4.  
* Protein floor: **180 g every day**, rest days included. Below 160 g is a priority flag.  
* Day types: `gym`, `z4_quality`, `long_z2`, `z2_easy`, `rest` (plus `deload`, `travel`, `sick`).  
* The deficit gates in §3 Step 4 and §7 only have something to suspend in Phase 2. In the other phases, report energy as "maintenance (phase)".  
* The 80 kg floor in DOSSIER §4 stays in force until the athlete decides otherwise (decision due at the 2027-01-03 checkpoint).

---

## **2\. Data Sources (Priority Order)**

| Priority | File | Contains |
| ----- | ----- | ----- |
| 1 | `latest.json` wellness array | Last 7 days of morning wellness including `weight_kg` (freshest local source) |
| 2 | `history.json` daily wellness entries | 30-day historical `weight_kg` for trend computation |
| 3 | `nutrition.json` | Daily macro intake log (Cronometer-aligned) |
| 3b | `nutrition_meals.json` | Per-food meal breakdown keyed by date; read on food-level questions, not needed for macro compliance |
| 4 | `latest.json` | Training load (CTL, ATL, TSB, ACWR, readiness, planned sessions) |
| 5 | `history.json` | Training trends (weekly TSS, hours, fitness markers) |
| 6 | `DOSSIER.md` §4 and §6 | Weight targets by phase (§4); daily targets by day type and protein floor (§6) |

Weight is logged daily in Intervals.icu's wellness screen (same screen as HRV/RHR) and flows into both `latest.json` (last 7 days) and `history.json` (full history) via `sync.py`. The field name in both files is `weight_kg`. **In local setups where the two files are pulled from GitHub independently, `latest.json` is often fresher than `history.json` — always read both, prefer `latest.json` for any overlapping dates, and use `history.json` only for entries older than the `latest.json` window.** No separate weight file is maintained.

**Data Discipline Rule (mirrors Section 11 Rule 3):** Every nutrition metric cited must come from a file read in the current response. Never cite weights, macros, or intake figures from conversation history or session memory.

**Missing data handling:** If `nutrition.json` is absent, do not attempt to estimate. Before flagging missing weight, compare the most recent date in `latest.json` wellness against the most recent date in `history.json` wellness. If `latest.json` is fresher, this is a local sync lag (`history.json` not pulled recently), not a data gap — proceed using `latest.json` and note the lag in the report so the athlete can `git pull` when convenient. Only prompt the athlete to log weight in Intervals.icu and run `sync.py` when **both** files lack recent entries. Never invent or extrapolate figures.

**Meal detail:** `nutrition.json` holds only daily macro totals — it is deliberately kept compact so it always reads in full. Per-food breakdown lives in `nutrition_meals.json` (keyed by date, written by the same `sync_cronometer.py` run). Read it **only** when the athlete asks a food-level question (e.g. "what did I eat Tuesday", "where are my calories coming from", "which meals are driving the sodium"). The standard macro-compliance review does **not** need it — do not load it routinely.

---

## **3\. Nutrition Coaching Workflow**

When the athlete requests a nutrition review or diet check-in:

### **Step 1 — Load and validate all data sources (in order)**

1. Read `latest.json` wellness array → extract `weight_kg` for the last 7 days  
2. Read `history.json` wellness entries → extract `weight_kg` for days 8–30 prior  
3. Merge into a unified weight series; if any date appears in both files, the `latest.json` value wins  
4. Read `nutrition.json` → extract all daily entries, note most recent date  
5. Read `latest.json` → extract: readiness\_decision, ACWR, TSB, CTL, planned sessions for today and next 7 days  
6. Read `DOSSIER.md` §4 and §6 → confirm the current phase, weight band and day-type targets

**Staleness check:** If the merged weight series has no entries in the last 5 days, flag this before proceeding and prompt the athlete to log weight in Intervals.icu and run `sync.py`. If only `history.json` is stale but `latest.json` has recent wellness entries, this is a local sync lag (run `git pull` in the data repo), not missing data — note it in the report but proceed. Same applies for nutrition: if `nutrition.json` is \> 5 days old, prompt for `sync_cronometer.py`.

### **Step 2 — Compute weight trend analysis**

From the merged `weight_kg` series built in Step 1 (`latest.json` wellness for recent dates, `history.json` wellness for older dates):

1. Calculate 7-day rolling average weight for each available day  
2. Calculate weekly rate of change (kg/week) from the 7-day average  
3. Compare against the current phase weight band (DOSSIER §4) and the checkpoints in the recomposition plan §9  
4. Compare rate against the phase target: hold within the band in Recovery, Phase 1 and Phase 3; lose 0.3 to 0.4 kg/week in Phase 2

**Alert conditions (Phase 2, lean cut):**

* Rate \> 0.7 kg/week → Flag: "Loss rate exceeds safe threshold. Risk of lean mass loss. Recommend increasing kcal by 200–300/day."  
* Rate \< 0.1 kg/week for 3+ consecutive weeks → Flag: "Weight stalled. Review calorie and carb targets for rest/easy days."  
* Rate negative (gaining weight) during non-deload, non-event-week period → Investigate nutrition data for pattern.

**Alert conditions (Recovery, Phase 1, Phase 3: maintenance):**

* 7d average outside the phase band (Phase 1: 80.5 to 82.5 kg) for 7+ days → Flag and review kcal against the day-type table.  
* A gain of 1 to 1.5 kg in the first two weeks of Phase 1 is expected (glycogen refill and creatine water). Do not flag it.

### **Step 3 — Compute nutrition compliance**

From the last 7 days of `nutrition.json`:

1. Cross-reference each day's `day_type` against the macro targets in DOSSIER §6 (current phase column)  
2. Compute daily protein average and the number of days at or above 180 g (the floor applies every day)  
3. Compute daily kcal average — compare against blended target for that week's day type mix  
4. Flag specific days where carbs were mismatched to day type (e.g., low carbs on a Z4/Z5 day is a fuelling error)

**Key compliance checks:**

* Protein \< 180 g on any day → below floor; count the days  
* Protein \< 160 g on any day → Flag as priority correction  
* CHO more than 10% below the day-type target on a `z4_quality`, `long_z2` or `gym` day → Flag as fuelling error  
* CHO more than 10% above the day-type target on a `rest` day → Note  
* kcal more than 300 away from the day-type target for the current phase → Note (in Phase 1 this is calibration data for the maintenance estimate, not a failure)  
* kcal \< 1,800 on any day → Flag immediately

### **Step 4 — Cross-reference training load signals**

From `latest.json` (the gates only bite in Phase 2; in maintenance phases report them for context and keep energy at maintenance):

1. Check ACWR → if ≥ 1.3, recommend suspending caloric deficit and eating to maintenance  
2. Check TSB → if \< −25, recommend maintenance calories  
3. Check readiness\_decision → if "modify" or "skip", flag that deficit days should be paused  
4. Check planned sessions for next 7 days → generate day-by-day carb/calorie targets

**Integration rule:** The training load signal always overrides the diet plan. A hard training week is not a weight loss week. This is by design.

### **Step 5 — Generate fueling plan for next 7 days**

For each of the next 7 days (using planned sessions from `latest.json` calendar):

* Assign a `day_type` from the DOSSIER §6 taxonomy (`gym`, `z4_quality`, `long_z2`, `z2_easy`, `rest`)  
* State kcal target, protein target, and CHO target for that day  
* Flag any upcoming quality sessions with pre/post-workout nutrition reminders  
* Flag gym days: 35 to 45 g protein within 2 h after the session, and a high-carb dinner

---

## **4\. Output Format (Deterministic)**

### **Nutrition Coach Report Structure**

NUTRITION COACH REPORT — \[DATE\]  
Data: weight last entry \[DATE\] (history.json) | nutrition.json last entry \[DATE\] | latest.json \[UTC TIMESTAMP\]

WEIGHT TREND  
  Current 7d avg: \[X.X\] kg  
  Rate (7d): \[+/-X.X\] kg/week  
  Phase: \[Recovery | 1 Rebuild | 2 Lean cut | 3 Consolidate\] | Target: \[hold 80.5 to 82.5 kg | lose 0.3 to 0.4 kg/week | hold\]  
  Milestone status: \[on track / ahead / behind\] — \[milestone date\]: target \[X.X\] kg, current trajectory \[X.X\] kg  
  Alert: \[if any\]

NUTRITION COMPLIANCE (last 7 days)  
  Avg protein: \[X\] g/day | days at or above 180 g: \[N\]/7  
  Avg kcal: \[X\] kcal/day  
  Carb periodization: \[compliant / N days mismatched\]  
  Flagged days: \[specific dates and issue if any\]

TRAINING LOAD OVERLAY  
  ACWR: \[X.XX\] | \[Phase 2: deficit OK / suspend deficit; other phases: maintenance (phase)\]  
  TSB: \[X\] — \[note if \< −25\]  
  Readiness today: \[go/modify/skip\]

NEXT 7 DAYS — FUELING PLAN  
  \[Date\] \[Day type\] — \[kcal\] kcal | \[protein\] g protein | \[CHO\] g carbs  
  \[Date\] \[Day type\] — ...  
  \[notes for quality sessions, gym days, pre/post nutrition reminders\]

COACH NOTE  
  \[2–3 sentences: primary observation, one adjustment if needed, one positive reinforcement\]

**Format rules:**

* Use structured lines, not bullet points (mirrors Section 11 output format)  
* Maximum 3 flagged items — prioritise most actionable  
* Do NOT provide calorie counts to 1-decimal precision; round to nearest 50 kcal  
* Do NOT cite "per Section 12"  
* Do NOT ask follow-up questions when data is complete  
* Do NOT conflate training performance with nutrition — they are reported separately

---

## **5\. Carb Periodization Validation Rules**

When evaluating `nutrition.json` against the DOSSIER §6 targets for the current phase:

| Condition | Classification | Coach Response |
| ----- | ----- | ----- |
| CHO more than 10% above the day-type target on a rest day | Overfuelled | Note and suggest trimming starch |
| CHO more than 10% below the day-type target on `z4_quality`, `long_z2` or `gym` | Under-fuelled | Flag as fuelling error |
| Protein \< 180 g any day | Below floor | Count toward weekly protein compliance |
| Protein \< 160 g any day | Insufficient | Flag as priority correction |
| kcal \< 1,800 any day | Dangerously low | Flag immediately; not compatible with training |

---

## **6\. Weight Trend Computation**

### **7-Day Rolling Average**

7d\_avg\[d\] \= mean(weight\_kg for days d-6 through d)

Requires minimum 3 entries to compute (flag if fewer than 3 entries present).

### **Weekly Rate of Change**

weekly\_rate \= 7d\_avg\[most recent day\] \- 7d\_avg\[7 days prior\]

Expressed as kg/week. Negative \= weight loss. Positive \= weight gain.

### **Trajectory to Goal (Phase 2 only)**

Applies during the lean cut (2027-01-04 to 2027-04-04). In maintenance phases, report the 7d average against the phase band instead.

weeks\_remaining \= (2027-04-04 \- today).days / 7  
current\_deficit\_from\_goal \= current\_7d\_avg \- cut\_end\_target\_kg (77.5 kg)  
required\_rate \= current\_deficit\_from\_goal / weeks\_remaining

Compare `required_rate` against `target_rate_kg_per_week` (0.35 kg/week):

* required\_rate ≤ 0.45 kg/week → on track  
* required\_rate 0.45 to 0.6 kg/week → behind: accept a slightly higher end weight rather than speeding up  
* required\_rate \> 0.6 kg/week → do not chase it; extend the cut or accept the landing point, because losing faster than 0.6 kg/week costs lean mass

**Do not recommend aggressive deficit if ACWR ≥ 1.3 or TSB \< −25, even if behind trajectory.** If the weight floor decision (DOSSIER §4) is still open when the 7d average approaches 80 kg, hold at 80 kg and ask the athlete.

---

## **7\. Interaction with Section 11 Readiness Protocol**

Nutrition data provides **contextual enrichment** to Section 11 readiness decisions but does **not** enter the P0–P3 readiness ladder.

**Cross-protocol rules:**

* If readiness\_decision \= "skip" → nutrition recommendation switches to maintenance kcal. No deficit.  
* If readiness\_decision \= "modify" → reduce CHO slightly on easy substitute session; maintain protein.  
* If HRV drop \>20% sustained → suspend deficit; investigate whether under-fuelling is a contributing factor (cross-reference kcal average over prior 5 days).  
* If RHR ↑≥5 bpm sustained → same as above.  
* Fasted sessions are not part of the recomposition programme; do not recommend them.

---

## **8\. Milestone Check-In Protocol**

At each checkpoint in the recomposition plan (§9: 15 Nov, 13 Dec, 3 Jan, 31 Jan, 28 Feb, 4 Apr, 2 May):

1. Compute current 7d average vs milestone target  
2. Compute delta (kg ahead/behind)  
3. Assess whether gap requires protocol adjustment or is within normal variance  
4. Review protein compliance over prior 4 weeks — consistent under-target protein is the most common reason for lean mass loss alongside fat  
5. Review the lifting log and the bioimpedance lean-mass trend (2 to 4 week average). Lifts rising while the scale is flat is recomposition working, not a stall.

**Output:** One paragraph milestone summary, 3 sentences maximum.

---

## **9\. SKILL.md Integration**

Add the following block to SKILL.md under **Data Sources** / **Optional files**:

\#\#\# Nutrition Data (Section 12\)  
\- \`nutrition.json\` — daily macro log (Cronometer-aligned); triggers nutrition compliance review  
\- \`nutrition\_meals.json\` — per-food meal breakdown keyed by date; read only on food-level questions, not for routine macro review  
\- \`SECTION\_12.md\` — nutrition coaching protocol; load when nutrition review requested  
\- Weight data — read \`weight\_kg\` from \`latest.json\` wellness array first (freshest 7-day window), then \`history.json\` wellness entries for older dates (logged via Intervals.icu)

When present, load nutrition data after training data. Nutrition coaching is a separate output section, not merged with the training report. Section 12 governs all nutrition output.  
---

## **10\. Cronometer Export Workflow**

When the athlete provides a Cronometer CSV export:

1. Parse the CSV for the `Daily Nutrition` sheet (not individual food entries)  
2. Extract columns: Date, Energy (kcal), Protein (g), Carbohydrates (g), Fat (g), Fiber (g), Water (g)  
3. Map each row to a `nutrition.json` daily entry  
4. Ask athlete to specify `day_type` for each date (or infer from `latest.json` calendar if available)  
5. Append to `nutrition.json` — do not overwrite existing entries  
6. Confirm row count and date range before writing

---

## **11\. Protocol Version History**

| Version | Date | Changes |
| ----- | ----- | ----- |
| 12.0 | 2026-04-16 | Initial release — daily nutrition, weight trend, carb periodization, Section 11 integration |
| 12.1 | 2026-04-16 | Weight source changed from weight\_history.json to history.json wellness entries (Intervals.icu pipeline) |
| 12.2 | 2026-05-15 | Rest day protein floor lowered to 160–175 g (175–195 g is reserved for training days; macro maths confirmed at 99 kg). Z4 quality carb target corrected to 277–340 g (2.8–3.5 g/kg) — prior 388–485 g target caused macro sum to exceed kcal ceiling by ~400 kcal. Validation rules updated accordingly. |
| 12.3 | 2026-06-07 | Per-food meal detail split out of `nutrition.json` into a new `nutrition_meals.json` (keyed by date) so `nutrition.json` stays compact and always reads in full — embedded meals had grown it past the file-read truncation limit, hiding recent days from review. `nutrition_meals.json` is read on demand for food-level questions only; macro-compliance review is unchanged. |
| 12.4 | 2026-10-11 | Recomposition programme: new §1a phase context (maintenance in Recovery, Phase 1 and Phase 3; deficit only in Phase 2); protein floor 180 g every day; `gym` day type; compliance checks and carb validation read the current phase column in DOSSIER §6; trajectory maths limited to Phase 2 with a 0.6 kg/week ceiling; dead DOSSIER references (6.9, 6.11) removed. |

