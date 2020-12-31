from sklearn.base import BaseEstimator
import numpy as np
from pathlib import Path
from src.utils.paths import PATH_DIR


liwc_dir = PATH_DIR+'res/liwc_pt/LIWC_Portuguese_negative.txt'


class LexiconNegative(BaseEstimator):
    def __init__(self, proportion=False):
        self.name = "PROP" if proportion else "NUM" + "NEGATIVE WORDS"
        self.file_name = liwc_dir
        self.lexicon = []
        self.proportion = proportion

    def __load_lexicon__(self):
        with open(self.file_name, "r") as f:
            self.lexicon = f.read().split('\n')

    def __value__(self, sentence):
        if self.proportion:
            return len([term for term in sentence if term.text in self.lexicon]) / len(sentence)
        else:
            return len([term for term in sentence if term.text in self.lexicon])

    def fit(self, X=None, y=None):
        return self

    def transform(self, sentences):
        self.__load_lexicon__()
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count)
