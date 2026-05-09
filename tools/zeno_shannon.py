import math
from collections import Counter

def calculate_entropy(data):
    """Calculates the Shannon Entropy of a string in bits."""
    if not data:
        return 0
    
    entropy = 0
    length = len(data)
    frequencies = Counter(data)
    
    for freq in frequencies.values():
        probability = freq / length
        # H = - Sum (p * log2(p))
        entropy -= probability * math.log2(probability)
        
    return entropy

print("=============================================")
print("   📊 ZENO-SHANNON: BIT ENTROPY ANALYZER")
print("=============================================\n")

passwords = [
    "password123",
    "correcthorsebatterystaple",
    "Z3n0!L@b$2026",
    "a" * 20 # Length isn't everything
]

print(f"{'Password String':<30} | {'Shannon Entropy (Bits)'}")
print("-" * 55)

for pwd in passwords:
    ent = calculate_entropy(pwd)
    print(f"{pwd:<30} | {ent:.4f}")
    
print("\n[+] Note: Repeated characters yield zero additional entropy.")
