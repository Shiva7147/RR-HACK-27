import pandas as pd

matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
rr_matches = matches[(matches['home_team_id'] == 3) | (matches['away_team_id'] == 3)].copy()
print(f"Total RR matches: {len(rr_matches)}")

# Outcomes
rr_wins = rr_matches[rr_matches['win_team_id'] == 3]
rr_losses = rr_matches[(rr_matches['win_team_id'] != 3) & (rr_matches['win_team_id'].notna())]
print(f"Total RR wins: {len(rr_wins)}")
print(f"Total RR losses: {len(rr_losses)}")

# Check close losses
print("\nRR Losses details:")
print(rr_losses[['match_id', 'match_date', 'venue_id', 'home_team', 'away_team', 'win_team_id', 'result']].to_string())

# Death bowling in bbb
bbb = pd.read_csv(r'D:\6af3166e7b922_data_pack\ball_by_ball.csv')
rr_death_bowling = bbb[(bbb['bowling_team_id'] == 3) & (bbb['overid'] >= 16)]
print(f"\nRR death deliveries bowled: {len(rr_death_bowling)}")
wickets = rr_death_bowling['is_wicket'].sum()
print(f"RR death wickets taken: {wickets}")
if wickets > 0:
    print(f"Death balls per wicket (Strike Rate): {len(rr_death_bowling)/wickets:.2f}")

# Check Saurav Chauhan (27962) 16 balls
sc_bat = bbb[bbb['striker_id'] == 27962]
print("\nSaurav Chauhan balls:")
print(sc_bat[['match_id', 'overid', 'runs_off_bat', 'extras_runs', 'is_wicket']].to_string())
