import math

def particle_in_box(n, box_length=1.0, points=50):
    """Calculates and plots the probability density of a 1D quantum state."""
    print(f"\n--- Quantum State: n = {n} (Energy Level) ---")
    print("Probability Density |Psi(x)|^2 across the Box:")
    
    max_prob = 2.0 / box_length # Maximum possible amplitude for normalization
    
    for i in range(points + 1):
        x = (i / points) * box_length
        # Psi(x) = sqrt(2/L) * sin(n * pi * x / L)
        # Probability = |Psi(x)|^2
        prob_density = (2.0 / box_length) * (math.sin(n * math.pi * x / box_length))**2
        
        # Scale to terminal width (max 40 hashes)
        bar_length = int((prob_density / max_prob) * 40)
        bar = "█" * bar_length
        
        print(f"x={x:.2f} | {bar}")

print("=============================================")
print("   ⚛️ ZENO-SCHRODINGER: PROBABILITY RENDERER")
print("=============================================")
# Render Ground State (n=1) and First Excited State (n=2)
particle_in_box(n=1)
particle_in_box(n=2)
