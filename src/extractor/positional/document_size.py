from src.utils import SpacySentenceTokenizer
from sklearn.base import BaseEstimator
import numpy as np


class DocumentSize(BaseEstimator):
    def __init__(self):
        self.name = "SIZE OF THE DOCUMENT CONTAINING THE SENTENCE"
        self.spacy_preprocessor = SpacySentenceTokenizer()

    def fit(self, x=None, y=None):
        return self

    def transform(self, documents):
        list_count = []
        for document in documents:
            sentences = self.spacy_preprocessor.transform(document)
            for sentence in sentences:
                list_count.append(len(document))
        return np.array(list_count).reshape(-1, 1)
