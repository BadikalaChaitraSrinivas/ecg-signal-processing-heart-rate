# ECG Signal Processing & Heart Rate Detection (Python + DSP)

In this project, I built a complete **ECG (Electrocardiogram) signal processing pipeline** using Python and Digital Signal Processing techniques, similar to what is used in medical monitors and wearable health devices.

The system performs:
- ECG loading and visualization  
- Baseline wander removal  
- 50 Hz powerline interference removal  
- Clean ECG generation  
- R-peak detection  
- Heart Rate (BPM) calculation  

This project helped me understand both biomedical signal characteristics and practical DSP implementation.

---

## Project Structure

```
ECG-Heart-Rate-DSP
│
├── data/
│   ├── ecg_sample.csv        # base ECG snippet
│   └── ecg_long.csv          # extended ECG with multiple beats
│
├── src/
│   ├── plot_ecg.py           # ECG visualization
│   ├── filter_baseline.py    # baseline drift removal
│   ├── notch_filter_ecg.py   # 50Hz powerline noise removal
│   ├── generate_long_ecg.py  # create longer ECG
│   └── rpeak_detection.py    # R-peaks + Heart Rate
│
├── results/
│   ├── raw_ecg_plot.png
│   ├── baseline_corrected_plot.png
│   ├── notch_filtered_plot.png
│   ├── rpeak_plot.png
│
├── README.md
└── requirements.txt
```

---

## Technology Stack
- Python  
- NumPy  
- Pandas  
- SciPy (signal processing)  
- Matplotlib  

Install dependencies:
```
pip install numpy scipy pandas matplotlib
```

---

# Processing Workflow

---

## 1. Loading and Visualizing the ECG  
**File:** `plot_ecg.py`

I started by loading the ECG signal from `ecg_sample.csv` and plotting it assuming a sampling frequency of 360 Hz.  
This helped me observe key ECG components like the P-wave, QRS complex, and T-wave. This is the raw signal before any processing.

---

## 2. Baseline Wander Removal  
**File:** `filter_baseline.py`

Real ECG signals usually drift due to breathing, electrode movement, and skin impedance.  
To fix this, I implemented a **high-pass filter (~0.5 Hz)** to remove very low-frequency drift.

**Result:**  
The signal becomes centered and stable, making it more clinically usable.

---

## 3. 50 Hz Powerline Noise Removal  
**File:** `notch_filter_ecg.py`

Since power supply systems introduce 50 Hz noise into ECG recordings, I implemented a **notch filter at 50 Hz** to eliminate this interference.

**Result:**  
A cleaner ECG waveform. Although the dataset I used is mostly clean, this step is essential in real-world biomedical systems.

---

## 4. Extending ECG to Multiple Heartbeats  
**File:** `generate_long_ecg.py`

The original ECG sample contained only one heartbeat, which is insufficient to calculate heart rate.  
So I generated a longer ECG signal (`ecg_long.csv`) by repeating the waveform to simulate a multi-second recording.

---

## 5. R-Peak Detection & Heart Rate Calculation  
**File:** `rpeak_detection.py`

I detected R-peaks using:
```
scipy.signal.find_peaks()
```

Then calculated:
- RR intervals (time between heartbeats)
- Average RR
- Heart Rate = 60 / Average RR

**Output includes:**
- ECG waveform with R-peaks marked
- Number of detected peaks
- RR intervals
- Calculated Heart Rate in BPM

At this stage, the system behaves like a basic ECG heart monitor.

---

# Frequency and DSP Reasoning

Even though ECG is primarily analyzed in the time domain, frequency-domain understanding is important.

| ECG Component | Frequency Range |
|--------------|-----------------|
Baseline drift | < 0.5 Hz  
Powerline noise | 50 Hz  
QRS energy     | ~5–15 Hz  

So the filtering strategy was:
- High-pass filter removes <0.5 Hz drift  
- Notch filter removes 50 Hz power noise  
- Remaining signal preserves meaningful ECG characteristics  

This ensures a clean time-domain waveform that still retains critical medical information.

---

# Final Outcome

By completing this project, I was able to:
- Build a working biomedical DSP pipeline  
- Implement medical-grade ECG preprocessing  
- Improve signal quality through filtering  
- Detect R-peaks accurately  
- Compute Heart Rate reliably  
- Visualize and interpret ECG data effectively  

### Key Skills Demonstrated
- Digital Signal Processing
- Biomedical signal understanding
- Python scientific computing
- Filtering and feature extraction
- Practical problem-solving and implementation

---

# Future Enhancements
I am planning to extend this project with:
- Heart Rate Variability (HRV) metrics such as SDNN and RMSSD  
- Testing with real clinical datasets (MIT-BIH)  
- Real-time ECG streaming and processing  
- GUI dashboard for visualization  
- Arrhythmia / abnormal heartbeat detection  

---

### About This Project
I built this project to practically learn Biomedical Signal Processing and to simulate how real ECG monitoring systems preprocess and analyze heart signals.

