from sklearn.base import BaseEstimator
import numpy as np
import re


class ProportionCapitalizedWords(BaseEstimator):
    def __init__(self):
        self.name = "PROPORTION OF CAPITALIZED WORDS"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            word_count = len(re.findall(r'[^\s!\?,\(\)\.]+', doc))
            capitalized_count = len(re.findall(r'[A-Z]\w+', doc))
            list_count.append(0 if capitalized_count == 0 else capitalized_count/word_count)
        return np.array(list_count).reshape(-1, 1)
