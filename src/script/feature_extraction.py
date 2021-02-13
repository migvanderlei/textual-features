from sklearn.pipeline import FeatureUnion, Pipeline
from pathlib import Path
import pandas as pd
from src.utils.features_list import ALL_FEATURES
from src.utils.features_list import RAW_TEXT_FEATURES
from src.utils.spacy_preprocessor import SpacyPreprocessor
from src.utils.csv_generator import generate_file
from src.utils.paths import PATH_DIR
import csv

DATASET_PATH = PATH_DIR+'res/datasets/raw/{}_dataset.tsv'

RAW_TEXT_FEATURES_NAMES = [feature[0] for feature in RAW_TEXT_FEATURES]
SPACY_FEATURES = [feature for feature in ALL_FEATURES if feature[0] not in RAW_TEXT_FEATURES_NAMES]


def feature_extraction(dataset_name):
    try:
        dataset_path = DATASET_PATH.format(dataset_name)

        data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
        raw_sentences = data['sentence']
        spacy_union = FeatureUnion(transformer_list=SPACY_FEATURES)

        pipeline = Pipeline(steps=[
            ('features', FeatureUnion(
                transformer_list=RAW_TEXT_FEATURES + [('spacy', Pipeline(steps=[
                        ('spacy_preprocessor', SpacyPreprocessor()),
                        ('spacy_features', spacy_union)
                    ]))],
            ))
        ])

        features = pipeline.fit_transform(raw_sentences)

        generate_file(features, RAW_TEXT_FEATURES+SPACY_FEATURES, dataset_name)
    except FileNotFoundError:
        print("Path do arquivo não econtrado: {}".format(dataset_path))
    except Exception as err:
        print(err)