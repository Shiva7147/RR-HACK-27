import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')

# Competitions 2670 and 3289
em_comps = [2670, 3289]
india_a = df_map[df_map['comp_id'].isin(em_comps) & df_map['team_name'].str.contains('India', case=False, na=False)]
print("India A players in emerging competitions count:", len(india_a['player_id'].unique()))

# Check 2025 IPL comp
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())

# Check 2026 IPL comp
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

# Also check whether they ever played an IPL match in dataset
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
m_ipl = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].tolist()
played_ipl = set(p11[p11['match_id'].isin(m_ipl)]['player_id'].unique())

print("\n--- ALL INDIA A / EMERGING PLAYERS ---")
for pid in india_a['player_id'].unique():
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    in_25 = pid in named_2025
    in_26 = pid in named_2026
    has_played_ipl = pid in played_ipl
    
    # What competitions did they play in?
    p_comps = df_map[df_map['player_id'] == pid]['comp_name'].unique().tolist()
    print(f"ID: {pid:6d} | {name:25s} | Named_2025_IPL: {str(in_25):5s} | Named_2026_IPL: {str(in_26):5s} | Played_IPL_Ever: {str(has_played_ipl):5s}")
