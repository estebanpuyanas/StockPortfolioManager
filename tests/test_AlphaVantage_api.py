import unittest
from unittest.mock import patch
from backend.api.alphaVantage_api import AlphaVantageAPI 

class TestAlphaVantageAPI(unittest.TestCase):
    @patch("backend.api.alphaVantage_api.requests.get")
    def test_get_stock_price(self, mock_get):
        mock_get.return_value.json.return_value = {
            "Global Quote": {"05. price": "150.00"}
        }
        api = AlphaVantageAPI("fake_api_key")
        price = api.get_stock_price("AAPL")
        self.assertEqual(price, 150.00)

if __name__ == "__main__":
    unittest.main()
