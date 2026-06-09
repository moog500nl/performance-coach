import json
from datetime import datetime

with open("c:/Zwift Coach/performance-coach/history.json", "r") as f:
    history = json.load(f)

with open("c:/Zwift Coach/performance-coach/latest.json", "r") as f:
    latest = json.load(f)

daily = history.get("daily_90d", [])
print(f"Daily logs length: {len(daily)}")

# Print days where weight, HRV, or RHR is not None
print(f"{'Date':<10} | {'Weight (kg)':<11} | {'HRV (ms)':<8} | {'RHR (bpm)':<8} | {'Sleep (h)':<9} | {'TSS':<5} | {'Feel':<4} | {'RPE':<4}")
print("-" * 80)
for day in daily:
    date = day.get("date")
    weight = day.get("weight_kg")
    hrv = day.get("hrv")
    rhr = day.get("rhr")
    sleep = day.get("sleep_hours")
    tss = day.get("total_tss", 0)
    feel = day.get("fatigue") # wait, is feel fatigue? Yes, 1-4 scale
    rpe = day.get("soreness")
    
    if weight is not None or hrv is not None or rhr is not None or sleep is not None:
        weight_str = f"{weight:.1f}" if weight is not None else "-"
        hrv_str = f"{hrv:.1f}" if hrv is not None else "-"
        rhr_str = f"{rhr:.1f}" if rhr is not None else "-"
        sleep_str = f"{sleep:.1f}" if sleep is not None else "-"
        feel_str = str(feel) if feel is not None else "-"
        rpe_str = str(rpe) if rpe is not None else "-"
        print(f"{date:<10} | {weight_str:<11} | {hrv_str:<8} | {rhr_str:<8} | {sleep_str:<9} | {tss:<5} | {feel_str:<4} | {rpe_str:<4}")

print("\nLatest data state:")
curr = latest.get("current_status", {}).get("current_metrics", {})
print(f"Weight: {curr.get('weight_kg')} kg")
print(f"HRV: {curr.get('hrv')} ms")
print(f"RHR: {curr.get('resting_hr')} bpm")
print(f"Sleep hours: {curr.get('sleep_hours')} h")
print(f"Feel (fatigue): {curr.get('fatigue')}")
print(f"Soreness: {curr.get('soreness')}")
print(f"Stress: {curr.get('stress')}")
print(f"Mood: {curr.get('mood')}")
print(f"Motivation: {curr.get('motivation')}")
