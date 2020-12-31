from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
from pathlib import Path
from src.utils.paths import PATH_DIR

emoji_dir = PATH_DIR+'res/dictionaries/emoji_ranking.csv'


class EmojiPolarityScore(BaseEstimator):
    def __init__(self, scoring_type='polarity'):
        self.scoring_type = scoring_type
        self.name = "SUM OF " + scoring_type.upper() + " EMOJIS"
        self.file_name = emoji_dir
        self.emoji_data = None

    def __get_emojis__(self, sentence):
        pass

    def __load_lexicon__(self):
        with open(self.file_name, "r") as f:
            self.emoji_data = pd.read_csv(self.file_name, index_col='char').to_dict('index')

    def __value__(self, sentence):
        score = 0
        for term in sentence:
            if term.text in self.emoji_data:
                score += self.emoji_data[term.text][self.scoring_type]
        return score

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        self.__load_lexicon__()
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count).reshape(-1, 1)
