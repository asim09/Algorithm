import socketio
import json
from redis_client import redis_client


socketEndpoint = 'wss://stream.coindcx.com'
sio = socketio.Client()


@sio.event
def connect():
    print("I'm connected!")
    sio.emit('join', {'channelName': "priceStats@spot@60s"})


@sio.on('priceStats@spot#update')
def on_message(response):
    print("priceStats@spot#update Response !!!")
    data = json.loads(response['data'])
    print(data)
    stats = data.get('stats', {})

    filtered_data = {
        symbol: details for symbol, details in stats.items()
        if isinstance(details, dict) and 'v' in details and 'pc' in details and details['v'] >= 5_000_00 and (details['pc'] > 0.5 or  details['pc'] < 0.3)
    }


    sorted_data = sorted(
        filtered_data.items(),
        key=lambda x: x[1]['pc'],
        reverse=True
    )
    json_data = json.dumps(sorted_data)
    # redis_client.set("moving_coins", json_data)

    # for i, (symbol, details) in enumerate(sorted_data, start=1):
    #     print(f"{i} ==> {symbol}: pc = {details['pc']}%, v = {details['v']:.2f}")
    # print()
    # print()


@sio.event
def disconnect():
    print("I'm disconnected!")


def main():
    try:
        sio.connect(socketEndpoint, transports='websocket')
        while True:
            sio.event('priceStats@spot#update', {'channelName': "priceStats@spot@60s"})
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        raise



# Run the main function
if __name__ == '__main__':
    main()