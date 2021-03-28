import requests
from config import TDAmeritradeClientid

# DailyPrices endpoint

# Define the endpoint
endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('GOOG')

# Define the payload
payload = {'apikey':TDAmeritradeClientid,
           'periodType':'day',
           'frequencyType':'minute',
           'frequency':'1',
           'period':'2',
           'startDate':'1608037920000',
           'endDate':'1608043800000',
           'needExtendedHoursData':'true'}

# Make a request
content = requests.get(url = endpoint, params = payload)

# Convert it to a dictionary
data = content.json()
print(data)