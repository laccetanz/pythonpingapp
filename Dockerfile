FROM python:3.9-slim

# Installiamo i tool di rete e puliamo la cache per tenere l'immagine piccola
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# Installiamo la libreria requests
RUN pip install --no-cache-dir requests

WORKDIR /app
COPY script.py .

CMD ["python", "-u", "script.py"]
