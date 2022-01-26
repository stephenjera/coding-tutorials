"""
This code trains a convolutional neural network to predict on audio
data and saves the model
"""

import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras

DATASET_PATH = "Simulated_Dataset_Matlab_two_seg.json"
MODEL_PATH = "CNN_model_Matlab_two_seg.h5"


def load_data(dataset_path):
    """ Loads training dataset from json file
        :param dataset_path (str): path to json file
        :return X (ndarray): inputs
        :return y (ndarray): targets
    """

    with open(dataset_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    return X, y


def prepare_datasets(test_size, validation_size):
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
    model.add(keras.layers.Dropout(0.3))  # avoid over fitting

    # output layer
    model.add(keras.layers.Dense(27, activation="softmax"))  # 27 is number of notes to categorise

    return model


def predict(model, X, y):

    X = X[np.newaxis, ...]  # predict on 1 sample at a time
    # print("shape of X = {}".format(X.shape))
    prediction = model.predict(X)  # X -> 3D array [number of time bins, mfcc_coefficients, channel]
    # print("prediction = {}".format(prediction))
    # extract index with max value
    predicted_index = np.argmax(prediction, axis=1)
    print("Expected index: {}, Predicted index: {}".format(y, predicted_index))
    return predicted_index


if __name__ == "__main__":
    # create training, validation and test sets
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)

    # build the CNN
    input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])
    model = build_model(input_shape)

    # compile the network
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer,
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    # train the network
    model.fit(X_train, y_train, validation_data=(X_validation, y_validation), batch_size=10, epochs=50)

    # evaluate the CNN on the test set
    test_error, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
    print("Accuracy on test set is: {}".format(test_accuracy))

    # save model
    model.save(MODEL_PATH)


