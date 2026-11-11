import pandas as pd
import numpy as np
import os

data_dir = r'D:\6af3166e7b922_data_pack'
bbb = pd.read_csv(os.path.join(data_dir, 'ball_by_ball.csv'))
mapping = pd.read_csv(os.path.join(data_dir, 'competition_team_player_mapping.csv'))

# Check which domestic players from India A or bench have balls faced or bowled
domestic_indian_list = [
    'Aaqib Khan', 'Subhranshu Senapati', 'Hari Nishaanth', 'Aryan Juyal', 
    'Bhagath Varma', 'Rahul Buddhi', 'Shubham Garhwal', 'KC Cariappa', 
    'Tejas Baroka', 'Anunay Singh', 'Ishan Porel', 'Chama Milind', 
    'Luvnith Sisodia', 'Vicky Ostwal', 'Harsh Dubey', 'Gurjapneet Singh',
    'Gurnoor Brar', 'Tanush Kotian', 'Hrithik Shokeen', 'Vignesh Puthur'
]

print("Checking domestic Indian players with 0 IPL 2026 matches:")
for p in domestic_indian_list:
    bat_b = bbb[bbb['striker_name'] == p]
    bowl_b = bbb[bbb['bowler_name'] == p]
    print(f"Player: {p:22s} | Balls Faced: {len(bat_b):3d} | Balls Bowled: {len(bowl_b):3d}")
