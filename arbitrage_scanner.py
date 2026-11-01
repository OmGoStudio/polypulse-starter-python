#!/usr/bin/env python3
"""
PolyPulse Starter Kit - Polymarket Arbitrage and Microprice Scanner
Loads empirical 1Hz/4Hz orderbook ticks, calculates binary outcome parity edge,
and detects spread mispricing across Polymarket and Binance Spot anchors.
"""

import pandas as pd
from pathlib import Path

def analyze_orderbook_feed(csv_path: str = "polypulse_sample.csv"):
    print("=" * 65)
    print(" [PolyPulse] Polymarket High-Frequency Arbitrage Scanner")
    print("=" * 65)

    if not Path(csv_path).exists():
        print(f"File {csv_path} not found. Downloading preview from Hugging Face...")
        url = "https://huggingface.co/datasets/OmGoStudio/polypulse-polymarket-sample/raw/main/polypulse_sample_preview.csv"
        df = pd.read_csv(url)
    else:
        df = pd.read_csv(csv_path)

    print(f"Loaded {len(df)} discrete isochronous orderbook ticks.")
    print(f"Observation Start : {df['timestamp_utc'].iloc[0]}")
    print(f"Observation End   : {df['timestamp_utc'].iloc[-1]}")
    print("-" * 65)

    # Calculate Mispricing Basis Points: Deviation from $1.00 Parity
    # Parity Edge = 1.00 - (pm_token_up_bid + pm_token_down_bid)
    avg_parity_bps = df['parity_edge_bps'].mean()
    max_parity_bps = df['parity_edge_bps'].max()
    min_maker_cost = df['maker_pair_cost'].min()

    print(f"Average Binary Parity Edge : {avg_parity_bps:.2f} bps")
    print(f"Maximum Observed Edge      : {max_parity_bps:.2f} bps")
    print(f"Minimum Maker Pair Cost    : ${min_maker_cost:.4f} (Discounts on Outcome Sets)")
    print("-" * 65)

    # Find Top 5 Arbitrage Windows
    arb_opportunities = df[df['parity_edge_bps'] > 50].sort_values(by='parity_edge_bps', ascending=False)
    print(f"Detected {len(arb_opportunities)} ticks with >50 bps parity mispricing:")
    print(arb_opportunities[['sec', 'timestamp_utc', 'pm_token_up_bid', 'pm_token_down_bid', 'parity_edge_bps', 'maker_pair_cost']].head())
    print("=" * 65)
    print("For continuous 3-Day (259k ticks) and 4Hz Vilnius feeds, visit: https://polypulse.ogs.biz.id")

if __name__ == "__main__":
    analyze_orderbook_feed()
