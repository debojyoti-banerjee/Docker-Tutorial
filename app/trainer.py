from app.data_loader import DataLoader
from app.preprocessor import preprocessor
from app.model import model
from app.exceptions import dataLoaderError,preprocessorError,modelError,trainerError

class trainer:
    def __init__(self):
        self.model=model()
        self.preprocessor=preprocessor()
        
    def train_and_save(self,path="model.pkl"):
        try:
            loader=DataLoader()
            x,y=loader.load_raw_data()
            x_scaled=self.preprocessor.fit_transform(x)
            self.model.ml_model.fit(x_scaled,y)
            self.model.save()
        except dataLoaderError as e:
            raise dataLoaderError(str(e))            
        except preprocessorError as e:
            raise preprocessorError(str(e))            
        except modelError as e:
            raise modelError(str(e))            
        except Exception as e:
            raise trainerError(str(e))        