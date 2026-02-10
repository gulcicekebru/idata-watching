import requests
import yaml
from datetime import datetime
from pathlib import Path
from telegram_notifier import send_message

# =====================
# CONFIG
# =====================
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "settings.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


URL = config["idata"]["login_url"]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive"
}

STATUS_FILE = Path("last_status.txt")

# =====================
# CORE LOGIC
# =====================
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

    if str(current_status) == "403":
        print(f"[{datetime.now()}] 403 alındı, alarm atlanıyor")
        STATUS_FILE.write_text("403")
        return


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


# =====================
# ENTRY POINT
# =====================
if __name__ == "__main__":
    check_status_change()
