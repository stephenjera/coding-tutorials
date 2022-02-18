"""
This code trains a convolutional neural network to predict on audio
data and saves the model
"""

# TODO Correctly format docstrings

import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from tensorflow.keras.utils import plot_model
from Notes_to_Frequency import notes_to_frequency

DATASET_PATH = "Dataset_JSON_Files/Hybrid_Limited_Dataset3.json"
MODEL_PATH = "CNN_Model_Files/CNN_Model_Matlab_Hybrid3.h5"

# tweaking model
DROPOUT = 0.3
NUMBER_OF_NOTES = 6  # number of notes to categorise
LEARNING_RATE = 0.0001
LOSS = "sparse_categorical_crossentropy"
BATCH_SIZE = 8
EPOCHS = 150


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


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
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    return X, y


def prepare_datasets(test_size, validation_size):
    """
    Create test and validation datasets
            :param test_size: size of test set
            :param validation_size: size of validation set
            :returns X_train (ndarray): training inputs
            :returns X_validation (ndarray): validation inputs
            :returns X_test (ndarray): testing inputs
            :returns y_train (ndarray): training targets
            :returns y_validation (ndarray): validation targets
            :returns y_test (ndarray): testing targets
    """
    # load data
    X, y = load_data(DATASET_PATH)

    # create train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # create train/validation split
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    # CNN expects 3D array inputs are only 2D
    X_train = X_train[..., np.newaxis]  # 4D array -> [num_samples, number of time bins, mfcc_coefficients, channel]
    X_test = X_test[..., np.newaxis]
    X_validation = X_validation[..., np.newaxis]

    return X_train, X_validation, X_test, y_train, y_validation, y_test


def build_model(input_shape):
    # create model
    model = keras.Sequential()

    # 1st conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides=(2, 2), padding="same"))
    model.add(keras.layers.BatchNormalization())  # speeds up training

    # 2nd conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides=(2, 2), padding="same"))
    model.add(keras.layers.BatchNormalization())  # speeds up training

    # 3rd conv layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation="relu", input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((2, 2), strides=(2, 2), padding="same"))
    model.add(keras.layers.BatchNormalization())  # speeds up training

    # flatten the output and feed into Dense layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation="relu"))
    model.add(keras.layers.Dropout(DROPOUT))  # avoid over fitting

    # output layer
    model.add(keras.layers.Dense(NUMBER_OF_NOTES, activation="softmax"))

    return model


def predict(model, X, y):

    X = X[np.newaxis, ...]  # predict on 1 sample at a time
    # print("shape of X = {}".format(X.shape))
    prediction = model.predict(X)  # X -> 3D array [number of time bins, mfcc_coefficients, channel]
    # print("prediction = {}".format(prediction))
    # extract index with max value
    predicted_index = np.argmax(prediction, axis=1)
    print("Expected index: {}, Predicted index: {}".format(y, predicted_index))
    predicted_note = get_nth_key(notes_to_frequency, predicted_index)
    # return predicted_index
    return predicted_note


if __name__ == "__main__":
    # create training, validation and test sets
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)

    # build the CNN
    input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])
    model = build_model(input_shape)

    # print model
    # plot_model(model, to_file='CNN_Model_Files/Model.png')

    # compile the network
    optimizer = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer,
                  loss=LOSS,
                  metrics=["accuracy"])

    # train the network
    history = model.fit(X_train, y_train, validation_data=(X_validation, y_validation), batch_size=BATCH_SIZE, epochs=EPOCHS)
    #print(history.history.keys())
    # evaluate the CNN on the test set
    test_error, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
    print("Accuracy on test set is: {}".format(test_accuracy))

    # plot accuracy
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.title("Model Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()

    # plot loss val_loss
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.title("Model Loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend(["train", "validation" ], loc="upper right")
    plt.show()

    # save model
    model.save(MODEL_PATH)


