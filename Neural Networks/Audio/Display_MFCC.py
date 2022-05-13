"""
This code displays the MFCC and spectrogram of the selected AUDIO_FILE
"""

import matplotlib.pyplot as plt
import seaborn as sns
import librosa.display

AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\C_Major_Scale.wav"
signal, sr = librosa.load(AUDIO_FILE)
signal_nom = librosa.util.normalize(signal)
mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
spectrogram = librosa.feature.melspectrogram(signal)
spectrogram = librosa.power_to_db(spectrogram)


# signal_db = librosa.amplitude_to_db(signal)
librosa.display.waveplot(signal_nom, sr=sr)
plt.title("Normalised Ample Guitar A4 waveform")
plt.ylabel("Aplitude ")
plt.xlabel("Time (s)")
plt.show()

plt.subplot(211)
plt.title("Ample Guitar A4 MFCC")
librosa.display.specshow(mfcc, sr=sr, x_axis="time", y_axis="log", bins_per_octave=13)
#plt.colorbar(format="%+2f")
plt.ylabel("Mel Coefficients")
plt.xlabel("Time (s)")

#plt.subplot(212)
plt.title("C Major Scale Spectrogram")
librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log", bins_per_octave=13)
#plt.colorbar(format="%+2f")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.rc('font', size=50) #controls default text size
plt.show()





