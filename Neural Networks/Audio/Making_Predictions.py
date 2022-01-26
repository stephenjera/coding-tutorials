import numpy as np
from tensorflow.keras.models import load_model
from MLP_NN import load_data
from sklearn.model_selection import train_test_split


DATASET_PATH = "simulated_data.json"

# load model
model = load_model('MLP_SAVE.h5')

# summarize model.
model.summary()

inputs, targets = load_data(DATASET_PATH)


predictions = model.predict(x=inputs, batch_size=5, verbose=0)
rounded_predictions = np.argmax(predictions, axis=-1)

#print(inputs)
for i in rounded_predictions:
    print(i)

