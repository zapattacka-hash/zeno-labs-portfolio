import socket
import datetime

def start_honeypot(port=2222):
    print("=============================================")
    print("   🍯 ZENO-HONEYPOT: DECEPTIVE LISTENER")
    print("=============================================\n")
    print(f"[*] Starting fake SSH service on port {port}...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    
    print("[*] Waiting for unauthorized connections. (Ctrl+C to stop)\n")
    
    try:
        while True:
            conn, addr = s.accept()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[!] {timestamp} - INTRUSION DETECTED: Connection from {addr[0]}:{addr[1]}")
            
            # Send a fake OpenSSH banner to trick scanners
            conn.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n")
            
            # Log whatever they send back
            try:
                data = conn.recv(1024)
                if data:
                    print(f"    Payload: {data.decode('utf-8', 'ignore').strip()}")
            except Exception:
                pass
                
            conn.close()
            print("[*] Connection dropped and logged.\n")
    except KeyboardInterrupt:
        print("\n[-] Honeypot offline.")
        s.close()

start_honeypot()
