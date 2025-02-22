from datetime import date
from alpha_vantage import get_stock_price  # Import API function

# Class representing a stock
class Stock:
    def __init__(self, stock_ticker: str, stock_name: str, current_shares: float, purchase_price: float, purchase_date: date): 
        self.stock_ticker = stock_ticker
        self.stock_name = stock_name
        self.current_shares = current_shares
        self.purchase_price = purchase_price
        self.current_price = get_stock_price(stock_ticker)  # Fetch current price at instantiation
        self.purchase_date = purchase_date

    def update_price(self):
        """Fetches the latest stock price from AlphaVantage and updates the stock."""
        self.current_price = get_stock_price(self.stock_ticker)
        print(f"Updated {self.stock_ticker} price to {self.current_price}")

    def __str__(self):
        """String representation of the stock object."""
        return (f"Stock({self.stock_ticker}, {self.stock_name}, Shares: {self.current_shares}, "
                f"Purchase Price: {self.purchase_price}, Current Price: {self.current_price}, "
                f"Purchase Date: {self.purchase_date})")

    def __repr__(self):
        """Representation of the stock object."""
        return self.__str__()
