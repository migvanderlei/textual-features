from sklearn.base import BaseEstimator
from numpy import np
import re


class TWTCountElongated(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF ELONGATED WORDS"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(
                re.findall(r"([a-zA-z])\1{2,}", doc)
            ))
        return np.array(list_count).reshape(-1, 1)
