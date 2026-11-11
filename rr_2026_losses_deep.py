import pandas as pd
import numpy as np

matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')
bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')

merged = matches.merge(comp, on='comp_id')
team_map = dict(zip(teams['team_id'], teams['team_name']))

rr_2026_losses = merged[(merged['season'] == '2026') & (merged['match_format'] == 'T20') & 
                        ((merged['home_team_id'] == 3) | (merged['away_team_id'] == 3)) & 
                        (merged['win_team_id'] != 3)].copy()

rr_2026_losses['opp_team'] = rr_2026_losses.apply(lambda r: team_map.get(r['away_team_id'] if r['home_team_id'] == 3 else r['home_team_id'], 'Unknown'), axis=1)

print("=== RR LOSSES IN IPL 2026 (DETAILED BREAKDOWN) ===")
for idx, r in rr_2026_losses.iterrows():
    m_id = r['match_id']
    m_bbb = bbb[bbb['match_id'] == m_id]
    
    # 1st inn and 2nd inn totals
    inn1 = m_bbb[m_bbb['innings'] == 1]
    inn2 = m_bbb[m_bbb['innings'] == 2]
    
    inn1_runs = inn1['runs'].sum() + inn1['extras1_runs'].sum() + inn1['extras_2_runs'].sum()
    inn1_wkts = inn1['is_wicket'].sum()
    inn1_bat = team_map.get(inn1['batting_team_id'].iloc[0], 'Unknown')
    
    inn2_runs = inn2['runs'].sum() + inn2['extras1_runs'].sum() + inn2['extras_2_runs'].sum()
    inn2_wkts = inn2['is_wicket'].sum()
    inn2_bat = team_map.get(inn2['batting_team_id'].iloc[0], 'Unknown')
    
    print(f"\nMatch {r['match_number']} ({r['stage']}): vs {r['opp_team']}")
    print(f"  Result: {r['result']}")
    print(f"  Inn 1: {inn1_bat} {inn1_runs}/{inn1_wkts} in {len(inn1)} balls")
    print(f"  Inn 2: {inn2_bat} {inn2_runs}/{inn2_wkts} in {len(inn2)} balls")
    
    # Identify phase breakdown in this loss
    inn_rr = inn1 if inn1['batting_team_id'].iloc[0] == 3 else inn2
    inn_opp = inn2 if inn1['batting_team_id'].iloc[0] == 3 else inn1
    
    # RR Death Batting or Bowling
    rr_death_bat = inn_rr[inn_rr['overid'] >= 16]
    rr_death_bowl = inn_opp[inn_opp['overid'] >= 16]
    print(f"  RR Death Batting (Overs 16-20): {rr_death_bat['runs'].sum()} runs, {rr_death_bat['is_wicket'].sum()} wkts off {len(rr_death_bat)} balls")
    print(f"  Opp Death Batting (Overs 16-20): {rr_death_bowl['runs'].sum()} runs, {rr_death_bowl['is_wicket'].sum()} wkts off {len(rr_death_bowl)} balls")
