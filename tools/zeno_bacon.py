print("=============================================")
print("   🥓 ZENO-BACON: TYPOGRAPHICAL STEGO")
print("=============================================\n")

# A = lowercase (0), B = uppercase (1)
def encode_bacon(secret_bin, cover_text):
    cover_text = cover_text.replace(" ", "").lower()
    if len(secret_bin) > len(cover_text):
        return "Error: Cover text too short for secret."
        
    stego_text = ""
    for i in range(len(secret_bin)):
        if secret_bin[i] == '1':
            stego_text += cover_text[i].upper()
        else:
            stego_text += cover_text[i].lower()
            
    # Append the rest of the un-encoded cover text
    stego_text += cover_text[len(secret_bin):]
    return stego_text

# Secret data: 10110 (could be ASCII bits)
secret = "10110"
cover = "This is a completely normal sentence."

print(f"[*] Secret Binary : {secret}")
print(f"[*] Cover Text    : {cover}\n")

encoded = encode_bacon(secret, cover)

print(f"[+] Encoded Stego : {encoded}")
print("\n[+] Observe the capitalization. That is the payload.")
