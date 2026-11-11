import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')

# What are all the competitions in the dataset?
print(comps['comp_name'].value_counts())

# Check how many players exist per team
print("\nPlayer count per team in df_map:")
print(df_map.groupby('team_name')['player_id'].nunique().sort_values(ascending=False))
