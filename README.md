# Aegis Order Flow

Free footprint, liquidity heatmap and order-flow terminal for gold. It runs entirely in the browser: no install, no account, no API keys.

## Files

| File | What it is |
|---|---|
| `Aegis Order Flow.html` | Main version (PC / Mac, also adapts to phones) |
| `Aegis Order Flow iPhone.html` | Phone-first layout (Panel button, big zoom buttons, pinch to zoom) |
| `index.html` | Copy of the main version, so the repo's web link opens straight into the app |

## Open it

- **PC / Mac:** download `Aegis Order Flow.html` and open it in Chrome.
- **iPhone:** open the app from its web link in Safari (Share → Add to Home Screen to use it like an app). Opening the file inside another app's preview blocks the live exchange feeds.

## Data

Live trades with real buy/sell aggressor side and full order books from public exchange websockets:

- Binance `XAUUSDT` gold perpetual (primary)
- Hyperliquid `xyz:GOLD`
- Bybit `XAUTUSDT`, OKX `XAUT-USDT-SWAP`, Kraken `PAXG/USD` (optional)

Other venues are basis-aligned onto the primary venue's price. Use ⚙ → price offset to line the axis up with your TradingView / OANDA chart. This is crypto-venue gold order flow, not CME futures, so treat it as a proxy.

## Features

- Footprint candles (bid × ask, delta, diagonal imbalances, POC), heatmap of resting liquidity, trade bubbles
- Order ladder, session volume profile, CVD, reversal signals, stacked-imbalance zones
- Your own levels: paste Aegis long/short levels and they are drawn on the chart with live flow at each level
- TradingView-style zoom: drag the price scale / time scale to stretch, AUTO price fit, trackpad and keyboard support
- Trades are stored in your browser so history builds up across refreshes
