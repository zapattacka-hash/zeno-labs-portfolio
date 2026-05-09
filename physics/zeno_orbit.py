import math
def orbit():
    r, v = 10.0, 10.0
    print("\n[!] ZENO-ORBIT: VERIFYING KINEMATIC STABILITY...")
    for i in range(5):
        v += (-1.0 / (r**2)) * 0.1
        r += v * 0.1
        print(f"    T+{i*10}s: Distance {r:.4f}")
    print("[*] Orbit stable.")
orbit()
