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
from audiomentations import Compose, AddGaussianNoise, TimeStretch, FrequencyMask,\
    PolarityInversion, Gain, GainTransition, LoudnessNormalization, TimeMask
from sklearn.model_selection import train_test_split


DATASET_PATH = "Hybrid_Limited_Dataset"  # name of folder with audio files
JSON_PATH = "Dataset_Augmented_JSON_Files/Hybrid_Limited_Dataset.json"  # name of file to be created
SAMPLE_RATE = 22050
DURATION = 4  # length of audio files measured in seconds
NUM_SEGMENTS = 4
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION


def load_dataset(dataset_path):
    # dictionary to store data
    data = {
        "mapping": [],
        "signal": [],
        "labels": []
    }

    # mappings, signal, label
    #data = [[],[],[]]
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
            #data[0].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))

            # process files for specific note
            for f in filenames:
                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
                data["signal"].append(signal)
                #data[1].append(signal)
                data["labels"].append(i - 1)  # each iterations is a different folder
                #data[2].append(i - 1)
    return data


def prepare_datasets(data, test_size, validation_size):
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
    #X, y = load_data(JSON_PATH)
    X = data["signal"]
    y = data["labels"]
    print("DatasetsX: ", len(X))
    print("Datasetsy: ", len(y))
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


def augment(signal, label):
    """
    Takes a signal and put it through an augmentation chain
    :param signal:
    :param label:
    :return: signal , label
    """
    # augmentation chain
    augment = Compose([
        # p is the probability of augmentation being applied
        AddGaussianNoise(min_amplitude=0.1, max_amplitude=0.2),
        TimeStretch(min_rate=0.8, max_rate=1.2),
        FrequencyMask(0.2, 0.5),
        PolarityInversion(),
        TimeMask(fade=True),
        LoudnessNormalization()
    ])
    signal = augment(signal, sample_rate=SAMPLE_RATE)
    return signal, label


def save_mfcc(json_path,  X_train, X_validation, X_test, y_train,
              y_validation, y_test,n_mfcc=13, n_fft=2048, hop_length=512,
              num_segments=1):
    data = {
        "X_train_augmented": [],
        "X_validation": [],
        "X_test": [],
        "y_train_augmented": [],
        "y_validation": [],
        "y_test" : []
    }

    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)  # round up always

    # create mfcc for training data
    for i in range(len(X_train)):
        # process segments extracting mfcc and storing data
        #for s in range(num_segments):
            #start_sample = num_samples_per_segment * s  # s=0 -> 0
            #finish_sample = start_sample + num_samples_per_segment  # s=0 -> num_samples_per_segment

            mfcc = librosa.feature.mfcc(X_train[i],
                                        sr=SAMPLE_RATE,
                                        n_fft=n_fft,
                                        n_mfcc=n_mfcc,
                                        hop_length=hop_length)
            mfcc = mfcc.T  # TODO find out why this is better to work with
            if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                data["X_train_augmented"].append(mfcc.tolist())
                data["y_train_augmented"].append(y_train[i])

    # create mfcc for validation data
    for j in range(len(X_validation)):
        # process segments extracting mfcc and storing data
        #for s in range(num_segments):
            #start_sample = num_samples_per_segment * s  # s=0 -> 0
            #finish_sample = start_sample + num_samples_per_segment  # s=0 -> num_samples_per_segment

            mfcc = librosa.feature.mfcc(X_test[j],
                                        sr=SAMPLE_RATE,
                                        n_fft=n_fft,
                                        n_mfcc=n_mfcc,
                                        hop_length=hop_length)
            mfcc = mfcc.T  # TODO find out why this is better to work with
            if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                data["X_validation"].append(mfcc.tolist())
                data["y_validation"].append(y_test[j])

    # create mfcc for test data
    for k in range(len(X_test)):
        # process segments extracting mfcc and storing data
        #for s in range(num_segments):
            #start_sample = num_samples_per_segment * s  # s=0 -> 0
            #finish_sample = start_sample + num_samples_per_segment  # s=0 -> num_samples_per_segment

            mfcc = librosa.feature.mfcc(X_test[k],
                                        sr=SAMPLE_RATE,
                                        n_fft=n_fft,
                                        n_mfcc=n_mfcc,
                                        hop_length=hop_length)
            mfcc = mfcc.T  # TODO find out why this is better to work with
            if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                data["X_test"].append(mfcc.tolist())
                data["y_test"].append(y_test[k])
    """
    data["X_validation"] = X_validation.tolist()
    data["X_test"] = X_test.tolist()
    data["y_validation"] = y_validation.tolist()
    data["y_test"] = y_test.tolist()
    """
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)




if __name__ == "__main__":
    # convert wav to JSON
    data = load_dataset(DATASET_PATH)
    print(data)

    # create training, validation and test sets
    X_train, X_validation, X_test, y_train, y_validation,\
    y_test = prepare_datasets(data, 0.25, 0.2)

    print("X train size: ", len(X_train))
    X_train_augmented = X_train.copy()
    y_train_augmented = y_train.copy()
    for i in range(len(X_train)):
        signal, label = augment(X_train[i], y_train[i])
        X_train_augmented.append(signal)
        y_train_augmented.append(label)
    print("X train augmented: ", len(X_train_augmented))
    print(y_train_augmented)

    save_mfcc(JSON_PATH, X_train_augmented, X_validation,
                       X_test, y_train_augmented, y_validation, y_test)


    #librosa.display.waveplot(np.asarray(X_train[0]), sr=SAMPLE_RATE)
    #plt.show()



