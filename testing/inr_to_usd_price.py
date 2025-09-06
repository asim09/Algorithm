# Description: This Event gives the latest price info 
# of a pair whenever there is a price change.



import json

import socketio
from telegram import format_timestamp_ist, send_telegram_message

PRICE_ALERT = {
    # "USDTINR": {"low": 85.0, "high": 92.0},
    "SOLINR": {"low": 14500.0, "high": 15450.0},
    "TRUMPINR": {"low": 785, "high": 850},
    # "IDEXINR": {"low": 1.5, "high": 2.9},
    # "KASINR": {"low": 7.5, "high": 9.0},
}
sol_lowest_price = None


socketEndpoint = "wss://stream.coindcx.com"
channel_name = "currentPrices@spot@10s"

sio = socketio.Client()
USD = None


@sio.event
def connect():
    print("✅ Connected to CoinDCX WebSocket")
    sio.emit("join", {"channelName": channel_name})


# Price update handler
@sio.on("currentPrices@spot#update")
def on_message(response):
    global USD
    # print("====USD previous Price===========", USD)
    try:
        price_data = json.loads(response["data"])
        timestamp = format_timestamp_ist(price_data.get("ts"))
        prices = price_data.get("prices", {})

        USD_NEW = prices.get('USDTINR')
        # print("Received New USD Price:", USD_NEW)

        # ✅ Only update if new value is not None
        if USD_NEW is not None:
            USD = USD_NEW
            # print("====USD Updated Price===========", USD)
        # else:
        #     print("====USD Unchanged (New value is None)===========", USD)
        
        # print("====USD NEW Price===========", USD)
        



        for symbol, thresholds in PRICE_ALERT.items():
            current_price = prices.get(symbol)
            
            if current_price:
                
                # Low price alert
                if current_price <= thresholds["low"]:
                    if USD:
                        print(f"🔻{symbol} ₹{current_price} - USD {current_price/USD:.2f}  @ {timestamp}")
                    print(f"🔻{symbol} ₹{current_price} - USD  @ {timestamp}")
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
                    if USD:
                        print(f"✅{symbol} ₹{current_price} - USD {current_price/USD:.2f} @ {timestamp}")
                    print(f"✅{symbol} ₹{current_price} - USD  @ {timestamp}")
                    

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
