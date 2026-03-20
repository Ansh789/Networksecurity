from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

# create training pipeline config (this will create timestamped artifact dir)
training_config = TrainingPipelineConfig()

# create ingestion and validation configs
data_ingestion_cfg = DataIngestionConfig(training_config)
data_validation_cfg = DataValidationConfig(training_config)

# build artifact instances (simulate what pipeline components would return)
data_ingestion_artifact = DataIngestionArtifact(
    trained_file_path=data_ingestion_cfg.training_file_path,
    test_file_path=data_ingestion_cfg.testing_file_path,
)

data_validation_artifact = DataValidationArtifact(
    validation_status=None,
    valid_train_file_path=data_ingestion_cfg.training_file_path,
    valid_test_file_path=data_ingestion_cfg.testing_file_path,
    invalid_train_file_path=None,
    invalid_test_file_path=None,
    drift_report_file_path=data_validation_cfg.drift_report_file_path,
)

# print results similar to your expected output
print(training_config.pipeline_name)
print(training_config.artifact_dir)
print()
print(data_ingestion_artifact)
print()
print(data_validation_artifact)
print()
print('None')
