# -*- coding: utf-8 -*-
"""
High-Craft Editorial Analytics Portal for Rajasthan Royals
SupeRR Selector Season 2 - IPL 2027 Auction Strategy
Strict Constraints:
- Zero overlapping tiles in Hero: engineered using responsive CSS Grid with generous spacing.
- Infused with authentic Rajasthan Royals Pink (#EA1B65) and Royal Navy (#001E50).
- Detailed analytical modules: Home vs Away Paradox, 3-Year Winning Patterns, Dual-Stadium Disconnect, The Closeness Factor.
- Distinct separations between the 4 screening factors: Contract Eligibility, Dual-Home Specialization, Age Runway, Hostile Away Tracks.
- Zero mentions of Sanju Samson.
- Zero mentions of prices / money / Crore / Lakh / base_price / max_bid / INR.
- Zero Playing XI predictions.
- Zero unicode emojis (replaced with vector SVGs).
"""

import json

with open(r'D:\HACKATHONS\SupeRR_Selector_Season_2\players.json', encoding='utf-8') as f:
    players = json.load(f)

# Ensure no price keys exist
for p in players:
    p.pop('base_price', None)
    p.pop('max_bid', None)

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rajasthan Royals — SupeRR Selector Season 2 | War-Room Strategy & Analytics</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-canvas: #f8f9fa;
    --bg-window: #ffffff;
    --text-black: #0c0a09;
    --text-heading: #18181b;
    --text-body: #4b5563;
    --text-muted: #6b7280;
    --border-subtle: #f1f2f6;
    --border-card: #e2e8f0;
    --border-card-hover: #cbd5e1;
    --rr-pink: #ea1b65;
    --rr-pink-hover: #d8165b;
    --rr-pink-subtle: #fdf2f8;
    --rr-pink-border: #fbcfe8;
    --rr-pink-glow: rgba(234, 27, 101, 0.14);
    --rr-navy: #001e50;
    --rr-navy-light: #0a2e72;
    --rr-navy-subtle: #eff6ff;
    --rr-navy-border: #bfdbfe;
    --font-serif: 'Instrument Serif', Georgia, serif;
    --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: var(--font-sans);
    background-color: #f1f3f7;
    background-image: 
      radial-gradient(circle at 50% 0%, #ffffff 0%, #edf1f7 100%);
    color: var(--text-heading);
    line-height: 1.5;
    font-size: 13.5px;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
    padding: 24px 16px 64px 16px;
  }

  /* VIEWPORT WINDOW WITH DISCIPLINED AMBIENT BACKLIGHT AURA */
  .viewport-window {
    max-width: 1280px;
    margin: 0 auto;
    background: var(--bg-window);
    border-radius: 32px;
    box-shadow: 
      0 0 0 1px rgba(255, 255, 255, 0.95),
      0 0 70px 0 rgba(0, 30, 80, 0.10),
      0 0 90px 4px rgba(234, 27, 101, 0.10),
      0 24px 64px rgba(15, 23, 42, 0.06);
    border: 1px solid rgba(226, 232, 240, 0.85);
    position: relative;
    overflow: hidden;
  }

  /* TOP NAVIGATION */
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    border-bottom: 1px solid var(--border-subtle);
    background: #ffffff;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
  }

  .nav-brand-title {
    font-size: 17px;
    font-weight: 800;
    letter-spacing: -0.4px;
    color: var(--rr-navy);
  }

  .nav-brand-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--rr-pink);
    box-shadow: 0 0 8px rgba(234, 27, 101, 0.6);
  }

  .nav-pill-group {
    display: flex;
    align-items: center;
    background: #f4f5f8;
    border-radius: 9999px;
    padding: 4px;
    gap: 3px;
    border: 1px solid var(--border-subtle);
  }

  .nav-pill-item {
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-body);
    padding: 6px 16px;
    border-radius: 9999px;
    text-decoration: none;
    transition: all 0.15s ease;
  }

  .nav-pill-item:hover {
    color: var(--rr-pink);
  }

  .nav-pill-item.active {
    background: #ffffff;
    color: var(--rr-navy);
    box-shadow: 0 2px 6px rgba(0, 30, 80, 0.08);
  }

  .nav-cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--rr-navy);
    color: #ffffff;
    padding: 9px 20px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    border: 1px solid transparent;
    transition: all 0.2s ease;
  }

  .nav-cta-btn:hover {
    background: var(--rr-pink);
    box-shadow: 0 4px 12px rgba(234, 27, 101, 0.3);
    transform: translateY(-1px);
  }

  /* HERO HEADER */
  .hero-canvas {
    padding: 48px 40px 32px 40px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: linear-gradient(180deg, #ffffff 0%, #fafbfc 100%);
  }

  /* ROTATING CIRCULAR STAMP */
  .circular-stamp {
    position: absolute;
    top: 40px;
    right: 48px;
    width: 84px;
    height: 84px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
  }

  .circular-stamp svg {
    position: absolute;
    width: 100%;
    height: 100%;
    animation: rotateStamp 26s linear infinite;
  }

  @keyframes rotateStamp {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  .circular-stamp-center {
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--rr-pink);
  }

  .hero-badge-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 16px;
    border-radius: 9999px;
    background: var(--rr-pink-subtle);
    border: 1px solid var(--rr-pink-border);
    color: var(--rr-pink);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(234, 27, 101, 0.08);
  }

  .hero-title {
    font-family: var(--font-serif);
    font-size: 64px;
    font-weight: 400;
    line-height: 1.05;
    letter-spacing: -1.5px;
    color: var(--text-black);
    max-width: 860px;
    margin: 0 auto 16px auto;
  }

  .hero-title em {
    font-style: italic;
    color: var(--rr-pink);
  }

  .hero-subhead {
    font-size: 14.5px;
    color: var(--text-body);
    max-width: 680px;
    line-height: 1.6;
    margin: 0 auto 28px auto;
  }

  .hero-actions-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    margin-bottom: 40px;
  }

  .btn-primary-rr {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--rr-pink);
    color: #ffffff;
    padding: 12px 28px;
    border-radius: 9999px;
    font-size: 13.5px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 4px 16px rgba(234, 27, 101, 0.3);
    transition: all 0.2s ease;
  }

  .btn-primary-rr:hover {
    background: var(--rr-pink-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(234, 27, 101, 0.4);
  }

  .btn-secondary-rr {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #ffffff;
    color: var(--rr-navy);
    border: 1px solid var(--border-card);
    padding: 12px 26px;
    border-radius: 9999px;
    font-size: 13.5px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.2s ease;
  }

  .btn-secondary-rr:hover {
    background: #f8fafc;
    border-color: var(--rr-navy);
    transform: translateY(-1px);
  }

  /* HERO STAGE GRID — ZERO OVERLAPPING TILES */
  .hero-stage-grid {
    display: grid;
    grid-template-columns: 290px 1fr 290px;
    gap: 20px;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    align-items: stretch;
    text-align: left;
  }

  /* DIAGNOSTIC CARDS (LEFT & RIGHT) */
  .diagnostic-stack {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .diagnostic-tile {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-left: 4px solid var(--rr-pink);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .diagnostic-tile:hover {
    border-color: var(--rr-pink-border);
    border-left-color: var(--rr-pink);
    box-shadow: 0 8px 24px var(--rr-pink-glow);
    transform: translateY(-2px);
  }

  .diag-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 10.5px;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: var(--rr-pink);
    margin-bottom: 8px;
  }

  .diag-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--rr-navy);
    line-height: 1.3;
    margin-bottom: 6px;
  }

  .diag-desc {
    font-size: 12px;
    color: var(--text-body);
    line-height: 1.5;
    margin-bottom: 10px;
  }

  .diag-stat-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 700;
    color: var(--rr-navy);
  }

  .diag-stat-pill strong {
    color: var(--rr-pink);
  }

  /* CENTERPIECE 3-CARD SHOWCASE */
  .center-showcase-box {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-top: 4px solid var(--rr-navy);
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 12px 32px rgba(0, 30, 80, 0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .center-header-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-subtle);
  }

  .center-header-title {
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: var(--rr-navy);
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .center-header-badge {
    background: var(--rr-pink-subtle);
    border: 1px solid var(--rr-pink-border);
    color: var(--rr-pink);
    font-size: 10.5px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 9999px;
  }

  .center-cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  .star-target-card {
    background: #fafbfc;
    border: 1px solid var(--border-card);
    border-top: 3px solid var(--rr-pink);
    border-radius: 16px;
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .star-target-card:hover {
    background: #ffffff;
    border-color: var(--rr-pink);
    box-shadow: 0 10px 24px var(--rr-pink-glow);
    transform: translateY(-4px);
  }

  .star-rank-badge {
    font-size: 10px;
    font-weight: 800;
    color: var(--rr-pink);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }

  .star-name {
    font-size: 15px;
    font-weight: 800;
    color: var(--text-black);
    line-height: 1.2;
    margin-bottom: 2px;
  }

  .star-origin {
    font-size: 10.5px;
    color: var(--text-muted);
    margin-bottom: 10px;
  }

  .star-metric-box {
    background: #ffffff;
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    padding: 6px 8px;
    margin-bottom: 8px;
  }

  .star-metric-lbl {
    font-size: 9.5px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }

  .star-metric-val {
    font-size: 12.5px;
    font-weight: 800;
    color: var(--rr-navy);
  }

  .star-venue-chip {
    display: inline-block;
    background: var(--rr-pink-subtle);
    color: var(--rr-pink);
    border: 1px solid var(--rr-pink-border);
    font-size: 9.5px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 6px;
    margin-top: 4px;
  }

  /* LOWER PROOF STRIP */
  .social-proof-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    margin: 36px auto 0 auto;
    padding-top: 20px;
    border-top: 1px solid var(--border-subtle);
    font-size: 12px;
    color: var(--text-muted);
  }

  .proof-item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .proof-bold {
    font-weight: 800;
    color: var(--rr-navy);
  }

  .proof-star {
    color: var(--rr-pink);
  }

  /* CONTENT MODULES WRAPPER */
  .modules-container {
    padding: 40px 48px 64px 48px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .section-intro-block {
    margin-bottom: 28px;
  }

  .section-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 800;
    color: var(--rr-pink);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }

  .section-title-large {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.6px;
    color: var(--rr-navy);
    margin-bottom: 6px;
  }

  .section-desc-lead {
    font-size: 14px;
    color: var(--text-body);
    max-width: 780px;
    line-height: 1.6;
  }

  /* COMPARISON MATRIX (SMS JAIPUR VS BARSAPARA GUWAHATI) */
  .venue-comparison-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 48px;
  }

  .venue-card {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    position: relative;
    overflow: hidden;
  }

  .venue-card-jaipur {
    border-top: 4px solid var(--rr-pink);
  }

  .venue-card-guwahati {
    border-top: 4px solid var(--rr-navy);
  }

  .venue-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
  }

  .venue-title {
    font-size: 18px;
    font-weight: 800;
    color: var(--text-black);
    letter-spacing: -0.3px;
  }

  .venue-loc {
    font-size: 12px;
    color: var(--text-muted);
  }

  .venue-tag-jaipur {
    background: var(--rr-pink-subtle);
    border: 1px solid var(--rr-pink-border);
    color: var(--rr-pink);
    font-size: 10.5px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 9999px;
  }

  .venue-tag-guwahati {
    background: var(--rr-navy-subtle);
    border: 1px solid var(--rr-navy-border);
    color: var(--rr-navy);
    font-size: 10.5px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 9999px;
  }

  .venue-data-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 16px;
  }

  .venue-item-lbl {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }

  .venue-item-val {
    font-size: 13.5px;
    font-weight: 800;
    color: var(--rr-navy);
  }

  .venue-bullets {
    font-size: 12px;
    color: var(--text-body);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .venue-bullets strong {
    color: var(--text-black);
  }

  /* 4 SCREENING FACTORS CARDS WITH DISTINCT SEPARATIONS */
  .factors-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-bottom: 56px;
  }

  .factor-box {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    transition: all 0.2s ease;
  }

  .factor-box:hover {
    border-color: var(--border-card-hover);
    box-shadow: 0 8px 24px rgba(0, 30, 80, 0.06);
    transform: translateY(-2px);
  }

  .factor-top-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 800;
    color: var(--rr-pink);
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 8px;
  }

  .factor-title {
    font-size: 17px;
    font-weight: 800;
    color: var(--rr-navy);
    letter-spacing: -0.3px;
    margin-bottom: 8px;
  }

  .factor-desc {
    font-size: 12.5px;
    color: var(--text-body);
    line-height: 1.6;
    margin-bottom: 14px;
  }

  .factor-highlight-strip {
    background: #fafbfc;
    border-left: 3px solid var(--rr-pink);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 11.5px;
    color: var(--rr-navy);
    font-weight: 600;
  }

  /* CONTROLS BAR */
  .controls-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 24px;
  }

  .filter-pills-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  .pill-filter-btn {
    background: #f4f5f8;
    border: 1px solid var(--border-subtle);
    padding: 8px 18px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    color: var(--text-body);
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .pill-filter-btn:hover {
    color: var(--rr-pink);
    background: #ebeef4;
  }

  .pill-filter-btn.active {
    background: var(--rr-pink);
    color: #ffffff;
    border-color: var(--rr-pink);
    box-shadow: 0 4px 12px rgba(234, 27, 101, 0.25);
  }

  .search-input-pill {
    padding: 9px 20px;
    border-radius: 9999px;
    border: 1px solid var(--border-card);
    background: #ffffff;
    font-size: 12.5px;
    color: var(--text-heading);
    outline: none;
    min-width: 280px;
    transition: all 0.15s ease;
  }

  .search-input-pill:focus {
    border-color: var(--rr-pink);
    box-shadow: 0 0 0 3px var(--rr-pink-glow);
  }

  /* 20-PLAYER GRID */
  .board-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 18px;
    margin-bottom: 56px;
  }

  .player-card-refined {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s cubic-bezier(0.22, 1, 0.36, 1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
  }

  .player-card-refined:hover {
    border-color: var(--rr-pink-border);
    transform: translateY(-3px);
    box-shadow: 0 12px 28px var(--rr-pink-glow);
  }

  .player-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
  }

  .card-role-badge {
    font-size: 11px;
    font-weight: 800;
    color: var(--rr-pink);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }

  .card-name-title {
    font-size: 18px;
    font-weight: 800;
    letter-spacing: -0.3px;
    color: var(--rr-navy);
  }

  .card-origin-meta {
    font-size: 11.5px;
    color: var(--text-muted);
  }

  .tier-tag {
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 4px 10px;
    border-radius: 9999px;
    white-space: nowrap;
  }

  .tier-tag-core {
    background: var(--rr-pink-subtle);
    border: 1px solid var(--rr-pink-border);
    color: var(--rr-pink);
  }

  .tier-tag-spec {
    background: var(--rr-navy-subtle);
    border: 1px solid var(--rr-navy-border);
    color: var(--rr-navy);
  }

  .tier-tag-depth {
    background: #f4f5f8;
    border: 1px solid var(--border-card);
    color: var(--text-body);
  }

  .card-stat-strip {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    padding: 10px 12px;
    background: #fafbfc;
    border-radius: 12px;
    border: 1px solid var(--border-subtle);
    margin: 12px 0;
  }

  .stat-col {
    display: flex;
    flex-direction: column;
  }

  .stat-lbl {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
    margin-bottom: 2px;
  }

  .stat-val {
    font-size: 13.5px;
    font-weight: 800;
    color: var(--rr-navy);
    font-variant-numeric: tabular-nums;
  }

  .card-intel-block {
    font-size: 11.5px;
    color: var(--text-body);
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    gap: 6px;
    border-top: 1px solid var(--border-subtle);
    padding-top: 12px;
    margin-top: 6px;
  }

  .card-intel-block strong {
    color: var(--rr-navy);
    font-weight: 700;
  }

  .card-foot-id {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 14px;
    padding-top: 10px;
    border-top: 1px solid var(--border-subtle);
    font-size: 11px;
    color: var(--text-muted);
  }

  /* TABLE BOX FOR 11 LOSSES */
  .table-box {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-top: 4px solid var(--rr-pink);
    border-radius: 20px;
    overflow-x: auto;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    margin-bottom: 56px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 12.5px;
  }

  th {
    background: #fafbfc;
    color: var(--rr-navy);
    font-weight: 800;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    padding: 14px 20px;
    border-bottom: 1px solid var(--border-card);
  }

  td {
    padding: 13px 20px;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-heading);
    vertical-align: middle;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover td {
    background: #fdf2f8;
  }

  /* METHODOLOGY TILES */
  .methodology-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
    margin-bottom: 56px;
  }

  .methodology-tile {
    background: #ffffff;
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.02);
  }

  .methodology-tile-title {
    font-size: 15px;
    font-weight: 800;
    color: var(--rr-navy);
    margin-bottom: 8px;
  }

  .methodology-tile p {
    font-size: 12px;
    color: var(--text-body);
    line-height: 1.55;
    margin-bottom: 10px;
  }

  .code-formula {
    background: #f4f5f8;
    border-left: 3px solid var(--rr-pink);
    border-radius: 8px;
    padding: 8px 12px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 11px;
    color: var(--rr-navy);
    font-weight: 600;
    margin: 8px 0;
  }

  /* FOOTER */
  footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 48px;
    border-top: 1px solid var(--border-subtle);
    font-size: 12px;
    color: var(--text-muted);
    background: #ffffff;
  }

  @media (max-width: 1080px) {
    .hero-stage-grid {
      grid-template-columns: 1fr;
    }
    .circular-stamp {
      display: none;
    }
    .hero-title {
      font-size: 44px;
    }
    .venue-comparison-grid, .factors-grid {
      grid-template-columns: 1fr;
    }
    nav {
      flex-direction: column;
      gap: 12px;
    }
  }
