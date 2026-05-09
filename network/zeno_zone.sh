#!/bin/bash
# Zeno-Zone: DNS Zone Transfer Vulnerability Scanner

if [ -z "$1" ]; then
    echo "Usage: ./zeno_zone.sh <target-domain.com>"
    exit 1
fi

DOMAIN=$1

echo -e "\n============================================="
echo -e "   🗺️ ZENO-ZONE: AXFR AUDITOR"
echo -e "   Target: $DOMAIN"
echo -e "=============================================\n"

# Find all authoritative nameservers for the domain
echo "[*] Discovering authoritative nameservers..."
NAMESERVERS=$(host -t ns $DOMAIN | awk '{print $4}')

if [ -z "$NAMESERVERS" ]; then
    echo "[-] No nameservers found. Exiting."
    exit 1
fi

# Attempt AXFR against each nameserver
for NS in $NAMESERVERS; do
    echo "[*] Attempting Zone Transfer against: $NS"
    # Using dig for the AXFR request
    RESULT=$(dig @$NS $DOMAIN AXFR +short)
    
    if [ -n "$RESULT" ] && ! echo "$RESULT" | grep -q "Transfer failed"; then
        echo -e "\n[!] VULNERABILITY DETECTED: Zone Transfer Successful on $NS!"
        echo -e "[!] Dumping DNS Records:\n"
        echo "$RESULT" | head -n 15
        echo "...(Truncated for terminal layout)..."
        echo -e "\n[!] Full zone map acquired."
        exit 0
    else
        echo "  [-] Failed (Secure)."
    fi
done

echo -e "\n[+] Audit Complete. Nameservers are secure against AXFR."
