from sklearn.base import BaseEstimator
import numpy as np


class Negation(BaseEstimator):
    def __init__(self):
        self.name = "PRESENCE OF NEGATION WORDS"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            presence = 0
            for token in doc:
                if token.text in ['não', 'nao', 'nem', 'nunca', 'nn', 'n', 'ñ']:
                    presence = 1
                    break
            list_count.append(presence)
        return np.array(list_count).reshape(-1, 1)
