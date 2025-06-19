
import logging
from telethon import TelegramClient, events, Button
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TelegramClient('forwarder_bot', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

def get_caption(msg):
    text = msg.text or ''
    prefix = "📥 Forwarded via @CGM_Files"
    return f"{prefix}\n\n📝 Original: {text}" if text else prefix

def get_buttons():
    return [[Button.url(label, url) for label, url in config.BUTTONS]]

@client.on(events.NewMessage(chats=config.SOURCE_CHANNELS))
async def handler(event):
    msg = event.message
    caption = get_caption(msg)
    buttons = get_buttons()
    try:
        if msg.media:
            await client.send_file(config.TARGET_CHANNEL, file=msg.media, caption=caption, buttons=buttons)
        else:
            await client.send_message(config.TARGET_CHANNEL, message=caption, buttons=buttons)
        await client.send_message(config.LOG_CHANNEL, f"✅ Forwarded from {event.chat.title}")
        logger.info(f"Forwarded message from {event.chat.title}")
    except Exception as e:
        error = str(e)
        await client.send_message(config.LOG_CHANNEL, f"⚠️ Error: {error}")
        logger.error(f"Failed to forward: {error}")

logger.info("🚀 Bot is running...")
client.run_until_disconnected()
