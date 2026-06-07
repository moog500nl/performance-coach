"""
sync_cronometer.py — Converts Cronometer CSV exports to nutrition.json
Mirrors the pattern of sync.py (intervals.icu → JSON mirror)
 
Protocol: Section 12 — Daily Nutrition & Weight Coaching (v12.0)
 
Usage:
    python sync_cronometer.py
    python sync_cronometer.py --data-dir ./data
    python sync_cronometer.py --dry-run
 
Input (place in data/cronometer/ — filename doesn't matter, globs by type):
    dailysummary*.csv   from Cronometer → Settings → Export Data → Daily Nutrition
    servings*.csv       from Cronometer → Settings → Export Data → Servings
 
Output:
    data/nutrition.json        daily macro totals — kept compact so it always
                               reads in full (no meal detail embedded)
    data/nutrition_meals.json  per-food meal breakdown, keyed by date; look here
                               when you need food-level detail for a given day
 
Merge behaviour:
    Existing entries in nutrition.json are preserved.
    New dates are added. Existing dates are updated with fresh CSV values for
    numeric nutrition fields. The fields 'day_type' and 'notes' are NEVER
    overwritten by the CSV — they must be set manually or by the coach.
"""
 
import csv
import json
import os
import sys
import glob
import hashlib
import argparse
import tempfile
from datetime import datetime, date, timezone
from pathlib import Path
from collections import defaultdict
 
SCRIPT_VERSION = "1.0.0"
SCRIPT_HASH = hashlib.md5(open(__file__, "rb").read()).hexdigest()[:8]
 
# ---------------------------------------------------------------------------
# Column mapping: Cronometer daily summary CSV → nutrition.json field names
# ---------------------------------------------------------------------------
DAILY_FIELD_MAP = {
    "Energy (kcal)":        "kcal_consumed",
    "Protein (g)":          "protein_g",
    "Carbs (g)":            "carbs_g",
    "Net Carbs (g)":        "net_carbs_g",
    "Fiber (g)":            "fiber_g",
    "Fat (g)":              "fat_g",
    "Water (g)":            "water_ml",       # 1 g water = 1 ml
    "Sodium (mg)":          "sodium_mg",
    "Potassium (mg)":       "potassium_mg",
    "Sugars (g)":           "sugars_g",
    "Added Sugars (g)":     "added_sugars_g",
    "Saturated (g)":        "saturated_fat_g",
    "Omega-3 (g)":          "omega3_g",
    "Calcium (mg)":         "calcium_mg",
    "Iron (mg)":            "iron_mg",
    "Vitamin D (IU)":       "vitamin_d_iu",
    "Completed":            "_completed",     # internal flag, not stored in output
}
 
# Fields stored in final JSON (subset — coach-relevant only)
COACH_FIELDS = [
    "kcal_consumed", "protein_g", "carbs_g", "net_carbs_g", "fiber_g",
    "fat_g", "water_ml", "sodium_mg", "potassium_mg", "sugars_g",
    "added_sugars_g", "saturated_fat_g", "omega3_g",
    "calcium_mg", "iron_mg", "vitamin_d_iu",
]
 
# Targets from DOSSIER Section 6 — used for compliance metadata
TARGETS = {
    "protein_g":      {"min": 175, "max": 195, "note": "daily target, all day types"},
    "fat_g":          {"min": 70,  "max": 90,  "note": "stable across day types"},
}
CARB_TARGETS_BY_DAY_TYPE = {
    "rest":                {"min": 145, "max": 195},
    "z2_easy":             {"min": 242, "max": 291},
    "z4_quality":          {"min": 388, "max": 485},
    "long_z2":             {"min": 388, "max": 485},
    "back_to_back_day1":   {"min": 435, "max": 485},
    "back_to_back_day2":   {"min": 435, "max": 485},
    "deload":              {"min": 200, "max": 250},
    "travel":              {"min": 200, "max": 300},
    "sick":                {"min": 150, "max": 250},
}
KCAL_TARGETS_BY_DAY_TYPE = {
    "rest":                {"min": 2100, "max": 2300},
    "z2_easy":             {"min": 2400, "max": 2600},
    "z4_quality":          {"min": 2700, "max": 2900},
    "long_z2":             {"min": 3000, "max": 3300},
    "back_to_back_day1":   {"min": 3100, "max": 3400},
    "back_to_back_day2":   {"min": 3100, "max": 3400},
    "deload":              {"min": 2200, "max": 2400},
    "travel":              {"min": 2200, "max": 2800},
    "sick":                {"min": 1800, "max": 2400},
}
 
 
def parse_float(val):
    """Safely parse a CSV value to float; return None if blank or non-numeric."""
    if val is None:
        return None
    val = str(val).strip()
    if val == "" or val.lower() in ("", "n/a", "-"):
        return None
    try:
        return round(float(val), 2)
    except ValueError:
        return None
 
 
