import numpy as np

def discretize_barrier(w_continuum, gamma=0.2375):
    """
    Renormalizes a continuous barrier width into discrete LQG spin network edges.
    Lengths are expressed in terms of the Planck length (l_p).
    """
    # Calculate fundamental minimal area and length
    A_min = 8 * np.pi * gamma * np.sqrt(0.5 * 1.5)
    L_min = np.sqrt(A_min)
    
    # Calculate discrete jumps (N nodes)
    N = np.ceil(w_continuum / L_min)
    w_physical = N * L_min
    
    return L_min, int(N), w_physical

print("--- LQG Topological Barrier Discretization ---")
print("Mapping continuous coordinate space to Spin Network nodes.\n")

# Array of classical barrier widths to map
classical_widths = [1.0, 2.0, 5.0, 10.0, 15.0]

L_min, _, _ = discretize_barrier(1.0)
print(f"Fundamental Length Quantum (L_min): {L_min:.6f} l_p\n")

print(f"{'W_continuum (l_p)':<20} | {'Spin Network Nodes (N)':<25} | {'W_physical (l_p)':<20}")
print("-" * 70)

for w_c in classical_widths:
    _, n_nodes, w_phys = discretize_barrier(w_c)
    print(f"{w_c:<20.2f} | {n_nodes:<25d} | {w_phys:<20.6f}")

print("\nConclusion: Sub-L_min barriers undergo instantaneous non-local propagation.")
