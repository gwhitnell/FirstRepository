import requests
import pandas as pd
from config import finnhubkey
from datetime import datetime
import datetime
from config import finnhubkey,finnhubticker,finnhubresolution,finnhubexportdir

#get the run date for filename
rundate = datetime.datetime.now().date() 

#define our endpoint
endpoint = 'https://finnhub.io/api/v1/scan/support-resistance'

# define params
params = {'symbol':finnhubticker,
         'resolution':finnhubresolution,
         'token':finnhubkey}


# build url and params and get data from endpoint
content = requests.get(url = endpoint,params = params)

# convert and store as dataframe
data = content.json()
stock_df = pd.DataFrame(data)

# transpose the data frame
stock_df = stock_df.transpose()

# display dataframe content
#print(stock_df)

# export to file
stock_df.to_csv(r'{0}\{1}_SupportResistance_{2}_{3}.csv'.format(finnhubexportdir,rundate,finnhubticker,finnhubresolution), index = None, header=True)