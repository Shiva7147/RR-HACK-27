import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))

# All IPL matches ever
ipl_comps = comp[comp['comp_name'].str.contains('IPL')]['comp_id'].unique()
ipl_matches = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].unique()

# Players who played in an IPL match
played_ipl_ids = set(p11[(p11['match_id'].isin(ipl_matches)) & (p11['is_played'] == 1)]['player_id'].unique())

# Also players in IPL 2026 squads
ipl_2026_comp = comp[comp['comp_name'] == 'IPL 2026']['comp_id'].iloc[0]
ipl_2026_squad_names = set(mapping[mapping['comp_id'] == ipl_2026_comp]['player_name'].unique())

# Also players currently in Rajasthan Royals
rr_players = set(mapping[mapping['team_name'] == 'Rajasthan Royals']['player_name'].unique())

print(f"Total players who ever played in IPL XI: {len(played_ipl_ids)}")
print(f"Total players in IPL 2026 squad: {len(ipl_2026_squad_names)}")
print(f"Total players in RR ever: {len(rr_players)}")

# Batters metrics
batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Pakistani players
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())

# PURE UNCAPPED & AVAILABLE PLAYERS:
# 1. NOT played in IPL (played_ipl_ids)
# 2. NOT in IPL 2026 squad
# 3. NOT in RR (already played for RR)
# 4. NOT Pakistani

pure_bat = batters[(~batters['striker_id'].isin(played_ipl_ids)) & 
                   (~batters['striker_name'].isin(ipl_2026_squad_names)) & 
                   (~batters['striker_name'].isin(rr_players)) & 
                   (~batters['striker_name'].isin(pak_players))].copy()

pure_bowl = bowlers[(~bowlers['bowler_id'].isin(played_ipl_ids)) & 
                    (~bowlers['bowler_name'].isin(ipl_2026_squad_names)) & 
                    (~bowlers['bowler_name'].isin(rr_players)) & 
                    (~bowlers['bowler_name'].isin(pak_players))].copy()

player_team_map = mapping.groupby('player_name')['team_name'].apply(lambda x: ', '.join(x.unique())).to_dict()
pure_bat['teams'] = pure_bat['striker_name'].map(player_team_map)
pure_bowl['teams'] = pure_bowl['bowler_name'].map(player_team_map)

print("\n--- Top Pure Uncapped Batters (0 IPL Games Ever, Not in RR, Not in IPL 2026) ---")
cols_b = ['striker_name', 'teams', 'total_balls', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(pure_bat[pure_bat['press_balls'] >= 25].sort_values('rci_bat_regularized', ascending=False)[cols_b].head(15).to_string(index=False))

print("\n--- Top Pure Uncapped Bowlers (0 IPL Games Ever, Not in RR, Not in IPL 2026) ---")
cols_bw = ['bowler_name', 'teams', 'total_balls', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(pure_bowl[pure_bowl['press_balls'] >= 25].sort_values('rci_bowl_regularized', ascending=False)[cols_bw].head(15).to_string(index=False))
