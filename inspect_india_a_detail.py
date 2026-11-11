import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Find all Indian players
# How do we know who is Indian?
# 1. Played for India or India A
# 2. Or is an Indian player in an IPL team
# Let's see all unique players in India or India A
india_reps = set(df_map[df_map['team_name'].isin(['India', 'India A'])]['player_id'].unique())

# Also let's inspect all players whose team_name is in IPL teams
ipl_comps_2026 = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
ipl_2026_squad_players = set(df_map[df_map['comp_id'].isin(ipl_comps_2026)]['player_id'].unique())

rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

print(f"Total India/India A players: {len(india_reps)}")

# Let's inspect India A players specifically:
print("\n=== ALL INDIA A PLAYERS & THEIR 2026 IPL SQUAD STATUS ===")
ia_df = df_map[df_map['team_name'] == 'India A'].drop_duplicates(subset=['player_id'])
for _, r in ia_df.iterrows():
    pid = r['player_id']
    name = r['player_name']
    in_26 = pid in ipl_2026_squad_players
    in_rr = pid in rr_players
    all_teams = ", ".join(df_map[df_map['player_id'] == pid]['team_name'].unique())
    print(f"ID: {pid:6d} | {name:25s} | In IPL 2026: {str(in_26):5s} | In RR: {str(in_rr):5s} | Teams: {all_teams}")
