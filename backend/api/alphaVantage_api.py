import requests
import os
import logging_messages as messages
from dotenv import load_dotenv

load_dotenv() 
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Base URL for AlphaVantage API
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")  # Store your API key in an environment variable

def get_stock_price(stock_ticker: str) -> float:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_ticker,
        "apikey": API_KEY
    }
    
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()

    if "Global Quote" in data:
        return float(data["Global Quote"]["05. price"])
    else:
        raise ValueError(f"Could not fetch stock price for {stock_ticker}: {data}")

def get_stock_info(stock_ticker: str):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock_ticker,
        "interval": "5min",
        "apikey": API_KEY
    }
    
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()

    if "Time Series (5min)" in data:
        latest_time = sorted(data["Time Series (5min)"].keys())[-1]
        latest_data = data["Time Series (5min)"][latest_time]
        return {
            "price": float(latest_data["1. open"]),
            "volume": int(latest_data["5. volume"])
        }
    else:
        raise ValueError(messages.STOCK_INFO_FETCH_FAIL)
