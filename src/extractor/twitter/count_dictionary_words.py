from sklearn.base import BaseEstimator
import numpy as np

words_dir = '../../../res/dictionaries/'


class CountDictionaryWords(BaseEstimator):
    def __init__(self):
        self.name = "COUNT DICTIONARY WORDS"
        self.file_name = words_dir + "palavras.txt"
        self.lexicon = []

    def __load_lexicon__(self):
        with open(self.file_name, "r") as f:
            self.lexicon = f.read().split('\n')

    def __value__(self, sentence):
        return len([term for term in sentence if term.text in self.lexicon])

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        self.__load_lexicon__()
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count)
