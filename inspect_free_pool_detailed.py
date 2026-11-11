import pandas as pd

df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
batters = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_batters_pressure_metrics.csv')
bowlers = pd.read_csv(r'D:\6af3166e7b922_data_pack\all_bowlers_pressure_metrics.csv')

# Find 2025 IPL competition
ipl_2025_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2025', 2025])]['comp_id'].tolist()
named_2025 = set(df_map[df_map['comp_id'].isin(ipl_2025_id)]['player_id'].unique())

# Also 2026 IPL competition
ipl_2026_id = comps[comps['comp_name'].str.contains('IPL', case=False, na=False) & comps['season'].isin(['2026', 2026])]['comp_id'].tolist()
named_2026 = set(df_map[df_map['comp_id'].isin(ipl_2026_id)]['player_id'].unique())

not_in_25_or_26 = set(df_map['player_id'].unique()) - named_2025 - named_2026

# Filter by Indian teams or Indian franchises
indian_franchises = ['Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Kolkata Knight Riders',
                     'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals',
                     'Royal Challengers Bengaluru', 'Sunrisers Hyderabad', 'India', 'India A']

df_ind_free = df_map[df_map['player_id'].isin(not_in_25_or_26) & df_map['team_name'].isin(indian_franchises)].copy()

print(f"Total unique players in this pool: {df_ind_free['player_id'].nunique()}")

# Add player details
player_summary = []
for pid in df_ind_free['player_id'].unique():
    name = df_map[df_map['player_id'] == pid]['player_name'].iloc[0]
    teams = ", ".join(df_map[df_map['player_id'] == pid]['team_name'].unique())
    comps_p = ", ".join(df_map[df_map['player_id'] == pid]['comp_name'].unique())
    
    # Check batting metrics
    b_row = batters[batters['striker_id'] == pid]
    b_balls = b_row['press_balls'].iloc[0] if len(b_row) > 0 else 0
    b_runs = b_row['press_runs'].iloc[0] if len(b_row) > 0 else 0
    b_sr = b_row['sr_press'].iloc[0] if len(b_row) > 0 else 0
    b_score = b_row['rci_bat_regularized'].iloc[0] if len(b_row) > 0 else 0
    
    # Check bowling metrics
    bw_row = bowlers[bowlers['bowler_id'] == pid]
    bw_balls = bw_row['press_balls'].iloc[0] if len(bw_row) > 0 else 0
    bw_econ = bw_row['econ_press'].iloc[0] if len(bw_row) > 0 else 0
    bw_wkts = bw_row['press_wickets'].iloc[0] if len(bw_row) > 0 else 0
    bw_score = bw_row['rci_bowl_regularized'].iloc[0] if len(bw_row) > 0 else 0
    
    player_summary.append({
        'player_id': pid,
        'name': name,
        'teams': teams,
        'press_balls_bat': b_balls,
        'press_runs_bat': b_runs,
        'sr_press_bat': b_sr,
        'bat_score': b_score,
        'press_balls_bowl': bw_balls,
        'econ_press_bowl': bw_econ,
        'wkts_press_bowl': bw_wkts,
        'bowl_score': bw_score
    })

res_df = pd.DataFrame(player_summary)

print("\n--- TOP BATTERS IN FREE/RELEASED POOL (Not in 2025 & Not in 2026 IPL) ---")
print(res_df.sort_values(by='bat_score', ascending=False)[['player_id', 'name', 'teams', 'press_balls_bat', 'press_runs_bat', 'sr_press_bat', 'bat_score']].head(25).to_string())

print("\n--- TOP BOWLERS IN FREE/RELEASED POOL (Not in 2025 & Not in 2026 IPL) ---")
print(res_df.sort_values(by='bowl_score', ascending=False)[['player_id', 'name', 'teams', 'press_balls_bowl', 'econ_press_bowl', 'wkts_press_bowl', 'bowl_score']].head(25).to_string())
