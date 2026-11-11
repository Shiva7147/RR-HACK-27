import pandas as pd
import numpy as np
import os

from find_pure_uncapped import never_ipl, ipl_played_player_ids, mapping, bbb

data_dir = r'D:\6af3166e7b922_data_pack'
batters = pd.read_csv(os.path.join(data_dir, 'all_batters_pressure_metrics.csv'))
bowlers = pd.read_csv(os.path.join(data_dir, 'all_bowlers_pressure_metrics.csv'))

# Indian players: in India A or in Indian domestic teams
india_a_players = mapping[mapping['team_name'] == 'India A']['player_name'].unique()

# Check which India A players have NEVER played an IPL match:
india_a_never_played_ipl = [p for p in india_a_players if mapping[mapping['player_name'] == p]['player_id'].iloc[0] not in ipl_played_player_ids]
print("India A players who have NEVER played an IPL match:")
print(india_a_never_played_ipl)

# Check all Indian players in the mapping who have never played an IPL match
# How to identify Indian players?
# In mapping, players who played for India, India A, or Indian domestic squads
indian_player_names = set(mapping[mapping['team_name'].isin(['India', 'India A'])]['player_name'].unique())

# Also players in IPL squads who have 0 matches played:
ipl_comps = [1358, 1715, 2193, 2725, 3298]
bench_ipl_players = mapping[(mapping['comp_id'].isin(ipl_comps)) & (~mapping['player_id'].isin(ipl_played_player_ids))]['player_name'].unique()
print(f"\nTotal bench / uncapped players who were in IPL squads but NEVER played an IPL match: {len(bench_ipl_players)}")
print("Sample bench players (0 IPL caps):", bench_ipl_players[:25])
