from sklearn.base import BaseEstimator
import spacy


class SpacySentenceTokenizer(BaseEstimator):

    def __init__(self):
        self.nlp = spacy.load('pt_core_news_lg')
        
    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        return list(self.nlp(sentences).sents)
