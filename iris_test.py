import requests

import pandas as pd
import requests

# Define the URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)

raw_text = response.text

lines = raw_text.split("\n")


sum = 0.0

for line in lines:
    data = line.split(",")
    num:str = data[0]    
    
    if num.isnumeric():
        sum = sum + float(num)

print(sum)




