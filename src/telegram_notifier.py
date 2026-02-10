import yaml
import asyncio
from telegram import Bot

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "settings.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


BOT_TOKEN = config["telegram"]["token"]
CHAT_ID = config["telegram"]["chat_id"]

bot = Bot(token=BOT_TOKEN)


async def _send(text):
    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


def send_message(text):
    asyncio.run(_send(text))
