import json
from datetime import datetime

with open("c:/Zwift Coach/performance-coach/history.json", "r") as f:
    history = json.load(f)

with open("c:/Zwift Coach/performance-coach/latest.json", "r") as f:
    latest = json.load(f)

# Let's count totals from weekly_180d since Jan 1, 2026
weekly = history.get("weekly_180d", [])
weeks_2026 = [w for w in weekly if w.get("week_start") >= "2026-01-01"]

total_hours = sum(w.get("total_hours", 0) for w in weeks_2026)
total_tss = sum(w.get("total_tss", 0) for w in weeks_2026)
total_activities = sum(w.get("activity_count", 0) for w in weeks_2026)

print(f"Stats since Jan 1, 2026 (based on weekly summaries):")
print(f"Total Weeks: {len(weeks_2026)}")
print(f"Total Hours: {total_hours:.1f} hours")
print(f"Total TSS: {total_tss:.0f}")
print(f"Total Activities: {total_activities}")

# CTL progression
ctl_values = [w.get("ctl_end") for w in weeks_2026 if w.get("ctl_end") is not None]
if ctl_values:
    print(f"CTL: Start of year {ctl_values[0]:.1f} -> Current {ctl_values[-1]:.1f} (Peak: {max(ctl_values):.1f})")

# RHR and HRV trends
rhr_values = [w.get("avg_rhr") for w in weeks_2026 if w.get("avg_rhr") is not None]
hrv_values = [w.get("avg_hrv") for w in weeks_2026 if w.get("avg_hrv") is not None]

if rhr_values:
    print(f"RHR: Start of year {rhr_values[0]:.1f} bpm -> Current {rhr_values[-1]:.1f} bpm (Lowest: {min(rhr_values):.1f} bpm)")
if hrv_values:
    print(f"HRV: Start of year (first recorded) {hrv_values[0]:.1f} ms -> Current {hrv_values[-1]:.1f} ms (Peak: {max(hrv_values):.1f} ms)")

# Let's count actual activities from intervals.json or recent_activities if needed.
# Let's check latest.json summary for current stats
curr_ctl = latest.get("current_status", {}).get("fitness", {}).get("ctl")
curr_atl = latest.get("current_status", {}).get("fitness", {}).get("atl")
curr_tsb = latest.get("current_status", {}).get("fitness", {}).get("tsb")
print(f"\nIntervals.icu Current Fitness (CTL/ATL/TSB): {curr_ctl:.1f} / {curr_atl:.1f} / {curr_tsb:.1f}")
