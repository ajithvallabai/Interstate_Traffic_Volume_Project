from trafficVolumePrediction import logger
from trafficVolumePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from trafficVolumePrediction.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from trafficVolumePrediction.pipeline.stage_03_training import ModelTrainingPipeline
from trafficVolumePrediction.pipeline.stage_04_evaluation import EvaluationPipeline
from trafficVolumePrediction.pipeline.predict import PredictionPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(">>>>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>>>>> stage {STAGE_NAME} completed <<<<< \n =========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f"*************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f"*************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"*************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

import numpy as np
model = PredictionPipeline()
print(model.predict(np.array([[0,288.28,0.0,0.0,40,0,0,2012,10,2,9]])))