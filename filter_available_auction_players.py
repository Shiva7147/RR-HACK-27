import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))

# 1. Identify IPL 2026 competition ID
ipl_2026_comp_id = comp[comp['comp_name'] == 'IPL 2026']['comp_id'].iloc[0]
print("IPL 2026 comp_id:", ipl_2026_comp_id)

# 2. All players who were in an IPL 2026 squad (actively playing / retained / signed in the latest season)
ipl_2026_players = set(mapping[mapping['comp_id'] == ipl_2026_comp_id]['player_name'].unique())
print(f"Total players in IPL 2026 squads: {len(ipl_2026_players)}")

# 3. All players who played in ANY IPL season (2022-2026)
ipl_comps = comp[comp['comp_name'].str.contains('IPL')]['comp_id'].unique()
all_ipl_played_ids = set(p11[(p11['match_id'].isin(matches[matches['comp_id'].isin(ipl_comps)]['match_id'])) & (p11['is_played'] == 1)]['player_id'].unique())
all_ipl_played_names = set(mapping[mapping['player_id'].isin(all_ipl_played_ids)]['player_name'].unique())

# Also Pakistani players are ineligible
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())

# Let's inspect who is NOT in IPL 2026 (i.e. completely free agent / open to be bought / uncapped domestic / emerging):
batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Category A: Pure Uncapped / Never Played IPL
bat_never_ipl = batters[(~batters['striker_name'].isin(all_ipl_played_names)) & (~batters['striker_name'].isin(pak_players))].copy()
bowl_never_ipl = bowlers[(~bowlers['bowler_name'].isin(all_ipl_played_names)) & (~bowlers['bowler_name'].isin(pak_players))].copy()

# Category B: Not in IPL 2026 (either never played IPL, or not selected in the latest IPL season)
bat_not_in_2026 = batters[(~batters['striker_name'].isin(ipl_2026_players)) & (~batters['striker_name'].isin(pak_players))].copy()
bowl_not_in_2026 = bowlers[(~bowlers['bowler_name'].isin(ipl_2026_players)) & (~bowlers['bowler_name'].isin(pak_players))].copy()

print(f"Batters who never played IPL: {len(bat_never_ipl)}")
print(f"Bowlers who never played IPL: {len(bowl_never_ipl)}")
print(f"Batters not in IPL 2026 squads: {len(bat_not_in_2026)}")
print(f"Bowlers not in IPL 2026 squads: {len(bowl_not_in_2026)}")

# Let's see what teams these non-IPL 2026 players belong to
player_team_map = mapping.groupby('player_name')['team_name'].apply(lambda x: ', '.join(x.unique())).to_dict()
bat_never_ipl['teams'] = bat_never_ipl['striker_name'].map(player_team_map)
bowl_never_ipl['teams'] = bowl_never_ipl['bowler_name'].map(player_team_map)

# Let's inspect top performers who have NEVER played an IPL match
print("\n=== TOP 20 BATTERS WHO NEVER PLAYED IPL (MIN 25 PRESSURE BALLS) ===")
cols_b = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(bat_never_ipl[bat_never_ipl['press_balls'] >= 25].sort_values('rci_bat_regularized', ascending=False)[cols_b].head(20).to_string(index=False))

print("\n=== TOP 20 BOWLERS WHO NEVER PLAYED IPL (MIN 25 PRESSURE BALLS) ===")
cols_bw = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(bowl_never_ipl[bowl_never_ipl['press_balls'] >= 25].sort_values('rci_bowl_regularized', ascending=False)[cols_bw].head(20).to_string(index=False))
