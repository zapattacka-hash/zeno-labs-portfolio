print("=============================================")
print("   🌌 ZENO-FRACTAL: MANDELBROT SET")
print("=============================================\n")

width, height = 80, 40
chars = " .:-=+*#%@" # Density mapping

for y in range(height):
    row = ""
    for x in range(width):
        # Map pixel to complex plane
        c = complex(-2.0 + (x / width) * 3.0, -1.5 + (y / height) * 3.0)
        z = 0j
        iteration = 0
        max_iter = 20
        
        while abs(z) <= 2 and iteration < max_iter:
            z = z*z + c
            iteration += 1
            
        if iteration == max_iter:
            row += "█" # Bounded (Inside the set)
        else:
            # Unbounded (Escaped)
            row += chars[iteration % len(chars)]
    print(row)
