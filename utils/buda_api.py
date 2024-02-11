import requests

# Constante para la URL base de la API de Buda.com
BUDA_API_BASE_URL = "https://www.buda.com/api/v2"

# Función para obtener todos los markets
async def get_all_markets():
    response = requests.get(f"{BUDA_API_BASE_URL}/markets")
    if response.status_code == 200:
        return response.json()['markets']
    else:
        raise ValueError('An error occurred fetching markets')

# Función para obtener el spread de un mercado específico
async def calculate_spread(market: str) -> float:
    response = requests.get(f"{BUDA_API_BASE_URL}/markets/{market}/ticker")
    if response.status_code == 200:
        data = response.json()
        max_bid = float(data['ticker']['max_bid'][0])
        min_ask = float(data['ticker']['min_ask'][0])
        return min_ask - max_bid
    else:
        raise ValueError('An error occurred fetching markets')