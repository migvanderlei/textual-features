import re
from sklearn.base import BaseEstimator
import numpy as np
from pathlib import Path
from src.utils.paths import PATH_DIR

words_dir = PATH_DIR+'res/dictionaries/palavras.txt'


class CountDictionaryWords(BaseEstimator):
    def __init__(self):
        self.name = "COUNT DICTIONARY WORDS"
        self.file_name = words_dir
        self.lexicon = None

    def __load_lexicon__(self):
        with open(self.file_name, "r") as f:
            self.lexicon = set(f.read().split('\n'))
            

    def __value__(self, sentence):
        return len([term for term in sentence if term in self.lexicon])

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        self.__load_lexicon__()
        list_count = []
        for sentence in sentences:
            words = re.findall(r'[^\s!\?,\(\)\.]+', sentence.lower())
            word_count = self.__value__(words)
            list_count.append(word_count)
        return np.array(list_count).reshape(-1, 1)
