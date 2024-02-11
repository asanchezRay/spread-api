from utils.buda_api import calculate_spread

alert_spread = {}

# Función para guardar un spread de "alerta"
async def set_alert(market):
    spread = await calculate_spread(market)
    alert_spread[market] = spread
    return {
        "message": "Alert saved successfully",
        "market": market,
        "alert": spread,
    }

# Función para realizar polling y verificar si el spread actual supera el de alerta
async def polling_alerts(market):
    if market not in alert_spread:
        raise ValueError('Alert spread not set')
    spread = await calculate_spread(market)
    
    diff = (float)(spread) - (float)(alert_spread[market])
    return {
        "alert": alert_spread[market],
        "market": market,
        "spread": spread,
        "is_greater": diff > 0,
        "is_less": diff < 0
    }