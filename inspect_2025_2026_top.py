import pandas as pd

bbb = pd.read_csv(r'D:\6af3166e7b922_data_pack\ball_by_ball.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
parq = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')[['match_id', 'innings', 'overid', 'over_ball_num', 'is_high_pressure']]

bbb = bbb.merge(parq, on=['match_id', 'innings', 'overid', 'over_ball_num'], how='left')
bbb = bbb.merge(matches[['match_id', 'comp_id']], on='match_id').merge(comps[['comp_id', 'comp_name', 'season']], on='comp_id')
bbb['is_high_pressure'] = bbb['is_high_pressure'].fillna(False)

# 2025-2026 ONLY
bbb_recent = bbb[bbb['season'].isin(['2025', '2026', 2025, 2026, '2025/26'])].copy()

# Exclude 2025 & 2026 IPL and RR
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'].tolist()
ipl_recent_pids = set(df_map[df_map['comp_id'].isin(ipl_comps) & df_map['comp_id'].isin(comps[comps['season'].isin(['2025', '2026', 2025, 2026])]['comp_id'])]['player_id'].unique())
rr_pids = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

# Batting
bbb_recent['is_boundary'] = bbb_recent['is_four'] | bbb_recent['is_six']
bbb_recent['is_dot'] = (bbb_recent['runs'] == 0) & (bbb_recent['extras1_runs'] == 6)

bat_press = bbb_recent[bbb_recent['is_high_pressure']].groupby(['striker_id', 'striker_name']).agg(
    balls=('match_id', 'count'),
    runs=('runs', 'sum'),
    boundaries=('is_boundary', 'sum'),
    sixes=('is_six', 'sum'),
    dots=('is_dot', 'sum'),
    dismissals=('is_wicket', 'sum')
).reset_index()

bat_press['sr'] = (bat_press['runs'] / bat_press['balls']) * 100
bat_press['bnd_pct'] = (bat_press['boundaries'] / bat_press['balls']) * 100
bat_press['dot_pct'] = (bat_press['dots'] / bat_press['balls']) * 100

# Filter available
bat_avail = bat_press[~bat_press['striker_id'].isin(ipl_recent_pids) & ~bat_press['striker_id'].isin(rr_pids)].copy()

# Add team mappings
player_teams = df_map.groupby('player_id')['team_name'].apply(lambda x: ", ".join(set(x))).to_dict()
bat_avail['teams'] = bat_avail['striker_id'].map(player_teams)

# Exclude Pakistani players (due to IPL geopolitical auction ineligibility)
pak_pids = set(df_map[df_map['team_name'].isin(['Pakistan', 'Pakistan A'])]['player_id'].unique())
bat_avail_nonpak = bat_avail[~bat_avail['striker_id'].isin(pak_pids)]

print("\n--- TOP BATTERS UNDER PRESSURE IN 2025-2026 (Min 15 pressure balls, non-Pak, non-IPL 25/26) ---")
print(bat_avail_nonpak[bat_avail_nonpak['balls'] >= 15].sort_values(by='sr', ascending=False).head(25).to_string())

# Bowling
bbb_recent['runs_conceded'] = bbb_recent['runs'] + bbb_recent['extras_2_runs'].fillna(0)
bbb_recent['is_bowler_wkt'] = bbb_recent['is_wicket'] & (~bbb_recent['dismissal_type'].astype(str).str.contains('run out', case=False, na=False))

bowl_press = bbb_recent[bbb_recent['is_high_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    balls=('match_id', 'count'),
    runs=('runs_conceded', 'sum'),
    wickets=('is_bowler_wkt', 'sum'),
    boundaries=('is_boundary', 'sum'),
    dots=('is_dot', 'sum')
).reset_index()

bowl_press['econ'] = (bowl_press['runs'] / bowl_press['balls']) * 6
bowl_press['bnd_pct'] = (bowl_press['boundaries'] / bowl_press['balls']) * 100
bowl_press['dot_pct'] = (bowl_press['dots'] / bowl_press['balls']) * 100

bowl_avail = bowl_press[~bowl_press['bowler_id'].isin(ipl_recent_pids) & ~bowl_press['bowler_id'].isin(rr_pids)].copy()
bowl_avail['teams'] = bowl_avail['bowler_id'].map(player_teams)
bowl_avail_nonpak = bowl_avail[~bowl_avail['bowler_id'].isin(pak_pids)]

print("\n--- TOP BOWLERS UNDER PRESSURE IN 2025-2026 (Min 15 pressure balls, non-Pak, non-IPL 25/26) ---")
print(bowl_avail_nonpak[bowl_avail_nonpak['balls'] >= 15].sort_values(by='econ', ascending=True).head(25).to_string())
