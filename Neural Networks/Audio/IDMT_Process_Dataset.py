
import os
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup
import librosa
import math
import json
import pandas as pd
import numpy as np
#import pandas_read_xml as pdx

DATASET_PATH = "IDMT-SMT-GUITAR_V2_Dataset/dataset1"
JSON_PATH = "Dataset_JSON_Files/IDMT-SMT-GUITAR_V2_Dataset.json"
SAMPLE_RATE = 22050
DURATION = 1  # length of audio files measured in seconds
NUM_SEGMENTS = 1
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
deleted = []


def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=1):
    # dictionary to store data
    dataset = {"audioFileName": [],
               "mfcc": [],
               "labels": [],
               "fretNumber": [],
               "stringNumber": []
               }

    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)
    print("expected_num_mfcc_vectors_per_segment: ", expected_num_mfcc_vectors_per_segment)
    # Loop through all the data
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        # dirpath = current folder path
        # dirnames = subfolders in dirpath
        # filenames = all files in dirpath
        #print(dirnames)
        # ensure that we're not at the root level (Audio folder)

        """
        for name in filenames:
            if "G53-40100-1111-00001.xml" in name:
                print(os.path.abspath(os.path.join(dirpath, name)))
        """
        if dirpath is not dataset_path:
            # process files for specific note
            for f in range(len(filenames)):
                # split file name into name and extension
                split_tup = os.path.splitext(filenames[f])
                file_path = os.path.abspath(os.path.join(dirpath, filenames[f]))
                if split_tup[1] == ".xml":
                    # get absolute path of file
                    print(file_path)
                    with open(file_path, "r") as fp:
                        data = fp.read()

                    # get data into processable format
                    soup = BeautifulSoup(data, "xml")
                    dataset["audioFileName"].append(soup.audioFileName.text)
                    dataset["labels"].append(int(soup.pitch.text))
                    dataset["fretNumber"].append(soup.fretNumber.text)
                    dataset["stringNumber"].append(soup.stringNumber.text)
                elif split_tup[1] == ".wav":
                    # load audio file
                    signal, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
                    # process segments extracting mfcc and storing data
                    for s in range(num_segments):
                        start_sample = num_samples_per_segment * s  # s=0 -> 0
                        finish_sample = start_sample + num_samples_per_segment  # s=0 -> num_samples_per_segment
                        mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],
                                                    sr=sr,
                                                    n_fft=n_fft,
                                                    n_mfcc=n_mfcc,
                                                    hop_length=hop_length)
                        mfcc = mfcc.T  # TODO find out why this is better to work with

                        # store mfcc for segment if it has expected length
                        if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                            dataset["mfcc"].append(mfcc.tolist())  # can't save numpy arrays
                        else:
                            deleted.append(file_path)

        # print(dataset)

    with open(json_path, "w") as fp:
        json.dump(dataset, fp, indent=4)

        """
        # Reading the data inside the xml file to a variable under the name  data
        with open("IDMT-SMT-GUITAR_V2_Dataset/dataset1/"
                         "Fender Strat Clean Neck SC/annotation/"
                         "G53-40100-1111-00001.xml", "r") as f:
            data = f.read()
        
        # print(data)
        
        soup = BeautifulSoup(data, "xml")
        
        print(soup)
        
        
        dataset_df = pd.DataFrame(dataset)
        #print(dataset_df)
        s = pd.DataFrame([soup.audioFileName.text], columns=["audioFileName"])
        dataset_df.append(s, ignore_index=True)
        t = pd.DataFrame([soup.pitch.text], columns=["pitch"])
        dataset_df.append(t, ignore_index=True)
        
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            print(dataset_df)
        
        #["audioFileName"] = soup.audioFileName.text
        #dataset_df["pitch"] = soup.pitch.text
        
        #dataset_df.append("audioFileName", soup.audioFileName.text)
        print(dataset_df.head())
        #print(soup.pitch.text)
        
        
        # Passing the stored data inside the beautifulsoup parser
        bs_data = BeautifulSoup(data, "xml")
        
        # Finding all instances of tag
        b_unique = bs_data.find_all('unique')
        print(b_unique)
        
        
        df = pd.read_xml("IDMT-SMT-GUITAR_V2_Dataset/dataset1/"
                         "Fender Strat Clean Neck SC/annotation/"
                         "G53-40100-1111-00001.xml")
        """


if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=NUM_SEGMENTS)
    print(deleted)

