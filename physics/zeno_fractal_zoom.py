import math

def render_zoom(width, height, centerX, centerY, zoom):
    chars = " .:-=+*#%@"
    for y in range(height):
        row = ""
        for x in range(width):
            # Scale coordinates based on zoom level
            zx = (x - width / 2.0) * 4.0 / (width * zoom) + centerX
            zy = (y - height / 2.0) * 4.0 / (width * zoom) + centerY
            c = complex(zx, zy)
            z = 0j
            iteration = 0
            while abs(z) <= 2 and iteration < 25:
                z = z*z + c
                iteration += 1
            if iteration == 25:
                row += "█"
            else:
                row += chars[iteration % len(chars)]
        print(row)

print("=============================================")
print("   🌌 ZENO-FRACTAL: SEAHORSE VALLEY ZOOM")
print("=============================================\n")

# Zooming into a specific high-detail coordinate
render_zoom(80, 40, -0.748, 0.1, 10.0)
