import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Let's inspect India A squad players in detail
india_a_players = df_map[df_map['team_name'] == 'India A']['player_id'].unique()
print(f"India A unique players count: {len(india_a_players)}")

# Batters among India A
ia_batters = batters[batters['striker_id'].isin(india_a_players)]
print("\n--- India A Batters in Dataset ---")
print(ia_batters[['striker_id', 'striker_name', 'total_balls', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'rci_bat_regularized']].sort_values(by='rci_bat_regularized', ascending=False).to_string())

# Bowlers among India A
ia_bowlers = bowlers[bowlers['bowler_id'].isin(india_a_players)]
print("\n--- India A Bowlers in Dataset ---")
print(ia_bowlers[['bowler_id', 'bowler_name', 'total_balls', 'press_balls', 'press_wickets', 'econ_press', 'econ_delta', 'bnd_conceded_pct_press', 'rci_bowl_regularized']].sort_values(by='rci_bowl_regularized', ascending=False).to_string())
