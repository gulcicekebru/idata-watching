import yaml
from telegram import Bot

# config oku
with open("config/settings.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

BOT_TOKEN = config["telegram"]["token"]
CHAT_ID = config["telegram"]["chat_id"]

bot = Bot(token=BOT_TOKEN)

bot.send_message(
    chat_id=CHAT_ID,
    text="🤖 Merhaba! iDATA watcher botu ayakta."
)

print("Mesaj gönderildi")
