# Description: This Event gives the latest price info 
# of a pair whenever there is a price change.

def test():
    return 'Test'
print(test())

# Description: This Event gives the latest price info 
# of a pair whenever there is a price change.



import json

import socketio
# from testing.telegram import format_timestamp_ist, send_telegram_message
from telegram import format_timestamp_ist, send_telegram_message

PRICE_ALERT = {
    "SOLINR": {"low": 14300.0, "high": 15400.0},
    "TRUMPINR": {"low": 795, "high": 820},
    "IDEXINR": {"low": 2.4, "high": 2.9},
}


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
        print()

        for symbol, thresholds in PRICE_ALERT.items():
            current_price = prices.get(symbol)
            if current_price:
                print(f"💹 {symbol}: ₹{current_price} @ {timestamp}")

                # Low price alert
                if current_price <= thresholds["low"]:
                    print(f"🔻{symbol} dropped to ₹{current_price} @ {timestamp}")
                    send_telegram_message(
                        f"🔻{symbol} dropped to ₹{current_price} @ {timestamp}"
                    )

                # High price alert
                if current_price >= thresholds["high"]:
                    print(
                        f"⬆️ HIGH ALERT: {symbol} \ndropped to ₹{current_price}\n@ {timestamp}"
                    )
                    send_telegram_message(
                        f"⬆️ HIGH ALERT\n{symbol} surged to ₹{current_price} (target: ₹{thresholds['high']})\n🕒 {timestamp}"
                    )

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
