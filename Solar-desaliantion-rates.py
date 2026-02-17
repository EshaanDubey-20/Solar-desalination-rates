# Thermal Desalination Simulation 


import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


#  1: Generate CSV

areas = [0.05, 0.1, 0.15, 0.2]           # Basin areas in m²
angles = [10, 15, 20, 25, 30, 35, 40, 45]  # Cover angles in degrees
time_hours = np.arange(0.5, 5.5, 0.5)     # Time intervals 0.5 → 5 hours
temp_water = 30
temp_ambient = 25

csv_filename = 'solar_still_data_full.csv'
with open(csv_filename, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['BasinArea','CoverAngle','TempWater','TempAmbient','Time_hr'])
    for area in areas:
        for angle in angles:
            for t in time_hours:
                writer.writerow([area, angle, temp_water, temp_ambient, t])

print(f"✅ CSV '{csv_filename}' created.")


# 2: Constants

L_v = 2.26e6
I = 800
eta_base = 0.7
k_loss = 50


# 3: Evaporation function

def evaporation_rate(area, angle, temp_water, temp_ambient, time_hr, eta=eta_base):
    eta_angle = eta * (1 - 0.002*(angle - 30)**2)
    Q_in = I * area * eta_angle * time_hr * 3600
    Q_loss = k_loss * (temp_water - temp_ambient) * time_hr * 3600
    m_evap = max((Q_in - Q_loss) / L_v, 0)
    return m_evap


# 4: Calculate yields

data = []

for area in areas:
    for angle in angles:
        for t in time_hours:
            yield_l = evaporation_rate(area, angle, temp_water, temp_ambient, t)
            data.append([area, angle, temp_water, temp_ambient, t, yield_l])

#5: Save results CSV
output_csv = 'solar_desalination_results.csv'
with open(output_csv, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['BasinArea','CoverAngle','TempWater','TempAmbient','Time_hr','Yield_L'])
    writer.writerows(data)

print(f"✅ Simulation results saved as '{output_csv}'")


#Heatmap for 3-hour yield

yield_matrix = np.zeros((len(angles), len(areas)))

for i, angle in enumerate(angles):
    for j, area in enumerate(areas):
        for row in data:
            if row[0]==area and row[1]==angle and row[4]==3:
                yield_matrix[i,j] = row[5]
                break

plt.figure(figsize=(8,6))
sns.heatmap(
    yield_matrix,
    xticklabels=np.round(areas,2),
    yticklabels=np.round(angles,0),
    annot=True,
    cmap="YlGnBu",
    cbar_kws={'label': 'Evaporation Yield (kg ~ L)'}
)
plt.xlabel("Basin Area (m²)")
plt.ylabel("Cover Angle (°)")
plt.title("Predicted 3-Hour Yield Heatmap")
plt.show()


# 6: Yield vs Time curves

plt.figure(figsize=(8,6))

plot_angles = [angles[0], angles[len(angles)//2], angles[-1]]
plot_areas = [areas[0], areas[-1]]

for angle in plot_angles:
    for area in plot_areas:
        yvals = [row[5] for row in data if row[0]==area and row[1]==angle]
        plt.plot(time_hours, yvals, marker='o', label=f"Area={area:.2f}m², Angle={angle:.0f}°")

plt.xlabel("Time (hours)")
plt.ylabel("Evaporated Water (kg ~ L)")
plt.title("Predicted Evaporation vs Time")
plt.grid(True)
plt.legend()
plt.show()

max_yield = 0
best_angle = 0
best_area = 0

for i, angle in enumerate(angles):
    for j, area in enumerate(areas):
        if yield_matrix[i,j] > max_yield:
            max_yield = yield_matrix[i,j]
            best_angle = angle
            best_area = area

print(f"✅ Optimal Cover Angle: {best_angle}°, Optimal Basin Area: {best_area} m², Predicted 3-hr Yield: {max_yield:.3f} kg (~L)")

