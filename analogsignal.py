import numpy as np
import matplotlib.pyplot as plt

# ---------------- Signal Parameters ---------------- #
amplitude = 10                      # Amplitude of the input sine wave (Volts)
duration = 1500                     # Duration of the signal in seconds (1500s → 50 cycles)
signal_freq = 1 / 30                # Frequency of the sine wave (1 cycle every 30s)
bits_per_sample = 8                 # PCM resolution: number of bits per sample
levels = 2 ** bits_per_sample       # Number of quantization levels (256 for 8 bits)

# ---------------- Generate Continuous Analog Signal ---------------- #
t = np.linspace(0, duration, duration * 1000)     # High-resolution time vector (1000 points/sec)
analog_signal = amplitude * np.sin(2 * np.pi * signal_freq * t)  # Generate analog sine wave

# ---------------- PCM Modulation and Demodulation Function ---------------- #
def pcm_process(fs):
    Ts = 1 / fs                                      # Sampling interval
    t_sampled = np.arange(0, duration, Ts)           # Sampled time vector
    sampled_signal = amplitude * np.sin(2 * np.pi * signal_freq * t_sampled)  # Sampled sine wave

    # Quantization: map sampled values to discrete levels
    max_val = np.max(sampled_signal)
    min_val = np.min(sampled_signal)
    step_size = (max_val - min_val) / (levels - 1)   # Quantization step size
    quantized_signal = np.round((sampled_signal - min_val) / step_size) * step_size + min_val

    # Encoding: convert quantized signal to integer PCM code (simulating binary)
    encoded_signal = ((quantized_signal - min_val) / step_size).astype(int)

    # Decoding: convert encoded values back to voltage levels
    decoded_signal = encoded_signal * step_size + min_val

    # Reconstruction: interpolate the decoded signal back to original time resolution
    reconstructed_signal = np.interp(t, t_sampled, decoded_signal)

    # ---------------- Plotting Results ---------------- #
    plt.figure(figsize=(14, 8))

    # Plot 1: Original analog signal
    plt.subplot(3, 1, 1)
    plt.plot(t, analog_signal, label='Original Signal')
    plt.title('Original Analog Signal')
    plt.grid()

    # Plot 2: Sampled and quantized signal (PCM Modulated)
    plt.subplot(3, 1, 2)
    plt.stem(t_sampled, quantized_signal, basefmt=" ")
    plt.title(f'Sampled and Quantized Signal (fs = {fs:.4f} Hz)')
    plt.grid()

    # Plot 3: Reconstructed signal (after decoding and interpolation)
    plt.subplot(3, 1, 3)
    plt.plot(t, reconstructed_signal, label='Reconstructed Signal', color='red')
    plt.title('Reconstructed Signal from PCM')
    plt.grid()

    plt.tight_layout()
    plt.show()

    return encoded_signal, decoded_signal

# ---------------- Run PCM Simulation at Different Sampling Rates ---------------- #
pcm_process(signal_freq / 2)    # Undersampling (fs = 0.5 * f)
pcm_process(signal_freq)        # Nyquist rate (fs = f)
pcm_process(signal_freq * 2)    # Oversampling (fs = 2 * f)
