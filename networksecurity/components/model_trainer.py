import sys
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.entity.artifact_entity import (
    ModelTrainerArtifact,
    DataTransformationArtifact,
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import (
    load_numpy_array_data,
    save_object,
)


class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact, model_trainer_config: ModelTrainerConfig):
        try:
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Starting model training")

            # load transformed numpy arrays
            train_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_test_file_path)

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]
            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            # simple classifier
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            # evaluate
            preds = model.predict(X_test)
            acc = float(accuracy_score(y_test, preds))
            logging.info(f"Model accuracy: {acc}")

            # ensure directory and save model
            model_path = self.model_trainer_config.trained_model_file_path
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            save_object(model_path, model)

            artifact = ModelTrainerArtifact(
                trained_model_file_path=model_path,
                is_trained=True,
                accuracy=acc,
            )

            return artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
