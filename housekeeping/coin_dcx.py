key = "61ee7934cffddd6c1689c821e9f710261435c9970ab5bba5"
secret = "2c22bdf2b187335dce0407110204be9d9a1762d2fd448c61a1bd56c6a63ef4cd"

import base64
import hashlib
import hmac
import json
import time

import requests

# Enter your API Key and Secret here. If you don't have one, you can generate it from the website.


# python3
secret_bytes = bytes(secret, encoding="utf-8")
# python2


# Generating a timestamp
timeStamp = int(round(time.time() * 1000))

body = {"timestamp": timeStamp}

json_body = json.dumps(body, separators=(",", ":"))

signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

url = "https://api.coindcx.com/exchange/v1/users/info"

headers = {
    "Content-Type": "application/json",
    "X-AUTH-APIKEY": key,
    "X-AUTH-SIGNATURE": signature,
}

response = requests.post(url, data=json_body, headers=headers)
data = response.json()
print(json.dumps(data, indent=4))
