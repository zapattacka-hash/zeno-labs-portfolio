import math

def simulate():
    # Tunneling Parameters
    V, E = 10.0, 2.0  # eV
    width_angstroms = 2.0
    nodes = 20  # Discrete LQG nodes
    
    # Calculate Attenuation (kappa)
    # kappa = sqrt(2m(V-E))/hbar
    kappa = 0.512 * math.sqrt(V - E) # Simplified coefficient
    
    print(f"--- LQG Tunneling Profile (V={V}eV, E={E}eV) ---")
    print(f"Node | Amplitude | Visualization")
    print("-" * 40)
    
    for i in range(nodes + 1):
        x = (width_angstroms / nodes) * i
        # Exponential decay: psi = exp(-kappa * x)
        amplitude = math.exp(-kappa * x)
        bar = "|" * int(amplitude * 30)
        print(f"{i:4} | {amplitude:.4f}    | {bar}")

if __name__ == "__main__":
    simulate()
