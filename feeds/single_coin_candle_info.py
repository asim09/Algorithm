# import socketio, json
# from stores import data_store
# from redis_client import redis_client


import socketio

socketEndpoint = 'wss://stream.coindcx.com'
sio = socketio.Client()


@sio.event
def connect():
    print("I'm connected!")
    sio.emit('join', {'channelName': "B-SOL_USDT_1m"})


@sio.on('candlestick')
def on_message(response):
    print("candlestick Response !!!")
    print(response)


def main():
    try:
        sio.connect(socketEndpoint, transports='websocket')
        while True:
            sio.event('candlestick', {'channelName': "B-BTC_USDT_1m"})
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        raise


# Run the main function
if __name__ == '__main__':
    main()


# socketEndpoint = 'wss://stream.coindcx.com'
# sio = socketio.Client()


# @sio.event
# def connect():
#     print("I'm connected!")
#     sio.emit('join', {'channelName': "B-SOL_USDT_1m"})


# @sio.on('candlestick')
# def on_message(response):
#     print("candlestick Response !!!")
#     print(response)
#     json_data = json.dumps(response['data'])
#     # json_data = json.dumps(data_store)
#     redis_client.set("candlestick_1m", json_data)



# @sio.event
# def disconnect():
#     print("I'm disconnected!")


# def main():
#     try:
#         sio.connect(socketEndpoint, transports='websocket')
#         while True:
#             sio.event('candlestick', {'channelName': "I-SOL_INR_1m"})
#     except Exception as e:
#         print(f"Error connecting to the server: {e}")
#         raise


# # Run the main function
# if __name__ == '__main__':
#     main()


#############################################
# import requests # Install requests module first.

# url = "https://api.coindcx.com/exchange/v1/markets_details"

# response = requests.get(url)
# data = response.json()
# for i, obj in enumerate(data):
#     if obj['coindcx_name']=='SOLINR':
#         print(obj)
#         print()