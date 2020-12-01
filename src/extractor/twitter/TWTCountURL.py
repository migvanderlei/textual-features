from sklearn.base import BaseEstimator
from numpy import np
import re


class TWT_CountURL(BaseEstimator):
    def __init__(self):
        self.name = "COUNT OF URLS"
        self.regex = r"((https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len(re.findall(self.regex, doc)))
        return np.array(list_count).reshape(-1, 1)
