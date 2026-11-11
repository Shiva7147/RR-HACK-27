import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')

# Let's inspect all players who have NEVER played an IPL game in the dataset
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
ipl_matches = matches[matches['comp_id'].isin(ipl_comps)]['match_id'].tolist()
played_ipl = set(p11[p11['match_id'].isin(ipl_matches)]['player_id'].unique())
named_ipl = set(df_map[df_map['comp_id'].isin(ipl_comps)]['player_id'].unique())

print(f"Total unique players: {df_map['player_id'].nunique()}")
print(f"Total players ever named in IPL: {len(named_ipl)}")
print(f"Total players ever played IPL: {len(played_ipl)}")

# Who are the players who NEVER played IPL or were NEVER named in IPL?
never_ipl = set(df_map['player_id'].unique()) - named_ipl
print(f"Total players NEVER named in any IPL team: {len(never_ipl)}")

# Of these 740 players, what teams do they belong to?
never_ipl_df = df_map[df_map['player_id'].isin(never_ipl)]
print("\nTeams of players who were NEVER in any IPL squad:")
print(never_ipl_df['team_name'].value_counts())
