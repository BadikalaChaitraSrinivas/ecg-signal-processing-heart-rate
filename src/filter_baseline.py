import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# ----- Load ECG -----
data = pd.read_csv("ecg_long.csv")
ecg = data["ecg"].values


fs = 360   # sampling frequency

# ----- High Pass Filter (remove baseline drift) -----
cutoff = 0.5   # Hz
order = 4

b, a = butter(order, cutoff/(fs/2), btype='high')
filtered_ecg = filtfilt(b, a, ecg)

# ----- Time axis -----
time = np.arange(len(ecg)) / fs

# ----- Plot comparison -----
plt.figure(figsize=(10,5))

plt.subplot(2,1,1)
plt.plot(time, ecg)
plt.title("Original ECG")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, filtered_ecg, color='green')
plt.title("After Baseline Drift Removal (High Pass Filter)")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
