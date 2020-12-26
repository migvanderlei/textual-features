from src.utils import SpacySentenceTokenizer
from sklearn.base import BaseEstimator
import numpy as np


class SentencePosition(BaseEstimator):
    def __init__(self, relative=False):
        self.name = "RELATIVE" if relative else "ABSOLUTE" + " POSITION OF THE SENTENCE"
        self.relative = relative
        self.spacy_preprocessor = SpacySentenceTokenizer()

    def fit(self, x=None, y=None):
        return self

    def __get_position(self, sentences, sentence):
        pos = sentences.index(sentence)+1
        if self.relative:
            return pos/len(sentences)\
        else:
            return pos

    def transform(self, documents):
        list_count = []
        for document in documents:
            sentences = self.spacy_preprocessor.transform(document)
            for sentence in sentences:
                list_count.append(self.__get_position(sentences, sentence))
        return np.array(list_count).reshape(-1, 1)
