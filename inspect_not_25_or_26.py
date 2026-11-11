import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')

# Find 2025 IPL competition
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())

# Also 2026 IPL competition
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

# Look at players in pool_not_2025
# Which ones have NEVER played in 2025 IPL and are NOT in 2026 IPL?
not_2025_or_2026 = df_map[~df_map['player_id'].isin(named_2025) & ~df_map['player_id'].isin(named_2026)]
print(f"Players not in 2025 AND not in 2026 IPL: {not_2025_or_2026['player_id'].nunique()}")

# Let's inspect the Indian players among them!
# Who has played for India, India A, or was an Indian player in 2022/2023/2024?
# Let's see who is in not_2025_or_2026 by team
print("\nTeams in not_2025_or_2026:")
print(not_2025_or_2026.groupby('team_name')['player_id'].nunique().sort_values(ascending=False))
