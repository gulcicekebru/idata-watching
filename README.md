# iDATA Appointment Watcher 🤖🇮🇹

This project monitors the iDATA / VFS Global Italy visa appointment page and sends a **Telegram notification** when the page status changes (e.g. appointment availability, page access changes).

It is designed to run **automatically in the background** using **Windows Task Scheduler**.

---

## 🧠 What I Built in This Project

In this project, I built an automated monitoring system to track the availability of the iDATA Italy visa page.

Instead of attempting to bypass CAPTCHA or authentication mechanisms, I designed a lightweight and ethical solution that:
- Periodically checks the public-facing page status
- Detects meaningful changes in availability
- Notifies the user instantly via a Telegram bot

### Key Contributions
- Designed a Python-based watcher that monitors HTTP status changes
- Implemented state tracking to detect real changes instead of repeated alerts
- Integrated Telegram Bot API for real-time notifications
- Externalized sensitive configuration using YAML and `.gitignore`
- Automated execution using Windows Task Scheduler

### Technologies Used
- Python
- Requests
- python-telegram-bot
- YAML
- Git & GitHub
- Windows Task Scheduler

This project reflects my ability to design practical automation tools, handle external integrations, and apply security-conscious development practices.


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

<pre>
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
</pre>

## ⚙️ How It Works

This project continuously monitors the iDATA Italy visa page and notifies the user via Telegram when a change is detected.

### 🔍 Workflow

1. **Configuration**
   - User creates a `settings.yaml` file based on `settings.example.yaml`
   - Telegram bot token and chat ID are stored locally (never committed)

2. **Status Check**
   - The watcher sends an HTTP request to the iDATA Italy page
   - A realistic browser `User-Agent` header is used
   - The HTTP status code is extracted (e.g. `403`, `200`)

3. **State Comparison**
   - The current status is compared with the last known status
   - The previous value is stored in `last_status.txt`

4. **Change Detection**
   - If the status changes (for example, from `403` to something else),
     the system considers this a meaningful update

5. **Telegram Notification**
   - A Telegram message is sent instantly to the user
   - The message includes:
     - Previous status
     - Current status
     - Timestamp

6. **Automation**
   - The script is designed to run periodically (e.g. via Windows Task Scheduler)
   - No manual browser checks are required

### 🚨 Why HTTP Status Monitoring?

iDATA heavily protects its pages with CAPTCHA and bot detection.
Instead of bypassing these systems, this project:
- Observes **surface-level availability**
- Alerts the user when **manual action may be required**
- Respects website security boundaries

### 🛡️ Security Notes
- No credentials or tokens are committed to the repository
- Sensitive files are excluded via `.gitignore`
- The project is intended for **personal and educational use only**


## ⚠️ Educational & personal use only