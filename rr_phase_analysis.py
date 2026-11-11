import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')

bbb_m = bbb.merge(matches[['match_id', 'comp_id', 'knock_out', 'win_team_id', 'match_number', 'stage', 'result']], on='match_id')
bbb_m = bbb_m.merge(comp[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id')

# Look at 2025 and 2026 RR matches
rr_25_26 = bbb_m[(bbb_m['season'].isin(['2025', '2026'])) & ((bbb_m['batting_team_id'] == 3) | (bbb_m['bowling_team_id'] == 3))]

# Define match phase: Powerplay (overs 1-6), Middle (7-15), Death (16-20)
# Note: overid in bbb is 1-indexed (1 to 20)
def get_phase(overid):
    if overid <= 6:
        return 'Powerplay (1-6)'
    elif overid <= 15:
        return 'Middle (7-15)'
    else:
        return 'Death (16-20)'

bbb_m['phase'] = bbb_m['overid'].apply(get_phase)

# RR Batting vs Opponent Batting in 2025 and 2026
rr_bat = bbb_m[(bbb_m['season'].isin(['2025', '2026'])) & (bbb_m['batting_team_id'] == 3)]
rr_bowl = bbb_m[(bbb_m['season'].isin(['2025', '2026'])) & (bbb_m['bowling_team_id'] == 3)]

print("=== RR BATTING BY PHASE (2025-2026) ===")
bat_phase = rr_bat.groupby('phase').agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    wickets=('is_wicket', 'sum'),
    fours=('is_four', 'sum'),
    sixes=('is_six', 'sum')
).reset_index()
bat_phase['strike_rate'] = (bat_phase['runs'] / bat_phase['balls']) * 100
bat_phase['balls_per_wicket'] = bat_phase['balls'] / bat_phase['wickets']
print(bat_phase.to_string(index=False))

print("\n=== RR BOWLING CONCEDED BY PHASE (2025-2026) ===")
bowl_phase = rr_bowl.groupby('phase').agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    wickets=('is_wicket', 'sum'),
    fours=('is_four', 'sum'),
    sixes=('is_six', 'sum')
).reset_index()
bowl_phase['economy'] = (bowl_phase['runs'] / (bowl_phase['balls'] / 6))
bowl_phase['strike_rate'] = bowl_phase['balls'] / bowl_phase['wickets']
print(bowl_phase.to_string(index=False))
