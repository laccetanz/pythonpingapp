import os
import time
import requests

target_ip = "8.8.8.8"
api_url = "https://jsonplaceholder.typicode.com/todos/1"

print(f"Monitoraggio avviato. Target Ping: {target_ip} | Test API: {api_url}")

while True:
    # 1. TEST PING
    response_ping = os.system(f"ping -c 1 -W 2 {target_ip} > /dev/null 2>&1")
    if response_ping == 0:
        ping_status = "PING OK"
    else:
        ping_status = "PING FAIL"

    # 2. TEST API (Requests)
    try:
        response_api = requests.get(api_url, timeout=5)
        if response_api.status_code == 200:
            api_status = f"OK (ID: {response_api.json().get('id')})"
        else:
            api_status = f"HTTP ERROR {response_api.status_code}"
    except Exception as e:
        api_status = f"CONNECTION ERROR: {e}"

    # Stampa i risultati
    print(f"{time.ctime()} -> Ping: {ping_status} | API: {api_status}")
    
    time.sleep(5)
