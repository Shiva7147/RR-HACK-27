import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Exclude 2025 IPL players
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())

# Exclude 2026 IPL players
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

# Exclude RR players
rr_players = set(df_map[df_map['team_name'] == 'Rajasthan Royals']['player_id'].unique())

# Indian players: anyone associated with India, India A, or Indian domestic / IPL franchises
indian_teams = ['India', 'India A', 'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans',
                'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings',
                'Royal Challengers Bengaluru', 'Sunrisers Hyderabad']

# Non-Indian national teams
overseas_teams = ['Afghanistan', 'Afghanistan A', 'Australia', 'Bangladesh', 'Bangladesh A',
                  'Canada', 'England', 'Hong Kong', 'Ireland', 'Japan', 'Kuwait', 'Nepal',
                  'Netherlands', 'New Zealand', 'Oman', 'Pakistan', 'Pakistan A', 'Scotland',
                  'Singapore', 'South Africa', 'Sri Lanka', 'Sri Lanka A', 'United Arab Emirates',
                  'United States Of America', 'West Indies', 'Zimbabwe']

# Get players who played for overseas teams to identify foreign players who played IPL
overseas_pids = set(df_map[df_map['team_name'].isin(overseas_teams)]['player_id'].unique())

# Eligible Indian player IDs:
# In df_map with an indian_teams entry, NOT in overseas_pids, NOT in named_2025, NOT in named_2026, NOT in rr_players
cand_pids = set(df_map[df_map['team_name'].isin(indian_teams)]['player_id'].unique()) - overseas_pids - named_2025 - named_2026 - rr_players

print(f"Total eligible Indian players found: {len(cand_pids)}")

# Let's inspect each candidate
candidates = []
for pid in cand_pids:
    p_rows = df_map[df_map['player_id'] == pid]
    name = p_rows['player_name'].iloc[0]
    teams = list(set(p_rows['team_name'].unique()))
    comps_list = p_rows['comp_name'].unique().tolist()
    
    # Check recency: what seasons did they play in?
    p_matches = p11[p11['player_id'] == pid].merge(matches, on='match_id').merge(comps, on='comp_id')
    recent_seasons = p_matches['season'].unique().tolist() if len(p_matches) > 0 else []
    recent_comps = p_matches['comp_name'].unique().tolist() if len(p_matches) > 0 else []
    
    in_india_a = 'India A' in teams
    
    # Batting metrics
    b_row = batters[batters['striker_id'] == pid]
    b_balls = b_row['press_balls'].iloc[0] if len(b_row) > 0 else 0
    b_runs = b_row['press_runs'].iloc[0] if len(b_row) > 0 else 0
    b_sr = b_row['sr_press'].iloc[0] if len(b_row) > 0 else 0
    b_bnd = b_row['bnd_pct_press'].iloc[0] if len(b_row) > 0 else 0
    b_score = b_row['rci_bat_regularized'].iloc[0] if len(b_row) > 0 else 0
    
    # Bowling metrics
    bw_row = bowlers[bowlers['bowler_id'] == pid]
    bw_balls = bw_row['press_balls'].iloc[0] if len(bw_row) > 0 else 0
    bw_econ = bw_row['econ_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_wkts = bw_row['press_wickets'].iloc[0] if len(bw_row) > 0 else 0
    bw_bnd = bw_row['bnd_conceded_pct_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_score = bw_row['rci_bowl_regularized'].iloc[0] if len(bw_row) > 0 else 0
    
    candidates.append({
        'player_id': pid,
        'name': name,
        'teams': ", ".join(teams),
        'in_india_a': in_india_a,
        'recent_seasons': ", ".join(map(str, recent_seasons)),
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

res = pd.DataFrame(candidates)
print(res.to_string())