def parse_bool(val):
    if val is None:
        return None
    return str(val).strip().lower() == "true"
 
 
def read_daily_summaries(input_dir: Path) -> dict:
    """Read all dailysummary*.csv files; return dict keyed by date string."""
    entries = {}
    pattern = str(input_dir / "dailysummary*.csv")
    files = sorted(glob.glob(pattern))
 
    if not files:
        print(f"  [warn] No dailysummary*.csv found in {input_dir}")
        return entries
 
    for fpath in files:
        print(f"  Reading daily summary: {fpath}")
        with open(fpath, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                date_str = row.get("Date", "").strip()
                if not date_str:
                    continue
                # Validate date format
                try:
                    datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    print(f"  [warn] Skipping row with invalid date: {date_str}")
                    continue
 
                entry = {"date": date_str}
                for csv_col, json_field in DAILY_FIELD_MAP.items():
                    if csv_col in row:
                        if json_field == "_completed":
                            entry["_completed"] = parse_bool(row[csv_col])
                        else:
                            val = parse_float(row[csv_col])
                            if val is not None:
                                entry[json_field] = val
 
                # Water: Cronometer reports grams; 1g = 1ml — already correct field name
                entries[date_str] = entry
 
    print(f"  Loaded {len(entries)} day(s) from daily summary files")
    return entries
 
 
def read_servings(input_dir: Path) -> dict:
    """
    Read all servings*.csv files.
    Returns dict keyed by date string, value is a list of meal groups
    with simplified food entries.
    """
    meals_by_date = defaultdict(lambda: defaultdict(list))
    pattern = str(input_dir / "servings*.csv")
    files = sorted(glob.glob(pattern))
 
    if not files:
        print(f"  [info] No servings*.csv found — skipping meal detail")
        return {}
 
    for fpath in files:
        print(f"  Reading servings: {fpath}")
        with open(fpath, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                date_str = row.get("Day", "").strip()
                if not date_str:
                    continue
                try:
                    datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    continue
 
                group = row.get("Group", "Uncategorized").strip().strip('"')
                food_name = row.get("Food Name", "").strip().strip('"')
                amount = row.get("Amount", "").strip()
                kcal = parse_float(row.get("Energy (kcal)"))
                protein = parse_float(row.get("Protein (g)"))
                carbs = parse_float(row.get("Carbs (g)"))
                fat = parse_float(row.get("Fat (g)"))
                time_str = row.get("Time", "").strip()
 
                if food_name:
                    food_entry = {
                        "food": food_name,
                        "amount": amount,
                        "kcal": kcal,
                        "protein_g": protein,
                        "carbs_g": carbs,
                        "fat_g": fat,
                    }
                    if time_str:
                        food_entry["time"] = time_str
                    # Remove None values to keep JSON compact
                    food_entry = {k: v for k, v in food_entry.items() if v is not None}
                    meals_by_date[date_str][group].append(food_entry)
 
    # Convert defaultdicts to plain dicts
    result = {}
    for date_str, groups in meals_by_date.items():
        result[date_str] = {group: items for group, items in groups.items()}
 
    print(f"  Loaded meal detail for {len(result)} day(s) from servings files")
    return result
 
 
def compute_compliance(entry: dict) -> dict:
    """
    Compute a simple compliance summary against DOSSIER Section 6 targets.
    Returns a dict with flags for the coach to read.
    """
    flags = []
    day_type = entry.get("day_type")
 
    protein = entry.get("protein_g")
    if protein is not None:
        if protein < 160:
            flags.append(f"protein_low:{protein:.0f}g (target 175-195g)")
        elif protein < 175:
            flags.append(f"protein_below_target:{protein:.0f}g (target 175-195g)")
 
    kcal = entry.get("kcal_consumed")
    if kcal is not None and kcal < 1800:
        flags.append(f"kcal_critically_low:{kcal:.0f} (min 1800 on any day)")
 
    if day_type:
        carbs = entry.get("carbs_g") or entry.get("net_carbs_g")
        if carbs is not None and day_type in CARB_TARGETS_BY_DAY_TYPE:
            t = CARB_TARGETS_BY_DAY_TYPE[day_type]
            if carbs < t["min"]:
                flags.append(f"carbs_low_for_{day_type}:{carbs:.0f}g (target {t['min']}-{t['max']}g)")
            elif carbs > t["max"] * 1.1:  # 10% tolerance above upper
                flags.append(f"carbs_high_for_{day_type}:{carbs:.0f}g (target {t['min']}-{t['max']}g)")
 
        if kcal is not None and day_type in KCAL_TARGETS_BY_DAY_TYPE:
            t = KCAL_TARGETS_BY_DAY_TYPE[day_type]
            if kcal < t["min"] - 200:
                flags.append(f"kcal_low_for_{day_type}:{kcal:.0f} (target {t['min']}-{t['max']})")
            elif kcal > t["max"] + 200:
                flags.append(f"kcal_high_for_{day_type}:{kcal:.0f} (target {t['min']}-{t['max']})")
 
    return {"flags": flags} if flags else {}


def load_training_data(data_dir: Path) -> dict:
    """
    Load training data from history.json and latest.json.
    Returns a dict mapping date string (YYYY-MM-DD) to a dict of training features:
    {
        "activity_types": set of strings,
        "total_hours": float,
        "total_tss": float,
        "is_hard_day": bool
    }
    """
    training = {}
    
    # 1. Load history.json if available
    history_path = data_dir / "history.json"
    if history_path.exists():
        try:
            with open(history_path, 'r') as f:
                history_data = json.load(f)
            daily_90d = history_data.get("daily_90d", [])
            for day in daily_90d:
                date_str = day.get("date", "").split("T")[0]
                if date_str:
                    act_types_str = day.get("activity_types", "")
                    act_types = set()
                    if act_types_str:
                        act_types = {t.strip() for t in act_types_str.split(",") if t.strip()}
                    training[date_str] = {
                        "activity_types": act_types,
                        "total_hours": day.get("total_hours", 0.0) or 0.0,
                        "total_tss": day.get("total_tss", 0.0) or 0.0,
                        "is_hard_day": day.get("is_hard_day", False) or False
                    }
        except Exception as e:
            print(f"  [warn] Failed to parse history.json for day classification: {e}")
            
    # 2. Load latest.json if available (overwriting/updating history)
    latest_path = data_dir / "latest.json"
    if latest_path.exists():
        try:
            with open(latest_path, 'r') as f:
                latest_data = json.load(f)
            
            # Aggregate recent activities
            recent_activities = latest_data.get("recent_activities", [])
            for act in recent_activities:
                date_str = act.get("date", act.get("start_date_local", "")).split("T")[0]
                if not date_str:
                    continue
                act_type = act.get("type", "")
                duration_hours = act.get("duration_hours", 0.0) or 0.0
                tss = act.get("tss", 0.0) or 0.0
                
                is_hard = False
                if tss >= 50 and act_type in ("Ride", "VirtualRide"):
                    # Check intensity factor or RPE
                    intensity_factor = act.get("intensity_factor", 0.0) or 0.0
                    rpe = act.get("rpe", 0) or 0
                    if intensity_factor >= 70.0 or rpe >= 5:
                        is_hard = True
                if act.get("has_intervals", False):
                    is_hard = True
                
                if date_str not in training:
                    training[date_str] = {
                        "activity_types": set(),
                        "total_hours": 0.0,
                        "total_tss": 0.0,
                        "is_hard_day": False
                    }
                
                if act_type:
                    training[date_str]["activity_types"].add(act_type)
                training[date_str]["total_hours"] += duration_hours
                training[date_str]["total_tss"] += tss
                if is_hard:
                    training[date_str]["is_hard_day"] = True
        except Exception as e:
            print(f"  [warn] Failed to parse latest.json for day classification: {e}")
            
    return training


def classify_day_type(date_str: str, training_data: dict) -> str:
    """
    Classifies the day_type for a date based on training logs.
    Taxonomy: rest | z2_easy | z4_quality | long_z2
    """
    day_info = training_data.get(date_str)
    if not day_info:
        return "rest"
        
    act_types = day_info.get("activity_types", set())
    total_hours = day_info.get("total_hours", 0.0)
    total_tss = day_info.get("total_tss", 0.0)
    is_hard_day = day_info.get("is_hard_day", False)
    
    # If no activities or hours/TSS is zero
    if not act_types or (total_hours == 0.0 and total_tss == 0.0):
        return "rest"
        
    # Walk only
    if len(act_types) == 1 and "Walk" in act_types:
        if total_hours >= 2.0:
            return "long_z2" # Walk >= 2h counts as long Z2 load-bearing conditioning
        return "rest" # Easy short walk is active recovery/rest
        
    # Cycling / Riding is present
    has_cycling = any(t in act_types for t in ("Ride", "VirtualRide", "MountainBikeRide", "GravelRide", "EBikeRide"))
    if has_cycling:
        if total_hours >= 2.0: # 120 min or more
            return "long_z2"
        elif is_hard_day or total_tss >= 50:
            return "z4_quality"
        else:
            return "z2_easy"
            
    # Default fallback for other sports (e.g. Strength, Run, Swim)
    if total_hours >= 2.0:
        return "long_z2"
    elif is_hard_day or total_tss >= 50:
        return "z4_quality"
    else:
        return "z2_easy"


def merge_into_existing(existing: list, new_by_date: dict, meals_by_date: dict, training_data: dict) -> list:
    """
    Merge new CSV data into existing nutrition.json entries.
    Rules:
    - Numeric nutrition fields: CSV wins (fresh data)
    - 'day_type': preserved from existing if already set; never overwritten. If None or missing, auto-classified.
    - 'notes': preserved from existing; never overwritten
    - 'meals': added from servings CSV if available; preserved if not
    - New dates are appended
    """
    existing_by_date = {e["date"]: e for e in existing if "date" in e}
 
    for date_str, csv_entry in new_by_date.items():
        if date_str in existing_by_date:
            existing_entry = existing_by_date[date_str]
            # Update numeric fields from CSV
            for field in COACH_FIELDS:
                if field in csv_entry:
                    existing_entry[field] = csv_entry[field]
            # Preserve day_type and notes — never overwrite unless day_type is missing/None
            if not existing_entry.get("day_type"):
                existing_entry["day_type"] = classify_day_type(date_str, training_data)
            # day_complete: update from CSV
            if "_completed" in csv_entry:
                existing_entry["day_complete"] = csv_entry["_completed"]
        else:
            # New date — build fresh entry
            new_entry = {"date": date_str}
            for field in COACH_FIELDS:
                if field in csv_entry:
                    new_entry[field] = csv_entry[field]
            if "_completed" in csv_entry:
                new_entry["day_complete"] = csv_entry["_completed"]
            # Auto-classify day_type based on training data
            new_entry["day_type"] = classify_day_type(date_str, training_data)
            new_entry["notes"] = ""
            existing_by_date[date_str] = new_entry
 
        # Meal detail lives in a separate file (nutrition_meals.json) to keep
        # nutrition.json lean and fully readable. Strip any embedded meals left
        # over from older sync versions so the daily file stays compact.
        existing_by_date[date_str].pop("meals", None)
 
        # Compute compliance flags (only when day_type is set)
        compliance = compute_compliance(existing_by_date[date_str])
        if compliance.get("flags"):
            existing_by_date[date_str]["compliance_flags"] = compliance["flags"]
        elif "compliance_flags" in existing_by_date[date_str]:
            del existing_by_date[date_str]["compliance_flags"]  # Clear stale flags
 
    # Strip any embedded meals from every entry (including untouched older dates
    # carried over from previous sync versions) — meals live in nutrition_meals.json.
    for entry in existing_by_date.values():
        entry.pop("meals", None)

    # Return sorted by date
    return sorted(existing_by_date.values(), key=lambda e: e["date"])
 
 
def load_existing_nutrition(output_path: Path) -> dict:
    """Load existing nutrition.json; return its structure."""
    if output_path.exists():
        with open(output_path) as f:
            return json.load(f)
    # Default structure
    return {
        "_schema": {
            "version": "1.1",
            "description": "Daily nutrition log for MK — Cronometer-aligned, generated by sync_cronometer.py",
            "source": "Cronometer CSV export",
            "coach_protocol": "SECTION_12.md",
        },
        "daily": [],
        "weekly_targets": {
            "_note": "Claude computes 7-day rolling averages from daily entries.",
            "avg_protein_g": 185,
            "avg_kcal_range": "2400-2700",
            "weight_loss_rate_kg_per_week": "0.3-0.5",
        },
    }


def load_existing_meals(meals_path: Path) -> dict:
    """Load existing nutrition_meals.json; return its meals_by_date mapping."""
    if meals_path.exists():
        try:
            with open(meals_path, encoding="utf-8") as f:
                return json.load(f).get("meals_by_date", {})
        except (json.JSONDecodeError, OSError) as e:
            print(f"  [warn] Could not read {meals_path.name}, starting fresh: {e}")
    return {}


def atomic_write_json(path: Path, obj) -> None:
    """
    Write `obj` as indented JSON to `path` atomically.

    Writes to a temp file in the same directory, flushes + fsyncs it, then
    os.replace()s it onto the target. A concurrent reader therefore always sees
    either the complete previous file or the complete new one — never a
    partially written or zero-padded intermediate state. UTF-8 is pinned so the
    byte output is identical regardless of the platform's default encoding.
    """
    fd, tmp_name = tempfile.mkstemp(
        dir=str(path.parent), prefix=path.name + ".", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
 
 
def main():
    parser = argparse.ArgumentParser(description="Sync Cronometer CSVs → nutrition.json")
    parser.add_argument(
        "--data-dir",
        default=".",
        help="Root data directory (default: current directory). "
             "Cronometer CSVs must be in <data-dir>/cronometer/",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without modifying any files",
    )
    parser.add_argument(
        "--no-meals",
        action="store_true",
        help="Skip meal-level detail from servings.csv (smaller output)",
    )
    args = parser.parse_args()
 
    data_dir = Path(args.data_dir).resolve()
    input_dir = data_dir / "cronometer"
    output_path = data_dir / "nutrition.json"
    meals_path = data_dir / "nutrition_meals.json"
 
    print(f"\nsync_cronometer.py v{SCRIPT_VERSION} (hash: {SCRIPT_HASH})")
    print(f"  Data dir   : {data_dir}")
    print(f"  Input dir  : {input_dir}")
    print(f"  Output     : {output_path}")
    print(f"  Dry run    : {args.dry_run}")
    print()
 
    if not input_dir.exists():
        print(f"[error] Input directory not found: {input_dir}")
        print(f"  Create it and place your Cronometer CSV exports inside:")
        print(f"  {input_dir}/dailysummary_YYYYMMDD.csv")
        print(f"  {input_dir}/servings_YYYYMMDD.csv")
        sys.exit(1)
 
    # Read CSV inputs
    print("Reading Cronometer exports...")
    daily_data = read_daily_summaries(input_dir)
    meals_data = {} if args.no_meals else read_servings(input_dir)
 
    if not daily_data:
        print("[error] No daily summary data found. Nothing to sync.")
        sys.exit(1)
 
    # Load existing nutrition.json
    print(f"\nLoading existing {output_path.name}...")
    existing = load_existing_nutrition(output_path)
    existing_count = len(existing.get("daily", []))
    print(f"  Found {existing_count} existing entries")

    # Assemble meal detail for the side file (nutrition_meals.json).
    # Precedence: previously-written meals file < meals embedded in old
    # nutrition.json (migrated) < fresh meals from this run's CSV.
    meals_by_date = load_existing_meals(meals_path)
    for entry in existing.get("daily", []):
        if entry.get("meals") and entry.get("date"):
            meals_by_date.setdefault(entry["date"], entry["meals"])
    meals_by_date.update(meals_data)  # CSV wins for any date it covers
 
    # Load training data for auto-classification
    print("Loading training data for day-type classification...")
    training_data = load_training_data(data_dir)
 
    # Merge
    print("\nMerging data...")
    merged_daily = merge_into_existing(
        existing.get("daily", []),
        daily_data,
        meals_data,
        training_data,
    )
 
    added = len(merged_daily) - existing_count
    print(f"  Result: {len(merged_daily)} entries ({added:+d} new)")
 
    # Build output
    output = existing.copy()
    output["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    output["sync_version"] = SCRIPT_VERSION
    output["script_hash"] = SCRIPT_HASH
    output["data_range"] = {
        "earliest": merged_daily[0]["date"] if merged_daily else None,
        "latest": merged_daily[-1]["date"] if merged_daily else None,
        "total_days": len(merged_daily),
        "complete_days": sum(1 for e in merged_daily if e.get("day_complete") is True),
        "incomplete_days": sum(1 for e in merged_daily if e.get("day_complete") is False),
        "unlogged_days": sum(1 for e in merged_daily if e.get("day_complete") is None),
    }
    output["daily"] = merged_daily
 
    # Days missing day_type (need manual annotation)
    needs_day_type = [e["date"] for e in merged_daily if not e.get("day_type")]
    if needs_day_type:
        output["_needs_day_type"] = needs_day_type
        print(f"\n[action required] {len(needs_day_type)} day(s) need 'day_type' set manually:")
        for d in needs_day_type[:10]:
            print(f"  {d}")
        if len(needs_day_type) > 10:
            print(f"  ... and {len(needs_day_type) - 10} more")
        print(f"  Options: rest | z2_easy | z4_quality | long_z2 | back_to_back_day1 | back_to_back_day2 | deload | travel | sick")
        print(f"  Or ask Claude: 'Set day types in nutrition.json using my training calendar'")
 
    # Build the separate meals file (sorted by date for stable diffs)
    meals_output = {
        "_schema": {
            "version": "1.0",
            "description": "Per-food meal detail for MK, split out of nutrition.json "
                           "to keep that file compact and readable. Keyed by date.",
            "source": "Cronometer servings CSV export",
            "note": "nutrition.json holds daily macro totals; this file holds the "
                    "food-level breakdown. Look up a date here when you need meal detail.",
        },
        "generated_at": output["generated_at"],
        "sync_version": SCRIPT_VERSION,
        "meals_by_date": {d: meals_by_date[d] for d in sorted(meals_by_date)},
    }

    if args.dry_run:
        print("\n[dry-run] Would write:")
        print(json.dumps(output, indent=2)[:2000])
        print("  ... (truncated)")
        print(f"\n[dry-run] Would also write {meals_path.name} "
              f"({len(meals_output['meals_by_date'])} day(s) of meal detail)")
    else:
        atomic_write_json(output_path, output)
        print(f"\nSuccess: Written to {output_path}")
        atomic_write_json(meals_path, meals_output)
        print(f"Success: Written meal detail to {meals_path}")
 
    print("\nDone.")
 
 
if __name__ == "__main__":
    main()