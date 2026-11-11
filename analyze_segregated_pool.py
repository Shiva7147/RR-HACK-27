import pandas as pd

# Load previous filtered candidates
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

foreign_known = ['David Wiese', 'Nathan Bracken', 'Benny Howell', 'Duan Jansen', 'Thomas Curran', 'Dwayne Bravo', 'Kedar Jadhav', 'Dinesh Karthik', 'Robin Uthappa', 'Ambati Rayudu', 'Shikhar Dhawan', 'Wriddhiman Saha']
# Notice: Rayudu, Uthappa, Dhawan, Saha, Karthik, Jadhav are retired veterans from past IPLs.

players_list = []
for pid in cand_pids:
    p_info = df_map[df_map['player_id'] == pid]
    name = p_info['player_name'].iloc[0]
    if name in ['David Wiese', 'Nathan Bracken', 'Benny Howell', 'Duan Jansen', 'Thomas Curran', 'Dwayne Bravo']:
        continue
    teams = list(set(p_info['team_name'].unique()))
    in_ia = 'India A' in teams
    
    p_matches = p11[p11['player_id'] == pid].merge(matches, on='match_id').merge(comps, on='comp_id')
    recent_seasons = sorted(p_matches['season'].unique().tolist()) if len(p_matches) > 0 else []
    
    # Batting
    b_row = batters[batters['striker_id'] == pid]
    b_balls = b_row['press_balls'].iloc[0] if len(b_row) > 0 else 0
    b_runs = b_row['press_runs'].iloc[0] if len(b_row) > 0 else 0
    b_sr = b_row['sr_press'].iloc[0] if len(b_row) > 0 else 0
    b_bnd = b_row['bnd_pct_press'].iloc[0] if len(b_row) > 0 else 0
    b_score = b_row['rci_bat_regularized'].iloc[0] if len(b_row) > 0 else 0
    
    # Bowling
    bw_row = bowlers[bowlers['bowler_id'] == pid]
    bw_balls = bw_row['press_balls'].iloc[0] if len(bw_row) > 0 else 0
    bw_runs = bw_row['press_runs_conceded'].iloc[0] if len(bw_row) > 0 else 0
    bw_econ = bw_row['econ_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_wkts = bw_row['press_wickets'].iloc[0] if len(bw_row) > 0 else 0
    bw_bnd = bw_row['bnd_conceded_pct_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_score = bw_row['rci_bowl_regularized'].iloc[0] if len(bw_row) > 0 else 0
    
    players_list.append({
        'player_id': pid,
        'name': name,
        'teams': ", ".join(teams),
        'in_india_a': in_ia,
        'recent_seasons': ", ".join(map(str, recent_seasons)),
        'is_retired': name in ['Ambati Rayudu', 'Robin Uthappa', 'Shikhar Dhawan', 'Wriddhiman Saha', 'Dinesh Karthik', 'Kedar Jadhav', 'Amit Mishra', 'Piyush Chawla', 'Umesh Yadav', 'Varun Aaron'],
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

p_df = pd.DataFrame(players_list)
print(f"Total active Indian domestic players (excluding foreign & retired): {len(p_df[~p_df['is_retired']])}")

active_pool = p_df[~p_df['is_retired']].copy()
print("\n--- TOP ACTIVE DOMESTIC BATTERS ---")
print(active_pool.sort_values(by='b_score', ascending=False)[['player_id', 'name', 'teams', 'in_india_a', 'recent_seasons', 'b_balls', 'b_runs', 'b_sr', 'b_bnd']].head(15).to_string())

print("\n--- TOP ACTIVE DOMESTIC BOWLERS ---")
print(active_pool.sort_values(by='bw_score', ascending=False)[['player_id', 'name', 'teams', 'in_india_a', 'recent_seasons', 'bw_balls', 'bw_econ', 'bw_wkts', 'bw_bnd']].head(15).to_string())
