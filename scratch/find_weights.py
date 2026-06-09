import json

with open("c:/Zwift Coach/performance-coach/history.json", "r") as f:
    data = json.load(f)

# Find all entries with weight_kg
all_days = data.get("daily_90d", [])
weight_records = []
for day in all_days:
    if day.get("weight_kg") is not None:
        weight_records.append((day.get("date"), day.get("weight_kg")))

# Also check weekly_180d
weekly_records = []
for wk in data.get("weekly_180d", []):
    if wk.get("weight_kg") is not None:
        weekly_records.append((wk.get("week_start"), wk.get("weight_kg")))

print("Daily weight records (last 90d):")
for r in weight_records:
    print(f"  {r[0]}: {r[1]} kg")

print("\nWeekly weight records (last 180d):")
for r in weekly_records:
    print(f"  {r[0]}: {r[1]} kg")
