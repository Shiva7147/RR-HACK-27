import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))

bbb_m = bbb.merge(matches[['match_id', 'comp_id', 'knock_out', 'stage']], on='match_id')
bbb_m = bbb_m.merge(comp[['comp_id', 'comp_name', 'season']], on='comp_id')

from process_entire_datapack import cond_chase, cond_death, cond_collapse
bbb_m['is_high_pressure'] = cond_chase | cond_death | cond_collapse

# 1. Detailed analysis of Sediqullah Atal
atal_b = bbb_m[bbb_m['striker_name'] == 'Sediqullah Atal']
print(f"=== SEDIQULLAH ATAL DELIVERY-LEVEL AUDIT ===")
print(f"Total balls faced in dataset: {len(atal_b)}")
print(f"Total runs scored: {atal_b['runs'].sum()}")
print(f"Overall Strike Rate: {(atal_b['runs'].sum() / len(atal_b)) * 100:.2f}")

atal_press = atal_b[atal_b['is_high_pressure']]
print(f"\nHigh Pressure balls faced: {len(atal_press)}")
print(f"High Pressure runs: {atal_press['runs'].sum()}")
print(f"Pressure Strike Rate: {(atal_press['runs'].sum() / len(atal_press)) * 100:.2f}")
print(f"Pressure Boundary Count: {atal_press['runs'].isin([4, 6]).sum()} ({(atal_press['runs'].isin([4, 6]).sum() / len(atal_press)) * 100:.2f}%)")
print(f"Pressure Dot Balls: {(atal_press['runs'] == 0).sum()} ({((atal_press['runs'] == 0).sum() / len(atal_press)) * 100:.2f}%)")
print(f"Pressure Dismissals: {atal_press['is_wicket'].sum()}")
print("Competitions played in dataset:", atal_b['comp_name'].unique().tolist())

# 2. Detailed analysis of Pramod Madushan
madushan_b = bbb_m[bbb_m['bowler_name'] == 'Pramod Madushan']
print(f"\n=== PRAMOD MADUSHAN DELIVERY-LEVEL AUDIT ===")
print(f"Total balls bowled in dataset: {len(madushan_b)}")
print(f"Total runs conceded: {madushan_b['runs'].sum()}")
print(f"Overall Economy: {(madushan_b['runs'].sum() / (len(madushan_b) / 6)):.2f}")
print(f"Overall Wickets: {madushan_b['is_wicket'].sum()}")

madushan_press = madushan_b[madushan_b['is_high_pressure']]
print(f"\nHigh Pressure balls bowled: {len(madushan_press)}")
print(f"High Pressure runs conceded: {madushan_press['runs'].sum()}")
print(f"Pressure Economy: {(madushan_press['runs'].sum() / (len(madushan_press) / 6)):.2f}")
print(f"Pressure Wickets: {madushan_press['is_wicket'].sum()}")
print(f"Pressure Dot Balls: {(madushan_press['runs'] == 0).sum()} ({((madushan_press['runs'] == 0).sum() / len(madushan_press)) * 100:.2f}%)")
print(f"Pressure Boundaries Conceded: {madushan_press['runs'].isin([4, 6]).sum()} ({(madushan_press['runs'].isin([4, 6]).sum() / len(madushan_press)) * 100:.2f}%)")
print("Competitions played in dataset:", madushan_b['comp_name'].unique().tolist())
