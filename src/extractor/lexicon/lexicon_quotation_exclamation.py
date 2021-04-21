from src.extractor.twitter import proportion_capitalized_words
from sklearn.base import BaseEstimator
import numpy as np


class LexiconQuotationExclamation(BaseEstimator):
    def __init__(self, proportion=False):
        self.name = "PROP" if proportion else "NUM" + "QUOTATION AND EXCLAMATION MARKS"
        self.proportion = proportion

    def __value__(self, sentence):
        if self.proportion:
            return sum([(term.text.count("!") + term.text.count("?")) for term in sentence]) / len(sentence)
        else:
            return sum([(term.text.count("!") + term.text.count("?")) for term in sentence])

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for sentence in sentences:
            value = self.__value__(sentence)
            list_count.append(value)
            if not self.proportion:
                print(value, sentence)
        return np.array(list_count).reshape(-1, 1)
