# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt a la imagen
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Crea un punto de montaje en el contenedor en /app
VOLUME /app

# Expone el puerto 8000 para que pueda ser accedido externamente
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