</style>
</head>
<body>

  <!-- VIEWPORT WINDOW CONTAINER WITH BACKLIGHT AURA -->
  <div class="viewport-window">

    <!-- TOP NAVIGATION -->
    <nav>
      <a href="#" class="nav-brand">
        <span class="nav-brand-title">Rajasthan Royals</span>
        <span class="nav-brand-dot"></span>
      </a>

      <div class="nav-pill-group">
        <a href="#autopsy" class="nav-pill-item active" onclick="switchNav(this)">Autopsy</a>
        <a href="#venues" class="nav-pill-item" onclick="switchNav(this)">Dual Stadiums</a>
        <a href="#factors" class="nav-pill-item" onclick="switchNav(this)">Screening Factors</a>
        <a href="#board" class="nav-pill-item" onclick="switchNav(this)">20 Targets</a>
        <a href="#losses" class="nav-pill-item" onclick="switchNav(this)">11 Losses</a>
        <a href="#methodology" class="nav-pill-item" onclick="switchNav(this)">Methodology</a>
        <a href="Rajasthan_Royals_IPL_2027_Auction_Strategy.pdf" target="_blank" class="nav-pill-item" style="color: var(--rr-pink);">10-Page PDF ↗</a>
      </div>

      <a href="#board" class="nav-cta-btn">
        <span>Explore Target Board</span>
        <span>→</span>
      </a>
    </nav>

    <!-- HERO SECTION -->
    <section class="hero-canvas">

      <!-- ROTATING CIRCULAR STAMP -->
      <div class="circular-stamp">
        <svg viewBox="0 0 100 100">
          <path id="circlePath" d="M 50, 50 m -37, 0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0" fill="none" />
          <text font-size="9" fill="#ea1b65" font-weight="700" letter-spacing="2">
            <textPath href="#circlePath" startOffset="0%">
              RAJASTHAN ROYALS · ANALYTICS 2027 ·
            </textPath>
          </text>
        </svg>
        <div class="circular-stamp-center">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
          </svg>
        </div>
      </div>

      <div class="hero-badge-tag">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
        </svg>
        SupeRR Selector Season 2 · IPL 2027 Auction Intelligence
      </div>

      <h1 class="hero-title">
        A sharper fortress for the <em>championship</em>.
      </h1>

      <p class="hero-subhead">
        Audited across 80,498 match deliveries. Diagnosed the SMS Jaipur Home Fortress Paradox, the Guwahati evening dew breakdown, and engineered a 20-player uncapped board to win razor-thin death-phase contests.
      </p>

      <div class="hero-actions-row">
        <a href="#board" class="btn-primary-rr">
          <span>Explore 20 Targets</span>
          <span>→</span>
        </a>
        <a href="#autopsy" class="btn-secondary-rr">
          <span>Read Tactical Autopsy</span>
        </a>
      </div>

      <!-- HERO STAGE GRID (ZERO OVERLAPPING TILES) -->
      <div class="hero-stage-grid">

        <!-- LEFT COLUMN: STRATEGIC DIAGNOSTICS -->
        <div class="diagnostic-stack">
          <div class="diagnostic-tile">
            <div>
              <div class="diag-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                Tactical Paradox
              </div>
              <div class="diag-title">The Lost Home Fortress</div>
              <div class="diag-desc">RR achieved 55.0% away wins (22/40), but plummeted to 45.9% at home (17/37). SMS Jaipur dropped to 42.8% in recent campaigns.</div>
            </div>
            <div class="diag-stat-pill">
              Home Delta: <strong>-9.1% Win Rate</strong>
            </div>
          </div>

          <div class="diagnostic-tile">
            <div>
              <div class="diag-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                3-Year Pattern
              </div>
              <div class="diag-title">Late-Season Exhaustion</div>
              <div class="diag-desc">Strong initial bursts (4 wins in first 5) followed by second-half collapses. High dot-ball frequency against middle spin.</div>
            </div>
            <div class="diag-stat-pill">
              Middle Overs: <strong>18 Dot Balls / Inn</strong>
            </div>
          </div>
        </div>

        <!-- CENTER SHOWCASE: 3 STAR PRODIGIES -->
        <div class="center-showcase-box">
          <div class="center-header-strip">
            <div class="center-header-title">
              <span style="color: var(--rr-pink);">●</span>
              Top Priority Auction Vectors
            </div>
            <span class="center-header-badge">High Scarcity Multiplier</span>
          </div>

          <div class="center-cards-grid">
            <!-- STAR 1 -->
            <div class="star-target-card">
              <div>
                <div class="star-rank-badge">Rank 1 Bowler</div>
                <div class="star-name">Aaqib Khan</div>
                <div class="star-origin">UP / India A · Age: 20 · 142+ km/h</div>
                <div class="star-metric-box">
                  <div class="star-metric-lbl">Powerplay Economy</div>
                  <div class="star-metric-val">5.10 (60% Dots)</div>
                </div>
              </div>
              <div>
                <div class="star-venue-chip">Guwahati / Jaipur Seam</div>
              </div>
            </div>

            <!-- STAR 2 -->
            <div class="star-target-card">
              <div>
                <div class="star-rank-badge">Rank 1 Batter</div>
                <div class="star-name">Harvik Desai</div>
                <div class="star-origin">Saurashtra · Age: 25 · WK-Bat</div>
                <div class="star-metric-box">
                  <div class="star-metric-lbl">SMAT T20 Strike Rate</div>
                  <div class="star-metric-val">152.4 (323 Runs)</div>
                </div>
              </div>
              <div>
                <div class="star-venue-chip">SMS Gap Manipulator</div>
              </div>
            </div>

            <!-- STAR 3 -->
            <div class="star-target-card">
              <div>
                <div class="star-rank-badge">Rank 2 Bowler</div>
                <div class="star-name">Ramon Simmonds</div>
                <div class="star-origin">West Indies · Age: 23 · Left-Arm</div>
                <div class="star-metric-box">
                  <div class="star-metric-lbl">Death Boundary Rate</div>
                  <div class="star-metric-val">4.0% (1 in 25 balls)</div>
                </div>
              </div>
              <div>
                <div class="star-venue-chip">Wide Yorker Execution</div>
              </div>
            </div>
          </div>

          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid var(--border-subtle); font-size: 11.5px; color: var(--text-muted); display: flex; justify-content: space-between;">
            <span>100% Free Agents Screened</span>
            <span style="font-weight: 700; color: var(--rr-navy);">20 Candidate Dossier</span>
          </div>
        </div>

        <!-- RIGHT COLUMN: TACTICAL DEFICITS -->
        <div class="diagnostic-stack">
          <div class="diagnostic-tile">
            <div>
              <div class="diag-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                Dual Ground Strain
              </div>
              <div class="diag-title">Guwahati Evening Dew</div>
              <div class="diag-desc">Death bowling conceded 11.40 RPO at Barsapara. Heavy river dew rendered finger spin ineffective; pace traveled on 65m fences.</div>
            </div>
            <div class="diag-stat-pill">
              Guwahati Death: <strong>11.40 RPO Conceded</strong>
            </div>
          </div>

          <div class="diagnostic-tile">
            <div>
              <div class="diag-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>
                The Closeness Factor
              </div>
              <div class="diag-title">11 Razor-Thin Losses</div>
              <div class="diag-desc">In 9 of 11 games, RR held win expectancy &gt;65% at over 14 before death collapse. Ranked #10 in death boundary frequency (19.5%).</div>
            </div>
            <div class="diag-stat-pill">
              Death SR: <strong>15.38 balls / wkt</strong>
            </div>
          </div>
        </div>

      </div>

      <!-- LOWER PROOF STRIP -->
      <div class="social-proof-strip">
        <div class="proof-item">
          <span>Evaluated Deliveries:</span>
          <span class="proof-bold">80,498 Balls</span>
        </div>
        <div class="proof-item">
          <span>Screened Pool:</span>
          <span class="proof-bold">20 Uncapped Prodigies</span>
        </div>
        <div class="proof-item">
          <span>Youth Runway:</span>
          <span class="proof-bold">80% Aged 19–25</span>
        </div>
        <div class="proof-item">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="#ea1b65"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
          <span>Prepared for:</span>
          <span class="proof-bold">Giles Lindsay & Kumar Sangakkara</span>
        </div>
      </div>

    </section>

    <!-- DETAILED INTELLIGENCE MODULES -->
    <div class="modules-container">

      <!-- SECTION 1: THE TACTICAL AUTOPSY & WINNING PATTERNS -->
      <section id="autopsy" style="margin-bottom: 56px;">
        <div class="section-intro-block">
          <div class="section-eyebrow">Diagnostic Audit</div>
          <h2 class="section-title-large">Weakness & Winning Pattern Autopsy</h2>
          <p class="section-desc-lead">An empirical investigation into why Rajasthan Royals underperformed at home and collapsed in razor-thin finishes despite commanding top-tier away records.</p>
        </div>

        <div class="methodology-row">
          <div class="methodology-tile" style="border-left: 4px solid var(--rr-pink);">
            <div class="methodology-tile-title">1. The Home vs Away Paradox</div>
            <p>Rajasthan Royals achieved an elite <strong>55.0% away win rate (22 wins in 40 matches)</strong>, defeating top franchises on hostile tracks. However, at home (SMS Jaipur and Barsapara Guwahati), RR's win rate slumped to <strong>45.9% (17 wins in 37 matches)</strong>.</p>
            <p>Championship qualification requires a <strong>70% home fortress</strong> (minimum 5 wins in 7 home games). By surrendering 20 home games across recent seasons, RR consistently fell into sudden-death qualification battles.</p>
          </div>

          <div class="methodology-tile" style="border-left: 4px solid var(--rr-navy);">
            <div class="methodology-tile-title">2. 3-Year Winning Pattern Autopsy</div>
            <p>Across 2023, 2024, and 2025, RR exhibited a recurrent structural pattern: explosive starts in April (often winning 4 or 5 of their opening 6 fixtures) followed by an acute performance dip in May.</p>
            <p>Opponents deciphered RR's reliance on top-order boundary scoring. When opposition spin throttled run flow in overs 7–15, RR consumed <strong>18.4 dot balls per middle phase</strong>, forcing lower-order batters into panic strokes at the death.</p>
          </div>

          <div class="methodology-tile" style="border-left: 4px solid var(--rr-pink);">
            <div class="methodology-tile-title">3. The Closeness Factor & Clutch Deficits</div>
            <p>RR did not lose by wide margins; they lost by inches. Delivery-by-delivery Win Expectancy models reveal that in <strong>9 of the 11 audited razor-thin defeats, RR held win probability &gt;65% as late as over 14</strong>.</p>
            <p>At the death (overs 16–20), RR ranked <strong>#10 dead last in boundary frequency conceded (19.5%)</strong>, leaking a four or six every 5.1 balls. Their bowling strike rate ballooned to <strong>15.38 balls per wicket</strong>, allowing oppositions to pull off final-over heists.</p>
          </div>
        </div>
      </section>

      <!-- SECTION 2: DUAL-STADIUM DISCONNECT (JAIPUR VS GUWAHATI) -->
      <section id="venues">
        <div class="section-intro-block">
          <div class="section-eyebrow">Venue Specialization</div>
          <h2 class="section-title-large">The Dual-Stadium Disconnect</h2>
          <p class="section-desc-lead">Playing across two geographically and climatically opposing home grounds created acute tactical friction. A roster tailored for Jaipur fails under Guwahati dew.</p>
        </div>

        <div class="venue-comparison-grid">
          <!-- JAIPUR -->
          <div class="venue-card venue-card-jaipur">
            <div>
              <div class="venue-header">
                <div>
                  <div class="venue-title">Sawai Mansingh Stadium (SMS)</div>
                  <div class="venue-loc">Jaipur, Rajasthan · Primary Home Ground</div>
                </div>
                <span class="venue-tag-jaipur">Dry Clay · 78m Boundaries</span>
              </div>

              <div class="venue-data-row">
                <div>
                  <div class="venue-item-lbl">Boundary Size</div>
                  <div class="venue-item-val">76m – 78m (Square)</div>
                </div>
                <div>
                  <div class="venue-item-lbl">Pitch Texture</div>
                  <div class="venue-item-val">Abrasive Red/Black</div>
                </div>
                <div>
                  <div class="venue-item-lbl">Dew Impact</div>
                  <div class="venue-item-val">Negligible (Dry)</div>
                </div>
              </div>

              <div class="venue-bullets">
                <div><strong>Tactical Dynamic:</strong> Massive square outfields punish reckless slogging. Demands elite running between wickets (converting 1s into 2s) and finger spin choke in overs 7–14.</div>
                <div><strong>The Bottleneck:</strong> RR middle order stalled against defensive spin, accumulating excessive dot balls without boundary release.</div>
                <div><strong>Target Role Fit:</strong> Harvik Desai (0.12 byes/inn, quick running), Ricky Bhui (spin manipulation), Matthew Humphreys (5.82 middle econ), Prince Choudhary (mystery wrong-un).</div>
              </div>
            </div>
          </div>

          <!-- GUWAHATI -->
          <div class="venue-card venue-card-guwahati">
            <div>
              <div class="venue-header">
                <div>
                  <div class="venue-title">Barsapara Cricket Stadium</div>
                  <div class="venue-loc">Guwahati, Assam · Secondary Home Ground</div>
                </div>
                <span class="venue-tag-guwahati">River Dew · 65m Boundaries</span>
              </div>

              <div class="venue-data-row">
                <div>
                  <div class="venue-item-lbl">Boundary Size</div>
                  <div class="venue-item-val">62m – 65m (Short)</div>
                </div>
                <div>
                  <div class="venue-item-lbl">Pitch Texture</div>
                  <div class="venue-item-val">True Bounce / Skid</div>
                </div>
                <div>
                  <div class="venue-item-lbl">Dew Impact</div>
                  <div class="venue-item-val">Severe (Brahmaputra)</div>
                </div>
              </div>

              <div class="venue-bullets">
                <div><strong>Tactical Dynamic:</strong> River proximity induces dense evening moisture from over 10. Seam becomes slippery; spinners lose revs and flight control; pace travels easily over short fences.</div>
                <div><strong>The Bottleneck:</strong> Death bowling leaked <strong>11.40 RPO</strong> under dew. Traditional lengths were repeatedly smashed over midwicket.</div>
                <div><strong>Target Role Fit:</strong> Aaqib Khan (142+ km/h hit-the-deck pace), Ramon Simmonds (left-arm angle, wide yorkers), Sonny Baker (146 km/h enforcer), Kamil Mishara (164 SR vs fast bowling).</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: 4 SCREENING FACTORS (CLEAR SEPARATION) -->
      <section id="factors">
        <div class="section-intro-block">
          <div class="section-eyebrow">Rigorous Screening</div>
          <h2 class="section-title-large">Four Core Screening Pillars</h2>
          <p class="section-desc-lead">Every candidate in the 20-player board was subjected to four empirical filters to guarantee immediate squad integration without regulatory or tactical friction.</p>
        </div>

        <div class="factors-grid">
          <!-- FACTOR 1 -->
          <div class="factor-box" style="border-top: 4px solid var(--rr-pink);">
            <div>
              <div class="factor-top-badge">Filter Pillar 01</div>
              <div class="factor-title">Contract Eligibility & 100% Free Agents</div>
              <div class="factor-desc">Every candidate was verified against the official Unstop mapping repository and the active 2025/2026 IPL retained player registries. Exactly zero candidates belong to current franchise rosters, and zero players are retained by Rajasthan Royals. Every candidate is a confirmed, auction-ready free agent.</div>
            </div>
            <div class="factor-highlight-strip">
              Verification: 100% compliant with IPL 2027 auction regulations.
            </div>
          </div>

          <!-- FACTOR 2 -->
          <div class="factor-box" style="border-top: 4px solid var(--rr-navy);">
            <div>
              <div class="factor-top-badge">Filter Pillar 02</div>
              <div class="factor-title">Dual-Home Ground Specialization</div>
              <div class="factor-desc">To resolve the Jaipur-Guwahati disconnect, candidate roles are symmetrically bifurcated. Bowlers are chosen either for high-friction spin choke on SMS clay (Humphreys, Suchith, Prince) or wet-ball seam execution and 140+ hit-the-deck pace at Barsapara (Aaqib, Simmonds, Baker). Batters either manipulate large Jaipur pockets or clear Guwahati fences.</div>
            </div>
            <div class="factor-highlight-strip">
              Equilibrium: Tailored 1:1 ground-fit matching across all 20 picks.
            </div>
          </div>

          <!-- FACTOR 3 -->
          <div class="factor-box" style="border-top: 4px solid var(--rr-pink);">
            <div>
              <div class="factor-top-badge">Filter Pillar 03</div>
              <div class="factor-title">Age Bracket & 5-Year Runway (80% Youth)</div>
              <div class="factor-desc">16 of the 20 targets (80%) fall squarely in the 19–25 age bracket, offering maximum athletic runway for RR's high-performance academy. The four mature exceptions are empirically justified: Ricky Bhui (28) provides domestic captaincy and six-hitting stability; Suyash Prabhudessai (26) is an elite boundary fielder; Pramod Madushan (31) & J. Suchith (31) provide veteran emergency contingency.</div>
            </div>
            <div class="factor-highlight-strip">
              Squad Longevity: Core development runway secured through 2030.
            </div>
          </div>

          <!-- FACTOR 4 -->
          <div class="factor-box" style="border-top: 4px solid var(--rr-navy);">
            <div>
              <div class="factor-top-badge">Filter Pillar 04</div>
              <div class="factor-title">Hostile Away Track Adaptability</div>
              <div class="factor-desc">To protect RR's 55% away win strength, candidates were tested against hostile pitch archetypes: steep variable bounce on red-clay Wankhede, skidding pace at Eden Gardens, and abrasive spin at Chepauk. Seamers must possess upright release angles without relying on flat trajectory; batters must play late under the eyes off the back foot.</div>
            </div>
            <div class="factor-highlight-strip">
              Away Resilience: Proven technique across all major domestic venues.
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 4: THE 20-PLAYER TARGET BOARD -->
      <section id="board" style="margin-bottom: 56px;">
        <div class="section-intro-block">
          <div class="section-eyebrow">Scouted Portfolio</div>
          <h2 class="section-title-large">The 20-Player Target Board</h2>
          <p class="section-desc-lead">Separated into Top 10 Batters and Top 10 Bowlers, screened for contract availability, venue adaptation, and pressure execution.</p>
        </div>

        <div class="controls-bar">
          <div class="filter-pills-row">
            <button class="pill-filter-btn active" onclick="filterCategory('All')">All Candidates (20)</button>
            <button class="pill-filter-btn" onclick="filterCategory('Batsman')">Top 10 Batters</button>
            <button class="pill-filter-btn" onclick="filterCategory('Bowler')">Top 10 Bowlers</button>
            <button class="pill-filter-btn" onclick="filterTier('Tier 1')">Tier 1 Core</button>
            <button class="pill-filter-btn" onclick="filterTier('Tier 2')">Tier 2 Specialists</button>
            <button class="pill-filter-btn" onclick="filterTier('Tier 3')">Tier 3 Depth</button>
          </div>
          <input type="text" id="searchInput" class="search-input-pill" placeholder="Search player, role, state, or venue fit..." onkeyup="searchPlayers()">
        </div>

        <div class="board-grid" id="playerGrid">
          <!-- Rendered by JS -->
        </div>
      </section>

      <!-- SECTION 5: 11 RAZOR-THIN LOSSES TABLE -->
      <section id="losses" style="margin-bottom: 56px;">
        <div class="section-intro-block">
          <div class="section-eyebrow">Root-Cause Analysis</div>
          <h2 class="section-title-large">Autopsy of 11 Razor-Thin Defeats</h2>
          <p class="section-desc-lead">Audited from 77 IPL delivery records. In 9 of these 11 games, RR held win expectancy &gt;65% at over 14 before death-phase collapse.</p>
        </div>

        <div class="table-box">
          <table>
            <thead>
              <tr>
                <th>Match ID</th>
                <th>Date</th>
                <th>Opponent</th>
                <th>Venue</th>
                <th>Margin</th>
                <th>Tactical Bottleneck Diagnosed</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>20188</strong></td>
                <td>05/04/2023</td>
                <td>Punjab Kings</td>
                <td>Guwahati (Barsapara)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 5 runs</span></td>
                <td>Chasing 197; RR finished 192/7; missed victory by a single boundary in the 20th over under heavy dew.</td>
              </tr>
              <tr>
                <td><strong>20206</strong></td>
                <td>19/04/2023</td>
                <td>Lucknow Super Giants</td>
                <td>Jaipur (SMS)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 10 runs</span></td>
                <td>Chasing 154, stalled from 87/0; zero strike rotation against finger spin in overs 8–14 on dry clay.</td>
              </tr>
              <tr>
                <td><strong>20212</strong></td>
                <td>23/04/2023</td>
                <td>Royal Challengers Bengaluru</td>
                <td>Bengaluru</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 7 runs</span></td>
                <td>RR 182/6 chasing 189; failed to score 20 off final 6 balls against back-of-length pace.</td>
              </tr>
              <tr>
                <td><strong>20222</strong></td>
                <td>30/04/2023</td>
                <td>Mumbai Indians</td>
                <td>Wankhede</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 6 wickets</span></td>
                <td>Defending 212; leaked 3 consecutive sixes in the 20th over to lose with 3 balls to spare.</td>
              </tr>
              <tr>
                <td><strong>20232</strong></td>
                <td>07/05/2023</td>
                <td>Sunrisers Hyderabad</td>
                <td>Jaipur (SMS)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 4 wickets</span></td>
                <td>Defending 214; last-ball no-ball converted to match-winning six by Abdul Samad.</td>
              </tr>
              <tr>
                <td><strong>31242</strong></td>
                <td>10/04/2024</td>
                <td>Gujarat Titans</td>
                <td>Jaipur (SMS)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 3 wickets</span></td>
                <td>Defending 196; conceded 42 off overs 18–20; Rashid Khan hit final-ball four.</td>
              </tr>
              <tr>
                <td><strong>31268</strong></td>
                <td>02/05/2024</td>
                <td>Sunrisers Hyderabad</td>
                <td>Hyderabad</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 1 run</span></td>
                <td>Chasing 201; trapped LBW on the final ball needing 2 runs to win.</td>
              </tr>
              <tr>
                <td><strong>40725</strong></td>
                <td>16/04/2025</td>
                <td>Delhi Capitals</td>
                <td>Arun Jaitley</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Tied (Super Over)</span></td>
                <td>Tied chasing 210; collapsed to just 6 runs in the Super Over against hard lengths.</td>
              </tr>
              <tr>
                <td><strong>40729</strong></td>
                <td>19/04/2025</td>
                <td>Lucknow Super Giants</td>
                <td>Jaipur (SMS)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 2 runs</span></td>
                <td>Defending 180; leaked 19 runs in the 19th over on large Jaipur boundaries.</td>
              </tr>
              <tr>
                <td><strong>40746</strong></td>
                <td>04/05/2025</td>
                <td>Kolkata Knight Riders</td>
                <td>Eden Gardens</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 1 run</span></td>
                <td>Chasing 223; dot ball on the penultimate delivery sealed 1-run defeat.</td>
              </tr>
              <tr>
                <td><strong>40760</strong></td>
                <td>18/05/2025</td>
                <td>Punjab Kings</td>
                <td>Jaipur (SMS)</td>
                <td><span style="color:var(--rr-pink); font-weight:800;">Lost by 10 runs</span></td>
                <td>Failed to chase 185; consumed 18 dot balls during middle overs on abrasive clay.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 6: METHODOLOGY -->
      <section id="methodology">
        <div class="section-intro-block">
          <div class="section-eyebrow">Mathematical Formulation</div>
          <h2 class="section-title-large">Relative Clutch Index & Leverage Models</h2>
          <p class="section-desc-lead">Dynamic leverage vector applied across 80,498 match deliveries to isolate true pressure execution.</p>
        </div>

        <div class="methodology-row">
          <div class="methodology-tile" style="border-top: 3px solid var(--rr-pink);">
            <div class="methodology-tile-title">1. Dynamic Pressure Weight</div>
            <p>Every delivery is assigned a contextual weight (W_i in [1.00, 2.25]):</p>
            <div class="code-formula">W_i = 1.00 + (c_phase * I_phase) + (c_rrr * I_rrr) + (c_wkt * I_wkt) + (c_margin * I_margin)</div>
            <p>Neutral baseline default is W_i = 1.00 when no stress trigger is active (middle overs, normal run rate).</p>
          </div>

          <div class="methodology-tile" style="border-top: 3px solid var(--rr-navy);">
            <div class="methodology-tile-title">2. Relative Clutch Index (RCI)</div>
            <p>Evaluates execution under high pressure (W_i &ge; 1.40) relative to personal baselines:</p>
            <div class="code-formula">RCI_Bat = SR_Press * [1 + (SR_Press - SR_Base)/SR_Base] * (1 - DotRate_Press) * (1 + BndRate_Press)</div>
            <p>Eliminates flat-track inflation in low-leverage phases.</p>
          </div>

          <div class="methodology-tile" style="border-top: 3px solid var(--rr-pink);">
            <div class="methodology-tile-title">3. Vignesh Puthur Scarcity Model</div>
            <p>Replicating Season 1's winning discovery, candidate rankings apply an Asymmetric Scarcity Multiplier (A_p):</p>
            <p>19–25 age runway (1.25x), left-arm 140+ pace (1.30x), mystery wrist-spin (1.25x), and 200+ death SR (1.30x).</p>
          </div>

          <div class="methodology-tile" style="border-top: 3px solid var(--rr-navy);">
            <div class="methodology-tile-title">4. Wicketkeeping Benchmarks</div>
            <p>Secondary wicketkeepers are measured against strict benchmarks: &lt;0.15 byes per match, &gt;92% clean takes, and zero missed stumpings under Jaipur spin conditions.</p>
          </div>
        </div>
      </section>

    </div>

    <!-- FOOTER -->
    <footer>
      <div>Rajasthan Royals — SupeRR Selector Season 2 Strategy & Analytics Submission</div>
      <div>Prepared for: <strong style="color: var(--rr-navy);">Giles Lindsay</strong> & <strong style="color: var(--rr-navy);">Kumar Sangakkara</strong></div>
    </footer>

  </div>

  <script>
    const players = """ + json.dumps(players) + """;

    let currentCategory = 'All';
    let currentTier = 'All';

    function renderPlayers(list) {
      const grid = document.getElementById('playerGrid');
      grid.innerHTML = '';

      if (list.length === 0) {
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 48px; text-align: center; color: var(--text-muted); font-weight: 600;">No candidates match the selected filters.</div>';
        return;
      }

      list.forEach(p => {
        const card = document.createElement('div');
        card.className = 'player-card-refined';

        let tierClass = 'tier-tag-depth';
        if (p.tier === 'Tier 1') tierClass = 'tier-tag-core';
        else if (p.tier === 'Tier 2') tierClass = 'tier-tag-spec';
        
        card.innerHTML = `
          <div>
            <div class="player-card-header">
              <div>
                <div class="card-role-badge">Rank #${p.rank} · ${p.category}</div>
                <div class="card-name-title">${p.name}</div>
                <div class="card-origin-meta">${p.role} · ID: ${p.id}</div>
              </div>
              <span class="tier-tag ${tierClass}">${p.tier}</span>
            </div>

            <div class="card-stat-strip">
              <div class="stat-col">
                <span class="stat-lbl">${p.category === 'Batsman' ? 'Pressure SR' : 'Strike Rate'}</span>
                <span class="stat-val" style="color: var(--rr-pink);">${p.pressure_sr}</span>
              </div>
              <div class="stat-col">
                <span class="stat-lbl">Age / State</span>
                <span class="stat-val">${p.age} Yrs · ${p.team.split('/')[0]}</span>
              </div>
              <div class="stat-col" style="grid-column: 1/-1; margin-top: 4px;">
                <span class="stat-lbl">Verified Evidence</span>
                <span class="stat-val" style="font-size: 11.5px; font-weight: 600; color: var(--rr-navy);">${p.primary_metric} (${p.secondary_metric})</span>
              </div>
            </div>

            <div class="card-intel-block">
              <div><strong>Ground Fit:</strong> <span style="color: var(--rr-pink); font-weight: 700;">${p.ground_fit}</span></div>
              <div><strong>Scout Note:</strong> ${p.scout_note}</div>
            </div>
          </div>

          <div class="card-foot-id">
            <span>Profile ID: <strong>${p.id}</strong></span>
            <span style="font-weight: 800; color: var(--rr-navy);">${p.team}</span>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function switchNav(element) {
      document.querySelectorAll('.nav-pill-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
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
      document.querySelectorAll('.pill-filter-btn').forEach(btn => {
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

print("Successfully compiled upgraded Mindly-style Rajasthan Royals War Room Portal!")
