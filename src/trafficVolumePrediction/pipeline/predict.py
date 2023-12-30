import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        result = model.predict(features)
        return [{'traffic': str(result[0][0])}]


