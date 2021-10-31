import librosa
import librosa.display
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#Setting up GPU usage
physical_devices = tf.config.experimental.list_physical_devices("GPU")
print("Num GPUs Available: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)

DATADIR = "Guitar Notes Dataset"
CATEGORIES = ["A0", "A1", "A2", "A3", "A4"]
training_data = []
# Inputs to neural network
X = []  # Features
Y = []  # Labels
frame_size = 2048
hop_size = 512


def create_training_data():
    class_num = []
    for catergory in CATEGORIES:
        path = os.path.join(DATADIR, catergory)  # path to notes
        class_num = CATEGORIES.index(catergory)  # convert labels to numbers
        samples_array = np.array([[]])
        for note in os.listdir(path):
            try:
                # Load with Librosa
                samples_array, sr = librosa.load(os.path.join(path, note), duration=3)
                #print("Samples array: ", samples_array)
            except Exception as e:
                pass

    # Extracting short time fourier transform
    stft_samples = [i for i in range(len(samples_array))]
    for i in range(len(samples_array)):
        stft_samples = librosa.stft(samples_array, n_fft=frame_size, hop_length=hop_size)
        #print("stft array: ", stft_samples)

    # Calculating spectrogram
    spectrograms = [i for i in range(len(stft_samples))]
    for stft in range(len(stft_samples)):
        spectrograms = np.abs(stft_samples[stft]) ** 2
        training_data.append([spectrograms, class_num])


create_training_data()
random.shuffle(training_data)  # Stop network from learning incorrect pattern
print("Length of training data: ", len(training_data))
print("Type of training data: ", type(training_data))
#print(training_data)
#for sample in training_data:
    #print(sample[1])

for features, label in training_data:
    X.append(features)
    Y.append(label)

# X needs to be a numpy array
X = np.array(X).reshape(-1, len(CATEGORIES))

print("X shape: ", X.shape)
print(type(X))
#print(X)
#print("Length of 1st element in X:", len(X[0][0]))
#print("Length of 2nd element in X:", len(X[0][1]))
#print("Length of 5th element in X:", len(X[0][4]))

#tf.convert_to_tensor(X, dtype=tf.float32)

Y = np.array(Y).reshape(-1, len(CATEGORIES))
print("Y shape: ", Y.shape)
print(type(Y))
#print(Y)

# Normailse data
X = X/len(CATEGORIES)
#print(X)


# Build model
model = Sequential([
    Dense(units=16, input_shape=X.shape, activation="relu"),
    Dense(units=32, activation="relu"),
    Dense(units=len(CATEGORIES), activation='softmax')
])

model.summary()
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
model.fit(x=X, y=Y, batch_size=1, epochs=10, verbose=2)

"""
model.add( input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64), (3, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="categorical_crossentropy",
              from_logits=False,
              label_smoothing=0,
              axis=-1,
              reduction="auto",
              metrics=['accuracy'])

model.fit(X, Y, batch_size=1)
"""
