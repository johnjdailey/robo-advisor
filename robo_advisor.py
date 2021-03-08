import json
import requests
import os
import csv

#converting numbers into price (used in previous projects)
def to_usd(my_price):
    return f"${my_price:,.2f}" 

ticker = ""
api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
request_url= "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(request_url)
#parse response texts from string to dictionary
parsed_response = json.loads(response.text)

#finding time it was last refreshed
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


#finding latest prices
tsd=parsed_response["Time Series (5min)"] #have been exploring with smaller intervals because I am trying to adapt this code to crypto day-trading eventually using Binance API 
dates = list(tsd.keys())
latest_interval = dates[0] # pulling the most recent day from list, assuming latest day is first

latest_closing_price = tsd[latest_interval]["4. close"]

#breakpoint()



#time_series_daily = parsed_response["Time Series (Daily)"]

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #find current date / when request was made using date/time module
print("-------------------------")
print(f"LATEST TIME:  {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_closing_price))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")