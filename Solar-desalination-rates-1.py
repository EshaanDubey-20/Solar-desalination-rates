import numpy as np
import matplotlib.pyplot as plt


# SETTINGS

area = 0.15
angles = [10, 25, 30, 45, 60, 75, 89.9]
time_hours = np.arange(0.5, 5.5, 0.5)

temp_water = 40
temp_ambient = 25


# CONSTANTS

L_v = 2.26e6
I = 900
eta_base = 0.65
k_loss = 3


# MODEL

def evap(angle, t):
    eta_angle = eta_base * (1 - 0.0012*(angle - 30)**2)
    Q_in = I * area * eta_angle * t * 3600
    Q_loss = k_loss * (temp_water - temp_ambient) * t * 3600
    m = (Q_in - Q_loss) / L_v
    return max(m, 1e-6)  # avoid log(0)


# FIND OPTIMAL ANGLE

total_yield = []
for angle in angles:
    total = sum(evap(angle, t) for t in time_hours)
    total_yield.append(total)

optimal_angle = angles[np.argmax(total_yield)]
print(f"✅ Optimal angle detected: {optimal_angle}°")


# GRAPH 1 — TIME CURVES + OPTIMAL MARK

plt.figure(figsize=(9,6))

for angle in angles:
    yields = [evap(angle, t) for t in time_hours]
    if angle == optimal_angle:
        plt.plot(time_hours, yields, linewidth=3.5, label=f"{angle}° (Optimal)")
    else:
        plt.plot(time_hours, yields, linewidth=2, alpha=0.7, label=f"{angle}°")

plt.title("Solar Still Output vs Time (Log Scale)")
plt.xlabel("Time (hours)")
plt.ylabel("Evaporated Water (kg ≈ L)")
plt.grid(True)
plt.yscale("log")
plt.legend(title="Cover Angle", ncol=2)
plt.tight_layout()
plt.show()




