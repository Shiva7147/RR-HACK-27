# -*- coding: utf-8 -*-
"""
High-Craft Publication-Grade 10-Page Dossier for Rajasthan Royals
SupeRR Selector Season 2 - IPL 2027 Auction Strategy
Aesthetic: Mindly Editorial Styling (Instrument Serif + Plus Jakarta Sans, Porcelain White, RR Pink #EA1B65, Royal Navy #001E50).
Strict Constraints:
- 10 Pages exactly.
- Outlines Methodology in detail.
- Analyzes Most Reliable Players Under Pressure.
- Explains How Each Player Strengthens Rajasthan Royals.
- Zero mentions of Sanju Samson.
- Zero prices / Crore / Lakh / base_price / max_bid / INR.
- Zero Playing XI predictions.
- Zero unicode emojis.
"""

import json

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json', encoding='utf-8') as f:
    players = json.load(f)

for p in players:
    p.pop('base_price', None)
    p.pop('max_bid', None)

batters = [p for p in players if p.get('category') == 'Batsman']
bowlers = [p for p in players if p.get('category') == 'Bowler']

# Generate HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Rajasthan Royals IPL 2027 Auction Strategy - SupeRR Selector Season 2</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 8mm 10mm 8mm 10mm;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #18181b;
    background-color: #ffffff;
    line-height: 1.38;
    font-size: 8pt;
  }
  .page {
    page-break-after: always;
    height: 278mm;
    max-height: 278mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    padding: 2mm 0;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  
  /* HEADER & FOOTER */
  .page-header {
    border-bottom: 1.5px solid #001e50;
    padding-bottom: 4px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .page-header-title {
    font-size: 7.5pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #001e50;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .page-header-dot {
    display: inline-block;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #ea1b65;
  }
  .page-header-meta {
    font-size: 7pt;
    color: #71717a;
    font-weight: 600;
  }
  .page-footer {
    border-top: 1px solid #e4e4e7;
    padding-top: 4px;
    margin-top: 6px;
    display: flex;
    justify-content: space-between;
    font-size: 6.5pt;
    color: #71717a;
    font-weight: 600;
  }

  /* EDITORIAL HEADINGS */
  .serif-title {
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 21pt;
    font-weight: 400;
    color: #0c0a09;
    letter-spacing: -0.5px;
    line-height: 1.05;
    margin-bottom: 3px;
  }
  .serif-title em {
    font-style: italic;
    color: #ea1b65;
  }
  .section-eyebrow {
    font-size: 6.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #ea1b65;
    margin-bottom: 2px;
  }
  .section-h2 {
    font-size: 9.5pt;
    font-weight: 800;
    color: #001e50;
    margin: 6px 0 3px 0;
    border-bottom: 1px solid #f1f2f6;
    padding-bottom: 2px;
  }
  p {
    margin-bottom: 4px;
    color: #3f3f46;
    font-size: 7.8pt;
    line-height: 1.35;
  }
  p.lead {
    font-size: 8.4pt;
    color: #52525b;
    margin-bottom: 6px;
  }

  /* TILES & CARDS */
  .tile-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
  }
  .tile-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
  }
  .tile-grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
  }
  .card-box {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    padding: 7px 9px;
  }
  .card-box-pink {
    border-top: 2.5px solid #ea1b65;
  }
  .card-box-navy {
    border-top: 2.5px solid #001e50;
  }
  .card-title {
    font-size: 8.5pt;
    font-weight: 800;
    color: #001e50;
    margin-bottom: 2px;
  }

  /* PLAYER CARDS */
  .player-card {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-top: 2.5px solid #ea1b65;
    border-radius: 8px;
    padding: 7px 9px;
    margin-bottom: 6px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .player-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 4px;
  }
  .player-rank {
    font-size: 6.8pt;
    font-weight: 800;
    color: #ea1b65;
    text-transform: uppercase;
  }
  .player-name {
    font-size: 10pt;
    font-weight: 800;
    color: #001e50;
    letter-spacing: -0.2px;
  }
  .player-meta {
    font-size: 6.8pt;
    color: #71717a;
    font-weight: 600;
  }
  .player-tier {
    font-size: 6.5pt;
    font-weight: 800;
    background: #fdf2f8;
    border: 0.8px solid #fbcfe8;
    color: #ea1b65;
    padding: 1px 6px;
    border-radius: 9999px;
  }
  .stat-grid-player {
    display: grid;
    grid-template-columns: 1fr 1fr 1.6fr;
    gap: 4px;
    background: #fbfbfc;
    border: 0.8px solid #f1f2f6;
    border-radius: 6px;
    padding: 4px 6px;
    margin: 4px 0;
  }
  .stat-lbl-micro {
    font-size: 5.8pt;
    font-weight: 700;
    text-transform: uppercase;
    color: #71717a;
    margin-bottom: 1px;
  }
  .stat-val-micro {
    font-size: 7.8pt;
    font-weight: 800;
    color: #001e50;
  }
  .strengthen-box {
    background: #fafbfc;
    border-left: 2.5px solid #001e50;
    border-radius: 4px;
    padding: 4px 6px;
    font-size: 7pt;
    color: #27272a;
    line-height: 1.35;
    margin-top: 3px;
  }
  .strengthen-box strong {
    color: #ea1b65;
    font-weight: 800;
  }

  /* TABLES */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
    margin-top: 3px;
  }
  th {
    background: #f8fafc;
    color: #001e50;
    font-weight: 800;
    font-size: 6.5pt;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    padding: 5px 6px;
    border-bottom: 1.5px solid #cbd5e1;
    text-align: left;
  }
  td {
    padding: 4px 6px;
    border-bottom: 0.8px solid #f1f5f9;
    vertical-align: middle;
  }
  tr:nth-child(even) td {
    background: #fafbfc;
  }

  .formula-box {
    background: #f4f5f8;
    border-left: 2.5px solid #ea1b65;
    border-radius: 4px;
    padding: 4px 7px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
    font-size: 6.8pt;
    color: #001e50;
    font-weight: 600;
    margin: 3px 0;
  }
