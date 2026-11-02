# PolyPulse - Python Quant Starter Kit

Python toolkit for quantitative analysis, spread arbitrage, and market-making backtesting on **Polymarket CLOB Order Book Datasets**.

Powered by [PolyPulse Data Infrastructure](https://ogs.biz.id/polypulse) &bull; [Hugging Face Dataset](https://huggingface.co/datasets/OmGoStudio/polypulse-polymarket-sample)

---

## What is this?
Polymarket binary prediction contracts (UP/DOWN, YES/NO) theoretically sum to **$1.00** at any given moment. Due to discrete matching engine liquidity and cross-venue latency with Binance Spot anchors, microsecond mispricings emerge.

This starter kit demonstrates how to:
1. Ingest isochronous discrete tick matrices (1.0s and 0.25s feeds).
2. Calculate empirical **Binary Parity Edge** in basis points (bps).
3. Identify maker-taker pair execution opportunities.

---

## Quickstart

```bash
git clone https://github.com/OmGoStudio/polypulse-starter-python.git
cd polypulse-starter-python
pip install -r requirements.txt
python arbitrage_scanner.py
```

---

## Commercial Datasets

| Dataset Package | Resolution | Total Ticks | One-Time Purchase | Store Link |
| :--- | :--- | :--- | :--- | :--- |
| **3 Days Standard** | 1Hz (1.0s) | 259,200 rows | **$19 USD** | [Gumroad Checkout](https://ogshub.gumroad.com/l/ywiqa) |
| **3 Days Vilnius Feed** | 4Hz (0.25s) | 1,036,800 rows | **$49 USD** | [Gumroad Checkout](https://ogshub.gumroad.com/l/bcppkw) |
| **1 Week Bundle** | 1Hz and 4Hz | 3,024,000+ rows | **$149 USD** | [Gumroad Checkout](https://ogshub.gumroad.com/l/axwvl) |
| **1 Month Archive** | Master Grid | 10,000,000+ rows | **$299 USD** | [Gumroad Checkout](https://ogshub.gumroad.com/l/ogswmh) |

Direct Web3 Polygon POS payment available at: [https://ogs.biz.id/polypulse](https://ogs.biz.id/polypulse)

---
MIT License &bull; OGS Sovereign Commercial Infrastructure
