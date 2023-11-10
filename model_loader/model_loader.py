# creating a class to save and load models
import os
import joblib
from application_logger.setup_logger import setup_logger



class ModelLoader():
    """
    class for load and save models.
    and load model from local machine.
    """
    def __init__(self):
        self.log = setup_logger("modelloader_log", "logs/model_loader.log")
        self.model_path = "./models"


    def save_model(self, model, model_name):    
        """
        Method: save_model
        Description: save model to the model_folder.

        Input: model, model_name (string)
        Output: None

        On Error: raise errro, log error

        Version: 1.0
        """
        try:
            self.log.info("Saving model")
            if not os.path.exists(self.model_path): # check if the model_path exists
                os.makedirs(self.model_path)
            path = os.path.join(self.model_path, model_name) + ".pkl" # create a path to save the model
            joblib.dump(model, path)
            self.log.info("Model Saved")
        except Exception as e:
            self.log.error("Error in saving model " + str(e))
            raise e
    

    def load_model(self, model_name):
        """
        Method: load_model
        Description: load model from the model_path

        Input: model_path (string)
        Output: model (object)

        On Error: raise errro, log error

        Version: 1.0
        """
        try:
            self.log.info("Loading model")
            path = os.path.join(self.model_path, model_name) # create a path to load the model
            model = joblib.load(path) # load the model
            self.log.info("Model loaded")
            return model # return the model
        except Exception as e:
            self.log.error("Error in loading model " + str(e))
            raise e

    

    

