import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'

print("Loading all datasets from:", data_dir)
bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
matches = pd.read_csv(os.path.join(data_dir, 'matches.csv'))
comp = pd.read_csv(os.path.join(data_dir, 'competitions.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))
p11 = pd.read_csv(os.path.join(data_dir, 'playing_eleven.csv'))
teams = pd.read_csv(os.path.join(data_dir, 'teams.csv'))

print("All datasets loaded successfully.")

# 1. Merge match and competition metadata into ball_by_ball
bbb = bbb.merge(matches[['match_id', 'comp_id', 'stage', 'knock_out', 'win_team_id', 'venue_id', 'revised_target']], on='match_id')
bbb = bbb.merge(comp[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id')

# 2. Sort chronologically
bbb = bbb.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# 3. Identify legal balls and extras
bbb['is_extra_ball'] = bbb['extras_type'].isin(['wide', 'Overstep'])
bbb['legal_ball'] = (~bbb['is_extra_ball']).astype(int)

# Total runs on delivery: batter runs + any extras
# In bbb, 'runs' is batter runs. Let's see if extra runs exist:
# When wide or no ball, wide is 1 run extra, no ball is 1 run extra
bbb['total_ball_runs'] = bbb['runs']
# Add 1 run for wides or no-balls if not already in runs
# We verified earlier that wides have runs=0, and add 1 run to team total
bbb['extra_run_value'] = np.where(bbb['extras_type'].isin(['wide', 'Overstep', 'byes', 'legbyes']), 1, 0)
# Plus any additional runs on extras_2_runs
bbb['total_ball_runs'] += bbb['extras_2_runs'] + np.where(bbb['extras_type'].isin(['wide', 'Overstep']), 1, 0)

# Cumulative match state
bbb['cum_runs'] = bbb.groupby(['match_id', 'innings'])['runs'].cumsum()
bbb['cum_wickets'] = bbb.groupby(['match_id', 'innings'])['is_wicket'].cumsum()
bbb['legal_balls_bowled'] = bbb.groupby(['match_id', 'innings'])['legal_ball'].cumsum()

# First innings totals to determine Target for Innings 2
inn1_totals = bbb[bbb['innings'] == 1].groupby('match_id')['cum_runs'].last().reset_index()
inn1_totals.columns = ['match_id', 'inn1_runs']
inn1_totals['target'] = inn1_totals['inn1_runs'] + 1

bbb = bbb.merge(inn1_totals[['match_id', 'target']], on='match_id', how='left')
# Use revised_target if present in matches.csv
bbb['target'] = np.where(bbb['revised_target'].notna() & (bbb['revised_target'] > 0), bbb['revised_target'], bbb['target'])

# Second innings chasing metrics
bbb['balls_remaining'] = np.where(bbb['innings'] == 2, np.maximum(0, 120 - bbb['legal_balls_bowled']), 120 - bbb['legal_balls_bowled'])
bbb['runs_required'] = np.where(bbb['innings'] == 2, np.maximum(0, bbb['target'] - bbb['cum_runs']), np.nan)
bbb['rrr'] = np.where((bbb['innings'] == 2) & (bbb['balls_remaining'] > 0), (bbb['runs_required'] / bbb['balls_remaining']) * 6, np.nan)
bbb['wickets_in_hand'] = 10 - bbb['cum_wickets']

# 4. Rigorous Pressure Definition:
# Factor 1: Chase Pressure (Innings 2, balls_remaining <= 60, and RRR >= 9.5 or (RRR >= 8.5 with <= 5 wickets in hand))
cond_chase = (bbb['innings'] == 2) & (bbb['balls_remaining'] <= 60) & ((bbb['rrr'] >= 9.5) | ((bbb['rrr'] >= 8.5) & (bbb['wickets_in_hand'] <= 5)))

# Factor 2: Death Overs (Overs 16-20)
cond_death = (bbb['overid'] >= 16)

# Factor 3: Crisis / Top-Order Collapse (Overs 1-10 with 4+ wickets lost, i.e. wickets_in_hand <= 6)
cond_collapse = (bbb['overid'] <= 10) & (bbb['wickets_in_hand'] <= 6)

bbb['is_high_pressure'] = cond_chase | cond_death | cond_collapse

# Knockout weight multiplier
bbb['pressure_weight'] = np.where(bbb['knock_out'] == True, 1.25, 1.0)

print(f"Total deliveries processed: {len(bbb)}")
print(f"High pressure deliveries: {bbb['is_high_pressure'].sum()} ({bbb['is_high_pressure'].mean()*100:.2f}%)")
print(f"  - Chase pressure balls: {cond_chase.sum()}")
print(f"  - Death overs balls: {cond_death.sum()}")
print(f"  - Crisis collapse balls: {cond_collapse.sum()}")

# Export processed delivery summary
bbb[['match_id', 'innings', 'overid', 'over_ball_num', 'striker_name', 'bowler_name', 'runs', 'is_wicket', 'is_high_pressure', 'pressure_weight']].to_parquet(
    os.path.join(data_dir, 'processed_pressure_deliveries.parquet'), index=False
)
print("Saved processed pressure deliveries to parquet.")
