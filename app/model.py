from sklearn.linear_model import LogisticRegression
from app.exceptions import modelError


class model:
    def __init__(self):
        self.ml_model=LogisticRegression()
    def get_model(self):
        try:
            return self.ml_model
        except Exception as e:
            raise modelError(str(e))