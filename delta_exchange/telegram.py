import json, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import requests
load_dotenv()
telegram_bot_token = os.getenv("telegram_bot_token")
telegram_chat_id = os.getenv("telegram_chat_id")




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


from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def convert_iso_to_ist(iso_time: str) -> str:
    # Strip trailing 'Z' (UTC indicator)
    iso_time = iso_time.replace("Z", "+00:00")

    # Truncate fractional seconds to 6 digits (microseconds)
    if "." in iso_time:
        date_part, frac = iso_time.split(".")
        frac, tz = frac.split("+")
        frac = frac[:6]  # keep only microseconds
        iso_time = f"{date_part}.{frac}+{tz}"

    # Parse as datetime
    utc_dt = datetime.fromisoformat(iso_time)
    
    # Convert to IST
    ist_dt = utc_dt.astimezone(ZoneInfo("Asia/Kolkata"))
    return ist_dt.strftime("%H:%M:%S %d-%m-%Y")



from datetime import datetime, timezone, timedelta

def to_ist(timestamp_micro):
    """
    Convert a microsecond timestamp to IST datetime string.
    
    Args:
        timestamp_micro (int): Timestamp in microseconds
    
    Returns:
        str: DateTime in IST formatted as "YYYY-MM-DD HH:MM:SS"
    """
    # Convert microseconds → seconds
    timestamp_sec = timestamp_micro / 1e6
    
    # Convert to UTC datetime
    utc_dt = datetime.fromtimestamp(timestamp_sec, tz=timezone.utc)
    
    # Define IST (UTC +5:30)
    ist_offset = timedelta(hours=5, minutes=30)
    ist_dt = utc_dt.astimezone(timezone(ist_offset))
    
    return ist_dt.strftime("%H:%M:%S %d-%m-%Y")


