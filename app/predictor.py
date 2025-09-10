from app.model import model
from app.preprocessor import preprocessor
from app.exceptions import predictorError,preprocessorError,modelError
class predictor:
    def __init__(self,path="model.pkl"):
        self.model=model()
        self.model.load(path)
        self.preprocessor=preprocessor()

    def predict(self,features):
        try:
            scaled_features=self.preprocessor.fit_transform([features])
            prediction=self.model.ml_model.predict(scaled_features)
            return int(prediction)
        except Exception as e:
            raise predictorError(str(e))
        except preprocessorError as e:
            raise preprocessorError(str(e))
        except modelError as e:
            raise modelError(str(e))
    