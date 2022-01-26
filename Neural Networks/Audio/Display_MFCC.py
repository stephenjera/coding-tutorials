"""
This code displays the MFCC and spectrogram of the selected AUDIO_FILE
"""

import matplotlib.pyplot as plt
import librosa.display


AUDIO_FILE = "D:\\M\\Matlab-Projects\\Guitar Simulation\\mary.wav"

signal, sr = librosa.load(AUDIO_FILE)
mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
spectrogram = librosa.feature.melspectrogram(signal)
spectrogram = librosa.power_to_db(spectrogram)

plt.subplot(211)
plt.title("E note MFCC Karplus-Strong")
librosa.display.specshow(mfcc, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2f")
plt.ylabel("coefficients")

plt.subplot(212)
plt.title("E note Spectrogram Karplus-Strong")
librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2f")
plt.show()




