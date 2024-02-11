from fastapi import FastAPI
import requests

app = FastAPI()

# Constante para la URL base de la API de Buda.com
BUDA_API_BASE_URL = "https://www.buda.com/api/v2"

alert_spread = {}

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

# Endpoint para calcular el spread de un mercado específico
@app.get("/spread/{market}")
async def get_spread(market: str):
    spread = await calculate_spread(market)
    return {"market": market, "spread": spread}

# Endpoint para obtener el spread de todos los mercados en una sola llamada
@app.get("/spreads")
async def get_all_spreads():
    markets = await get_all_markets()
    return [await get_spread(market['id']) for market in markets if await get_spread(market['id']) is not None]

# Endpoint para guardar un spread de "alerta"
@app.post("/alert/{market}")
async def set_alert(market):
    spread = await get_spread(market)
    alert_spread[market] = spread['spread']
    return {
        "message": "Alert saved successfully",
        "alert": spread,
    }

# Endpoint para realizar polling y verificar si el spread actual supera el de alerta
@app.get("/polling/{market}")
async def polling_alerts(market):
    if market not in alert_spread:
        raise ValueError('Alert spread not set')
    spread = await get_spread(market)
    
    diff = (float)(spread["spread"]) - (float)(alert_spread[market])
    return {
        "alert": alert_spread[market],
        "spread": spread,
        "is_greater": diff > 0,
        "is_less": diff < 0
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
