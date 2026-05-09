import numpy as np

def lorenz_system(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """Calculates the spatial derivatives for the Lorenz Attractor."""
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def integrate_lorenz(state_0, dt=0.01, steps=1000):
    """Uses Euler integration to step the system forward in time."""
    x, y, z = state_0
    trajectory = []
    
    for _ in range(steps):
        dx, dy, dz = lorenz_system(x, y, z)
        x += dx * dt
        y += dy * dt
        z += dz * dt
        trajectory.append((x, y, z))
    
    return trajectory

print("=============================================")
print("   🌪️ ZENO-CHAOS: LORENZ DIVERGENCE ENGINE")
print("=============================================")

# Define two initial states with a 0.0001 microscopic difference
state_A = (1.0, 1.0, 1.0)
state_B = (1.0, 1.0, 1.0001)

print(f"[*] Initial State A : {state_A}")
print(f"[*] Initial State B : {state_B}")
print("[*] Running numerical integration (1000 steps)...\n")

traj_A = integrate_lorenz(state_A)
traj_B = integrate_lorenz(state_B)

print(f"{'Step':<10} | {'Distance Between States (Divergence)':<40}")
print("-" * 55)

# Sample the divergence at specific intervals to show the Butterfly Effect
for step in [10, 100, 500, 999]:
    xA, yA, zA = traj_A[step]
    xB, yB, zB = traj_B[step]
    
    # Calculate Euclidean distance between the two systems
    distance = np.sqrt((xA - xB)**2 + (yA - yB)**2 + (zA - zB)**2)
    print(f"{step:<10} | {distance:<40.6f}")

print("\nConclusion: Microscopic variations yield macroscopic chaos.")
