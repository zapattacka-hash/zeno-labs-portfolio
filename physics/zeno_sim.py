import numpy as np

def simulate_zeno_effect(total_time, num_measurements, rabi_frequency):
    """
    Simulates the survival probability of a quantum state under frequent measurement.
    """
    # Time interval between measurements
    dt = total_time / num_measurements
    
    # Unitary time evolution matrix U = exp(-i * H * dt)
    # H = rabi_frequency * sigma_x
    U = np.array([
        [np.cos(rabi_frequency * dt), -1j * np.sin(rabi_frequency * dt)],
        [-1j * np.sin(rabi_frequency * dt), np.cos(rabi_frequency * dt)]
    ], dtype=complex)
    
    survival_probability = 1.0
    
    for _ in range(num_measurements):
        # Initial state |0> (after each measurement collapse)
        psi = np.array([1.0, 0.0], dtype=complex)
        
        # Evolve state for time dt
        psi_evolved = np.matmul(U, psi)
        
        # Calculate probability of projecting back into |0>
        p_0 = np.abs(psi_evolved[0])**2
        
        # Update cumulative survival probability path
        survival_probability *= p_0
        
    return survival_probability

# System Parameters
# Set T to the exact time required for a full unobserved transition to |1> (Pi pulse)
T = np.pi / 2 
Omega = 1.0

print("--- Quantum Zeno Effect Simulation ---")
print(f"Total Time (T) = {T:.4f} (Unobserved probability of survival is 0.0)\n")

# Run simulation for increasing measurement frequencies
frequencies = [1, 5, 20, 100, 1000, 10000]

for N in frequencies:
    P_survive = simulate_zeno_effect(T, N, Omega)
    print(f"Measurements (N={N:<5d}) | Survival Probability: {P_survive:.6f}")
