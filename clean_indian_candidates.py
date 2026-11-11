import pandas as pd

# Load the candidate list script output
df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Exclude 2025 and 2026 IPL
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

# Manual overseas filter for foreign players who only played in IPL in this dataset
foreign_known = ['David Wiese', 'Nathan Bracken', 'Benny Howell', 'Duan Jansen', 'Thomas Curran']

filtered_cands = []
for pid in cand_pids:
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    if name in foreign_known:
        continue
    teams = list(set(df_map[df_map['player_id'] == pid]['team_name'].unique()))
    
    # Matches played
    p_matches = p11[p11['player_id'] == pid].merge(matches, on='match_id').merge(comps, on='comp_id')
    recent_seasons = sorted(p_matches['season'].unique().tolist()) if len(p_matches) > 0 else []
    
    # Batting
    b_row = batters[batters['striker_id'] == pid]
    b_balls = b_row['press_balls'].iloc[0] if len(b_row) > 0 else 0
    b_runs = b_row['press_runs'].iloc[0] if len(b_row) > 0 else 0
    b_sr = b_row['sr_press'].iloc[0] if len(b_row) > 0 else 0
    b_bnd = b_row['bnd_pct_press'].iloc[0] if len(b_row) > 0 else 0
    b_dots = b_row['press_dots'].iloc[0] if len(b_row) > 0 else 0
    b_dismissals = b_row['press_dismissals'].iloc[0] if len(b_row) > 0 else 0
    b_score = b_row['rci_bat_regularized'].iloc[0] if len(b_row) > 0 else 0
    
    # Bowling
    bw_row = bowlers[bowlers['bowler_id'] == pid]
    bw_balls = bw_row['press_balls'].iloc[0] if len(bw_row) > 0 else 0
    bw_runs = bw_row['press_runs_conceded'].iloc[0] if len(bw_row) > 0 else 0
    bw_econ = bw_row['econ_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_wkts = bw_row['press_wickets'].iloc[0] if len(bw_row) > 0 else 0
    bw_bnd = bw_row['bnd_conceded_pct_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_dots = bw_row['press_dots'].iloc[0] if len(bw_row) > 0 else 0
    bw_score = bw_row['rci_bowl_regularized'].iloc[0] if len(bw_row) > 0 else 0
    
    in_ia = 'India A' in teams
    
    filtered_cands.append({
        'player_id': pid,
        'name': name,
        'teams': ", ".join(teams),
        'in_india_a': in_ia,
        'recent_seasons': ", ".join(map(str, recent_seasons)),
        'b_balls': b_balls,
        'b_runs': b_runs,
        'b_sr': b_sr,
        'b_bnd': b_bnd,
        'b_dots': b_dots,
        'b_dismissals': b_dismissals,
        'b_score': b_score,
        'bw_balls': bw_balls,
        'bw_runs': bw_runs,
        'bw_econ': bw_econ,
        'bw_wkts': bw_wkts,
        'bw_bnd': bw_bnd,
        'bw_dots': bw_dots,
        'bw_score': bw_score
    })

df_clean = pd.DataFrame(filtered_cands)
print(f"Cleaned Indian players count: {len(df_clean)}")

# Show players who have actual match actions under pressure (b_balls > 0 or bw_balls > 0)
active_pressure = df_clean[(df_clean['b_balls'] > 0) | (df_clean['bw_balls'] > 0)].sort_values(by=['in_india_a', 'b_score', 'bw_score'], ascending=[False, False, False])
print("\n--- INDIAN PLAYERS WITH DELIVERIES UNDER PRESSURE ---")
print(active_pressure[['player_id', 'name', 'teams', 'in_india_a', 'recent_seasons', 'b_balls', 'b_runs', 'b_sr', 'bw_balls', 'bw_econ', 'bw_wkts']].to_string())

# Show players with zero pressure balls (bench players / squad members in 2024 or earlier)
bench_players = df_clean[(df_clean['b_balls'] == 0) & (df_clean['bw_balls'] == 0)]
print(f"\nBench / Uncapped players with 0 pressure deliveries: {len(bench_players)}")
print(bench_players[['player_id', 'name', 'teams', 'in_india_a', 'recent_seasons']].to_string())
