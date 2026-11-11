# -*- coding: utf-8 -*-
import json

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json') as f:
    players = json.load(f)

# Ensure no price or unwanted keys
for p in players:
    p.pop('base_price', None)
    p.pop('max_bid', None)

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rajasthan Royals — SupeRR Selector Season 2 | War-Room Strategy Portal</title>
<style>
  :root {
    --rr-navy-deep: #000c1e;
    --rr-navy-base: #001533;
    --rr-navy-surface: #001d47;
    --rr-navy-glass: rgba(0, 24, 60, 0.65);
    --rr-navy-glass-hover: rgba(0, 32, 80, 0.82);
    --rr-pink: #ea1b65;
    --rr-pink-hover: #d01556;
    --rr-pink-glow: rgba(234, 27, 101, 0.35);
    --rr-pink-subtle: rgba(234, 27, 101, 0.12);
    --rr-gold: #c5a059;
    --rr-gold-subtle: rgba(197, 160, 89, 0.15);
    --text-primary: #ffffff;
    --text-secondary: #cbd5e1;
    --text-muted: #8496ad;
    --border-glass: rgba(255, 255, 255, 0.12);
    --border-glass-strong: rgba(255, 255, 255, 0.24);
    --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: var(--font-stack);
    background-color: var(--rr-navy-deep);
    background-image: 
      radial-gradient(ellipse at 15% 10%, rgba(234, 27, 101, 0.14) 0%, transparent 45%),
      radial-gradient(ellipse at 85% 15%, rgba(0, 50, 120, 0.35) 0%, transparent 50%),
      radial-gradient(circle at 50% 85%, rgba(0, 30, 80, 0.4) 0%, transparent 70%),
      linear-gradient(180deg, #000c1e 0%, #001433 50%, #000c1e 100%);
    background-attachment: fixed;
    color: var(--text-primary);
    line-height: 1.5;
    font-size: 13.5px;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
    padding-bottom: 80px;
  }

  /* TOP PROFESSIONAL NAVIGATION */
  header {
    background: rgba(0, 16, 42, 0.75);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-glass);
    padding: 14px 28px;
    position: sticky;
    top: 0;
    z-index: 50;
  }

  .header-container {
    max-width: 1240px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .brand-crest {
    width: 32px;
    height: 32px;
    border-radius: 6px;
    background: linear-gradient(135deg, var(--rr-pink) 0%, #002255 100%);
    border: 1px solid rgba(255, 255, 255, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 14px;
    color: #ffffff;
    letter-spacing: -0.5px;
    box-shadow: 0 0 12px var(--rr-pink-glow);
  }

  .brand-text {
    display: flex;
    flex-direction: column;
  }

  .brand-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.2px;
  }

  .brand-subtitle {
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .rr-badge {
    display: inline-flex;
    align-items: center;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-glass);
    color: var(--text-secondary);
    font-variant-numeric: tabular-nums;
  }

  .rr-badge-pink {
    background: var(--rr-pink-subtle);
    border-color: rgba(234, 27, 101, 0.35);
    color: #ff85ad;
  }

  .rr-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 7px 16px;
    font-size: 11.5px;
    font-weight: 600;
    border-radius: 4px;
    background: var(--rr-pink);
    color: #ffffff;
    border: 1px solid var(--rr-pink);
    text-decoration: none;
    transition: all 0.15s ease;
    cursor: pointer;
    box-shadow: 0 2px 8px var(--rr-pink-glow);
  }

  .rr-btn:hover {
    background: var(--rr-pink-hover);
    border-color: var(--rr-pink-hover);
  }

  /* MAIN LAYOUT */
  main {
    max-width: 1240px;
    margin: 0 auto;
    padding: 28px 16px;
  }

  /* WAR-ROOM HERO BANNER */
  .hero-panel {
    background: var(--rr-navy-glass);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid var(--border-glass);
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 24px;
    position: relative;
    border-left: 4px solid var(--rr-pink);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 16px 40px rgba(0, 0, 0, 0.4);
  }

  .hero-pretitle {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--rr-gold);
    font-weight: 700;
    margin-bottom: 6px;
  }

  .hero-title {
    font-size: 26px;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -0.4px;
    margin-bottom: 8px;
    line-height: 1.2;
  }

  .hero-desc {
    font-size: 13.5px;
    color: var(--text-secondary);
    max-width: 980px;
    line-height: 1.6;
    margin-bottom: 20px;
  }

  .hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  /* KPI METRICS GRID */
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }

  .kpi-card {
    background: var(--rr-navy-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 6px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s ease;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }

  .kpi-card:hover {
    background: var(--rr-navy-glass-hover);
    border-color: var(--border-glass-strong);
    transform: translateY(-2px);
  }

  .kpi-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: var(--text-muted);
    font-weight: 700;
    margin-bottom: 8px;
  }

  .kpi-val {
    font-size: 28px;
    font-weight: 800;
    color: var(--text-primary);
    font-variant-numeric: tabular-nums;
    line-height: 1.1;
    margin-bottom: 6px;
  }

  .kpi-meta {
    font-size: 11.5px;
    color: var(--text-secondary);
  }

  .kpi-progress {
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 2px;
    margin-top: 12px;
    overflow: hidden;
  }

  .kpi-fill {
    height: 100%;
    background: var(--rr-pink);
    border-radius: 2px;
  }

  /* NAVIGATION TABS */
  .tabs-bar {
    display: flex;
    gap: 6px;
    border-bottom: 1px solid var(--border-glass);
    margin-bottom: 24px;
    overflow-x: auto;
    padding-bottom: 2px;
  }

  .tab-btn {
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 10px 18px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s ease;
    white-space: nowrap;
  }

  .tab-btn:hover {
    color: var(--text-primary);
  }

  .tab-btn.active {
    color: var(--rr-pink);
    border-bottom-color: var(--rr-pink);
  }

  /* TAB PANES */
  .tab-pane {
    display: none;
  }

  .tab-pane.active {
    display: block;
  }

  /* CONTROLS (SEARCH & FILTERS) */
  .controls-bar {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    background: var(--rr-navy-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 6px;
    padding: 12px 18px;
  }

  .filter-group {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
  }

  .filter-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-glass);
    color: var(--text-secondary);
    padding: 5px 14px;
    border-radius: 4px;
    font-size: 11.5px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .filter-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
  }

  .filter-btn.active {
    background: var(--rr-pink);
    border-color: var(--rr-pink);
    color: #ffffff;
  }

  .search-input {
    padding: 6px 14px;
    font-size: 12px;
    border: 1px solid var(--border-glass-strong);
    background: rgba(0, 12, 30, 0.6);
    color: var(--text-primary);
    border-radius: 4px;
    width: 260px;
    outline: none;
    font-family: inherit;
    transition: border-color 0.15s ease;
  }

  .search-input:focus {
    border-color: var(--rr-pink);
    box-shadow: 0 0 0 1px var(--rr-pink);
  }

  .search-input::placeholder {
    color: var(--text-muted);
  }

  /* PLAYER CARDS GRID */
  .player-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 18px;
  }

  .player-card {
    background: var(--rr-navy-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 6px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 14px;
    transition: all 0.2s ease;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }

  .player-card:hover {
    background: var(--rr-navy-glass-hover);
    border-color: var(--border-glass-strong);
    transform: translateY(-2px);
  }

  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .card-title-group {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .card-rank-tag {
    font-size: 10.5px;
    font-weight: 700;
    color: var(--rr-pink);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .card-player-name {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
  }

  .card-role-sub {
    font-size: 11.5px;
    color: var(--text-muted);
  }

  .metrics-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    background: rgba(0, 14, 36, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 10px 12px;
    border-radius: 4px;
  }

  .metric-entry {
    display: flex;
    flex-direction: column;
  }

  .metric-entry-label {
    font-size: 9.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 700;
    letter-spacing: 0.5px;
  }

  .metric-entry-val {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text-primary);
    font-variant-numeric: tabular-nums;
  }

  .card-narrative {
    font-size: 12px;
    color: var(--text-secondary);
    display: flex;
    flex-direction: column;
    gap: 6px;
    line-height: 1.5;
  }

  .card-narrative strong {
    color: var(--text-primary);
  }

  .card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border-glass);
    padding-top: 10px;
    font-size: 11px;
    color: var(--text-muted);
  }

  /* DATA TABLES */
  .table-wrap {
    background: var(--rr-navy-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 6px;
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
  }

  th, td {
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border-glass);
    font-variant-numeric: tabular-nums;
  }

  th {
    background: rgba(0, 16, 42, 0.85);
    color: var(--text-muted);
    font-weight: 700;
    text-transform: uppercase;
    font-size: 10px;
    letter-spacing: 0.6px;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover td {
    background: rgba(255, 255, 255, 0.02);
  }

  /* METHODOLOGY GRIDS */
  .content-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 18px;
  }

  .content-card {
    background: var(--rr-navy-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 6px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .content-card-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .content-card p {
    font-size: 12.5px;
    color: var(--text-secondary);
    line-height: 1.55;
  }

  .content-card ul {
    margin-left: 18px;
    font-size: 12px;
    color: var(--text-secondary);
  }

  .content-card li {
    margin-bottom: 6px;
  }

  .formula-box {
    background: rgba(0, 12, 30, 0.7);
    border: 1px solid var(--border-glass);
    padding: 8px 12px;
    border-radius: 4px;
    font-family: "Courier New", Courier, monospace;
    font-size: 11px;
    color: #ff85ad;
    margin: 6px 0;
  }

  .section-intro {
    margin-bottom: 18px;
  }

  .section-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 4px;
  }

  .section-desc {
    font-size: 13px;
    color: var(--text-muted);
  }

  /* FOOTER */
  footer {
    border-top: 1px solid var(--border-glass);
    background: rgba(0, 12, 30, 0.85);
    padding: 24px 28px;
    margin-top: 48px;
    font-size: 11.5px;
    color: var(--text-muted);
  }

  .footer-container {
    max-width: 1240px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }
</style>
</head>
<body>

  <!-- TOP PROFESSIONAL NAVIGATION -->
  <header>
    <div class="header-container">
      <div class="brand-group">
        <div class="brand-crest">RR</div>
        <div class="brand-text">
          <div class="brand-title">Rajasthan Royals</div>
          <div class="brand-subtitle">SupeRR Selector Season 2 | War-Room Strategy Portal</div>
        </div>
      </div>
      <div class="header-actions">
        <span class="rr-badge">80,498 Deliveries Evaluated</span>
        <span class="rr-badge rr-badge-pink">20 Uncapped Targets</span>
        <a href="Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf" target="_blank" class="rr-btn">Executive PDF Dossier</a>
      </div>
    </div>
  </header>

  <main>

    <!-- WAR-ROOM HERO BANNER -->
    <div class="hero-panel">
      <div class="hero-pretitle">Official Strategy & Analytics Dossier — IPL 2027</div>
      <div class="hero-title">Target Acquisition & Home Fortress Calibration</div>
      <div class="hero-desc">
        An empirical audit of 80,498 match deliveries isolating 20 high-scarcity, uncapped domestic and emerging talents to resolve Rajasthan Royals' dual-home venue vulnerabilities and closing-phase execution deficits.
      </div>
      <div class="hero-tags">
        <span class="rr-badge">Evaluated Records: 80,498 Deliveries</span>
        <span class="rr-badge">RR Matches Analyzed: 77 Fixtures</span>
        <span class="rr-badge rr-badge-pink">Youth Index: 80% (Ages 19–25)</span>
        <span class="rr-badge">Audience: Giles Lindsay & Kumar Sangakkara</span>
      </div>
    </div>

    <!-- CORE DIAGNOSTIC KPIS -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div>
          <div class="kpi-label">Home vs Away Win Rate</div>
          <div class="kpi-val">
            <span style="color: #f87171;">45.9%</span>
            <span style="font-size: 16px; font-weight: 400; color: var(--text-muted);">vs</span>
            <span style="color: #4ade80;">55.0%</span>
          </div>
          <div class="kpi-meta">Home: 17/37 wins | Away: 22/40 wins (The Lost Fortress)</div>
        </div>
        <div class="kpi-progress">
          <div class="kpi-fill" style="width: 45.9%; background: #f87171;"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div>
          <div class="kpi-label">RR Death Boundary Frequency</div>
          <div class="kpi-val" style="color: #f87171;">19.5%</div>
          <div class="kpi-meta">Tournament Rank #10 (Dead last in IPL overs 16–20)</div>
        </div>
        <div class="kpi-progress">
          <div class="kpi-fill" style="width: 19.5%; background: var(--rr-pink);"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div>
          <div class="kpi-label">Death Bowling Strike Rate</div>
          <div class="kpi-val">15.38</div>
          <div class="kpi-meta">68 wickets in 1,046 balls | Leaked 11.40 RPO at Guwahati</div>
        </div>
        <div class="kpi-progress">
          <div class="kpi-fill" style="width: 65%; background: #38bdf8;"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div>
          <div class="kpi-label">Verified Target Board</div>
          <div class="kpi-val" style="color: #4ade80;">20 Players</div>
          <div class="kpi-meta">10 Pure Batters / All-Rounders & 10 Bowlers</div>
        </div>
        <div class="kpi-progress">
          <div class="kpi-fill" style="width: 100%; background: #4ade80;"></div>
        </div>
      </div>
    </div>

    <!-- TABS BAR -->
    <div class="tabs-bar">
      <button class="tab-btn active" onclick="switchTab('board')">Target Board (20 Players)</button>
      <button class="tab-btn" onclick="switchTab('losses')">11 Razor-Thin Losses</button>
      <button class="tab-btn" onclick="switchTab('methodology')">Methodology & Mathematical Model</button>
      <button class="tab-btn" onclick="switchTab('factors')">Key Analytical Screening Factors</button>
    </div>

    <!-- TAB 1: TARGET BOARD -->
    <div id="pane-board" class="tab-pane active">
      <div class="controls-bar">
        <div class="filter-group">
          <button class="filter-btn active" onclick="filterCategory('All')">All (20)</button>
          <button class="filter-btn" onclick="filterCategory('Batsman')">Top 10 Batters</button>
          <button class="filter-btn" onclick="filterCategory('Bowler')">Top 10 Bowlers</button>
          <button class="filter-btn" onclick="filterTier('Tier 1')">Tier 1 Core</button>
          <button class="filter-btn" onclick="filterTier('Tier 2')">Tier 2 Specialists</button>
          <button class="filter-btn" onclick="filterTier('Tier 3')">Tier 3 Depth</button>
        </div>
        <input type="text" id="searchInput" class="search-input" placeholder="Search player, state, or tactical role..." onkeyup="searchPlayers()">
      </div>

      <div class="player-grid" id="playerGrid">
        <!-- Injected via JavaScript -->
      </div>
    </div>

    <!-- TAB 2: 11 RAZOR-THIN LOSSES -->
    <div id="pane-losses" class="tab-pane">
      <div class="section-intro">
        <div class="section-title">Diagnostic Audit: The 11 Razor-Thin Losses</div>
        <div class="section-desc">Audited from 77 IPL delivery records. In 9 of these 11 games, RR held win expectancy &gt;65% at over 14 before death-phase collapse.</div>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Match ID</th>
              <th>Date</th>
              <th>Opponent</th>
              <th>Venue</th>
              <th>Result & Margin</th>
              <th>Tactical Bottleneck Diagnosed</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>20188</strong></td>
              <td>05/04/2023</td>
              <td>Punjab Kings</td>
              <td>Guwahati (Barsapara)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 5 runs</span></td>
              <td>Chasing 197; RR finished 192/7; missed victory by a single boundary hit in the 20th over.</td>
            </tr>
            <tr>
              <td><strong>20206</strong></td>
              <td>19/04/2023</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 10 runs</span></td>
              <td>Chasing 154, stalled from 87/0; zero strike rotation against finger spin in overs 8–14.</td>
            </tr>
            <tr>
              <td><strong>20212</strong></td>
              <td>23/04/2023</td>
              <td>Royal Challengers Bengaluru</td>
              <td>Bengaluru</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 7 runs</span></td>
              <td>RR 182/6 chasing 189; failed to score 20 off final 6 balls against hard lengths.</td>
            </tr>
            <tr>
              <td><strong>20222</strong></td>
              <td>30/04/2023</td>
              <td>Mumbai Indians</td>
              <td>Wankhede</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 6 wickets</span></td>
              <td>Defending 212; leaked 3 consecutive sixes in the 20th over to lose with 3 balls to spare.</td>
            </tr>
            <tr>
              <td><strong>20232</strong></td>
              <td>07/05/2023</td>
              <td>Sunrisers Hyderabad</td>
              <td>Jaipur (SMS)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 4 wickets</span></td>
              <td>Defending 214; last-ball no-ball converted to match-winning six by Abdul Samad.</td>
            </tr>
            <tr>
              <td><strong>31242</strong></td>
              <td>10/04/2024</td>
              <td>Gujarat Titans</td>
              <td>Jaipur (SMS)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 3 wickets</span></td>
              <td>Defending 196; conceded 42 off overs 18–20; Rashid Khan hit final-ball four.</td>
            </tr>
            <tr>
              <td><strong>31268</strong></td>
              <td>02/05/2024</td>
              <td>Sunrisers Hyderabad</td>
              <td>Hyderabad</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 1 run</span></td>
              <td>Chasing 201; trapped LBW on the final ball needing 2 runs to win.</td>
            </tr>
            <tr>
              <td><strong>40725</strong></td>
              <td>16/04/2025</td>
              <td>Delhi Capitals</td>
              <td>Arun Jaitley</td>
              <td><span style="color:#f87171; font-weight:700;">Tied (Super Over)</span></td>
              <td>Tied chasing 210; collapsed to just 6 runs in the Super Over.</td>
            </tr>
            <tr>
              <td><strong>40729</strong></td>
              <td>19/04/2025</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 2 runs</span></td>
              <td>Defending 180; leaked 19 runs in the 19th over on large Jaipur boundaries.</td>
            </tr>
            <tr>
              <td><strong>40746</strong></td>
              <td>04/05/2025</td>
              <td>Kolkata Knight Riders</td>
              <td>Eden Gardens</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 1 run</span></td>
              <td>Chasing 223; dot ball on the penultimate delivery sealed 1-run defeat.</td>
            </tr>
            <tr>
              <td><strong>40760</strong></td>
              <td>18/05/2025</td>
              <td>Punjab Kings</td>
              <td>Jaipur (SMS)</td>
              <td><span style="color:#f87171; font-weight:700;">Lost by 10 runs</span></td>
              <td>Failed to chase 185; consumed 18 dot balls during middle overs on abrasive clay.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 3: METHODOLOGY -->
    <div id="pane-methodology" class="tab-pane">
      <div class="section-intro">
        <div class="section-title">Methodology & Mathematical Formulation</div>
        <div class="section-desc">Dynamic leverage vector applied across 80,498 match deliveries.</div>
      </div>

      <div class="content-grid">
        <div class="content-card">
          <div class="content-card-title">1. Dynamic Pressure Weight</div>
          <p>Every delivery is assigned a contextual weight ($W_i \in [1.00, 2.25]$):</p>
          <div class="formula-box">W_i = 1.00 + (c_phase * I_phase) + (c_rrr * I_rrr) + (c_wkt * I_wkt) + (c_margin * I_margin)</div>
          <p>Neutral baseline default is $W_i = 1.00$ when no stress trigger is active (middle overs, normal run rate).</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">2. Relative Clutch Index (RCI)</div>
          <p>Evaluates execution under high pressure ($W_i \ge 1.40$) relative to personal baselines:</p>
          <div class="formula-box">RCI_Bat = SR_Press * [1 + (SR_Press - SR_Base)/SR_Base] * (1 - DotRate_Press) * (1 + BndRate_Press)</div>
          <p>Eliminates flat-track inflation in low-leverage phases.</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">3. Vignesh Puthur Scarcity Model</div>
          <p>Replicating Season 1's winning discovery, candidate rankings apply an Asymmetric Scarcity Multiplier ($A_p$):</p>
          <ul>
            <li>Age 19–25 Runway: 1.25x</li>
            <li>Left-Arm 140+ km/h Pace: 1.30x</li>
            <li>Mystery Wrist-Spin: 1.25x</li>
            <li>200+ Death SR: 1.30x</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">4. Screening Constraints</div>
          <p>100% free agents verified against 2025/2026 IPL franchise rosters and Unstop mapping. 80% youth index (16 of 20 targets aged 19–25).</p>
        </div>
      </div>
    </div>

    <!-- TAB 4: KEY SCREENING FACTORS -->
    <div id="pane-factors" class="tab-pane">
      <div class="section-intro">
        <div class="section-title">Key Analytical Factors That Determined Selection</div>
        <div class="section-desc">The four core empirical pillars applied across the entire candidate pool.</div>
      </div>

      <div class="content-grid">
        <div class="content-card">
          <div class="content-card-title">1. Contract & Eligibility Verification</div>
          <p>100% free agents screened against official 2025/2026 IPL retained rosters and Unstop mapping ledger. Zero players contracted to other IPL franchises; zero players belonging to Rajasthan Royals.</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">2. Dual-Home Venue Specialization</div>
          <p><strong>SMS Jaipur (Dry Clay, 78m Boundaries):</strong> Gap manipulation, running hard 2s, and finger/wrist spin squeeze (Harvik Desai, Ricky Bhui, Matthew Humphreys, Prince Choudhary, J. Suchith).</p>
          <p><strong>Barsapara Guwahati (Dew & Pace):</strong> 140+ km/h hit-the-deck pace and left-arm wide-line yorkers to counter slippery wet balls (Aaqib Khan, Sonny Baker, Ramon Simmonds, Kamil Mishara).</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">3. Age Bracket & Youth Runway (19–25 Sweet Spot)</div>
          <p>16 of 20 targets (80%) are aged 19–25. Strategic exceptions justified: Ricky Bhui (28) provides mature domestic captaincy ballast (#1 SMAT six-hitter); Suyash Prabhudessai (26) offers elite fielding; Pramod Madushan (31) & J. Suchith (31) serve as veteran base-price contingency insurance.</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">4. Ground & Hostile Away Track Adaptation</div>
          <p>Compact back-foot techniques playing late under eyes (Ricky Bhui, Suyash Prabhudessai); upright seam discipline extracting variable bounce without relying on flat pace (Vidhwath Kaverappa, Sonny Baker).</p>
        </div>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer>
    <div class="footer-container">
      <div>Rajasthan Royals — SupeRR Selector Season 2 Strategy & Analytics Submission</div>
      <div>Prepared for: <strong>Giles Lindsay</strong> & <strong>Kumar Sangakkara</strong></div>
    </div>
  </footer>

  <script>
    const players = """ + json.dumps(players) + """;

    let currentCategory = 'All';
    let currentTier = 'All';

    function renderPlayers(list) {
      const grid = document.getElementById('playerGrid');
      grid.innerHTML = '';

      if (list.length === 0) {
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 48px; text-align: center; color: var(--text-muted);">No players match the selected filters.</div>';
        return;
      }

      list.forEach(p => {
        const card = document.createElement('div');
        card.className = 'player-card';

        const tierBadgeClass = p.tier === 'Tier 1' ? 'rr-badge-pink' : '';
        
        card.innerHTML = `
          <div>
            <div class="card-top">
              <div class="card-title-group">
                <span class="card-rank-tag">Rank #${p.rank} · ${p.category}</span>
                <span class="card-player-name">${p.name}</span>
                <span class="card-role-sub">${p.role} · ID: ${p.id}</span>
              </div>
              <span class="rr-badge ${tierBadgeClass}">${p.tier}</span>
            </div>

            <div class="metrics-box" style="margin: 12px 0;">
              <div class="metric-entry">
                <span class="metric-entry-label">${p.category === 'Batsman' ? 'Pressure SR' : 'Strike Rate'}</span>
                <span class="metric-entry-val" style="color: #ff85ad;">${p.pressure_sr}</span>
              </div>
              <div class="metric-entry">
                <span class="metric-entry-label">Age / State</span>
                <span class="metric-entry-val">${p.age} Yrs · ${p.team.split('/')[0]}</span>
              </div>
              <div class="metric-entry" style="grid-column: 1/-1; margin-top: 2px;">
                <span class="metric-entry-label">Verified Evidence</span>
                <span class="metric-entry-val" style="font-size: 11px; font-weight: 500; color: var(--text-secondary);">${p.primary_metric} (${p.secondary_metric})</span>
              </div>
            </div>

            <div class="card-narrative">
              <div><strong>Ground Fit:</strong> ${p.ground_fit}</div>
              <div><strong>Scout Note:</strong> ${p.scout_note}</div>
            </div>
          </div>

          <div class="card-footer">
            <span>Profile ID: ${p.id}</span>
            <span style="font-weight: 600; color: #ff85ad;">${p.team}</span>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));

      event.target.classList.add('active');
      document.getElementById('pane-' + tabId).classList.add('active');
    }

    function filterCategory(cat) {
      currentCategory = cat;
      currentTier = 'All';
      updateFilterButtons();
      applyFilters();
    }

    function filterTier(tier) {
      currentTier = tier;
      currentCategory = 'All';
      updateFilterButtons();
      applyFilters();
    }

    function updateFilterButtons() {
      document.querySelectorAll('.filter-btn').forEach(btn => {
        const text = btn.innerText;
        if (currentCategory !== 'All' && text.includes(currentCategory)) {
          btn.classList.add('active');
        } else if (currentTier !== 'All' && text.includes(currentTier)) {
          btn.classList.add('active');
        } else if (currentCategory === 'All' && currentTier === 'All' && text.startsWith('All')) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
    }

    function searchPlayers() {
      applyFilters();
    }

    function applyFilters() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      let filtered = players.filter(p => {
        const matchesCategory = currentCategory === 'All' || p.category === currentCategory;
        const matchesTier = currentTier === 'All' || p.tier === currentTier;
        const matchesSearch = !q || 
          p.name.toLowerCase().includes(q) || 
          p.id.toString().includes(q) || 
          p.team.toLowerCase().includes(q) || 
          p.role.toLowerCase().includes(q) ||
          p.ground_fit.toLowerCase().includes(q);

        return matchesCategory && matchesTier && matchesSearch;
      });

      renderPlayers(filtered);
    }

    // Initial render
    renderPlayers(players);
  </script>
</body>
</html>
"""

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully written rebuilt Rajasthan Royals official branded war-room dashboard")
