import pandas as pd

df = pd.read_csv(r'D:\6af3166e7b922_data_pack\competition_team_player_mapping.csv')
pids = [6488, 7049, 48551, 3651, 8652, 8085, 26854, 27962, 7548, 8726,
        8632, 8298, 22471, 31227, 24473, 27959, 49665, 27466, 6932, 2852]

for i, pid in enumerate(pids):
    sub = df[df['player_id'] == pid]
    name = sub.iloc[0]['player_name'] if len(sub) > 0 else 'UNKNOWN'
    role_type = "Batsman" if i < 10 else "Bowler"
    rank = (i % 10) + 1
    print(f"{role_type} {rank} (ID {pid}): {name}")
