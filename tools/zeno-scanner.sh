#!/bin/bash
# Zeno-Scanner: Edge Compliance & Recon Automation
# Author: Zacheriah Alan Potter (Zeno Labs)
# Description: Automates edge fingerprinting and trust policy extraction.

if [ -z "$1" ]; then
    echo "Usage: ./zeno-scanner.sh <domain>"
    exit 1
fi

TARGET=$1

echo -e "\n============================================="
echo -e "   🛡️ ZENO-SCANNER: TARGET [ $TARGET ]"
echo -e "============================================="

# 1. Edge/WAF Fingerprinting
echo -e "\n[*] Fingerprinting Edge Infrastructure..."
curl -Is -m 5 "https://www.$TARGET" | grep -i -E "Server|Via|X-Cache|Strict-Transport-Security" | sed 's/^/    -> /'

# 2. Origin IP Mapping
echo -e "\n[*] Resolving Origin IP..."
dig $TARGET +short | sed 's/^/    -> /'

# 3. Trust Policies (SPF/DMARC)
echo -e "\n[*] Extracting Trust Policies..."
dig $TARGET TXT +short | grep "v=spf1" | sed 's/^/    -> /'
dig _dmarc.$TARGET TXT +short | sed 's/^/    -> /'

echo -e "\n============================================="
echo -e "   [+] SCAN COMPLETE"
echo -e "=============================================\n"
