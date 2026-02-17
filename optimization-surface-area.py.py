import numpy as np
import matplotlib.pyplot as plt


# Constants

L_v = 2.26e6        # latent heat (J/kg)
I = 800             # solar intensity (W/m²)
eta_base = 0.7      # base efficiency
k_loss = 3       # heat loss coefficient

temp_water = 30     # °C
temp_ambient = 25   # °C
time_test = 3       # hours


# Evaporation Function

def evaporation_rate(area, angle, temp_water, temp_ambient, time_hr):
    # Angle efficiency (parabolic)
    eta_angle = eta_base * (1 - 0.002 * (angle - 30)**2)
    eta_angle = max(eta_angle, 0)  # prevent negative efficiency

    Q_in = I * area * eta_angle * time_hr * 3600
    Q_loss = k_loss * (temp_water - temp_ambient) * time_hr * 3600

    net_heat = max(Q_in - Q_loss, 0)
    return net_heat / L_v  # kg ≈ liters


# Dual Optimization
# Area: 0.02–0.05 m²
# Angle: 10–89.9°


area_range = np.linspace(0.02, 0.05, 40)
angle_range = np.linspace(10, 89.9, 80)

max_yield = -1
best_area = None
best_angle = None

for area in area_range:
    for angle in angle_range:
        y = evaporation_rate(area, angle, temp_water, temp_ambient, time_test)

        if y > max_yield:
            max_yield = y
            best_area = area
            best_angle = angle


# Results

print("\n🔍 OPTIMIZATION RESULTS")
print(f"Best Surface Area: {best_area:.4f} m²")
print(f"Best Cover Angle: {best_angle:.2f}°")
print(f"Maximum Yield: {max_yield:.5f} L")


# Plot Area vs Yield

area_yields = [
    evaporation_rate(a, best_angle, temp_water, temp_ambient, time_test)
    for a in area_range
]

plt.figure(figsize=(7,5))
plt.plot(area_range, area_yields, marker='o')
plt.scatter(best_area, max_yield)

plt.xlabel("Surface Area (m²)")
plt.ylabel("Freshwater Yield (L)")
plt.title(f"Yield vs Area at Optimal Angle ({best_angle:.1f}°)")
plt.grid(True)

plt.annotate(
    f"Best ≈ {best_area:.3f} m²",
    (best_area, max_yield),
    xytext=(best_area + 0.002, max_yield * 0.9),
    arrowprops=dict(arrowstyle="->")
)

plt.show()
