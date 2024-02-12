from utils.buda_api import calculate_spread, get_all_markets
from pydantic import BaseModel

# Modelo de respuesta para la obtención de spreads
class SpreadResponseModel(BaseModel):
    market: str
    spread: float
    
# Función para obtener el spread de un mercado
async def get_spread(market: str) -> SpreadResponseModel:
    spread = await calculate_spread(market)
    return SpreadResponseModel(market=market, spread=spread)

# Función para obtener el spread de todos los mercados
async def get_spreads():
    markets = await get_all_markets()
    return [await get_spread(market['id']) for market in markets]