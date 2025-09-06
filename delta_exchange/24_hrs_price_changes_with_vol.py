import websocket
import json
from telegram import format_timestamp_ist, send_telegram_message, convert_iso_to_ist, to_ist

# production websocket base url
WEBSOCKET_URL = "wss://socket.india.delta.exchange"



PRICE_ALERT = {
    # "USDTINR": {"low": 88.80, "high": 91.0},
    "SOLUSDT": {"low": 205.50, "high": 208.50},
    # "MUSD": {"low": 1.50, "high": 2.50},
    "FARTCONUSDT": {"low": 0.95, "high": 1.2},
    # "TRUMPINR": {"low": 785, "high": 850},
    # "IDEXINR": {"low": 1.5, "high": 2.9},
    # "KASINR": {"low": 7.5, "high": 8.8},
}




def on_error(ws, error):
    print(f"Socket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Socket closed with status: {close_status_code} and message: {close_msg}")

def on_open(ws):

  # subscribe tickers of perpetual futures - BTCUSD & ETHUSD, call option C-BTC-95200-200225 and put option - P-BTC-95200-200225
  symbols = list(PRICE_ALERT.keys())
#   symbols = ['SOLUSDT']
  symbols = ['FARTCONUSDT']
  print("========================",symbols)
  subscribe(ws, "v2/ticker", ['FARTCONUSDT'])
#   subscribe(ws, "v2/ticker", ["all"])
  # subscribe 1 minute ohlc candlestick of perpetual futures - MARK:BTCUSD(mark price) & ETHUSD(ltp), call option C-BTC-95200-200225(ltp) and put option - P-BTC-95200-200225(ltp).
  subscribe(ws, "candlestick_1m", ["MARK:BTCUSD", "ETHUSD", "C-BTC-95200-200225", "P-BTC-95200-200225"])

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
    message_json = json.loads(message)
    print(json.dumps(message_json, indent=2))
    print()
    print()
    print()
    # mp = message_json.get('mark_price')

    timestamp = to_ist(message_json.get("timestamp"))
    current_price = float(message_json['mark_price'])
    current_price = round(current_price, 3)
    # for symbol, thresholds in PRICE_ALERT.items():
    #     if symbol == 'SOLUSDT':pass
    symbol = message_json.get("symbol")
    # print(symbol)
    thresholds = PRICE_ALERT[symbol]
    # print(thresholds)
    # print(current_price)
    # if current_price:
                
    #     # Low price alert
    #     if current_price <= thresholds["low"]:
    #         print(f"🔻{symbol} ₹{current_price} @ {timestamp}")
    #         send_telegram_message(
    #             f"🔻{symbol} ₹{current_price} @ {timestamp}"
    #         )

    #     # High price alert
    #     elif current_price >= thresholds["high"]:
    #         print(
    #             f"⬆️ {symbol} Price ₹{current_price}  - @ {timestamp}"
    #         )
    #         send_telegram_message(
    #             f"⬆️ {symbol} Price ₹{current_price}  - @ {timestamp}"
    #         )
    #     else:
    #         if symbol !='USDTINR':
    #             print()
    #             print(f"✅ {symbol}: ₹{current_price} at {timestamp}")
    #         if symbol =='MUSD':
    #             send_telegram_message(
    #             f"✅ {symbol} ₹{current_price} @ {timestamp}"
    #         )


if __name__ == "__main__":
    ws = websocket.WebSocketApp(WEBSOCKET_URL, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()  