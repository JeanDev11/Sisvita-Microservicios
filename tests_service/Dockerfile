# Dockerfile para tests_service
# Usar la imagen oficial de Python desde Docker Hub.
FROM python:3.11.3-slim

# Establecer el directorio de trabajo en el contenedor.
WORKDIR /app

# Copiar inicialmente solo el archivo requirements.txt para aprovechar la caché de Docker.
COPY requirements.txt .

# Instalar los paquetes necesarios.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor.
COPY . .

# Exponer el puerto en el que se ejecuta tu aplicación Flask.
EXPOSE 5000

# Definir la variable de entorno.
ENV FLASK_APP=app.app
ENV PYTHONPATH=/app

# Ejecutar la aplicación Flask con el servidor gunicorn para producción.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]