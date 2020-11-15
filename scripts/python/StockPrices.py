# %%

# Script to get stock information on companies via yfinance API 
# https://pypi.org/project/yfinance/

import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import yfinance as yf

print('Enter your ticker:')
x = input()

print('Enter your period? (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:)')
y = input()

df = yf.Ticker(x)

# show analysts recommendations
recom = df.recommendations
final_df = recom.sort_values(by=['Date'], ascending=False).head(5)
print(final_df)


old = df.history(period = y)
old.head()


# Reset index of dataframe in order to visulaise
old = old.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      old[i]  =  old[i].astype('float64')


# Plot linechart for period 
import plotly.express as px
fig = px.line(old, x="Date", y="Open", title= x + ' Stock Prices')
fig.show()


# show next event (earnings, etc)
calender = df.calendar
calender.head(10)

# %%
