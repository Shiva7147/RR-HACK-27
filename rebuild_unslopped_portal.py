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
<title>Rajasthan Royals — SupeRR Selector Season 2 | Scouting & Analytics War-Room</title>
<style>
  :root {
    --sand-bg: #e8dcd5;
    --dusk-sky: #f5ebe6;
    --quartz-pink: #f9d8de;
    --quartz-rose: #ea9ab2;
    --amethyst-soft: #c4b5fd;
    --glass-slab-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.42) 0%, rgba(245, 230, 236, 0.22) 100%);
    --glass-card-bg: linear-gradient(160deg, rgba(255, 255, 255, 0.48) 0%, rgba(240, 225, 232, 0.28) 100%);
    --glass-border: rgba(255, 255, 255, 0.72);
    --glass-border-subtle: rgba(255, 255, 255, 0.45);
    --glass-shadow: 0 30px 60px rgba(168, 120, 138, 0.22), inset 0 1.5px 2px rgba(255, 255, 255, 0.85), inset 0 -2px 4px rgba(0, 0, 0, 0.04);
    --text-headline: #2d1d28;
    --text-body: #4a3844;
    --text-muted: #7c6875;
    --rose-accent: #d85d85;
    --rose-glow: rgba(216, 93, 133, 0.45);
    --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: var(--font-stack);
    background-color: var(--sand-bg);
    /* Warm desert dunes and quartz crystal atmospheric lighting */
    background-image: 
      radial-gradient(ellipse at 50% 0%, #fff1f4 0%, #fae6ec 35%, #eedad4 70%, #dfcbca 100%);
    background-attachment: fixed;
    color: var(--text-headline);
    line-height: 1.5;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
    padding-bottom: 96px;
    position: relative;
    overflow-x: hidden;
  }

  /* AMBIENT QUARTZ SPHERES & CRYSTAL REFLECTIONS */
  .ambient-orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(1px);
    backdrop-filter: blur(10px);
  }

  .orb-1 {
    width: 140px;
    height: 140px;
    top: 60px;
    right: 8%;
    background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.95), rgba(244, 182, 203, 0.5) 50%, rgba(192, 132, 252, 0.3) 100%);
    box-shadow: 0 20px 40px rgba(200, 140, 165, 0.25), inset 0 2px 4px rgba(255, 255, 255, 0.9);
  }

  .orb-2 {
    width: 80px;
    height: 80px;
    top: 240px;
    left: 4%;
    background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.95), rgba(249, 168, 212, 0.45) 55%, rgba(251, 191, 140, 0.3) 100%);
    box-shadow: 0 16px 32px rgba(210, 150, 175, 0.2);
  }

  .orb-3 {
    width: 50px;
    height: 50px;
    bottom: 120px;
    right: 14%;
    background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.95), rgba(216, 180, 254, 0.5) 60%, rgba(244, 114, 182, 0.3) 100%);
    box-shadow: 0 10px 24px rgba(180, 140, 190, 0.2);
  }

  /* FROSTED GLASS TOP NAV */
  nav {
    max-width: 1200px;
    margin: 24px auto 0 auto;
    padding: 0 16px;
    position: relative;
    z-index: 20;
  }

  .nav-glass-bar {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    border-radius: 9999px;
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 15px;
    font-weight: 700;
    color: var(--text-headline);
    letter-spacing: -0.3px;
  }

  .brand-gem {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #ffffff, var(--rose-accent) 70%);
    box-shadow: 0 0 10px rgba(216, 93, 133, 0.6);
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .nav-link-item {
    font-size: 13px;
    font-weight: 500;
    color: var(--text-body);
    text-decoration: none;
    cursor: pointer;
    transition: color 0.15s ease;
  }

  .nav-link-item:hover {
    color: var(--rose-accent);
  }

  .nav-badge-pill {
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid var(--glass-border);
    padding: 5px 14px;
    border-radius: 9999px;
    font-size: 11.5px;
    font-weight: 600;
    color: var(--text-headline);
    box-shadow: inset 0 1px 1px #ffffff;
  }

  /* MAIN COMPOSITION (MATCHING THE REFERENCE HERO SCENE) */
  .hero-composition {
    max-width: 1200px;
    margin: 28px auto 0 auto;
    padding: 0 16px;
    position: relative;
    z-index: 10;
  }

  /* THE MAIN FLOATING SMOKED GLASS SLAB */
  .main-glass-slab {
    background: var(--glass-slab-bg);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    border-radius: 36px;
    padding: 48px 48px 180px 48px;
    position: relative;
    min-height: 480px;
  }

  /* Liquid Meniscus bottom wave cut */
  .main-glass-slab::after {
    content: '';
    position: absolute;
    bottom: -14px;
    left: 20%;
    width: 120px;
    height: 24px;
    background: rgba(255, 255, 255, 0.45);
    border-radius: 0 0 20px 20px;
    backdrop-filter: blur(24px);
    border: 1px solid var(--glass-border);
    border-top: none;
    box-shadow: 0 10px 20px rgba(168, 120, 138, 0.15);
  }

  .slab-hero-content {
    max-width: 520px;
  }

  .slab-hero-headline {
    font-size: 38px;
    font-weight: 800;
    line-height: 1.12;
    letter-spacing: -1px;
    color: var(--text-headline);
    margin-bottom: 12px;
  }

  .slab-hero-subhead {
    font-size: 14px;
    color: var(--text-body);
    line-height: 1.6;
    margin-bottom: 24px;
  }

  /* DISCOVER BUTTON WITH LIQUID MENISCUS DROP */
  .liquid-action-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 32px;
    font-size: 13.5px;
    font-weight: 600;
    color: var(--text-headline);
    background: rgba(255, 255, 255, 0.65);
    border: 1px solid var(--glass-border);
    border-radius: 9999px;
    box-shadow: inset 0 1.5px 2px #ffffff, 0 12px 28px rgba(180, 120, 140, 0.2);
    cursor: pointer;
    text-decoration: none;
    position: relative;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .liquid-action-btn:hover {
    background: rgba(255, 255, 255, 0.85);
    transform: translateY(-2px);
    box-shadow: inset 0 1.5px 2px #ffffff, 0 16px 36px rgba(180, 120, 140, 0.25);
  }

  .liquid-action-btn::after {
    content: '';
    position: absolute;
    bottom: -6px;
    left: 30%;
    width: 22px;
    height: 8px;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 0 0 10px 10px;
    border: 1px solid var(--glass-border);
    border-top: none;
  }

  /* RIGHT-SIDE FLOATING PILL TABS ATTACHED TO SLAB */
  .slab-side-pills {
    position: absolute;
    top: 48px;
    right: -24px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    z-index: 15;
  }

  .slab-pill-item {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    padding: 12px 24px;
    border-radius: 9999px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-headline);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.2s ease;
    text-decoration: none;
    white-space: nowrap;
    position: relative;
  }

  .slab-pill-item:hover {
    background: rgba(255, 255, 255, 0.85);
    transform: translateX(4px);
    color: var(--rose-accent);
  }

  .slab-pill-item::after {
    content: '';
    position: absolute;
    bottom: -6px;
    left: 24px;
    width: 18px;
    height: 7px;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 0 0 8px 8px;
    border: 1px solid var(--glass-border);
    border-top: none;
  }

  /* RIGHT CURVED GLASS PANEL (LIKE 'MY ROUTINE' IN IMAGE) */
  .curved-metrics-panel {
    position: absolute;
    right: 48px;
    bottom: 48px;
    width: 420px;
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    border-radius: 30px;
    padding: 28px;
    z-index: 12;
    transform: perspective(1000px) rotateY(-8deg);
    transition: transform 0.3s ease;
  }

  .curved-metrics-panel:hover {
    transform: perspective(1000px) rotateY(0deg);
  }

  .curved-panel-title {
    font-size: 17px;
    font-weight: 700;
    color: var(--text-headline);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .metric-slider-row {
    margin-bottom: 14px;
  }

  .slider-label-group {
    display: flex;
    justify-content: space-between;
    font-size: 11.5px;
    color: var(--text-body);
    font-weight: 600;
    margin-bottom: 5px;
  }

  .slider-capsule-track {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.35);
    border-radius: 9999px;
    border: 1px solid rgba(255, 255, 255, 0.6);
    overflow: hidden;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);
  }

  .slider-capsule-fill {
    height: 100%;
    border-radius: 9999px;
    background: linear-gradient(90deg, #f472b6, #fb923c);
    box-shadow: 0 0 10px rgba(244, 114, 182, 0.5);
  }

  /* THREE FLOATING FEATURE PRODUCT-STYLE GLASS CARDS */
  .floating-cards-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: -120px;
    position: relative;
    z-index: 25;
    max-width: 680px;
  }

  .featured-glass-card {
    background: var(--glass-card-bg);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    border-radius: 26px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 230px;
    position: relative;
    transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .featured-glass-card:hover {
    transform: translateY(-6px);
    background: rgba(255, 255, 255, 0.62);
    box-shadow: 0 36px 70px rgba(168, 120, 138, 0.28);
  }

  .featured-glass-card::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 32%;
    width: 32px;
    height: 9px;
    background: rgba(255, 255, 255, 0.55);
    border-radius: 0 0 12px 12px;
    border: 1px solid var(--glass-border);
    border-top: none;
  }

  .card-indicator-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--rose-accent);
    box-shadow: 0 0 8px var(--rose-accent);
  }

  .card-top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }

  .card-category-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 700;
    color: var(--rose-accent);
  }

  .card-player-name {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-headline);
    line-height: 1.2;
    margin-bottom: 2px;
  }

  .card-role-desc {
    font-size: 11px;
    color: var(--text-muted);
    margin-bottom: 12px;
  }

  .card-highlight-val {
    font-size: 12.5px;
    font-weight: 700;
    color: var(--text-headline);
    font-variant-numeric: tabular-nums;
    margin-bottom: 4px;
  }

  .card-subtext {
    font-size: 11px;
    color: var(--text-body);
    line-height: 1.4;
  }

  /* LOWER DETAILED CONTENT SECTIONS */
  .details-container {
    max-width: 1200px;
    margin: 80px auto 0 auto;
    padding: 0 16px;
    position: relative;
    z-index: 10;
  }

  .section-glass-panel {
    background: var(--glass-slab-bg);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
    border-radius: 32px;
    padding: 36px;
    margin-bottom: 32px;
    position: relative;
  }

  .section-header-title {
    font-size: 22px;
    font-weight: 800;
    color: var(--text-headline);
    letter-spacing: -0.5px;
    margin-bottom: 6px;
  }

  .section-header-sub {
    font-size: 13.5px;
    color: var(--text-muted);
    margin-bottom: 24px;
  }

  /* CONTROLS (SEARCH & FILTER PILLS) */
  .controls-bar {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
  }

  .filter-group {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
  }

  .filter-pill {
    background: rgba(255, 255, 255, 0.55);
    border: 1px solid var(--glass-border);
    color: var(--text-body);
    padding: 7px 18px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: inset 0 1px 1px #ffffff;
    transition: all 0.15s ease;
  }

  .filter-pill:hover {
    background: rgba(255, 255, 255, 0.8);
    color: var(--text-headline);
  }

  .filter-pill.active {
    background: var(--rose-accent);
    color: #ffffff;
    border-color: var(--rose-accent);
    box-shadow: 0 4px 14px var(--rose-glow);
  }

  .search-pill-input {
    padding: 9px 20px;
    font-size: 12.5px;
    border: 1px solid var(--glass-border);
    background: rgba(255, 255, 255, 0.65);
    color: var(--text-headline);
    border-radius: 9999px;
    width: 280px;
    outline: none;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.04);
    font-family: inherit;
  }

  .search-pill-input:focus {
    background: #ffffff;
    border-color: var(--rose-accent);
    box-shadow: 0 0 12px var(--rose-glow);
  }

  /* TARGET BOARD 20 PLAYERS GRID */
  .target-board-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 20px;
  }

  .player-board-card {
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    box-shadow: inset 0 1px 1.5px rgba(255, 255, 255, 0.9), 0 16px 36px rgba(168, 120, 138, 0.16);
    border-radius: 24px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 14px;
    position: relative;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .player-board-card:hover {
    background: rgba(255, 255, 255, 0.75);
    transform: translateY(-3px);
    box-shadow: inset 0 1px 1.5px #ffffff, 0 24px 48px rgba(168, 120, 138, 0.22);
  }

  .player-board-card::after {
    content: '';
    position: absolute;
    bottom: -6px;
    left: 28%;
    width: 24px;
    height: 7px;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 0 0 10px 10px;
    border: 1px solid var(--glass-border);
    border-top: none;
  }

  .board-card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .board-rank-pill {
    font-size: 10.5px;
    font-weight: 700;
    color: var(--rose-accent);
    text-transform: uppercase;
    letter-spacing: 0.6px;
  }

  .board-player-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-headline);
  }

  .board-role-sub {
    font-size: 11.5px;
    color: var(--text-muted);
  }

  .board-metrics-block {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    background: rgba(255, 255, 255, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.65);
    padding: 10px 14px;
    border-radius: 14px;
  }

  .board-metric-item {
    display: flex;
    flex-direction: column;
  }

  .board-metric-lbl {
    font-size: 9.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 700;
    letter-spacing: 0.5px;
  }

  .board-metric-val {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text-headline);
    font-variant-numeric: tabular-nums;
  }

  .board-card-desc {
    font-size: 12px;
    color: var(--text-body);
    display: flex;
    flex-direction: column;
    gap: 6px;
    line-height: 1.5;
  }

  .board-card-desc strong {
    color: var(--text-headline);
  }

  .board-card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.6);
    padding-top: 10px;
    font-size: 11px;
    color: var(--text-muted);
  }

  /* GLASS TABLE */
  .table-glass-wrap {
    background: rgba(255, 255, 255, 0.5);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    overflow-x: auto;
    box-shadow: inset 0 1px 1px #ffffff;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
  }

  th, td {
    padding: 14px 18px;
    text-align: left;
    border-bottom: 1px solid rgba(255, 255, 255, 0.5);
    font-variant-numeric: tabular-nums;
  }

  th {
    background: rgba(255, 255, 255, 0.7);
    color: var(--text-muted);
    font-weight: 700;
    text-transform: uppercase;
    font-size: 10px;
    letter-spacing: 0.8px;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover td {
    background: rgba(255, 255, 255, 0.4);
  }

  /* METHODOLOGY CARDS */
  .method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
  }

  .method-card {
    background: rgba(255, 255, 255, 0.45);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 20px;
    box-shadow: inset 0 1px 1px #ffffff;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .method-card-title {
    font-size: 14.5px;
    font-weight: 700;
    color: var(--text-headline);
  }

  .method-card p {
    font-size: 12.5px;
    color: var(--text-body);
    line-height: 1.5;
  }

  .formula-box {
    background: rgba(255, 255, 255, 0.65);
    border: 1px solid var(--glass-border);
    padding: 8px 12px;
    border-radius: 12px;
    font-family: "Courier New", Courier, monospace;
    font-size: 11px;
    color: var(--rose-accent);
    margin: 4px 0;
  }

  /* FOOTER */
  footer {
    max-width: 1200px;
    margin: 48px auto 0 auto;
    padding: 24px 16px 0 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.6);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    color: var(--text-muted);
    flex-wrap: wrap;
    gap: 12px;
    position: relative;
    z-index: 10;
  }

  @media (max-width: 900px) {
    .curved-metrics-panel {
      position: static;
      width: 100%;
      transform: none;
      margin-top: 24px;
    }
    .floating-cards-row {
      margin-top: 24px;
      max-width: 100%;
      grid-template-columns: 1fr;
    }
    .slab-side-pills {
      position: static;
      flex-direction: row;
      flex-wrap: wrap;
      margin-top: 20px;
    }
    .main-glass-slab {
      padding: 32px 24px 32px 24px;
    }
  }
