import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))

batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Find IPL 2026 matches and squad players
ipl_2026_comp = comp[comp['comp_name'] == 'IPL 2026']['comp_id'].iloc[0]
ipl_2026_matches = matches[matches['comp_id'] == ipl_2026_comp]['match_id'].unique()

# Players who actively played in IPL 2026 (in playing XI)
ipl_2026_played_ids = set(p11[(p11['match_id'].isin(ipl_2026_matches)) & (p11['is_played'] == 1)]['player_id'].unique())
# Players in an IPL 2026 squad
ipl_2026_squad_ids = set(mapping[mapping['comp_id'] == ipl_2026_comp]['player_id'].unique())
ipl_2026_squad_names = set(mapping[mapping['comp_id'] == ipl_2026_comp]['player_name'].unique())

# Also check Pakistani players (ineligible)
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())

# Player team mappings for reference
player_all_teams = mapping.groupby('player_name')['team_name'].apply(lambda x: ', '.join(x.unique())).to_dict()

# CRITERIA:
# 1. NOT in IPL 2026 squad (not playing currently for any IPL franchise).
# 2. NOT a Pakistani player (auction ineligible).
# 3. Available to be bought at the auction!

eligible_batters = batters[(~batters['striker_name'].isin(ipl_2026_squad_names)) & 
                           (~batters['striker_name'].isin(pak_players))].copy()

eligible_bowlers = bowlers[(~bowlers['bowler_name'].isin(ipl_2026_squad_names)) & 
                           (~bowlers['bowler_name'].isin(pak_players))].copy()

eligible_batters['teams'] = eligible_batters['striker_name'].map(player_all_teams)
eligible_bowlers['teams'] = eligible_bowlers['bowler_name'].map(player_all_teams)

# Let's see: how many balls did they face/bowl under pressure?
print(f"Total eligible auction-available batters in dataset: {len(eligible_batters)}")
print(f"Total eligible auction-available bowlers in dataset: {len(eligible_bowlers)}")

# Sort by RCI regularized
print("\n=== TOP 25 ELIGIBLE AUCTION-AVAILABLE BATTERS UNDER PRESSURE (NOT IN IPL 2026) ===")
cols_bat = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(eligible_batters[eligible_batters['press_balls'] >= 20].sort_values('rci_bat_regularized', ascending=False)[cols_bat].head(25).to_string(index=False))

print("\n=== TOP 25 ELIGIBLE AUCTION-AVAILABLE BOWLERS UNDER PRESSURE (NOT IN IPL 2026) ===")
cols_bowl = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(eligible_bowlers[eligible_bowlers['press_balls'] >= 20].sort_values('rci_bowl_regularized', ascending=False)[cols_bowl].head(25).to_string(index=False))
