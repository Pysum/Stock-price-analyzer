import plotly.graph_objs as go
import pandas as pd
import requests

# Define the stock symbol and timeframe
symbol = "AAPL"
timeframe = "D"

# Fetch the data from the API
url = f"https://finnhub.io/api/v1/stock/candle?symbol={symbol}&resolution={timeframe}&token=ch25vj9r01qroac5tj9gch25vj9r01qroac5tja0"
response = requests.get(url)
data = response.json()

# Convert the data into a Pandas DataFrame
df = pd.DataFrame({
    "time": pd.to_datetime(data["t"], unit="s"),  # convert Unix timestamp to datetime
    "open": data["o"],
    "high": data["h"],
    "low": data["l"],
    "close": data["c"],
    "volume": data["v"]
})

# Resample the data to fill any missing values and make sure the data is evenly spaced
df.set_index("time", inplace=True)
df = df.resample("D").agg({
    "open": "first",
    "high": "max",
    "low": "min",
    "close": "last",
    "volume": "sum"
})
df = df.ffill()

# Create the candlestick chart using plotly
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                      open=df['open'],
                                      high=df['high'],
                                      low=df['low'],
                                      close=df['close'])])

# Customize the layout of the chart
fig.update_layout(title=symbol + ' Stock Price',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)

# Show the chart
fig.show()
