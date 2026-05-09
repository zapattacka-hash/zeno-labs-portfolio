import numpy as np

def spinor_transfer_matrix(E, V_array, x_array, m, v_F, hbar):
    num_regions = len(V_array)
    M_global = np.identity(2, dtype=complex)
    
    def wave_params(V):
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

    for j in range(num_regions - 1):
        k_j, z_j = wave_params(V_array[j])
        k_next, z_next = wave_params(V_array[j+1])
        
        W_j = compute_W(k_j, z_j, x_array[j])
        W_next = compute_W(k_next, z_next, x_array[j])
        
        W_j_inv = np.linalg.inv(W_j)
        T_j = np.matmul(W_j_inv, W_next)
        
        M_global = np.matmul(M_global, T_j)

    M11 = M_global[0, 0]
    t = 1.0 / M11
    
    k_0, _ = wave_params(V_array[0])
    k_f, _ = wave_params(V_array[-1])
    
    eps_0 = E - V_array[0]
    eps_f = E - V_array[-1]
    
    kinematic_factor = (k_f / k_0) * ((eps_0 + m * v_F**2) / (eps_f + m * v_F**2))
    
    if np.iscomplex(k_f):
        return 0.0
        
    T_prob = np.real(kinematic_factor * np.abs(t)**2)
    return T_prob

# Test Parameters
E_incident = 0.5
V_landscape = [0, 1.0, 0]
x_boundaries = [0, 5]
m_particle = 0.1
v_fermi = 1.0
h_bar = 1.0

# Run the simulation
probability = spinor_transfer_matrix(E_incident, V_landscape, x_boundaries, m_particle, v_fermi, h_bar)
print(f"Tunneling Probability (T): {probability}")
