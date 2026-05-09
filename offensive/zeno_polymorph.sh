#!/bin/bash
# Zeno-Polymorph: Self-Mutating Script

echo -e "\n============================================="
echo -e "   🦠 ZENO-POLYMORPH: HASH MUTATOR"
echo -e "=============================================\n"

# Calculate current hash before mutation
OLD_HASH=$(sha256sum "$0" | awk '{print $1}')
echo "[*] Initial Hash: $OLD_HASH"

# Execute Payload
echo "[+] Executing core payload... (Infiltration complete)"

# Mutation Engine: Append random entropy to the end of the file as a comment
ENTROPY=$(head -c 16 /dev/urandom | xxd -p)
echo "# MUTATION_SIGNATURE: $ENTROPY" >> "$0"

# Calculate new hash after mutation
NEW_HASH=$(sha256sum "$0" | awk '{print $1}')
echo "[*] Mutated Hash: $NEW_HASH"
echo "[+] Script hash successfully altered. AV signature evaded."
