from feeds.redis_client import redis_client
import json
from feeds.stores import data_store
print(data_store['current_price_10s'])
print(data_store['most_trading_with_24Hrs_volume'])
data_store['current_price_10s'] = {'a': 'b'}
json_data1 = json.dumps(data_store['current_price_10s'])
redis_client.set("current_price_10s", json_data1)
# candlestick_data = redis_client.get("candlestick_1m")
price_data = redis_client.get("current_price_10s")

# combined_data = {
#     "current_price_10s": json.loads(price_data) if price_data else {},
#     "most_trading_with_24Hrs_volume": {},
#     "candlestick_1m": json.loads(candlestick_data) if candlestick_data else {}
# }


print("===========", price_data)
# redis_client.flushdb()
# redis_client.flushall()
# print("Flushed all Redis databases")
keys = redis_client.keys('*')
print("===========", keys)
# print("Remaining keys:", keys if keys else "None")
