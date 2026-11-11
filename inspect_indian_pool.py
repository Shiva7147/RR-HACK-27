import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Find all players associated with India, India A, or Indian domestic in mapping
india_players = df_map[df_map['team_name'].str.contains('India|Chennai|Mumbai|Kolkata|Rajasthan|Delhi|Punjab|Bangalore|Gujarat|Lucknow|Hyderabad', case=False, na=False)]

# What are the teams in df_map?
print("Teams in df_map with 'India' or domestic:")
print(df_map[df_map['team_name'].str.contains('India', case=False, na=False)]['team_name'].value_counts())

# Check IPL 2026 squads specifically
ipl_2026_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
ipl_2026_players = set(df_map[df_map['comp_id'].isin(ipl_2026_comps)]['player_id'].unique())

# Also check IPL 2025 squads
ipl_2025_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
ipl_2025_players = set(df_map[df_map['comp_id'].isin(ipl_2025_comps)]['player_id'].unique())

all_ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
all_ipl_players = set(df_map[df_map['comp_id'].isin(all_ipl_comps)]['player_id'].unique())

print(f"Total Indian players mapped: {len(india_players['player_id'].unique())}")
print(f"Total IPL 2026 players: {len(ipl_2026_players)}")

# Players who played for India A or India in dataset
india_reps = df_map[df_map['team_name'].isin(['India A', 'India', 'India Emerging'])]['player_id'].unique()

print("\n--- Indian Players NOT in IPL 2026 Squads ---")
for pid in india_reps:
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    in_26 = pid in ipl_2026_players
    in_25 = pid in ipl_2025_players
    in_any_ipl = pid in all_ipl_players
    teams = ", ".join(df_map[df_map['player_id'] == pid]['team_name'].unique())
    if not in_26:
        print(f"ID: {pid:6d} | {name:25s} | in_IPL_2026: {in_26} | in_IPL_2025: {in_25} | in_any_IPL: {in_any_ipl} | Teams: {teams}")
