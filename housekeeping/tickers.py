


import requests
import time
import datetime
import json

url = "https://api.coindcx.com/exchange/ticker"

def fetch_data():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for 4xx/5xx
        data = response.json()
        
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] ✅ Data fetched successfully")

        return data  # ✅ This is the actual return

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None  # Return None in case of error


# 🔁 Always-running loop
while True:
    result = fetch_data()
    
    if result:
        # 👇 You can filter or process the result here
        print(json.dumps(result, indent=2))  # Just printing 1st item for example
    
    time.sleep(10)
