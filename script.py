import os
import time
import threading
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

# Variabile globale per memorizzare l'ultimo stato
status_report = {"last_ping": "Inizializzazione...", "api_test": "Inizializzazione..."}

def monitor_logic():
    target = "8.8.8.8"
    while True:
        # Test Ping
        response = os.system(f"ping -c 1 -W 2 {target} > /dev/null 2>&1")
        status_report["last_ping"] = "ONLINE" if response == 0 else "OFFLINE"
        
        # Esempio BS4: prendiamo il titolo di una pagina
        try:
            r = requests.get("https://www.google.com")
            soup = BeautifulSoup(r.text, 'html.parser')
            status_report["api_test"] = f"Connesso a {soup.title.string}"
        except Exception as e:
            status_report["api_test"] = f"Errore: {e}"
            
        time.sleep(5)

@app.route('/')
def home():
    return f"""
    <h1>Monitoraggio Server</h1>
    <p><b>Stato Google Ping:</b> {status_report['last_ping']}</p>
    <p><b>Test Web (BS4):</b> {status_report['api_test']}</p>
    <hr>
    <p>Ultimo aggiornamento: {time.ctime()}</p>
    <script>setTimeout(function() {{ location.reload(); }}, 5000);</script>
    """

if __name__ == '__main__':
    # Avvia il monitoraggio in un thread separato
    threading.Thread(target=monitor_logic, daemon=True).start()
    # Avvia Flask sulla porta 5000
    app.run(host='0.0.0.0', port=5000)
