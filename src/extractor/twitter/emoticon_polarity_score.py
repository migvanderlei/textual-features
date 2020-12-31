from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
from pathlib import Path
from src.utils.paths import PATH_DIR

emoticon_dir = PATH_DIR+'res/dictionaries/emoticon_sentiment_lexicon.tsv'


class EmoticonPolarityScore(BaseEstimator):
    def __init__(self):
        self.name = "SUM OF EMOTICON SCORE"
        self.file_name = emoticon_dir
        self.emoticon_data = None

    def __get_emojis__(self, sentence):
        pass

    def __load_lexicon__(self):
        with open(self.file_name, "r") as f:
            self.emoticon_data = pd.read_csv(self.file_name, sep='\t', index_col='emoticon').to_dict('index')

    def __value__(self, sentence):
        score = 0
        for term in sentence:
            if term.text in self.emoticon_data:
                score += self.emoticon_data[term.text]['sentiment']
        return score

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        self.__load_lexicon__()
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count).reshape(-1, 1)
