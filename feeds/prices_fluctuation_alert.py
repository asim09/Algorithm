# Description: This Event gives the latest price info 
# of a pair whenever there is a price change.



import json

import socketio
from telegram import format_timestamp_ist, send_telegram_message
from stores import data_store
from redis_client import redis_client






PRICE_ALERT = {
    # "USDTINR": {"low": 88.0, "high": 92.0},
    "SOLUSDT": {"low": 181.10, "high": 193.40},
    "FARTCONUSDT": {"low": 0.95, "high": 1.2},
    # "TRUMPINR": {"low": 785, "high": 850},
    # "IDEXINR": {"low": 1.5, "high": 2.9},
    # "KASINR": {"low": 7.5, "high": 8.8},
}
sol_lowest_price = None


socketEndpoint = "wss://stream.coindcx.com"
channel_name = "currentPrices@spot@10s"

sio = socketio.Client()


@sio.event
def connect():
    print("✅ Connected to CoinDCX WebSocket")
    sio.emit("join", {"channelName": channel_name})


# Price update handler
@sio.on("currentPrices@spot#update")
def on_message(response):
    try:
        price_data = json.loads(response["data"])
        timestamp = format_timestamp_ist(price_data.get("ts"))
        prices = price_data["prices"]
        # json_data = json.dumps(prices)
        # redis_client.set("current_price_10s", json_data)
        # filtered_data = {symbol: prices.get(symbol) for symbol in PRICE_ALERT if symbol in prices}
        

        for symbol, thresholds in PRICE_ALERT.items():
            current_price = prices.get(symbol)
            
            if current_price:
                
                # Low price alert
                if current_price <= thresholds["low"]:
                    print(f"🔻{symbol} ₹{current_price} @ {timestamp}")
                    send_telegram_message(
                        f"🔻{symbol} ₹{current_price} @ {timestamp}"
                    )

                # High price alert
                elif current_price >= thresholds["high"]:
                    print(
                        f"⬆️ {symbol} Price ₹{current_price}  - @ {timestamp}"
                    )
                    send_telegram_message(
                        f"⬆️ {symbol} Price ₹{current_price}  - @ {timestamp}"
                    )
                else:
                    print()
                    print(f"✅ {symbol}: ₹{current_price} at {timestamp}")
                    

    except Exception as e:
        print("❌ Error parsing response:", e)


# ✅ Start connection
def main():
    try:
        sio.connect(socketEndpoint, transports="websocket")
        sio.wait()
    except Exception as e:
        print(f"❌ Connection Error: {e}")


# ✅ Entry point
if __name__ == "__main__":
    main()
