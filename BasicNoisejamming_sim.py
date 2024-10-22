import numpy as np
import matplotlib.pyplot as plt

# Parameters
time = np.linspace(0, 1, 1000)  # Time vector
radar_freq = 10  # Radar frequency in Hz
radar_signal = np.sin(2 * np.pi * radar_freq * time)  # Radar signal (sine wave)

# Jamming Signal - Noise
jamming_power = 0.5
jamming_signal = jamming_power * np.random.normal(0, 1, len(time))  # White noise

# Combine radar and jamming signals
combined_signal = radar_signal + jamming_signal

# Plot the signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(time, radar_signal)
plt.title('Radar Signal')
plt.subplot(3, 1, 2)
plt.plot(time, jamming_signal)
plt.title('Jamming Signal (Noise)')
plt.subplot(3, 1, 3)
plt.plot(time, combined_signal)
plt.title('Combined Radar and Jamming Signal')
plt.tight_layout()
plt.show()
