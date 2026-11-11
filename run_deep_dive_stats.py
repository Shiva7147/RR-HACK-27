import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\6af3166e7b922_data_pack\ball_by_ball.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')

# Load pressure flags
parq = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')[['match_id', 'innings', 'overid', 'over_ball_num', 'is_high_pressure', 'pressure_weight']]
bbb = bbb.merge(parq, on=['match_id', 'innings', 'overid', 'over_ball_num'], how='left')

bbb['is_high_pressure'] = bbb['is_high_pressure'].fillna(False)

# Phase
bbb['over_num'] = bbb['overid'] + 1
bbb['phase'] = pd.cut(bbb['over_num'], bins=[0, 6, 15, 20], labels=['Powerplay (1-6)', 'Middle (7-15)', 'Death (16-20)'])
bbb['is_boundary'] = bbb['is_four'] | bbb['is_six']
bbb['is_dot'] = (bbb['runs'] == 0) & (bbb['extras1_runs'] == 6) # 6 means no extra

# Filter Sediqullah Atal (8647)
atal = bbb[bbb['striker_id'] == 8647].copy()
print("=== SEDIQULLAH ATAL (8647) ===")
print(f"Total Balls: {len(atal)}, Total Runs: {atal['runs'].sum()}, Fours: {atal['is_four'].sum()}, Sixes: {atal['is_six'].sum()}")
atal_agg = atal.groupby(['phase', 'is_high_pressure']).agg(
    balls=('match_id', 'count'),
    runs=('runs', 'sum'),
    dots=('is_dot', 'sum'),
    boundaries=('is_boundary', 'sum'),
    sixes=('is_six', 'sum'),
    dismissals=('is_wicket', 'sum')
).reset_index()
atal_agg['sr'] = (atal_agg['runs'] / atal_agg['balls']) * 100
atal_agg['bnd_pct'] = (atal_agg['boundaries'] / atal_agg['balls']) * 100
atal_agg['dot_pct'] = (atal_agg['dots'] / atal_agg['balls']) * 100
print(atal_agg.to_string())

# Matchup vs Pace and Spin for Atal
print("\n--- Atal vs Pace vs Spin under Pressure ---")
atal_matchup = atal[atal['is_high_pressure']].groupby('pace_or_spin').agg(
    balls=('match_id', 'count'),
    runs=('runs', 'sum'),
    boundaries=('is_boundary', 'sum'),
    dots=('is_dot', 'sum'),
    dismissals=('is_wicket', 'sum')
).reset_index()
atal_matchup['sr'] = (atal_matchup['runs'] / atal_matchup['balls']) * 100
atal_matchup['bnd_pct'] = (atal_matchup['boundaries'] / atal_matchup['balls']) * 100
print(atal_matchup.to_string())

# Pramod Madushan (6932)
pm = bbb[bbb['bowler_id'] == 6932].copy()
# bowler runs conceded: runs + wide/noball runs
pm['runs_conceded'] = pm['runs'] + pm['extras_2_runs'].fillna(0)
# bowler wickets: exclude run outs
pm['is_bowler_wkt'] = pm['is_wicket'] & (~pm['dismissal_type'].astype(str).str.contains('run out', case=False, na=False))

print("\n=== PRAMOD MADUSHAN (6932) ===")
print(f"Total Balls: {len(pm)}, Runs Conceded: {pm['runs_conceded'].sum()}, Wickets: {pm['is_bowler_wkt'].sum()}")
pm_agg = pm.groupby(['phase', 'is_high_pressure']).agg(
    balls=('match_id', 'count'),
    runs_conceded=('runs_conceded', 'sum'),
    dots=('is_dot', 'sum'),
    boundaries=('is_boundary', 'sum'),
    wickets=('is_bowler_wkt', 'sum')
).reset_index()
pm_agg['econ'] = (pm_agg['runs_conceded'] / pm_agg['balls']) * 6
pm_agg['bnd_pct'] = (pm_agg['boundaries'] / pm_agg['balls']) * 100
pm_agg['dot_pct'] = (pm_agg['dots'] / pm_agg['balls']) * 100
print(pm_agg.to_string())

# Madushan by over range under pressure
print("\n--- Madushan Death Overs (16-20) specifically ---")
pm_death = pm[pm['phase'] == 'Death (16-20)'].groupby('is_high_pressure').agg(
    balls=('match_id', 'count'),
    runs=('runs_conceded', 'sum'),
    wickets=('is_bowler_wkt', 'sum'),
    boundaries=('is_boundary', 'sum'),
    dots=('is_dot', 'sum')
).reset_index()
pm_death['econ'] = (pm_death['runs'] / pm_death['balls']) * 6
pm_death['bnd_pct'] = (pm_death['boundaries'] / pm_death['balls']) * 100
print(pm_death.to_string())
