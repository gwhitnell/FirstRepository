import requests
import pandas as pd
from config import finnhubkey
from datetime import datetime
import datetime
from config import finnhubkey,finnhubticker,finnhubresolution,finnhubexportdir

#get the run date for filename
rundate = datetime.datetime.now().date() 

#define our endpoint
endpoint = 'https://finnhub.io/api/v1/scan/pattern'

# define params
params = {'symbol':finnhubticker,
         'resolution':finnhubresolution,
         'token':finnhubkey}


# build url and params and get data from endpoint
content = requests.get(url = endpoint,params = params)

# convert and store as dataframe
data = content.json()
#print(data)

# use of 2 dataframes as json is nested and need to flatten based on the points value
stock_df = pd.DataFrame(data)
nested_df = pd.DataFrame(stock_df.points.values.tolist())

# convert milliseconds to datetime
nested_df['atime'] = pd.to_datetime(nested_df['atime'],unit='s')
nested_df['dtime'] = pd.to_datetime(nested_df['dtime'],unit='s')
nested_df['sortTime'] = pd.to_datetime(nested_df['sortTime'],unit='s')

# display dataframe content
print(nested_df)

# export to file
nested_df.to_csv(r'{0}\{1}_PatternType_{2}_{3}.csv'.format(finnhubexportdir,rundate,finnhubticker,finnhubresolution), index = None, header=True)