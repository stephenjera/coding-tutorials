"""
This code takes the DATASET_PATH path and MODEL_PATH to predict the
expected index, the model must be provided with the correct data.

"""

# TODO calculate confusion matrix metrics

import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from CNN import load_data
from CNN import predict


DATASET_PATH = "Dataset_JSON_Files/Simulated_Dataset_Matlab_Two_Seg.json"  # data used for predictions
MODEL_PATH = "CNN_Model_Files/CNN_Model_Matlab_Test_2.h5"


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
    predicted_note = []
    predicted_index = []
    for i in range(len(X)):
        note, index = predict(model, X[i], y[i])
        predicted_note.append(note)
        predicted_index.append(index)
    # https://stackoverflow.com/questions/40729875/calculate-precision-and-recall-in-a-confusion-matrix
    conf = confusion_matrix(y, predicted_index)
    sns.heatmap(conf, annot=True)

    # plot graph
    xaxis = []
    xaxis.extend(range(0, len(X)))
    plt.scatter(xaxis, predicted_note)
    plt.title("Predicted Note of OnlyA4Recorded using CNN_Model_Matlab_Test")
    plt.xlabel('Sample')
    plt.ylabel('Predicted Note')
    plt.show()



