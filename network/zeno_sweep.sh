#!/bin/bash
# Zeno-Sweep: Rapid Subnet Discovery

if [ -z "$1" ]; then
    echo "Usage: ./zeno_sweep.sh <192.168.1>"
    exit 1
fi

SUBNET=$1
echo -e "\n============================================="
echo -e "   📡 ZENO-SWEEP: SUBNET MAPPER"
echo -e "   Target Subnet: $SUBNET.0/24"
echo -e "=============================================\n"

echo "[*] Launching asynchronous ICMP probes..."

for i in {1..254}; do
    # Ping with 1 count, 1 sec timeout, run in background (&) for speed
    ping -c 1 -W 1 "$SUBNET.$i" > /dev/null 2>&1 && echo "[+] Host Up: $SUBNET.$i" &
done

# Wait for all background tasks to finish
wait
echo -e "\n[+] Sweep complete."
