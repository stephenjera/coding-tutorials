"""
This code displays the MFCC and spectrogram of the selected AUDIO_FILE
"""

import matplotlib.pyplot as plt
import librosa.display


# AUDIO_FILE = "D:\\M\\Matlab-Projects\\Guitar Simulation\\mary.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Notes Recorded\\A5\\A5.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Data\\A2.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Simulated_Dataset_Matlab\\A5\\A5.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Simulation\\A2 Simulated\\A2\\A20.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Simulation\\excite-picked-nodamp.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Notes Recorded\\overlapped A4.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Notes Recorded\\Virtual Guitar A4.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Notes Recorded\\note-a-flamenco-5th-string_A.wav"
# AUDIO_FILE =  "D:\\P\\Python-Projects\\Neural Networks\\Audio\\GuitarSet\\audio_hex-pickup_debleeded\\00_BN1-129-Eb_comp_hex_cln.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Notes Recorded\\apronus A4.wav"
# AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Guitar Simulation\\A4 Simulated\\A4\\A4.wav"
AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Apronus_Dataset\\G4\\G4.wav"

signal, sr = librosa.load(AUDIO_FILE)
mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
spectrogram = librosa.feature.melspectrogram(signal)
spectrogram = librosa.power_to_db(spectrogram)

plt.subplot(211)
plt.title("Apronus_Dataset G4 MFCC")
librosa.display.specshow(mfcc, sr=sr, x_axis="time", y_axis="log", bins_per_octave=13)
plt.colorbar(format="%+2f")
plt.ylabel("Mel Coefficients (frequency)")

plt.subplot(212)
plt.title("Apronus_Dataset G4 Spectrogram")
librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log", bins_per_octave=13)
plt.colorbar(format="%+2f")
plt.ylabel("Frequency (Hz)")
plt.show()




