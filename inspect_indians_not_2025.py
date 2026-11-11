import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')

# Find 2025 IPL competition
ipl_2025_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_in_2025_ipl = set(df_map[df_map['comp_id'].isin(ipl_2025_comps)]['player_id'].unique())

# Also 2026 IPL teams
ipl_2026_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_in_2026_ipl = set(df_map[df_map['comp_id'].isin(ipl_2026_comps)]['player_id'].unique())

# Indian players: played for India or India A
india_pids = set(df_map[df_map['team_name'].isin(['India', 'India A'])]['player_id'].unique())

indians_not_in_2025 = india_pids - named_in_2025_ipl
print(f"Indian players NOT named in 2025 IPL teams: {len(indians_not_in_2025)}")

for pid in indians_not_in_2025:
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    in_26 = pid in named_in_2026_ipl
    comps_played = df_map[df_map['player_id'] == pid][['comp_id', 'comp_name', 'team_name']].drop_duplicates()
    print(f"\n=================== {name} (ID: {pid}) | In IPL 2026: {in_26} ===================")
    print(comps_played.to_string())
