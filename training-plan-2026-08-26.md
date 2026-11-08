# Training Plan — August 26–30, 2026 (Return week: rebuild the anchor, not just the volume)

```json
{
  "plan_version": "1.0",
  "phase": "Base -> Build (re-entry)",
  "phase_week": 1,
  "theme": "Four days back from a nine-day layoff, and the athlete asked to hit it hard. The constraint is not fatigue - TSB is +14 on arrival and ACWR never crosses 1.23 all week. The constraint is that Sunday is locked rest and 48h spacing between hard sessions leaves exactly two quality slots. So both of them have to earn their place: Thursday's 4x8 at 195W is the threshold stimulus this block has had none of AND the FTP answer without spending a day on a test; Saturday's long ride finally gets an HR FLOOR, because the last three long rides were ridden as Z1.",
  "readiness_at_generation": "Projected from latest.json synced 2026-08-16 15:52 plus planned Aug 17 session. Aug 26 arrival: CTL 27.8 / ATL 13.6 / TSB +14.3, ACWR 0.00 (layoff artifact). Last observed readiness P3 green - 6 green, 0 amber. Re-check readiness_decision on the morning of Aug 26 after sync.",
  "load_target_TSS_cycling": "~312",
  "volume_hours_cycling": "~7.0",
  "quality_sessions": 2,
  "long_rides": 1,
  "session_templates": ["AE-7", "TH-2", "AE-1", "AE-6"],
  "progression_vector": "intensity_anchor_correction (tempo @170W -> threshold @195W)",
  "load_variance": false,
  "FTP": 211,
  "LTHR": 154,
  "intensity_basis": "Indoor = power (FTP 211 W, set 2026-06-03, per latest.json synced 2026-08-16 15:52). Outdoor = HR only (no power meter on the Condor)."
}
```

**Generated:** 2026-08-16 · FTP **211 W** (set Jun 3 — **84 days stale** by Aug 26) · eFTP 195 · LTHR 154 · Max HR 170 · Weight **84.2 kg** (Aug 16) · data synced **2026-08-16 15:52**

⚠️ **Sync before Wednesday.** These are projections. Run `sync.py` on Aug 26 morning and re-check `readiness_decision` before the first session. `history.json` was last generated 2026-07-30 and is 17 days stale — worth regenerating too.

---

## Goals audit

| Goal | Target | Now (proj. Aug 30) | Rate | Status |
|---|---|---|---|---|
| **Weight** → 80 kg | −0.3 to −0.5 kg/wk | 84.2 kg (Aug 16), 4.2 kg to go | **−1.05 kg/wk** since Jul 30 | 🔴 **losing more than twice the target rate** |
| **CTL** → 40–45 by mid-Sept | 40 by ~Sept 15 | 31.7 | +3.9 this week | 🔴 needs ~375 TSS/wk sustained — realistic landing is **35–37** |
| **FTP** → 230 W | 230 by end 2026 | 211 nominal / 195 eFTP | 0% in 84 days | 🟡 unanchored — Thursday resolves it |
| **Long ride** (MDS durability) | 3 h+ sustained Z2 | 3 h 02 (Aug 16) — but **94.8% in Z1** | duration ✅, intensity ❌ | 🟡 duration is there, the ride is not |
| **Back-to-back days** | consecutive training days | 4 straight (Wed–Sat) | vs 3 pre-holiday | 🟢 |

**Two of these need saying plainly.**

**Weight is falling too fast.** Jul 30 → Aug 16: 86.7 → 84.2 kg, −1.05 kg/wk against a −0.3 to −0.5 target. That is fat *and* lean mass, and it is the most likely reason your 1200s and 3600s power anchors are drifting down while volume looks fine on paper. The holiday will interrupt it either way. When you're back, the deficit needs to shrink, not the training.

**The mid-Sept CTL target is not reachable.** CTL 40 requires 280 TSS/week *sustained at equilibrium*; from 31.7 on Aug 30, even holding 312 TSS/wk lands you at ~35.4 by Sept 13. That is not a failure — it is the arithmetic of a nine-day break. Worth re-anchoring the DOSSIER to **36–38 by mid-Sept** rather than chasing a number that would need your biggest-ever week, twice, on the back of a layoff.

---

## The week

| Day | Session | Target | Modality | Duration | Est. TSS |
|---|---|---|---|---|---|
| **Wed Aug 26** | **AE-7 progressive endurance** — return day, deliberately not hard | 135 → 145 → 2×10 @ 155 W · HR 117–127 | 🏠 Zwift | 92 min | ~62 |
| **Thu Aug 27** | **TH-2 Seiler 4×8 @ 195 W** ⚡ the week's centrepiece | 195 W · HR 145–154 · RPE 6–8 | 🏠 Zwift | 78 min | ~85 |
| **Fri Aug 28** | **AE-1 easy Z2** — converted rest day, one-week exception | 135 W · RPE 3–4 | 🏠 Zwift | 60 min | ~40 |
| **Sat Aug 29** | **AE-6 fast-finish long ride** — priority session | **HR floor 118**, ceiling 131 · fast finish 132–140 | 🚲 Outdoor | **3 h** | ~125 |
| **Sun Aug 30** | **REST — locked** | — | Rest | — | 0 |
| **Total** | 4 rides | | **~7.0 h** | **~312 TSS** |

