import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
mapping = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competition_team_player_mapping.csv')
from pressure_engine import bbb as bbb_press

# All players in the dataset
all_players_mapping = mapping.drop_duplicates(subset=['player_id', 'player_name'])
print("Total unique players in mapping table:", len(all_players_mapping))

# Players in emerging tournaments (comp_id 2670, 3289)
emerging_comps = [2670, 3289]
emerging_mapping = mapping[mapping['comp_id'].isin(emerging_comps)]
print("Emerging tournament players count:", emerging_mapping['player_name'].nunique())
print("Emerging teams:", emerging_mapping['team_name'].unique())

# Let's inspect domestic / emerging players batting and bowling in the dataset
# Let's see: what if the user means players from the emerging tournaments or uncapped domestic pool?
# Let's get batting stats under pressure for all emerging tournament players
emerging_player_names = emerging_mapping['player_name'].unique()

from rank_candidates import batters, bowlers

em_batters = batters[batters['striker_name'].isin(emerging_player_names)].sort_values('clutch_bat_score', ascending=False)
print("\n=== TOP EMERGING BATTERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bat = ['striker_name', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'boundary_pct_press', 'dot_pct_press', 'clutch_bat_score']
print(em_batters[cols_bat].head(15).to_string(index=False))

em_bowlers = bowlers[bowlers['bowler_name'].isin(emerging_player_names)].sort_values('clutch_bowl_score', ascending=False)
print("\n=== TOP EMERGING BOWLERS UNDER PRESSURE (MIN 120 PRESSURE BALLS) ===")
cols_bowl = ['bowler_name', 'press_balls', 'press_runs', 'econ_press', 'press_wickets', 'dot_pct_press', 'boundary_pct_conceded_press', 'clutch_bowl_score']
print(em_bowlers[cols_bowl].head(15).to_string(index=False))
