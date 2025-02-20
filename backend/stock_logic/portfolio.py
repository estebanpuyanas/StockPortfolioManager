from datetime import date 
from typing import Dict
from .Stock import Stock  # Assuming the Stock class is defined in stock.py in the same directory
import logging_messages as logging_messages

# Class representing a portfolio:
class Portfolio: 
    
    # Constructor:
    def __init__(self): 
        self.stocks: Dict[str, Stock] = {} # Intialize empty dictionary to store the stocks. 

    # Add stock to portfolio: 
    def add_stock(self, stock_ticker: str, stock: Stock) -> None: 
        if Stock.stock_ticker in self.stocks: 
            raise ValueError(logging_messages.STOCK_IN_PORTFOLIO)
        else:
            self.stocks[stock_ticker] = stock
            print(logging_messages.STOCK_ADDED)

    # Remove stock from portfolio:
    def remove_stock(self, stock_ticker: str) -> None: 
        if stock_ticker in self.stocks: 
            del self.stocks[stock_ticker]
            print(logging_messages.STOCK_REMOVED)
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)
        
    # Update stock in portfolio: 
    def update_stock(self, stock_ticker: str, new_shares: float):
        if stock_ticker in self.stocks:
            stock = self.stocks[stock_ticker]
            stock.current_shares = new_shares
            print(logging_messages.UPDATED_NUM_SHARES)
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)
        
    # Get stock from portfolio:
    def get_stock(self, stock_ticker: str) -> Stock: 
        if stock_ticker in self.stocks: 
            return self.stocks[stock_ticker]
        else:
            raise ValueError(logging_messages.STOCK_NOT_IN_PORTFOLIO)


