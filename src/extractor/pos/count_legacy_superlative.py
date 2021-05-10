from sklearn.base import BaseEstimator
import numpy as np
# import spacy
from src.utils.paths import PATH_DIR
# import pt_core_news_sm
filename = PATH_DIR+'res/legacy/{}_superlative.txt'

datasets = {
    2281: 'computerbr',
    2000: 'reli',
    1049: 'tripadvisor',
    350: 'reli_original',
    840: 'hotel',
    2053: 'comp_twitter',
    2754: 'comp_buscape'
}

class CountSuperlatives(BaseEstimator):
    def __init__(self):
        self.name = "LEGACY SUPERLATIVES"

    def fit(self, x=None, y=None):
        return self
    
    def transform(self, sentences):
        tam = len(sentences)
        data_path = filename.format(datasets[tam]) 
        
        recovered = np.loadtxt(data_path)

        return np.array(recovered).reshape(-1, 1)
    
    # def legacy_extraction(self, raw_sentences, dataset):
    #     nlp = pt_core_news_sm.load()
    #     sentences = list(nlp.pipe(raw_sentences, n_threads=4))

    #     list_count = []
    #     for doc in sentences:
    #         list_count.append(len([token for token in doc if 'SUP' in token.tag_]))
    #     extracted = np.array(list_count).reshape(-1,1)
    #     np.savetxt(filename.format(dataset), extracted)
    #     return True
