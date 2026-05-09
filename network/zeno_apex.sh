#!/bin/bash
# Zeno-Apex: IP Geolocation and ASN Profiler

if [ -z "$1" ]; then
    echo "Usage: ./zeno_apex.sh <IP_OR_DOMAIN>"
    exit 1
fi

TARGET=$1
echo -e "\n============================================="
echo -e "   🌍 ZENO-APEX: THREAT INTEL TRACKER"
echo -e "   Target: $TARGET"
echo -e "=============================================\n"

# Fetch JSON data from IP-API
DATA=$(curl -s "http://ip-api.com/line/$TARGET?fields=status,message,country,regionName,city,lat,lon,isp,org,as,query")

# Check if the query was successful (first line should be 'success')
STATUS=$(echo "$DATA" | head -n 1)

if [ "$STATUS" != "success" ]; then
    echo "[-] Tracker Failed. Is the target a valid IP/Domain?"
    exit 1
fi

# Parse output (line by line based on the API response structure)
IP=$(echo "$DATA" | sed -n '11p')
COUNTRY=$(echo "$DATA" | sed -n '2p')
REGION=$(echo "$DATA" | sed -n '3p')
CITY=$(echo "$DATA" | sed -n '4p')
LAT=$(echo "$DATA" | sed -n '5p')
LON=$(echo "$DATA" | sed -n '6p')
ISP=$(echo "$DATA" | sed -n '7p')
ORG=$(echo "$DATA" | sed -n '8p')
ASN=$(echo "$DATA" | sed -n '9p')

echo "[+] Resolved IP  : $IP"
echo "[+] Location     : $CITY, $REGION, $COUNTRY"
echo "[+] Coordinates  : $LAT, $LON"
echo "[+] ISP          : $ISP"
echo "[+] Organization : $ORG"
echo "[+] ASN          : $ASN"
echo -e "\n[+] Tracking complete."
