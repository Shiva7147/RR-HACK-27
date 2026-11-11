import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Find ALL competitions that are IPL
ipl_comps = comps[comps['comp_name'].str.contains('IPL|Indian Premier League', case=False, na=False)]['comp_id'].tolist()
print("IPL comp IDs:", ipl_comps)

# Find ALL players ever mapped to any IPL team in any season
ipl_players_all_time = set(df_map[df_map['comp_id'].isin(ipl_comps)]['player_id'].unique())
print(f"Total players ever named in an IPL squad in this dataset: {len(ipl_players_all_time)}")

# Also find all players who ever played an IPL match
matches_ipl = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].tolist()
ipl_played_all_time = set(p11[p11['match_id'].isin(matches_ipl)]['player_id'].unique())
print(f"Total players who ever played an IPL match: {len(ipl_played_all_time)}")

# Union of any player ever in an IPL squad or match
any_ipl_player = ipl_players_all_time.union(ipl_played_all_time)
print(f"Union of any IPL player: {len(any_ipl_player)}")

# Now find all players associated with India or India A
india_players = df_map[df_map['team_name'].isin(['India', 'India A'])]
print(f"Total entries for India / India A: {len(india_players)}")

# Players who played for India or India A BUT NEVER IN ANY IPL SQUAD OR MATCH
pure_uncapped_indians = set(india_players['player_id'].unique()) - any_ipl_player
print(f"Pure uncapped Indian players in dataset: {len(pure_uncapped_indians)}")

for pid in pure_uncapped_indians:
    p_info = df_map[df_map['player_id'] == pid]
    name = p_info['player_name'].iloc[0]
    teams = ", ".join(p_info['team_name'].unique())
    print(f"Player ID: {pid:6d} | Name: {name:25s} | Teams: {teams}")
