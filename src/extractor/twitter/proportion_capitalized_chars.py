from sklearn.base import BaseEstimator
import numpy as np
import re


class ProportionCapitalizedChars(BaseEstimator):
    def __init__(self):
        self.name = "PROPORTION OF CAPITALIZED CHARACTERS"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            words = re.findall(r'([A-Z])', doc)
            list_count.append(0 if len(words) == 0 else len(words) / len(doc))
        return np.array(list_count).reshape(-1, 1)