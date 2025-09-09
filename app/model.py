from sklearn.linear_model import LogisticRegression

class model:
    def __init__(self):
        self.ml_model=LogisticRegression()
    def get_model(self):
        return self.ml_model