import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, features):
        self.features =features

    def predict(self):
        # load model C:\Users\MCW\Documents\Ajith\MLOps\project_02\Interstate_Traffic_Volume_Project\artifacts\prepare_base_model\base_model_updated.h5
        # model = load_model(os.path.join("artifacts","training", "model.h5"))
        # C:\Users\MCW\Documents\Ajith\MLOps\project_02\Interstate_Traffic_Volume_Project\artifacts\prepare_callbacks\checkpoint_dir\model.h5
        model = load_model(os.path.join("artifacts","prepare_callbacks", "checkpoint_dir", "model.h5"))
        result = model.predict(self.features)
        print(result)
        return [{'traffic': result}]


