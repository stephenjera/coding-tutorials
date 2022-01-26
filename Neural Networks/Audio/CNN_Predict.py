"""
This code takes the DATASET_PATH path and MODEL_PATH to predict the
expected index, the model must be provided with the correct data.

"""

import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from CNN import load_data
from CNN import predict


DATASET_PATH = "Simulated_Dataset_Matlab.json"
MODEL_PATH = "CNN_model_Matlab.h5"


def prepare_data(dataset):
    # load dataset
    X, y = load_data(DATASET_PATH)
    print("initial shape of X = {}".format(X.shape))

    # CNN expects 3D array inputs are only 2D
    X = X[..., np.newaxis]  # 4D array -> [num_samples, number of time bins, mfcc_coefficients, channel]
    print("returned shape of X = {}".format(X.shape))
    print("returned shape of y = {}".format(y.shape))

    return X, y


if __name__ == "__main__":
    # load model
    model = load_model(MODEL_PATH)

    # summarize model.
    model.summary()

    # load data
    X, y = prepare_data(DATASET_PATH)

    # make prediction on a sample
    predicted_index = []
    for i in range(len(X)):
        predicted_index.append(predict(model, X[i], y[i]))

    # plot graph
    xaxis = []
    xaxis.extend(range(0, len(X)))
    plt.scatter(xaxis, predicted_index)
    plt.title("Predicted Note of Sample")
    plt.xlabel('Sample')
    plt.ylabel('Predicted Index')
    plt.show()



