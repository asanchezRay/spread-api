import unittest
from unittest.mock import AsyncMock, patch
from api.alerts import set_alert, polling_alerts, alert_spread

class TestAlerts(unittest.IsolatedAsyncioTestCase):

    async def test_set_alert(self):
        market = "BTC-CLP"
        expected_result = {
            "message": "Alert saved successfully",
            "market": market,
            "alert": 0.05,
        }
        mock_calculate_spread = AsyncMock(return_value=0.05)
        with patch('api.alerts.calculate_spread', mock_calculate_spread):
            result = await set_alert(market)
            self.assertEqual(result, expected_result)
            mock_calculate_spread.assert_called_once_with(market)
    
    async def test_polling_alerts(self):
        market = "BTC-CLP"
        alert_spread[market] = 0.05

        current_spread = 0.06

        mock_calculate_spread = AsyncMock(return_value=current_spread)
        with patch('api.alerts.calculate_spread', mock_calculate_spread):
            # Testing when current spread is greater than alert spread
            result = await polling_alerts(market)
            self.assertTrue(result["is_greater"])
            self.assertFalse(result["is_less"])
            mock_calculate_spread.assert_called_once_with(market)

        current_spread = 0.04
        mock_calculate_spread = AsyncMock(return_value=current_spread)
        with patch('api.alerts.calculate_spread', mock_calculate_spread):
            # Testing when current spread is less than alert spread
            result = await polling_alerts(market)
            self.assertTrue(result["is_less"])
            self.assertFalse(result["is_greater"])
            mock_calculate_spread.assert_called_once_with(market)
    
    async def test_polling_alerts_invalid_market(self):
        market = "ETH-BTC"
        with self.assertRaises(ValueError) as context:
            await polling_alerts(market)
        self.assertEqual(str(context.exception), 'Alert spread not set')

