from utils.buda_api import calculate_spread
from pydantic import BaseModel

alert_spread = {}

class SetAlertResponseModel(BaseModel):
    market: str
    alert: float
    message: str

class PollingAlertResponseModel(BaseModel):
    alert: float
    market: str
    spread: float
    is_greater: bool
    is_less: bool

# Función para guardar un spread de "alerta"
async def set_alert(market) -> SetAlertResponseModel:
    spread = await calculate_spread(market)
    alert_spread[market] = spread
    return SetAlertResponseModel(market=market, alert=spread, message="Alert saved successfully")

# Función para realizar polling y verificar si el spread actual supera el de alerta
async def polling_alerts(market) -> PollingAlertResponseModel:
    if market not in alert_spread:
        raise ValueError('Alert spread not set')
    spread = await calculate_spread(market)
    
    diff = (float)(spread) - (float)(alert_spread[market])
    return PollingAlertResponseModel(
        alert=alert_spread[market],
        market=market,
        spread=spread,
        is_greater=  diff > 0,
        is_less = diff < 0
    )