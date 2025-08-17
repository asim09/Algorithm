import socketio
import json

socketEndpoint = 'wss://stream.coindcx.com'
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('join', {'channelName': "B-SOL_USDT_1m"})  # or "I-SOL_INR_1m"

@sio.on('candlestick')
def on_candle(response):
    print("Got candlestick event!")
    print(json.dumps(response, indent=2))

@sio.event
def disconnect():
    print("I'm disconnected!")

if __name__ == '__main__':
    sio.connect(socketEndpoint, transports='websocket')
    sio.wait()
