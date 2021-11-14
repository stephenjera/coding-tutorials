import matplotlib.pyplot as plt
import librosa.display


AUDIO_FILE = "Long_Song_Test\\Sample1\\Sample1.wav"

signal, sr = librosa.load(AUDIO_FILE)
mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
spectrogram = librosa.feature.melspectrogram(signal)
spectrogram = librosa.power_to_db(spectrogram)
plt.subplot(211)
librosa.display.specshow(mfcc, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2f")
plt.ylabel("coefficients")

plt.subplot(212)
librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2f")
plt.show()




