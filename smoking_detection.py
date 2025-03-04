import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Simulate heart rate data
np.random.seed(42)
hr_data = np.random.normal(75, 5, 1000)  # Normal heart rate data
hr_data[500:505] = [120, 130, 125, 115, 110]  # Smoking-related heart rate spike

# Identify peaks (spikes) in the heart rate data
peaks, _ = find_peaks(hr_data, height=100)  # Height threshold for smoking spike

# Plot data and detected peaks
plt.figure(figsize=(10, 5))
plt.plot(hr_data, label='Heart Rate')
plt.plot(peaks, hr_data[peaks], "x", label='Detected Smoking Spike')
plt.title('Heart Rate with Detected Smoking Spikes')
plt.xlabel('Time')
plt.ylabel('Heart Rate (bpm)')
plt.legend()
plt.show()

# Output detected spikes (smoking-related heart rate increase)
print(f"Detected Smoking Spikes at indices: {peaks}")
