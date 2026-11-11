import pandas as pd
import numpy as np

matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')
bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')

merged = matches.merge(comp, on='comp_id')
team_map = dict(zip(teams['team_id'], teams['team_name']))

# Find IPL finals in 2022, 2023, 2024, 2025, 2026
ipl_matches = merged[merged['match_format'] == 'T20'].copy()
finals = ipl_matches[ipl_matches['stage'].str.contains('Final', case=False, na=False)]
print("=== IPL CHAMPIONS (FINALS) 2022-2026 ===")
for idx, r in finals.sort_values('season').iterrows():
    winner = team_map.get(r['win_team_id'], f"Team {r['win_team_id']}")
    print(f"Season {r['season']}: Winner = {winner} | Match: {r['home_team']} vs {r['away_team']} | Result: {r['result']}")
