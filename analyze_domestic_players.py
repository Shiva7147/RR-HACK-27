import pandas as pd
import numpy as np

mapping = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competition_team_player_mapping.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
from pressure_engine import bbb as bbb_press

# Let's inspect domestic Indian players in the dataset
# Indian domestic players who play in IPL teams or have domestic background
ipl_comps = comp[comp['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].unique()
ipl_mapping = mapping[mapping['comp_id'].isin(ipl_comps)].drop_duplicates(subset=['player_id', 'player_name'])

# Overseas vs Indian player identification:
# Non-Indian national teams in competitions.csv:
t20i_comps = comp[comp['match_format'] == 'T20I']['comp_id'].unique()
t20i_mapping = mapping[mapping['comp_id'].isin(t20i_comps)]

# If a player played for India in T20I or only in IPL teams, they are Indian
india_teams = t20i_mapping[t20i_mapping['team_name'].str.contains('India', case=False, na=False)]['player_name'].unique()
non_india_intl_players = t20i_mapping[~t20i_mapping['team_name'].str.contains('India', case=False, na=False)]['player_name'].unique()

print(f"Total players in IPL mapping: {len(ipl_mapping)}")
print(f"Total players in India international: {len(india_teams)}")
print(f"Total non-India international players: {len(non_india_intl_players)}")

# Identify Indian domestic / uncapped / emerging players in IPL
# Players who played in IPL but NOT for non-Indian international teams:
indian_players = ipl_mapping[~ipl_mapping['player_name'].isin(non_india_intl_players)]
print(f"Total Indian players in IPL pool: {len(indian_players)}")

# Uncapped or domestic Indian players (not played for India senior T20I in this dataset)
domestic_indian_players = indian_players[~indian_players['player_name'].isin(india_teams)]
print(f"Total domestic / uncapped Indian players in IPL pool: {len(domestic_indian_players)}")

# Look at top domestic Indian batters under pressure
from rank_candidates import batters, bowlers

domestic_batters = batters[batters['striker_name'].isin(domestic_indian_players['player_name'])].sort_values('clutch_bat_score', ascending=False)
print("\n=== TOP DOMESTIC INDIAN BATTERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bat = ['striker_name', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'boundary_pct_press', 'dot_pct_press', 'clutch_bat_score']
print(domestic_batters[cols_bat].head(15).to_string(index=False))

domestic_bowlers = bowlers[bowlers['bowler_name'].isin(domestic_indian_players['player_name'])].sort_values('clutch_bowl_score', ascending=False)
print("\n=== TOP DOMESTIC INDIAN BOWLERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bowl = ['bowler_name', 'press_balls', 'press_runs', 'econ_press', 'press_wickets', 'dot_pct_press', 'boundary_pct_conceded_press', 'clutch_bowl_score']
print(domestic_bowlers[cols_bowl].head(15).to_string(index=False))
