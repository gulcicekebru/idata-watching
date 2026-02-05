import requests
import yaml
import asyncio
from telegram import Bot
from datetime import datetime
from pathlib import Path
from telegram_notifier import send_message
from datetime import datetime

STATUS_FILE = Path("last_status.txt")


# config oku
with open("config/settings.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

URL = config["idata"]["login_url"]
BOT_TOKEN = config["telegram"]["token"]
CHAT_ID = config["telegram"]["chat_id"]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive"
}


STATUS_FILE = "last_status.txt"


def get_current_status():
    try:
        r = requests.get(URL, headers=HEADERS, timeout=20)
        return r.status_code
    except Exception as e:
        return f"error:{e}"

def check_status_change():
    current_status = get_current_status()

    if STATUS_FILE.exists():
        last_status = STATUS_FILE.read_text().strip()
    else:
        last_status = None

    if str(current_status) != str(last_status):
        message = (
            f"🚨 iDATA durum değişti!\n\n"
            f"Önce: {last_status}\n"
            f"Şimdi: {current_status}\n"
            f"Tarih: {datetime.now()}"
        )
        send_message(message)
        STATUS_FILE.write_text(str(current_status))
    else:
        print(f"[{datetime.now()}] Durum aynı: {current_status}")



def get_last_status():
    try:
        with open(STATUS_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def save_status(status):
    with open(STATUS_FILE, "w") as f:
        f.write(str(status))


async def notify(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def main():
    current_status = get_current_status()
    last_status = get_last_status()

    print(f"[{datetime.now()}] Status:", current_status)

    if last_status is None:
        save_status(current_status)
        return

    if str(current_status) != str(last_status):
        msg = (
            "⚠️ iDATA İtalya için durum değişti!\n\n"
            f"Önceki: {last_status}\n"
            f"Şimdi: {current_status}\n\n"
            "👉 Kontrol etmeni öneririm."
        )
        await notify(msg)

    save_status(current_status)


if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    check_status_change()

