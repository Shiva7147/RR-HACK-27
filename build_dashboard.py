# -*- coding: utf-8 -*-
import json

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json') as f:
    players = json.load(f)

# Clean out any mention of price from players data
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
    --bg-deep: #0e0a14;
    --text-pure: #ffffff;
    --text-bright: #f1f5f9;
    --text-soft: #cbd5e1;
    --text-dim: #94a3b8;
    --glass-bg: rgba(30, 22, 38, 0.58);
    --glass-bg-hover: rgba(45, 33, 56, 0.72);
    --glass-card: rgba(26, 19, 34, 0.62);
    --glass-border: rgba(255, 255, 255, 0.16);
    --glass-border-strong: rgba(255, 255, 255, 0.32);
    --glass-inner-bevel: rgba(255, 255, 255, 0.38);
    --rose-glow: #f472b6;
    --rose-soft: rgba(244, 114, 182, 0.22);
    --amber-glow: #fb923c;
    --amber-soft: rgba(251, 146, 60, 0.22);
    --royal-navy: #1e3a8a;
    --emerald-glow: #34d399;
    --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: var(--font-stack);
    background-color: var(--bg-deep);
    /* High-craft ethereal crystal dusk atmosphere (rose-quartz, amethyst, warm dune sands) */
    background-image: 
      radial-gradient(circle at 18% 12%, rgba(244, 114, 182, 0.16) 0%, transparent 45%),
      radial-gradient(circle at 82% 16%, rgba(192, 132, 252, 0.14) 0%, transparent 40%),
      radial-gradient(circle at 50% 50%, rgba(251, 146, 60, 0.08) 0%, transparent 60%),
      radial-gradient(circle at 85% 82%, rgba(244, 114, 182, 0.12) 0%, transparent 50%),
      radial-gradient(circle at 15% 88%, rgba(147, 197, 253, 0.08) 0%, transparent 45%),
      linear-gradient(180deg, #130d1a 0%, #0c0812 100%);
    background-attachment: fixed;
    color: var(--text-bright);
    line-height: 1.55;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
    padding-bottom: 80px;
  }

  /* LIQUID GLASS HEADER */
  header {
    background: rgba(24, 17, 31, 0.65);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border-bottom: 1px solid var(--glass-border);
    padding: 16px 32px;
    position: sticky;
    top: 0;
    z-index: 50;
    box-shadow: inset 0 -1px 0 rgba(255, 255, 255, 0.08), 0 10px 30px rgba(0, 0, 0, 0.4);
  }

  .header-container {
    max-width: 1240px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }

  .brand-group {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .brand-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-pure);
    letter-spacing: -0.3px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .brand-title .brand-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--rose-glow);
    box-shadow: 0 0 12px var(--rose-glow);
  }

  .brand-subtitle {
    font-size: 12px;
    color: var(--text-dim);
    letter-spacing: 0.3px;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  /* LIQUID GLASS PILLS */
  .glass-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    font-size: 11.5px;
    font-weight: 600;
    border-radius: 9999px;
    background: rgba(255, 255, 255, 0.08);
    color: var(--text-soft);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: inset 0 1px 1px var(--glass-inner-bevel), 0 4px 12px rgba(0, 0, 0, 0.2);
    font-variant-numeric: tabular-nums;
    text-decoration: none;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .glass-pill:hover {
    background: rgba(255, 255, 255, 0.15);
    border-color: var(--glass-border-strong);
    color: var(--text-pure);
    transform: translateY(-1px);
  }

  .glass-pill-rose {
    background: rgba(244, 114, 182, 0.15);
    color: #fbcfe8;
    border-color: rgba(244, 114, 182, 0.35);
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.4), 0 0 16px rgba(244, 114, 182, 0.2);
  }

  .glass-pill-amber {
    background: rgba(251, 146, 60, 0.15);
    color: #fed7aa;
    border-color: rgba(251, 146, 60, 0.35);
  }

  /* MAIN WRAPPER */
  main {
    max-width: 1240px;
    margin: 0 auto;
    padding: 32px 16px;
  }

  /* HERO BANNER */
  .hero-glass {
    background: var(--glass-card);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 28px;
    padding: 32px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 1px 2px var(--glass-inner-bevel), 0 24px 60px rgba(0, 0, 0, 0.45);
  }

  /* Liquid Meniscus bottom highlight line */
  .hero-glass::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 10%;
    right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(244, 114, 182, 0.6), rgba(251, 146, 60, 0.6), transparent);
  }

  .hero-title {
    font-size: 26px;
    font-weight: 700;
    color: var(--text-pure);
    letter-spacing: -0.5px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .hero-desc {
    font-size: 14px;
    color: var(--text-soft);
    max-width: 900px;
    line-height: 1.6;
    margin-bottom: 20px;
  }

  /* KPI CARDS (LIQUID CRYSTAL FINISH) */
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 18px;
    margin-bottom: 32px;
  }

  .kpi-card {
    background: var(--glass-card);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 1px 1.5px var(--glass-inner-bevel), 0 16px 40px rgba(0, 0, 0, 0.35);
    transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .kpi-card:hover {
    background: var(--glass-bg-hover);
    border-color: var(--glass-border-strong);
    transform: translateY(-2px);
    box-shadow: inset 0 1px 1.5px var(--glass-inner-bevel), 0 20px 48px rgba(0, 0, 0, 0.45);
  }

  .kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 20px;
    right: 20px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  }

  .kpi-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: var(--text-dim);
    font-weight: 600;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .kpi-value {
    font-size: 30px;
    font-weight: 700;
    color: var(--text-pure);
    font-variant-numeric: tabular-nums;
    line-height: 1.1;
    margin-bottom: 8px;
  }

  .kpi-meta {
    font-size: 12px;
    color: var(--text-soft);
  }

  /* PROGRESS BAR EFFECT */
  .progress-track {
    width: 100%;
    height: 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 9999px;
    margin-top: 10px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.05);
  }

  .progress-fill {
    height: 100%;
    border-radius: 9999px;
    background: linear-gradient(90deg, #ec4899, #f472b6, #fb923c);
    box-shadow: 0 0 10px rgba(244, 114, 182, 0.5);
  }

  /* FROSTED TABS NAVIGATION */
  .tabs-bar {
    display: flex;
    gap: 8px;
    background: rgba(24, 17, 31, 0.55);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    padding: 6px;
    border-radius: 9999px;
    margin-bottom: 28px;
    overflow-x: auto;
    box-shadow: inset 0 1px 1px var(--glass-inner-bevel), 0 8px 24px rgba(0, 0, 0, 0.25);
  }

  .tab-btn {
    background: transparent;
    border: none;
    padding: 10px 22px;
    font-size: 13px;
    font-weight: 500;
    color: var(--text-soft);
    cursor: pointer;
    border-radius: 9999px;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
    white-space: nowrap;
  }

  .tab-btn:hover {
    color: var(--text-pure);
    background: rgba(255, 255, 255, 0.08);
  }

  .tab-btn.active {
    background: rgba(255, 255, 255, 0.16);
    color: var(--text-pure);
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.4), 0 4px 14px rgba(0, 0, 0, 0.2);
  }

  /* TAB PANES */
  .tab-pane {
    display: none;
    animation: fadeIn 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .tab-pane.active {
    display: block;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* CONTROLS (SEARCH & FILTER PILLS) */
  .controls-bar {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    margin-bottom: 24px;
    background: var(--glass-card);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 12px 20px;
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    box-shadow: inset 0 1px 1px var(--glass-inner-bevel);
  }

  .filter-group {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
  }

  .filter-btn {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--glass-border);
    color: var(--text-soft);
    padding: 6px 16px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .filter-btn:hover {
    background: rgba(255, 255, 255, 0.12);
    border-color: var(--glass-border-strong);
    color: var(--text-pure);
  }

  .filter-btn.active {
    background: rgba(244, 114, 182, 0.22);
    color: #ffffff;
    border-color: rgba(244, 114, 182, 0.5);
    box-shadow: 0 0 14px rgba(244, 114, 182, 0.3);
  }

  .search-input {
    padding: 8px 18px;
    font-size: 12.5px;
    border: 1px solid var(--glass-border-strong);
    background: rgba(20, 14, 26, 0.6);
    color: var(--text-pure);
    border-radius: 9999px;
    width: 270px;
    outline: none;
    font-family: inherit;
    transition: all 0.2s ease;
  }

  .search-input:focus {
    background: rgba(30, 22, 38, 0.85);
    border-color: var(--rose-glow);
    box-shadow: 0 0 16px rgba(244, 114, 182, 0.3);
  }

  .search-input::placeholder {
    color: var(--text-dim);
  }

  /* PLAYER CARDS GRID */
  .player-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 22px;
  }

  .player-card {
    background: var(--glass-card);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 16px;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 1px 1.5px var(--glass-inner-bevel), 0 16px 40px rgba(0, 0, 0, 0.35);
    transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .player-card:hover {
    background: var(--glass-bg-hover);
    border-color: var(--glass-border-strong);
    transform: translateY(-3px);
    box-shadow: inset 0 1px 2px var(--glass-inner-bevel), 0 24px 60px rgba(0, 0, 0, 0.5);
  }

  /* Meniscus liquid wave bottom highlight on each card */
  .player-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 20%;
    right: 20%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(244, 114, 182, 0.4), transparent);
  }

  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .player-meta-title {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .player-rank-badge {
    font-size: 11px;
    font-weight: 700;
    color: var(--rose-glow);
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }

  .player-name {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-pure);
  }

  .player-role-sub {
    font-size: 12px;
    color: var(--text-dim);
  }

  .jewel-beacon {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--amber-glow);
    box-shadow: 0 0 12px var(--amber-glow);
  }

  .metrics-strip {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    background: rgba(18, 12, 24, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 12px 14px;
    border-radius: 14px;
  }

  .metric-item {
    display: flex;
    flex-direction: column;
  }

  .metric-item-label {
    font-size: 10px;
    text-transform: uppercase;
    color: var(--text-dim);
    letter-spacing: 0.6px;
    font-weight: 600;
  }

  .metric-item-val {
    font-size: 14px;
    font-weight: 700;
    color: var(--text-pure);
    font-variant-numeric: tabular-nums;
  }

  .card-narrative {
    font-size: 12.5px;
    color: var(--text-soft);
    display: flex;
    flex-direction: column;
    gap: 8px;
    line-height: 1.5;
  }

  .card-narrative strong {
    color: var(--text-pure);
  }

  .card-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 12px;
    font-size: 11.5px;
    color: var(--text-dim);
  }

  /* GLASS DATA TABLE */
  .table-container {
    background: var(--glass-card);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    overflow-x: auto;
    box-shadow: inset 0 1px 1.5px var(--glass-inner-bevel), 0 20px 50px rgba(0, 0, 0, 0.35);
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
  }

  th, td {
    padding: 14px 18px;
    text-align: left;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    font-variant-numeric: tabular-nums;
  }

  th {
    background: rgba(20, 14, 26, 0.6);
    color: var(--text-dim);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 10.5px;
    letter-spacing: 0.8px;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover td {
    background: rgba(255, 255, 255, 0.04);
  }

  /* CONTENT GRIDS */
  .content-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 22px;
  }

  .content-card {
    background: var(--glass-card);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    box-shadow: inset 0 1px 1.5px var(--glass-inner-bevel), 0 16px 40px rgba(0, 0, 0, 0.35);
  }

  .content-card-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-pure);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .content-card p {
    font-size: 13px;
    color: var(--text-soft);
    line-height: 1.6;
  }

  .content-card ul {
    margin-left: 18px;
    font-size: 12.5px;
    color: var(--text-soft);
  }

  .content-card li {
    margin-bottom: 6px;
  }

  .formula-box {
    background: rgba(18, 12, 24, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 10px 14px;
    border-radius: 12px;
    font-family: "Courier New", Courier, monospace;
    font-size: 11.5px;
    color: var(--rose-glow);
    margin: 8px 0;
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.4);
  }

  .section-intro {
    margin-bottom: 22px;
  }

  .section-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-pure);
    margin-bottom: 4px;
  }

  .section-desc {
    font-size: 13px;
    color: var(--text-soft);
  }

  /* FOOTER */
  footer {
    border-top: 1px solid var(--glass-border);
    background: rgba(20, 14, 26, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 24px 32px;
    margin-top: 60px;
    font-size: 12px;
    color: var(--text-dim);
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

  <!-- HEADER -->
  <header>
    <div class="header-container">
      <div class="brand-group">
        <div class="brand-title">
          <span class="brand-dot"></span>
          <span>Rajasthan Royals</span>
          <span style="color: var(--text-dim); font-weight: 300;">|</span>
          <span style="font-weight: 600; color: var(--text-soft);">SupeRR Selector Season 2</span>
        </div>
        <div class="brand-subtitle">War-Room Auction Strategy & Scouting Intelligence Portal — IPL 2027</div>
      </div>
      <div class="header-actions">
        <span class="glass-pill glass-pill-rose">80,498 Deliveries Evaluated</span>
        <span class="glass-pill glass-pill-amber">20 Uncapped Targets</span>
        <a href="Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf" target="_blank" class="glass-pill">Executive PDF Dossier</a>
      </div>
    </div>
  </header>

  <main>

    <!-- HERO PANEL -->
    <div class="hero-glass">
      <div class="hero-title">
        <span>Empirical Scouting Intelligence & Venue Calibration</span>
      </div>
      <div class="hero-desc">
        Rebuilding the fortress: an algorithmic audit across 80,498 match deliveries isolating 20 high-scarcity, uncapped domestic and emerging talents to resolve Rajasthan Royals' home-venue vulnerabilities and death-phase execution deficits.
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        <span class="glass-pill">Evaluated Records: 80,498 Deliveries</span>
        <span class="glass-pill">RR Matches Analyzed: 77 Fixtures</span>
        <span class="glass-pill glass-pill-rose">Youth Index: 80% (Ages 19–25)</span>
      </div>
    </div>

    <!-- KPI CARDS -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">
          <span>Home vs Away Win Rate</span>
          <span class="jewel-beacon"></span>
        </div>
        <div class="kpi-value">
          <span style="color: #f87171;">45.9%</span>
          <span style="font-size: 18px; font-weight: 300; color: var(--text-dim);">vs</span>
          <span style="color: #4ade80;">55.0%</span>
        </div>
        <div class="kpi-meta">Home: 17/37 wins | Away: 22/40 wins (The Lost Fortress)</div>
        <div class="progress-track">
          <div class="progress-fill" style="width: 45.9%;"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-label">
          <span>RR Death Boundary Rate</span>
          <span class="jewel-beacon" style="background:#f472b6; box-shadow:0 0 12px #f472b6;"></span>
        </div>
        <div class="kpi-value" style="color: #f87171;">19.5%</div>
        <div class="kpi-meta">Tournament Rank #10 (Dead last in IPL overs 16–20)</div>
        <div class="progress-track">
          <div class="progress-fill" style="width: 19.5%; background: linear-gradient(90deg, #f87171, #ef4444);"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-label">
          <span>Death Bowling Strike Rate</span>
          <span class="jewel-beacon" style="background:#fb923c; box-shadow:0 0 12px #fb923c;"></span>
        </div>
        <div class="kpi-value">15.38 Balls/Wkt</div>
        <div class="kpi-meta">68 wickets in 1,046 balls | Leaked 11.40 RPO at Guwahati</div>
        <div class="progress-track">
          <div class="progress-fill" style="width: 65%;"></div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-label">
          <span>Scouted Board Targets</span>
          <span class="jewel-beacon" style="background:#34d399; box-shadow:0 0 12px #34d399;"></span>
        </div>
        <div class="kpi-value" style="color: #34d399;">20 Verified</div>
        <div class="kpi-meta">10 Pure Batters / All-Rounders & 10 Bowlers</div>
        <div class="progress-track">
          <div class="progress-fill" style="width: 100%; background: linear-gradient(90deg, #10b981, #34d399);"></div>
        </div>
      </div>
    </div>

    <!-- TABS NAVIGATION -->
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
          <button class="filter-btn" onclick="filterTier('Tier 1')">Tier 1 Core (6)</button>
          <button class="filter-btn" onclick="filterTier('Tier 2')">Tier 2 Specialists (7)</button>
          <button class="filter-btn" onclick="filterTier('Tier 3')">Tier 3 Depth (7)</button>
        </div>
        <input type="text" id="searchInput" class="search-input" placeholder="Search player, state, or role..." onkeyup="searchPlayers()">
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
      <div class="table-container">
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
              <td><span class="glass-pill glass-pill-rose">Lost by 5 runs</span></td>
              <td>Chasing 197; RR finished 192/7; missed victory by a single boundary hit in the 20th over.</td>
            </tr>
            <tr>
              <td><strong>20206</strong></td>
              <td>19/04/2023</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 10 runs</span></td>
              <td>Chasing 154, stalled from 87/0; zero strike rotation against finger spin in overs 8–14.</td>
            </tr>
            <tr>
              <td><strong>20212</strong></td>
              <td>23/04/2023</td>
              <td>Royal Challengers Bengaluru</td>
              <td>Bengaluru</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 7 runs</span></td>
              <td>RR 182/6 chasing 189; failed to score 20 off final 6 balls against hard lengths.</td>
            </tr>
            <tr>
              <td><strong>20222</strong></td>
              <td>30/04/2023</td>
              <td>Mumbai Indians</td>
              <td>Wankhede</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 6 wickets</span></td>
              <td>Defending 212; leaked 3 consecutive sixes in the 20th over to lose with 3 balls to spare.</td>
            </tr>
            <tr>
              <td><strong>20232</strong></td>
              <td>07/05/2023</td>
              <td>Sunrisers Hyderabad</td>
              <td>Jaipur (SMS)</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 4 wickets</span></td>
              <td>Defending 214; last-ball no-ball converted to match-winning six by Abdul Samad.</td>
            </tr>
            <tr>
              <td><strong>31242</strong></td>
              <td>10/04/2024</td>
              <td>Gujarat Titans</td>
              <td>Jaipur (SMS)</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 3 wickets</span></td>
              <td>Defending 196; conceded 42 off overs 18–20; Rashid Khan hit final-ball four.</td>
            </tr>
            <tr>
              <td><strong>31268</strong></td>
              <td>02/05/2024</td>
              <td>Sunrisers Hyderabad</td>
              <td>Hyderabad</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 1 run</span></td>
              <td>Chasing 201; trapped LBW on the final ball needing 2 runs to win.</td>
            </tr>
            <tr>
              <td><strong>40725</strong></td>
              <td>16/04/2025</td>
              <td>Delhi Capitals</td>
              <td>Arun Jaitley</td>
              <td><span class="glass-pill glass-pill-rose">Tied (Super Over)</span></td>
              <td>Tied chasing 210; collapsed to just 6 runs in the Super Over.</td>
            </tr>
            <tr>
              <td><strong>40729</strong></td>
              <td>19/04/2025</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 2 runs</span></td>
              <td>Defending 180; leaked 19 runs in the 19th over on large Jaipur boundaries.</td>
            </tr>
            <tr>
              <td><strong>40746</strong></td>
              <td>04/05/2025</td>
              <td>Kolkata Knight Riders</td>
              <td>Eden Gardens</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 1 run</span></td>
              <td>Chasing 223; dot ball on the penultimate delivery sealed 1-run defeat.</td>
            </tr>
            <tr>
              <td><strong>40760</strong></td>
              <td>18/05/2025</td>
              <td>Punjab Kings</td>
              <td>Jaipur (SMS)</td>
              <td><span class="glass-pill glass-pill-rose">Lost by 10 runs</span></td>
              <td>Failed to chase 185; consumed 18 dot balls during middle overs on abrasive clay.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 3: METHODOLOGY -->
    <div id="pane-methodology" class="tab-pane">
      <div class="section-intro">
        <div class="section-title">Methodology: How We Did It & Mathematical Formulation</div>
        <div class="section-desc">Evaluating 80,498 ball-by-ball deliveries using dynamic leverage modeling to isolate genuine clutch execution.</div>
      </div>

      <div class="content-grid">
        <div class="content-card">
          <div class="content-card-title">1. Multi-Variable Pressure Formulation</div>
          <p>Traditional metrics aggregate raw runs and wickets, ignoring context. We assigned every single delivery a dynamic Pressure Weight ($W_i \in [1.00, 2.25]$):</p>
          <div class="formula-box">W_i = 1.00 + (c_phase * I_phase) + (c_rrr * I_rrr) + (c_wkt * I_wkt) + (c_margin * I_margin)</div>
          <ul>
            <li><strong>Neutral Baseline ($W_i = 1.00$):</strong> Default weight when no pressure conditions are active (middle overs, normal run rate).</li>
            <li><strong>Phase Multipliers:</strong> Death overs 16–20 ($+0.50$), Middle overs 7–15 ($+0.20$), Powerplay ($+0.10$).</li>
            <li><strong>Required Run Rate Stress:</strong> In chases with $\text{RRR} \ge 10.0$ RPO, activates $+0.30$ scalar.</li>
            <li><strong>Wicket Depletion Strain:</strong> Wickets in hand $\le 4$ activates $+0.25$ scalar.</li>
            <li><strong>Margin Pressure:</strong> Margin $\le 18$ runs or balls $\le 18$ activates $+0.20$.</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">2. Relative Clutch Index (RCI)</div>
          <p>Isolates performance under high leverage ($W_i \ge 1.40$) relative to personal baseline averages:</p>
          <div class="formula-box">RCI_Bat = SR_Press * [1 + (SR_Press - SR_Base)/SR_Base] * (1 - DotRate_Press) * (1 + BndRate_Press)</div>
          <div class="formula-box">RCI_Bowl = [1 / (Econ_Press + 0.01)] * DotRate_Press * (1 - BndConceded_Press) * [1 + (Wkts_Press/Balls_Press)*6]</div>
          <p>Filters out flat-track bullies who feast in dead rubbers or low-leverage phases.</p>
        </div>

        <div class="content-card">
          <div class="content-card-title">3. The Vignesh Puthur Scarcity Model</div>
          <p>Replicating Season 1's winning discovery of Vignesh Puthur, candidate rankings apply an Asymmetric Scarcity Multiplier ($A_p$):</p>
          <ul>
            <li><strong>Age Sweet-Spot ($19 \le \text{Age} \le 25$):</strong> $1.25\times$ upside bonus for multi-year retention runway.</li>
            <li><strong>Skill Scarcity ($S_p$):</strong> Left-arm 140+ pace ($1.30\times$), Mystery wrist-spin ($1.25\times$), 200+ death SR ($1.30\times$).</li>
            <li><strong>Execution Efficiency ($E_p$):</strong> High statistical output in pressure phases ($1.20\times$).</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">4. Quantitative Wicketkeeping Benchmark</div>
          <p>Wicketkeeping efficiency dictates razor-thin match outcomes:</p>
          <ul>
            <li><strong>Bye Concession Rate:</strong> Target &lt; 0.15 byes/match. <strong>Dhruv Jurel:</strong> 0.15; <strong>Harvik Desai:</strong> 0.12 in SMAT (9 dismissals in 7 innings).</li>
            <li><strong>Dismissal Conversion:</strong> Target &gt; 92.0% clean takes. <strong>Jurel:</strong> 94.1%; <strong>Aravelly Avanish:</strong> 96.4% in ICC U19 World Cup.</li>
            <li><strong>Jaipur Spin Deflection:</strong> Standing up to finger spin on dry clay saves ~14.2 boundary runs/season.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 4: KEY SCREENING FACTORS -->
    <div id="pane-factors" class="tab-pane">
      <div class="section-intro">
        <div class="section-title">Key Analytical Factors That Determined Selection</div>
        <div class="section-desc">The empirical screening pillars applied across the entire candidate pool.</div>
      </div>

      <div class="content-grid">
        <div class="content-card">
          <div class="content-card-title">1. Contract & Eligibility Verification</div>
          <p><strong>100% Free Agents:</strong> Screened against official 2025/2026 IPL retained rosters and Unstop mapping ledger.</p>
          <ul>
            <li>Zero players contracted to other IPL franchises.</li>
            <li>Zero players belonging to Rajasthan Royals.</li>
            <li>Full eligibility under BCCI auction rules (uncapped domestic & uncapped overseas).</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">2. Dual-Home Venue Specialization</div>
          <p><strong>Overcoming the 45.9% Home Trap:</strong></p>
          <ul>
            <li><strong>SMS Jaipur (Dry Clay, 78m Boundaries):</strong> Gap manipulation, running hard 2s, and finger/wrist spin squeeze (Harvik Desai, Ricky Bhui, Matthew Humphreys, Prince Choudhary, J. Suchith).</li>
            <li><strong>Barsapara Guwahati (Dew & Pace):</strong> 140+ km/h hit-the-deck pace and left-arm wide-line yorkers to counter slippery wet balls (Aaqib Khan, Sonny Baker, Ramon Simmonds, Kamil Mishara).</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">3. Age Bracket & Youth Runway (19–25 Sweet Spot)</div>
          <p><strong>80% Youth Index (16 of 20 Players):</strong></p>
          <ul>
            <li>16 players aged 19–25 provide high athletic energy and multi-season retention runway.</li>
            <li><strong>Deliberate Exceptions Justified:</strong> Ricky Bhui (28) provides mature domestic captaincy ballast (#1 SMAT six-hitter); Suyash Prabhudessai (26) offers elite fielding; Pramod Madushan (31) & J. Suchith (31) serve as veteran base-price contingency insurance.</li>
          </ul>
        </div>

        <div class="content-card">
          <div class="content-card-title">4. Ground & Hostile Away Track Adaptation</div>
          <p><strong>Pitches That Make No Sense (Ekana / Chepauk / Spongy Decks):</strong></p>
          <ul>
            <li>Compact back-foot techniques playing late under eyes (Ricky Bhui, Suyash Prabhudessai).</li>
            <li>Upright seam discipline extracting variable bounce without relying on flat pace (Vidhwath Kaverappa, Sonny Baker).</li>
            <li>Defensive finger spin darts denying elevation (Matthew Humphreys, Jagadeesha Suchith).</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer>
    <div class="footer-container">
      <div>SupeRR Selector Season 2 — Rajasthan Royals Analytics & Scouting Submission</div>
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
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 48px; text-align: center; color: var(--text-dim);">No players match the selected filters.</div>';
        return;
      }

      list.forEach(p => {
        const card = document.createElement('div');
        card.className = 'player-card';

        const tierBadgeClass = p.tier === 'Tier 1' ? 'glass-pill-rose' : (p.tier === 'Tier 2' ? 'glass-pill-amber' : '');
        
        card.innerHTML = `
          <div>
            <div class="card-top">
              <div class="player-meta-title">
                <span class="player-rank-badge">Rank #${p.rank} · ${p.category}</span>
                <span class="player-name">${p.name}</span>
                <span class="player-role-sub">${p.role} · ID: ${p.id}</span>
              </div>
              <span class="glass-pill ${tierBadgeClass}">${p.tier}</span>
            </div>

            <div class="metrics-strip" style="margin: 14px 0;">
              <div class="metric-item">
                <span class="metric-item-label">${p.category === 'Batsman' ? 'Pressure SR' : 'Strike Rate'}</span>
                <span class="metric-item-val" style="color: var(--rose-glow);">${p.pressure_sr}</span>
              </div>
              <div class="metric-item">
                <span class="metric-item-label">Age / State</span>
                <span class="metric-item-val">${p.age} Yrs · ${p.team.split('/')[0]}</span>
              </div>
              <div class="metric-item" style="grid-column: 1/-1; margin-top: 2px;">
                <span class="metric-item-label">Verified Performance Evidence</span>
                <span class="metric-item-val" style="font-size: 11.5px; font-weight: 500; color: var(--text-soft);">${p.primary_metric} (${p.secondary_metric})</span>
              </div>
            </div>

            <div class="card-narrative">
              <div><strong>Ground Fit:</strong> ${p.ground_fit}</div>
              <div><strong>Scout Note:</strong> ${p.scout_note}</div>
            </div>
          </div>

          <div class="card-bottom">
            <span>Profile ID: ${p.id}</span>
            <span style="font-weight: 600; color: var(--rose-glow);">${p.team}</span>
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

print("Successfully written updated ethereal crystal glass index.html and dashboard.html")
