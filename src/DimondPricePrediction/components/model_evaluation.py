import os
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import dagshub
import numpy as np
import pickle
from src.DimondPricePrediction.utils.utils import load_object
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import warnings
warnings.filterwarnings("ignore", message="Setuptools is replacing distutils")





class ModelEvaluation:
    def __init__(self):
        logging.info("Evaluation Started")
        # Initialize DAGsHub
        dagshub.init(repo_owner='utkarsh9911', repo_name='Gemstone-Price-Pridictor-using-DAgshub-and-MLOPS', mlflow=True)

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        logging.info("Evaluation metrics captured")
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
             
             X_test,y_test=(test_array[:,:-1], test_array[:,-1])

             model_path=os.path.join("artifacts","model.pkl")
             model=load_object(model_path)

             #mlflow.set_registry_uri("")
             
             logging.info("model has register")

             tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

             print(tracking_url_type_store)



             with mlflow.start_run():

                prediction=model.predict(X_test)

                (rmse,mae,r2)=self.eval_metrics(y_test,prediction)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                 # Model registry does not work with file store
                if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")


        except Exception as e:

            raise customexception(e,sys)




        
      