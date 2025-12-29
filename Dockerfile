# Usa un'immagine Python leggera
FROM python:3.9-alpine

# Installa l'utility ping (spesso non presente nelle immagini slim)
RUN apk add --no-cache iputils

# Imposta la cartella di lavoro
WORKDIR /app

# Copia lo script nella cartella
COPY script.py .

# Esegue lo script
CMD ["python", "-u", "script.py"]
