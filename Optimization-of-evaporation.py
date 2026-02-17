     import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Physics Constants
# ===============================
g = 9.81           # gravity (m/s^2)
rho = 1.225        # air density (kg/m^3)
Cd = 0.47          # drag coefficient (sphere)
A = 0.01           # cross-sectional area (m^2)
m = 0.145          # mass (kg) - cricket ball
v0 = 30            # initial velocity (m/s)
dt = 0.01          # timestep

# ===============================
# Projectile Simulator
# ===============================
def simulate_range(angle_deg):
    angle = np.radians(angle_deg)

    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)

    x, y = 0, 0

    while y >= 0:
        v = np.sqrt(vx**2 + vy**2)

        # Drag force
        Fd = 0.5 * rho * Cd * A * v**2
        ax = -Fd * vx / (m * v)
        ay = -g - (Fd * vy / (m * v))

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

    return x  # horizontal range


# ===============================
# Optimization Algorithm
# ===============================
angles = np.linspace(1, 89.9, 200)  # avoid 0 and 90
ranges = []

for a in angles:
    r = simulate_range(a)
    ranges.append(r)

ranges = np.array(ranges)

# Find optimal angle
best_index = np.argmax(ranges)
best_angle = angles[best_index]
best_range = ranges[best_index]

print("Optimal Angle:", round(best_angle, 2), "degrees")
print("Maximum Range:", round(best_range, 2), "meters")

# ===============================
# Plot Range vs Angle
# ===============================
plt.figure(figsize=(8,5))
plt.plot(angles, ranges, linewidth=2)
plt.scatter(best_angle, best_range)  # highlight optimum

plt.title("Range vs Launch Angle (With Air Resistance)")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid(True)

# Annotate best point
plt.annotate(
    f"Best ≈ {best_angle:.1f}°",
    (best_angle, best_range),
    xytext=(best_angle+5, best_range-5),
    arrowprops=dict(arrowstyle="->")
)

plt.show()
