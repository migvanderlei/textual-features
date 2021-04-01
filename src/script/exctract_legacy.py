import pandas as pd
from src.extractor.pos import CountComparatives
from src.extractor.pos import CountSuperlatives

from src.utils.paths import PATH_DIR
import csv
DATASET_PATH = PATH_DIR+"res/datasets/raw/{}_dataset.tsv"

def exctract_legacy(dataset):
    dataset_path = DATASET_PATH.format(dataset)
    print(dataset_path)
    data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
    raw_sentences = data['sentence']
    
    comp = CountComparatives()
    comp.legacy_extraction(raw_sentences, dataset)
    extracted_data = comp.transform(raw_sentences)
    print(extracted_data.shape)
    sup = CountSuperlatives()
    sup.legacy_extraction(raw_sentences, dataset)
    extracted_data = sup.transform(raw_sentences)
    print(extracted_data.shape)

if __name__ == "__main__":
    dataset='hotel'
    exctract_legacy(dataset)