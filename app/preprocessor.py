from sklearn.preprocessing import StandardScaler
from app.exceptions import preprocessorError

class preprocessor:
    def __init__(self):
        self.scaler=StandardScaler()
        
    def fit_transform(self,x):
        try:
            return self.scaler.fit_transform(x)
        except Exception as e:
            raise preprocessorError(str(e))