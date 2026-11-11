import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))

batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Find all players who have EVER played in an IPL match or been in an IPL squad
ipl_comps = comp[comp['comp_name'].str.contains('IPL')]['comp_id'].unique()
ipl_matches = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].unique()

ever_ipl_played_ids = set(p11[(p11['match_id'].isin(ipl_matches)) & (p11['is_played'] == 1)]['player_id'].unique())
ever_ipl_squad_ids = set(mapping[mapping['comp_id'].isin(ipl_comps)]['player_id'].unique())
ever_ipl_squad_names = set(mapping[mapping['comp_id'].isin(ipl_comps)]['player_name'].unique())

# Also Pakistani players (ineligible)
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())

# Strictly PURE UNCAPPED / NEVER PLAYED IPL / NEVER IN IPL SQUAD
pure_uncapped_batters = batters[(~batters['striker_name'].isin(ever_ipl_squad_names)) & 
                                (~batters['striker_name'].isin(pak_players))].copy()

pure_uncapped_bowlers = bowlers[(~bowlers['bowler_name'].isin(ever_ipl_squad_names)) & 
                                (~bowlers['bowler_name'].isin(pak_players))].copy()

player_teams = mapping.groupby('player_name')['team_name'].apply(lambda x: ', '.join(x.unique())).to_dict()
pure_uncapped_batters['teams'] = pure_uncapped_batters['striker_name'].map(player_teams)
pure_uncapped_bowlers['teams'] = pure_uncapped_bowlers['bowler_name'].map(player_teams)

print("=== PURE UNCAPPED BATTERS (0 IPL SQUADS EVER) SORTED BY RCI ===")
cols_b = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(pure_uncapped_batters[pure_uncapped_batters['press_balls'] >= 30].sort_values('rci_bat_regularized', ascending=False)[cols_b].head(15).to_string(index=False))

print("\n=== PURE UNCAPPED BOWLERS (0 IPL SQUADS EVER) SORTED BY RCI ===")
cols_bw = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(pure_uncapped_bowlers[pure_uncapped_bowlers['press_balls'] >= 30].sort_values('rci_bowl_regularized', ascending=False)[cols_bw].head(15).to_string(index=False))
