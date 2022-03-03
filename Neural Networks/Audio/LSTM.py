import json
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from tensorflow.keras.utils import plot_model
from Notes_to_Frequency import notes_to_frequency

DATASET_PATH = "Dataset_JSON_Files/Simulated_Dataset_Matlab_Spectrograms.json"
MODEL_PATH = "CNN_Model_Files/CNN_Model_Matlab_Test_2.h5"

# tweaking model
DROPOUT = 0.3
NUMBER_OF_NOTES = 27  # number of notes to classify
LEARNING_RATE = 0.0001
LOSS = "sparse_categorical_crossentropy"
BATCH_SIZE = 32
EPOCHS = 30


def load_data(dataset_path):
    """
    Loads training dataset from json file.
        :param data_path (str): Path to json file containing data
        :return X (ndarray): Inputs
        :return y (ndarray): Targets
    """

    with open(dataset_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    X = np.array(data["mfcc"])
    #X = np.array(data["spectrogram"])
    y = np.array(data["labels"])
    return X, y


def plot_history(history):
    """
    Plots accuracy/loss for training/validation set as a function of the epochs
        :param history: Training history of model

    """

    fig, axs = plt.subplots(2)

    # create accuracy sublpot
    axs[0].plot(history.history["accuracy"], label="train accuracy")
    axs[0].plot(history.history["val_accuracy"], label="test accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy evaluation")

    # create error sublpot
    axs[1].plot(history.history["loss"], label="train error")
    axs[1].plot(history.history["val_loss"], label="test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error evaluation")

    plt.show()

#TODO verify docstring makes is similar to CNN
def prepare_datasets(test_size, validation_size):
    """
    Loads data and splits it into train, validation and test sets.
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
    X, y = load_data(DATASET_PATH)

    # create train, validation and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # create train/validation split
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    return X_train, X_validation, X_test, y_train, y_validation, y_test


def build_model(input_shape):
    """Generates RNN-LSTM model
    :param input_shape (tuple): Shape of input set
    :return model: RNN-LSTM model
    """

    # build network topology
    model = keras.Sequential()

    # 2 LSTM layers
    # return sequence to pass onto next layer
    model.add(keras.layers.LSTM(64, input_shape=input_shape, return_sequences=True))
    model.add(keras.layers.LSTM(64))

    # dense layer
    model.add(keras.layers.Dense(64, activation='relu'))

    # dropout layer (mitigate overfitting)
    model.add(keras.layers.Dropout(DROPOUT))

    # output layer
    model.add(keras.layers.Dense(NUMBER_OF_NOTES, activation='softmax'))

    return model


#TODO complete function and docstring
def predict(model, X, y):
    """
        Predict on data
            :param model:
            :param X:
            :param y:
            :return: predicted_note
            :return: predicted_index
        """
    pass


if __name__ == "__main__":

    # create training, validation and test sets
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)

    # Build LSTM
    input_shape = (X_train.shape[1], X_train.shape[2]) # 130, 13 [number of slices, mfcc coeffceints]
    model = build_model(input_shape)

    #TODO complete printing of model

    # print model
    # plot_model(model, to_file='CNN_Model_Files/Model.png')

    # compile model
    optimiser = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimiser,
                  loss=LOSS,
                  metrics=['accuracy'])

    model.summary()

    # train the model
    history = model.fit(X_train, y_train, validation_data=(X_validation, y_validation),
                        batch_size=BATCH_SIZE, epochs=EPOCHS)

    # plot accuracy/error for training and validation
    plot_history(history)

    # evaluate model on test set
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
    print('\nTest accuracy:', test_accuracy)

    # save model
    model.save(MODEL_PATH)
