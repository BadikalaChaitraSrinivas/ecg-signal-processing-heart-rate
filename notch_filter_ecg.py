import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt

# ----- Load ECG -----
data = pd.read_csv("ecg_long.csv")
ecg = data["ecg"].values


fs = 360  # sampling frequency

# ----- 50 Hz Notch Filter -----
f0 = 50       # frequency to remove
Q = 30        # Quality factor (sharpness of notch)

b, a = iirnotch(f0/(fs/2), Q)
filtered_ecg = filtfilt(b, a, ecg)

# ----- Time axis -----
time = np.arange(len(ecg)) / fs

# ----- Plot comparison -----
plt.figure(figsize=(10,5))

plt.subplot(2,1,1)
plt.plot(time, ecg)
plt.title("Before 50 Hz Noise Removal")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, filtered_ecg, color='red')
plt.title("After 50 Hz Notch Filter")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
