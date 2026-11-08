## DATA ACCESS:
1. Read latest.json from the data directory
2. Read history.json from the data directory
3. Read intervals.json when analyzing a specific activity which has_intervals: true or has_dfa: true
4. Read routes.json when a planned event has has_terrain: true
5. Read protocol from SECTION_11.md
6. Read report templates from examples/reports/
7. Read workout templates from examples/workout-library/WORKOUT_REFERENCE.md
8. When nutrition review is requested: read nutrition.json from the data directory, then read SECTION_12.md
9. Weight data comes from the `weight` field in history.json daily wellness entries — do NOT look for a separate weight file
10. If data files appear stale, ask the athlete to run sync (training: sync.py / nutrition: sync_cronometer.py)
Do NOT fetch from URLs — all files are local, EXCEPT if being asked to suggest specific Zwift workouts, if so, then search URLs. If any data file is missing or unreadable, stop and ask the user to run sync.py rather than falling back to URL fetching.

## DOCUMENTS:
- SECTION_11.md — training protocol
- SECTION_12.md — nutrition & diet protocol (load only when nutrition review requested)
- DOSSIER.md — athlete profile
- examples/reports/ — report templates
- examples/workout-library/WORKOUT_REFERENCE.md — session templates for planning
- recomposition-plan-2026-10-19.md: the current programme (Oct 2026 to May 2027): phases, weekly template, gym programme, nutrition targets, checkpoints
- gym/Revised Gym Routine II.xlsx: the athlete's gym spreadsheet (machines, starting weights, hip mobility). Read it for any gym question; the Gym A/B sessions built from it are in recomposition-plan §6

## NUTRITION COACHING:

**Triggers:** Any request involving food, meals, calories, weight, macros, fueling, recipes, or cooking.

**Preflight (mandatory):** Read SECTION_12.md §1a and §3 Step 4. Open response with a single line: `Phase: [Recovery | 1 Rebuild | 2 Lean cut | 3 Consolidate] | Energy: [maintenance | deficit active | deficit paused: <triggering signal>]`. The deficit gates only apply in Phase 2. Protein floor is 180 g every day.

**Reads:**
- nutrition.json (always; flag any date where day_type is missing)
- nutrition_meals.json (only on food-level questions — what was eaten, calorie/macro sources; not for routine macro review)
- SECTION_12.md: §1a and §3 Step 4 for preflight, full file for deep reviews
- DOSSIER.md §4 for the phase weight band and floor, §6 for daily targets by day type
- latest.json wellness for weight_kg (preferred over history.json)

**Output:** Keep as a separate block from training reports.

**Dinner suggestions:** After preflight, suggest your own recipes. Do not use cooking book list.txt (retired 2026-10-11). Pescatarian: fish and seafood yes, no meat or poultry. Vegetarian dishes are fine too, so don't default to fish every night. Match the recipe to the evening's day_type: high-carb (pasta, grains, legumes) for gym, quality and long-ride days; protein-forward, lower-starch for rest and easy. Aim for ~40 g protein at dinner. Give ingredients with quantities per serving, the method, and approximate kcal and protein per serving. Flag weeknight (≤45 min active prep) vs weekend.