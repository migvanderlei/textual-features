from sklearn.pipeline import FeatureUnion, Pipeline
from pathlib import Path
import pandas as pd
from src.utils.spacy_preprocessor import SpacyPreprocessor
from src.utils.features_list import POS_FEATURES_LIST
from src.utils.csv_generator import generate_file

DATASET_PATH = '../../res/datasets/{}_dataset.tsv'


def feature_extraction(dataset_name):
    dataset_path = Path(DATASET_PATH.format(dataset_name)).resolve()

    data = pd.read_csv(dataset_path, sep='\t')
    sentences = SpacyPreprocessor().transform(data['sentence'])

    union = FeatureUnion(transformer_list=POS_FEATURES_LIST)

    features = union.fit_transform(sentences)

    print(features)
    generate_file(features, POS_FEATURES_LIST, 'teste')



feature_extraction("teste")
