from sklearn.base import BaseEstimator
from numpy import np
import re


class TWTCountMentions(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF MENTIONS (@user)"

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(re.findall(r"@[a-zA-Z0-9_]{,15}\b", doc)))
        return np.array(list_count).reshape(-1, 1)
