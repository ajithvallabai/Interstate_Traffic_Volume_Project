import tensorflow as tf
from pathlib import Path
from trafficVolumePrediction.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        train_model = tf.keras.Sequential()
        train_model.add(tf.keras.layers.LSTM(128, activation='relu', return_sequences=True, input_shape= (self.config.params_features, 1)))
        train_model.add(tf.keras.layers.LSTM(64, activation='relu'))
        train_model.add(tf.keras.layers.Dense(25))
        self.model = train_model

        self.save_model(path=self.config.base_model_path, model=self.model)
    
    @staticmethod
    def _prepare_full_model(model, learning_rate):

        prediction = tf.keras.layers.Dense(1)(model.output)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer='adam', loss='mean_squared_error'
        )

        full_model.summary()
        return full_model
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)