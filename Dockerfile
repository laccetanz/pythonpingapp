FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia il file dei requisiti e installa tutto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto (anche se useremo il volume per lo script)
COPY . .

CMD ["python", "-u", "script.py"]
