import json
from datetime import datetime

with open("c:/Zwift Coach/performance-coach/history.json", "r") as f:
    data = json.load(f)

weekly = data.get("weekly_180d", [])
print(f"Total weeks: {len(weekly)}")

print(f"{'Week Start':<12} | {'Hours':<5} | {'TSS':<5} | {'CTL':<5} | {'TSB':<5} | {'HRV':<5} | {'RHR':<5} | {'Sleep':<5} | {'Weight':<6} | {'Feel':<4} | {'RPE':<4} | {'Phase':<12}")
print("-" * 92)

for wk in weekly:
    week_start = wk.get("week_start", "")
    hours = wk.get("total_hours", 0)
    tss = wk.get("total_tss", 0)
    ctl = wk.get("ctl_end", 0)
    tsb = wk.get("tsb_end", 0)
    hrv = wk.get("avg_hrv", 0)
    rhr = wk.get("avg_rhr", 0)
    sleep = wk.get("avg_sleep_hours", 0)
    weight = wk.get("weight_kg", 0)
    feel = wk.get("avg_feel", 0)
    rpe = wk.get("avg_rpe", 0)
    phase = wk.get("phase_detected", "")
    
    # Format values
    hours_str = f"{hours:.1f}" if hours is not None else "-"
    tss_str = f"{tss:.0f}" if tss is not None else "-"
    ctl_str = f"{ctl:.1f}" if ctl is not None else "-"
    tsb_str = f"{tsb:.1f}" if tsb is not None else "-"
    hrv_str = f"{hrv:.1f}" if hrv is not None else "-"
    rhr_str = f"{rhr:.1f}" if rhr is not None else "-"
    sleep_str = f"{sleep:.1f}" if sleep is not None else "-"
    weight_str = f"{weight:.1f}" if weight is not None else "-"
    feel_str = f"{feel:.1f}" if feel is not None else "-"
    rpe_str = f"{rpe:.1f}" if rpe is not None else "-"
    phase_str = str(phase) if phase is not None else "-"
    
    print(f"{week_start:<12} | {hours_str:<5} | {tss_str:<5} | {ctl_str:<5} | {tsb_str:<5} | {hrv_str:<5} | {rhr_str:<5} | {sleep_str:<5} | {weight_str:<6} | {feel_str:<4} | {rpe_str:<4} | {phase_str:<12}")
