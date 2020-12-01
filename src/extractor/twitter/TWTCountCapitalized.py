from sklearn.base import BaseEstimator
from numpy import np
import re


class TWTCountCapitalized(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF CAPITALIZED WORDS"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(re.findall(r'(\b[A-Z]{2,}\b)', doc)))
        return np.array(list_count).reshape(-1, 1)
