from sklearn.base import BaseEstimator
import numpy as np


class FutureTense(BaseEstimator):
    def __init__(self):
        self.name = "PRESENCE OF FUTURE TENSE VERBS IN THE SENTENCE"

    def fit(self, X=None, y=None):
        return self

    def __is_future(self, tag):
        return 'Tense=Fut' in tag.split('|')

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            presence = 0
            for token in doc:
                if (token.pos_ == 'VERB' or token.pos_ == 'AUX') and self.__is_future(token.tag_):
                    presence = 1
                    break
            list_count.append(presence)
        return np.array(list_count).reshape(-1, 1)
