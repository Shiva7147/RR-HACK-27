import pandas as pd
import numpy as np
import os

from find_true_auction_targets import eligible_batters, eligible_bowlers, mapping, comp

# Let's filter for Domestic / Emerging players:
# Emerging tournaments: comp_id 2670 (Mens T20 Emerging Teams Asia Cup 2024), 3289 (Asia Cup Rising Stars 2025)
# plus Indian domestic players who have 0 IPL games or unselected in IPL 2026!
emerging_comps = [2670, 3289]
emerging_players = set(mapping[mapping['comp_id'].isin(emerging_comps)]['player_name'].unique())

# Also Indian domestic players who were not in IPL 2026
indian_domestic_unselected = set(mapping[mapping['team_name'].isin(['India A']) | (mapping['comp_name'].str.contains('IPL') & ~mapping['comp_name'].str.contains('IPL 2026'))]['player_name'].unique())

# Combined domestic scouting candidate pool
domestic_scouting_pool = emerging_players.union(indian_domestic_unselected)

# Exclude Pakistani players
pak_players = set(mapping[mapping['team_name'].str.contains('Pakistan', case=False, na=False)]['player_name'].unique())
domestic_scouting_pool = domestic_scouting_pool - pak_players

# Exclude players currently in IPL 2026 squads
ipl_2026_squad_names = set(mapping[mapping['comp_name'] == 'IPL 2026']['player_name'].unique())
domestic_scouting_pool = domestic_scouting_pool - ipl_2026_squad_names

# Let's filter our eligible batters and bowlers
dom_bat = eligible_batters[eligible_batters['striker_name'].isin(domestic_scouting_pool)].sort_values('rci_bat_regularized', ascending=False)
dom_bowl = eligible_bowlers[eligible_bowlers['bowler_name'].isin(domestic_scouting_pool)].sort_values('rci_bowl_regularized', ascending=False)

print("=== DOMESTIC CANDIDATE BATTERS NOT PLAYING CURRENTLY IN IPL ===")
cols_bat = ['striker_name', 'teams', 'press_balls', 'press_runs', 'sr_press', 'sr_delta', 'bnd_pct_press', 'dot_pct_press', 'rci_bat_regularized']
print(dom_bat[cols_bat].head(20).to_string(index=False))

print("\n=== DOMESTIC CANDIDATE BOWLERS NOT PLAYING CURRENTLY IN IPL ===")
cols_bowl = ['bowler_name', 'teams', 'press_balls', 'press_runs_conceded', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(dom_bowl[cols_bowl].head(20).to_string(index=False))
