#!/bin/bash
# Zeno-Knock: Covert Port Authorization

if [ "$#" -ne 4 ]; then
    echo "Usage: ./zeno_knock.sh <TARGET_IP> <PORT1> <PORT2> <PORT3>"
    exit 1
fi

TARGET=$1
P1=$2
P2=$3
P3=$4

echo -e "\n============================================="
echo -e "   🚪 ZENO-KNOCK: STEALTH AUTHORIZATION"
echo -e "=============================================\n"

echo "[*] Executing sequence on $TARGET ($P1 -> $P2 -> $P3)..."

# Connects to the ports rapidly and closes the connection without sending data
# 2>/dev/null hides the "Connection refused" errors, keeping it stealthy
(echo >/dev/tcp/$TARGET/$P1) 2>/dev/null
sleep 0.5
(echo >/dev/tcp/$TARGET/$P2) 2>/dev/null
sleep 0.5
(echo >/dev/tcp/$TARGET/$P3) 2>/dev/null

echo "[+] Knock sequence transmitted. If daemon is active, payload port is open."
