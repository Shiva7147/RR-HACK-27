import pandas as pd
import numpy as np

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')

merged = bbb.merge(matches[['match_id', 'comp_id']], on='match_id')
merged = merged.merge(comp[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id')
ipl = merged[merged['comp_name'].str.contains('IPL', case=False, na=False)]

print("=== IPL ORANGE & PURPLE CAP LEADERS PER SEASON IN DATASET ===")
for season in sorted(ipl['season'].unique()):
    s_df = ipl[ipl['season'] == season]
    
    # Top run getter
    bat = s_df.groupby('striker_name')['runs'].sum().reset_index().sort_values('runs', ascending=False).iloc[0]
    
    # Top wicket taker
    bowl = s_df.groupby('bowler_name')['is_wicket'].sum().reset_index().sort_values('is_wicket', ascending=False).iloc[0]
    
    # RR top run getter and wicket taker
    rr_bat_df = s_df[s_df['batting_team_id'] == 3].groupby('striker_name')['runs'].sum().reset_index().sort_values('runs', ascending=False)
    rr_bat = rr_bat_df.iloc[0] if len(rr_bat_df) > 0 else None
    
    rr_bowl_df = s_df[s_df['bowling_team_id'] == 3].groupby('bowler_name')['is_wicket'].sum().reset_index().sort_values('is_wicket', ascending=False)
    rr_bowl = rr_bowl_df.iloc[0] if len(rr_bowl_df) > 0 else None
    
    print(f"\n--- Season {season} ---")
    print(f"  Orange Cap: {bat['striker_name']} ({bat['runs']} runs)")
    print(f"  Purple Cap: {bowl['bowler_name']} ({bowl['is_wicket']} wickets)")
    if rr_bat is not None:
        print(f"  RR Top Batter: {rr_bat['striker_name']} ({rr_bat['runs']} runs)")
    if rr_bowl is not None:
        print(f"  RR Top Bowler: {rr_bowl['bowler_name']} ({rr_bowl['is_wicket']} wickets)")
