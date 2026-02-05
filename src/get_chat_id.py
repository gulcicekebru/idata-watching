import asyncio
import yaml
from telegram import Bot

# settings.yaml oku
with open("config/settings.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

BOT_TOKEN = config["telegram"]["token"]

async def main():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()

    for update in updates:
        if update.message:
            print("Chat ID:", update.message.chat_id)

if __name__ == "__main__":
    asyncio.run(main())
