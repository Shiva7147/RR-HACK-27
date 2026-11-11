import pandas as pd
from compare_rr_vs_champions import bat_summary, bowl_summary

print("=== POWERPLAY (1-6) BATTING (IPL 2025-2026) ===")
pp_bat = bat_summary[bat_summary['phase'] == 'Powerplay'].sort_values('strike_rate', ascending=False)
print(pp_bat[['team_name', 'strike_rate', 'boundary_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))

print("\n=== POWERPLAY (1-6) BOWLING (IPL 2025-2026) ===")
pp_bowl = bowl_summary[bowl_summary['phase'] == 'Powerplay'].sort_values('economy', ascending=True)
print(pp_bowl[['team_name', 'economy', 'boundary_conceded_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))

print("\n=== MIDDLE OVERS (7-15) BATTING (IPL 2025-2026) ===")
mid_bat = bat_summary[bat_summary['phase'] == 'Middle'].sort_values('strike_rate', ascending=False)
print(mid_bat[['team_name', 'strike_rate', 'boundary_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))

print("\n=== MIDDLE OVERS (7-15) BOWLING (IPL 2025-2026) ===")
mid_bowl = bowl_summary[bowl_summary['phase'] == 'Middle'].sort_values('economy', ascending=True)
print(mid_bowl[['team_name', 'economy', 'boundary_conceded_pct', 'dot_pct', 'balls_per_wicket']].to_string(index=False))
