

import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))

# from price_change_with_24Hrs_vol import
from feeds.redis_client import redis_client


moving_coins = redis_client.get("moving_coins")
json_data_coins = json.loads(moving_coins)

candlestick_1m = redis_client.get("candlestick_1m")
json_data_candle = json.loads(candlestick_1m)

# for i, (symbol, details) in enumerate(json_data_candle , start=1):
#     print(f"{i} ==> {symbol}: pc = {details['pc']}%, v = {details['v']:.2f}")


print("==============================")
print(moving_coins)
# print(json.dumps(json_data_coins, indent=2))
print("==============================")
