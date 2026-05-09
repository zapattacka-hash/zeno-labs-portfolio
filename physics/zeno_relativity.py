import sys
import math

# Speed of light in m/s
c = 299792458.0

def calculate_dilation(velocity_percent_c, stationary_years):
    v = (velocity_percent_c / 100.0) * c
    
    if v >= c:
        return "Error: Velocity must be strictly less than c."
        
    # Lorentz Factor: gamma = 1 / sqrt(1 - v^2/c^2)
    gamma = 1.0 / math.sqrt(1 - (v**2 / c**2))
    
    # Delta t' = Delta t / gamma
    traveler_years = stationary_years / gamma
    return gamma, traveler_years

print("=============================================")
print("   ⏱️ ZENO-RELATIVITY: TIME DILATION")
print("=============================================\n")

test_speeds = [10, 50, 90, 99, 99.9, 99.99]
observer_time = 10.0 # 10 years passed on Earth

print(f"Stationary Observer Time: {observer_time} Years\n")
print(f"{'% of c':<10} | {'Lorentz Factor (gamma)':<25} | {'Traveler Time (Years)':<20}")
print("-" * 60)

for speed in test_speeds:
    gamma, t_time = calculate_dilation(speed, observer_time)
    print(f"{speed:<10} | {gamma:<25.6f} | {t_time:<20.6f}")

print("\n[+] Near c, observer time diverges infinitely from local time.")
