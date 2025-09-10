from sklearn.linear_model import LogisticRegression
from app.exceptions import modelError
import pickle


class model:
    def __init__(self):
        self.ml_model=LogisticRegression()
        
        
    def save(self,path="model.pkl"):
        try:
            with open(path,"wb") as f:
                pickle.dump(self.ml_model,f)
        except Exception as e:
            raise modelError(str(e))
        
    def load(self,path="model.pkl"):
        try:
            with open(path,"rb") as f:
                self.ml_model=pickle.load(f)
        except Exception as e:
            raise modelError(str(e))