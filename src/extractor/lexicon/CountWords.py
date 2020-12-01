import re
import numpy as np
from sklearn.base import BaseEstimator


class CountWords(BaseEstimator):
    def __init__(self):
        self.name = "WORDS"

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        tokenized_sentences = []
        for sentence in sentences:
            words = len(re.findall(r'[^\s!\?,\(\)\.]+', sentence))
            tokenized_sentences.append(words)
        return np.array(tokenized_sentences).reshape(-1, 1)
