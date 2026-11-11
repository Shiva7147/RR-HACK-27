import pandas as pd
import numpy as np
import os

from find_true_auction_targets import eligible_batters, eligible_bowlers, mapping, comp

# Master list of Top 10 Batters and Top 10 Bowlers who:
# 1. Are Domestic / Emerging players from the proprietary dataset
# 2. Have NEVER played an IPL game or are NOT in any IPL 2026 squad (open to be bought!)
# 3. Are eligible for the IPL auction (non-Pakistani)
# 4. Have demonstrated elite performance under pressure in the dataset!

top10_bat_names = [
    'Sediqullah Atal',
    'Kamil Mishara',
    'Mohammad Ishaq',
    'Alishan Sharafu',
    'Sahan Arachchige',
    'Asif Khan',
    'Towhid Hridoy',
    'SM Meherob Hasan',
    'Nizakat Khan',
    'Aamir Kaleem'
]

top10_bowl_names = [
    'Pramod Madushan',
    'Dushan Hemantha',
    'Ripon Mondol',
    'Sharafuddin Ashraf',
    'Nipun Ransika',
    'SM Meherob Hasan',
    'Kartik Meiyappan',
    'Muhammad Jawadullah',
    'Ehsan Khan',
    'Aaqib Khan'
]

print("=== VERIFYING BATTERS: SQUAD CONFLICT & PRESSURE STATS ===")
for rank, name in enumerate(top10_bat_names, 1):
    m_info = mapping[mapping['player_name'] == name]
    teams = m_info['team_name'].unique().tolist()
    comps = m_info['comp_name'].unique().tolist()
    in_ipl = any('IPL' in c for c in comps)
    in_ipl_2026 = any('IPL 2026' in c for c in comps)
    
    b_stat = eligible_batters[eligible_batters['striker_name'] == name]
    if len(b_stat) > 0:
        bs = b_stat.iloc[0]
        print(f"Rank {rank:2d}: {name:20s} | Teams: {teams} | In IPL 2026: {in_ipl_2026} | Press Balls: {bs['press_balls']:4.0f} | Press Runs: {bs['press_runs']:4.0f} | Press SR: {bs['sr_press']:6.2f} | Delta SR: {bs['sr_delta']:+6.2f} | Bnd%: {bs['bnd_pct_press']:5.2f}% | Dot%: {bs['dot_pct_press']:5.2f}% | RCI: {bs['rci_bat_regularized']:6.2f}")
    else:
        print(f"Rank {rank:2d}: {name:20s} | Teams: {teams} | No pressure batting stats recorded")

print("\n=== VERIFYING BOWLERS: SQUAD CONFLICT & PRESSURE STATS ===")
for rank, name in enumerate(top10_bowl_names, 1):
    m_info = mapping[mapping['player_name'] == name]
    teams = m_info['team_name'].unique().tolist()
    comps = m_info['comp_name'].unique().tolist()
    in_ipl = any('IPL' in c for c in comps)
    in_ipl_2026 = any('IPL 2026' in c for c in comps)
    
    bw_stat = eligible_bowlers[eligible_bowlers['bowler_name'] == name]
    if len(bw_stat) > 0:
        bws = bw_stat.iloc[0]
        print(f"Rank {rank:2d}: {name:20s} | Teams: {teams} | In IPL 2026: {in_ipl_2026} | Press Balls: {bws['press_balls']:4.0f} | Press Econ: {bws['econ_press']:5.2f} | Press Wkts: {bws['press_wickets']:3.0f} | Dot%: {bws['dot_pct_press']:5.2f}% | Bnd Conceded%: {bws['bnd_conceded_pct_press']:5.2f}% | RCI: {bws['rci_bowl_regularized']:6.2f}")
    else:
        # Check raw balls bowled if bowler had < 20 pressure balls
        raw_b = bbb[bbb['bowler_name'] == name]
        press_b = raw_b[raw_b['is_high_pressure']]
        print(f"Rank {rank:2d}: {name:20s} | Teams: {teams} | Raw Total Balls: {len(raw_b)} | Raw Press Balls: {len(press_b)}")
