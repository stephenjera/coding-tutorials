# Extracting a spectrogram from audio file
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# File path
filename = "Sample1.wav"

# Load audio file with libROSA
# Sample1 is a numpy array and sr = sample rate
sample1, sr = librosa.load(filename)

# Extracting short time fourier transform
frame_size = 2048
hop_size = 512

S_sample1 = librosa.stft(sample1, n_fft=frame_size, hop_length=hop_size)
# S_sample1.shape
# type(S_sample1[0][0])

# Calculating spectrogram
Y_sample1 = np.abs(S_sample1) ** 2

# Visualising the spectrogram


def plot_spectrogram(y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(y,
                             sr=sr,
                             hop_length=hop_length,
                             x_axis="time",
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")


# Linear spectrogram
# plot_spectrogram(Y_sample1, sr, hop_size)

# Log amplitude spectrogram
Y_log_sample1 = librosa.power_to_db(Y_sample1)
# plot_spectrogram(Y_log_sample1, sr, hop_size)

# Log frequency spectrogram
plot_spectrogram(Y_log_sample1, sr, hop_size, y_axis="log")
plt.show()



