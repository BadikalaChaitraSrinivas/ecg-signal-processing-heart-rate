import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----- Load ECG -----
data = pd.read_csv("ecg_long.csv")
ecg = data["ecg"].values


# Sampling frequency (standard MIT-BIH style)
fs = 360
time = np.arange(len(ecg)) / fs

print("Samples:", len(ecg))
print("Duration (sec):", len(ecg)/fs)

# ----- Plot ECG -----
plt.figure(figsize=(10,4))
plt.plot(time, ecg)
plt.title("Raw ECG Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.show()
