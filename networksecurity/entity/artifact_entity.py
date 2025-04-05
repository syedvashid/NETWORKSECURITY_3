from dataclasses import dataclass
@dataclass
class DataIngestionArtifacts:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifacts:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifacts:
        transformed_object_file_path: str
        transformed_train_file_path: str
        transformed_test_file_path: str

@dataclass
class classificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float


@dataclass
class ModelTrainerArtifacts:
    trained_model_file_path:str
    tain_metric_artifact:classificationMetricArtifact
    test_metric_artifact:classificationMetricArtifact