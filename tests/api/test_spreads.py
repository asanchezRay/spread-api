import unittest
from unittest.mock import AsyncMock, patch
from api.spreads import get_spread, get_spreads

class TestSpreads(unittest.IsolatedAsyncioTestCase):

    async def test_get_spread(self):
        market = "BTC-CLP"
        mock_calculate_spread = AsyncMock(return_value=0.05)
        with patch('api.spreads.calculate_spread', mock_calculate_spread):
            result = await get_spread(market)
            self.assertEqual(result, {"market": market, "spread": 0.05})
            mock_calculate_spread.assert_called_once_with(market)

    async def test_get_spreads(self):
        mock_get_all_markets = AsyncMock(return_value=[{"id": "BTC-CLP"}, {"id": "ETH-BTC"}])
        mock_calculate_spread = AsyncMock(return_value=0.05)
        with patch('api.spreads.get_all_markets', mock_get_all_markets), \
             patch('api.spreads.calculate_spread', mock_calculate_spread):
            result = await get_spreads()
            expected_result = [{"market": "BTC-CLP", "spread": 0.05}, {"market": "ETH-BTC", "spread": 0.05}]
            self.assertEqual(result, expected_result)
            mock_get_all_markets.assert_called_once()
            mock_calculate_spread.assert_any_call("BTC-CLP")
            mock_calculate_spread.assert_any_call("ETH-BTC")
