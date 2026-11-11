import pandas as pd

bbb = pd.read_csv(r'D:\6af3166e7b922_data_pack\ball_by_ball.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
parq = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')[['match_id', 'innings', 'overid', 'over_ball_num', 'is_high_pressure']]

# Merge to get season
bbb = bbb.merge(parq, on=['match_id', 'innings', 'overid', 'over_ball_num'], how='left')
bbb = bbb.merge(matches[['match_id', 'comp_id']], on='match_id').merge(comps[['comp_id', 'comp_name', 'season']], on='comp_id')

bbb['is_high_pressure'] = bbb['is_high_pressure'].fillna(False)

# Filter STRICTLY for 2025 and 2026 deliveries!
bbb_recent = bbb[bbb['season'].isin(['2025', '2026', 2025, 2026, '2025/26'])].copy()
print(f"Total deliveries in 2025-2026 seasons: {len(bbb_recent)}")

# Exclude 2025 & 2026 IPL squad players and RR
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
named_ipl_recent = set(df_map[df_map['comp_id'].isin(ipl_comps) & df_map['comp_id'].isin(comps[comps['season'].isin(['2025', '2026', 2025, 2026])]['comp_id'])]['player_id'].unique())
rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

# Batting metrics in 2025-2026 under pressure
bbb_recent['is_boundary'] = bbb_recent['is_four'] | bbb_recent['is_six']
bbb_recent['is_dot'] = (bbb_recent['runs'] == 0) & (bbb_recent['extras1_runs'] == 6)

bat_recent = bbb_recent.groupby(['striker_id', 'striker_name', 'is_high_pressure']).agg(
    balls=('match_id', 'count'),
    runs=('runs', 'sum'),
    dots=('is_dot', 'sum'),
    boundaries=('is_boundary', 'sum'),
    sixes=('is_six', 'sum'),
    dismissals=('is_wicket', 'sum')
).unstack(fill_value=0)

# Filter for available players
avail_bat_ids = set(bat_recent.index.get_level_values(0)) - named_ipl_recent - rr_players

print(f"Available batters with 2025-2026 deliveries: {len(avail_bat_ids)}")

# Bowling metrics in 2025-2026 under pressure
bbb_recent['runs_conceded'] = bbb_recent['runs'] + bbb_recent['extras_2_runs'].fillna(0)
bbb_recent['is_bowler_wkt'] = bbb_recent['is_wicket'] & (~bbb_recent['dismissal_type'].astype(str).str.contains('run out', case=False, na=False))

bowl_recent = bbb_recent.groupby(['bowler_id', 'bowler_name', 'is_high_pressure']).agg(
    balls=('match_id', 'count'),
    runs=('runs_conceded', 'sum'),
    dots=('is_dot', 'sum'),
    boundaries=('is_boundary', 'sum'),
    wickets=('is_bowler_wkt', 'sum')
).unstack(fill_value=0)

avail_bowl_ids = set(bowl_recent.index.get_level_values(0)) - named_ipl_recent - rr_players
print(f"Available bowlers with 2025-2026 deliveries: {len(avail_bowl_ids)}")
