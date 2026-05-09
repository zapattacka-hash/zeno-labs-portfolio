import math

def calculate_wormhole_distance(r_throat, r_ship):
    """
    Calculates the proper distance l(r) from the throat of the wormhole
    to a coordinate radius r, using the Schwarzschild metric.
    """
    if r_ship < r_throat:
        return "Error: Ship cannot be inside the throat radius."
        
    # Proper distance integral solution for Flamm Paraboloid
    part1 = math.sqrt(r_ship * (r_ship - r_throat))
    part2 = r_throat * math.log(math.sqrt(r_ship / r_throat) + math.sqrt((r_ship / r_throat) - 1))
    
    distance = part1 + part2
    return distance

print("=============================================")
print("   🌌 ZENO-WORMHOLE: EINSTEIN-ROSEN METRIC")
print("=============================================\n")

throat_radius = 10.0  # Schwarzschild radius (Event Horizon)
ship_radii = [10.1, 15.0, 50.0, 100.0]

print(f"[*] Wormhole Throat Radius (rs): {throat_radius} km\n")
print(f"{'Ship Coord Radius (r)':<25} | {'Proper Distance to Throat (l)':<25}")
print("-" * 55)

for r in ship_radii:
    dist = calculate_wormhole_distance(throat_radius, r)
    print(f"{r:<25.1f} | {dist:<25.4f}")
