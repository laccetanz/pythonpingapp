import os
import time

target = "8.8.8.8" # IP di Google DNS

print(f"Avvio monitoraggio ping verso {target}...")

while True:
    response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")
    if response == 0:
        print(f"{time.ctime()}: Google è raggiungibile")
    else:
        print(f"{time.ctime()}: Google NON è raggiungibile")
    time.sleep(5)
