import pandas as pd
import numpy as np
import os

from find_true_auction_targets import eligible_bowlers, mapping

# Let's inspect candidate bowlers who:
# - Are NOT in IPL 2026
# - Have >= 20 pressure balls
# - Have high RCI score
cand_bowlers = eligible_bowlers[eligible_bowlers['press_balls'] >= 20].sort_values('rci_bowl_regularized', ascending=False)
print("Candidate bowlers with no IPL 2026 conflict:")
cols = ['bowler_name', 'teams', 'press_balls', 'econ_press', 'press_wickets', 'dot_pct_press', 'bnd_conceded_pct_press', 'rci_bowl_regularized']
print(cand_bowlers[cols].head(20).to_string(index=False))
