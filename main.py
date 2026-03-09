import os
import asyncio
from telegram import Bot
from telegram.error import InvalidToken
from dotenv import load_dotenv
from scanner import scan_market
from poster import generate_signal_message

# ===== Load environment variables from .env =====
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# ===== Validate token & channel =====
if not BOT_TOKEN or BOT_TOKEN.strip() == "":
    raise ValueError("❌ BOT_TOKEN is missing! Please set it in your .env file.")
if not CHANNEL_ID or CHANNEL_ID.strip() == "":
    raise ValueError("❌ CHANNEL_ID is missing! Please set it in your .env file.")

try:
    bot = Bot(token=BOT_TOKEN)
except InvalidToken:
    raise ValueError("❌ Invalid BOT_TOKEN! Make sure you copied it correctly from BotFather.")

posted = set()

# ===== Safe send function with auto-delete =====
async def send_message_safe(message, delete_after=3000):
    for i in range(3):
        try:
            msg = await bot.send_message(chat_id=CHANNEL_ID, text=message)
            asyncio.create_task(delete_after_delay(msg.message_id, delete_after))
            return
        except Exception as e:
            print("Telegram error:", e)
            await asyncio.sleep(15)

# ===== Delete message after a delay =====
async def delete_after_delay(message_id, delay):
    await asyncio.sleep(delay)
    try:
        await bot.delete_message(chat_id=CHANNEL_ID, message_id=message_id)
        print(f"Deleted message {message_id} after {delay} seconds")
    except Exception as e:
        print(f"Failed to delete message {message_id}:", e)

# ===== Main bot loop =====
async def run_bot():
    print("🚀 High Quality Signal Bot Started")
    while True:
        try:
            signals = scan_market()
            for s in signals:
                key = f"{s['coin']}_{s['trade_type']}"
                if key not in posted:
                    message = generate_signal_message(
                        s["coin"],
                        s["entry"],
                        s["sl"],
                        s["tp1"],
                        s["tp2"],
                        s["tp3"],
                        s["trade_type"],
                        s["confidence"]
                    )
                    print("Posting:", s["coin"], s["trade_type"])
                    await send_message_safe(message)
                    posted.add(key)
                    await asyncio.sleep(15)  # avoid flood control
        except Exception as e:
            print("Bot error:", e)
        await asyncio.sleep(30)  # wait before next scan

# ===== Run the bot =====
asyncio.run(run_bot())
