import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

ipl_comps_2026 = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
ipl_2026_squad_players = set(df_map[df_map['comp_id'].isin(ipl_comps_2026)]['player_id'].unique())
rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

# Exclude any player currently in an IPL 2026 squad OR who played for RR
avail_batters = batters[~batters['striker_id'].isin(ipl_2026_squad_players) & ~batters['striker_id'].isin(rr_players)].copy()
avail_bowlers = bowlers[~bowlers['bowler_id'].isin(ipl_2026_squad_players) & ~bowlers['bowler_id'].isin(rr_players)].copy()

# Add team mappings
player_teams = df_map.groupby('player_id')['team_name'].apply(lambda x: ", ".join(set(x))).to_dict()
avail_batters['teams'] = avail_batters['striker_id'].map(player_teams)
avail_bowlers['teams'] = avail_bowlers['bowler_id'].map(player_teams)

print(f"Total available batters not in IPL 2026: {len(avail_batters)}")
print(f"Total available bowlers not in IPL 2026: {len(avail_bowlers)}")

# Let's inspect top available batters with min 20 pressure balls
top_avail_bat = avail_batters[avail_batters['press_balls'] >= 20].sort_values(by='rci_bat_regularized', ascending=False)
print("\n--- TOP AVAILABLE BATTERS (Not in IPL 2026 & Not in RR) ---")
print(top_avail_bat[['striker_id', 'striker_name', 'teams', 'total_balls', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'rci_bat_regularized']].head(20).to_string())

# Top available bowlers with min 20 pressure balls
top_avail_bowl = avail_bowlers[avail_bowlers['press_balls'] >= 20].sort_values(by='rci_bowl_regularized', ascending=False)
print("\n--- TOP AVAILABLE BOWLERS (Not in IPL 2026 & Not in RR) ---")
print(top_avail_bowl[['bowler_id', 'bowler_name', 'teams', 'total_balls', 'press_balls', 'press_wickets', 'econ_press', 'econ_delta', 'bnd_conceded_pct_press', 'rci_bowl_regularized']].head(20).to_string())
