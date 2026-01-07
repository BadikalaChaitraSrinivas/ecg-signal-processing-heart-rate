import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# ----- Load ECG -----
data = pd.read_csv("ecg_long.csv")
ecg = data["ecg"].values

fs = 360
time = np.arange(len(ecg)) / fs

# ----- Detect Peaks -----
# height = threshold, distance = minimum gap to avoid false detections
peaks, _ = find_peaks(ecg, height=0.5, distance=50)

# ----- Plot -----
plt.figure(figsize=(10,4))
plt.plot(time, ecg)
plt.plot(time[peaks], ecg[peaks], "ro", label="R-peaks")
plt.title("R-Peak Detection")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

print("Detected R-peaks:", len(peaks))


# ---- Heart Rate Calculation ----
if len(peaks) > 1:
    rr_intervals = np.diff(peaks) / fs   # convert sample gaps to seconds
    avg_rr = rr_intervals.mean()
    heart_rate = 60 / avg_rr

    print("RR Intervals (seconds):", rr_intervals)
    print("Average RR Interval:", avg_rr)
    print("Estimated Heart Rate (BPM):", heart_rate)
else:
    print("Not enough peaks to calculate heart rate")

# ---- HRV Calculation ----
if len(peaks) > 2:
    sdnn = np.std(rr_intervals)
    rmssd = np.sqrt(np.mean(np.square(np.diff(rr_intervals))))
    print("SDNN:", sdnn)
    print("RMSSD:", rmssd)

for p in peaks:
    plt.axvline(time[p], color='r', linestyle='--')

