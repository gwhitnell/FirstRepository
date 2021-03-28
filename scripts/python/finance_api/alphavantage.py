from alpha_vantage.timeseries import TimeSeries
from config import alphakey

key = alphakey

ts = TimeSeries(key)

aapl, meta = ts.get_daily(symbol="AAPL")
print(aapl["2020-09-01"])
