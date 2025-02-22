
import unittest
from datetime import date
from model import Portfolio
from model import Stock

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        """Set up a portfolio and add stocks before each test."""
        self.portfolio = Portfolio()
        self.apple = Stock("AAPL", "Apple Inc.", 10, 150.0, date(2024, 2, 20))
        self.portfolio.add_stock("AAPL", self.apple)

    def test_add_stock(self):
        """Ensure a stock is added correctly."""
        self.assertIn("AAPL", self.portfolio.stocks)

    def test_update_stock(self):
        """Test updating shares in a stock."""
        self.portfolio.update_stock("AAPL", 20)
        self.assertEqual(self.portfolio.stocks["AAPL"].current_shares, 20)

    def test_remove_stock(self):
        """Ensure stock removal works."""
        self.portfolio.remove_stock("AAPL")
        self.assertNotIn("AAPL", self.portfolio.stocks)

if __name__ == "__main__":
    unittest.main()
