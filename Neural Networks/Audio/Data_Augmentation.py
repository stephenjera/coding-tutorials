"""
Pre-process audio files
"""


import os
import librosa
import math
import json
import librosa
import random
import numpy as np
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt
from audiomentations import Compose, AddGaussianNoise, TimeStretch
from sklearn.model_selection import train_test_split
from audiomentations import Compose, AddGaussianNoise, TimeStretch


DATASET_PATH = "Hybrid_Limited_Dataset"  # name of folder with audio files
JSON_PATH = "Dataset_Augmented_JSON_Files/Hybrid_Limited_Dataset.json"  # name of file to be created
SAMPLE_RATE = 22050
DURATION = 4  # length of audio files measured in seconds
NUM_SEGMENTS = 4
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION


def save_audio(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    # dictionary to store data
    data = {
        "mapping": [],
        # "spectrogram": [],
        "signal": [],  # not in use for Spectrogram conversion
        "labels": []
    }
    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)  # round up always

    # Loop through all the data
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        # dirpath = current folder path
        # dirnames = subfolders in dirpath
        # filenames = all files in dirpath

        # ensure that we're not at the root level (Audio folder)
        if dirpath is not dataset_path:
            # save the semantic label (name of the note)
            dirpath_components = dirpath.split("\\")  # TODO confirm what this actually does
            semantic_label = dirpath_components[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))

            # process files for specific note
            for f in filenames:
                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)

                data["signal"].append(signal.tolist()) # can't save numpy arrays as json
                data["labels"].append(i - 1)  # each iterations is a different folder

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


def load_data(dataset_path):
    """
    Loads training dataset from json file
        :param dataset_path (str): path to json file
        :return X (ndarray): inputs
        :return y (ndarray): targets
    """

    with open(dataset_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    # X = np.array(data["spectrogram"])  # for testing Spectrograms
    X = np.array(data["signal"])
    y = np.array(data["labels"])

    return X, y


def prepare_datasets(test_size, validation_size):
    """
    Create test and validation datasets
        :param test_size (float): Value in [0, 1] indicating percentage of data set to allocate to test split
        :param validation_size (float): Value in [0, 1] indicating percentage of train set to allocate to validation split
        :return X_train (ndarray): Input training set
        :return X_validation (ndarray): Input validation set
        :return X_test (ndarray): Input test set
        :return y_train (ndarray): Target training set
        :return y_validation (ndarray): Target validation set
        :return y_test (ndarray): Target test set
    """
    # load data
    X, y = load_data(JSON_PATH)

    # create train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # create train/validation split
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    """
    # CNN expects 3D array inputs are only 2D
    X_train = X_train[..., np.newaxis]  # 4D array -> [num_samples, number of time bins, mfcc_coefficients, channel]
    X_test = X_test[..., np.newaxis]
    X_validation = X_validation[..., np.newaxis]
    """
    return X_train, X_validation, X_test, y_train, y_validation, y_test


if __name__ == "__main__":
    # convert wav to JSON
    save_audio(DATASET_PATH, JSON_PATH, num_segments=2)

    # create training, validation and test sets
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)

    librosa.display.waveplot(np.asarray(X_train[0]), sr=SAMPLE_RATE)
    plt.show()

    # example of an augmentation chain
    augment = Compose([
        # p is the probability of augmentation being applied
        AddGaussianNoise(min_amplitude=0.1, max_amplitude=0.2, p=1),
        TimeStretch(min_rate=0.8, max_rate=1.2, p=1)
    ])

