import os 
import urllib.request as request
import zipfile
from trafficVolumePrediction import logger
from trafficVolumePrediction.utils.common import get_size
from trafficVolumePrediction.entity.config_entity import DataIngestionConfig
import time

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        delay = 5
        max_retries = 3
        for _ in range(max_retries):
            try:
                if not os.path.exists(self.config.local_data_file):
                    filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                    )
                    logger.info(f"{filename} download! with following info: \n {headers}")
                else:
                    logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            except Exception as e:
                logger.info(f"Delay for next attempt {e}")
                time.sleep(delay)
                delay *= 2
        else:
            logger.info(f"Failed for {self.config.source_URL} after {max_retries} attempt")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)