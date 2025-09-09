from sklearn.datasets import load_iris
from app.exceptions import dataLoaderError

class DataLoader:
    def load_raw_data(self):
        try:
            iris=load_iris()
            return iris.data,iris.target
        except Exception as e:
            raise dataLoaderError(str(e))