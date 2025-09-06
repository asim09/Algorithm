import socketio

socketEndpoint = 'wss://stream.coindcx.com'
sio = socketio.Client()


@sio.event
def connect():
    print("I'm connected!")
    sio.emit('join', {'channelName': "B-BTC_USDT@orderbook@20"})


@sio.on('depth-snapshot')
def on_message(response):
    print("depth-snapshot Response !!!")
    print(response)


def main():
    try:
        sio.connect(socketEndpoint, transports='websocket')
        while True:
            sio.event('depth-snapshot', {'channelName': "B-BTC_USDT@orderbook@20"})
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        raise


# Run the main function
if __name__ == '__main__':
    main()