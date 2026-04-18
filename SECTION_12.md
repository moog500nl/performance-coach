# **Section 12 — Daily Nutrition & Weight Coaching Protocol (v12.0)**

**Protocol Version:** 12.1 **Last Updated:** 2026-04-16 **Companion to:** SECTION\_11.md (AI Coach Protocol v11.33+) **License:** MIT

---

## **1\. Purpose & Scope**

Section 12 governs daily nutrition coaching: weight trajectory monitoring, macro compliance, carb periodization alignment, and fueling recommendations relative to training load.

Section 11 v11.26 covers **in-ride** fueling (KJ→carbs dosing, absorption limits, W′ depletion). Section 12 covers **off-bike daily nutrition** — strategic diet management in tandem with the training programme.

---

## **2\. Data Sources (Priority Order)**

| Priority | File | Contains |
| ----- | ----- | ----- |
| 1 | `history.json` daily wellness entries | Morning body weight (logged via Intervals.icu wellness) |
| 2 | `nutrition.json` | Daily macro intake log (Cronometer-aligned) |
| 3 | `latest.json` | Training load (CTL, ATL, TSB, ACWR, readiness, planned sessions) |
| 4 | `history.json` | Training trends (weekly TSS, hours, fitness markers) |
| 5 | `DOSSIER.md Section 6` | Nutrition targets and weight goals |

Weight is logged daily in Intervals.icu's wellness screen (same screen as HRV/RHR) and flows into `history.json` via `sync.py`. The `weight` field appears in each day's wellness entry. No separate weight file is maintained.

**Data Discipline Rule (mirrors Section 11 Rule 3):** Every nutrition metric cited must come from a file read in the current response. Never cite weights, macros, or intake figures from conversation history or session memory.

**Missing data handling:** If `nutrition.json` is absent, do not attempt to estimate. If weight entries are missing from `history.json` wellness fields, prompt the athlete to log weight in Intervals.icu and run `sync.py`. Never invent or extrapolate figures.

---

## **3\. Nutrition Coaching Workflow**

When the athlete requests a nutrition review or diet check-in:

### **Step 1 — Load and validate all data sources (in order)**

1. Read `history.json` → extract `weight` field from daily wellness entries for the last 30 days  
2. Read `nutrition.json` → extract all daily entries, note most recent date  
3. Read `latest.json` → extract: readiness\_decision, ACWR, TSB, CTL, planned sessions for today and next 7 days  
4. Read `DOSSIER.md` Section 6 → confirm targets

**Staleness check:** If weight wellness entries or nutrition data are \> 5 days old, flag this before proceeding. Prompt athlete to log weight in Intervals.icu and run `sync.py`, or to export from Cronometer and run `sync_cronometer.py`.

### **Step 2 — Compute weight trend analysis**

From `history.json` daily wellness `weight` entries:

1. Calculate 7-day rolling average weight for each available day  
2. Calculate weekly rate of change (kg/week) from the 7-day average  
3. Compare against milestones from DOSSIER Section 6.11  
4. Compare rate against target range (0.3–0.5 kg/week)

**Alert conditions:**

* Rate \> 0.7 kg/week → Flag: "Loss rate exceeds safe threshold. Risk of lean mass loss. Recommend increasing kcal by 200–300/day."  
* Rate \< 0.1 kg/week for 3+ consecutive weeks → Flag: "Weight stalled. Review calorie and carb targets for rest/easy days."  
* Rate negative (gaining weight) during non-deload, non-event-week period → Investigate nutrition data for pattern.

### **Step 3 — Compute nutrition compliance**

From the last 7 days of `nutrition.json`:

1. Cross-reference each day's `day_type` against the macro targets in DOSSIER Section 6  
2. Compute daily protein average — compare against 175–195 g target  
3. Compute daily kcal average — compare against blended target for that week's day type mix  
4. Flag specific days where carbs were mismatched to day type (e.g., low carbs on a Z4/Z5 day is a fuelling error)

**Key compliance checks:**

* Protein \< 160 g on any day → Flag (insufficient for muscle preservation)  
* CHO \< 200 g on a Z4/Z5 day → Flag as fuelling error (training quality at risk)  
* CHO \> 350 g on a rest day → Flag (undermining weight loss target)  
* kcal \> 3,500 on a rest day → Flag

### **Step 4 — Cross-reference training load signals**

From `latest.json`:

1. Check ACWR → if ≥ 1.3, recommend suspending caloric deficit and eating to maintenance  
2. Check TSB → if \< −25, recommend maintenance calories  
3. Check readiness\_decision → if "modify" or "skip", flag that deficit days should be paused  
4. Check planned sessions for next 7 days → generate day-by-day carb/calorie targets

**Integration rule:** The training load signal always overrides the diet plan. A hard training week is not a weight loss week. This is by design.

### **Step 5 — Generate fueling plan for next 7 days**

For each of the next 7 days (using planned sessions from `latest.json` calendar):

* Assign a `day_type` from DOSSIER Section 6 taxonomy  
* State kcal target, protein target, and CHO target for that day  
* Flag any upcoming quality sessions with pre/post-workout nutrition reminders  
* Flag back-to-back days and confirm Day 1 dinner CHO loading priority

