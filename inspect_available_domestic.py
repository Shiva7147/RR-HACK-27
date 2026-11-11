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

# Find all players who played in IPL 2026 or IPL 2025
ipl_recent_comps = comp[comp['comp_name'].isin(['IPL 2025', 'IPL 2026'])]['comp_id'].unique()
ipl_recent_matches = matches[matches['comp_id'].isin(ipl_recent_comps)]['match_id'].unique()

# Players who played in IPL 2025 or IPL 2026
recent_ipl_played_ids = set(p11[(p11['match_id'].isin(ipl_recent_matches)) & (p11['is_played'] == 1)]['player_id'].unique())
recent_ipl_squad_ids = set(mapping[mapping['comp_id'].isin(ipl_recent_comps)]['player_id'].unique())

# Also all IPL played ever
all_ipl_comps = comp[comp['comp_name'].str.contains('IPL')]['comp_id'].unique()
all_ipl_matches = matches[matches['comp_id'].isin(all_ipl_comps)]['match_id'].unique()
ever_ipl_played_ids = set(p11[(p11['match_id'].isin(all_ipl_matches)) & (p11['is_played'] == 1)]['player_id'].unique())

# Senior International players for India
senior_india_ids = set(mapping[mapping['team_name'] == 'India']['player_id'].unique())

# Let's inspect Indian domestic players who have NEVER played in IPL:
# Indian domestic: in India A, or in domestic squads, but NOT in ever_ipl_played_ids and NOT in senior_india_ids
# Let's see:
india_a_players = mapping[mapping['team_name'] == 'India A'][['player_id', 'player_name']].drop_duplicates()
print("All India A players in dataset:")
india_a_players['ever_played_ipl'] = india_a_players['player_id'].isin(ever_ipl_played_ids)
india_a_players['played_recent_ipl'] = india_a_players['player_id'].isin(recent_ipl_played_ids)
india_a_players['in_recent_ipl_squad'] = india_a_players['player_id'].isin(recent_ipl_squad_ids)
print(india_a_players.to_string(index=False))

# Now let's check all Indian players in mapping who are NOT in recent_ipl_squad_ids (not in 2025/2026 squads):
all_indian_in_mapping = mapping[mapping['team_name'].isin(['India A', 'India']) | mapping['comp_name'].str.contains('IPL')][['player_id', 'player_name']].drop_duplicates()
all_indian_in_mapping['in_recent_ipl_squad'] = all_indian_in_mapping['player_id'].isin(recent_ipl_squad_ids)
all_indian_in_mapping['ever_played_ipl'] = all_indian_in_mapping['player_id'].isin(ever_ipl_played_ids)
all_indian_in_mapping['is_senior_india'] = all_indian_in_mapping['player_id'].isin(senior_india_ids)

available_indian_domestic = all_indian_in_mapping[(~all_indian_in_mapping['in_recent_ipl_squad']) & (~all_indian_in_mapping['is_senior_india'])]
print(f"\nIndian players NOT in any IPL 2025/2026 squad (open/unselected/free agents): {len(available_indian_domestic)}")
print(available_indian_domestic.head(30).to_string(index=False))
