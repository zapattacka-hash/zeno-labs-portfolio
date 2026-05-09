import numpy as np

def von_neumann_entropy(rho):
    """Calculates the Von Neumann entropy of a density matrix."""
    # Find eigenvalues
    eigenvalues = np.linalg.eigvalsh(rho)
    # Filter out zero eigenvalues to avoid log2(0)
    eigenvalues = eigenvalues[eigenvalues > 1e-10]
    # S = -Tr(rho * log2(rho))
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    return np.abs(entropy) # Absolute value to clean up -0.0

print("--- Zeno Labs: Quantum Entanglement & Entropy ---")

# 1. Define the maximally entangled Bell State |Phi+> = (|00> + |11>) / sqrt(2)
state_00 = np.array([1, 0, 0, 0])
state_11 = np.array([0, 0, 0, 1])
bell_state = (state_00 + state_11) / np.sqrt(2)

# 2. Global Density Matrix (rho_AB)
rho_AB = np.outer(bell_state, bell_state.conj())
global_entropy = von_neumann_entropy(rho_AB)

print(f"Global System Entropy (S_AB) : {global_entropy:.2f} bits (Pure State)")

# 3. Partial Trace to find Reduced Density Matrix of Subsystem A (rho_A)
# Tracing out qubit B from a 4x4 matrix yields a 2x2 matrix
rho_A = np.array([
    [rho_AB[0,0] + rho_AB[1,1], rho_AB[0,2] + rho_AB[1,3]],
    [rho_AB[2,0] + rho_AB[3,1], rho_AB[2,2] + rho_AB[3,3]]
])

local_entropy = von_neumann_entropy(rho_A)

print(f"Local Subsystem Entropy (S_A): {local_entropy:.2f} bits (Maximally Mixed)")
print("\nConclusion: Subsystem state is completely undefined until measured. Spooky action verified.")
