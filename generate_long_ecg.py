import pandas as pd

# Load existing short ECG
data = pd.read_csv("ecg_sample.csv")
short_ecg = data["ecg"].values

# Repeat the ECG 6 times to simulate multiple beats
long_ecg = list(short_ecg) * 6

# Save to new csv
df = pd.DataFrame({"ecg": long_ecg})
df.to_csv("ecg_long.csv", index=False)

print("Long ECG file created: ecg_long.csv")
print("Length:", len(long_ecg))
