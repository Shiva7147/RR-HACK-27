import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')
bbb = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')

# IPL 2025 comp
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025_ipl = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())

# Also IPL 2026
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026_ipl = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

# India or India A players
india_pids = set(df_map[df_map['team_name'].isin(['India', 'India A'])]['player_id'].unique())

# Indian players NOT named in 2025 IPL teams
eligible_indians = india_pids - named_2025_ipl

print(f"Eligible Indian player IDs count: {len(eligible_indians)}")

print("\n--- BATTING METRICS FOR ELIGIBLE INDIANS ---")
bat_el = batters[batters['striker_id'].isin(eligible_indians)]
print(bat_el[['striker_id', 'striker_name', 'total_balls', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'rci_bat_regularized']].to_string())

print("\n--- BOWLING METRICS FOR ELIGIBLE INDIANS ---")
bowl_el = bowlers[bowlers['bowler_id'].isin(eligible_indians)]
print(bowl_el[['bowler_id', 'bowler_name', 'total_balls', 'press_balls', 'press_wickets', 'econ_press', 'econ_delta', 'bnd_conceded_pct_press', 'rci_bowl_regularized']].to_string())
