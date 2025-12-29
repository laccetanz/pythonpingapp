FROM python:3.9-alpine

# Installa iputils e le dipendenze per requests
RUN apk add --no-cache iputils

# Installa requests
RUN pip install --no-cache-dir requests

WORKDIR /app
COPY script.py .

CMD ["python", "-u", "script.py"]
