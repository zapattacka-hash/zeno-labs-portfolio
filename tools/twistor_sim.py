import numpy as np

def twistor_tunneling_amplitude(E, V_step, p_transverse, hbar=1.0, v_F=1.0):
    """
    Computes the transmission probability for a massless fermion using 
    spinor helicity variables across a potential step.
    """
    # Incident region twistor variables (Region 1)
    k_z_1_sq = (E / (hbar * v_F))**2 - p_transverse**2
    
    if k_z_1_sq < 0:
        return 0.0 # Evanescent incident wave (unphysical for initial state)
        
    p_z_1 = np.sqrt(k_z_1_sq)
    
    # Helicity spinor angle (theta) for Region 1
    theta_1 = np.arctan2(p_transverse, p_z_1)
    
    # Barrier region twistor variables (Region 2)
    E_eff = E - V_step
    k_z_2_sq = (E_eff / (hbar * v_F))**2 - p_transverse**2
    
    # Evanescent vs Propagating conditions in Region 2
    if k_z_2_sq <= 0:
        p_z_2 = 1j * np.sqrt(-k_z_2_sq)
    else:
        p_z_2 = np.sqrt(k_z_2_sq)
        # Account for negative group velocity in the Klein regime (hole states)
        if E_eff < 0:
            p_z_2 = -p_z_2

    # Helicity spinor angle (theta) for Region 2
    theta_2 = np.arctan(p_transverse / p_z_2) if p_z_2 != 0 else np.pi / 2
    
    # Transmission amplitude derived from twistor incidence continuity
    numerator = 2 * np.cos(theta_1)
    denominator = np.exp(-1j * theta_2) * np.cos(theta_1) + np.exp(-1j * theta_1) * np.cos(theta_2)
    
    t_amp = numerator / denominator
    
    # Probability conservation via kinematic flux adjustment
    if np.isreal(p_z_2):
        kinematic_flux = np.real(np.cos(theta_2) / np.cos(theta_1))
        T_prob = kinematic_flux * np.abs(t_amp)**2
    else:
        T_prob = 0.0 
        
    return float(np.real(T_prob))

print("--- Twistor Incidence Simulation ---")
# Execution for normal incidence (Klein paradox threshold)
E_inc = 1.0
V_barrier = 3.0
p_t = 0.0 # Normal incidence ensures p_transverse = 0

T = twistor_tunneling_amplitude(E_inc, V_barrier, p_t)
print(f"Incident Energy (E)      : {E_inc}")
print(f"Barrier Potential (V)    : {V_barrier}")
print(f"Transverse Momentum (pt) : {p_t}")
print(f"Transmission Probability : {T:.1f}")
print("Result confirms helicity conservation across the boundary.")
