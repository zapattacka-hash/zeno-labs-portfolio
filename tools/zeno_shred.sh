#!/bin/bash
# Zeno-Shred: Secure Data Destruction

if [ -z "$1" ]; then
    echo "Usage: ./zeno_shred.sh <file_to_destroy>"
    exit 1
fi

TARGET=$1

if [ ! -f "$TARGET" ]; then
    echo "[-] File not found."
    exit 1
fi

SIZE=$(wc -c < "$TARGET")

echo -e "\n============================================="
echo -e "   ☢️ ZENO-SHRED: OPSEC FILE ERASURE"
echo -e "=============================================\n"

echo "[*] Target: $TARGET ($SIZE bytes)"

for pass in {1..3}; do
    echo "[*] Pass $pass/3: Overwriting with /dev/urandom..."
    dd if=/dev/urandom of="$TARGET" bs=1 count="$SIZE" conv=notrunc status=none
done

echo "[*] Unlinking inode..."
rm -f "$TARGET"

echo "[+] Target eradicated."
