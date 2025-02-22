from datetime import date
from typing import Dict
from .Stock import Stock  
from alpha_vantage import get_stock_price  # Import API function
import logging_messages as logging_messages

class Portfolio: 
    def __init__(self): 
        self.stocks: Dict[str, Stock] = {}

    def add_stock(self, stock_ticker: str, stock_name: str, shares: float, purchase_price: float, purchase_date: date):
        if stock_ticker in self.stocks:
            raise ValueError(logging_messages.STOCK_IN_PORTFOLIO)

        current_price = get_stock_price(stock_ticker)  # Fetch real-time stock price
        stock = Stock(stock_ticker, stock_name, shares, purchase_price, current_price, purchase_date)
        self.stocks[stock_ticker] = stock
        print(logging_messages.STOCK_ADDED)

    def remove_stock(self, stock_ticker: str):
        if stock_ticker in self.stocks:
            del self.stocks[stock_ticker]
            print(logging_messages.STOCK_REMOVED)
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)

    def update_stock(self, stock_ticker: str, new_shares: float):
        if stock_ticker in self.stocks:
            stock = self.stocks[stock_ticker]
            stock.current_shares = new_shares
            print(logging_messages.UPDATED_NUM_SHARES)
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)

    def update_stock_price(self, stock_ticker: str):
        if stock_ticker in self.stocks:
            stock = self.stocks[stock_ticker]
            stock.current_price = get_stock_price(stock_ticker)
            print(f"Updated {stock_ticker} price to {stock.current_price}")
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)

    def get_stock(self, stock_ticker: str) -> Stock:
        if stock_ticker in self.stocks:
            return self.stocks[stock_ticker]
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)

    def calculate_portfolio_value(self):
        return sum(stock.current_shares * stock.current_price for stock in self.stocks.values())
