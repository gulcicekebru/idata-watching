from telegram import Bot
import yaml

with open("config/settings.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

bot = Bot(token=config["telegram"]["token"])

updates = bot.get_updates()

for update in updates:
    if update.message:
        print("Chat ID:", update.message.chat.id)
        print("Text:", update.message.text)
