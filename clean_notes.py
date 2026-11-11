import json

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json') as f:
    players = json.load(f)

for p in players:
    p['scout_note'] = p['scout_note'].replace(" at base price (INR 20L)", "").replace(" at base price", "").replace("12-crore", "marquee international")

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json', 'w') as f:
    json.dump(players, f, indent=2)

print("Cleaned scout notes in players.json")
