import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')

merged_m = matches.merge(comp, on='comp_id')
team_map = dict(zip(teams['team_id'], teams['team_name']))

# Filter to IPL 2025 and IPL 2026
ipl_25_26_m = merged_m[(merged_m['season'].isin(['2025', '2026'])) & (merged_m['comp_name'].str.contains('IPL', case=False, na=False))]
m_ids = ipl_25_26_m['match_id'].unique()

bbb_ipl = bbb[bbb['match_id'].isin(m_ids)].merge(ipl_25_26_m[['match_id', 'season', 'win_team_id', 'knock_out']], on='match_id')

def get_phase(overid):
    if overid <= 6:
        return 'Powerplay'
    elif overid <= 15:
        return 'Middle'
    else:
        return 'Death'

bbb_ipl['phase'] = bbb_ipl['overid'].apply(get_phase)

# Let's compare Rajasthan Royals (team_id=3) vs Champions (RCB team_id=1 in 2025/2026, KKR team_id=2 in 2024, etc.)
# Let's check team IDs
print("Teams in IPL 2025-2026:")
ipl_teams = bbb_ipl[['batting_team_id']].drop_duplicates()
ipl_teams['team_name'] = ipl_teams['batting_team_id'].map(team_map)
print(ipl_teams)

# Phase breakdown for every team in IPL 2025-2026
bat_summary = bbb_ipl.groupby(['batting_team_id', 'phase']).agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    wickets=('is_wicket', 'sum'),
    boundaries=('runs', lambda x: x.isin([4, 6]).sum()),
    dots=('runs', lambda x: (x == 0).sum())
).reset_index()
bat_summary['team_name'] = bat_summary['batting_team_id'].map(team_map)
bat_summary['strike_rate'] = (bat_summary['runs'] / bat_summary['balls']) * 100
bat_summary['boundary_pct'] = (bat_summary['boundaries'] / bat_summary['balls']) * 100
bat_summary['dot_pct'] = (bat_summary['dots'] / bat_summary['balls']) * 100
bat_summary['balls_per_wicket'] = bat_summary['balls'] / bat_summary['wickets']

bowl_summary = bbb_ipl.groupby(['bowling_team_id', 'phase']).agg(
    balls=('runs', 'count'),
    runs=('runs', 'sum'),
    wickets=('is_wicket', 'sum'),
    boundaries=('runs', lambda x: x.isin([4, 6]).sum()),
    dots=('runs', lambda x: (x == 0).sum())
).reset_index()
bowl_summary['team_name'] = bowl_summary['bowling_team_id'].map(team_map)
bowl_summary['economy'] = (bowl_summary['runs'] / (bowl_summary['balls'] / 6))
bowl_summary['boundary_conceded_pct'] = (bowl_summary['boundaries'] / bowl_summary['balls']) * 100
bowl_summary['dot_pct'] = (bowl_summary['dots'] / bowl_summary['balls']) * 100
bowl_summary['balls_per_wicket'] = bowl_summary['balls'] / bowl_summary['wickets']

# Focus on Death phase (Overs 16-20)
print("\n=== DEATH OVERS (16-20) BATTING COMPARISON (IPL 2025-2026) ===")
death_bat = bat_summary[bat_summary['phase'] == 'Death'].sort_values('strike_rate', ascending=False)
print(death_bat[['team_name', 'balls', 'runs', 'strike_rate', 'boundary_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))

print("\n=== DEATH OVERS (16-20) BOWLING COMPARISON (IPL 2025-2026) ===")
death_bowl = bowl_summary[bowl_summary['phase'] == 'Death'].sort_values('economy', ascending=True)
print(death_bowl[['team_name', 'balls', 'economy', 'boundary_conceded_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))
