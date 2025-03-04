import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate heart rate and skin temperature data
np.random.seed(42)
hr_data = np.random.normal(75, 5, 1000)  # Normal heart rate data
temp_data = np.random.normal(36.5, 0.5, 1000)  # Normal skin temperature data

# Simulate alcohol consumption event (change in heart rate and temperature)
hr_data[500:505] = [90, 95, 85, 100, 110]  # Heart rate increase after alcohol
temp_data[500:505] = [37.2, 37.5, 37.3, 37.4, 37.6]  # Skin temperature rise after alcohol

# Plot heart rate and temperature
plt.figure(figsize=(10, 5))

# Heart Rate Plot
plt.subplot(2, 1, 1)
plt.plot(hr_data, label='Heart Rate')
plt.title('Heart Rate with Alcohol-Induced Changes')
plt.xlabel('Time')
plt.ylabel('Heart Rate (bpm)')

# Skin Temperature Plot
plt.subplot(2, 1, 2)
plt.plot(temp_data, label='Skin Temperature', color='red')
plt.title('Skin Temperature with Alcohol-Induced Changes')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')

plt.tight_layout()
plt.show()

# Output changes post-alcohol consumption
print("Heart Rate and Skin Temperature change after alcohol consumption (Index 500-505):")
for i in range(500, 505):
    print(f"Index {i}: HR = {hr_data[i]} bpm, Temp = {temp_data[i]}°C")
