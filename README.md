# Spread API para Buda.com

Esta API proporciona funcionalidades para calcular los spreads del mercado de criptomonedas utilizando la API de Buda.com. Además, permite a los usuarios establecer y monitorear alertas de spread en tiempo real.

## Funcionalidades

- Cálculo del spread para cualquier mercado disponible en Buda.com.
- Obtención de spreads de todos los mercados con una sola llamada a la API.
- Guardar un spread de "alerta" para comparar con el spread actual mediante polling.


### Prerrequisitos

- **Docker**: Es necesario tener Docker instalado para ejecutar la aplicación. Puedes descargar e instalar Docker desde [aquí](https://docs.docker.com/get-docker/).

#### Para usuarios de Windows (Opcional)

Si estás utilizando Windows, también necesitarás tener Make instalado. Puedes descargar e instalar Make desde [aquí](https://www.gnu.org/software/make/).

#### Para usuarios de Linux o macOS (Opcional)

Si estás utilizando un sistema operativo basado en GNU, como Linux o macOS, es probable que ya tengas Make instalado. Puedes verificarlo ejecutando el siguiente comando en tu terminal:

```bash
make --version 
```

Si Make está instalado, verás información sobre la versión. En caso de no tenerlo instalado, puedes instalarlo fácilmente en tu sistema ejecutando el siguiente comando en tu consola:

```bash
sudo apt-get install make
```

Una vez instalado, podrás utilizar Make para facilitar la construcción y ejecución de la aplicación.

### Instalación

1. Clona el repositorio:
    ``` bash
    git clone https://github.com/asanchezRay/spread-api
    ```
2. Construye y ejecuta la imagen Docker:
    
    Hay 2 opciones para esto
    
    - Utilizando el MakeFile
        ``` bash
        make build
        make run
        ```

    - Directamente los comandos de Docker
        ``` bash
        docker build -t spread_api .
        docker run -d -p 8000:8000 spread_api
        ```


## Uso

Después de instalar y ejecutar la API en tu entorno local, estará funcionando en un contenedor de Docker. Puedes realizar pruebas utilizando la documentación de Swagger disponible en http://localhost:8000/docs, a través de [Postman](https://www.postman.com) o ejecutando comandos en tu consola con `curl`.

### Endpoints
#### Obtener el Spread de un Mercado Específico

- **Descripción**: Este endpoint permite obtener el spread para un mercado específico.
- **URL**:  `/spread/{market}`
- **Método HTTP**: GET
- **Parametros de URL**:
    - `market`: El mercado del cual obtener el spread.
- **Ejemplo de uso**:
    ```bash
    curl http://localhost:8000/spread/BTC-CLP
    ```

#### Obtener los Spreads de Todos los Mercados

- **Descripción**: Este endpoint permite obtener el spread de todos los mercados en una sola llamada.
- **URL**:  `/spreads`
- **Método HTTP**: GET
- **Ejemplo de uso**:
    ```bash
    curl http://localhost:8000/spreads
    ```

#### Guardar un Spread de Alerta

- **Descripción**: Este endpoint permite guardar un spread de alerta para un mercado específico.
- **URL**:  `/alert/{market}`
- **Método HTTP**: POST
- **Parametros de URL**:
    - `market`:  El mercado para el cual guardar el spread de alerta.
- **Ejemplo de uso**:
    ```bash
    curl -X POST http://localhost:8000/alert/BTC-CLP
    ```

#### Realizar Polling de Alertas

- **Descripción**: Este endpoint permite realizar polling y verificar si el spread actual supera el de alerta.
- **URL**:  `/polling/{market}`
- **Método HTTP**: GET
- **Parametros de URL**:
    - `market`:  El mercado para el cual realizar el polling.
- **Ejemplo de uso**:
    ```bash
    curl http://localhost:8000/polling/BTC-CLP
    ```


