from utils.buda_api import calculate_spread, get_all_markets

# Función para obtener el spread de un mercado
async def get_spread(market: str):
    spread = await calculate_spread(market)
    return {"market": market, "spread": spread}

# Función para obtener el spread de todos los mercados
async def get_spreads():
    markets = await get_all_markets()
    return [await get_spread(market['id']) for market in markets if await get_spread(market['id']) is not None]