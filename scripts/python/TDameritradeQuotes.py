import requests
from config import TDAmeritradeClientid
import pandas as df
from datetime import datetime

# DailyPrices endpoint

# Define the endpoint
endpoint = r"https://api.tdameritrade.com/v1/marketdata/quotes"

# Define the payload
payload = {'apikey':TDAmeritradeClientid,
           'symbol':'GOOG,MSFT,APPL,PINS,LMND'}

# Make a request
content = requests.get(url = endpoint, params = payload)

# Convert it to a dictionary
data = content.json()
#print(data)

# dataframe
stock_df = df.DataFrame(data)
#print(stock_df)

# transpose the data frame
stock_df = stock_df.transpose()
#print(stock_df)

# export file
#stock_df.to_csv(r'C:\Users\garet\Downloads\export_dataframe.csv', index = None, header=True)



