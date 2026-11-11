import pandas as pd

bbb = pd.read_csv(r'D:\6af3166e7b922_data_pack\ball_by_ball.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
parq = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')[['match_id', 'innings', 'overid', 'over_ball_num', 'is_high_pressure']]

bbb = bbb.merge(parq, on=['match_id', 'innings', 'overid', 'over_ball_num'], how='left')
bbb['is_high_pressure'] = bbb['is_high_pressure'].fillna(False)
bbb['over_num'] = bbb['overid'] + 1
bbb['phase'] = pd.cut(bbb['over_num'], bins=[0, 6, 15, 20], labels=['Powerplay (1-6)', 'Middle (7-15)', 'Death (16-20)'])
bbb['is_boundary'] = bbb['is_four'] | bbb['is_six']
bbb['is_dot'] = (bbb['runs'] == 0) & (bbb['extras1_runs'] == 6)

def analyze_batter(pid, name):
    df = bbb[bbb['striker_id'] == pid].copy()
    print(f"\n=================== BATTER: {name} (ID: {pid}) ===================")
    print(f"Total Balls Faced: {len(df)}, Runs: {df['runs'].sum()}, 4s: {df['is_four'].sum()}, 6s: {df['is_six'].sum()}, Wickets: {df['is_wicket'].sum()}")
    agg = df.groupby(['phase', 'is_high_pressure']).agg(
        balls=('match_id', 'count'),
        runs=('runs', 'sum'),
        dots=('is_dot', 'sum'),
        boundaries=('is_boundary', 'sum'),
        sixes=('is_six', 'sum'),
        dismissals=('is_wicket', 'sum')
    ).reset_index()
    agg['sr'] = (agg['runs'] / agg['balls']) * 100
    agg['bnd_pct'] = (agg['boundaries'] / agg['balls']) * 100
    agg['dot_pct'] = (agg['dots'] / agg['balls']) * 100
    print(agg.to_string())

def analyze_bowler(pid, name):
    df = bbb[bbb['bowler_id'] == pid].copy()
    df['runs_conceded'] = df['runs'] + df['extras_2_runs'].fillna(0)
    df['is_bowler_wkt'] = df['is_wicket'] & (~df['dismissal_type'].astype(str).str.contains('run out', case=False, na=False))
    print(f"\n=================== BOWLER: {name} (ID: {pid}) ===================")
    print(f"Total Balls Bowled: {len(df)}, Runs Conceded: {df['runs_conceded'].sum()}, Wickets: {df['is_bowler_wkt'].sum()}")
    agg = df.groupby(['phase', 'is_high_pressure']).agg(
        balls=('match_id', 'count'),
        runs_conceded=('runs_conceded', 'sum'),
        dots=('is_dot', 'sum'),
        boundaries=('is_boundary', 'sum'),
        wickets=('is_bowler_wkt', 'sum')
    ).reset_index()
    agg['econ'] = (agg['runs_conceded'] / agg['balls']) * 6
    agg['bnd_pct'] = (agg['boundaries'] / agg['balls']) * 100
    agg['dot_pct'] = (agg['dots'] / agg['balls']) * 100
    print(agg.to_string())

analyze_batter(5029, "Prerak Mankad")
analyze_batter(6671, "Lalit Yadav")
analyze_bowler(8632, "Aaqib Khan")
analyze_bowler(2852, "Jagadeesha Suchith")
analyze_bowler(27959, "Hrithik Shokeen")
