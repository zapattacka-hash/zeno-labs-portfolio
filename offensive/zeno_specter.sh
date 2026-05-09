#!/bin/bash
# Zeno-Specter: Rapid HTTP Security Header Analyzer

if [ -z "$1" ]; then
    echo "Usage: ./zeno_specter.sh <https://target.com>"
    exit 1
fi

TARGET=$1
echo -e "\n============================================="
echo -e "   🕵️ ZENO-SPECTER: HEADER AUDIT"
echo -e "   Target: $TARGET"
echo -e "=============================================\n"

HEADERS=$(curl -s -I -L "$TARGET")

# Array of critical security headers to check
SECURITY_HEADERS=(
    "Strict-Transport-Security"
    "Content-Security-Policy"
    "X-Frame-Options"
    "X-Content-Type-Options"
    "Referrer-Policy"
)

echo "[+] Analyzing HTTP Response..."
echo "$HEADERS" | grep -i "HTTP/"

echo -e "\n[+] Security Header Status:"
for header in "${SECURITY_HEADERS[@]}"; do
    if echo "$HEADERS" | grep -i -q "^$header:"; then
        echo -e "  [PASS] $header is present."
    else
        echo -e "  [FAIL] $header is MISSING! (Potential vulnerability)"
    fi
done

echo -e "\n============================================="
echo -e "   [+] AUDIT COMPLETE"
echo -e "=============================================\n"
