from sklearn.base import BaseEstimator
import numpy as np


class CountAdj(BaseEstimator):
    def __init__(self):
        self.name = "ADJ"

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(len([token for token in doc if token.pos_ == 'ADJ']))
            for token in doc:
                if 'Cmp' in token.tag_ or 'Sup' in token.tag_ or 'Degree=' in token.tag_:
                    print(token.pos_, token.tag_)
        return np.array(list_count).reshape(-1, 1)
