import json

import requests
import socketio
from fastapi import BackgroundTasks, FastAPI

# ========== CONFIG ==========
ALERT_PRICE = 15500.0  # Alert price
socketEndpoint = "wss://stream.coindcx.com"
channel_name = "currentPrices@spot@10s"

telegram_bot_token = "8224351927:AAFdCZoKr7KkKBDBdAdGOW0JF5buSDtKnMU"
telegram_chat_id = "7926727897"  # Replace with your chat ID
# ============================

app = FastAPI()
sio = socketio.Client()


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Telegram error:", response.text)
    except Exception as e:
        print("Telegram send error:", e)


@sio.event
def connect():
    print("✅ Connected to CoinDCX WebSocket")
    sio.emit("join", {"channelName": channel_name})


@sio.on("currentPrices@spot#update")
def on_message(response):
    try:
        price_data = json.loads(response["data"])
        sol_inr = price_data["prices"].get("SOLINR")
        if sol_inr:
            print(f"💹 SOLINR: ₹{sol_inr}")
            if sol_inr <= ALERT_PRICE:
                msg = f"🚨 Alert! SOLINR dropped to ₹{sol_inr}"
                print(msg)
                send_telegram_message(msg)
    except Exception as e:
        print("❌ Error:", e)


def run_socket_client():
    try:
        sio.connect(socketEndpoint, transports=["websocket"])
        sio.wait()
    except Exception as e:
        print(f"❌ Socket connection error: {e}")


@app.get("/start-alert")
def start_alert(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_socket_client)
    return {"status": "started", "message": "Price alerting started in background."}
