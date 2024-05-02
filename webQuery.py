import requests

def get_stock_data(symbol):
    base_url = "https://www.alphavantage.co/query"
    api_key = "11R1UGRP10LKEMDQ"  
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    time_series_data = data.get("Time Series (Daily)")
    if time_series_data is None:
        return None

    dates = list(time_series_data.keys())
    prices = [float(time_series_data[date]["4. close"]) for date in dates]

    return {"dates": dates, "prices": prices}
