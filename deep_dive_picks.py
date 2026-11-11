import pandas as pd
import numpy as np

bbb = pd.read_parquet(r'D:\6af3166e7b922_data_pack\processed_pressure_deliveries.parquet')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')

# Merge competition info
bbb = bbb.merge(matches[['match_id', 'comp_id']], on='match_id').merge(comps[['comp_id', 'comp_name', 'season']], on='comp_id')

# Analysis for Sediqullah Atal (8647)
atal = bbb[bbb['striker_id'] == 8647]
print(f"Sediqullah Atal total balls: {len(atal)}")
print(f"Total runs: {atal['runs'].sum()}, Dismissals: {atal['is_dismissal'].sum()}")

# Phase breakdown
atal['phase'] = pd.cut(atal['over_number'], bins=[-1, 5, 14, 20], labels=['Powerplay (1-6)', 'Middle (7-15)', 'Death (16-20)'])
phase_summary = atal.groupby(['phase', 'is_pressure']).agg(
    balls=('ball_id', 'count'),
    runs=('runs', 'sum'),
    boundaries=('is_boundary', 'sum'),
    sixes=('is_six', 'sum'),
    fours=('is_four', 'sum'),
    dots=('is_dot', 'sum'),
    dismissals=('is_dismissal', 'sum')
).reset_index()
phase_summary['sr'] = (phase_summary['runs'] / phase_summary['balls']) * 100
phase_summary['bnd_pct'] = (phase_summary['boundaries'] / phase_summary['balls']) * 100
phase_summary['dot_pct'] = (phase_summary['dots'] / phase_summary['balls']) * 100
print("\n--- Sediqullah Atal Phase & Pressure Breakdown ---")
print(phase_summary.to_string())

# Analysis for Pramod Madushan (6932)
madushan = bbb[bbb['bowler_id'] == 6932]
print(f"\nPramod Madushan total balls bowled: {len(madushan)}")
print(f"Total runs conceded: {madushan['runs_conceded_bowler'].sum()}, Wickets: {madushan['is_bowler_wicket'].sum()}")

madushan['phase'] = pd.cut(madushan['over_number'], bins=[-1, 5, 14, 20], labels=['Powerplay (1-6)', 'Middle (7-15)', 'Death (16-20)'])
m_phase = madushan.groupby(['phase', 'is_pressure']).agg(
    balls=('ball_id', 'count'),
    runs_conceded=('runs_conceded_bowler', 'sum'),
    wickets=('is_bowler_wicket', 'sum'),
    boundaries=('is_boundary', 'sum'),
    dots=('is_dot', 'sum')
).reset_index()
m_phase['econ'] = (m_phase['runs_conceded'] / m_phase['balls']) * 6
m_phase['bnd_pct'] = (m_phase['boundaries'] / m_phase['balls']) * 100
m_phase['dot_pct'] = (m_phase['dots'] / m_phase['balls']) * 100
print("\n--- Pramod Madushan Phase & Pressure Breakdown ---")
print(m_phase.to_string())
