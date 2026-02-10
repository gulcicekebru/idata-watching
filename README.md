# iDATA Appointment Watcher 🤖🇮🇹

This project monitors the iDATA / VFS Global Italy visa appointment page and sends a **Telegram notification** when the page status changes (e.g. appointment availability, page access changes).

It is designed to run **automatically in the background** using **Windows Task Scheduler**.

---

## ✨ Features

- Periodically checks iDATA Italy visa page
- Detects page status changes (HTTP status based)
- Sends instant notifications via Telegram Bot
- Prevents duplicate alerts using local state tracking
- Secure configuration management (no secrets in repo)
- Works with Windows Task Scheduler

---

## 🛠️ Technologies Used

- Python 3
- `requests`
- `python-telegram-bot`
- `PyYAML`
- Async programming (`asyncio`)
- Windows Task Scheduler

---

## 📁 Project Structure

idata-watching/
├── src/
│ ├── idata_watcher.py # Main logic that checks iDATA page status
│ ├── telegram_notifier.py # Sends notifications via Telegram bot
│ └── get_chat_id.py # Utility script to retrieve Telegram chat ID
│
├── config/
│ └── settings.example.yaml # Example configuration file (no secrets)
│
├── .gitignore # Files and folders ignored by git
├── README.md # Project documentation
└── requirements.txt # Python dependencies