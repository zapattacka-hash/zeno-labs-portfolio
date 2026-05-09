#!/bin/bash
# Zeno-Phantom: Dangling CNAME & Takeover Scanner
# Author: Zacheriah Alan Potter (Zeno Labs)
# Description: Scans subdomain lists for vulnerable cloud routing.

if [ -z "$1" ]; then
    echo "Usage: ./zeno-phantom.sh <subdomains.txt>"
    exit 1
fi

TARGET_LIST=$1

echo -e "\n============================================="
echo -e "   👻 ZENO-PHANTOM: TAKEOVER SCANNER"
echo -e "============================================="

while read -r SUB; do
    # Skip empty lines
    [ -z "$SUB" ] && continue
    
    CNAME=$(dig $SUB CNAME +short)
    
    if [ -n "$CNAME" ]; then
        # Check against known hijackable cloud providers
        if echo "$CNAME" | grep -i -E "azurewebsites\.net|s3\.amazonaws\.com|github\.io|trafficmanager\.net"; then
            echo -e "[!] HIGH RISK CNAME FOUND: $SUB -> $CNAME"
        else
            echo -e "[*] SECURE CNAME ROUTING: $SUB -> $CNAME"
        fi
    else
        echo -e "[-] NO CNAME RECORD: $SUB"
    fi
done < "$TARGET_LIST"

echo -e "\n============================================="
echo -e "   [+] SCAN COMPLETE"
echo -e "=============================================\n"
