from sklearn.base import BaseEstimator
import numpy as np
import re


class CountMentions(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF MENTIONS (@user)"

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(re.findall(r"@[a-zA-Z0-9_]{,15}\b", doc)))
        return np.array(list_count).reshape(-1, 1)
