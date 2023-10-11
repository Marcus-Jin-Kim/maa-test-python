import pandas as pd
import requests
import json
import pprint



url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
raw_text = response.text
# print(raw_text)

data = json.loads(raw_text)

# pprint.pprint(data)
# print(data['date'])
# print(data['provider'])


# print(data['rates']['KRW'])


sum = 0.0
for key, value in data['rates'].items():
    print(f"key :{key}, value: {value}")
    sum = sum + value

print(f"sum = {sum}")





