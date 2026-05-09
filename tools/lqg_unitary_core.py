import numpy as np

def unitary_wave_params(E, V, m, v_F, hbar):
    epsilon = E - V
    if abs(epsilon) > m * v_F**2:
        k = np.sqrt(epsilon**2 - (m * v_F**2)**2) / (hbar * v_F)
        # Sign inversion for hole-state group velocity
        if epsilon < 0:
            k = -k
        z = (hbar * v_F * k) / (epsilon + m * v_F**2)
    else:
        kappa = np.sqrt((m * v_F**2)**2 - epsilon**2) / (hbar * v_F)
        k = 1j * kappa
        z = (1j * hbar * v_F * kappa) / (epsilon + m * v_F**2)
    return k, z

def compute_W(k, z, x):
    return np.array([
        [np.exp(1j * k * x), np.exp(-1j * k * x)],
        [z * np.exp(1j * k * x), - (1/z) * np.exp(-1j * k * x)]
    ], dtype=complex)

def calculate_unitary_transmission(E, V_barrier, width, m, v_F, hbar):
    V_array = [0.0, V_barrier, 0.0]
    x_array = [0.0, width]
    
    M_global = np.identity(2, dtype=complex)
    
    for j in range(2):
        k_j, z_j = unitary_wave_params(E, V_array[j], m, v_F, hbar)
        k_next, z_next = unitary_wave_params(E, V_array[j+1], m, v_F, hbar)
        
        W_j = compute_W(k_j, z_j, x_array[j])
        W_next = compute_W(k_next, z_next, x_array[j])
        
        W_j_inv = np.linalg.inv(W_j)
        T_j = np.matmul(W_j_inv, W_next)
        M_global = np.matmul(M_global, T_j)

    t = 1.0 / M_global[0, 0]
    
    _, z_0 = unitary_wave_params(E, V_array[0], m, v_F, hbar)
    _, z_f = unitary_wave_params(E, V_array[-1], m, v_F, hbar)
    
    # Strict probability current ratio
    J_inc = np.real(z_0)
    J_trans = np.real(z_f)
    
    if J_inc == 0 or J_trans == 0:
        return 0.0
        
    T_prob = np.abs(J_trans / J_inc) * np.abs(t)**2
    return float(np.clip(T_prob, 0.0, 1.0))

# Execute Unitarity Check for LQG Boundaries
E_inc = 0.5
V_bar = 0.8
m_part = 0.1
test_widths = [2.273616, 4.547231, 6.820847]

print("--- Unitary Resolved LQG Tunneling ---")
print(f"{'W_LQG':<15} | {'T (Unitary)':<20}")
print("-" * 38)

for w_lqg in test_widths:
    T_unit = calculate_unitary_transmission(E_inc, V_bar, w_lqg, m_part, 1.0, 1.0)
    print(f"{w_lqg:<15.6f} | {T_unit:<20.6f}")
