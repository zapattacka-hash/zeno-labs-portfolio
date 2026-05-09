import time

WHITELIST = {80, 443, 8080, 22, 4444}

def get_listening_ports():
    ports = set()
    try:
        # Direct read of the kernel's TCP table
        with open("/proc/net/tcp", "r") as f:
            lines = f.readlines()[1:] # Skip header
            for line in lines:
                parts = line.split()
                # '0A' in the second column means the state is 'LISTEN'
                state = parts[3]
                if state == "0A":
                    # The local address/port is in hex: e.g., 00000000:115C
                    local_addr = parts[1]
                    port_hex = local_addr.split(":")[1]
                    port = int(port_hex, 16)
                    ports.add(port)
    except Exception:
        pass
    return ports

print("=============================================")
print("   🛡️ ZENO-AUTOGUARD: KERNEL-READ MODE")
print("=============================================")
print(f"[*] Whitelisted Ports: {WHITELIST}")
print("[*] Sentry active. Reading /proc/net/tcp directly...")

try:
    while True:
        current_ports = get_listening_ports()
        for port in current_ports:
            if port not in WHITELIST:
                print(f"\n[!] ALERT: Unauthorized Listener on Port {port}!")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Sentry standing down.")
