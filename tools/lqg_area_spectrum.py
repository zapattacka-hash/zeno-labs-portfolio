import numpy as np

def calculate_lqg_area_spectrum(max_spin, gamma=0.2375):
    """
    Computes the quantized area eigenvalues for an LQG spin network.
    Returns area in units of the Planck area (l_p^2).
    """
    spins = np.arange(0.5, max_spin + 0.5, 0.5)
    
    # Area operator eigenvalue formula: A = 8 * pi * gamma * sqrt(j * (j + 1))
    areas = 8 * np.pi * gamma * np.sqrt(spins * (spins + 1))
    
    return spins, areas

print("--- LQG Spin Network: Quantized Area Spectrum ---")
print("Units: Planck Area (l_p^2)\n")
print(f"{'Spin (j)':<10} | {'Eigenvalue (Area)':<20} | {'Delta (Jump)':<20}")
print("-" * 55)

max_j = 5.0
spins, areas = calculate_lqg_area_spectrum(max_j)

previous_area = 0.0
for j, area in zip(spins, areas):
    delta = area - previous_area
    print(f"{j:<10.1f} | {area:<20.6f} | {delta:<20.6f}")
    previous_area = area

print("\nNotice the Delta decreases asymptotically. Spacetime becomes quasi-continuous at higher spins.")
