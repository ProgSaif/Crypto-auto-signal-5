Here’s a professional **README.md** for your GitHub repo, ready to copy and paste:

---

# 🚀 Crypto Signal Bot – High Quality Signals

A **Telegram bot** that automatically scans all USDT trading pairs on Binance and posts **high-quality trading signals** using **RSI, EMA trend, volume spikes, and ATR-based TP/SL**.

Signals are posted with **debug info** and **auto-deletion** to keep your channel clean.

---

## Features ✅

* ✅ Works for **every USDT coin** on Binance.
* ✅ High-quality signals based on:

  * **RSI** (oversold/overbought detection)
  * **EMA trend** (fast vs slow EMA)
  * **Volume spike** detection
  * **ATR-based TP/SL levels**
* ✅ **Confidence scoring** for each trade.
* ✅ Auto-delete messages after a set period.
* ✅ Debug prints for **why a coin does or does not trigger a signal**.
* ✅ Safe Telegram posting with retry logic.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/crypto-signal-bot.git
cd crypto-signal-bot
```

2. **Create a Python virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file**

```env
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=@your_telegram_channel
```

---

## File Structure

```
crypto-signal-bot/
│
├─ main.py           # Main bot loop, posts signals to Telegram
├─ scanner.py        # Fetches market data & generates signals
├─ signals.py        # High-quality signal logic (RSI, EMA, volume, ATR)
├─ poster.py         # Formats Telegram messages
├─ requirements.txt  # Python dependencies
├─ .env              # Telegram bot token & channel ID
└─ Procfile          # For deployment (Heroku/Railway)
```

---

## Usage

```bash
python main.py
```

The bot will:

1. Scan all USDT pairs every **30 seconds**.
2. Check **price change, EMA trend, RSI, and volume spike**.
3. Calculate **entry, TP1-3, SL** based on ATR.
4. Post the signal to Telegram **if confidence is high**.
5. Auto-delete after 5 minutes (configurable).

---

## Deployment

### 🚂 Deploy on Railway / Heroku

1. Push your code to a GitHub repo.
2. Connect your repo to **Railway or Heroku**.
3. Add environment variables `BOT_TOKEN` and `CHANNEL_ID`.
4. Set the worker to:

```
python main.py
```

5. Deploy and your bot runs **24/7**.

---

## Debugging

* **Check console logs**: Each coin prints:

```
BTCUSDT -> RSI: 53, Trend: UP, Volume Spike: False, Change: 0.0123, Volume: 1234567
```

* Shows why signals **fail or pass**.
* Ensures your bot is working for **all coins**.

---

## Contributing

Pull requests and suggestions are welcome!

* Add new **signal strategies** (EMA crossover, candlestick patterns, etc.).
* Improve **volume or liquidity filters**.
* Optimize **performance for large markets**.

---

## License

MIT License – free to use and modify.


