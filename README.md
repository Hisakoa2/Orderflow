# Aegis Order Flow

Free footprint, liquidity heatmap and order-flow terminal for gold. Runs in your browser: no install, no account, no API keys.

## ▶ Open it

**Web links (live data, nothing to download):**
- 💻 **PC / Mac:** https://hisakoa2.github.io/Orderflow/pc.html
- 📱 **iPhone:** https://hisakoa2.github.io/Orderflow/phone.html

The web link works once GitHub Pages is on: the repo must be **Public**, then **Settings → Pages → Deploy from a branch → main → / (root) → Save**.

**On iPhone:** open the link in **Safari** → Share → **Add to Home Screen**. It then opens full-screen like an app. Opening the file inside another app's preview (Claude, Files) blocks the live exchange feeds.

**Download instead:** click **[Aegis Order Flow.html](Aegis%20Order%20Flow.html)** → **Download raw file** (↓ icon, top right of the file view) and open it in Chrome. Tagged versions are also under **[Releases](../../releases)**.

## Files

| File | What it is |
|---|---|
| `Aegis Order Flow.html` | Main version (PC / Mac, also adapts to phones). This is the one that gets edited. |
| `Aegis Order Flow iPhone.html` | Phone-first layout, built from the main file |
| `index.html` | Copy of the main version, so the web link opens straight into the app |
| `manifest.json`, `icon-*.png` | App name and icon for Add to Home Screen |
| `tools/build.py` | Rebuilds `index.html` and the iPhone version from the main file |

## Data

Live trades with the real buy/sell aggressor side and full order books from public exchange websockets:

- Binance `XAUUSDT` gold perpetual (primary)
- Hyperliquid `xyz:GOLD`
- Bybit `XAUTUSDT`, OKX `XAUT-USDT-SWAP`, Kraken `PAXG/USD` (optional)

This is gold order flow from crypto exchanges, not CME futures, so treat it as a strong proxy. Prices can sit a few dollars from OANDA / TradingView: tap **⇄ Align**, type your TradingView price, and everything lines up.

## Features

- Footprint candles (bid × ask, delta, diagonal imbalances, POC), heatmap of resting liquidity, trade bubbles
- Order ladder, session volume profile, CVD, reversal signals, stacked-imbalance zones
- **Book control**: who has more resting orders within ±$3 of price, plus the biggest bid and ask walls
- **Your levels**: paste Aegis long/short levels; they're drawn on the chart with live flow at each one
- TradingView-style zoom: drag the price scale / time scale to stretch, AUTO price fit, trackpad and keyboard support
- **Aa** changes the footprint number size
- Trades are stored in your browser so history builds up across refreshes
