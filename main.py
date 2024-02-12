from fastapi import FastAPI
from api.spreads import get_spreads, get_spread
from api.alerts import set_alert, polling_alerts

app = FastAPI()

# Endpoint para calcular el spread de un mercado específico
@app.get("/spread/{market}")
async def get_spread_wrapper(market: str):
    return await get_spread(market)

# Endpoint para obtener el spread de todos los mercados en una sola llamada
@app.get("/spreads")
async def get_all_spreads():
    return await get_spreads()

# Endpoint para guardar un spread de "alerta"
@app.post("/alert/{market}")
async def set_alert_wrapper(market):
    return await set_alert(market)

# Endpoint para realizar polling y verificar si el spread actual supera el de alerta
@app.get("/polling/{market}")
async def polling_alerts_wrapper(market):
    return await polling_alerts(market)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
