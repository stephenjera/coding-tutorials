"""
This code creates the JSON file of the notes
"""

# TODO Correctly format docstrings
# TODO Test if MFCC to spectrogram changes work as intended

import os
import librosa
import math
import json

# DATASET_PATH = "Simulated_Dataset_Matlab_Limited"
# JSON_PATH = "Dataset_JSON_Files/Simulated_Dataset_Matlab_Limited.json"
DATASET_PATH = "Only_A4_Recorded_Trimmed"  # name of folder with audio files
JSON_PATH = "Dataset_JSON_Files/Only_A4_Recorded_Trimmed3.json"  # name of file to be created
SAMPLE_RATE = 22050
DURATION = 3  # length of audio files measured in seconds(all files are variable lengths)
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION


# Modified to create spectrograms instead of MFCCs (Testing phase)
def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    """Creates a JSON file of the MFCCs for the dataset
        :param
        ----------
         dataset_path: path to the dataset folder
         json_path: name of JSON file to be created
         n_mfcc: number of MFCC coefficients to create
         n_fft:
         hop_length:
         num_segments:

    """
    # dictionary to store data
    data = {
        "mapping": [],
        # "spectrogram": [],
        "mfcc": [],  # not in use for Spectrogram conversion
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
            dirpath_components = dirpath.split("\\")    # TODO confirm what this actually does
            semantic_label = dirpath_components[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))

            # process files for specific note
            for f in filenames:
                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)

                # process segments extracting mfcc and storing data
                for s in range(num_segments):
                    start_sample = num_samples_per_segment * s  # s=0 -> 0
                    finish_sample = start_sample + num_samples_per_segment  # s=0 -> num_samples_per_segment

                    """
                    # Modification to use spectrograms
                    spectrogram = librosa.feature.melspectrogram(signal[start_sample:finish_sample],
                                                sr=sr,
                                                n_fft=n_fft,
                                                hop_length=hop_length)

                    spectrogram = spectrogram.T

                    # Says MFCC but should work for spectrograms
                    if len(spectrogram) == expected_num_mfcc_vectors_per_segment:
                        data["spectrogram"].append(spectrogram.tolist())  # can't save numpy arrays as json files
                        data["labels"].append(i - 1)  # each iterations is a different folder
                        print("{}, segment:{}".format(file_path, s + 1))
                    """
                    mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],
                                                sr=sr,
                                                n_fft=n_fft,
                                                n_mfcc=n_mfcc,
                                                hop_length=hop_length)
                    mfcc = mfcc.T  # TODO find out why this is better to work with

                    # store mfcc for segment if it has expected length
                    if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                        data["mfcc"].append(mfcc.tolist())  # can't save numpy arrays as json files
                        data["labels"].append(i - 1)  # each iterations is a different folder
                        print("{}, segment:{}".format(file_path, s+1))

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=DURATION)
