import os 
import sys 
import pandas as pd
import numpy as np
"""
defining the common constant variable for traning pipeline 
"""
TARGET_COLUMN ="Result"
PIPELINE_NAME : str = "networksecurity"
ARTIFACTS_DIR : str = "Artifacts"
FILE_NAME : str = "NetworkData.csv"

TRAIN_FILE_NAME :str ="train.csv"
TEST_FILE_NAME :str ="test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")



"""
Data Ingestion related constant start here with DATA_INGESTION VAR NAME 

"""
DATA_INGESTION_COLLECTION_NAME = "NetworkData"
DATA_INGESTION_DATABASE_NAME : str = "akshan09061999"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTION_DIR: str = "ingested"
DATA_INGESTION_TRAIN_SPLIT_RATION: float = 0.2


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME 
"""

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"
