import pandas as pd
import numpy as np
import os

from find_exact_uncapped_open import played_ipl_ids, mapping, bbb, batters, bowlers

# Find all Indian players in mapping who NEVER played an IPL game
# In mapping, players who played for India, India A, or are Indian domestic players
# Let's find players whose nationality/teams are Indian
all_indian_players = mapping[mapping['team_name'].isin(['India', 'India A']) | 
                             mapping['comp_name'].str.contains('IPL')]['player_name'].unique()

# Exclude overseas players in IPL
overseas_teams = ['Australia', 'England', 'South Africa', 'New Zealand', 'West Indies', 'Sri Lanka', 'Bangladesh', 'Afghanistan', 'Zimbabwe', 'Ireland', 'Netherlands', 'Pakistan']
overseas_players = set(mapping[mapping['team_name'].isin(overseas_teams)]['player_name'].unique())

indian_domestic_candidates = [p for p in all_indian_players if p not in overseas_players]

# Check which ones have NEVER played an IPL match:
uncapped_indians = []
for p in indian_domestic_candidates:
    p_ids = mapping[mapping['player_name'] == p]['player_id'].unique()
    has_played = any(pid in played_ipl_ids for pid in p_ids)
    if not has_played:
        # Check balls faced and bowled
        b_faced = len(bbb[bbb['striker_name'] == p])
        b_bowled = len(bbb[bbb['bowler_name'] == p])
        uncapped_indians.append({
            'player_name': p,
            'balls_faced': b_faced,
            'balls_bowled': b_bowled
        })

df_uncapped_ind = pd.DataFrame(uncapped_indians)
print(f"Total uncapped Indian players in mapping: {len(df_uncapped_ind)}")
print("\nUncapped Indian players who actually faced balls or bowled balls in the dataset:")
print(df_uncapped_ind[(df_uncapped_ind['balls_faced'] > 0) | (df_uncapped_ind['balls_bowled'] > 0)].to_string(index=False))
