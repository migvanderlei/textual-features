from sklearn.base import BaseEstimator
import numpy as np


# ADV + [<SUP> | <COMP>] -> VERB + [ PCP | GER | PS | IMPF]  -> *
class SyntacticRule5(BaseEstimator):
    def __init__(self):
        self.name = "RULE 5"

    def fit(self, x=None, y=None):
        return self

    def __pattern__(self, sentence):
        for i in range(len(sentence)):
            if i + 1 < len(sentence):
                if sentence[i].pos_ == "ADV" or (sentence[i].pos_ == "ADV" and "<SUP>" in sentence[i].tag_) or (
                        sentence[i].pos_ == "ADV" and "<COMP>" in sentence[i].tag_):
                    if sentence[i + 1].pos_ == "VERB" or (
                            sentence[i].pos_ == "VERB" and "<PCP>" in sentence[i].tag_) or (
                            sentence[i].pos_ == "VERB" and "<GER>" in sentence[i].tag_) or (
                            sentence[i].pos_ == "VERB" and "<PS>" in sentence[i].tag_) or (
                            sentence[i].pos_ == "VERB" and "<IMPF>" in sentence[i].tag_):
                        return 1
        return 0

    def transform(self, sentences):
        list_count = []
        for doc in sentences:
            list_count.append(self.__pattern__(doc))
        return np.array(list_count).reshape(-1, 1)
