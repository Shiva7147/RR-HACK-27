import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')

emerging_comps = comps[comps['comp_name'].str.contains('Emerging|Rising', case=False, na=False)]
print("Emerging Competitions:")
print(emerging_comps[['comp_id', 'comp_name', 'season']])

# Get players in these emerging competitions
emerging_ids = emerging_comps['comp_id'].tolist()
em_map = df_map[df_map['comp_id'].isin(emerging_ids)]

print("\nTeams in Emerging Competitions:")
print(em_map[['comp_id', 'team_name']].drop_duplicates())

print(f"\nTotal players in Emerging Competitions: {len(em_map['player_id'].unique())}")
