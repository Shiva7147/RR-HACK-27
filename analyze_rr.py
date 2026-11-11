import pandas as pd
import numpy as np

matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')
merged = matches.merge(comp, on='comp_id')

rr_matches = merged[(merged['home_team_id'] == 3) | (merged['away_team_id'] == 3)].copy()
rr_matches = rr_matches[rr_matches['match_format'] == 'T20'].sort_values(['season', 'match_date'])

team_map = dict(zip(teams['team_id'], teams['team_name']))
rr_matches['opp_team'] = rr_matches.apply(lambda r: team_map.get(r['away_team_id'] if r['home_team_id'] == 3 else r['home_team_id'], 'Unknown'), axis=1)
rr_matches['is_win'] = (rr_matches['win_team_id'] == 3)

print('=== RR ALL MATCHES SUMMARY BY SEASON ===')
for season, grp in rr_matches.groupby('season'):
    wins = grp['is_win'].sum()
    losses = len(grp) - wins
    print(f'\n--- Season {season}: Played {len(grp)}, Won {wins}, Lost {losses} (Win Rate: {wins/len(grp)*100:.1f}%) ---')
    print('Losses:')
    for idx, r in grp[~grp['is_win']].iterrows():
        ko_str = ' [KNOCKOUT]' if r['knock_out'] else ''
        print(f"  Match {r['match_number']} ({r['stage']}{ko_str}): vs {r['opp_team']} -> {r['result']}")
