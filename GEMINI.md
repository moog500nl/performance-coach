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

## NUTRITION COACHING:

**Triggers:** Any request involving food, meals, calories, weight, macros, fueling, recipes, or cooking.

**Preflight (mandatory):** Read SECTION_12.md §4. Open response with a single line: `Deficit status: [active | suspended | paused] — [triggering signal]`. Apply §4's rules to all sizing.

**Reads:**
- nutrition.json (always; flag any date where day_type is missing)
- SECTION_12.md — §4 for preflight, full file for deep reviews
- DOSSIER.md §6 for weight goal trajectory
- latest.json wellness for weight_kg (preferred over history.json)
- cooking book list.txt (dinner suggestions only)

**Output:** Keep as a separate block from training reports.

**Dinner suggestions:** After preflight, match recipes to the evening's day_type — high-carb (pasta, grains, legumes) for Z4 / long Z2 / back-to-back; protein-forward, lower-starch for rest and easy. Flag weeknight (≤45 min active prep) vs weekend.