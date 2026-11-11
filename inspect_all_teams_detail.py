import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')

# Let's inspect all unique team names in competitions where Indian players might play
print("All teams across all competitions:")
print(df_map['team_name'].value_counts().to_string())
