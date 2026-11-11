import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')

# Merge match metadata
bbb = bbb.merge(matches[['match_id', 'comp_id', 'knock_out', 'win_team_id']], on='match_id')
bbb = bbb.merge(comp[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id')

# Sort chronologically by match, innings, overid, over_ball_num
bbb = bbb.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# Calculate cumulative runs and wickets per innings
bbb['is_extra_ball'] = bbb['extras_type'].isin(['wide', 'Overstep'])
bbb['ball_count'] = (~bbb['is_extra_ball']).astype(int)

# Group by match_id and innings
bbb['cum_runs'] = bbb.groupby(['match_id', 'innings'])['runs'].cumsum()
bbb['cum_wickets'] = bbb.groupby(['match_id', 'innings'])['is_wicket'].cumsum()
bbb['legal_balls'] = bbb.groupby(['match_id', 'innings'])['ball_count'].cumsum()

# First innings total per match to find target for innings 2
inn1_totals = bbb[bbb['innings'] == 1].groupby('match_id')['cum_runs'].last().reset_index()
inn1_totals.rename(columns={'cum_runs': 'target'}, inplace=True)
inn1_totals['target'] += 1 # Target is runs + 1

bbb = bbb.merge(inn1_totals, on='match_id', how='left')

# Innings 2 calculations
bbb['balls_remaining'] = np.where(bbb['innings'] == 2, np.maximum(0, 120 - bbb['legal_balls']), 120 - bbb['legal_balls'])
bbb['runs_required'] = np.where(bbb['innings'] == 2, np.maximum(0, bbb['target'] - bbb['cum_runs']), np.nan)
bbb['rrr'] = np.where((bbb['innings'] == 2) & (bbb['balls_remaining'] > 0), (bbb['runs_required'] / bbb['balls_remaining']) * 6, np.nan)
bbb['wickets_in_hand'] = 10 - bbb['cum_wickets']

# Pressure classification
# Condition 1: Chasing high RRR (Innings 2, balls_remaining <= 60, rrr >= 9.5 or (rrr >= 8.5 and wickets_in_hand <= 5))
cond_chase_pressure = (bbb['innings'] == 2) & (bbb['balls_remaining'] <= 60) & ((bbb['rrr'] >= 9.5) | ((bbb['rrr'] >= 8.5) & (bbb['wickets_in_hand'] <= 5)))

# Condition 2: Death overs (Overs 16-20) in close contest (either Innings 1, or Innings 2 with rrr between 7 and 15)
cond_death_pressure = (bbb['overid'] >= 16)

# Condition 3: Top-order crisis / collapse recovery (Overs 1-10 with wickets_in_hand <= 6, i.e. 4+ wickets down early)
cond_collapse_pressure = (bbb['overid'] <= 10) & (bbb['wickets_in_hand'] <= 6)

bbb['is_high_pressure'] = cond_chase_pressure | cond_death_pressure | cond_collapse_pressure

print(f"Total deliveries: {len(bbb)}")
print(f"High pressure deliveries: {bbb['is_high_pressure'].sum()} ({bbb['is_high_pressure'].mean()*100:.2f}%)")
print(f"Breakdown of high pressure: Chase={cond_chase_pressure.sum()}, Death={cond_death_pressure.sum()}, Collapse={cond_collapse_pressure.sum()}")
