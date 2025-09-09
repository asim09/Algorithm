import websocket
import json, time
from telegram import format_timestamp_ist, send_telegram_message, convert_iso_to_ist, to_ist

WEBSOCKET_URL = "wss://socket.india.delta.exchange"

PRICE_ALERT = {
    "SOLUSD": {"low": 211.30,"high": 218.75}
    # "ENAUSD": {"low": 0.17100, "high": 0.17200},
    # "BIOUSD": {"low": 0.17100, "high": 0.17200},
    # "MUSD": {"low": 1.6340, "high": 1.6350},
    # "USDTINR": {"low": 88.80, "high": 91.0},
    # "TRUMPINR": {"low": 785, "high": 850},
}
symbols = list(PRICE_ALERT.keys())

def on_error(ws, error):
    print(f"Socket Error: {error}")
    try:
        ws.close()
    except:
        pass

def on_close(ws, close_status_code, close_msg):
    print(f"Socket closed with status: {close_status_code} and message: {close_msg}")

def on_open(ws):
  print(f"Socket opened")
  # subscribe tickers of perpetual futures - BTCUSD & ETHUSD, call option C-BTC-95200-200225 and put option - P-BTC-95200-200225
  subscribe(ws, "v2/ticker", symbols)
  # subscribe 1 minute ohlc candlestick of perpetual futures - MARK:BTCUSD(mark price) & ETHUSD(ltp), call option C-BTC-95200-200225(ltp) and put option - P-BTC-95200-200225(ltp).
#   subscribe(ws, "candlestick_1m", ["MARK:BTCUSD", "ETHUSD", "C-BTC-95200-200225", "P-BTC-95200-200225"])

def subscribe(ws, channel, symbols):
    payload = {
        "type": "subscribe",
        "payload": {
            "channels": [
                {
                    "name": channel,
                    "symbols": symbols
                }
            ]
        }
    }
    ws.send(json.dumps(payload))

def on_message(ws, message):
    # print json response
    data = json.loads(message)
    if "type" in data and data["type"] == "v2/ticker":
        # print(data)
        symbol = data.get("symbol")
        current_price = round(float(data.get("mark_price")), 5)
        thresholds = PRICE_ALERT.get(symbol)
        timestamp = to_ist(data.get("timestamp"))
        # current_price = round(float(mark_price), 3)
        if thresholds:
            if current_price <= thresholds["low"]:
                alert_msg = f"🔻 {symbol} {current_price} @ {timestamp}"
                send_telegram_message(alert_msg)
            elif current_price >= thresholds["high"]:
                alert_msg = f"⬆️ {symbol} {current_price} @ {timestamp}"
                send_telegram_message(alert_msg)

        # finally:
            print(f"✅ {symbol}: {current_price} at {timestamp}")

def start_socket():
    while True:
        try:
            ws = websocket.WebSocketApp(
                WEBSOCKET_URL,
                on_open=on_open,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close,
            )
            ws.run_forever(ping_interval=20, ping_timeout=10)  # <— added keepalive
        except Exception as e:
            print(f"🔥 Exception: {e}")
        finally:
            print("🔄 Reconnecting in 5 seconds...")
            time.sleep(5)

    

if __name__ == "__main__":
  start_socket()
# kill cmd  to restart terminal process after any change in script
# (env) root@LAPTOP-A99G22PN:/home/asim/code/trade# pkill -f test_price_for_coins.py