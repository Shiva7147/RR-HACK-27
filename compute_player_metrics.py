import pandas as pd
import numpy as np
import os

from process_entire_datapack import bbb, mapping

print("Computing complete player metrics from data pack...")

# --- 1. Batting Metrics ---
bat_base = bbb.groupby(['striker_id', 'striker_name']).agg(
    total_balls=('runs', 'count'),
    total_runs=('runs', 'sum'),
    total_dots=('runs', lambda x: (x == 0).sum()),
    total_boundaries=('runs', lambda x: x.isin([4, 6]).sum()),
    total_fours=('is_four', 'sum'),
    total_sixes=('is_six', 'sum'),
    total_dismissals=('is_wicket', 'sum')
).reset_index()

bat_base['sr_base'] = (bat_base['total_runs'] / bat_base['total_balls']) * 100
bat_base['dot_pct_base'] = (bat_base['total_dots'] / bat_base['total_balls']) * 100
bat_base['bnd_pct_base'] = (bat_base['total_boundaries'] / bat_base['total_balls']) * 100

# High Pressure Batting
bbb_hp = bbb[bbb['is_high_pressure']]
bat_press = bbb_hp.groupby(['striker_id', 'striker_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries=('runs', lambda x: x.isin([4, 6]).sum()),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_dismissals=('is_wicket', 'sum')
).reset_index()

bat_press['sr_press'] = (bat_press['press_runs'] / bat_press['press_balls']) * 100
bat_press['dot_pct_press'] = (bat_press['press_dots'] / bat_press['press_balls']) * 100
bat_press['bnd_pct_press'] = (bat_press['press_boundaries'] / bat_press['press_balls']) * 100
bat_press['balls_per_dismissal_press'] = bat_press['press_balls'] / bat_press['press_dismissals'].replace(0, np.nan)

batters = bat_base.merge(bat_press, on=['striker_id', 'striker_name'], how='left')
batters = batters.fillna({
    'press_balls': 0, 'press_runs': 0, 'press_dots': 0, 'press_boundaries': 0,
    'press_fours': 0, 'press_sixes': 0, 'press_dismissals': 0,
    'sr_press': 0, 'dot_pct_press': 100, 'bnd_pct_press': 0
})

batters['sr_delta'] = batters['sr_press'] - batters['sr_base']

# Empirical Bayes regularized clutch batting index (RCI_Bat)
# League average par strike rate in pressure = 145.0, boundary% = 18.0%, dot% = 35.0%
batters['rci_bat'] = (
    0.35 * (batters['sr_press'] / 145.0 * 100) +
    0.30 * (batters['bnd_pct_press'] / 18.0 * 100) +
    0.20 * ((50.0 - batters['dot_pct_press']) / 20.0 * 100) +
    0.15 * (np.clip(batters['sr_delta'], -25, 40) / 20.0 * 100)
)
# Multiply by sample size reliability factor: sqrt(press_balls / (press_balls + 30))
batters['reliability_factor'] = np.sqrt(batters['press_balls'] / (batters['press_balls'] + 30.0))
batters['rci_bat_regularized'] = batters['rci_bat'] * batters['reliability_factor']

# --- 2. Bowling Metrics ---
bowl_base = bbb.groupby(['bowler_id', 'bowler_name']).agg(
    total_balls=('runs', 'count'),
    total_runs_conceded=('total_ball_runs', 'sum'),
    total_dots=('runs', lambda x: (x == 0).sum()),
    total_boundaries_conceded=('runs', lambda x: x.isin([4, 6]).sum()),
    total_wickets=('is_wicket', 'sum')
).reset_index()

bowl_base['econ_base'] = (bowl_base['total_runs_conceded'] / (bowl_base['total_balls'] / 6))
bowl_base['dot_pct_base'] = (bowl_base['total_dots'] / bowl_base['total_balls']) * 100
bowl_base['bnd_conceded_pct_base'] = (bowl_base['total_boundaries_conceded'] / bowl_base['total_balls']) * 100

# High Pressure Bowling
bowl_press = bbb_hp.groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('runs', 'count'),
    press_runs_conceded=('total_ball_runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries_conceded=('runs', lambda x: x.isin([4, 6]).sum()),
    press_wickets=('is_wicket', 'sum')
).reset_index()

bowl_press['econ_press'] = (bowl_press['press_runs_conceded'] / (bowl_press['press_balls'] / 6))
bowl_press['dot_pct_press'] = (bowl_press['press_dots'] / bowl_press['press_balls']) * 100
bowl_press['bnd_conceded_pct_press'] = (bowl_press['press_boundaries_conceded'] / bowl_press['press_balls']) * 100
bowl_press['balls_per_wkt_press'] = bowl_press['press_balls'] / bowl_press['press_wickets'].replace(0, np.nan)

bowlers = bowl_base.merge(bowl_press, on=['bowler_id', 'bowler_name'], how='left')
bowlers = bowlers.fillna({
    'press_balls': 0, 'press_runs_conceded': 0, 'press_dots': 0, 'press_boundaries_conceded': 0,
    'press_wickets': 0, 'econ_press': 18.0, 'dot_pct_press': 0, 'bnd_conceded_pct_press': 50.0
})

bowlers['econ_delta'] = bowlers['econ_base'] - bowlers['econ_press'] # Positive is better

# Empirical Bayes regularized clutch bowling index (RCI_Bowl)
# League par death/pressure economy = 9.80, dot% = 35.0%, wkt per ball = 0.07 (14.2 balls/wkt)
bowlers['rci_bowl'] = (
    0.35 * (np.maximum(0, 13.5 - bowlers['econ_press']) / 4.0 * 100) +
    0.30 * (bowlers['dot_pct_press'] / 35.0 * 100) +
    0.25 * ((bowlers['press_wickets'] / np.maximum(1, bowlers['press_balls']) * 6) / 0.5 * 100) +
    0.10 * (np.clip(bowlers['econ_delta'] + 2, 0, 4) / 4.0 * 100)
)
bowlers['reliability_factor'] = np.sqrt(bowlers['press_balls'] / (bowlers['press_balls'] + 30.0))
bowlers['rci_bowl_regularized'] = bowlers['rci_bowl'] * bowlers['reliability_factor']

# Save full results
data_dir = r'D:\6af3166e7b922_data_pack'
batters.to_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'), index=False)
bowlers.to_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'), index=False)
print("Saved all_batters_pressure_metrics.csv and all_bowlers_pressure_metrics.csv to data pack folder.")
