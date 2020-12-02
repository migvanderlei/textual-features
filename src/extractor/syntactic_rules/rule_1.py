from sklearn.base import BaseEstimator
import numpy as np


# ADJ -> NOUN -> *
class SyntacticRule1(BaseEstimator):
    def __init__(self):
        self.name = "RULE 1"

    def fit(self, x=None, y=None):
        return self

    def __pattern__(self, sentence):
        for i in range(len(sentence)):
            if i + 1 < len(sentence):
                if sentence[i].pos_ == "ADJ":
                    if sentence[i + 1].pos_ == "NOUN":
                        return 1
        return 0

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(self.__pattern__(doc))
        return np.array(list_count).reshape(-1, 1)
