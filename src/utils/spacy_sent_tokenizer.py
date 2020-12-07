import pt_core_news_lg
from sklearn.base import BaseEstimator


class SpacySentenceTokenizer(BaseEstimator):

    def __init__(self):
        self.nlp = pt_core_news_lg.load()

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        return list(self.nlp(sentences).sents)
