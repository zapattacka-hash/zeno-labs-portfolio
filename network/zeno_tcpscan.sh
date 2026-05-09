#!/bin/bash
# Zeno-Scanner: Native Bash TCP Port Scanner

if [ -z "$1" ]; then
    echo "Usage: ./zeno_tcpscan.sh <IP_ADDRESS>"
    exit 1
fi

TARGET=$1
PORTS=(21 22 23 25 53 80 111 139 443 445 3306 3389 8080 8443)

echo -e "\n============================================="
echo -e "   🔍 ZENO-SCANNER: NATIVE TCP SWEEPER"
echo -e "   Target: $TARGET"
echo -e "=============================================\n"

echo "[*] Initiating scan sequence..."

for PORT in "${PORTS[@]}"; do
    # Try to open a TCP connection with a 1-second timeout
    (timeout 1 bash -c "echo >/dev/tcp/$TARGET/$PORT") 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "  [+] PORT $PORT: OPEN"
    fi
done

echo -e "\n[+] Scan complete."
