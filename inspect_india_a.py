import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')

p_comps = p11.merge(matches[['match_id', 'comp_id']], on='match_id').merge(comps, on='comp_id')
ipl_comps = comps[comps['comp_name'].str.contains('IPL|Indian Premier League', case=False, na=False)]['comp_id'].tolist()

ipl_played_players = set(p_comps[p_comps['comp_id'].isin(ipl_comps)]['player_id'].unique())
all_players = set(df_map['player_id'].unique())

# Also find which players are in IPL squads in df_map
ipl_squad_players = set(df_map[df_map['comp_id'].isin(ipl_comps)]['player_id'].unique())

print(f"Total unique players in mapping: {len(all_players)}")
print(f"Players who appeared in IPL matches in dataset: {len(ipl_played_players)}")
print(f"Players listed in IPL squads in mapping: {len(ipl_squad_players)}")

india_a = df_map[df_map['team_name'].str.contains('India A', case=False, na=False)]
print("\n--- India A Players ---")
for _, r in india_a.drop_duplicates(subset=['player_id']).iterrows():
    played_ipl = r['player_id'] in ipl_played_players
    in_ipl_squad = r['player_id'] in ipl_squad_players
    print(f"ID: {r['player_id']} | Name: {r['player_name']} | Played IPL in dataset: {played_ipl} | In IPL Squad: {in_ipl_squad}")

# Check what other competitions are in the dataset
print("\n--- Non-IPL Competitions ---")
non_ipl_comps = comps[~comps['comp_id'].isin(ipl_comps)]
print(non_ipl_comps[['comp_id', 'comp_name', 'season']].to_string())
