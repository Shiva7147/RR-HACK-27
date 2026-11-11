import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
mapping = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competition_team_player_mapping.csv')
from pressure_engine import bbb as bbb_press

# Filter for IPL Auction Eligible Domestic / Emerging Players
# Exclude Pakistani players as they are not eligible for IPL auction
pak_teams = mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique()

# Let's inspect all domestic Indian / Emerging players (min 50 pressure balls)
bat_overall = bbb_press.groupby(['striker_id', 'striker_name']).agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    dots=('runs', lambda x: (x == 0).sum()),
    boundaries=('runs', lambda x: (x.isin([4, 6])).sum()),
    dismissals=('is_wicket', 'sum')
).reset_index()
bat_overall['sr_base'] = (bat_overall['runs'] / bat_overall['balls']) * 100

bat_press = bbb_press[bbb_press['is_high_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries=('runs', lambda x: (x.isin([4, 6])).sum()),
    press_dismissals=('is_wicket', 'sum')
).reset_index()
bat_press['sr_press'] = (bat_press['press_runs'] / bat_press['press_balls']) * 100
bat_press['boundary_pct_press'] = (bat_press['press_boundaries'] / bat_press['press_balls']) * 100
bat_press['dot_pct_press'] = (bat_press['press_dots'] / bat_press['press_balls']) * 100

batters = bat_overall.merge(bat_press, on=['striker_id', 'striker_name'])
batters['sr_delta'] = batters['sr_press'] - batters['sr_base']

# Clutch Batting Score
batters['clutch_bat_score'] = (
    0.40 * (batters['sr_press'] / 150.0 * 100) + 
    0.30 * (batters['boundary_pct_press'] / 20.0 * 100) + 
    0.20 * ((50 - batters['dot_pct_press']) / 20.0 * 100) + 
    0.10 * (np.clip(batters['sr_delta'], -20, 40) / 20.0 * 100)
)

# Eligible emerging/domestic batters
emerging_comps = [2670, 3289]
emerging_players = mapping[mapping['comp_id'].isin(emerging_comps)]['player_name'].unique()
uncapped_domestic = mapping[~mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique()

dom_bat = batters[(batters['press_balls'] >= 50) & 
                  (~batters['striker_name'].isin(pak_teams)) & 
                  (batters['striker_name'].isin(emerging_players) | batters['striker_name'].isin(mapping[mapping['team_name'] == 'India A']['player_name']))].copy()

dom_bat = dom_bat.sort_values('clutch_bat_score', ascending=False)
print("=== TOP EMERGING & DOMESTIC BATTERS UNDER PRESSURE (MIN 50 PRESSURE BALLS) ===")
cols_bat = ['striker_name', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'boundary_pct_press', 'dot_pct_press', 'clutch_bat_score']
print(dom_bat[cols_bat].head(20).to_string(index=False))

# Bowling
bowl_overall = bbb_press.groupby(['bowler_id', 'bowler_name']).agg(
    balls=('runs', 'count'),
    runs_conceded=('runs', 'sum'),
    dots=('runs', lambda x: (x == 0).sum()),
    boundaries_conceded=('runs', lambda x: (x.isin([4, 6])).sum()),
    wickets=('is_wicket', 'sum')
).reset_index()
bowl_overall['econ_base'] = (bowl_overall['runs_conceded'] / (bowl_overall['balls'] / 6))

bowl_press = bbb_press[bbb_press['is_high_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_boundaries_conceded=('runs', lambda x: (x.isin([4, 6])).sum()),
    press_wickets=('is_wicket', 'sum')
).reset_index()
bowl_press['econ_press'] = (bowl_press['press_runs'] / (bowl_press['press_balls'] / 6))
bowl_press['dot_pct_press'] = (bowl_press['press_dots'] / bowl_press['press_balls']) * 100
bowl_press['boundary_pct_conceded_press'] = (bowl_press['press_boundaries_conceded'] / bowl_press['press_balls']) * 100

bowlers = bowl_overall.merge(bowl_press, on=['bowler_id', 'bowler_name'])
bowlers['econ_delta'] = bowlers['econ_base'] - bowlers['econ_press']

bowlers['clutch_bowl_score'] = (
    0.35 * (np.maximum(0, 13.0 - bowlers['econ_press']) / 4.0 * 100) + 
    0.30 * (bowlers['dot_pct_press'] / 40.0 * 100) + 
    0.25 * ((bowlers['press_wickets'] / bowlers['press_balls'] * 6) / 0.5 * 100) + 
    0.10 * (np.clip(bowlers['econ_delta'] + 2, 0, 4) / 4.0 * 100)
)

dom_bowl = bowlers[(bowlers['press_balls'] >= 50) & 
                    (~bowlers['bowler_name'].isin(pak_teams)) & 
                    (bowlers['bowler_name'].isin(emerging_players) | bowlers['bowler_name'].isin(mapping[mapping['team_name'] == 'India A']['player_name']))].copy()

dom_bowl = dom_bowl.sort_values('clutch_bowl_score', ascending=False)
print("\n=== TOP EMERGING & DOMESTIC BOWLERS UNDER PRESSURE (MIN 50 PRESSURE BALLS) ===")
cols_bowl = ['bowler_name', 'press_balls', 'press_runs', 'econ_press', 'press_wickets', 'dot_pct_press', 'boundary_pct_conceded_press', 'clutch_bowl_score']
print(dom_bowl[cols_bowl].head(20).to_string(index=False))
