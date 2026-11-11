import pandas as pd

p11 = pd.read_csv(r'D:\6af3166e7b922_data_pack\playing_eleven.csv')
matches = pd.read_csv(r'D:\6af3166e7b922_data_pack\matches.csv')
comps = pd.read_csv(r'D:\6af3166e7b922_data_pack\competitions.csv')
df_map = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')

def check_player(pid, name):
    print(f"\n=================== {name} (ID: {pid}) ===================")
    teams = df_map[df_map['player_id'] == pid][['comp_id', 'team_name']].merge(comps, on='comp_id')
    print("Teams and Comps mapped:")
    print(teams[['comp_name', 'season', 'team_name']].to_string())
    
    # Matches played
    p_matches = p11[p11['player_id'] == pid].merge(matches, on='match_id').merge(comps, on='comp_id')
    print(f"Total matches played in dataset: {len(p_matches)}")
    ipl_played = p_matches[p_matches['comp_name'].str.contains('IPL', case=False, na=False)]
    print(f"IPL matches played in dataset: {len(ipl_played)}")
    if len(ipl_played) > 0:
        print(ipl_played[['match_date', 'comp_name', 'home_team', 'away_team']])

check_player(8647, "Sediqullah Atal")
check_player(6932, "Pramod Madushan")
check_player(8632, "Aaqib Khan")
check_player(8380, "Mohammad Rishad Hossain")
check_player(7049, "Kamil Mishara")
