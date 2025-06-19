
# Telegram Auto-Forward Bot 📤

Live-forwards messages (with media) from one or more source channels to a target channel. Also adds custom captions, inline buttons, and logs activity.

## 🛠️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/telegram-auto-forward-bot.git
   cd telegram-auto-forward-bot
   ```

2. Copy and edit your config:
   ```bash
   cp config.example.py config.py
   # Fill in API_ID, API_HASH, BOT_TOKEN, channel IDs, and BUTTONS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## 🚀 Deployment

Deployable to any cloud service like Render or Heroku.

Example Render start command:
```
python main.py
```

Make sure `config.py` is created in the deployed environment.
