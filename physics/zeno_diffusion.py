print("=============================================")
print("   🔥 ZENO-DIFFUSION: THERMAL DYNAMICS")
print("=============================================\n")

# Simulation parameters
length = 40
time_steps = 50
alpha = 0.4  # Thermal diffusivity
u = [0.0] * length

# Inject a thermal spike in the center
u[length // 2] = 100.0

print("Initial State:")
print("".join(["█" if val > 10 else "." for val in u]))

for t in range(time_steps):
    u_new = u.copy()
    
    # Apply 1D heat equation via finite differences
    for i in range(1, length - 1):
        u_new[i] = u[i] + alpha * (u[i+1] - 2*u[i] + u[i-1])
        
    u = u_new
    
    # Print telemetry every 10 steps
    if (t + 1) % 10 == 0:
        print(f"\nStep {t + 1}:")
        # Visual representation mapping temp to ASCII
        vis = []
        for val in u:
            if val > 50: vis.append("█")
            elif val > 20: vis.append("▓")
            elif val > 5: vis.append("▒")
            elif val > 1: vis.append("░")
            else: vis.append(".")
        print("".join(vis))
        
print("\n[+] Entropy increases; equilibrium approaches.")
