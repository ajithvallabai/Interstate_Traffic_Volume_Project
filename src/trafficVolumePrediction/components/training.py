import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from trafficVolumePrediction.entity.config_entity import TrainingConfig
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_generator(self):
        # Todo: Make below one genric and remove train test split
        #  (x_val, y_val)
        data = pd.read_csv(self.config.training_data)
        x = np.array(data[["holiday","temp","rain_1h","snow_1h","clouds_all","weather_main","weather_description","year","month","day","hour"]])
        y = np.array(data[["traffic_volume"]])
        self.xtrain, self.xval, self.ytrain, self.yval = train_test_split(x, y, 
                                                        test_size=0.20, 
                                                        random_state=33)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_per_epoch = len(self.xtrain) // self.config.params_batch_size
        self.validation_steps = len(self.xval)  // self.config.params_batch_size
        self.model.fit(
            self.xtrain,
            self.ytrain,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=(self.xval, self.yval),
            # validation_split=0.20,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )