import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests

telegram_bot_token = "8224351927:AAFdCZoKr7KkKBDBdAdGOW0JF5buSDtKnMU"
telegram_chat_id = "7926727897"  # Replace with your actual chat ID
# ============================================================


# ✅ Telegram message sender
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    try:
        r = requests.post(url, data=payload)
        if r.status_code != 200:
            print("Failed to send Telegram message:", r.text)
    except Exception as e:
        print("Error sending message:", e)


# ✅ IST timestamp formatter
def format_timestamp_ist(timestamp_ms):
    timestamp_sec = timestamp_ms / 1000
    utc_dt = datetime.fromtimestamp(timestamp_sec, tz=timezone.utc)
    ist_dt = utc_dt.astimezone(ZoneInfo("Asia/Kolkata"))
    return ist_dt.strftime("%H:%M:%S %d:%m:%Y")
