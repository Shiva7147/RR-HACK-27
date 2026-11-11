import pandas as pd
import numpy as np
import os

from find_pure_uncapped import never_ipl, never_in_ipl_squad, mapping, bbb, comp

data_dir = r'D:\6af3166e7b922_data_pack'
batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Merge mapping details so we know what teams they played for
player_teams = mapping.groupby('player_id').agg(
    teams=('team_name', lambda x: ', '.join(x.unique())),
    comps=('comp_name', lambda x: ', '.join(x.unique()))
).reset_index()

# 1. Non-IPL Batters: never played in IPL match
bat_non_ipl = batters[batters['striker_id'].isin(never_ipl['player_id'])].copy()
bat_non_ipl = bat_non_ipl.merge(player_teams, left_on='striker_id', right_on='player_id', how='left')

# 2. Non-IPL Bowlers: never played in IPL match
bowl_non_ipl = bowlers[bowlers['bowler_id'].isin(never_ipl['player_id'])].copy()
bowl_non_ipl = bowl_non_ipl.merge(player_teams, left_on='bowler_id', right_on='player_id', how='left')

print(f"Total non-IPL batters who faced deliveries: {len(bat_non_ipl)}")
print(f"Total non-IPL bowlers who bowled deliveries: {len(bowl_non_ipl)}")

# Let's inspect the top non-IPL batters with min 30 pressure balls
top_bat_non_ipl = bat_non_ipl[bat_non_ipl['press_balls'] >= 30].sort_values('rci_bat_regularized', ascending=False)
print("\n=== TOP 25 NON-IPL BATTERS UNDER PRESSURE (MIN 30 PRESSURE BALLS) ===")
cols_b = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(top_bat_non_ipl[cols_b].head(25).to_string(index=False))

# Let's inspect the top non-IPL bowlers with min 30 pressure balls
top_bowl_non_ipl = bowl_non_ipl[bowl_non_ipl['press_balls'] >= 30].sort_values('rci_bowl_regularized', ascending=False)
print("\n=== TOP 25 NON-IPL BOWLERS UNDER PRESSURE (MIN 30 PRESSURE BALLS) ===")
cols_bw = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(top_bowl_non_ipl[cols_bw].head(25).to_string(index=False))
