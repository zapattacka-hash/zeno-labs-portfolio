import ipaddress
import sys

def analyze_subnet(cidr_string):
    try:
        network = ipaddress.IPv4Network(cidr_string, strict=False)
        print("=============================================")
        print("   🕸️ ZENO-SUBNET: ARCHITECTURE ANALYZER")
        print("=============================================\n")
        
        print(f"[+] Target CIDR     : {cidr_string}")
        print(f"[+] Network Address : {network.network_address}")
        print(f"[+] Subnet Mask     : {network.netmask}")
        print(f"[+] Broadcast IP    : {network.broadcast_address}")
        print(f"[+] Usable Hosts    : {network.num_addresses - 2}")
        print(f"[+] IP Range        : {network.network_address + 1} - {network.broadcast_address - 1}")
    except ValueError as e:
        print(f"[-] Invalid CIDR Format: {e}")

# Default execution
analyze_subnet("192.168.1.50/26")
