import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Find all Indian players who have played for India A or India or are in domestic
india_pids = df_map[df_map['team_name'].isin(['India', 'India A'])]['player_id'].unique()

# Check their IPL 2026 status
ipl_2026_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
ipl_2026_pids = set(df_map[df_map['comp_id'].isin(ipl_2026_comps)]['player_id'].unique())
rr_pids = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

print("=== INDIAN BATTERS NOT IN IPL 2026 SQUADS & NOT IN RR ===")
ind_bat = batters[batters['striker_id'].isin(india_pids) & ~batters['striker_id'].isin(ipl_2026_pids) & ~batters['striker_id'].isin(rr_pids)]
print(ind_bat[['striker_id', 'striker_name', 'total_balls', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'rci_bat_regularized']].to_string())

print("\n=== INDIAN BOWLERS NOT IN IPL 2026 SQUADS & NOT IN RR ===")
ind_bowl = bowlers[bowlers['bowler_id'].isin(india_pids) & ~bowlers['bowler_id'].isin(ipl_2026_pids) & ~bowlers['bowler_id'].isin(rr_pids)]
print(ind_bowl[['bowler_id', 'bowler_name', 'total_balls', 'press_balls', 'press_wickets', 'econ_press', 'econ_delta', 'bnd_conceded_pct_press', 'rci_bowl_regularized']].to_string())
