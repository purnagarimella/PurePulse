import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate heart rate data
np.random.seed(42)
hr_data = np.random.normal(75, 5, 1000)  # Normal heart rate data

# Simulate HRV (high HRV could represent relaxation, low HRV represents stress)
hrv_data = np.random.normal(60, 10, 1000)  # HRV data (measured in ms)

# Simulate stress event (heart rate increase and HRV decrease)
hr_data[500:505] = [90, 95, 85, 90, 92]  # Heart rate increase during stress
hrv_data[500:505] = [45, 42, 40, 38, 35]  # HRV decrease during stress

# Plot HR and HRV
plt.figure(figsize=(10, 5))

# Heart Rate Plot
plt.subplot(2, 1, 1)
plt.plot(hr_data, label='Heart Rate')
plt.title('Heart Rate with Stress-Induced Changes')
plt.xlabel('Time')
plt.ylabel('Heart Rate (bpm)')

# HRV Plot
plt.subplot(2, 1, 2)
plt.plot(hrv_data, label='HRV (Stress Indicator)', color='orange')
plt.title('HRV with Stress-Induced Changes')
plt.xlabel('Time')
plt.ylabel('HRV (ms)')

plt.tight_layout()
plt.show()

# Output stress-related changes
print("Heart Rate and HRV changes during stress (Index 500-505):")
for i in range(500, 505):
    print(f"Index {i}: HR = {hr_data[i]} bpm, HRV = {hrv_data[i]} ms")
