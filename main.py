from fastapi import FastAPI, APIRouter, Path
from typing import List
from api.spreads import get_spreads, get_spread, SpreadResponseModel
from api.alerts import set_alert, polling_alerts, SetAlertResponseModel, PollingAlertResponseModel

app = FastAPI()

router = APIRouter()

# Endpoint para calcular el spread de un mercado específico
@router.get("/spread/{market}", response_model=SpreadResponseModel, response_model_exclude_unset=True)
async def get_spread_wrapper(market: str = Path(..., example="BTC-CLP")) -> SpreadResponseModel:
    """
    Obtiene el spread para un mercado específico.

    Args:
        market (str): El mercado del cual obtener el spread.

    Returns:
        SpreadResponseModel: Un objeto que contiene el spread del mercado.
    """
    return await get_spread(market)

# Endpoint para obtener el spread de todos los mercados en una sola llamada
@router.get("/spreads", response_model=List[SpreadResponseModel])
async def get_all_spreads_wrapper():
    """
    Obtiene el spread de todos los mercados.

    Returns:
        List[SpreadResponseModel]: Una lista de objetos que contienen los spreads de todos los mercados.
    """
    return await get_spreads()

# Endpoint para guardar un spread de "alerta"
@router.post("/alert/{market}", response_model=SetAlertResponseModel, response_model_exclude_unset=True)
async def set_alert_wrapper(market: str = Path(..., example="BTC-CLP")):
    """
    Guarda un spread de alerta para un mercado específico.

    Args:
        market (str): El mercado para el cual guardar el spread de alerta.

    Returns:
        dict: Un objeto que indica el éxito de la operación.
    """
    return await set_alert(market)

# Endpoint para realizar polling y verificar si el spread actual supera el de alerta
@router.get("/polling/{market}", response_model=PollingAlertResponseModel, response_model_exclude_unset=True)
async def polling_alerts_wrapper(market: str = Path(..., example="BTC-CLP")):
    """
    Realiza polling y verifica si el spread actual supera el de alerta.

    Args:
        market (str): El mercado para el cual realizar el polling.

    Returns:
        PollingAlertResponseModel: Un objeto que indica si el spread actual supera el de alerta.
    """
    return await polling_alerts(market)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
