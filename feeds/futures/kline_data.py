
# import socketio
# import hmac
# import hashlib
# import json
# import time
# import asyncio
# from datetime import datetime
# from socketio.exceptions import TimeoutError
# socketEndpoint = 'wss://stream.coindcx.com'
# sio = socketio.AsyncClient()

# key = "61ee7934cffddd6c1689c821e9f710261435c9970ab5bba5"
# secret = "2c22bdf2b187335dce0407110204be9d9a1762d2fd448c61a1bd56c6a63ef4cd"

# import socketio
# import hmac
# import hashlib
# import json
# import asyncio

# socketEndpoint = 'wss://stream.coindcx.com'
# sio = socketio.AsyncClient()


# secret_bytes = bytes(secret, encoding='utf-8')

# body = {"channel": "coindcx"}
# json_body = json.dumps(body, separators=(',', ':'))
# signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

# @sio.event
# async def connect():
#     print("Connected!")
#     await sio.emit('join', { 
#         'channelName': 'coindcx', 
#         'authSignature': signature, 
#         'apiKey': key 
#     })

# @sio.on('df-position-update')
# async def on_message(response):
#     print(response["data"])
#     # example of leaving channel after receiving first message
#     await sio.emit('leave', { 'channelName': 'coindcx' })
#     print("Left channel!")

# async def main():
#     await sio.connect(socketEndpoint, transports=['websocket'])
#     await sio.wait()

# if __name__ == "__main__":
#     asyncio.run(main())

