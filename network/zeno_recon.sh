#!/bin/bash
# Zeno-Recon: Passive DNS & Subdomain Enumerator

if [ -z "$1" ]; then
    echo "Usage: ./zeno_recon.sh <domain.com>"
    exit 1
fi

TARGET=$1
echo -e "\n============================================="
echo -e "   🛰️ ZENO-RECON: PASSIVE ENUMERATION"
echo -e "   Target: $TARGET"
echo -e "=============================================\n"

echo "[*] Querying global DNS datasets..."
# Uses the HackerTarget Host Search API for passive recon
RESULT=$(curl -s "https://api.hackertarget.com/hostsearch/?q=$TARGET")

if echo "$RESULT" | grep -q "error"; then
    echo "[-] API Error or Limit Reached."
else
    echo -e "[+] Subdomains & IPs Discovered:\n"
    # Format output into a clean table
    echo "$RESULT" | awk -F, 'BEGIN {printf "%-35s | %-15s\n", "SUBDOMAIN", "IP ADDRESS"; print "--------------------------------------------------------"} {printf "%-35s | %-15s\n", $1, $2}'
fi

echo -e "\n============================================="
echo -e "   [+] RECON COMPLETE"
echo -e "=============================================\n"
