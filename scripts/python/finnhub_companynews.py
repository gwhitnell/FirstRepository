import requests
import pandas as pd
from datetime import datetime
import datetime
from config import finnhubkey,finnhubticker,finnhubfrom,finnhubto,finnhubexportdir

#get the run date for filename
rundate = datetime.datetime.now().date() 

#define our endpoint
endpoint = 'https://finnhub.io/api/v1/company-news'

# define params
params ={'symbol':finnhubticker,
         'from':finnhubfrom,
         'to':finnhubto,
         'token':finnhubkey}


# build url and params and get data from endpoint
content = requests.get(url = endpoint,params = params)

# convert and store as dataframe
data = content.json()
stock_df = pd.DataFrame(data)

# convert milliseconds to datetime
stock_df['datetime'] = pd.to_datetime(stock_df['datetime'],unit='s')

# display dataframe content
print(stock_df)

# export to file
stock_df.to_csv(r'{0}\{1}_CompanyNews_{2}_{3}_{4}.csv'.format(finnhubexportdir,rundate,finnhubticker, finnhubfrom, finnhubto), index = None, header=True)