### Projected load

| Date | TSS | CTL | ATL | TSB | ACWR |
|---|---|---|---|---|---|
| Aug 25 (arrival) | 0 | 27.8 | 13.6 | **+14.3** | 0.00 |
| Aug 26 | 62 | 28.6 | 20.5 | +8.2 | 0.26 |
| Aug 27 | 85 | 30.0 | 29.7 | +0.3 | 0.62 |
| Aug 28 | 40 | 30.2 | 31.2 | −0.9 | 0.76 |
| Aug 29 | 125 | 32.5 | 44.6 | −12.1 | 1.18 |
| **Aug 30** | 0 | **31.7** | 38.2 | −6.5 | **1.23** |

**ACWR never leaves the safe band.** It peaks at 1.23 on Sunday — below the 1.3 gate. You have more headroom than the week uses; the limiter is 48h hard-session spacing and a locked Sunday, not load tolerance. CTL lands at 31.7 against 32.4 pre-holiday: **the week pays back the layoff exactly, and no more.** That is what a return week should do.

---

## ⚡ Thursday is the session, and it answers the FTP question for free

You didn't want to spend a day on a formal test. Fine — 4×8 min *is* the 2×8-min test protocol doubled, so this session pays twice.

The case for 195 W over the 170 W you've been riding: on Aug 11 you held 168 W for four 12-min reps at RPE 5, HR topping out at 133. Work-portion IF was 0.80, and the protocol's RPE band for IF 0.75–0.85 is **4–6**. RPE 5 was exactly on script. That session wasn't a failure — it was *tempo*, correctly executed, wearing a sweet-spot label. **195 W is 92% of FTP 211 and 100% of eFTP 195.** It is the first genuinely threshold-anchored session of this block.

| Outcome | What it means | What happens next |
|---|---|---|
| All four within 5% of 195 W, HR settles **145–154**, RPE 6–8 | FTP 211 stands | Ladder to 4×10 next week; autumn block builds off 211 |
| Rep 3 or 4 sags below 185 W, **or** HR pins at 154+ from rep 2 | Threshold sits nearer eFTP | Working FTP drops to **~198**; every autumn target rebuilds off that |
| RPE ≤ 5 across all four | 195 W is *still* too soft | We go up again — say so if it happens |

ERG is on. If rep 2 has you at RPE 9 with HR pinned, step down to 185 W with the +/− keys for reps 3–4. **A controlled step down is a clean result. Grinding a fading rep in ERG is not.** Can't hold 185 W on rep 3 → stop the set. That protects Saturday.

---

## 🚲 Saturday finally gets a floor

Your last three long rides have a pattern. Aug 16: 3 h 02, avg HR **110** against a ceiling of 131 — **2 h 52 of it in Z1**, nine minutes in Z2, in 21.9 °C with no wind. Aug 8: same duration, avg HR 125, **139 TSS vs 93**. Same ride, 33% cheaper eight days later.

Ceilings alone haven't worked. So this one has a **floor**:

- **HR floor 118, ceiling 131.** If your 30-minute average is under 118, lift the pace. That is the instruction.
- **Fast finish:** in the last 45 minutes, **2 × 10 min at HR 132–140**, 5 min easy between. This is what makes it an AE-6 and it is the point of the session — sub-threshold work on depleted legs is the single most MDS-relevant thing you can do on a bike.
- Duration floor 2 h 30, hard stop 3 h 30.

No power meter on the Condor, so HR is the whole instrument. If the weather turns, say so and I'll build the indoor AE-3 fallback.

---

## One risk, said once

Two hard days in your first four back is aggressive, and Thursday is day 2. The numbers support it — TSB +14 on arrival, ACWR peaking at 1.23, readiness green at last read — and a nine-day break costs conditioning, not tolerance. But **check `readiness_decision` on Wednesday morning after sync.** If it comes back `modify` or `skip`, Thursday moves to Friday and Saturday drops the fast finish. That's the only contingency; otherwise run it as written.

---

## Schedule note

**Friday Aug 28 is a one-week exception**, converted from your standing rest day because you'll be three days back from a layoff. **Sunday Aug 30 stays locked as rest.** The standing Friday-rest / Sunday-rest pattern resumes from Sept 1 — I have not amended the DOSSIER, and won't unless you tell me to make it permanent.

---

## Reference zones (FTP 211 W · LTHR 154 · Max HR 170)

| Zone | Power | HR | Used this week |
|---|---|---|---|
| Z1 recovery | 100–116 W | < 111 | recoveries, cooldowns |
| Z2 endurance | 118–158 W | 111–131 | Wed, Fri, Sat main |
| Z3 tempo | 159–190 W | 132–142 | Sat fast finish |
| Z4 threshold | 191–222 W | 143–154 | **Thu 4×8 @ 195 W** |
| Z5 VO₂max | 223–253 W | 155+ | — |
