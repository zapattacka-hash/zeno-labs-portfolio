import numpy as np

def wave_params(E, V, m, v_F, hbar):
    epsilon = E - V
    if abs(epsilon) > m * v_F**2:
        k = np.sqrt(epsilon**2 - (m * v_F**2)**2) / (hbar * v_F)
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

def calculate_transmission(E, V_barrier, width, m, v_F, hbar):
    # Free space -> Barrier -> Free space
    V_array = [0.0, V_barrier, 0.0]
    x_array = [0.0, width]
    
    M_global = np.identity(2, dtype=complex)
    
    for j in range(2):
        k_j, z_j = wave_params(E, V_array[j], m, v_F, hbar)
        k_next, z_next = wave_params(E, V_array[j+1], m, v_F, hbar)
        
        W_j = compute_W(k_j, z_j, x_array[j])
        W_next = compute_W(k_next, z_next, x_array[j])
        
        W_j_inv = np.linalg.inv(W_j)
        T_j = np.matmul(W_j_inv, W_next)
        M_global = np.matmul(M_global, T_j)

    t = 1.0 / M_global[0, 0]
    
    k_0, _ = wave_params(E, V_array[0], m, v_F, hbar)
    k_f, _ = wave_params(E, V_array[-1], m, v_F, hbar)
    eps_0 = E - V_array[0]
    eps_f = E - V_array[-1]
    
    if np.iscomplex(k_f):
        return 0.0
        
    kin_factor = (k_f / k_0) * ((eps_0 + m * v_F**2) / (eps_f + m * v_F**2))
    return float(np.real(kin_factor * np.abs(t)**2))

def get_lqg_width(w_continuum, gamma=0.2375):
    A_min = 8 * np.pi * gamma * np.sqrt(0.5 * 1.5)
    L_min = np.sqrt(A_min)
    N = np.ceil(w_continuum / L_min)
    return N * L_min

# System Parameters
E_inc = 0.5
V_bar = 0.8
m_part = 0.1
v_fermi = 1.0
hbar = 1.0

test_widths = [1.0, 2.0, 3.0, 4.0, 5.0]

print("--- Continuum vs LQG Discretized Spinor Tunneling ---")
print(f"E_inc={E_inc}, V_barrier={V_bar}, m={m_part}\n")
print(f"{'W_continuum':<15} | {'T (Continuum)':<20} | {'W_LQG':<15} | {'T (LQG)':<20}")
print("-" * 75)

for w_c in test_widths:
    T_cont = calculate_transmission(E_inc, V_bar, w_c, m_part, v_fermi, hbar)
    
    w_lqg = get_lqg_width(w_c)
    T_lqg = calculate_transmission(E_inc, V_bar, w_lqg, m_part, v_fermi, hbar)
    
    print(f"{w_c:<15.2f} | {T_cont:<20.6f} | {w_lqg:<15.6f} | {T_lqg:<20.6f}")
