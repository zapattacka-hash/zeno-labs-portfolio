import os
import datetime

def check_vitals():
    print(f"\n[!] ZENO-SENTINEL: {datetime.datetime.now()}")
    # Check Uptime
    uptime = os.popen('uptime -p').read().strip()
    # Check Memory
    mem = os.popen('free -m | grep Mem').read().split()
    
    print(f"[*] SYSTEM {uptime}")
    print(f"[*] MEMORY: {mem[2]}MB used / {mem[1]}MB total")
    print("[*] STATUS: NOMINAL")
check_vitals()
