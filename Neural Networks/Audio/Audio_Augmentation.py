import librosa
import random
import numpy as np
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt
from audiomentations import Compose, AddGaussianNoise, TimeStretch


AUDIO_FILE = "D:\\P\\Python-Projects\\Neural Networks\\Audio\\Hybrid_Limited_Dataset\\A4\\Ample A4.wav"


def plot_signal_and_augmented(signal, augmented_signal, sr):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveplot(signal, sr=sr, ax=ax[0])
    ax[0].set(title="Original Signal")
    librosa.display.waveplot(augmented_signal, sr=sr, ax=ax[1])
    ax[1].set(title="Augmented Signal")
    plt.show()

def add_white_noise(signal, noise_percentage_factor):
    """
    Add white noise to a signal
    :param signal: signal to be augmented
    :param noise_percentage_factor: percentage of noise the signal shoule be
    :return: augmented_signal
    """
    # create gaussian distribution centered around zero
    # uses stanard deviation of the signal
    # noise should be same size as signal
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal


def time_stretch(signal, time_stretch_rate):
    """
    Stretch the signal in time
    :param signal: signal to be augmented
    :param time_stretch_rate: value to stretch by
    value should be between 0.8 and 1.2 to avoid major artifacts
    :return: augmented signal
    """

    return librosa.effects.time_stretch(signal, time_stretch_rate)


# Likey won't need this function
def pitch_scale(signal, sr, num_semitones):
    # no more than 5 or 5 semitones to avoid degradation of audio
    return librosa.effects.pitch_shift(signal, sr, num_semitones)


def invert_polarity(signal):
    # invert the signal
    return signal * -1


def random_gain(signal, min_factor=0.1, max_factor=0.12):
    """
    Scale signal by a random gain factor
    :param signal: signal to be augmented
    :param min_factor: minimum gain factor
    :param max_factor: maximum gain factor
    :return: augmented_signal
    """
    # generate random number between the factors
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


if __name__=="__main__":
    signal, sr = librosa.load(AUDIO_FILE)  # y is a numpy array of the wav file, sr = sample rate
    augmented_signal = random_gain(signal, 2, 4)
    plot_signal_and_augmented(signal, augmented_signal, sr)

    # example of an augmentation chain
    augment = Compose([
        # p is the probability of augmentation being applied
        AddGaussianNoise(min_amplitude=0.1, max_amplitude=0.2, p=1),
        TimeStretch(min_rate=0.8, max_rate=1.2, p=1)
    ])

    augmented_signal = augment(signal, sr)
    plot_signal_and_augmented(signal, augmented_signal, sr)