---

## **4\. Output Format (Deterministic)**

### **Nutrition Coach Report Structure**

NUTRITION COACH REPORT — \[DATE\]  
Data: weight last entry \[DATE\] (history.json) | nutrition.json last entry \[DATE\] | latest.json \[UTC TIMESTAMP\]

WEIGHT TREND  
  Current 7d avg: \[X.X\] kg  
  Rate (7d): \[+/-X.X\] kg/week  
  Target rate: −0.3 to −0.5 kg/week  
  Milestone status: \[on track / ahead / behind\] — \[milestone date\]: target \[X.X\] kg, current trajectory \[X.X\] kg  
  Alert: \[if any\]

NUTRITION COMPLIANCE (last 7 days)  
  Avg protein: \[X\] g/day — \[on target / below target / above target\]  
  Avg kcal: \[X\] kcal/day  
  Carb periodization: \[compliant / N days mismatched\]  
  Flagged days: \[specific dates and issue if any\]

TRAINING LOAD OVERLAY  
  ACWR: \[X.XX\] — \[deficit OK / suspend deficit\]  
  TSB: \[X\] — \[note if \< −25\]  
  Readiness today: \[go/modify/skip\]

NEXT 7 DAYS — FUELING PLAN  
  \[Date\] \[Day type\] — \[kcal\] kcal | \[protein\] g protein | \[CHO\] g carbs  
  \[Date\] \[Day type\] — ...  
  \[notes for quality sessions, back-to-back days, pre/post nutrition reminders\]

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

When evaluating `nutrition.json` against DOSSIER targets:

| Condition | Classification | Coach Response |
| ----- | ----- | ----- |
| CHO ≥ 350 g on rest day | Overfuelled | Note and suggest 150–200 g reduction |
| CHO ≥ 350 g on Z2 easy day | Acceptable upper range | No flag |
| CHO \< 250 g on Z4/Z5 day | Under-fuelled | Flag as fuelling error |
| CHO \< 300 g on long Z2 (2h+) | Under-fuelled | Flag — likely to compromise session quality |
| Protein \< 160 g any day | Insufficient | Flag as priority correction |
| kcal \< 1,800 any day | Dangerously low | Flag immediately — not compatible with training |

---

## **6\. Weight Trend Computation**

### **7-Day Rolling Average**

7d\_avg\[d\] \= mean(weight\_kg for days d-6 through d)

Requires minimum 3 entries to compute (flag if fewer than 3 entries present).

### **Weekly Rate of Change**

weekly\_rate \= 7d\_avg\[most recent day\] \- 7d\_avg\[7 days prior\]

Expressed as kg/week. Negative \= weight loss. Positive \= weight gain.

### **Trajectory to Goal**

weeks\_remaining \= (goal\_date \- today).days / 7  
current\_deficit\_from\_goal \= current\_7d\_avg \- goal\_weight\_kg  
required\_rate \= current\_deficit\_from\_goal / weeks\_remaining

Compare `required_rate` against `target_rate_kg_per_week` (0.4 kg/week):

* required\_rate ≤ 0.6 kg/week → on track  
* required\_rate 0.6–0.8 kg/week → slightly behind — moderate adjustment  
* required\_rate \> 0.8 kg/week → significantly behind — review protocol

**Do not recommend aggressive deficit if ACWR ≥ 1.3 or TSB \< −25, even if behind trajectory.**

---

## **7\. Interaction with Section 11 Readiness Protocol**

Nutrition data provides **contextual enrichment** to Section 11 readiness decisions but does **not** enter the P0–P3 readiness ladder.

**Cross-protocol rules:**

* If readiness\_decision \= "skip" → nutrition recommendation switches to maintenance kcal. No deficit.  
* If readiness\_decision \= "modify" → reduce CHO slightly on easy substitute session; maintain protein.  
* If HRV drop \>20% sustained → suspend deficit; investigate whether under-fuelling is a contributing factor (cross-reference kcal average over prior 5 days).  
* If RHR ↑≥5 bpm sustained → same as above.  
* Fasted Z2 sessions (DOSSIER 6.9) require RI ≥ 0.85 — this gate is sourced from `latest.json`; confirm before recommending.

---

## **8\. Milestone Check-In Protocol**

At each monthly milestone (see DOSSIER Section 6.11):

1. Compute current 7d average vs milestone target  
2. Compute delta (kg ahead/behind)  
3. Assess whether gap requires protocol adjustment or is within normal variance  
4. Review protein compliance over prior 4 weeks — consistent under-target protein is the most common reason for lean mass loss alongside fat  
5. Review training phase — if CTL building strongly, a slightly slower weight loss rate is acceptable

**Output:** One paragraph milestone summary, 3 sentences maximum.

---

## **9\. SKILL.md Integration**

Add the following block to SKILL.md under **Data Sources** / **Optional files**:

\#\#\# Nutrition Data (Section 12\)  
\- \`nutrition.json\` — daily macro log (Cronometer-aligned); triggers nutrition compliance review  
\- \`SECTION\_12.md\` — nutrition coaching protocol; load when nutrition review requested  
\- Weight data — read from \`history.json\` daily wellness \`weight\` field (logged via Intervals.icu)

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

