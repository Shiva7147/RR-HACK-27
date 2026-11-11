import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Exclude 2025 & 2026 IPL and RR
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())
rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

overseas_teams = ['Afghanistan', 'Afghanistan A', 'Australia', 'Bangladesh', 'Bangladesh A',
                  'Canada', 'England', 'Hong Kong', 'Ireland', 'Japan', 'Kuwait', 'Nepal',
                  'Netherlands', 'New Zealand', 'Oman', 'Pakistan', 'Pakistan A', 'Scotland',
                  'Singapore', 'South Africa', 'Sri Lanka', 'Sri Lanka A', 'United Arab Emirates',
                  'United States Of America', 'West Indies', 'Zimbabwe']
overseas_pids = set(df_map[df_map['team_name'].isin(overseas_teams)]['player_id'].unique())

indian_teams = ['India', 'India A', 'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans',
                'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings',
                'Royal Challengers Bengaluru', 'Sunrisers Hyderabad']

cand_pids = set(df_map[df_map['team_name'].isin(indian_teams)]['player_id'].unique()) - overseas_pids - named_2025 - named_2026 - rr_players

retired = ['Ambati Rayudu', 'Robin Uthappa', 'Shikhar Dhawan', 'Wriddhiman Saha', 'Dinesh Karthik',
           'Kedar Jadhav', 'Amit Mishra', 'Piyush Chawla', 'Umesh Yadav', 'Varun Aaron']
foreign = ['David Wiese', 'Nathan Bracken', 'Benny Howell', 'Duan Jansen', 'Thomas Curran', 'Dwayne Bravo', 'Andrew Tye']

pool = []
for pid in cand_pids:
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    if name in retired or name in foreign:
        continue
    teams = list(set(df_map[df_map['player_id'] == pid]['team_name'].unique()))
    in_ia = 'India A' in teams
    
    # Batting
    b_row = batters[batters['striker_id'] == pid]
    b_balls = b_row['press_balls'].iloc[0] if len(b_row) > 0 else 0
    b_runs = b_row['press_runs'].iloc[0] if len(b_row) > 0 else 0
    b_sr = b_row['sr_press'].iloc[0] if len(b_row) > 0 else 0
    b_bnd = b_row['bnd_pct_press'].iloc[0] if len(b_row) > 0 else 0
    b_dots = b_row['press_dots'].iloc[0] if len(b_row) > 0 else 0
    b_score = b_row['rci_bat_regularized'].iloc[0] if len(b_row) > 0 else 0
    
    # Bowling
    bw_row = bowlers[bowlers['bowler_id'] == pid]
    bw_balls = bw_row['press_balls'].iloc[0] if len(bw_row) > 0 else 0
    bw_econ = bw_row['econ_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_wkts = bw_row['press_wickets'].iloc[0] if len(bw_row) > 0 else 0
    bw_bnd = bw_row['bnd_conceded_pct_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_dots = bw_row['press_dots'].iloc[0] if len(bw_row) > 0 else 0
    bw_score = bw_row['rci_bowl_regularized'].iloc[0] if len(bw_row) > 0 else 0
    
    pool.append({
        'player_id': pid,
        'name': name,
        'teams': ", ".join(teams),
        'in_india_a': in_ia,
        'b_balls': b_balls,
        'b_runs': b_runs,
        'b_sr': b_sr,
        'b_bnd': b_bnd,
        'b_score': b_score,
        'bw_balls': bw_balls,
        'bw_econ': bw_econ,
        'bw_wkts': bw_wkts,
        'bw_bnd': bw_bnd,
        'bw_score': bw_score
    })

pdf = pd.DataFrame(pool)
print("Pool size:", len(pdf))

# Let's inspect the top batters
top_batters = pdf[pdf['b_balls'] > 0].sort_values(by='b_score', ascending=False)
print("\n--- TOP BATTERS WITH PRESSURE DATA ---")
print(top_batters[['player_id', 'name', 'teams', 'in_india_a', 'b_balls', 'b_runs', 'b_sr', 'b_bnd', 'b_score']].to_string())

# Also unplayed/bench batters with high domestic potential
bench_batters = pdf[(pdf['b_balls'] == 0) & (pdf['bw_balls'] == 0)]
print(f"\nBench / Domestic players count: {len(bench_batters)}")

# Top bowlers
top_bowlers = pdf[pdf['bw_balls'] > 0].sort_values(by='bw_score', ascending=False)
print("\n--- TOP BOWLERS WITH PRESSURE DATA ---")
print(top_bowlers[['player_id', 'name', 'teams', 'in_india_a', 'bw_balls', 'bw_econ', 'bw_wkts', 'bw_bnd', 'bw_score']].to_string())
