import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

ipl_comps = comps[comps['comp_name'].str.contains('IPL|Indian Premier League', case=False, na=False)]['comp_id'].tolist()
ipl_players = set(df_map[df_map['comp_id'].isin(ipl_comps)]['player_id'].unique())

# Filter batters who are NOT in any IPL squad
bat_non_ipl = batters[~batters['striker_id'].isin(ipl_players)].copy()
bowl_non_ipl = bowlers[~bowlers['bowler_id'].isin(ipl_players)].copy()

player_teams = df_map.groupby('player_id')['team_name'].apply(lambda s: ", ".join(set(s))).to_dict()
bat_non_ipl['teams'] = bat_non_ipl['striker_id'].map(player_teams)
bowl_non_ipl['teams'] = bowl_non_ipl['bowler_id'].map(player_teams)

print("\n--- TOP NON-IPL BATTERS UNDER PRESSURE (Min 25 pressure balls) ---")
top_bat = bat_non_ipl[bat_non_ipl['press_balls'] >= 25].sort_values(by='rci_bat_regularized', ascending=False)
print(top_bat[['striker_id', 'striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'rci_bat_regularized']].head(25).to_string())

print("\n--- TOP NON-IPL BOWLERS UNDER PRESSURE (Min 24 pressure balls) ---")
top_bowl = bowl_non_ipl[bowl_non_ipl['press_balls'] >= 24].sort_values(by='rci_bowl_regularized', ascending=False)
print(top_bowl[['bowler_id', 'bowler_name', 'teams', 'press_balls', 'press_wickets', 'econ_press', 'econ_delta', 'bnd_conceded_pct_press', 'rci_bowl_regularized']].head(25).to_string())
