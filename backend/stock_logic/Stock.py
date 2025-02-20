from datetime import date

# Class representing stock: 
class Stock:
    
    # Constructor: 
    def __init__(self, stock_ticker: str, stock_name: str, current_shares: float, purchase_price: float, current_price: float, purchase_date: date): 
        self.stock_ticker = stock_ticker
        self.stock_name = stock_name
        self.current_shares = current_shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date
        

    # Basic getters: 
    def get_ticker(self): 
        return self.stock_ticker
    
    def get_name(self): 
        return self.stock_name
    
    def get_curr_shares(self): 
        return self.current_shares
    
    def get_purchase_price(self):
        return self.purchase_price
    
    def get_curr_price(self):
        return self.current_price
    
    def get_purchase_date(self):
        return self.purchase_date
    