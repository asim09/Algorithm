import requests # Install requests module first.

url = "https://api.coindcx.com/exchange/v1/markets"

response = requests.get(url)
data = response.json()
print(data)


import requests
import time
import datetime

url = "https://api.coindcx.com/exchange/v1/markets"

def fetch_inr_markets():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Filter INR markets
        inr_markets = [symbol for symbol in data if symbol.endswith("INR")]

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(f"[{now}] ✅ Found {len(inr_markets)} INR markets")

        return inr_markets

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []
markets = fetch_inr_markets()
# 🔁 Infinite loop to fetch INR markets every 10 seconds
# while True:
#     markets = fetch_inr_markets()

#     # Print first 5 INR symbols as a sample
#     for market in markets[:5]:
#         print(f"🔹 {market['symbol']} - {market['base_currency_name']}")

#     print("-" * 50)
#     time.sleep(10)
