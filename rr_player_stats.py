import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')

# Merge match metadata
bbb_m = bbb.merge(matches[['match_id', 'comp_id', 'knock_out', 'win_team_id']], on='match_id')
bbb_m = bbb_m.merge(comp[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id')

# Check RR matches specifically
rr_bbb = bbb_m[(bbb_m['batting_team_id'] == 3) | (bbb_m['bowling_team_id'] == 3)]

print(f"Total balls in dataset: {len(bbb_m)}")
print(f"Total balls in RR matches: {len(rr_bbb)}")

# Batting breakdown for RR players
rr_bat = bbb_m[bbb_m['batting_team_id'] == 3]
rr_bat_stats = rr_bat.groupby('striker_name').agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    fours=('is_four', 'sum'),
    sixes=('is_six', 'sum'),
    dismissals=('is_wicket', 'sum')
).reset_index()
rr_bat_stats['strike_rate'] = (rr_bat_stats['runs'] / rr_bat_stats['balls']) * 100
rr_bat_stats['average'] = rr_bat_stats['runs'] / rr_bat_stats['dismissals'].replace(0, np.nan)
rr_bat_stats = rr_bat_stats.sort_values('runs', ascending=False)
print("\nTop Run Scorers for RR in IPL (2022-2026):")
print(rr_bat_stats.head(10).to_string(index=False))

# Bowling breakdown for RR players
rr_bowl = bbb_m[bbb_m['bowling_team_id'] == 3]
rr_bowl_stats = rr_bowl.groupby('bowler_name').agg(
    balls=('runs', 'count'),
    runs_conceded=('runs', 'sum'),
    wickets=('is_wicket', 'sum')
).reset_index()
rr_bowl_stats['economy'] = (rr_bowl_stats['runs_conceded'] / (rr_bowl_stats['balls'] / 6))
rr_bowl_stats['strike_rate'] = rr_bowl_stats['balls'] / rr_bowl_stats['wickets'].replace(0, np.nan)
rr_bowl_stats = rr_bowl_stats.sort_values('wickets', ascending=False)
print("\nTop Wicket Takers for RR in IPL (2022-2026):")
print(rr_bowl_stats.head(10).to_string(index=False))