</style>
</head>
<body>

  <!-- AMBIENT CRYSTAL SPHERES -->
  <div class="ambient-orb orb-1"></div>
  <div class="ambient-orb orb-2"></div>
  <div class="ambient-orb orb-3"></div>

  <!-- FROSTED GLASS TOP NAV -->
  <nav>
    <div class="nav-glass-bar">
      <div class="nav-brand">
        <span class="brand-gem"></span>
        <span>Rajasthan Royals</span>
        <span style="color: var(--text-muted); font-weight: 300;">|</span>
        <span style="font-weight: 600; color: var(--text-body);">SupeRR Selector S2</span>
      </div>
      <div class="nav-links">
        <a href="#board-section" class="nav-link-item">Target Board</a>
        <a href="#losses-section" class="nav-link-item">11 Losses Audit</a>
        <a href="#method-section" class="nav-link-item">Methodology</a>
        <a href="Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf" target="_blank" class="nav-badge-pill" style="text-decoration:none;">10-Page PDF</a>
      </div>
    </div>
  </nav>

  <!-- HERO COMPOSITION (RECREATING THE REFERENCE SCENE) -->
  <section class="hero-composition">
    
    <!-- MAIN FLOATING SMOKED GLASS SLAB -->
    <div class="main-glass-slab">
      <div class="slab-hero-content">
        <div class="slab-hero-headline">
          Scouting & Analytics War-Room
        </div>
        <div class="slab-hero-subhead">
          An empirical evaluation across 80,498 match deliveries isolating 20 high-scarcity uncapped talents calibrated to solve Rajasthan Royals' home-venue deficits.
        </div>
        <a href="#board-section" class="liquid-action-btn">
          Explore Target Board
        </a>
      </div>

      <!-- RIGHT ATTACHED LIQUID PILL TABS -->
      <div class="slab-side-pills">
        <a href="#board-section" class="slab-pill-item">
          <span>⚡</span>
          <span>Top 10 Batters</span>
        </a>
        <a href="#board-section" class="slab-pill-item">
          <span>🎯</span>
          <span>Top 10 Bowlers</span>
        </a>
        <a href="#losses-section" class="slab-pill-item">
          <span>📊</span>
          <span>11 Razor Losses</span>
        </a>
        <a href="#method-section" class="slab-pill-item">
          <span>🔬</span>
          <span>Clutch Formula</span>
        </a>
      </div>

      <!-- RIGHT CURVED GLASS METRICS PANEL (MATCHING 'MY ROUTINE') -->
      <div class="curved-metrics-panel">
        <div class="curved-panel-title">
          <span>Core Diagnosis</span>
          <span style="font-size: 11px; color: var(--rose-accent);">77 Fixtures</span>
        </div>

        <div class="metric-slider-row">
          <div class="slider-label-group">
            <span>Away Win Rate</span>
            <span>55.0% (22/40)</span>
          </div>
          <div class="slider-capsule-track">
            <div class="slider-capsule-fill" style="width: 55.0%; background: linear-gradient(90deg, #10b981, #34d399);"></div>
          </div>
        </div>

        <div class="metric-slider-row">
          <div class="slider-label-group">
            <span>Home Win Rate (Deficit)</span>
            <span>45.9% (17/37)</span>
          </div>
          <div class="slider-capsule-track">
            <div class="slider-capsule-fill" style="width: 45.9%; background: linear-gradient(90deg, #f87171, #fb923c);"></div>
          </div>
        </div>

        <div class="metric-slider-row">
          <div class="slider-label-group">
            <span>Death Boundary Frequency</span>
            <span>19.5% (Rank #10)</span>
          </div>
          <div class="slider-capsule-track">
            <div class="slider-capsule-fill" style="width: 19.5%; background: linear-gradient(90deg, #f43f5e, #f472b6);"></div>
          </div>
        </div>

        <div class="metric-slider-row">
          <div class="slider-label-group">
            <span>Youth Index (Ages 19–25)</span>
            <span>80.0% (16/20)</span>
          </div>
          <div class="slider-capsule-track">
            <div class="slider-capsule-fill" style="width: 80.0%;"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- THREE FLOATING FEATURE PRODUCT-STYLE GLASS CARDS -->
    <div class="floating-cards-row">
      <!-- CARD 1 -->
      <div class="featured-glass-card">
        <div>
          <div class="card-top-header">
            <span class="card-category-label">Pace Spearhead</span>
            <span class="card-indicator-dot"></span>
          </div>
          <div class="card-player-name">Aaqib Khan</div>
          <div class="card-role-desc">Age: 20 · UP / India A · 142+ km/h</div>
          <div class="card-highlight-val">5.10 PP Economy (60% Dots)</div>
        </div>
        <div class="card-subtext">Dismissed Mayank Agarwal in Ranji Trophy; matches elite quicks in early-over dot suppression.</div>
      </div>

      <!-- CARD 2 -->
      <div class="featured-glass-card">
        <div>
          <div class="card-top-header">
            <span class="card-category-label">Wicketkeeper-Batter</span>
            <span class="card-indicator-dot"></span>
          </div>
          <div class="card-player-name">Harvik Desai</div>
          <div class="card-role-desc">Age: 25 · Saurashtra · Top-Order</div>
          <div class="card-highlight-val">323 Runs · 152.4 SR in SMAT</div>
        </div>
        <div class="card-subtext">0.12 byes/inn with 9 dismissals; gap manipulation converts 1s into 2s at SMS Jaipur.</div>
      </div>

      <!-- CARD 3 -->
      <div class="featured-glass-card">
        <div>
          <div class="card-top-header">
            <span class="card-category-label">Death Seamer</span>
            <span class="card-indicator-dot"></span>
          </div>
          <div class="card-player-name">Ramon Simmonds</div>
          <div class="card-role-desc">Age: 23 · West Indies · Left-Arm</div>
          <div class="card-highlight-val">4.00% Death Boundary (1 in 25)</div>
        </div>
        <div class="card-subtext">5.04 death economy across 25 balls; natural left-arm angle executes wide yorkers in dew.</div>
      </div>
    </div>

  </section>

  <!-- LOWER DETAILED MODULES -->
  <main class="details-container">

    <!-- SECTION 1: TARGET BOARD -->
    <section id="board-section" class="section-glass-panel">
      <div class="section-header-title">The 20-Player Target Board</div>
      <div class="section-header-sub">Screened for contract availability, venue adaptation, and pressure execution.</div>

      <div class="controls-bar">
        <div class="filter-group">
          <button class="filter-pill active" onclick="filterCategory('All')">All (20)</button>
          <button class="filter-pill" onclick="filterCategory('Batsman')">Top 10 Batters</button>
          <button class="filter-pill" onclick="filterCategory('Bowler')">Top 10 Bowlers</button>
          <button class="filter-pill" onclick="filterTier('Tier 1')">Tier 1 Core</button>
          <button class="filter-pill" onclick="filterTier('Tier 2')">Tier 2 Specialists</button>
          <button class="filter-pill" onclick="filterTier('Tier 3')">Tier 3 Depth</button>
        </div>
        <input type="text" id="searchInput" class="search-pill-input" placeholder="Search by player, state, or role..." onkeyup="searchPlayers()">
      </div>

      <div class="target-board-grid" id="playerGrid">
        <!-- Rendered by JS -->
      </div>
    </section>

    <!-- SECTION 2: 11 RAZOR-THIN LOSSES -->
    <section id="losses-section" class="section-glass-panel">
      <div class="section-header-title">Diagnostic Audit: The 11 Razor-Thin Losses</div>
      <div class="section-header-sub">Match-by-match delivery verification where RR held &gt;65% win probability before final overs collapse.</div>

      <div class="table-glass-wrap">
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
              <td><span class="board-rank-pill">Lost by 5 runs</span></td>
              <td>Chasing 197; finished 192/7; death overs lacked 1 boundary hit in the 20th over.</td>
            </tr>
            <tr>
              <td><strong>20206</strong></td>
              <td>19/04/2023</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span class="board-rank-pill">Lost by 10 runs</span></td>
              <td>Chasing 154, stalled from 87/0; zero strike rotation against finger spin in overs 8–14.</td>
            </tr>
            <tr>
              <td><strong>20212</strong></td>
              <td>23/04/2023</td>
              <td>Royal Challengers Bengaluru</td>
              <td>Bengaluru</td>
              <td><span class="board-rank-pill">Lost by 7 runs</span></td>
              <td>RR 182/6 chasing 189; failed to score 20 off final 6 balls against hard lengths.</td>
            </tr>
            <tr>
              <td><strong>20222</strong></td>
              <td>30/04/2023</td>
              <td>Mumbai Indians</td>
              <td>Wankhede</td>
              <td><span class="board-rank-pill">Lost by 6 wickets</span></td>
              <td>Defending 212; leaked 3 consecutive sixes in the 20th over to lose with 3 balls left.</td>
            </tr>
            <tr>
              <td><strong>20232</strong></td>
              <td>07/05/2023</td>
              <td>Sunrisers Hyderabad</td>
              <td>Jaipur (SMS)</td>
              <td><span class="board-rank-pill">Lost by 4 wickets</span></td>
              <td>Defending 214; last-ball no-ball converted to match-winning six by Abdul Samad.</td>
            </tr>
            <tr>
              <td><strong>31242</strong></td>
              <td>10/04/2024</td>
              <td>Gujarat Titans</td>
              <td>Jaipur (SMS)</td>
              <td><span class="board-rank-pill">Lost by 3 wickets</span></td>
              <td>Defending 196; conceded 42 off overs 18–20; Rashid Khan hit final-ball four.</td>
            </tr>
            <tr>
              <td><strong>31268</strong></td>
              <td>02/05/2024</td>
              <td>Sunrisers Hyderabad</td>
              <td>Hyderabad</td>
              <td><span class="board-rank-pill">Lost by 1 run</span></td>
              <td>Chasing 201; trapped LBW on the final ball needing 2 runs to win.</td>
            </tr>
            <tr>
              <td><strong>40725</strong></td>
              <td>16/04/2025</td>
              <td>Delhi Capitals</td>
              <td>Arun Jaitley</td>
              <td><span class="board-rank-pill">Tied (Super Over)</span></td>
              <td>Tied chasing 210; collapsed to just 6 runs in the Super Over.</td>
            </tr>
            <tr>
              <td><strong>40729</strong></td>
              <td>19/04/2025</td>
              <td>Lucknow Super Giants</td>
              <td>Jaipur (SMS)</td>
              <td><span class="board-rank-pill">Lost by 2 runs</span></td>
              <td>Defending 180; leaked 19 runs in the 19th over on large Jaipur boundaries.</td>
            </tr>
            <tr>
              <td><strong>40746</strong></td>
              <td>04/05/2025</td>
              <td>Kolkata Knight Riders</td>
              <td>Eden Gardens</td>
              <td><span class="board-rank-pill">Lost by 1 run</span></td>
              <td>Chasing 223; dot ball on penultimate delivery sealed 1-run defeat.</td>
            </tr>
            <tr>
              <td><strong>40760</strong></td>
              <td>18/05/2025</td>
              <td>Punjab Kings</td>
              <td>Jaipur (SMS)</td>
              <td><span class="board-rank-pill">Lost by 10 runs</span></td>
              <td>Failed to chase 185; consumed 18 dot balls during middle overs on abrasive clay.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 3: METHODOLOGY -->
    <section id="method-section" class="section-glass-panel">
      <div class="section-header-title">Methodology & Mathematical Formulation</div>
      <div class="section-header-sub">Dynamic leverage vector applied across 80,498 match deliveries.</div>

      <div class="method-grid">
        <div class="method-card">
          <div class="method-card-title">1. Dynamic Pressure Weight</div>
          <p>Every delivery is assigned a contextual weight ($W_i \in [1.00, 2.25]$):</p>
          <div class="formula-box">W_i = 1.00 + (c_phase * I_phase) + (c_rrr * I_rrr) + (c_wkt * I_wkt) + (c_margin * I_margin)</div>
          <p>Neutral baseline default is $W_i = 1.00$ when no stress trigger is active.</p>
        </div>

        <div class="method-card">
          <div class="method-card-title">2. Relative Clutch Index (RCI)</div>
          <p>Evaluates execution under high pressure ($W_i \ge 1.40$) vs personal baselines:</p>
          <div class="formula-box">RCI_Bat = SR_Press * [1 + (SR_Press - SR_Base)/SR_Base] * (1 - DotRate_Press) * (1 + BndRate_Press)</div>
          <p>Eliminates flat-track inflation in low-leverage phases.</p>
        </div>

        <div class="method-card">
          <div class="method-card-title">3. Vignesh Puthur Scarcity Model</div>
          <p>Replicating Season 1's discovery, candidate rankings apply an Asymmetric Scarcity Multiplier ($A_p$):</p>
          <p>19–25 age runway ($1.25\times$), left-arm 140+ pace ($1.30\times$), mystery wrist-spin ($1.25\times$), and 200+ death SR ($1.30\times$).</p>
        </div>

        <div class="method-card">
          <div class="method-card-title">4. Screening Constraints</div>
          <p>100% free agents verified against 2025/2026 IPL franchise rosters and Unstop mapping. 80% youth index (16 of 20 targets aged 19–25).</p>
        </div>
      </div>
    </section>

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
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 48px; text-align: center; color: var(--text-muted);">No players match the selected filters.</div>';
        return;
      }

      list.forEach(p => {
        const card = document.createElement('div');
        card.className = 'player-board-card';
        
        card.innerHTML = `
          <div>
            <div class="board-card-top">
              <div>
                <span class="board-rank-pill">Rank #${p.rank} · ${p.category}</span>
                <div class="board-player-title">${p.name}</div>
                <div class="board-role-sub">${p.role} · ID: ${p.id}</div>
              </div>
              <span class="card-indicator-dot" style="margin-top: 4px;"></span>
            </div>

            <div class="board-metrics-block" style="margin: 12px 0;">
              <div class="board-metric-item">
                <span class="board-metric-lbl">${p.category === 'Batsman' ? 'Pressure SR' : 'Strike Rate'}</span>
                <span class="board-metric-val" style="color: var(--rose-accent);">${p.pressure_sr}</span>
              </div>
              <div class="board-metric-item">
                <span class="board-metric-lbl">Age / State</span>
                <span class="board-metric-val">${p.age} Yrs · ${p.team.split('/')[0]}</span>
              </div>
              <div class="board-metric-item" style="grid-column: 1/-1; margin-top: 2px;">
                <span class="board-metric-lbl">Verified Evidence</span>
                <span class="board-metric-val" style="font-size: 11px; font-weight: 500; color: var(--text-body);">${p.primary_metric} (${p.secondary_metric})</span>
              </div>
            </div>

            <div class="board-card-desc">
              <div><strong>Ground Fit:</strong> ${p.ground_fit}</div>
              <div><strong>Scout Note:</strong> ${p.scout_note}</div>
            </div>
          </div>

          <div class="board-card-footer">
            <span>Profile ID: ${p.id}</span>
            <span style="font-weight: 600; color: var(--rose-accent);">${p.team}</span>
          </div>
        `;
        grid.appendChild(card);
      });
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
      document.querySelectorAll('.filter-pill').forEach(btn => {
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

print("Successfully written rebuilt portal exactly matching reference design")
