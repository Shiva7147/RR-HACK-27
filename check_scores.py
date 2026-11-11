import pandas as pd

bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')
matches = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\matches.csv')

print('extras_2_runs distribution:')
print(bbb['extras_2_runs'].value_counts())

for mid in matches['match_id'].head(5):
    m_info = matches[matches['match_id'] == mid].iloc[0]
    m_bbb = bbb[bbb['match_id'] == mid]
    print(f"\nMatch {mid}: {m_info['home_team']} vs {m_info['away_team']} -> {m_info['result']}")
    for inn in [1, 2]:
        inn_b = m_bbb[m_bbb['innings'] == inn]
        if len(inn_b) == 0:
            continue
        total_runs_col = inn_b['runs'].sum()
        extras_count = inn_b['extras_type'].notna().sum()
        # Check wide deliveries
        wides = inn_b[inn_b['extras_type'] == 'wide']
        noballs = inn_b[inn_b['extras_type'] == 'Overstep']
        print(f"  Inn {inn} ({inn_b['batting_team_id'].iloc[0]}): len={len(inn_b)}, sum(runs)={total_runs_col}, extras_count={extras_count}, wide_sum_runs={wides['runs'].sum()}, noball_sum_runs={noballs['runs'].sum()}")
