from housing.entity.config_entity import DataIngestionConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
import tarfile
import urllib

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys)
    
    def download_housing_data(self,):
        try:
            download_url =self.data_ingestion_config.tgz_download_dir
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)



    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e