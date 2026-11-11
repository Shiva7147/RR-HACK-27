import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')

# Exclude 2025 and 2026 IPL
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())
rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

# Eligible pool
pool_pids = set(df_map['player_id'].unique()) - named_2025 - named_2026 - rr_players

# Check competitions in 2025 and 2026 in the dataset!
comps_25_26 = comps[comps['season'].isin(['2025', '2026', 2025, 2026, '2025/26'])]
print("2025-2026 Competitions in the dataset:")
print(comps_25_26[['comp_id', 'comp_name', 'season']].to_string())

# Check matches played in 2025-2026 by eligible players
m_25_26 = matches[matches['comp_id'].isin(comps_25_26['comp_id'])]['match_id'].tolist()
p_played_25_26 = p11[p11['match_id'].isin(m_25_26) & p11['player_id'].isin(pool_pids)]

print(f"\nEligible players who played matches in 2025-2026 in dataset: {p_played_25_26['player_id'].nunique()}")

# Let's inspect who these players are and their teams
recent_players = df_map[df_map['player_id'].isin(p_played_25_26['player_id'].unique())].drop_duplicates(subset=['player_id'])
print(recent_players[['player_id', 'player_name', 'team_name']].to_string())
