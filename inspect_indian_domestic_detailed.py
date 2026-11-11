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

# Senior India International players who are permanent national team stars (not auction scouting gems):
# e.g., Rohit Sharma, Virat Kohli, Hardik Pandya, Jasprit Bumrah, Ravindra Jadeja, Suryakumar Yadav, KL Rahul, Rishabh Pant, Shubman Gill, Mohammed Shami, Mohammed Siraj, Arshdeep Singh, Axar Patel, Kuldeep Yadav, Sanju Samson, Yashasvi Jaiswal
senior_india_icons = [
    'Rohit Sharma', 'Virat Kohli', 'Hardik Pandya', 'Jasprit Bumrah', 'Ravindra Jadeja',
    'Suryakumar Yadav', 'KL Rahul', 'Rishabh Pant', 'Shubman Gill', 'Mohammed Shami',
    'Mohammed Siraj', 'Arshdeep Singh', 'Axar Patel', 'Kuldeep Yadav', 'Sanju Samson',
    'Yashasvi Jaiswal', 'Shreyas Iyer', 'Yuzvendra Chahal', 'Ravichandran Ashwin', 'Bhuvneshwar Kumar'
]

# Identify Indian players in the dataset:
# Players who played for India A, or are Indian domestic players
# In mapping, let's see which players have Indian domestic teams or played for India A
india_a_players = set(mapping[mapping['team_name'] == 'India A']['player_name'].unique())

# Also all Indian domestic players in IPL squads
# How to get Indian players vs Overseas players?
# Overseas players in IPL squads: they also appear in senior international teams of overseas countries!
overseas_senior_teams = [
    'Australia', 'England', 'South Africa', 'New Zealand', 'West Indies', 
    'Sri Lanka', 'Bangladesh', 'Afghanistan', 'Zimbabwe', 'Ireland', 'Netherlands'
]
overseas_intl_players = set(mapping[mapping['team_name'].isin(overseas_senior_teams)]['player_name'].unique())

# Also Pakistani players
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())

# All players in IPL competitions
ipl_comps = comp[comp['comp_name'].str.contains('IPL')]['comp_id'].unique()
ipl_all_players = set(mapping[mapping['comp_id'].isin(ipl_comps)]['player_name'].unique())

# Domestic Indian Players = in IPL or India A, but NOT in overseas_intl_players, NOT in pak_players, NOT in senior_india_icons
indian_domestic_pool = (ipl_all_players.union(india_a_players)) - overseas_intl_players - pak_players - set(senior_india_icons)

print(f"Total Indian domestic / uncapped players identified: {len(indian_domestic_pool)}")

# Batters
ind_bat = batters[batters['striker_name'].isin(indian_domestic_pool)].copy()
# Bowlers
ind_bowl = bowlers[bowlers['bowler_name'].isin(indian_domestic_pool)].copy()

# Add team mappings
player_teams = mapping.groupby('player_name')['team_name'].apply(lambda x: ', '.join(x.unique())).to_dict()
ind_bat['teams'] = ind_bat['striker_name'].map(player_teams)
ind_bowl['teams'] = ind_bowl['bowler_name'].map(player_teams)

print("\n=== TOP 25 INDIAN DOMESTIC / UNCAPPED BATTERS UNDER PRESSURE ===")
cols_b = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(ind_bat[ind_bat['press_balls'] >= 30].sort_values('rci_bat_regularized', ascending=False)[cols_b].head(25).to_string(index=False))

print("\n=== TOP 25 INDIAN DOMESTIC / UNCAPPED BOWLERS UNDER PRESSURE ===")
cols_bw = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(ind_bowl[ind_bowl['press_balls'] >= 30].sort_values('rci_bowl_regularized', ascending=False)[cols_bw].head(25).to_string(index=False))
