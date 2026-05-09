import socket
def scan():
    print("\n[!] ZENO-GHOST: SCANNING INTERNAL PORTS...")
    for p in [22, 80, 4444, 5555]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        if s.connect_ex(('127.0.0.1', p)) == 0:
            print(f"[*] ECHO DETECTED: Port {p} is OPEN")
        s.close()
    print("[*] Scan complete.")
scan()
