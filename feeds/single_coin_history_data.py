import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))


import requests, json # Install requests module first.
from datetime import datetime, timezone, timedelta
import pandas as pd


url = "https://public.coindcx.com/market_data/candles?pair=B-SOL_USDT&interval=5m&limit=5" # Replace 'SNTBTC' with the desired market pair.

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
df["time_ist"] = (pd.to_datetime(df["time"], unit="ms", utc=True) 
                  + timedelta(hours=5, minutes=30)).dt.strftime("%H:%M:%S %d-%m-%Y")

# print(df)
print()
data = df.to_dict(orient="records")

print(json.dumps(data, indent=2))



def to_ist():
    timestamp_ms = 1754804100000

    # Convert milliseconds to seconds
    timestamp_s = timestamp_ms / 1000

    # Create UTC datetime
    utc_time = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)

    # Define IST offset (+5:30)
    ist_offset = timedelta(hours=5, minutes=30)

    # Convert to IST
    ist_time = utc_time + ist_offset
    return ist_time

    print("IST Time:", ist_time.strftime("%Y-%m-%d %H:%M:%S"))