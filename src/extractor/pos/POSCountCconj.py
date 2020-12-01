from sklearn.base import BaseEstimator
import numpy as np


class POSCountCconj(BaseEstimator):
    def __init__(self):
        self.name = "CCONJ"

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len([token for token in doc if token.pos_ == 'CCONJ']))
        return np.array(list_count).reshape(-1, 1)
