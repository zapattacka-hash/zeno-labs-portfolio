import numpy as np

def simulate_continuous_watcher(gamma, dt, steps, Omega):
    """
    Integrates the Lindblad master equation for a continuously observed two-level system.
    """
    # Initialize pure state |0><0|
    rho = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    
    # Hamiltonian (Sigma_x) driving the transition
    H = Omega * np.array([[0, 1], [1, 0]], dtype=complex)
    
    # Measurement operator (Sigma_z)
    L = np.array([[1, 0], [0, -1]], dtype=complex)
    L_dagger = np.conjugate(L).T
    
    survival_history = []
    
    for _ in range(steps):
        survival_history.append(np.real(rho[0, 0]))
        
        # Commutator: -i[H, rho]
        comm = np.matmul(H, rho) - np.matmul(rho, H)
        
        # Dissipator: L rho L^dag - 0.5 * {L^dag L, rho}
        term1 = np.matmul(L, np.matmul(rho, L_dagger))
        term2 = 0.5 * np.matmul(L_dagger, np.matmul(L, rho))
        term3 = 0.5 * np.matmul(rho, np.matmul(L_dagger, L))
        dissipator = gamma * (term1 - term2 - term3)
        
        # Euler integration step
        drho_dt = -1j * comm + dissipator
        rho = rho + drho_dt * dt
        
        # Enforce trace=1 to correct floating point drift
        rho /= np.trace(rho)
        
    return survival_history

# System Parameters
Omega = 1.0          # Base transition frequency
dt = 0.01            # Time step
time_vector = np.arange(0, 5, dt)
steps = len(time_vector)

print("--- Continuous Watcher Daemon Initialized ---\n")

# Scenario 1: Weak Measurement (Low gamma)
gamma_weak = 0.1
history_weak = simulate_continuous_watcher(gamma_weak, dt, steps, Omega)
print(f"[Weak Watcher]  Final State |0> Population: {history_weak[-1]:.6f}")

# Scenario 2: Strong Measurement (High gamma)
gamma_strong = 50.0
history_strong = simulate_continuous_watcher(gamma_strong, dt, steps, Omega)
print(f"[Strong Watcher] Final State |0> Population: {history_strong[-1]:.6f}\n")

print("System state successfully localized under continuous observation.")
