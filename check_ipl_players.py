import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
mapping = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competition_team_player_mapping.csv')

# Check which players played in IPL
ipl_comps = comp[comp['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].unique()
ipl_players = mapping[mapping['comp_id'].isin(ipl_comps)]['player_name'].unique()
print(f"Total unique players who played in IPL in the dataset: {len(ipl_players)}")
