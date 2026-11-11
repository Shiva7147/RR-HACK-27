import pandas as pd
import numpy as np

# Load our processed data
from pressure_engine import bbb

# Min ball thresholds
MIN_PRESSURE_BALLS_BAT = 120 # at least 20 overs faced in high pressure
MIN_PRESSURE_BALLS_BOWL = 120 # at least 20 overs bowled in high pressure

# Batting Stats
bat_overall = bbb.groupby(['striker_id', 'striker_name']).agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    dots=('runs', lambda x: (x == 0).sum()),
    boundaries=('runs', lambda x: (x.isin([4, 6])).sum()),
    dismissals=('is_wicket', 'sum')
).reset_index()
bat_overall['sr_base'] = (bat_overall['runs'] / bat_overall['balls']) * 100
bat_overall['dot_pct_base'] = (bat_overall['dots'] / bat_overall['balls']) * 100

bat_press = bbb[bbb['is_high_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries=('runs', lambda x: (x.isin([4, 6])).sum()),
    press_dismissals=('is_wicket', 'sum')
).reset_index()
bat_press['sr_press'] = (bat_press['press_runs'] / bat_press['press_balls']) * 100
bat_press['boundary_pct_press'] = (bat_press['press_boundaries'] / bat_press['press_balls']) * 100
bat_press['dot_pct_press'] = (bat_press['press_dots'] / bat_press['press_balls']) * 100
bat_press['balls_per_dismissal_press'] = bat_press['press_balls'] / bat_press['press_dismissals'].replace(0, np.nan)

batters = bat_overall.merge(bat_press, on=['striker_id', 'striker_name'])
batters = batters[batters['press_balls'] >= MIN_PRESSURE_BALLS_BAT].copy()
batters['sr_delta'] = batters['sr_press'] - batters['sr_base']

# Clutch Batting Score = SR_press * (1 - dot_pct_press/100) * (boundary_pct_press/100) + Bayesian SR delta boost
# Or weighted combination of Strike Rate in Pressure, Dot Ball Minimization, and Boundary Frequency
batters['clutch_bat_score'] = (
    0.40 * (batters['sr_press'] / 150.0 * 100) + 
    0.30 * (batters['boundary_pct_press'] / 20.0 * 100) + 
    0.20 * ((50 - batters['dot_pct_press']) / 20.0 * 100) + 
    0.10 * (np.clip(batters['sr_delta'], -20, 40) / 20.0 * 100)
)
top_batters = batters.sort_values('clutch_bat_score', ascending=False)

print("=== TOP 20 BATTERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bat = ['striker_name', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'boundary_pct_press', 'dot_pct_press', 'clutch_bat_score']
print(top_batters[cols_bat].head(20).to_string(index=False))

# Bowling Stats
bowl_overall = bbb.groupby(['bowler_id', 'bowler_name']).agg(
    balls=('runs', 'count'),
    runs_conceded=('runs', 'sum'),
    dots=('runs', lambda x: (x == 0).sum()),
    boundaries_conceded=('runs', lambda x: (x.isin([4, 6])).sum()),
    wickets=('is_wicket', 'sum')
).reset_index()
bowl_overall['econ_base'] = (bowl_overall['runs_conceded'] / (bowl_overall['balls'] / 6))
bowl_overall['dot_pct_base'] = (bowl_overall['dots'] / bowl_overall['balls']) * 100

bowl_press = bbb[bbb['is_high_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries_conceded=('runs', lambda x: (x.isin([4, 6])).sum()),
    press_wickets=('is_wicket', 'sum')
).reset_index()
bowl_press['econ_press'] = (bowl_press['press_runs'] / (bowl_press['press_balls'] / 6))
bowl_press['dot_pct_press'] = (bowl_press['press_dots'] / bowl_press['press_balls']) * 100
bowl_press['balls_per_wicket_press'] = bowl_press['press_balls'] / bowl_press['press_wickets'].replace(0, np.nan)
bowl_press['boundary_pct_conceded_press'] = (bowl_press['press_boundaries_conceded'] / bowl_press['press_balls']) * 100

bowlers = bowl_overall.merge(bowl_press, on=['bowler_id', 'bowler_name'])
bowlers = bowlers[bowlers['press_balls'] >= MIN_PRESSURE_BALLS_BOWL].copy()
bowlers['econ_delta'] = bowlers['econ_base'] - bowlers['econ_press'] # Positive means lower econ under pressure

# Clutch Bowling Score: rewarding low pressure economy, high dot ball %, high wicket frequency
# Clutch Bowler Score = (12.0 - Econ_press)*15 + (Dot_pct_press)*1.2 + (Press_wickets / Press_balls * 600) + Econ_delta*5
bowlers['clutch_bowl_score'] = (
    0.35 * (np.maximum(0, 13.0 - bowlers['econ_press']) / 4.0 * 100) + 
    0.30 * (bowlers['dot_pct_press'] / 40.0 * 100) + 
    0.25 * ((bowlers['press_wickets'] / bowlers['press_balls'] * 6) / 0.5 * 100) + 
    0.10 * (np.clip(bowlers['econ_delta'] + 2, 0, 4) / 4.0 * 100)
)
top_bowlers = bowlers.sort_values('clutch_bowl_score', ascending=False)

print("\n=== TOP 20 BOWLERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bowl = ['bowler_name', 'press_balls', 'press_runs', 'econ_press', 'press_wickets', 'dot_pct_press', 'boundary_pct_conceded_press', 'clutch_bowl_score']
print(top_bowlers[cols_bowl].head(20).to_string(index=False))
