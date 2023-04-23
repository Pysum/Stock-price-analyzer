# Stock-price-analyzer

The provided code imports the plotly.graph_objs module as go and the pandas module as pd, 
and also imports the requests module. 
The code then defines the stock symbol and timeframe, and fetches the data from the Finnhub API using the requests module. 
The response from the API is converted into a Pandas DataFrame that contains the columns "time", "open", "high", "low", and "...".
The "time" column is created by converting the Unix timestamp in the "t" key of the response dictionary to a Pandas datetime format using pd.to_datetime(). 
The other columns are created by extracting the corresponding values from the response dictionary. The code uses Plotly to visualize the data in the DataFrame.
