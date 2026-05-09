import hashlib
import sys

def crack_hash(target_hash, hash_type, wordlist_file):
    print(f"[*] Initializing {hash_type.upper()} cracker...")
    print(f"[*] Target Hash: {target_hash}")
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                word = line.strip()
                
                # Hash the current word
                if hash_type.lower() == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type.lower() == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    return "[-] Unsupported hash type."
                
                # Check for collision
                if hashed_word == target_hash:
                    return f"\n[+] CRACKED! \n[+] Hash: {target_hash} \n[+] Plaintext: {word}"
                    
    except FileNotFoundError:
        return f"[-] Error: Wordlist '{wordlist_file}' not found."
        
    return "\n[-] Attack finished. Hash not found in wordlist."

# Generates a quick test wordlist so the script works out of the box
with open("mini_dict.txt", "w") as f:
    f.write("admin\npassword\nzenolabs\nquantum\nhacker\n")

print("=============================================")
print("   ☠️ ZENO-BRUTE: HASH COLLISION ENGINE")
print("=============================================\n")

# MD5 hash for "zenolabs"
target = "d11b33b70e7bd5b867c46927dccab3df" 
print(crack_hash(target, 'md5', 'mini_dict.txt'))
