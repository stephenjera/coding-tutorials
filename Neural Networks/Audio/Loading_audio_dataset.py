import librosa
import librosa.display
import random
import numpy as np
import matplotlib.pyplot as plt
import os

DATADIR = "Guitar Notes Dataset"
CATEGORIES = ["A0", "A1", "A2", "A3", "A4"]
training_data = []
# Inputs to neural network
X = []  # Features
Y = []  # Labels


def create_training_data():
    for catergory in CATEGORIES:
        path = os.path.join(DATADIR, catergory)  # path to notes
        class_num = CATEGORIES.index(catergory)  # convert labels to numbers
        for note in os.listdir(path):
            try:
                # Load with Librosa
                samples_array, sr = librosa.load(os.path.join(path, note), sr=22050, duration=3)
                training_data.append([samples_array, class_num])
            except Exception as e:
                pass


create_training_data()
random.shuffle(training_data)  # Stop network from learning incorrect pattern
#print(len(training_data))
#print(training_data)
for sample in training_data:
    print(sample[1])

for features, label in training_data:
    X.append(features)
    Y.append(label)

# X needs to be a numpy array
X = np.array(X).reshape(-1, len(CATEGORIES))
print(X)

