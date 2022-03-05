"""
This code takes the DATASET_PATH path and MODEL_PATH to predict the
expected index, the model must be provided with the correct data.

"""

# TODO calculate confusion matrix metrics

import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, \
    precision_score, recall_score, f1_score, classification_report
import seaborn as sns
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from CNN import load_data
from CNN import predict


DATASET_PATH = "Dataset_JSON_Files/Only_A4_Recorded_Trimmed3.json"  # data used for predictions
MODEL_PATH = "CNN_Model_Files/CNN_Model_Matlab_Hybrid3.h5"


def prepare_data(dataset):
    # load dataset
    X, y = load_data(dataset)
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

    #print(y)
    print(predicted_index)
    cm = confusion_matrix(y, predicted_index)
    # tn, fp, fn, tp = confusion_matrix(y, predicted_index).ravel()
    # print("tn: {} fp: {} fn: {} tp: {}".format(tn, fp, fn, tp))

    # calculate metrics
    report = classification_report(y, predicted_index, zero_division=0)
    accuracy = accuracy_score(y, predicted_index)
    precision_macro = precision_score(y, predicted_index, average="macro")
    precision_micro = precision_score(y, predicted_index, average="micro")
    recall_macro = recall_score(y, predicted_index, average="macro")
    recall_micro = recall_score(y, predicted_index, average="micro")
    f1_score_macro = f1_score(y, predicted_index, average="macro")
    f1_score_micro = f1_score(y, predicted_index, average="micro")

    # calculate metrics from confusion matrix
    true_pos = np.diag(cm) # true positives are the diagonal of cm
    false_pos = np.sum(cm, axis=0) - true_pos
    false_neg = np.sum(cm, axis=1) - true_pos


    # python return 0 divide by 0 as NAN
    #precision = np.sum(np.nan_to_num(true_pos / (true_pos + false_pos)))
    #recall = np.sum(np.nan_to_num(true_pos / (true_pos + false_neg)))
    #specificity = np.sum(np.nan_to_num(true_neg / (true_neg + false_pos)))
    print("Accuracy: ", accuracy)
    print("Precsion macro: ", precision_macro)
    print("Precsion micro: ", precision_micro)
    print("Recall macro: ", recall_macro)
    print("Recall micro: ", recall_micro)
    print("F1 score macro: ", f1_score_macro)
    print("F1 score micro: ", f1_score_micro)
    print(report)


    #print("Specificity: ", specificity)


    # plot confusion matrix
    sns.heatmap(cm, annot=True)
    plt.title("Confusion matrix")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()



    # plot graph
    xaxis = []
    xaxis.extend(range(0, len(X)))
    plt.scatter(xaxis, predicted_note)
    plt.title("Predicted Note of OnlyA4Recorded using CNN_Model_Matlab_Test")
    plt.xlabel('Sample')
    plt.ylabel('Predicted Note')
    plt.show()



