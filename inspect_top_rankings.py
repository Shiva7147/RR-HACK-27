import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'
batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))

# Exclude Pakistani players as they are ineligible for IPL auction
pak_players = mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique()

batters_el = batters[~batters['striker_name'].isin(pak_players)].copy()
bowlers_el = bowlers[~bowlers['bowler_name'].isin(pak_players)].copy()

# Filter min pressure balls for robust reliability
# Threshold: at least 70 pressure balls (about 12 overs of clutch exposure)
top10_bat_overall = batters_el[batters_el['press_balls'] >= 70].sort_values('rci_bat_regularized', ascending=False).head(15)
top10_bowl_overall = bowlers_el[bowlers_el['press_balls'] >= 70].sort_values('rci_bowl_regularized', ascending=False).head(15)

print("=== OVERALL TOP 15 BATTERS UNDER PRESSURE (MIN 70 PRESSURE BALLS) ===")
cols_bat = ['striker_name', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(top10_bat_overall[cols_bat].to_string(index=False))

print("\n=== OVERALL TOP 15 BOWLERS UNDER PRESSURE (MIN 70 PRESSURE BALLS) ===")
cols_bowl = ['bowler_name', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(top10_bowl_overall[cols_bowl].to_string(index=False))

# Now let's inspect the DOMESTIC & EMERGING talent pool:
# Players in India A, Sri Lanka A, Afghanistan A, Bangladesh A, UAE, Oman, Hong Kong OR uncapped domestic
emerging_comps = [2670, 3289]
emerging_players = mapping[mapping['comp_id'].isin(emerging_comps)]['player_name'].unique()

# Let's inspect domestic emerging with min 50 pressure balls
top15_dom_bat = batters_el[(batters_el['press_balls'] >= 50) & 
                          (batters_el['striker_name'].isin(emerging_players) | 
                           batters_el['striker_name'].isin(mapping[mapping['team_name'] == 'India A']['player_name']))].sort_values('rci_bat_regularized', ascending=False).head(15)

top15_dom_bowl = bowlers_el[(bowlers_el['press_balls'] >= 50) & 
                            (bowlers_el['bowler_name'].isin(emerging_players) | 
                             bowlers_el['bowler_name'].isin(mapping[mapping['team_name'] == 'India A']['player_name']))].sort_values('rci_bowl_regularized', ascending=False).head(15)

print("\n=== TOP 15 DOMESTIC / EMERGING BATTERS UNDER PRESSURE (MIN 50 PRESSURE BALLS) ===")
print(top15_dom_bat[cols_bat].to_string(index=False))

print("\n=== TOP 15 DOMESTIC / EMERGING BOWLERS UNDER PRESSURE (MIN 50 PRESSURE BALLS) ===")
print(top15_dom_bowl[cols_bowl].to_string(index=False))
