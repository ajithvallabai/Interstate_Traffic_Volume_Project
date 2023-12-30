import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from trafficVolumePrediction.entity.config_entity import EvaluationConfig
from trafficVolumePrediction.utils.common import save_json
from pathlib import Path
import tensorflow as tf

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        data = pd.read_csv(self.config.training_data)
        x = np.array(data[["holiday","temp","rain_1h","snow_1h","clouds_all","weather_main","weather_description","year","month","day","hour"]])
        y = np.array(data[["traffic_volume"]])
        self.xtrain, self.xval, self.ytrain, self.yval = train_test_split(x, y, 
                                                        test_size=0.20, 
                                                        random_state=33)

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(x=self.xval,
                        y=self.yval,
                        batch_size=self.config.params_batch_size,)

    
    def save_score(self):
        scores = {"loss": self.score}
        save_json(path=Path("scores.json"), data=scores)
