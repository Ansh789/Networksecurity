import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()
        model_artifact = training_pipeline.run_pipeline()
        print(model_artifact)
    except Exception as e:
        logging.exception(str(e))
        raise NetworkSecurityException(e, sys)
    
    
    
    
    
    