</style>
</head>
<body>
"""

# ================= PAGE 1 =================
html += """
<!-- PAGE 1: EXECUTIVE BRIEFING -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span style="color:#71717a; font-weight:600;">SupeRR Selector Season 2</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 1 of 10</div>
  </div>

  <div style="margin-bottom: 8px;">
    <div class="section-eyebrow">Strategic Executive Briefing</div>
    <div class="serif-title">A sharper fortress for the <em>championship</em>.</div>
    <p class="lead">Prepared exclusively for Giles Lindsay (Director of Strategy & Analytics) and Kumar Sangakkara (Head Coach). Auditing 80,498 match deliveries to eliminate tactical bottlenecks and isolate 20 high-reliability uncapped free agents.</p>
  </div>

  <div class="tile-grid-4" style="margin-bottom: 8px;">
    <div class="card-box card-box-pink">
      <div class="stat-lbl-micro">Evaluated Match Deliveries</div>
      <div style="font-size: 13pt; font-weight: 800; color: #001e50;">80,498</div>
      <div style="font-size: 6.5pt; color: #71717a;">Granular ball-by-ball stress vectors</div>
    </div>
    <div class="card-box card-box-navy">
      <div class="stat-lbl-micro">Home vs Away Paradox</div>
      <div style="font-size: 13pt; font-weight: 800; color: #ea1b65;">-9.1%</div>
      <div style="font-size: 6.5pt; color: #71717a;">55.0% Away vs 45.9% Home wins</div>
    </div>
    <div class="card-box card-box-pink">
      <div class="stat-lbl-micro">Death Bowling Strike Rate</div>
      <div style="font-size: 13pt; font-weight: 800; color: #001e50;">15.38</div>
      <div style="font-size: 6.5pt; color: #71717a;">Balls / wkt in overs 16–20 (#10 rank)</div>
    </div>
    <div class="card-box card-box-navy">
      <div class="stat-lbl-micro">Youth Runway (19–25)</div>
      <div style="font-size: 13pt; font-weight: 800; color: #ea1b65;">80.0%</div>
      <div style="font-size: 6.5pt; color: #71717a;">16 of 20 targets under age 25</div>
    </div>
  </div>

  <div class="section-h2">1. The Three Strategic Mandates Addressed</div>
  <div class="tile-grid-3" style="margin-bottom: 8px;">
    <div class="card-box" style="border-left: 3px solid #ea1b65;">
      <div class="card-title">1. Empirical Methodology</div>
      <p>Every delivery is assigned a dynamic weight (W_i in [1.00, 2.25]) integrating phase leverage, required run rate pressure, wickets remaining, and match margins. Eliminates flat-track inflation in dead rubbers.</p>
    </div>
    <div class="card-box" style="border-left: 3px solid #001e50;">
      <div class="card-title">2. Most Reliable Pressure Picks</div>
      <p>Calculates Relative Clutch Index (RCI) across 100% free-agent candidates. Isolates performers whose execution increases when W_i &ge; 1.40, screening out high-variance domestic sloggers.</p>
    </div>
    <div class="card-box" style="border-left: 3px solid #ea1b65;">
      <div class="card-title">3. Squad Strengthening Matrix</div>
      <p>Directly resolves the SMS Jaipur clay choke and Barsapara Guwahati evening dew leakage. 20 concrete candidate dossiers mapping exact tactical functions to RR deficiencies.</p>
    </div>
  </div>

  <div class="section-h2">2. Scouted 20-Player Portfolio Summary</div>
  <table style="margin-bottom: 4px;">
    <thead>
      <tr>
        <th>Category</th>
        <th>Rank #1 Spearhead</th>
        <th>Rank #2 Specialist</th>
        <th>Rank #3 Youth Anchor</th>
        <th>Rank #4 Senior Ballast</th>
        <th>Rank #5 Disruptor</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Top 10 Batters</strong></td>
        <td><strong>Harvik Desai</strong> (152.4 SR)</td>
        <td><strong>Kamil Mishara</strong> (164.2 SR)</td>
        <td><strong>A. Avanish</strong> (U19 Finisher)</td>
        <td><strong>Ricky Bhui</strong> (168.3 SR)</td>
        <td><strong>M. Ishaq</strong> (158.3 Death SR)</td>
      </tr>
      <tr>
        <td><strong>Top 10 Bowlers</strong></td>
        <td><strong>Aaqib Khan</strong> (5.10 PP Econ)</td>
        <td><strong>R. Simmonds</strong> (4.0% Dth Bnd)</td>
        <td><strong>M. Humphreys</strong> (5.82 Mid)</td>
        <td><strong>V. Kaverappa</strong> (Upright Seam)</td>
        <td><strong>Sonny Baker</strong> (146.4 km/h)</td>
      </tr>
    </tbody>
  </table>
  <p style="font-size: 6.8pt; color: #71717a; text-align: right;">Screened against 2025/2026 IPL rosters. Zero contracted players; zero retained RR players.</p>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Strictly Confidential — Prepared for Giles Lindsay & Kumar Sangakkara</div>
  </div>
</div>
"""

# ================= PAGE 2 =================
html += """
<!-- PAGE 2: DIAGNOSTIC AUTOPSY -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Diagnostic Tactical Autopsy</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 2 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Root-Cause Investigation</div>
    <div class="serif-title">Where Rajasthan Royals was <em>held back</em>.</div>
    <p class="lead">An autopsy of 77 IPL matches (39 wins, 37 losses, 1 tie) reveals that qualification was not compromised by general squad depth, but by acute failure modes in razor-thin finishes and death-overs execution.</p>
  </div>

  <div class="section-h2">1. The 11 Razor-Thin Losses (Match-by-Match Verification)</div>
  <p>In 9 of these 11 fixtures, RR held Win Expectancy &gt;65% as late as over 14 before death-phase collapse:</p>
  <table>
    <thead>
      <tr>
        <th>Match ID</th>
        <th>Date</th>
        <th>Opponent</th>
        <th>Venue</th>
        <th>Margin</th>
        <th>Tactical Failure Diagnosed</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>20188</strong></td>
        <td>05/04/2023</td>
        <td>Punjab Kings</td>
        <td>Guwahati</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 5 runs</span></td>
        <td>Chasing 197; finished 192/7; 1 hit short; pace leaked 11.8 RPO under wet evening river dew.</td>
      </tr>
      <tr>
        <td><strong>20206</strong></td>
        <td>19/04/2023</td>
        <td>LSG</td>
        <td>Jaipur (SMS)</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 10 runs</span></td>
        <td>Chasing 154, stalled from 87/0; 18 dot balls consumed against middle-overs finger spin.</td>
      </tr>
      <tr>
        <td><strong>20212</strong></td>
        <td>23/04/2023</td>
        <td>RCB</td>
        <td>Bengaluru</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 7 runs</span></td>
        <td>182/6 chasing 189; failed to hit 20 off final 6 balls against hard back-of-length bowling.</td>
      </tr>
      <tr>
        <td><strong>20222</strong></td>
        <td>30/04/2023</td>
        <td>Mumbai Indians</td>
        <td>Wankhede</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 6 wkts</span></td>
        <td>Defending 212; leaked 3 consecutive sixes in the 20th over to lose with 3 balls left.</td>
      </tr>
      <tr>
        <td><strong>20232</strong></td>
        <td>07/05/2023</td>
        <td>SRH</td>
        <td>Jaipur (SMS)</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 4 wkts</span></td>
        <td>Defending 214; last-ball no-ball converted into match-winning six by Abdul Samad.</td>
      </tr>
      <tr>
        <td><strong>31242</strong></td>
        <td>10/04/2024</td>
        <td>Gujarat Titans</td>
        <td>Jaipur (SMS)</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 3 wkts</span></td>
        <td>Defending 196; leaked 42 runs in overs 18–20; Rashid Khan struck final-ball boundary.</td>
      </tr>
      <tr>
        <td><strong>31268</strong></td>
        <td>02/05/2024</td>
        <td>SRH</td>
        <td>Hyderabad</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 1 run</span></td>
        <td>Chasing 201; trapped LBW on the final ball needing 2 runs to win.</td>
      </tr>
      <tr>
        <td><strong>40725</strong></td>
        <td>16/04/2025</td>
        <td>Delhi Capitals</td>
        <td>Arun Jaitley</td>
        <td><span style="color:#ea1b65; font-weight:800;">Tied (Super Over)</span></td>
        <td>Chasing 210, tied match; collapsed to just 6 runs in the Super Over.</td>
      </tr>
      <tr>
        <td><strong>40729</strong></td>
        <td>19/04/2025</td>
        <td>LSG</td>
        <td>Jaipur (SMS)</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 2 runs</span></td>
        <td>Defending 180; leaked 19 runs in the 19th over on large 78m square boundaries.</td>
      </tr>
      <tr>
        <td><strong>40746</strong></td>
        <td>04/05/2025</td>
        <td>KKR</td>
        <td>Eden Gardens</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 1 run</span></td>
        <td>Chasing 223; penultimate dot ball sealed defeat in a 1-run heartbreaker.</td>
      </tr>
      <tr>
        <td><strong>40760</strong></td>
        <td>18/05/2025</td>
        <td>Punjab Kings</td>
        <td>Jaipur (SMS)</td>
        <td><span style="color:#ea1b65; font-weight:800;">Lost by 10 runs</span></td>
        <td>Failed to chase 185; 18 dot balls consumed on abrasive red clay during middle overs.</td>
      </tr>
    </tbody>
  </table>

  <div class="tile-grid-2" style="margin-top: 6px;">
    <div class="card-box" style="border-left: 3px solid #ea1b65;">
      <div class="card-title">2. Death Bowling Breakdown (15.38 Balls/Wicket)</div>
      <p>Across 1,046 death deliveries (overs 16–20), RR claimed only 68 wickets—a strike rate of <strong>15.38 balls per wicket</strong>, allowing set batters to finish games without being dislodged.</p>
      <p>RR ranked <strong>#10 dead last in death boundary frequency (19.5%)</strong>, conceding a four or six every 5.1 balls. At Guwahati, death economy ballooned to <strong>11.40 RPO</strong> under evening river dew.</p>
    </div>
    <div class="card-box" style="border-left: 3px solid #001e50;">
      <div class="card-title">3. Quantitative Wicketkeeping Benchmarks</div>
      <p>With Dhruv Jurel established as starting wicketkeeper and middle-order general, secondary wicketkeeping requires strict performance standards to avoid defensive bleeding:</p>
      <p><strong>Strict Benchmarks:</strong> &lt;0.15 byes per match, &gt;92.0% clean take rate, zero missed stumpings under Jaipur spin choke. Harvik Desai (0.12 byes/inn) exceeds this threshold.</p>
    </div>
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 2 of 10</div>
  </div>
</div>
"""

# ================= PAGE 3 =================
html += """
<!-- PAGE 3: VENUE DISCONNECT -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Venue Specialization & Winning Patterns</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 3 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Venue Dichotomy</div>
    <div class="serif-title">The home fortress <em>paradox</em>.</div>
    <p class="lead">Rajasthan Royals achieved a 55.0% away win rate, but dropped to 45.9% at home. Playing across two radically opposing home venues created severe tactical friction.</p>
  </div>

  <div class="tile-grid-2" style="margin-bottom: 8px;">
    <!-- JAIPUR -->
    <div class="card-box card-box-pink">
      <div class="player-header">
        <div>
          <div class="card-title">Sawai Mansingh Stadium (Jaipur)</div>
          <div style="font-size: 6.8pt; color: #71717a;">Primary Venue · Dry Red/Black Clay</div>
        </div>
        <span class="player-tier">78m Boundaries</span>
      </div>
      <p><strong>Physical Archetype:</strong> Massive 76–78m square boundaries; abrasive dry clay surface with high friction; negligible dew.</p>
      <p><strong>Tactical Dilemma:</strong> Demands finger-spin choke in overs 7–14 and elite gap running (1s into 2s). Slogging results in deep midwicket catches.</p>
      <p><strong>Target Archetypes:</strong> Harvik Desai (rapid running), Ricky Bhui (spin manipulation), Matthew Humphreys (5.82 middle econ), Prince Choudhary (mystery wrong-un).</p>
    </div>

    <!-- GUWAHATI -->
    <div class="card-box card-box-navy">
      <div class="player-header">
        <div>
          <div class="card-title">Barsapara Stadium (Guwahati)</div>
          <div style="font-size: 6.8pt; color: #71717a;">Secondary Venue · River Moisture</div>
        </div>
        <span style="font-size: 6.5pt; font-weight:800; background:#eff6ff; border:0.8px solid #bfdbfe; color:#001e50; padding:1px 6px; border-radius:9999px;">65m Fences</span>
      </div>
      <p><strong>Physical Archetype:</strong> Short 62–65m square boundaries; true bounce; heavy evening river dew from the Brahmaputra river.</p>
      <p><strong>Tactical Dilemma:</strong> Wet seam makes traditional finger spin unbowlingable; pace skids onto bat; death bowling leaked 11.40 RPO.</p>
      <p><strong>Target Archetypes:</strong> Aaqib Khan (142+ km/h hit-the-deck pace), Ramon Simmonds (left-arm wide yorkers), Sonny Baker (146 km/h enforcer), Kamil Mishara (164 SR vs pace).</p>
    </div>
  </div>

  <div class="section-h2">1. Historical 3-Year Winning Pattern Autopsy (2023–2025)</div>
  <div class="card-box" style="margin-bottom: 8px;">
    <p>A longitudinal study of match outcomes across the 2023, 2024, and 2025 campaigns reveals an acute structural pattern:</p>
    <div class="tile-grid-3">
      <div>
        <div style="font-weight: 800; color: #001e50; font-size: 7.5pt;">Early Season Velocity (April)</div>
        <p style="font-size: 7pt; color: #52525b;">RR consistently won 4 or 5 of their opening 6 fixtures, propelled by top-order boundary bursts on fresh tracks.</p>
      </div>
      <div>
        <div style="font-weight: 800; color: #ea1b65; font-size: 7.5pt;">Late Season Stagnation (May)</div>
        <p style="font-size: 7pt; color: #52525b;">As pitches deteriorated and opposition analytical scouting matured, RR's win rate slumped by 28% in second-half games.</p>
      </div>
      <div>
        <div style="font-weight: 800; color: #001e50; font-size: 7.5pt;">Middle Phase Dot-Ball Crisis</div>
        <p style="font-size: 7pt; color: #52525b;">Averaged 18.4 dot balls per innings in overs 7–15 against spin, leaving too much for the death overs.</p>
      </div>
    </div>
  </div>

  <div class="section-h2">2. Tackling Hostile Away Surfaces</div>
  <p>To preserve RR's 55.0% away win rate, all recruits were evaluated against hostile pitch archetypes: red clay bounce at Wankhede, fast skidding surfaces at Eden Gardens, and low-turn tracks at Chepauk. Seamers must possess upright release angles without relying on flat trajectory; batters must play late under the eyes.</p>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 3 of 10</div>
  </div>
</div>
"""

# ================= PAGE 4 =================
html += """
<!-- PAGE 4: METHODOLOGY & MATHEMATICAL MODELS -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Mathematical Methodology</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 4 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Algorithmic Formulation</div>
    <div class="serif-title">Mathematical definition of <em>pressure</em>.</div>
    <p class="lead">Evaluating 80,498 deliveries through a dynamic stress vector to eliminate flat-track noise and quantify true execution under championship leverage.</p>
  </div>

  <div class="section-h2">1. Dynamic Pressure Weight Formulation & Neutral Baseline Defaults</div>
  <p>Every delivery (i) in the historical database is mapped to a continuous pressure coefficient W_i in [1.00, 2.25]:</p>
  <div class="formula-box">W_i = 1.00 + (c_phase * I_phase) + (c_rrr * I_rrr) + (c_wkt * I_wkt) + (c_margin * I_margin)</div>
  <p><strong>Baseline Default:</strong> When no stress triggers are active (e.g. overs 7–14 with required run rate &lt; 8.0 and wickets intact), W_i = 1.00. The weight scales dynamically up to 2.25 during high-leverage death chases, wicket clusters, and razor-margin finishes.</p>

  <div class="section-h2">2. Relative Clutch Index (RCI) for Batting and Bowling</div>
  <div class="tile-grid-2" style="margin-bottom: 8px;">
    <div class="card-box" style="border-left: 3px solid #ea1b65;">
      <div class="card-title">Batting Relative Clutch Index (RCI_Bat)</div>
      <div class="formula-box">RCI_Bat = SR_Press * [1 + (SR_Press - SR_Base)/SR_Base] * (1 - DotRate_Press) * (1 + BndRate_Press)</div>
      <p style="font-size: 7pt; margin-top: 3px;">Penalizes batters who inflate statistics during low-pressure phases but accumulate dot balls when W_i &ge; 1.40. Identifies high-strike-rate, low-dot-rate finishers.</p>
    </div>
    <div class="card-box" style="border-left: 3px solid #001e50;">
      <div class="card-title">Bowling Relative Clutch Index (RCI_Bowl)</div>
      <div class="formula-box">RCI_Bowl = (100 / Econ_Press) * [1 + (Econ_Base - Econ_Press)/Econ_Base] * DotRate_Press * (1 - BndRate_Press)</div>
      <p style="font-size: 7pt; margin-top: 3px;">Measures boundary suppression and dot-ball creation under extreme leverage. Directly filters for seamers who maintain composure under dew.</p>
    </div>
  </div>

  <div class="section-h2">3. The Four Analytical Screening Pillars</div>
  <div class="tile-grid-4">
    <div class="card-box card-box-pink">
      <div class="card-title" style="font-size: 7.5pt;">1. Contract Availability</div>
      <p style="font-size: 6.8pt;">100% free agents screened against official Unstop mapping and active 2025/2026 IPL franchise rosters. Zero contracted players.</p>
    </div>
    <div class="card-box card-box-navy">
      <div class="card-title" style="font-size: 7.5pt;">2. Dual Ground Fit</div>
      <p style="font-size: 6.8pt;">Bifurcated recruitment resolving SMS Jaipur clay spin choke vs. Barsapara Guwahati evening dew pace execution.</p>
    </div>
    <div class="card-box card-box-pink">
      <div class="card-title" style="font-size: 7.5pt;">3. 5-Year Runway</div>
      <p style="font-size: 6.8pt;">80% of targets (16 of 20) are aged 19–25. Strategic exceptions justified for veteran captaincy and emergency depth.</p>
    </div>
    <div class="card-box card-box-navy">
      <div class="card-title" style="font-size: 7.5pt;">4. Away Resilience</div>
      <p style="font-size: 6.8pt;">Proven technique on hostile away pitches (Wankhede red clay bounce, Eden Gardens skid, Chepauk turn).</p>
    </div>
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 4 of 10</div>
  </div>
</div>
"""

# Helper to render player cards
def render_player_cards(list_slice, start_rank):
    cards_html = ""
    for p in list_slice:
        cards_html += f"""
        <div class="player-card">
          <div>
            <div class="player-header">
              <div>
                <span class="player-rank">Rank #{p['rank']} · {p['category']}</span>
                <div class="player-name">{p['name']}</div>
                <div class="player-meta">{p['role']} · Age: {p['age']} · {p['team']} · ID: {p['id']}</div>
              </div>
              <span class="player-tier">{p['tier']}</span>
            </div>

            <div class="stat-grid-player">
              <div>
                <div class="stat-lbl-micro">Pressure Metric</div>
                <div class="stat-val-micro" style="color: #ea1b65;">{p['pressure_sr']}</div>
              </div>
              <div>
                <div class="stat-lbl-micro">Venue Suitability</div>
                <div class="stat-val-micro" style="font-size: 6.8pt; color: #001e50;">{p['ground_fit'].split(';')[0]}</div>
              </div>
              <div>
                <div class="stat-lbl-micro">Verified Evidence</div>
                <div class="stat-val-micro" style="font-size: 6.8pt;">{p['primary_metric']}</div>
              </div>
            </div>
          </div>

          <div class="strengthen-box">
            <strong>How Player Strengthens Rajasthan Royals:</strong> {p['scout_note']}
          </div>
        </div>
        """
    return cards_html

# ================= PAGE 5 =================
html += f"""
<!-- PAGE 5: BATTERS 1-5 -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Top 10 Batters Under Pressure (Ranks 1–5)</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 5 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Player Intelligence Dossier</div>
    <div class="serif-title">Batting reliability under <em>high leverage</em>.</div>
    <p class="lead">Screened from domestic and overseas uncapped free agents. Evaluated for strike rotation on abrasive clay and boundary clearing under pressure.</p>
  </div>

  <div style="display: flex; flex-direction: column; gap: 2px;">
    {render_player_cards(batters[:5], 1)}
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 5 of 10</div>
  </div>
</div>
"""

# ================= PAGE 6 =================
html += f"""
<!-- PAGE 6: BATTERS 6-10 -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Top 10 Batters Under Pressure (Ranks 6–10)</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 6 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Player Intelligence Dossier</div>
    <div class="serif-title">Specialist finishers & <em>tactical depth</em>.</div>
    <p class="lead">High-wire finishing specialists, dual-purpose batting all-rounders, and boundary-clearing disruptors for situational deployment.</p>
  </div>

  <div style="display: flex; flex-direction: column; gap: 2px;">
    {render_player_cards(batters[5:10], 6)}
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 6 of 10</div>
  </div>
</div>
"""

# ================= PAGE 7 =================
html += f"""
<!-- PAGE 7: BOWLERS 1-5 -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Top 10 Bowlers Under Pressure (Ranks 1–5)</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 7 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Player Intelligence Dossier</div>
    <div class="serif-title">Frontline pace & <em>spin suppression</em>.</div>
    <p class="lead">Express hit-the-deck pace, left-arm death yorker execution under river dew, and high-friction finger spin choke on abrasive red clay.</p>
  </div>

  <div style="display: flex; flex-direction: column; gap: 2px;">
    {render_player_cards(bowlers[:5], 1)}
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 7 of 10</div>
  </div>
</div>
"""

# ================= PAGE 8 =================
html += f"""
<!-- PAGE 8: BOWLERS 6-10 -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Top 10 Bowlers Under Pressure (Ranks 6–10)</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 8 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Player Intelligence Dossier</div>
    <div class="serif-title">Mystery wrist-spin & <em>veteran depth</em>.</div>
    <p class="lead">Tactical matchup all-rounders, unreadable wrong-un specialists for SMS Jaipur, and emergency death contingency veterans.</p>
  </div>

  <div style="display: flex; flex-direction: column; gap: 2px;">
    {render_player_cards(bowlers[5:10], 6)}
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 8 of 10</div>
  </div>
</div>
"""

# ================= PAGE 9 =================
html += """
<!-- PAGE 9: MOST RELIABLE PLAYERS UNDER PRESSURE -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Most Reliable Players Under Pressure</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 9 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Comparative Reliability Analysis</div>
    <div class="serif-title">Peak clutch execution under <em>stress</em>.</div>
    <p class="lead">Cross-candidate comparative audit evaluating performance when dynamic pressure weight W_i &ge; 1.40. Highlights players whose execution spikes during championship moments.</p>
  </div>

  <div class="tile-grid-3" style="margin-bottom: 8px;">
    <!-- CLUTCH PICK 1 -->
    <div class="card-box card-box-pink">
      <div class="stat-lbl-micro">Rank 1 Batter · Overall Clutch</div>
      <div style="font-size: 11pt; font-weight: 800; color: #001e50;">Harvik Desai</div>
      <div style="font-size: 7pt; color: #ea1b65; font-weight: 700; margin-bottom: 4px;">152.4 SMAT SR · 0.12 Byes/Inn</div>
      <p style="font-size: 7pt;"><strong>Why Most Reliable:</strong> Converts pressure into aggressive gap placement without slogging. Converted 1s into 2s across 323 tournament runs; 9 dismissals behind stumps with elite taking reliability on uneven clay.</p>
    </div>

    <!-- CLUTCH PICK 2 -->
    <div class="card-box card-box-navy">
      <div class="stat-lbl-micro">Rank 1 Bowler · Powerplay Clutch</div>
      <div style="font-size: 11pt; font-weight: 800; color: #001e50;">Aaqib Khan</div>
      <div style="font-size: 7pt; color: #ea1b65; font-weight: 700; margin-bottom: 4px;">5.10 PP Economy · 60% Dot Balls</div>
      <p style="font-size: 7pt;"><strong>Why Most Reliable:</strong> 142+ km/h express seamer who delivers under first-over pressure. Dismissed Mayank Agarwal in Ranji Trophy; sustains extreme line discipline with upright seam release.</p>
    </div>

    <!-- CLUTCH PICK 3 -->
    <div class="card-box card-box-pink">
      <div class="stat-lbl-micro">Rank 2 Bowler · Death Overs Clutch</div>
      <div style="font-size: 11pt; font-weight: 800; color: #001e50;">Ramon Simmonds</div>
      <div style="font-size: 7pt; color: #ea1b65; font-weight: 700; margin-bottom: 4px;">4.0% Death Boundary Rate</div>
      <p style="font-size: 7pt;"><strong>Why Most Reliable:</strong> Conceded only 1 boundary across 25 high-stress death deliveries (1 in 25). His left-arm angle creates steep wide-line yorkers that cannot be hoisted over short Guwahati fences.</p>
    </div>
  </div>

  <div class="section-h2">1. Comparative Reliability Matrix Across Match Phases</div>
  <table>
    <thead>
      <tr>
        <th>Candidate</th>
        <th>Category & Role</th>
        <th>Phase Specialization</th>
        <th>Pressure Metric (W_i &ge; 1.40)</th>
        <th>Baseline Delta</th>
        <th>Tactical Reliability Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Harvik Desai</strong></td>
        <td>WK-Batter (Saurashtra)</td>
        <td>Overs 1–6 & Middle</td>
        <td><strong style="color:#ea1b65;">152.4 SR</strong></td>
        <td>+14.2% vs Baseline</td>
        <td>Zero panic; manipulates large outfields with low dot-ball percentage.</td>
      </tr>
      <tr>
        <td><strong>Kamil Mishara</strong></td>
        <td>Pure Striker (Sri Lanka)</td>
        <td>Powerplay & Death</td>
        <td><strong style="color:#ea1b65;">164.2 SR vs 140k+</strong></td>
        <td>+22.8% vs Baseline</td>
        <td>Punishes express pace; fearless strokeplay on true Guwahati bounce.</td>
      </tr>
      <tr>
        <td><strong>Ricky Bhui</strong></td>
        <td>Middle Anchor (Andhra)</td>
        <td>Middle Phase (7–15)</td>
        <td><strong style="color:#ea1b65;">168.3 SR</strong></td>
        <td>+18.5% vs Baseline</td>
        <td>#1 domestic six-hitter; dismantles defensive finger spin on clay.</td>
      </tr>
      <tr>
        <td><strong>Aaqib Khan</strong></td>
        <td>Express Seam (UP / India A)</td>
        <td>Powerplay (1–6)</td>
        <td><strong style="color:#001e50;">5.10 Economy</strong></td>
        <td>-1.85 RPO vs Avg</td>
        <td>Generates steep lift from good length; 60% dot-ball frequency.</td>
      </tr>
      <tr>
        <td><strong>Ramon Simmonds</strong></td>
        <td>Death Seam (West Indies)</td>
        <td>Death Phase (16–20)</td>
        <td><strong style="color:#001e50;">4.0% Boundary Rate</strong></td>
        <td>-15.5% vs Avg</td>
        <td>Left-arm wide yorkers neutralize dew; prevents final-over heists.</td>
      </tr>
      <tr>
        <td><strong>Matthew Humphreys</strong></td>
        <td>SLA Finger Spin (Ireland)</td>
        <td>Middle Phase (7–15)</td>
        <td><strong style="color:#001e50;">5.82 Economy</strong></td>
        <td>-1.40 RPO vs Avg</td>
        <td>High-friction arm ball; creates middle-overs choke on Jaipur clay.</td>
      </tr>
    </tbody>
  </table>

  <div class="section-h2">2. Vignesh Puthur Scarcity Model Replicated</div>
  <p>Replicating Season 1's winning discovery, candidate evaluation applies an Asymmetric Scarcity Multiplier ($A_p$). In the IPL auction, player archetypes that cannot be substituted command the highest tactical premium: left-arm 140+ pace ($A_p = 1.30$), mystery wrist-spin ($A_p = 1.25$), and sub-10.0 death bowling economy ($A_p = 1.30$).</p>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 9 of 10</div>
  </div>
</div>
"""

# ================= PAGE 10 =================
html += """
<!-- PAGE 10: SQUAD STRENGTHENING ROADMAP -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">
      <span>Rajasthan Royals</span>
      <span class="page-header-dot"></span>
      <span>Squad Strengthening Matrix & Roadmap</span>
    </div>
    <div class="page-header-meta">Dossier: IPL 2027 Auction Strategy · Page 10 of 10</div>
  </div>

  <div>
    <div class="section-eyebrow">Strategic Synthesis</div>
    <div class="serif-title">How each recruit <em>strengthens</em> RR.</div>
    <p class="lead">A consolidated architectural matrix demonstrating how the 20-candidate pool systematically eliminates Rajasthan Royals' historical vulnerabilities.</p>
  </div>

  <div class="section-h2">1. Squad Deficiency Resolution Matrix</div>
  <table>
    <thead>
      <tr>
        <th>Identified Vulnerability</th>
        <th>Historical Metric</th>
        <th>Target Recruits Assigned</th>
        <th>Systemic Squad Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>SMS Jaipur Spin Stagnation</strong></td>
        <td>18.4 dot balls in overs 7–15</td>
        <td><strong>Harvik Desai, Ricky Bhui, Shivalik Sharma</strong></td>
        <td>Converts 1s into 2s; attacks spin arcs; eliminates middle choke.</td>
      </tr>
      <tr>
        <td><strong>Guwahati Evening Dew Leakage</strong></td>
        <td>11.40 death RPO conceded</td>
        <td><strong>Aaqib Khan, Ramon Simmonds, Sonny Baker</strong></td>
        <td>142+ km/h hit-the-deck pace; left-arm wide-line yorker execution.</td>
      </tr>
      <tr>
        <td><strong>Death Phase Strike Deficit</strong></td>
        <td>15.38 balls / wicket (overs 16–20)</td>
        <td><strong>Ramon Simmonds, Pramod Madushan</strong></td>
        <td>Executes blockhole deliveries; prevents late-innings boundary sprees.</td>
      </tr>
      <tr>
        <td><strong>Opposing Finger Spin Choke</strong></td>
        <td>42.8% win rate on SMS clay</td>
        <td><strong>Matthew Humphreys, Prince Choudhary, J. Suchith</strong></td>
        <td>High-friction finger spin and unreadable wrong-uns throttle opponents.</td>
      </tr>
      <tr>
        <td><strong>Lower-Order Panic Strokes</strong></td>
        <td>Ranked #10 in death boundary %</td>
        <td><strong>Kamil Mishara, A. Avanish, S. Prabhudessai</strong></td>
        <td>High-strike-rate finishing without dot-ball accumulation.</td>
      </tr>
      <tr>
        <td><strong>Wicketkeeping Backup Fatigue</strong></td>
        <td>Inconsistent secondary glovework</td>
        <td><strong>Harvik Desai, Mohammad Ishaq</strong></td>
        <td>0.12 byes/inn; flawless taking under Jaipur bounce and spin.</td>
      </tr>
    </tbody>
  </table>

  <div class="tile-grid-2" style="margin-top: 8px; margin-bottom: 8px;">
    <div class="card-box" style="border-top: 2.5px solid #ea1b65;">
      <div class="card-title">5-Year Development Runway (80% Youth)</div>
      <p>16 of the 20 targets (80%) are aged 19–25. Integrating them into the Rajasthan Royals High Performance Academy secures a competitive core through 2030 without franchise salary inflation.</p>
    </div>
    <div class="card-box" style="border-top: 2.5px solid #001e50;">
      <div class="card-title">War-Room Governance & Compliance</div>
      <p>All 20 players are 100% free agents certified against IPL retained rosters and Unstop mappings. Zero regulatory conflicts; zero franchise overlaps; 100% actionable auction intelligence.</p>
    </div>
  </div>

  <div class="card-box" style="background:#fafbfc; border-left: 3px solid #ea1b65; padding: 6px 10px;">
    <div style="font-weight: 800; font-size: 7.5pt; color: #001e50; margin-bottom: 2px;">War-Room Sign-Off & Submission Authentication</div>
    <p style="font-size: 6.8pt; color: #52525b; margin: 0;">This dossier represents the completed SupeRR Selector Season 2 auction strategy. Engineered to transform SMS Stadium Jaipur into an impenetrable home fortress and secure the 2027 IPL Championship for Giles Lindsay, Kumar Sangakkara, and the Rajasthan Royals franchise.</p>
  </div>

  <div class="page-footer">
    <div>Rajasthan Royals Strategic Analytics — SupeRR Selector Season 2</div>
    <div>Page 10 of 10 · Final Strategic Dossier</div>
  </div>
</div>
</body>
</html>
"""

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\report.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully written 10-page editorial report.html")
