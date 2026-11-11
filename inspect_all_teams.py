import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')

# Competitions
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()

# Mapping teams
player_teams = df_map.groupby('player_id')['team_name'].apply(lambda x: list(set(x))).to_dict()

# Who is in IPL 2026?
in_ipl_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())
in_any_ipl = set(df_map[df_map['comp_id'].isin(ipl_comps)]['player_id'].unique())

# Also who played in IPL 2026 matches?
p_ipl_2026 = set(p11.merge(pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')[['match_id', 'comp_id']], on='match_id')[lambda x: x['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

print(f"Total players in dataset: {len(player_teams)}")
print(f"Players in IPL 2026 squads: {len(in_ipl_2026)}")
print(f"Players in any IPL squad: {len(in_any_ipl)}")

# Let's inspect players who are domestic Indian players
# How are domestic Indian players identified in df_map?
# Let's print all teams in df_map
all_teams = df_map['team_name'].unique().tolist()
print("\nUnique teams in df_map:")
print(sorted(all_teams))
