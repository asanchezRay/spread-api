import unittest
from unittest.mock import patch
from utils.buda_api import get_all_markets, calculate_spread

class TestBudaAPI(unittest.IsolatedAsyncioTestCase):

    async def test_get_all_markets_success(self):
        mock_response = [{"id": "BTC-CLP"}, {"id": "ETH-BTC"}]
        with patch('utils.buda_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {'markets': mock_response}
            result = await get_all_markets()
            self.assertEqual(result, mock_response)

    async def test_get_all_markets_failure(self):
        with patch('utils.buda_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            with self.assertRaises(ValueError):
                await get_all_markets()

    async def test_calculate_spread_success(self):
        market = "BTC-CLP"
        mock_response = {
            'ticker': {
                'max_bid': ['1000'],
                'min_ask': ['1100']
            }
        }
        with patch('utils.buda_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            result = await calculate_spread(market)
            self.assertEqual(result, 100)

    async def test_calculate_spread_failure(self):
        market = "BTC-CLP"
        with patch('utils.buda_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            with self.assertRaises(ValueError):
                await calculate_spread(market)

