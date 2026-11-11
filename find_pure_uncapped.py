import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))
teams = pd.read_csv(os.path.join(data_dir, 'teams.csv'))

# 1. Identify all IPL competitions in competitions.csv
ipl_comps = comp[comp['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].unique()
print("IPL competitions:", comp[comp['comp_id'].isin(ipl_comps)][['comp_id', 'comp_name', 'season']])

# 2. Identify all matches that are IPL matches
ipl_matches = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].unique()
print(f"Total IPL matches in dataset: {len(ipl_matches)}")

# 3. Identify all players who EVER played an IPL match in playing_eleven.csv
p11_ipl = p11[(p11['match_id'].isin(ipl_matches)) & (p11['is_played'] == 1)]
ipl_played_player_ids = set(p11_ipl['player_id'].unique())
print(f"Total players who have actually played at least 1 IPL match: {len(ipl_played_player_ids)}")

# Also check mapping for players mapped to IPL teams
mapping_ipl = mapping[mapping['comp_id'].isin(ipl_comps)]
ipl_squad_player_ids = set(mapping_ipl['player_id'].unique())
ipl_squad_player_names = set(mapping_ipl['player_name'].unique())
print(f"Total players who were in an IPL squad: {len(ipl_squad_player_ids)}")

# Also check senior international players: players who played senior international matches for Full Member nations
senior_full_members = ['India', 'Australia', 'England', 'South Africa', 'New Zealand', 'West Indies', 'Sri Lanka', 'Bangladesh', 'Afghanistan', 'Pakistan']
senior_comps = comp[(comp['match_format'] == 'T20I') & (~comp['comp_name'].str.contains('Emerging|Rising Stars|A$', regex=True))]
# Full international players
senior_mapping = mapping[(mapping['comp_id'].isin(senior_comps['comp_id'])) & (mapping['team_name'].isin(senior_full_members))]
senior_intl_player_ids = set(senior_mapping['player_id'].unique())
senior_intl_player_names = set(senior_mapping['player_name'].unique())
print(f"Total senior international full member players: {len(senior_intl_player_ids)}")

# Exclude Pakistani players as they are ineligible for IPL
pak_mapping = mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]
pak_player_ids = set(pak_mapping['player_id'].unique())

# 4. Now, find the UNCAPPED & NON-IPL PLAYERS who have NEVER played an IPL game:
# Filter: NOT in ipl_played_player_ids AND NOT in pak_player_ids
print("\n--- Identifying Pure Uncapped / Non-IPL Domestic Players ---")
all_mapping_players = mapping[['player_id', 'player_name']].drop_duplicates()
all_mapping_players['has_played_ipl'] = all_mapping_players['player_id'].isin(ipl_played_player_ids)
all_mapping_players['in_ipl_squad'] = all_mapping_players['player_id'].isin(ipl_squad_player_ids)
all_mapping_players['is_senior_intl'] = all_mapping_players['player_id'].isin(senior_intl_player_ids)
all_mapping_players['is_pakistan'] = all_mapping_players['player_id'].isin(pak_player_ids)

# Let's see the count of players who have NEVER played IPL
never_ipl = all_mapping_players[(~all_mapping_players['has_played_ipl']) & (~all_mapping_players['is_pakistan'])]
print(f"Total players who have NEVER played an IPL match (non-Pakistani): {len(never_ipl)}")

# Let's see players who have NEVER been in an IPL squad
never_in_ipl_squad = all_mapping_players[(~all_mapping_players['in_ipl_squad']) & (~all_mapping_players['is_pakistan'])]
print(f"Total players who have NEVER been in an IPL squad (non-Pakistani): {len(never_in_ipl_squad)}")
