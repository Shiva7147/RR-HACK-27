import pandas as pd
import numpy as np

mapping = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competition_team_player_mapping.csv')
comp = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\competitions.csv')
teams = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\teams.csv')
bbb = pd.read_csv(r'D:\HACKATHONS\SupeRR_Selector_Season_2\data\ball_by_ball.csv')

# Let's inspect which players are in India A, Sri Lanka A, Afghanistan A, Bangladesh A, or emerging domestic teams
emerging_comps = [2670, 3289]
emerging_players = mapping[mapping['comp_id'].isin(emerging_comps)]['player_name'].unique()
print(f"Total emerging tournament players: {len(emerging_players)}")

# Players who played in India A
india_a_players = mapping[mapping['team_name'] == 'India A']['player_name'].unique()
print(f"Total India A players: {len(india_a_players)}")
print("India A players list:")
print(sorted(india_a_players))

# Check players who have never played senior international cricket (uncapped domestic)
# Senior international teams in competitions.csv:
senior_intl_teams = teams[(teams['comp_id'].isin(comp[comp['match_format'] == 'T20I']['comp_id'])) & 
                          (~teams['team_name'].str.contains(' A$', regex=True))]['team_name'].unique()
print("\nSenior International Teams count:", len(senior_intl_teams))

senior_intl_players = mapping[mapping['team_name'].isin(senior_intl_teams)]['player_name'].unique()
print(f"Total senior international players: {len(senior_intl_players)}")

# Uncapped Indian domestic players in dataset (played in IPL or India A, but NOT for India Senior Men in T20I)
india_senior = mapping[mapping['team_name'] == 'India']['player_name'].unique()
print(f"India Senior Men players in dataset: {len(india_senior)}")

# Uncapped Indian domestic players:
all_indian_players = mapping[mapping['team_name'].isin(['India', 'India A']) | 
                             (mapping['comp_id'].isin(comp[comp['comp_name'].str.contains('IPL')]['comp_id']) & 
                              ~mapping['player_name'].isin(senior_intl_players))]['player_name'].unique()

uncapped_domestic = [p for p in all_indian_players if p not in india_senior]
print(f"\nTotal Uncapped Indian Domestic Players identified: {len(uncapped_domestic)}")
print("First 30 Uncapped Indian Domestic Players:")
print(uncapped_domestic[:30])
