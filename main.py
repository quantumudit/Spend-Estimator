"""
This module is responsible for executing the data pipeline stages which include
Data Ingestion, Data Validation, Data Preparation, Data Transformation, Model Trainer,
Model Evaluation. Each stage is encapsulated in its own class and has a main method
that executes the tasks for that stage. If any exceptions occur during the
execution of a stage, they are logged and re-raised as a CustomException.
"""
from src.exception import CustomException
from src.logger import logger
from src.pipelines.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>> %s started <<<<<<", STAGE_NAME)
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.error(CustomException(e))
    raise CustomException(e) from e
