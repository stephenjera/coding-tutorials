import numpy as np
from tensorflow.keras.models import load_model
from CNN import load_data
from CNN import predict


DATASET_PATH = "simulated_data.json"
MODEL_PATH = "CNN_model.h5"


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
    predict(model, X[2], y[2])
