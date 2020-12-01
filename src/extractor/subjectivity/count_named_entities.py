from sklearn.base import BaseEstimator
import numpy as np


class CountNE(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF NAMED ENTITIES"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(doc.ents))
        return np.array(list_count).reshape(-1, 1)
