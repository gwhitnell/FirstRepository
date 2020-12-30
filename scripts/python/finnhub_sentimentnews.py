import requests
import pandas as pd
from datetime import datetime
import datetime
from config import finnhubkey,finnhubticker,finnhubfrom,finnhubto,finnhubexportdir

#get the run date for filename
rundate = datetime.datetime.now().date() 

#define our endpoint
endpoint = 'https://finnhub.io/api/v1/news-sentiment'

# define params
params ={
         'token':finnhubkey,   
         'symbol':finnhubticker
        }


# build url and params and get data from endpoint
content = requests.get(url = endpoint,params = params)

# convert and store as dataframe
data = content.json()
stock_df = pd.DataFrame(data)

# display dataframe content
print(stock_df)

# export to file
stock_df.to_csv(r'{0}\{1}_SentimentNews_{2}.csv'.format(finnhubexportdir,rundate,finnhubticker), index = None, header=True)