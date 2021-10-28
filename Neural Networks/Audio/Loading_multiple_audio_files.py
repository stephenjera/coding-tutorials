import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os


#TODO mutilpe return values for load with librosa


def load_data(name):
    file_names = []
    path = 'Data'
    x = 0
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            file_names.append(os.path.join(root, name))
#        for name in directories:
 #           print(os.path.join(root, name))
    return file_names


def load_with_librosa(filenames):
    samples = [i for i in range(len(filenames))]  # initialse samples
    for i in range(len(filenames)):
        samples[i], sr = librosa.load(file_names[i])
    return samples


# Extracting short time fourier transform
def extract_stft(samples_in):
    s_samples = [i for i in range(len(samples_in))]
    frame_size = 2048
    hop_size = 512

    for i in range(len(samples_in)):
        s_samples[i] = librosa.stft(samples_in[i], n_fft=frame_size, hop_length=hop_size)
    return s_samples


def calc_spectrogram(s_samples):
    # Calculating spectrogram
    y_samples = [i for i in range(len(s_samples))]
    for i in range(len(s_samples)):
        y_samples[i] = np.abs(s_samples[i]) ** 2
    return y_samples


# Visualising the spectrogram
def plot_spectrogram(y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(y,
                             sr=sr,
                             hop_length=hop_length,
                             x_axis="time",
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_names = load_data("test")
    print(file_names)
    samples = load_with_librosa(file_names)
    print(samples)
    s_samples = extract_stft(samples)
    print(s_samples)
    spectrograms = calc_spectrogram(s_samples)
    print("printing spectrograms")
    print(spectrograms)

    # Visualising the spectrogram
    frame_size = 2048
    hop_size = 512
    sr = 22050
    # Log amplitude spectrogram
    Y_log_sample = librosa.power_to_db(spectrograms[1])
    print(Y_log_sample)
    plot_spectrogram(Y_log_sample, sr, hop_size, y_axis="log")
    plt.show()
