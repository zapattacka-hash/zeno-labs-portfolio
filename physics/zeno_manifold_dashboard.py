import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Apply terminal-friendly dark theme styling
plt.style.use('dark_background')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 14))
fig.suptitle('Quantum System Architecture: Final Telemetry', fontsize=16, y=0.98)

# --- Panel 1: Quantum Zeno Effect ---
N_meas = np.logspace(0, 4, 50)
T_total = np.pi / 2
Omega = 1.0
# Survival probability approximation for large N
P_survive = np.exp(- (Omega * T_total)**2 / N_meas)

ax1.plot(N_meas, P_survive, color='cyan', lw=2)
ax1.set_xscale('log')
ax1.set_title('Measurement-Induced State Arrest')
ax1.set_xlabel('Measurement Frequency (N)')
ax1.set_ylabel('Survival Probability P(t)')
ax1.grid(True, alpha=0.2)
ax1.axhline(1.0, color='red', linestyle='--', alpha=0.5, label='Arrest Limit')
ax1.legend()

# --- Panel 2: LQG Area Spectrum ---
spins = np.arange(0.5, 5.5, 0.5)
gamma = 0.2375
areas = 8 * np.pi * gamma * np.sqrt(spins * (spins + 1))

ax2.step(spins, areas, where='mid', color='magenta', lw=2, marker='o')
ax2.set_title('Topological Discretization (LQG)')
ax2.set_xlabel('Spin Network Edge Representation (j)')
ax2.set_ylabel('Quantized Area ($l_p^2$)')
ax2.grid(True, alpha=0.2)

# --- Panel 3: Unitary Klein Tunneling ---
W_lqg = np.array([2.27, 4.54, 6.82, 9.09, 11.36])
T_unitary = np.ones_like(W_lqg)

ax3.plot(W_lqg, T_unitary, color='lime', lw=2, marker='s', markersize=8)
ax3.set_title('Massless Fermion Unitarity (Klein Regime)')
ax3.set_xlabel('Discrete Barrier Width ($l_p$)')
ax3.set_ylabel('Transmission Probability (T)')
ax3.set_ylim(0.0, 1.2)
ax3.grid(True, alpha=0.2)
ax3.axhline(1.0, color='red', linestyle='--', alpha=0.5)

# Render and Save
plt.tight_layout(pad=3.0)
output_filename = 'quantum_manifold_dashboard.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"--- Visual Compilation Complete ---")
print(f"Dashboard saved locally as: {output_filename}")
