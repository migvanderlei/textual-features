from senticnet.senticnet import SenticNet
from sklearn.base import BaseEstimator
import numpy as np


class SensitivityScore(BaseEstimator):
    def __init__(self, absolute=False, average=False):
        self.name = "AVERAGE" if average else "SUM" + " OF SENSITIVITY SCORES" + (" (ABS)" if absolute else "")
        self.sn = SenticNet('pt')
        self.abs = absolute
        self.avg = average

    def __value__(self, sentence):
        total = 0
        for word in sentence:
            try:
                if self.abs:
                    score = abs(self.sn.sentics(word.text.lower())['sensitivity'])
                else:
                    score = self.sn.sentics(word.text.lower())['sensitivity']
                total += score
            except KeyError:
                pass
        if self.avg:
            return total / len(sentence)
        else:
            return total

    def fit(self, x=None, y=None):
        return self

    def transform(self, sentences):
        list_count = []
        for sentence in sentences:
            list_count.append(self.__value__(sentence))
        return np.array(list_count).reshape(-1, 1)
