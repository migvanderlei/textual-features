from sklearn.base import BaseEstimator
import numpy as np


class LEXQuotationExclamation(BaseEstimator):
    def __init__(self, proportion=False):
        self.name = "PROP" if proportion else "NUM" + "QUOTATION AND EXCLAMATION MARKS"
        self.proportion = proportion

    def __value__(self, sentence):
        if self.proportion:
            return len([term for term in sentence if term.text in ["!", "?"]]) / len(sentence)
        else:
            return len([term for term in sentence if term.text in ["!", "?"]])

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count).reshape(-1, 1)
